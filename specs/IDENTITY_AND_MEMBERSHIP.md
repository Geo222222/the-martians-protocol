# Identity and Membership Specification

## Martian Identity

Every human participant receives one persistent Martian Identity (`MID`). Names, households, affiliations, roles, and controllers are mutable attributes; the MID is the durable identity reference.

An MID survives name changes, marriage, divorce, relocation, household changes, business changes, loss of active privileges, incapacity, and death.

## Membership classes

A Family Network may classify human relationships as:

- lineal descendant;
- biological relative;
- adopted relative;
- spouse;
- legally recognized family relationship;
- guardian/dependent relationship;
- affiliated member; or
- trusted contributor.

Membership class does not automatically determine ownership, compensation, inheritance, reputation, or governance authority.

Businesses and other organizations are Enterprise Nodes, not human Martian identities.

## Participation status

Supported lifecycle states include:

- `ACTIVE`
- `INACTIVE`
- `SUSPENDED`
- `SEPARATED`
- `DECEASED`
- `ARCHIVED`

Changing status does not erase historical participation.

## Relationship graph

Relationships are represented through attestations rather than unrestricted administrator edits. A relationship claim may progress through states such as:

- asserted;
- verified;
- disputed;
- corrected; or
- superseded.

High-confidence relationships may require multiple attestations and/or evidence hashes. Raw birth certificates, adoption records, DNA records, court records, and equivalent source documents remain private.

## Children and guardianship

An authorized guardian may create an MID for a child. The identity begins under guardian-controlled custody but must remain the same identity as control transitions toward adulthood.

Recommended lifecycle:

`GUARDIAN_CONTROLLED -> YOUTH_PARTICIPANT -> LIMITED_SELF_CUSTODY -> ADULT_SELF_CUSTODY`

The precise transition ages and legal requirements are network- and jurisdiction-specific.

## Recovery

Identity control must support recovery without allowing arbitrary identity reassignment. Critical identities should support social recovery, multi-party guardianship, or another policy that avoids a single lost key permanently destroying access.

## Privacy

Public or family-visible identity data must be minimized. Government identifiers, identity documents, medical data, financial records, recovery secrets, and private keys are Vault-class data and must never be written raw to a public chain.