# The Martians Protocol

> **A private-by-default family enterprise, stewardship, and generational coordination protocol.**

The Martians Protocol is infrastructure for families that want to operate as durable multi-generational institutions rather than collections of disconnected individuals, businesses, records, and memories.

Its purpose is to coordinate identity, family relationships, enterprise activity, contribution, agreements, authority, governance, succession, treasury policy, security/resilience responsibility, and institutional knowledge across generations **without turning family history into a public ledger**.

## Core principles

> **The protocol exists to strengthen the family institution; the family does not exist to create demand for the protocol token.**

> **Everything material must be provable. Only minimum necessary evidence should be preserved or disclosed.**

The protocol deliberately separates concepts that must never collapse into one another:

- **Identity** — who you are.
- **Kinship** — how you are connected.
- **Contribution** — what you did.
- **Stewardship** — how you have served.
- **Ownership** — what legally belongs to you.
- **Authority** — what you are permitted to decide.
- **Enterprise relationship** — how one organization is connected to another without pretending that relationship alone proves legal ownership.
- **Security responsibility** — what protective, continuity, or incident-management function has been delegated.
- **MARS** — what protocol economic capacity you can deploy, if an economic layer is eventually justified.

## Privacy architecture

The Martians holds **stewardship truth**. It does not need a separate Martians blockchain.

```text
THE MARTIANS
private stewardship system
      |
      | minimum necessary proofs
      v
BIG BOOK
private authoritative proof history
      |
      +---- scoped internal verification
      |
      +---- explicitly selected commitments/claims
                 |
                 v
            LITTLE BOOK
            public testimony
```

Underlying contracts, identity documents, dispute evidence, private correspondence, regulated records, and other sensitive source material belong in **The Vault** or governed private stores.

The shared privacy classes are:

- `PUBLIC_PROOF`
- `PARTICIPANT_PROOF`
- `CONFIDENTIAL_EVIDENCE`
- `SECRET_REGULATED`

Family membership does not grant blanket access. Access is scoped by role, domain, matter, participant rights, delegated authority, and legitimate need.

The **Little Book must never be sufficient to reconstruct the private Big Book or the private Martians history**.

See `specs/PRIVACY_AND_ARCHIVE.md` and `architecture/THE_BOOK_INTEGRATION.md`.

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

Current status: **v0.2 privacy and proof architecture foundation**.

This repository remains specification-first. Smart contracts, tokens, and blockchain infrastructure do not precede the rules they are supposed to enforce.

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
│   ├── TRUST_MODEL.md
│   └── THE_BOOK_INTEGRATION.md
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
2. Privacy classes, least privilege, and minimum-necessary proof rules.
3. Identity, family graph, membership, and guardianship.
4. Enterprise registry, ownership attestations, and enterprise-to-enterprise relationships.
5. Scoped roles, security/resilience, and authority attestations.
6. Contribution and participant-proof lifecycle.
7. Agreement and governance primitives.
8. Vault/archive, key recovery, retention, and succession.
9. Cryptographic signatures and Big Book integration.
10. Explicit Little Book public claims and state commitments.
11. Permissioned/public blockchain adapters only where trust analysis proves they add value.
12. Treasury controls.
13. MARS economic layer only after demonstrated protocol necessity.

## Non-goals

The Martians Protocol does not claim that a blockchain record automatically creates legal ownership, kinship, inheritance rights, corporate authority, property title, employment status, security licensing, weapons authority, or contractual validity. Legal structures remain governed by applicable law and controlling documents.

A protocol record that one organization was `CREATED_BY` or `ORIGINATED_BY` another organization describes an asserted relationship; it does not substitute for formation, capitalization, tax, or ownership documents.

The protocol does not require raw family history, strategy, private relationships, disputes, identity data, financial records, or regulated data to become public or immutable merely to achieve institutional legitimacy.

## License

A license will be selected after the protocol governance and commercialization model are finalized.
