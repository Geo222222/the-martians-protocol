import hashlib
import unittest
from datetime import datetime, timezone

from martians_protocol import Agreement, Attestation, Contribution, ContributionType, Enterprise, EnterpriseKind, EventLedger, Identity, IdentityStatus, InvariantViolation, InvalidIdentifier, InvalidTransition, MembershipClass, Network, ProtocolEvent, ProtocolRegistry, Relationship, RelationshipStatus, RelationshipType


class ProtocolFixture(unittest.TestCase):
    def setUp(self):
        self.registry = ProtocolRegistry()
        self.net1 = Network("NET:MW:000001", "Martin × Williams", "MW")
        self.net2 = Network("NET:OTHER:000001", "Other Family", "OTHER")
        self.registry.add_network(self.net1); self.registry.add_network(self.net2)
        self.alice = Identity("MID:MW:000001", "NET:MW:000001", "Alice", MembershipClass.LINEAL_DESCENDANT)
        self.bob = Identity("MID:MW:000002", "NET:MW:000001", "Bob", MembershipClass.SPOUSE)
        self.other = Identity("MID:OTHER:000001", "NET:OTHER:000001", "Other", MembershipClass.LINEAL_DESCENDANT)
        self.registry.add_identity(self.alice); self.registry.add_identity(self.bob); self.registry.add_identity(self.other)
        self.enterprise = Enterprise("ENT:MW:000001", "NET:MW:000001", "Example Enterprise", EnterpriseKind.FAMILY_OWNED)
        self.registry.add_enterprise(self.enterprise)


class IdentifierTests(unittest.TestCase):
    def test_malformed_identifier_rejected(self):
        with self.assertRaises(InvalidIdentifier): Identity("MID:mw:1", "NET:MW:000001", "Bad", MembershipClass.SPOUSE)

    def test_network_namespace_must_match_id_namespace(self):
        with self.assertRaises(InvariantViolation): Network("NET:MW:000001", "Wrong", "OTHER")


class RegistryInvariantTests(ProtocolFixture):
    def test_protocol_ids_cannot_be_reused(self):
        with self.assertRaises(InvariantViolation): self.registry.add_identity(self.alice)

    def test_cross_network_relationship_is_forbidden(self):
        rel = Relationship("REL:MW:000001", "NET:MW:000001", self.alice.identity_id, self.other.identity_id, RelationshipType.RELATED_TO)
        with self.assertRaises(InvariantViolation): self.registry.add_relationship(rel)

    def test_cross_network_contribution_is_forbidden(self):
        c = Contribution("CTR:MW:000001", "NET:MW:000001", self.alice.identity_id, self.other.identity_id, ContributionType.MENTORSHIP, "Mentorship")
        with self.assertRaises(InvariantViolation): self.registry.add_contribution(c)

    def test_cross_network_agreement_is_forbidden(self):
        a = Agreement("AGR:MW:000001", "NET:MW:000001", (self.alice.identity_id, self.other.identity_id), "PROJECT", hashlib.sha256(b"agreement").hexdigest())
        with self.assertRaises(InvariantViolation): self.registry.add_agreement(a)

    def test_contribution_does_not_create_ownership(self):
        c = Contribution("CTR:MW:000001", "NET:MW:000001", self.alice.identity_id, self.enterprise.enterprise_id, ContributionType.CAPITAL, "Capital contribution", valuation_minor_units=10000, valuation_currency="USD")
        self.registry.add_contribution(c)
        self.assertEqual(len(self.registry.enterprises), 1); self.assertFalse(hasattr(c, "ownership_percent"))

    def test_relationship_correction_supersedes_history_instead_of_deleting_it(self):
        old = Relationship("REL:MW:000001", "NET:MW:000001", self.alice.identity_id, self.bob.identity_id, RelationshipType.RELATED_TO, RelationshipStatus.VERIFIED)
        self.registry.add_relationship(old)
        corrected = Relationship("REL:MW:000002", "NET:MW:000001", self.alice.identity_id, self.bob.identity_id, RelationshipType.SPOUSE_OF, RelationshipStatus.VERIFIED, supersedes_relationship_id=old.relationship_id)
        self.registry.add_relationship(corrected)
        self.assertIn(old.relationship_id, self.registry.relationships)
        self.assertEqual(self.registry.relationships[old.relationship_id].status, RelationshipStatus.SUPERSEDED)

    def test_attestation_subject_and_issuer_must_share_network(self):
        att = Attestation("ATT:MW:000001", "NET:MW:000001", self.alice.identity_id, self.other.identity_id, "IDENTITY_VERIFIED", {"verified": True})
        with self.assertRaises(InvariantViolation): self.registry.add_attestation(att)


class IdentityLifecycleTests(unittest.TestCase):
    def test_archived_identity_cannot_be_reactivated(self):
        identity = Identity("MID:MW:000001", "NET:MW:000001", "Alice", MembershipClass.LINEAL_DESCENDANT, status=IdentityStatus.ARCHIVED)
        with self.assertRaises(InvalidTransition): identity.transition(IdentityStatus.ACTIVE)

    def test_death_preserves_identity_and_allows_archive_only(self):
        identity = Identity("MID:MW:000001", "NET:MW:000001", "Alice", MembershipClass.LINEAL_DESCENDANT).transition(IdentityStatus.DECEASED)
        archived = identity.transition(IdentityStatus.ARCHIVED)
        self.assertEqual(archived.identity_id, identity.identity_id)
        with self.assertRaises(InvalidTransition): identity.transition(IdentityStatus.ACTIVE)


class EventLedgerTests(unittest.TestCase):
    def setUp(self):
        self.ledger = EventLedger(); self.now = datetime(2026, 8, 20, 12, 0, tzinfo=timezone.utc)

    def make_event(self, seq, previous=None, payload=None):
        return ProtocolEvent(f"EVT:MW:{seq:06d}", "NET:MW:000001", "IDENTITY_REGISTERED", "MID:MW:000001", "MID:MW:000002", payload or {"status": "ACTIVE"}, self.now, previous)

    def test_event_payload_hash_is_deterministic(self):
        self.assertEqual(self.make_event(1, payload={"a":1,"b":2}).payload_hash, self.make_event(2, payload={"b":2,"a":1}).payload_hash)

    def test_event_chain_requires_current_ledger_head(self):
        head = self.ledger.append(self.make_event(1))
        with self.assertRaises(InvariantViolation): self.ledger.append(self.make_event(2, previous="0"*64))
        self.ledger.append(self.make_event(2, previous=head)); self.assertTrue(self.ledger.verify("NET:MW:000001"))

    def test_event_ids_cannot_be_reused(self):
        first = self.make_event(1); self.ledger.append(first)
        with self.assertRaises(InvariantViolation): self.ledger.append(first)

    def test_event_is_immutable(self):
        event = self.make_event(1)
        with self.assertRaises(Exception): event.event_type = "MUTATED"


if __name__ == "__main__": unittest.main()
