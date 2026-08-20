from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from enum import Enum
from typing import Mapping

from .errors import InvalidTransition, InvariantViolation
from .ids import IdKind, parse_id


class PrivacyClass(str, Enum):
    PUBLIC = "PUBLIC"
    FAMILY = "FAMILY"
    RESTRICTED = "RESTRICTED"
    VAULT = "VAULT"


class MembershipClass(str, Enum):
    LINEAL_DESCENDANT = "LINEAL_DESCENDANT"
    BIOLOGICAL_RELATIVE = "BIOLOGICAL_RELATIVE"
    ADOPTED_RELATIVE = "ADOPTED_RELATIVE"
    SPOUSE = "SPOUSE"
    LEGAL_RELATION = "LEGAL_RELATION"
    GUARDIAN_DEPENDENT = "GUARDIAN_DEPENDENT"
    AFFILIATED_MEMBER = "AFFILIATED_MEMBER"
    TRUSTED_CONTRIBUTOR = "TRUSTED_CONTRIBUTOR"


class IdentityStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    SUSPENDED = "SUSPENDED"
    SEPARATED = "SEPARATED"
    DECEASED = "DECEASED"
    ARCHIVED = "ARCHIVED"


_IDENTITY_TRANSITIONS = {
    IdentityStatus.ACTIVE: {IdentityStatus.INACTIVE, IdentityStatus.SUSPENDED, IdentityStatus.SEPARATED, IdentityStatus.DECEASED},
    IdentityStatus.INACTIVE: {IdentityStatus.ACTIVE, IdentityStatus.SUSPENDED, IdentityStatus.SEPARATED, IdentityStatus.DECEASED},
    IdentityStatus.SUSPENDED: {IdentityStatus.ACTIVE, IdentityStatus.INACTIVE, IdentityStatus.SEPARATED, IdentityStatus.DECEASED},
    IdentityStatus.SEPARATED: {IdentityStatus.ACTIVE, IdentityStatus.DECEASED, IdentityStatus.ARCHIVED},
    IdentityStatus.DECEASED: {IdentityStatus.ARCHIVED},
    IdentityStatus.ARCHIVED: set(),
}


class RelationshipType(str, Enum):
    PARENT_OF = "PARENT_OF"
    CHILD_OF = "CHILD_OF"
    SPOUSE_OF = "SPOUSE_OF"
    SIBLING_OF = "SIBLING_OF"
    GUARDIAN_OF = "GUARDIAN_OF"
    DEPENDENT_OF = "DEPENDENT_OF"
    RELATED_TO = "RELATED_TO"


class RelationshipStatus(str, Enum):
    ASSERTED = "ASSERTED"
    VERIFIED = "VERIFIED"
    DISPUTED = "DISPUTED"
    SUPERSEDED = "SUPERSEDED"


class EnterpriseKind(str, Enum):
    FAMILY_OWNED = "FAMILY_OWNED"
    FAMILY_CONTROLLED = "FAMILY_CONTROLLED"
    FAMILY_AFFILIATED = "FAMILY_AFFILIATED"


class ContributionType(str, Enum):
    LABOR = "LABOR"
    CAPITAL = "CAPITAL"
    INTELLECTUAL_PROPERTY = "INTELLECTUAL_PROPERTY"
    ENTERPRISE_CREATION = "ENTERPRISE_CREATION"
    REVENUE_CREATION = "REVENUE_CREATION"
    MENTORSHIP = "MENTORSHIP"
    CAREGIVING = "CAREGIVING"
    LEADERSHIP = "LEADERSHIP"
    EDUCATION = "EDUCATION"
    PROPERTY = "PROPERTY"
    OPPORTUNITY_CREATION = "OPPORTUNITY_CREATION"
    RISK_BEARING = "RISK_BEARING"


