# EIF formula registry schema

This file describes the YAML schema for `examples/eif_formula_registry.yaml`.
The registry is a formula-matching aid. It should not be used as a substitute
for checking the observed data, target, model, assumptions, nuisance
definitions, and positivity conditions.

## Entry shape

Each top-level key is a stable snake-case identifier:

```yaml
ate:
  observed_data: "O = (Y, A, X)"
  target: "psi = E[Y(1)-Y(0)]"
  assumptions:
    - "consistency"
    - "exchangeability"
    - "positivity"
  nuisances:
    m1: "E[Y|A=1,X]"
    m0: "E[Y|A=0,X]"
    e: "P(A=1|X)"
  eif: "..."
  estimator: "..."
  warnings:
    - "Check propensity score positivity."
```

## Required fields

The validator requires every entry to include:

- `observed_data`
- `target`
- `warnings`
- either `eif` or `status`

## Strict-mode fields

For regular EIF entries, strict mode requires:

- `eif`
- `estimator`
- `nuisances`

For nonregular or non-EIF entries, strict mode requires:

- `status`
- `recommendation`

Use:

```bash
python3 scripts/validate_formula_registry.py --strict
```

## Field meanings

`observed_data`:
The observed data unit used by the formula.

`target`:
The population-level target parameter or functional.

`assumptions`:
Identification, regularity, support, or model assumptions needed before using
the formula.

`nuisances`:
Population-level nuisance functions appearing in the EIF or estimator.

`eif`:
The influence-function or efficient-influence-function expression. This field
does not by itself certify that the formula applies to a new problem.

`estimator`:
A short description of the usual estimator implied by the EIF.

`status`:
Used when no standard EIF is supplied, such as nonregular or unidentified
targets.

`recommendation`:
The safer alternative when the entry is nonregular, unidentified, or otherwise
not a standard EIF formula.

`warnings`:
The most important traps, denominator conditions, positivity checks, or ways
the formula is commonly misused.

## Style rules

- Prefer concise strings for formulas and targets.
- Use lists for `assumptions` and `warnings`.
- Use a mapping for `nuisances`, even when it is empty.
- Do not add a registry entry unless the formula's observed data and target are
  clear.
- For restricted semiparametric models, do not list a full-model IF as an EIF
  unless the tangent-space projection has been verified.
