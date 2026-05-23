# EIF agent task specification

This document defines a standard protocol for a coding agent that derives and implements efficient influence functions (EIFs).

The goal is to prevent the agent from simply copying a familiar formula. The agent must first classify the statistical problem, state the target, verify regularity, derive or retrieve the correct EIF, and then implement and validate it.

---

## 1. Required input from the user

For every EIF task, the agent should ask for or infer the following information.

### 1.1 Observed data structure

Specify the observed data unit:

\[
O = \text{[fill in]}
\]

Examples:

\[
O=Y,
\]

\[
O=(R,RY,X),
\]

\[
O=(Y,A,X),
\]

\[
O=(L_0,A_0,L_1,A_1,\ldots,L_K,A_K,Y).
\]

The agent must identify which variables are observed and which are counterfactual or latent.

---

### 1.2 Target parameter

Specify the target parameter:

\[
\psi(P)=\text{[fill in]}.
\]

Examples:

\[
\psi=E(Y),
\]

\[
\psi=E\{Y(1)-Y(0)\},
\]

\[
\psi=P\{Y(a)\le t\},
\]

\[
\psi=E\{Y^d\}.
\]

The target must be a population-level functional, not an estimator.

---

### 1.3 Statistical model

Specify the model:

- [ ] Fully nonparametric model
- [ ] Semiparametric model
- [ ] Restricted model with parametric or structural constraints
- [ ] Causal model
- [ ] Missing-data model
- [ ] Censoring / survival model
- [ ] Longitudinal treatment model
- [ ] Instrumental-variable model
- [ ] Other

The agent must state whether the proposed EIF is for the full nonparametric observed-data model or for a restricted semiparametric model.

---

### 1.4 Identification assumptions

List assumptions needed to identify the target from observed data.

Examples:

For missing data:

\[
Y\perp R\mid X,
\]

\[
P(R=1\mid X)>0.
\]

For point-treatment causal inference:

\[
Y=AY(1)+(1-A)Y(0),
\]

\[
(Y(1),Y(0))\perp A\mid X,
\]

\[
0<c<P(A=1\mid X)<1-c.
\]

For longitudinal treatment:

\[
Y^d \perp A_t \mid H_t
\]

for each treatment time \(t\), together with sequential positivity.

---

### 1.5 Desired output

The agent should output:

1. Observed-data structure
2. Target parameter
3. Identification formula
4. Nuisance functions
5. Likelihood factorization
6. Score decomposition
7. Pathwise derivative derivation
8. Final EIF
9. Mean-zero verification
10. Estimator or pseudo-outcome when implementation is requested
11. Numerical validation tests
12. Warnings or limitations

---

## 2. Problem classification

Before deriving an EIF, the agent must classify the task.

If the task is given in free-form prose or LaTeX, first apply:

```text
eif_latex_problem_protocol.md
```

Then assign a target triage route using:

```text
eif_target_triage.md
```

If the target is novel or not covered by known formulas, use:

```text
eif_research_problem_protocol.md
```

If the task is unfamiliar, ambiguous, restricted, longitudinal, censored, optimization-based, or potentially nonregular, use:

```text
eif_hard_problem_protocol.md
```

The final answer should be checked against:

```text
eif_answer_rubric.md
```

### 2.1 Full-data smooth functional

Examples:

\[
E(Y),\quad
E\{g(Y)\},\quad
P(Y\le t),\quad
\operatorname{Var}(Y).
\]

Usually the EIF is simple:

\[
h(O)-E\{h(O)\}.
\]

---

### 2.2 Ratio or transformation of simpler functionals

Examples:

\[
\frac{E(Y)}{E(Z)},
\]

\[
\log E(Y),
\]

\[
\log \frac{\mu_1}{\mu_0}.
\]

Use the delta method.

If

\[
\psi=\frac{\alpha}{\beta},
\]

then

\[
D_\psi
=
\frac{D_\alpha-\psi D_\beta}{\beta}.
\]

---

### 2.3 Missing-data problem

Example:

\[
O=(R,RY,X),
\]

\[
Y\perp R\mid X.
\]

Typical EIF structure:

\[
\frac{R}{\pi(X)}\{Y-m(X)\}+m(X)-\psi.
\]

---

### 2.4 Point-treatment causal problem

Example:

\[
O=(Y,A,X).
\]

Typical EIF structure:

\[
\frac{I(A=a)}{P(A=a\mid X)}
\{Y-m_a(X)\}
+
m_a(X)-\mu_a.
\]

ATE is obtained by differencing the two mean-potential-outcome EIFs.

---

### 2.5 Longitudinal treatment regime

Example:

\[
O=(L_0,A_0,L_1,A_1,\ldots,L_K,A_K,Y).
\]

Typical EIF structure:

