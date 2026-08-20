# The Martians Protocol

> **A cryptographic family enterprise, stewardship, and generational coordination protocol.**

The Martians Protocol is infrastructure for families that want to operate as durable multi-generational institutions rather than collections of disconnected individuals, businesses, records, and memories.

Its purpose is to preserve and coordinate identity, family relationships, enterprise activity, contribution, agreements, authority, governance, succession, treasury policy, security/resilience responsibility, and institutional knowledge across generations.

## Core principle

> **The protocol exists to strengthen the family institution; the family does not exist to create demand for the protocol token.**

The protocol deliberately separates concepts that must never collapse into one another:

- **Identity** — who you are.
- **Kinship** — how you are connected.
- **Contribution** — what you did.
- **Stewardship** — how you have served.
- **Ownership** — what legally belongs to you.
- **Authority** — what you are permitted to decide.
- **Enterprise relationship** — how one organization is connected to another without pretending that relationship alone proves legal ownership.
- **Security responsibility** — what protective, continuity, or incident-management function has been delegated.
- **MARS** — what protocol economic capacity you can deploy.

## Genesis implementation

The first implementation is **Genesis Network 0001 — Martin × Williams**.

The current family-enterprise reference graph includes:

- **GetTwisted** — owned by Sheryl Williams + Michael Williams;
- **Sheryl Williams Hair Replacement** — owned by Sheryl Williams;
- **CodeReign** — Djuvane Martin's technology and engineering organization;
- **SalonSignal** — a distinct salon-technology organization/venture created through CodeReign; and
- **The Martians** — the family coordination layer, not the automatic owner of the organizations above.

The Genesis network also exercises a shared **Security & Resilience** capability, currently proposed for Taheem Williams, covering physical-security coordination, continuity, incident readiness, and cyber/physical coordination without creating ownership or unrestricted enforcement authority.

The genesis family is the proving ground, not a hard-coded special case. The protocol must be capable of supporting additional independent family networks later without changing its constitutional model.

## Repository status

Current status: **v0.1 foundation and specification phase**.

This repository is intentionally specification-first. Smart contracts and token issuance do not precede the protocol rules they are supposed to enforce.

## Repository map

```text
the-martians-protocol/
├── constitution/
│   ├── PRINCIPLES.md
│   └── PROTOCOL_INVARIANTS.md
├── specs/
│   ├── IDENTITY_AND_MEMBERSHIP.md
│   ├── ENTERPRISE_AND_OWNERSHIP.md
│   ├── SECURITY_AND_RESILIENCE.md
│   ├── CONTRIBUTION_AND_ATTESTATION.md
│   ├── GOVERNANCE_AND_SUCCESSION.md
│   ├── PRIVACY_AND_ARCHIVE.md
│   ├── TREASURY.md
│   └── MARS_ECONOMICS.md
├── architecture/
│   ├── SYSTEM_ARCHITECTURE.md
│   └── TRUST_MODEL.md
├── genesis/
│   └── network-0001/
│       └── GENESIS_SPEC.md
├── whitepaper/
│   └── THE_MARTIANS_PROTOCOL.md
└── docs/
    └── ROADMAP.md
```

## Implementation order

1. Protocol invariants and constitutional boundaries.
2. Identity, family graph, membership, and guardianship.
3. Enterprise registry, ownership attestations, and enterprise-to-enterprise relationships.
4. Scoped role, security/resilience, and authority attestations.
5. Contribution ledger and attestation engine.
6. Agreement and governance primitives.
7. Privacy, archive, key recovery, and succession.
8. Cryptographic signatures and tamper-evident event history.
9. Selective on-chain anchoring.
10. Treasury controls.
11. MARS economic layer only after demonstrated protocol necessity.

## Non-goals

The Martians Protocol does not claim that a blockchain record automatically creates legal ownership, kinship, inheritance rights, corporate authority, property title, employment status, security licensing, weapons authority, or contractual validity. Legal structures remain governed by applicable law and their controlling documents.

A protocol record that one organization was `CREATED_BY` or `ORIGINATED_BY` another organization describes an asserted relationship; it does not substitute for formation, capitalization, tax, or ownership documents.

Sensitive family records, exploitable security details, credentials, access codes, protected health information, or confidential facility-security information must not be placed directly on a public blockchain.

## License

A license will be selected after the protocol governance and commercialization model are finalized.