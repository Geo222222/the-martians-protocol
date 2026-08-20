from __future__ import annotations

from dataclasses import replace

from .domain import Agreement, Attestation, Contribution, Enterprise, Identity, Network, Relationship, RelationshipStatus
from .errors import InvariantViolation
from .ids import IdKind, parse_id


class ProtocolRegistry:
    """In-memory Day 1 registry enforcing storage-independent invariants."""

    def __init__(self) -> None:
        self.networks = {}
        self.identities = {}
        self.relationships = {}
        self.enterprises = {}
        self.contributions = {}
        self.agreements = {}
        self.attestations = {}
        self._all_ids = set()

    def _claim_id(self, object_id: str) -> None:
        parse_id(object_id)
        if object_id in self._all_ids:
            raise InvariantViolation(f"protocol id cannot be reused: {object_id}")
        self._all_ids.add(object_id)

    def add_network(self, network: Network) -> None:
        self._claim_id(network.network_id)
        self.networks[network.network_id] = network

    def _require_network(self, network_id: str) -> None:
        if network_id not in self.networks:
            raise InvariantViolation(f"unknown network: {network_id}")

    def _network_of(self, object_id: str) -> str:
        kind = parse_id(object_id).kind
        mapping = {
            IdKind.IDENTITY: self.identities,
            IdKind.RELATIONSHIP: self.relationships,
            IdKind.ENTERPRISE: self.enterprises,
            IdKind.CONTRIBUTION: self.contributions,
            IdKind.AGREEMENT: self.agreements,
            IdKind.ATTESTATION: self.attestations,
        }.get(kind)
        if mapping is None or object_id not in mapping:
            raise InvariantViolation(f"unknown referenced object: {object_id}")
        return mapping[object_id].network_id

    def _require_same_network(self, network_id: str, *object_ids: str) -> None:
        for object_id in object_ids:
            if self._network_of(object_id) != network_id:
                raise InvariantViolation("cross-network references are forbidden")

    def add_identity(self, identity: Identity) -> None:
        self._require_network(identity.network_id)
        for guardian_id in identity.guardian_ids:
            self._require_same_network(identity.network_id, guardian_id)
        self._claim_id(identity.identity_id)
        self.identities[identity.identity_id] = identity

    def add_enterprise(self, enterprise: Enterprise) -> None:
        self._require_network(enterprise.network_id)
        self._claim_id(enterprise.enterprise_id)
        self.enterprises[enterprise.enterprise_id] = enterprise

    def add_relationship(self, relationship: Relationship) -> None:
        self._require_network(relationship.network_id)
        self._require_same_network(relationship.network_id, relationship.subject_id, relationship.object_id)
        if relationship.supersedes_relationship_id:
            self._require_same_network(relationship.network_id, relationship.supersedes_relationship_id)
            old = self.relationships[relationship.supersedes_relationship_id]
            if old.status == RelationshipStatus.SUPERSEDED:
                raise InvariantViolation("a superseded relationship cannot be superseded again")
            self.relationships[old.relationship_id] = replace(old, status=RelationshipStatus.SUPERSEDED)
        self._claim_id(relationship.relationship_id)
        self.relationships[relationship.relationship_id] = relationship

    def add_contribution(self, contribution: Contribution) -> None:
        self._require_network(contribution.network_id)
        self._require_same_network(contribution.network_id, contribution.contributor_id, contribution.recipient_id)
        self._claim_id(contribution.contribution_id)
        self.contributions[contribution.contribution_id] = contribution

    def add_agreement(self, agreement: Agreement) -> None:
        self._require_network(agreement.network_id)
        self._require_same_network(agreement.network_id, *agreement.party_ids)
        self._claim_id(agreement.agreement_id)
        self.agreements[agreement.agreement_id] = agreement

    def add_attestation(self, attestation: Attestation) -> None:
        self._require_network(attestation.network_id)
        self._require_same_network(attestation.network_id, attestation.issuer_id, attestation.subject_id)
        self._claim_id(attestation.attestation_id)
        self.attestations[attestation.attestation_id] = attestation
