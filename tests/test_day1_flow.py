import hashlib
import unittest
from datetime import datetime, timezone

from martians_protocol import Agreement, Attestation, Contribution, ContributionType, Enterprise, EnterpriseKind, EventLedger, Identity, MembershipClass, Network, ProtocolEvent, ProtocolRegistry


class Day1FlowTest(unittest.TestCase):
    def test_genesis_flow_can_be_represented_without_blockchain(self):
        registry = ProtocolRegistry(); network = Network("NET:MW:000001", "Martin × Williams", "MW"); registry.add_network(network)
        founder = Identity("MID:MW:000001", network.network_id, "Founder", MembershipClass.LINEAL_DESCENDANT)
        member = Identity("MID:MW:000002", network.network_id, "Member", MembershipClass.LINEAL_DESCENDANT)
        registry.add_identity(founder); registry.add_identity(member)
        enterprise = Enterprise("ENT:MW:000001", network.network_id, "Family Enterprise", EnterpriseKind.FAMILY_OWNED); registry.add_enterprise(enterprise)
        contribution = Contribution("CTR:MW:000001", network.network_id, member.identity_id, enterprise.enterprise_id, ContributionType.LABOR, "Built protocol feature", ("git:deadbeef",)); registry.add_contribution(contribution)
        attestation = Attestation("ATT:MW:000001", network.network_id, founder.identity_id, contribution.contribution_id, "CONTRIBUTION_VERIFIED", {"verified": True}); registry.add_attestation(attestation)
        agreement = Agreement("AGR:MW:000001", network.network_id, (founder.identity_id, enterprise.enterprise_id), "PROJECT", hashlib.sha256(b"private document bytes").hexdigest()); registry.add_agreement(agreement)
        ledger = EventLedger()
        first = ProtocolEvent("EVT:MW:000001", network.network_id, "CONTRIBUTION_RECORDED", member.identity_id, contribution.contribution_id, {"type": contribution.contribution_type.value}, datetime(2026, 8, 20, 13, 0, tzinfo=timezone.utc), None)
        head = ledger.append(first)
        second = ProtocolEvent("EVT:MW:000002", network.network_id, "ATTESTATION_ISSUED", founder.identity_id, attestation.attestation_id, {"claim_type": attestation.claim_type}, datetime(2026, 8, 20, 13, 1, tzinfo=timezone.utc), head)
        ledger.append(second)
        self.assertTrue(ledger.verify(network.network_id)); self.assertEqual(len(registry.identities), 2); self.assertEqual(len(registry.enterprises), 1); self.assertEqual(len(registry.contributions), 1); self.assertEqual(len(registry.attestations), 1); self.assertEqual(len(registry.agreements), 1)


if __name__ == "__main__": unittest.main()
