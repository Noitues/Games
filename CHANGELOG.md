# Changelog

Every rule patch to `RULES_SPEC.md`, with the spec version it produced. Harness-only changes are listed separately.

## Spec

### 0.1.0 — 2026-09-22
- Initial spec as supplied. No patches yet: the brief allows patches only between batches, after the human review gate, and only on repeated structural evidence (a rule with 3 or more ambiguities).

## Harness

### 2026-09-23
- Initial harness: engine, arms (A, B, C and §13 variants), chargen, run, batch, analyze, schema, scripted backend and engine tests.
- Interim rulings AMB-01…AMB-26 (see `docs/design_notes.md` and `harness/rulings.py`).