\[
\sum_{t=0}^K
W_t^d
\{Q_{t+1}-Q_t\}
+
Q_0-\psi_d.
\]

---

### 2.6 Censoring / survival problem

The agent must distinguish:

1. No censoring
2. Status-at-\(t\) missing-data representation
3. Full right-censoring counting-process representation

Survival EIFs can be more delicate than ATE EIFs. The agent should explicitly state which censoring model is being used.

---

### 2.7 Restricted semiparametric model

If the model imposes constraints, the agent must not automatically use the full nonparametric EIF.

The agent should state:

\[
D_{\text{EIF}}
=
\Pi_{\mathcal T}D_{\text{full}},
\]

where \(\mathcal T\) is the tangent space of the restricted model.

For projection details, use:

```text
theory/eif_projection_guide.md
```

If projection is not derived, the agent should say so.

---

### 2.8 Potentially nonregular target

The agent should flag targets such as:

\[
p_Y(y_0),
\]

\[
E\{Y(1)-Y(0)\mid X=x\}
\]

for continuous \(X\),

\[
\max_x m(x),
\]

\[
\arg\max_x m(x),
\]

optimal treatment rule value without margin conditions,

parameters involving unknown change points or boundaries.

The agent must not force a standard EIF for a nonregular target.

---

## 3. Required derivation protocol

The agent must follow this procedure.

### Step 0: Normalize the problem and pass hard gates

Before deriving, write a normalized problem specification:

```text
Observed data:
O = ...

Scientific target:
...

Observed-data functional:
...

Model:
...

Identification assumptions:
...

Regularity status:
...

Target triage route:
...

Research status if no known formula applies:
derived and verified / candidate IF / valid IF but not EIF /
projection unresolved / differentiability unclear / unidentified / nonregular
```

Then check:

1. Is the target identified from the observed-data law?
2. Is the target pathwise differentiable under the stated model?
3. Is the requested EIF for the full nonparametric model or a restricted model?
4. Are all positivity, support, density, and denominator conditions stated?
5. Does the problem trigger any danger-zone case?

If the target fails identification or pathwise differentiability, the agent should stop and explain the failure rather than forcing an EIF.

### Step 1: Write the target as an observed-data functional

For example, for ATE:

\[
\psi
=
E\{m_1(X)-m_0(X)\}.
\]

For missing-data mean:

\[
\psi
=
E\{m(X)\}.
\]

For policy value:

\[
\psi_d
=
E\{m_d(X)\}.
\]

---

### Step 2: Identify nuisance functions

Examples:

For ATE:

\[
m_a(X)=E(Y\mid A=a,X),
\]

\[
e(X)=P(A=1\mid X).
\]

For missing-data mean:

\[
m(X)=E(Y\mid X),
\]

\[
\pi(X)=P(R=1\mid X).
\]

For longitudinal regime:

\[
g_t(H_t)=P(A_t=d_t(H_t)\mid H_t),
\]

\[
Q_t(H_t)=E\{Q_{t+1}\mid H_t,A_t=d_t(H_t)\}.
\]

---

### Step 3: Factorize the likelihood

For ATE:

\[
p(o)=p(y\mid a,x)p(a\mid x)p(x).
\]

For missing data:

\[
p(o)=p(y\mid x)^r p(r\mid x)p(x).
\]

For longitudinal treatment:

\[
p(o)=p(l_0)
\prod_{t=0}^K
p(a_t\mid h_t)p(l_{t+1}\mid h_t,a_t)
p(y\mid \bar l_K,\bar a_K).
\]

---

### Step 4: Decompose the score

For ATE:

\[
S(O)=S_Y(Y\mid A,X)+S_A(A\mid X)+S_X(X).
\]

For each score component, state its conditional mean-zero property, such as:

\[
E\{S_Y\mid A,X\}=0.
\]

---

### Step 5: Compute the pathwise derivative component by component

For each likelihood component:

1. Perturb only that component.
2. Compute the derivative of the target.
3. Rewrite the derivative as an inner product:

\[
E\{\phi_j(O)S_j(O)\}.
\]

4. Extract \(\phi_j(O)\).

For hard problems, use a component ledger:

```text
Likelihood component | Score | Mean-zero restriction | Target depends on it? | Derivative | IF component
```

---

### Step 6: Sum components and center

\[
D_\psi(O)=\sum_j \phi_j(O).
\]

Check:

\[
E\{D_\psi(O)\}=0.
\]

If not centered, subtract the expectation.

---

### Step 7: If restricted model, project

If the model is restricted, use:

\[
D_{\text{EIF}}
=
\Pi_{\mathcal T}D_{\text{full}}.
\]

If the projection is not available, state:

```text
The full nonparametric EIF is derived, but the restricted-model EIF requires projection onto the model tangent space.
```

