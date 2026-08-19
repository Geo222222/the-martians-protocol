# Privacy and Generational Archive Specification

## Disclosure tiers

The protocol defines three baseline data classes.

### Family Public

Visible to appropriately authorized family-network participants. Examples may include display identity, selected family-graph relationships, enterprises, roles, public contributions, and approved historical timeline entries.

### Restricted

Visible only to explicitly authorized people or roles. Examples include contracts, compensation, treasury information, ownership evidence, internal business records, and sensitive governance discussions.

### Vault

Highest-risk encrypted material. Examples include identity documents, tax records, medical records, estate documents, bank information, government identifiers, legal disputes, recovery secrets, and private keys.

Vault data must never be written raw to a public blockchain.

## Privacy principle

> **Maximum verification, minimum disclosure.**

The protocol should prefer encrypted off-chain source data and selectively expose hashes, signatures, claims, proofs, permissions, and attestations only when necessary.

## Generational archive

The archive is intended to preserve institutional context, not merely transactions.

Future generations should be able to determine:

- who participated;
- what they built;
- what responsibilities they held;
- what businesses and assets existed;
- who contributed and how;
- what major decisions were made;
- why those decisions were made;
- what failures and lessons were recorded;
- how ownership and authority transitioned;
- what knowledge was considered important; and
- what prior generations intended successors to preserve or improve.

## Context preservation

Where privacy permits, significant events should support explanatory context so descendants can understand why an event occurred rather than seeing only a timestamp or transfer value.

## Durability

The archive should be exportable and cryptographically verifiable so that family history does not depend permanently on one vendor, administrator, database, or user interface.