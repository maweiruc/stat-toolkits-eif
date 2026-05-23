# stat-toolkits-eif

Current version: **v1.0.0**. See `VERSION.md` and `CHANGELOG.md`.

A documentation-first toolkit for deriving, checking, and validating influence
functions and efficient influence functions (EIFs) in semiparametric
statistics.

This repository is part of the `stat-toolkits-*` series. The Python import
package is `eif_toolkit`, and the validation CLI is `eif-validate`.

The main goal is not formula lookup. The goal is a robust workflow:

```text
normalize problem -> triage target -> check identification/regularity ->
derive pathwise derivative -> find IF/EIF -> verify -> implement if needed
```

It supports both standard problems and research problems where no exact formula is available in the literature.

---

## Which File Should I Read?

```text
For humans:
  Start with MANUAL.md.
  For first-time testers, start with TRIAL_GUIDE.md.
  Then read examples/eif_workflow_examples.md.

For coding agents:
  Start with AGENTS.md.
  Then follow the protocol files in agent/.

For theory:
  Read theory/semiparametric_influence_function_guide.md.
  For restricted models, read theory/eif_projection_guide.md.

For formula comparison:
  Use examples/eif_examples.md and examples/eif_formula_registry.yaml.
  Do not use them as a substitute for derivation.
```

---

## Document Roles

| File | Role |
| --- | --- |
| `VERSION.md` | Current release version and scope |
| `CHANGELOG.md` | Release history |
| `CONTRIBUTING.md` | Contribution, validation, and privacy guidance |
| `MANUAL.md` | Human-facing usage manual, with prompt templates |
| `TRIAL_GUIDE.md` | First-time trial guide and feedback checklist |
| `AGENTS.md` | Agent-facing operating instructions |
| `agent/eif_agent_task_spec.md` | Standard EIF task workflow |
| `agent/eif_latex_problem_protocol.md` | Parsing free-form or LaTeX problems |
| `agent/eif_target_triage.md` | Routing targets to the right derivation strategy |
| `agent/eif_research_problem_protocol.md` | First-principles derivation for novel targets |
| `agent/eif_hard_problem_protocol.md` | Hard-mode gates for unfamiliar or delicate problems |
| `agent/eif_answer_rubric.md` | Checklist for accepting or rejecting an answer |
| `agent/eif_validation_tests.md` | Mathematical and numerical validation checks |
| `agent/eif_implementation_guide.md` | Pseudo-outcomes, standard errors, cross-fitting |
| `agent/eif_danger_zone.md` | Common nonregularity and formula-misuse cases |
| `theory/semiparametric_influence_function_guide.md` | General IF/EIF theory |
| `theory/eif_projection_guide.md` | Tangent-space projection under restricted models |
| `theory/eif_restricted_moment_worked_derivation.md` | Worked projection derivation for restricted conditional mean models |
| `theory/eif_plsim_worked_derivation.md` | Worked tangent-space derivation for the partially linear single index model |
| `examples/eif_workflow_examples.md` | Copy-paste usage examples |
| `examples/eif_benchmark_tasks.md` | Standard benchmark tasks |
| `examples/eif_hard_benchmark_tasks.md` | Hard/research-adjacent benchmark tasks |
| `examples/eif_formula_registry.yaml` | Machine-readable formula registry |
| `examples/eif_formula_registry_schema.md` | Registry field schema and style rules |
| `simulations/eif_simulation_tests.md` | Simulation test designs |

---

## Quick Start

For a normal EIF derivation, ask:

```text
Please use the EIF toolkit in this folder.

Observed data:
O = ...

Target:
...

Model/assumptions:
...

Please derive the IF/EIF. Do not implement code unless requested.
```

For a research problem, add:

```text
This may be a novel target. Please use research mode.
Do not rely on formula lookup.
Build the derivation from first principles.
Make a maximum-effort attempt to get the final IF/EIF.
Only mark unresolved after trying the identifiable verification/projection/operator steps.
Clearly distinguish candidate IF, valid IF, EIF, projection unresolved, and nonregular conclusions.
```

More templates are in `MANUAL.md` and `examples/eif_workflow_examples.md`.

## Problem Inbox

Use `problems/latex_inbox/` for LaTeX or free-form EIF problems.

- Put each new problem in its own `problem_XXX/` folder with `problem.tex`.
- `notes.md` is optional; when missing, the agent should generate it before
  derivation.
- Local/private working folders can stay ignored by git when needed.

## Engineering Checks

The small Python package in this repository is only for registry validation.
It is not a statistical EIF computation API.

```bash
python3 scripts/validate_formula_registry.py --strict
python3 -m eif_toolkit.registry_validation --strict
python3 -m unittest discover -s tests
```

---

## Core Modes

### Fast Mode

Use when the target exactly matches a known regular problem, such as a mean, variance, ratio, missing-data mean, ATE, ATT, or mean potential outcome.

The registry can be used only after checking the observed data, target, model, assumptions, nuisance definitions, and positivity conditions.

### Hard Mode

Use when formula lookup is unsafe, for example:

- censoring or coarsening
- longitudinal regimes
- continuous treatments
- mediation
- transportability
- IV or weak-ratio targets
- quantiles with density issues
- optimal or learned rules
- restricted semiparametric models
- pointwise CATE, density at a point, max, argmax, or post-selection targets

Hard mode requires identification, regularity, support, and tangent-space checks before giving an EIF.

### Research Mode

Use when no exact formula is available. The output should be a derivation record, not just a formula.

Research mode should push past the first candidate IF or representer. If projection or verification is not complete, the answer should show the attempted score checks, projection or normal equations, and the precise mathematical obstruction.

Research-mode answers should label their status:

```text
derived and verified / candidate IF / valid IF but not efficient /
projection unresolved / differentiability unclear / unidentified / nonregular
```

---

## Minimal Acceptance Checklist

Do not accept an EIF answer unless it states:

- observed-data unit \(O\)
- target parameter as a population-level functional
- identification assumptions, when needed
- observed-data functional
- statistical model
- regularity/pathwise differentiability status
- nuisance functions
- likelihood factorization
- score decomposition
- pathwise derivative argument
- final candidate IF / valid IF / EIF, or reason no standard EIF exists
- mean-zero verification
- pathwise derivative identity check
- positivity/support warnings
- projection status for restricted models

---

## Repository Layout

```text
eif_toolkit/
  README.md
  VERSION.md
  CHANGELOG.md
  MANUAL.md
  TRIAL_GUIDE.md
  AGENTS.md

  agent/
    eif_agent_task_spec.md
    eif_latex_problem_protocol.md
    eif_target_triage.md
    eif_research_problem_protocol.md
    eif_hard_problem_protocol.md
    eif_answer_rubric.md
    eif_validation_tests.md
    eif_implementation_guide.md
    eif_danger_zone.md

  theory/
    semiparametric_influence_function_guide.md
    eif_projection_guide.md
    eif_restricted_moment_worked_derivation.md
    eif_plsim_worked_derivation.md
    eif_worked_derivations.md
    eif_references.md

  examples/
    eif_workflow_examples.md
    eif_examples.md
    eif_formula_registry.yaml
    eif_benchmark_tasks.md
    eif_hard_benchmark_tasks.md

  simulations/
    eif_simulation_tests.md

  problems/
    latex_inbox/
```
