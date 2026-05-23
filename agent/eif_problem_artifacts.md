# EIF problem artifact conventions

This file is the canonical specification for files inside
`problems/latex_inbox/problem_*/`.

The goal is to keep the problem intake, derivation output, and optional export
artifacts separate.

## 1. Standard files

Recommended layout:

```text
problem.tex
notes.md
solution.md
solution.tex
solution.pdf
```

### `problem.tex`

User-supplied problem statement. This is the source of truth for the problem.

It may contain a complete LaTeX document, a paper excerpt, or a smaller LaTeX
fragment. The agent should normalize it before deriving an IF/EIF.

### `notes.md`

Optional intake brief. If absent, generate it before derivation. If present,
read it as context guidance. Do not overwrite an existing `notes.md` unless the
user asks.

`notes.md` should include:

1. observed data
2. target
3. model / assumptions
4. target triage route
5. preferred mode: fast / hard / research
6. nuisance functions
7. possible danger zones
8. planned derivation route

`notes.md` is not the final answer. It should not contain a full solution
unless the user intentionally put extra context there.

### `solution.md`

Durable derivation output. After deriving a LaTeX inbox problem, always create
or update `solution.md` in the same folder.

`solution.md` should be detailed enough to audit the derivation without relying
on the chat transcript. It should include:

1. normalized problem
2. identification and assumptions
3. nuisance functions
4. likelihood and tangent/score decomposition
5. candidate IF, valid IF, EIF/projection/nonregular status
6. verification checks
7. obstruction ledger if unresolved

If `solution.md` already exists and the user asks to rerun or derive again,
update it with the new derivation.

The chat response should summarize the conclusion and point to `solution.md`.

### `solution.tex`

Optional LaTeX export. Generate it only when the user explicitly asks for LaTeX
output. It may be created from `solution.md` or directly from the current
derivation.

### `solution.pdf`

Optional compiled PDF. Generate it only when the user explicitly asks for PDF
output. Compile it from `solution.tex`.

If PDF compilation fails, keep `solution.tex` and report the compile error.

## 2. Minimal prompt reminder

For LaTeX inbox problems, prompts should include:

```text
如果 notes.md 不存在，请先自动生成。
请将详细推导保存到同目录 solution.md。
```

## 3. Status labels for `solution.md`

Research-mode `solution.md` files should clearly label the result as one of:

```text
derived and verified under stated assumptions
candidate IF with unresolved verification
valid IF but efficiency/projection not completed
full-model IF only; projection unresolved
identified but pathwise differentiability unclear
unidentified
nonregular
```

Do not call an expression an EIF unless the relevant pathwise derivative and
tangent-space projection checks have been completed.
