# Treasury Specification

## Purpose

A Family Network may operate one or more protocol-controlled or protocol-observed treasuries. Each treasury must have an explicit mandate rather than functioning as an undifferentiated pool of family money.

## Treasury classes

Examples include:

- `EDUCATION`
- `EMERGENCY`
- `ENTERPRISE`
- `INVESTMENT`
- `PROPERTY`
- `INNOVATION`
- `PHILANTHROPY`
- `GENERATIONAL`
- `OPERATING`

## Required policy

Each treasury SHOULD define:

- purpose;
- eligible expenditures;
- prohibited expenditures;
- funding sources;
- authorized approvers;
- approval threshold;
- transaction limits;
- reporting policy;
- investment policy where applicable;
- beneficiary rules;
- emergency authority; and
- succession/recovery policy.

## Example: Education Treasury

Purpose: increase the productive capability of current and future family members.

Potential permitted uses:

- tuition;
- certifications;
- books;
- equipment;
- apprenticeships;
- research; and
- approved training.

Potential prohibited uses:

- unrelated consumer spending;
- undisclosed personal debt;
- unauthorized speculation; and
- expenditures outside the treasury mandate.

## Control model

Treasury control may use multisignature, role-based authorization, spending limits, timelocks, proposal thresholds, and audit requirements according to risk.

## Legal boundary

Protocol control does not remove tax, fiduciary, trust, corporate, banking, securities, investment-management, or other legal obligations. A treasury implementation must identify the legal owner or governing vehicle of the underlying assets.

## Auditability

Treasury decisions should be auditable without requiring unrestricted public disclosure of sensitive family financial information.