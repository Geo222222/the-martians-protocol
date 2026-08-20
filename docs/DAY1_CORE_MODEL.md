# Day 1 Core Domain Model

## Scope

Day 1 establishes storage-agnostic protocol semantics. It intentionally has **no blockchain dependency, wallet requirement, token contract, database, or network service**.

The implementation provides canonical typed identifiers, family-network isolation, immutable domain records, identity lifecycle rules, relationship correction by supersession rather than deletion, enterprise/contribution/agreement/attestation primitives, privacy classifications, deterministic protocol event envelopes, per-network append-only hash chaining, JSON Schema Draft 2020-12 wire contracts, and invariant tests.

## Canonical identifier form

`<KIND>:<NAMESPACE>:<SEQUENCE>`

Examples: `NET:MW:000001`, `MID:MW:000001`, `ENT:MW:000001`, `CTR:MW:000001`, `AGR:MW:000001`, `ATT:MW:000001`, `EVT:MW:000001`.

The namespace is an isolation/readability hint, not the security boundary. The registry enforces the actual network reference boundary.

## Day 1 invariants enforced in code

1. Protocol IDs are unique and cannot be reused inside a registry/ledger.
2. Cross-network relationships, contributions, agreements, guardianship, and attestations are rejected.
3. Contribution records do not create ownership rights.
4. Historical relationships are corrected by supersession; the prior record remains traceable.
5. Archived identities cannot be reactivated.
6. Death does not create a new identity; the same MID survives into archival state.
7. Event payload hashes are deterministic under canonical JSON serialization.
8. Event streams are per-network and require the current ledger-head hash.
9. Event envelopes are immutable values.
10. Privacy is explicit: `PUBLIC`, `FAMILY`, `RESTRICTED`, or `VAULT`.

## Important non-claims

The Day 1 event ledger is **not a blockchain** and is not described as decentralized consensus. It is a deterministic, tamper-evident local model that gives later cryptographic anchoring a stable semantic foundation.

The model does not issue MARS, tokenize legal ownership, or assign governance rights based on capital.

## Running tests

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The test suite uses only the Python standard library.
