# System Architecture

## Layered model

The Martians Protocol is organized as six logical layers.

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

### 4. Governance Layer

- proposals
- policies
- scoped authority
- voting/approval mechanisms
- succession and recovery

### 5. Economic Layer

- treasury policies
- protocol services
- future MARS asset
- optional staking and economic security

### 6. Cryptographic and Data Layer

- keys and signatures
- content hashes
- tamper-evident event history
- encrypted private storage
- selectively disclosed proofs and attestations
- optional blockchain anchoring
- generational archive

## Architectural rule

Blockchain is not the system of record for every piece of family data. The architecture should choose the minimum-trust mechanism appropriate to each state transition.

## Off-chain by default for sensitive state

Private source records, family documents, legal evidence, financial records, and other Restricted/Vault information remain encrypted off-chain. A hash or cryptographic commitment may be anchored when independently verifiable existence or integrity provides real value.

## Event model

The protocol should evolve around append-oriented events. State is derived from events such as:

- identity created;
- controller changed;
- relationship asserted;
- relationship verified;
- enterprise registered;
- ownership attested;
- contribution submitted;
- contribution verified;
- agreement signed;
- authority delegated;
- governance decision executed;
- succession triggered; and
- archive record superseded.

Corrections are new events; they are not silent mutation of history.

## Network isolation

Every Family Network has a stable network identifier and its own membership, authority, privacy, treasury, and governance state. Shared protocol infrastructure must not imply shared family governance.

## Genesis rule

Network `0001` is the genesis implementation. Martin × Williams data, naming, rules, or roles must not be hard-coded into generic protocol modules.

## Smart-contract boundary

Only state transitions that benefit from independent execution, common settlement, tamper resistance, multi-party control, or public verification should become smart contracts. Conventional application logic remains conventional application logic when that is safer and simpler.