class AgreementStatus(str, Enum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    TERMINATED = "TERMINATED"
    SUPERSEDED = "SUPERSEDED"


@dataclass(frozen=True, slots=True)
class Network:
    network_id: str
    name: str
    namespace: str
    privacy: PrivacyClass = PrivacyClass.FAMILY

    def __post_init__(self) -> None:
        parsed = parse_id(self.network_id, IdKind.NETWORK)
        if parsed.namespace != self.namespace:
            raise InvariantViolation("network id namespace must equal network namespace")
        if not self.name.strip():
            raise InvariantViolation("network name cannot be empty")


@dataclass(frozen=True, slots=True)
class Identity:
    identity_id: str
    network_id: str
    display_name: str
    membership_class: MembershipClass
    status: IdentityStatus = IdentityStatus.ACTIVE
    guardian_ids: tuple[str, ...] = ()
    privacy: PrivacyClass = PrivacyClass.FAMILY

    def __post_init__(self) -> None:
        parse_id(self.identity_id, IdKind.IDENTITY)
        parse_id(self.network_id, IdKind.NETWORK)
        if not self.display_name.strip():
            raise InvariantViolation("display name cannot be empty")
        if self.identity_id in self.guardian_ids:
            raise InvariantViolation("identity cannot be its own guardian")
        for guardian_id in self.guardian_ids:
            parse_id(guardian_id, IdKind.IDENTITY)

    def transition(self, new_status: IdentityStatus) -> "Identity":
        if new_status == self.status:
            return self
        if new_status not in _IDENTITY_TRANSITIONS[self.status]:
            raise InvalidTransition(f"identity cannot transition from {self.status.value} to {new_status.value}")
        return replace(self, status=new_status)


@dataclass(frozen=True, slots=True)
class Relationship:
    relationship_id: str
    network_id: str
    subject_id: str
    object_id: str
    relationship_type: RelationshipType
    status: RelationshipStatus = RelationshipStatus.ASSERTED
    supersedes_relationship_id: str | None = None
    privacy: PrivacyClass = PrivacyClass.FAMILY

    def __post_init__(self) -> None:
        parse_id(self.relationship_id, IdKind.RELATIONSHIP)
        parse_id(self.network_id, IdKind.NETWORK)
        parse_id(self.subject_id, IdKind.IDENTITY)
        parse_id(self.object_id, IdKind.IDENTITY)
        if self.subject_id == self.object_id:
            raise InvariantViolation("self-relationships are not valid")
        if self.supersedes_relationship_id:
            parse_id(self.supersedes_relationship_id, IdKind.RELATIONSHIP)


@dataclass(frozen=True, slots=True)
class Enterprise:
    enterprise_id: str
    network_id: str
    name: str
    kind: EnterpriseKind
    jurisdiction: str | None = None
    privacy: PrivacyClass = PrivacyClass.FAMILY

    def __post_init__(self) -> None:
        parse_id(self.enterprise_id, IdKind.ENTERPRISE)
        parse_id(self.network_id, IdKind.NETWORK)
        if not self.name.strip():
            raise InvariantViolation("enterprise name cannot be empty")


@dataclass(frozen=True, slots=True)
class Contribution:
    contribution_id: str
    network_id: str
    contributor_id: str
    recipient_id: str
    contribution_type: ContributionType
    description: str
    evidence_refs: tuple[str, ...] = ()
    valuation_minor_units: int | None = None
    valuation_currency: str | None = None
    privacy: PrivacyClass = PrivacyClass.FAMILY

    def __post_init__(self) -> None:
        parse_id(self.contribution_id, IdKind.CONTRIBUTION)
        parse_id(self.network_id, IdKind.NETWORK)
        parse_id(self.contributor_id, IdKind.IDENTITY)
        if parse_id(self.recipient_id).kind not in {IdKind.IDENTITY, IdKind.ENTERPRISE}:
            raise InvariantViolation("contribution recipient must be an identity or enterprise")
        if not self.description.strip():
            raise InvariantViolation("contribution description cannot be empty")
        if self.valuation_minor_units is not None and self.valuation_minor_units < 0:
            raise InvariantViolation("valuation cannot be negative")
        if (self.valuation_minor_units is None) != (self.valuation_currency is None):
            raise InvariantViolation("valuation amount and currency must either both be set or both be absent")
        if self.valuation_currency and (len(self.valuation_currency) != 3 or not self.valuation_currency.isupper()):
            raise InvariantViolation("valuation currency must be a 3-letter uppercase code")


@dataclass(frozen=True, slots=True)
class Agreement:
    agreement_id: str
    network_id: str
    party_ids: tuple[str, ...]
    agreement_type: str
    document_hash: str
    status: AgreementStatus = AgreementStatus.DRAFT
    privacy: PrivacyClass = PrivacyClass.RESTRICTED

    def __post_init__(self) -> None:
        parse_id(self.agreement_id, IdKind.AGREEMENT)
        parse_id(self.network_id, IdKind.NETWORK)
        if len(set(self.party_ids)) < 2:
            raise InvariantViolation("agreement requires at least two distinct parties")
        for party_id in self.party_ids:
            if parse_id(party_id).kind not in {IdKind.IDENTITY, IdKind.ENTERPRISE}:
                raise InvariantViolation("agreement party must be an identity or enterprise")
        if not self.agreement_type.strip():
            raise InvariantViolation("agreement type cannot be empty")
        if len(self.document_hash) != 64 or any(c not in "0123456789abcdef" for c in self.document_hash):
            raise InvariantViolation("document_hash must be a lowercase SHA-256 hex digest")


@dataclass(frozen=True, slots=True)
class Attestation:
    attestation_id: str
    network_id: str
    issuer_id: str
    subject_id: str
    claim_type: str
    claim: Mapping[str, object] = field(default_factory=dict)
    evidence_refs: tuple[str, ...] = ()
    issued_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    privacy: PrivacyClass = PrivacyClass.FAMILY

    def __post_init__(self) -> None:
        parse_id(self.attestation_id, IdKind.ATTESTATION)
        parse_id(self.network_id, IdKind.NETWORK)
        if parse_id(self.issuer_id).kind not in {IdKind.IDENTITY, IdKind.ENTERPRISE}:
            raise InvariantViolation("attestation issuer must be an identity or enterprise")
        if parse_id(self.subject_id).kind not in {IdKind.IDENTITY, IdKind.RELATIONSHIP, IdKind.ENTERPRISE, IdKind.CONTRIBUTION, IdKind.AGREEMENT}:
            raise InvariantViolation("unsupported attestation subject")
        if not self.claim_type.strip():
            raise InvariantViolation("claim type cannot be empty")
        if self.issued_at.tzinfo is None:
            raise InvariantViolation("issued_at must be timezone-aware")