---

## 4. Required implementation protocol

The agent should implement the EIF-based estimator as follows.

### 4.1 Pseudo-outcome

Whenever possible, express the EIF as

\[
D_\psi(O;\eta,\psi)
=
D(O;\eta)-\psi.
\]

Then define:

\[
\hat\psi
=
\mathbb P_n D(O;\hat\eta).
\]

Estimated EIF:

\[
\hat D_{\psi,i}
=
D(O_i;\hat\eta)-\hat\psi.
\]

Standard error:

\[
\widehat{SE}
=
\frac{\operatorname{sd}(\hat D_{\psi,1},\ldots,\hat D_{\psi,n})}{\sqrt n}.
\]

---

### 4.2 Cross-fitting

If nuisance functions are estimated by flexible methods, use cross-fitting.

Algorithm:

```text
1. Split data into K folds.
2. For each fold k:
   a. Fit nuisance functions on all other folds.
   b. Predict nuisance functions on fold k.
3. Combine out-of-fold predictions.
4. Compute pseudo-outcomes.
5. Estimate psi by their sample mean.
6. Compute EIF values and standard error.
```

---

### 4.3 Positivity handling

If EIF includes inverse probabilities, the agent must:

1. Report the minimum and maximum of estimated probabilities.
2. Clip probabilities only as a numerical stabilization step.
3. Warn if heavy clipping is required.

Example:

```python
e_hat = np.clip(e_hat, eps, 1.0 - eps)
```

---

## 5. Required validation protocol

The agent must perform or outline the following checks:

1. Mean-zero check
2. Standard-error calculation
3. Special-case reduction
4. Finite-difference pathwise derivative check, when feasible
5. Orthogonality check, when using nuisance functions
6. Positivity diagnostics
7. Nonregular-target warning
8. Research-mode unresolved-step report, if applicable

---

## 6. Standard output template

The agent should output in this order:

```text
# EIF derivation result

## 1. Observed data

## 2. Target parameter

## 3. Target triage and derivation route

## 4. Identification assumptions

## 5. Model and regularity status

## 6. Observed-data functional

## 7. Nuisance functions

## 8. Likelihood factorization

## 9. Score decomposition

## 10. Component ledger for hard problems

## 11. Pathwise derivative

## 12. Candidate IF / valid IF / EIF / projection or nonregularity conclusion

## 13. Research status and unresolved steps, if applicable

## 14. Mean-zero verification

## 15. Pathwise derivative identity check

## 16. Estimator and implementation, if requested

## 17. Validation tests

## 18. Warnings and limitations
```

For `problems/latex_inbox/problem_*/` tasks, write this detailed output to `solution.md` in the problem folder and follow `agent/eif_problem_artifacts.md` for artifact rules.

---

## 7. Minimal prompt for a coding agent

```text
You are given a semiparametric target parameter. Derive its influence function or efficient influence function, and implement the estimator only if requested or useful.

Before deriving the EIF, normalize the problem and assign a target triage route. Then classify the problem as one of:
1. full-data smooth functional;
2. ratio or smooth transformation;
3. missing-data problem;
4. point-treatment causal problem;
5. longitudinal treatment regime;
6. survival or censoring problem;
7. restricted semiparametric model;
8. potentially nonregular target.

Then follow this protocol:
1. Define the observed data O.
2. State the target parameter psi(P).
3. Assign the target triage route.
4. State identification assumptions.
5. Express psi(P) as an observed-data functional.
6. Identify all nuisance functions.
7. Factorize the likelihood.
8. Decompose the score.
9. Use a component ledger for hard problems.
10. Compute the pathwise derivative for each likelihood component.
11. Rewrite each derivative as an inner product with the corresponding score.
12. Sum and center the IF components.
13. If the model is restricted, project onto the tangent space or state that projection is required.
14. Implement the estimator, EIF values, standard error, confidence interval, and validation checks only if requested or useful.
15. If the target is nonregular, do not force a standard EIF. Explain the issue and suggest a regularized or smoothed alternative.
```

---

## 8. Final checklist for the agent

Before returning the answer, the agent must confirm:

- [ ] The target is a population-level functional.
- [ ] The target triage route is stated.
- [ ] The observed-data functional is correctly identified.
- [ ] All nuisance functions are defined.
- [ ] Positivity assumptions are stated.
- [ ] The likelihood factorization matches the data structure.
- [ ] The score decomposition is stated.
- [ ] The EIF is mean-zero.
- [ ] The estimator solves the empirical EIF equation when appropriate.
- [ ] The standard error is based on the empirical EIF variance.
- [ ] Cross-fitting is used or explicitly discussed.
- [ ] Nonregularity is considered.
- [ ] Restricted-model projection is considered.
