# Contributing

Thanks for improving the EIF toolkit. This project is documentation-first: the
main contribution is a clearer, more auditable path from a statistical problem
to an IF/EIF, a nonregularity conclusion, or a precise unresolved obstruction.

## Contribution Types

Useful contributions include:

- new or corrected formula registry entries in `examples/eif_formula_registry.yaml`;
- benchmark tasks in `examples/`;
- worked derivations or theory cards in `theory/`;
- agent protocols, rubrics, or danger-zone checks in `agent/`;
- reusable simulation or validation notes in `simulations/`;
- worked inbox examples under `problems/latex_inbox/`.

## Formula Registry Entries

When adding or editing a registry entry:

1. Match the observed data, target, model, assumptions, and nuisance functions exactly.
2. Include `observed_data`, `target`, `warnings`, and either `eif` or `status`.
3. For regular EIF entries, include `nuisances` and `estimator`.
4. For nonregular or unidentified entries, include `status` and `recommendation`.
5. Add warnings for positivity, denominator, support, and restricted-model projection issues.

Run:

```bash
python3 scripts/validate_formula_registry.py --strict
python3 -m eif_toolkit.registry_validation --strict
python3 -m unittest discover -s tests
```

## Derivation Standard

An EIF contribution should not stop at a familiar formula. It should state:

```text
Observed data:
Target:
Identification assumptions:
Observed-data functional:
Likelihood factorization:
Score decomposition:
IF/EIF:
Mean-zero check:
Pathwise derivative check:
Special-case checks:
Warnings or unresolved steps:
```

For research-mode problems, follow `agent/eif_research_problem_protocol.md`.
Unresolved status should include the maximum-effort obstruction ledger.

## Sources and References

Public project files should cite papers, books, and lecture notes
bibliographically. Do not depend on private working files, generated parsing
outputs, or tool-specific local processing steps.

If you use a new source to improve the toolkit:

1. Add independently written summaries, derivations, examples, or cards.
2. Cite the source in `theory/eif_references.md` when useful.
3. Do not copy long passages.
4. Do not add private source files to the repository.

The `references/` folder is a private local workspace. Only
`references/README.md` should be tracked.

## Privacy and Hygiene

Before pushing publicly, check:

```bash
git status --short --ignored
git ls-files references
```

Expected behavior:

- only `references/README.md` is tracked under `references/`;
- local PDFs, notes, converted files, and private inbox folders stay ignored;
- no secrets, tokens, private paths, or personal data are committed.

## CI

GitHub Actions runs the registry validator and unit tests on pushes and pull
requests. Contributions should keep CI green.
