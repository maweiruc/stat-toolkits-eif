# EIF toolkit trial guide

This guide is for someone trying the toolkit for the first time.

The shortest version:

```text
请读取 problems/latex_inbox/problem_XXX/problem.tex，
使用 EIF toolkit 的 research mode 推导 IF/EIF。
如果 notes.md 不存在，请先自动生成。
不要直接套公式；请尽最大努力给出最终 IF/EIF。
只有在识别、regularity、projection/operator inverse 真正卡住时才标 unresolved。
请明确区分 candidate IF、valid IF、EIF、projection unresolved 或 nonregular。
```

Replace `problem_XXX` with the folder you want to test.

---

## 1. What to Try First

### Trial A: Restricted moment model

Use:

```text
problems/latex_inbox/problem_001/problem.tex
```

This tests whether the agent can derive:

\[
S_{\mathrm{eff}}
=
\varepsilon\sigma^{-2}(X)\dot m_\beta(X)
\]

and distinguish raw score from efficient score.

Prompt:

```text
请读取 problems/latex_inbox/problem_001/problem.tex，
使用 EIF toolkit 的 research mode 推导 IF/EIF。
如果 notes.md 不存在，请先自动生成。
不要直接套公式；请尽最大努力给出最终 IF/EIF。
只有在识别、regularity、projection/operator inverse 真正卡住时才标 unresolved。
请明确区分 candidate IF、valid IF、EIF、projection unresolved 或 nonregular。
```

### Trial B: Partially linear single index model

Use:

```text
problems/latex_inbox/problem_002/problem.tex
```

This tests whether the agent can handle nuisance tangent spaces and projection for an unknown function \(g(Z^\top\alpha)\).

Prompt:

```text
请读取 problems/latex_inbox/problem_002/problem.tex，
使用 EIF toolkit 的 research mode 推导 IF/EIF。
如果 notes.md 不存在，请先自动生成。
不要直接套公式；请尽最大努力给出最终 IF/EIF。
只有在识别、regularity、projection/operator inverse 真正卡住时才标 unresolved。
请明确区分 candidate IF、valid IF、EIF、projection unresolved 或 nonregular。
```

### Trial C: Your own LaTeX problem

Put your LaTeX file here:

```text
problems/latex_inbox/problem_003/problem.tex
```

Do not create `notes.md` unless you want to add extra context. If `notes.md` is absent, the agent should generate it automatically.

Prompt:

```text
请读取 problems/latex_inbox/problem_003/problem.tex，
使用 EIF toolkit 的 research mode 推导 IF/EIF。
如果 notes.md 不存在，请先自动生成。
不要直接套公式；请尽最大努力给出最终 IF/EIF。
只有在识别、regularity、projection/operator inverse 真正卡住时才标 unresolved。
请明确区分 candidate IF、valid IF、EIF、projection unresolved 或 nonregular。
```

---

## 2. What Good Output Looks Like

A good answer should include:

1. normalized problem statement
2. symbol table
3. target triage route
4. assumptions and model restrictions
5. nuisance functions
6. likelihood factorization
7. tangent space or score decomposition
8. candidate IF / valid IF / efficient score / EIF
9. projection or orthogonality argument
10. final status

The final status should be one of:

```text
derived and verified under stated assumptions
candidate IF with unresolved verification
valid IF but efficiency/projection not completed
full-model IF only; projection unresolved
identified but pathwise differentiability unclear
unidentified
nonregular
```

---

## 3. Red Flags

Do not accept an answer if it:

- jumps directly to a familiar formula without normalizing the problem
- calls a raw score efficient without projection
- calls a full-model IF an EIF under a restricted model
- ignores identifiability constraints
- ignores nuisance tangent spaces
- gives an EIF for a nonregular target without explaining the regularization
- omits mean-zero or orthogonality checks
- stops at candidate IF or projection unresolved without attempting the visible verification/projection/operator next step

---

## 4. Feedback Template

When reporting trial feedback, use:

```text
Problem tested:

Was notes.md generated or read correctly?

Was the target normalized correctly?

Was the mode correct: fast / hard / research?

Did the derivation distinguish candidate IF, valid IF, efficient score, and EIF?

Were tangent spaces or projections handled correctly?

What was confusing?

What should be improved?
```
