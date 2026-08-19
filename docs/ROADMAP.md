# Martians Protocol Alpha Roadmap

## Objective

Produce a working Genesis Network 0001 alpha that proves identity, family graph, enterprise registration, contribution attestations, agreement events, cryptographic signatures/hashes, and tamper-evident history without requiring a production token.

## Day 1 — Protocol Model

- finalize constitutional invariants;
- define canonical IDs and event envelope;
- define identity, relationship, enterprise, contribution, agreement, and attestation schemas;
- define privacy classes;
- define network isolation rules.

**Exit:** machine-readable schemas and protocol event semantics are stable enough to code against.

## Day 2 — Identity and Family Graph

- implement Martian Identity;
- implement Family Network membership;
- implement relationship assertions and lifecycle states;
- implement guardian-controlled identities;
- implement authorization boundaries.

**Exit:** Network 0001 can resolve members and relationships without hard-coding family names into generic protocol logic.

## Day 3 — Enterprise and Contribution Ledger

- implement Enterprise Nodes;
- implement ownership attestations;
- implement contribution records;
- implement configurable attestation policies;
- preserve immutable event provenance.

**Exit:** an authorized enterprise can receive and verify a contribution tied to an MID.

## Day 4 — Agreement and Governance Terminal

- implement agreement metadata and document hashes;
- implement signatures and milestones;
- implement scoped authority policies;
- implement basic governance proposals/approvals;
- expose protocol state through a terminal-oriented API/UI surface.

**Exit:** parties can create, sign, advance, and verify an agreement lifecycle.

## Day 5 — Cryptographic Verification

- implement key/signature abstraction;
- hash canonical events;
- chain or otherwise tamper-proof event references;
- implement verification CLI/API;
- add testnet anchoring only where useful;
- test recovery and invalid-signature paths.

**Exit:** an independent verifier can detect modified protocol history.

## Day 6 — Genesis Alpha Certification

- populate non-sensitive Network 0001 demonstration state;
- execute end-to-end identity -> enterprise -> contribution/agreement -> attestation -> cryptographic verification flow;
- run security and invariant tests;
- document known limitations;
- update whitepaper with implemented architecture;
- tag the alpha when certification criteria pass.

**Exit:** `v0.1.0-alpha` is demonstrable and its claims are backed by executable evidence.

## Deferred beyond Alpha

- production MARS token;
- token sale or exchange listing;
- public mainnet treasury assets;
- tokenized legal ownership;
- unrestricted public family records;
- claims of full decentralization before the trust model supports them.

## Alpha certification rule

A feature is not considered protocol capability merely because a UI displays it. Certification requires executable protocol behavior, authorization tests, negative-path tests, persistence evidence, and cryptographic verification where the feature claims cryptographic integrity.