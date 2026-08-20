# Machine-readable schemas

These JSON Schema Draft 2020-12 documents define the Day 1 wire format for core Martians Protocol objects. They are storage- and blockchain-agnostic.

Cross-object invariants such as network isolation, ID reuse prevention, lifecycle rules, and supersession semantics are enforced by the domain model and tests because JSON Schema alone cannot safely express those repository-wide constraints.
