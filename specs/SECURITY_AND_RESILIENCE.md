# Security and Resilience Specification

## Purpose

The protocol must be able to represent security, continuity, and incident-management responsibility without confusing those responsibilities with ownership, law-enforcement authority, or unrestricted access.

## Security Role Attestation

A Security Role Attestation may contain:

- identity reference;
- family-network reference;
- enterprise scope;
- role type;
- delegated capabilities;
- explicit exclusions;
- effective date;
- expiration/review date;
- delegating authority;
- evidence or agreement reference; and
- verification status.

Initial role/capability types may include:

- `SECURITY_COORDINATOR`
- `PHYSICAL_SECURITY_REVIEWER`
- `BUSINESS_CONTINUITY_COORDINATOR`
- `INCIDENT_COORDINATOR`
- `ACCESS_CONTROL_ADMINISTRATOR`
- `SECURITY_VENDOR_COORDINATOR`
- `CYBER_PHYSICAL_LIAISON`

## Genesis reference role

Genesis Network 0001 currently proposes:

**Taheem Williams — Security & Resilience Lead**

The role is intended to cover physical-security coordination, facility risk review, access procedures, incident documentation, emergency planning, business continuity, security-vendor coordination, and coordination with CodeReign on cyber/physical security dependencies.

## Authority exclusions

A protocol Security Role Attestation must not be interpreted as automatically granting:

- ownership;
- police powers;
- arrest authority;
- unrestricted surveillance authority;
- unrestricted access to company systems or customer data;
- weapons licensing;
- authority to carry or use a weapon on behalf of an organization;
- employment status; or
- authority beyond that delegated by the relevant enterprise owner or controlling document.

Where regulated protective services are required, qualification and authority remain governed by applicable law, licensing, insurance, employer/vendor arrangements, property authorization, and organizational policy.

## Separation of security domains

The protocol should permit separate but coordinated domains:

- identity and authorization;
- cybersecurity;
- physical security;
- personnel safety;
- incident management; and
- business continuity.

For Genesis Network 0001, CodeReign is the technical/cybersecurity engineering capability while the Security & Resilience role coordinates physical-security and continuity responsibilities. Neither scope automatically overrides the other.

## Privacy

Detailed security plans are normally Restricted or Vault-class data. Public-chain anchors should contain only non-sensitive commitments/hashes or public-safe attestations. Alarm codes, access credentials, exploitable facility layouts, surveillance blind spots, weapon-storage details, and other operationally sensitive security information must not be published on-chain.