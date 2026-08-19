# Trust Model

## Objective

The Martians Protocol should reduce unnecessary trust without pretending trust can be eliminated from family life.

## Trust domains

### Human trust

Some claims inherently require people: kinship attestations, mentorship, caregiving, contextual contribution, and governance judgment.

### Institutional trust

Legal ownership, corporate authority, identity documents, court orders, trusts, estates, and regulated financial records may depend on external institutions and jurisdictions.

### Cryptographic trust

Signatures, hashes, commitments, multisignature policies, and append-only event structures can provide integrity, provenance, authorization evidence, and tamper detection.

### Protocol trust

Smart contracts or shared protocol services may enforce deterministic state transitions where their assumptions are appropriate.

## Trust minimization rules

- Do not trust one administrator to rewrite history.
- Do not trust one key with irreversible control over critical network functions.
- Do not treat a blockchain as proof that an off-chain factual claim is true; it can prove that a claim was recorded or signed.
- Do not expose confidential source material merely to increase public verifiability.
- Require stronger attestation thresholds as consequence and irreversibility increase.
- Preserve evidence provenance.

## Threats to design against

- compromised administrator credentials;
- lost private keys;
- colluding attestators;
- false contribution claims;
- unauthorized disclosure of family records;
- governance capture;
- token-based plutocracy leaking into family authority;
- founder overreach;
- succession failure;
- ambiguous ownership claims;
- retrospective history rewriting;
- cross-network privilege escalation;
- smart-contract bugs;
- malicious or accidental protocol upgrades; and
- dependency on a single vendor or application.

## Core principle

Cryptography protects integrity and authorization. Governance establishes legitimate authority. Evidence supports factual claims. Law governs legal rights. These must not be confused.