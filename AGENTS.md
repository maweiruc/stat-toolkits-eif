# Agent instructions for the EIF toolkit

This repository is a documentation-first toolkit for deriving, validating, and implementing efficient influence functions (EIFs). It is not primarily a Python package yet. Treat the files in `agent/`, `theory/`, `examples/`, and `simulations/` as the working system.

## First files to read

For any EIF task, read these files first:

1. `agent/eif_agent_task_spec.md`
2. `agent/eif_latex_problem_protocol.md`
3. `agent/eif_target_triage.md`
4. `agent/eif_research_problem_protocol.md`
5. `agent/eif_hard_problem_protocol.md`
6. `agent/eif_answer_rubric.md`
7. `theory/semiparametric_influence_function_guide.md`
8. `theory/eif_projection_guide.md`
9. `agent/eif_danger_zone.md`
10. `examples/eif_examples.md`
11. `agent/eif_validation_tests.md`
12. `agent/eif_implementation_guide.md`

Use `examples/eif_formula_registry.yaml` only after checking that the observed data, target, model, assumptions, nuisance definitions, and positivity conditions match.

For self-testing or evaluation, use both `examples/eif_benchmark_tasks.md` and `examples/eif_hard_benchmark_tasks.md`.

## Default workflow

When the user gives a problem, especially in LaTeX:

1. Normalize the problem statement.
2. Assign a target triage label.
3. State the observed-data unit \(O\).
4. Separate the scientific target from the observed-data functional.
5. State identification assumptions.
6. State the statistical model.
7. Check pathwise differentiability.
8. Check whether the model is fully nonparametric or restricted.
9. Identify nuisance functions and positivity conditions.
10. Factorize the likelihood and decompose the score.
11. Derive the IF/EIF component by component.
12. Verify mean zero and the pathwise derivative identity.
13. Check special-case reductions.
14. Provide estimator, standard error, and validation code only when requested or useful.

## LaTeX inbox behavior

When the user asks to process a LaTeX problem under `problems/latex_inbox/problem_*/problem.tex`, check whether `notes.md` exists in the same folder.

If `notes.md` does not exist, create it automatically before derivation. The generated notes should include:

1. observed data
2. target
3. model / assumptions
4. target triage route
5. preferred mode: fast / hard / research
6. nuisance functions
7. possible danger zones
8. planned derivation route

If `notes.md` already exists, read it and treat it as user/context guidance. Do not overwrite existing notes unless the user asks.

## Research problems

If no exact formula is available, switch to research mode. Build the derivation from first principles using `agent/eif_research_problem_protocol.md`.

Research mode is a maximum-effort mode, not permission to stop at the first plausible intermediate result. After finding a candidate IF/EIF, keep working through the verification and projection steps whenever a next mathematical step is identifiable.

Do not stop at `candidate IF/EIF`, `projection unresolved`, or `full-model IF only` until you have tried the relevant escalation steps: verify all score components, formulate the projection or normal equations, try to solve them, check special cases, and consider operator or implicit-function forms. If the derivation still cannot be completed, include a short obstruction ledger describing what was tried and exactly where the argument fails.

In research mode, clearly label the result as one of:

- derived and verified under stated assumptions
- candidate IF/EIF with unresolved verification
- full-model IF only, projection unresolved
- identified but differentiability unclear
- unidentified
- nonregular

Do not overclaim efficiency for a novel target until the pathwise derivative identity and tangent-space projection have been checked.

## Hard problems

Use hard-problem mode when the target involves:

- censoring or coarsening
- missing data
- longitudinal treatment regimes
- continuous treatments
- mediation
- transportability
- IV or ratio targets
- quantiles
- optimal or learned treatment rules
- density at a point
- pointwise CATE with continuous covariates
- argmax, maximum, threshold, boundary, or post-selection targets
- restricted semiparametric models

In hard mode, do not use the registry as the source of truth. Build a component ledger:

```text
Likelihood component | Score | Mean-zero restriction | Target depends on it? | Derivative | IF component
```

## Failure is allowed

Do not force an EIF. If the target is unidentified or not pathwise differentiable under the stated model, say so clearly and suggest a regular alternative when possible.

If a full nonparametric influence function is derived but the user asked for efficiency under a restricted model, do not call it the EIF unless the tangent-space projection has been performed.
