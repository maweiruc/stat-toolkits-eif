# Changelog

## v1.0.0

Initial documentation-first release of the EIF derivation toolkit.

### Added

- Human usage guide: `MANUAL.md`
- Agent instructions: `AGENTS.md`
- Trial guide: `TRIAL_GUIDE.md`
- LaTeX problem inbox: `problems/latex_inbox/`
- Automatic `notes.md` convention for LaTeX problems
- LaTeX problem normalization protocol
- Target triage protocol
- Research-mode derivation protocol
- Hard-problem protocol
- Answer rubric
- Validation tests guide
- Implementation guide
- Danger-zone guide
- Formula registry
- Formula registry schema and lightweight validation tooling
- GitHub Actions CI for registry validation and unit tests
- Contribution and local-reference hygiene guidance
- Standard and hard benchmark tasks
- Simulation test designs
- Projection guide for restricted semiparametric models
- Worked derivation for the restricted moment model
- Worked derivation for the partially linear single index model
- Maximum-effort research-mode rule before declaring candidate/projection-unresolved status

### Scope

This release is intended for deriving, auditing, and validating IF/EIF formulas, especially for semiparametric research problems where formula lookup is insufficient.

### Not Included

- Statistical Python/R package API
- Automated symbolic algebra
- Automated LaTeX parsing beyond agent workflow
- Full numerical simulation runner
- Formal theorem-proving or proof assistant integration
