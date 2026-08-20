# Enterprise and Ownership Specification

## Enterprise classes

A Family Network may register organizations as:

- `FAMILY_OWNED`
- `FAMILY_CONTROLLED`
- `FAMILY_AFFILIATED`

These classifications are descriptive and must not overstate legal ownership or control.

## Enterprise Node

An Enterprise Node should support at least:

- stable enterprise identifier;
- legal/display name;
- jurisdiction;
- entity type;
- classification;
- ownership attestations;
- responsible operators;
- relationship to other enterprises;
- status; and
- evidence references.

## Enterprise-to-enterprise relationships

The protocol should be able to record relationships between organizations without confusing those relationships with legal ownership.

Initial relationship types may include:

- `CREATED_BY`
- `ORIGINATED_BY`
- `PARENT_OF`
- `SUBSIDIARY_OF`
- `SERVICE_PROVIDER_TO`
- `CUSTOMER_OF`
- `DESIGN_PARTNER_OF`
- `AFFILIATED_WITH`

Each relationship record should include source enterprise, target enterprise, relationship type, effective date, attestor(s), evidence where appropriate, verification status, and an optional legal-status qualifier.

A `CREATED_BY` or `ORIGINATED_BY` relationship does **not** prove parent/subsidiary ownership. A `PARENT_OF` or `SUBSIDIARY_OF` assertion should require stronger evidence tied to controlling legal documents.

### Genesis example

Genesis Network 0001 currently uses the operating assertion:

- `SalonSignal ORIGINATED_BY CodeReign`

This records the family-enterprise operating relationship while leaving exact legal parentage, equity, capitalization, and tax treatment to formation documents and applicable law.

## Ownership rule

The initial protocol records ownership; it does not create ownership.

A verified ownership record may contain enterprise or asset identifier, legal owner reference, ownership percentage or interest, evidence hash/reference, effective date, jurisdiction, verifier(s), and verification status.

The underlying legal system and controlling documents remain authoritative.

## Future digital representation

A later specification may support digital representations of legally recognized ownership where technically and legally appropriate. Any such representation must be explicitly linked to the legal mechanism that gives it effect.

No generic token balance may be interpreted as legal ownership merely because it exists on-chain.

## Authority boundaries

Enterprise governance is scoped to the enterprise. Family governance does not automatically grant operational or ownership authority over an enterprise. Enterprise owners and authorized managers retain their legally and contractually defined authority.

Shared family capabilities—technology, business intelligence, marketing, education, or security/resilience—must be represented as scoped roles or service relationships rather than implied ownership.