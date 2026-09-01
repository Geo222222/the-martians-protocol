# Privacy, Proof, and Generational Archive Specification

## Governing principle

> **Everything material must be provable. Only minimum necessary evidence should be preserved or disclosed.**

The Martians is a private stewardship institution first. Family membership, kinship, contribution, succession, enterprise participation, or stewardship does not create blanket access to institutional history.

The protocol must maximize legitimate verification while minimizing disclosure.

## Four privacy classes

The Martians uses the same privacy vocabulary as `Geo222222/the-book`.

### `PUBLIC_PROOF`

Deliberately public testimony. Examples may include a public institutional genesis claim, a deliberately public authority credential, a public enterprise assertion, or a public state commitment.

Audience: anyone.

Persistence: durable.

### `PARTICIPANT_PROOF`

Durable proof needed by a named participant or authorized role to exercise or verify a right. Examples include the participant's own contribution, voting entitlement, scoped authority, agreement entitlement, or distribution claim.

Audience: named participants and authorized roles.

Persistence: durable.

A participant's right to verify their own record does not imply access to another participant's record.

### `CONFIDENTIAL_EVIDENCE`

Sensitive institutional evidence such as agreements, valuations, enterprise financials, private governance deliberations, disputes, succession reasoning, stewardship review, family matters, and internal standing.

Audience: selected roles, domains, and matters.

Persistence: governed by retention policy while the Big Book preserves the minimum proof necessary to establish material history.

### `SECRET_REGULATED`

Highest-risk source material: government identifiers, identity documents, bank credentials, tax records, medical records, private keys, recovery secrets, protected child information, and comparable regulated/private material.

Audience: extremely restricted systems.

**Raw `SECRET_REGULATED` source material must never be written directly to a blockchain, public proof surface, or general-purpose institutional event log.**

The restricted system may produce a digest/reference proving the exact source object relied upon.

## The Vault

The Vault holds underlying source evidence that requires encryption, access controls, retention policy, lawful deletion, or restricted handling.

Examples include contracts, estate documents, identity evidence, bank records, private correspondence, dispute evidence, and sensitive family records.

The Book should normally preserve:

```text
what material event occurred
who had authority
which policy/agreement governed it
which exact evidence version was relied upon by digest/reference
who is allowed to verify the proof
```

not the full source material.

## The Big Book

The Big Book is the private authoritative proof history shared with Benjamin, The Hand, and other institutional domains. The Martians does not operate a separate blockchain merely because it has stewardship events.

Martians proof namespaces may include:

```text
MARTIANS.IDENTITY
MARTIANS.RELATIONSHIP
MARTIANS.CONTRIBUTION
MARTIANS.STEWARDSHIP
MARTIANS.AUTHORITY
MARTIANS.AGREEMENT
MARTIANS.GOVERNANCE
MARTIANS.SUCCESSION
MARTIANS.ENTITLEMENT
MARTIANS.CORRECTION
```

Big Book access is scoped by role, domain, matter, participant rights, authority, and legitimate need.

A child does not automatically inherit visibility into every historical dispute. A business partner does not gain family history. A family member does not automatically receive another member's financial records.

## The Little Book

The Little Book is the public testimony surface. It is not a mirror or export of Martians history.

The Martians may deliberately support public proofs such as:

- institutional genesis claims;
- public keys and revocations;
- externally verifiable authority credentials;
- selected enterprise assertions;
- periodic Big Book state commitments;
- intentionally public attestations.

The public verifier receives the minimum claim necessary for the verification purpose, not the family ledger.

## Non-reconstruction rule

> **The Little Book must never be sufficient to reconstruct the private Martians history.**

A public observer must not be able to derive private family relationships, disputes, contribution amounts, inheritance planning, internal standing, private business relationships, children's records, succession deliberations, or confidential agreements unless a specific claim is deliberately published.

## Internal least privilege

No participant receives more information than is necessary to:

- exercise their rights;
- perform delegated authority;
- satisfy a fiduciary/legal duty;
- participate in a defined matter; or
- verify a legitimate claim.

Access should support scoped roles, matter membership, domain membership, participant-specific rights, temporary delegation, expiration, revocation, and audit.

## Generational archive

The archive preserves institutional context without requiring unrestricted visibility.

Future generations should be able, where authorized, to determine:

- what institutions existed;
- what responsibilities and authorities existed;
- what contributions and major decisions were recorded;
- how ownership and authority transitioned;
- what failures and lessons were intentionally preserved;
- what prior generations intended successors to preserve or improve.

Explanatory context may exist in the Vault or confidential archive while the Big Book preserves cryptographic proof that the exact context record existed and was relied upon.

## Corrections and dignity

Immutable event history must not become immutable personal harm.

False claims, superseded judgments, changed circumstances, and corrected records are represented through correction, revocation, supersession, and access policy. The institution preserves the fact that a record changed without requiring every sensitive allegation or private detail to become permanently exposed.

## Durability

Proof history, public commitments, and source archives must be exportable and cryptographically verifiable so institutional continuity does not depend on one vendor, one administrator, one database, one blockchain, or one user interface.
