# EIF toolkit 使用手册

这个 toolkit 的目标不是让 agent 背公式，而是让它在半参数统计问题中稳定地完成：

```text
问题规范化 -> 目标分诊 -> 识别 -> regularity 检查 -> pathwise derivative -> IF/EIF -> 验证
```

尤其适合两类问题：

1. 标准问题：ATE、ATT、missing-data mean、ratio、quantile、longitudinal regime 等。
2. Research 问题：文献中没有现成 EIF，需要从 first principles 推导。

如果你是第一次试用或要让别人试用，先看 `TRIAL_GUIDE.md`。

---

## 1. 最简单的使用方式

日常最短 prompt：

```text
请读取 problems/latex_inbox/problem_XXX/problem.tex，
使用 EIF toolkit 的 research mode 推导 IF/EIF。
如果 notes.md 不存在，请先自动生成。
不要直接套公式；请尽最大努力给出最终 IF/EIF。
只有在识别、regularity、projection/operator inverse 真正卡住时才标 unresolved。
请明确区分 candidate IF、valid IF、EIF、projection unresolved 或 nonregular。
```

通常这几行就够了。详细规则已经写在 `AGENTS.md` 和 `agent/eif_research_problem_protocol.md` 里。

在一个新的 agent/chat 里，直接贴下面这段：

```text
Please use the EIF toolkit in this folder.

First read:
1. AGENTS.md
2. agent/eif_agent_task_spec.md
3. agent/eif_latex_problem_protocol.md
4. agent/eif_target_triage.md
5. agent/eif_research_problem_protocol.md
6. agent/eif_hard_problem_protocol.md
7. agent/eif_answer_rubric.md
8. theory/semiparametric_influence_function_guide.md
9. theory/eif_projection_guide.md
10. agent/eif_danger_zone.md
11. examples/eif_examples.md
12. agent/eif_validation_tests.md

Then solve the following EIF problem.

Observed data:
[fill in]

Target:
[fill in]

Model/assumptions:
[fill in]

Please return:
1. normalized problem statement
2. target triage route
3. identification formula
4. regularity status
5. nuisance functions
6. likelihood factorization
7. score decomposition
8. component ledger if needed
9. IF/EIF derivation
10. mean-zero and pathwise derivative checks
11. warnings, projection issues, or unresolved research steps
```

如果你只是想先推导，不想写代码，可以加：

```text
Do not implement code unless I ask for it.
```

---

## 2. 选择使用模式

### 2.1 Fast mode

用于标准题，且公式库里有精确匹配。

例子：

```text
Observed data O=(Y,A,X). Target psi=E[Y(1)-Y(0)].
Assume consistency, exchangeability, and positivity.
Derive the EIF under the nonparametric observed-data model.
```

Agent 应该先确认这是 ATE，然后可以用公式库作为 comparison。

### 2.2 Hard mode

用于容易套错公式的问题。

触发条件包括：

- ATT 但容易误用 ATE
- censoring/survival
- mediation
- continuous treatment
- longitudinal regime
- ratio denominator 可能弱
- quantile density 可能为 0
- restricted semiparametric model
- pointwise CATE / density at a point / argmax

Hard mode 要求 component ledger。

### 2.3 Research mode

用于没有现成公式的问题。重点不是快速给最终答案，而是建立可审查的 derivation record。

Research mode 要求 agent 尽最大努力解决问题。得到 candidate IF 或 representer 之后，不能立刻停止；必须继续检查所有 score components，必要时写出 projection/normal equations，并尝试 closed form、离散/有限维版本、特殊情形、reparameterization 或 operator/implicit-function 解法。只有这些步骤仍然卡住时，才可以标记 unresolved。

Research mode 输出必须标注状态：

```text
Status:
- derived and verified under stated assumptions
- candidate IF with unresolved verification
- valid IF but efficiency/projection not completed
- full-model IF only; projection unresolved
- identified but pathwise differentiability unclear
- unidentified
- nonregular
```

这对真正的研究问题很重要，因为有时正确答案不是一个公式，而是一个精确的数学障碍。

---

## 3. 你应该怎样写问题

最推荐的格式：

```text
Observed data:
O = ...

Scientific target:
...

Identification assumptions:
...

Statistical model:
...

Question:
Derive the IF/EIF. If no standard EIF exists, explain why.
```

如果是 causal problem，最好区分：

