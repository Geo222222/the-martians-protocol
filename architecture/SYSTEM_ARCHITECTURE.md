# System Architecture

## Architectural identity

The Martians holds **stewardship truth**: family-network identity, scoped relationships, contribution, authority, agreements, governance, succession, entitlement, and institutional context.

It does not become legitimate by publishing family history to a blockchain. It becomes legitimate through provable authority, governing documents, reproducible records, evidence, and cryptographic integrity.

## Layered model

The Martians Protocol is organized as seven logical layers.

### 1. Family Network Layer

- Martian Identity
- membership
- family graph
- guardianship
- lifecycle status

### 2. Enterprise Layer

- enterprise registry
- ownership attestations
- roles
- agreements
- project relationships

### 3. Stewardship Layer

- contributions
- attestations
- reputation dimensions
- credentials
- participant entitlements

### 4. Governance Layer

- proposals
- policies
- scoped authority
- voting/approval mechanisms
- succession and recovery
- corrections and revocations

### 5. Economic Layer

- treasury policies
- protocol services
- future MARS asset
- optional economic security where justified

### 6. Private Data and Vault Layer

- encrypted source evidence
- contracts and estate records
- private correspondence and deliberations
- identity/regulated documents
- matter-level access controls
- retention and lawful deletion
- versioned evidence references

### 7. Proof and Verification Layer

Provided through `Geo222222/the-book`:

- signed event proofs
- evidence digests and references
- privacy classes and visibility scope
- private Big Book history
- append-only lineage
- state/Merkle commitments
- explicit Little Book public attestations
- optional permissioned/private and public blockchain adapters

## Architectural rule

> **Everything material must be provable. Not everything known by The Martians belongs in a ledger, and almost nothing belongs on a public chain by default.**

Blockchain is not the system of record for every piece of family data. The architecture chooses the minimum-trust and minimum-disclosure mechanism appropriate to each state transition.

## Big Book relationship

The Martians does not need a separate Martians blockchain.

```text
THE MARTIANS
stewardship truth
      |
      | minimum necessary signed proofs
      v
BIG BOOK
private authoritative proof history
      |
      +---- authorized internal verification
      |
      +---- selected commitments/claims
                 |
                 v
            LITTLE BOOK
           public testimony
```

The Big Book may eventually be implemented using a permissioned blockchain when independently controlled trustees, auditors, trusts, custodians, or other institutions need to agree on history without trusting one operator completely.

Multiple nodes controlled by one operator provide redundancy, not independent trust.

## Off-ledger by default for sensitive source state

Private family documents, legal evidence, financial records, identity documents, disputes, health information, children-related records, succession deliberations, and other confidential or secret/regulated information remain in the Vault or governed application stores.

The Big Book may record a hash, cryptographic commitment, authority, visibility scope, and durable evidence reference when verifiable existence or integrity provides real value.

## Privacy classes

Every material proof is classified independently from its domain meaning:

- `PUBLIC_PROOF`
- `PARTICIPANT_PROOF`
- `CONFIDENTIAL_EVIDENCE`
- `SECRET_REGULATED`

Family membership never implies full Big Book visibility.

## Event model

The protocol evolves around append-oriented material events such as:

- identity created;
- controller changed;
- relationship asserted or verified;
- enterprise registered;
- ownership attested;
- contribution accepted or corrected;
- agreement accepted;
- authority delegated, expired, or revoked;
- governance decision executed;
- succession triggered;
- entitlement established or changed; and
- archive record superseded.

Corrections are new events; they are not silent mutation of history.

Not every chat message, thought, draft, family interaction, or intermediate calculation is a material event.

## Public proof model

There is no automatic Big Book-to-Little Book projection.

The Little Book may receive only explicitly approved public artifacts such as:

- genesis and charter commitments;
- public keys and revocations;
- public authority credentials;
- periodic state commitments;
- deliberately public enterprise/asset attestations.

The public surface must never be sufficient to reconstruct private stewardship history.

## Network isolation

Every Family Network has a stable network identifier and its own membership, authority, privacy, treasury, and governance state. Shared Book infrastructure must not imply shared family governance or cross-network read access.

## Genesis rule

Network `0001` is the genesis implementation. Genesis-specific people, enterprises, naming, rules, or roles must not be hard-coded into generic protocol modules.

## Smart-contract boundary

Only state transitions that benefit from independent execution, common settlement, tamper resistance, multi-party control, or public verification should become smart contracts.

Conventional application logic, encrypted storage, signatures, and databases remain conventional when they provide the safer and simpler mechanism.