```text
Scientific target:
E[Y(1)-Y(0)]

Identification assumptions:
consistency, exchangeability, positivity

Observed-data model:
fully nonparametric model for O=(Y,A,X)
```

如果是 research problem，可以写：

```text
This may be a novel target. Please use research mode.
Do not rely on formula lookup. Build the derivation from first principles.
Make a maximum-effort attempt to get the final IF/EIF.
Only mark projection/operator inverse/verification unresolved after trying the next mathematical steps.
Clearly distinguish candidate IF, valid IF, EIF, projection unresolved, and nonregular conclusions.
```

如果你的问题来自 `problems/latex_inbox/problem_XXX/problem.tex`，你不需要自己写 `notes.md`。默认约定是：

```text
If notes.md does not exist, the agent first generates notes.md as a problem digest,
then uses it for the IF/EIF derivation.
```

自动生成的 `notes.md` 会包括 observed data、target、assumptions、triage route、preferred mode、nuisance functions、danger zones 和 planned derivation route。

---

## 4. Agent 应该如何回答

一个合格答案至少应该有：

```text
1. Observed data
2. Target parameter
3. Target triage and derivation route
4. Identification assumptions
5. Model and regularity status
6. Observed-data functional
7. Nuisance functions
8. Likelihood factorization
9. Score decomposition
10. Component ledger for hard/research problems
11. Pathwise derivative
12. candidate IF / valid IF / EIF / projection or nonregularity conclusion
13. Mean-zero verification
14. Pathwise derivative identity check
15. Special-case checks
16. Warnings and unresolved steps
```

对于 research problem，还应该有：

```text
Assumption ledger
Research derivation ledger
Efficiency status
Unresolved mathematical steps, if any
```

---

## 5. 什么时候不要接受答案

如果 agent 出现下面行为，不要接受：

- 没有写 observed-data functional 就直接给 EIF。
- 把 estimator 的 derivative 当作 influence function。
- 对 causal/missing/censored target 不写 identification assumptions。
- 对 restricted model 直接使用 full nonparametric EIF，却称为 efficient。
- 对 pointwise CATE、density at a point、argmax、optimal rule 硬套标准 EIF。
- 忘记 positivity、density denominator、ratio denominator。
- 没有 mean-zero check。
- 没有说明 pathwise derivative identity。
- 对 research problem 用“看起来像 ATE”之类的类比代替推导。
- 对 research problem 停在 candidate IF 或 projection unresolved，但没有尝试可见的 verification/projection/operator 下一步。

---

## 6. 常用 prompt 片段

### 6.1 要求严格模式

```text
Use hard/research mode. Do not use the registry as the source of truth.
Use it only as a comparison after deriving the result.
```

### 6.2 要求不要过度声称

```text
If the expression is only a candidate IF, label it as candidate.
If it is a valid IF but not yet efficient, label it as valid IF, not EIF.
If projection is unresolved, say so explicitly.
Do not call it an EIF unless efficiency has been verified under the stated model.
```

### 6.3 要求 component ledger

```text
Please include a component ledger:
Likelihood component | Score | Mean-zero restriction | Target depends on it? | Derivative | IF component
```

### 6.4 要求验证

```text
After deriving the EIF, verify:
1. mean zero
2. pathwise derivative identity
3. special-case reductions
4. positivity/support conditions
```

### 6.5 要求 research derivation

```text
This is a research target and may not appear in the literature.
Please use the research derivation ledger:
Step | Object | Result | Status | Notes
After a candidate IF or representer is found, keep going: verify all score components,
formulate and try to solve any projection/normal equations, and only then mark
unresolved with an obstruction ledger if the derivation still cannot be completed.
Separate assumptions, proved steps, candidate IF, valid IF, EIF, and unresolved steps.
```

---

## 7. 推荐阅读路径

如果你是使用者，不是 agent，建议按这个顺序读：

1. `MANUAL.md`
2. `examples/eif_workflow_examples.md`
3. `AGENTS.md`
4. `agent/eif_latex_problem_protocol.md`
5. `agent/eif_target_triage.md`
6. `agent/eif_research_problem_protocol.md`
7. `agent/eif_answer_rubric.md`
8. `theory/semiparametric_influence_function_guide.md`

如果你要处理 restricted model，再读：

```text
theory/eif_projection_guide.md
```

如果你要测试 agent 能力，再读：

```text
examples/eif_benchmark_tasks.md
examples/eif_hard_benchmark_tasks.md
```
