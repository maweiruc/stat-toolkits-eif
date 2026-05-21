# EIF workflow examples

This file gives copy-paste examples for using the EIF toolkit. The examples are written as prompts to an agent.

---

## Example 1: Standard ATE

### Prompt

```text
Please use the EIF toolkit.

Observed data:
O=(Y,A,X), where A is binary.

Scientific target:
psi = E[Y(1)-Y(0)].

Assumptions:
consistency, conditional exchangeability (Y(1),Y(0)) independent of A given X,
and positivity 0 < P(A=1|X) < 1.

Model:
fully nonparametric observed-data model.

Derive the EIF. No Python code needed.
```

### Expected route

```text
Target triage:
causal g-formula / point-treatment ATE

Observed-data functional:
psi(P)=E[m_1(X)-m_0(X)]

Nuisances:
m_a(X)=E(Y|A=a,X), e(X)=P(A=1|X)

EIF:
A/e(X){Y-m_1(X)}
-
(1-A)/(1-e(X)){Y-m_0(X)}
+
m_1(X)-m_0(X)-psi
```

The answer should verify mean zero and explain why \(p(a\mid x)\) has no direct target derivative for the usual ATE, though \(e(X)\) appears in the observed-data representer.

---

## Example 2: LaTeX missing-data mean

### Prompt

```text
Please use the EIF toolkit and first normalize the LaTeX problem.

We observe
\[
O=(X,R,RY),
\]
where \(R=1\) means \(Y\) is observed. The target is
\[
\psi=E(Y).
\]
Assume
\[
Y \perp R \mid X,\qquad \pi(X)=P(R=1\mid X)>0.
\]
Derive the EIF under the nonparametric observed-data model.
```

### Expected route

```text
Target triage:
observed-data coarsening / missing-data mean

Observed-data functional:
psi(P)=E[m(X)], m(X)=E(Y|X)

Nuisances:
m(X), pi(X)

EIF:
R/pi(X) {Y-m(X)} + m(X) - psi
```

The answer should reduce to \(Y-\psi\) when \(R=1\) and \(\pi(X)=1\).

---

## Example 3: Nonregular pointwise CATE

### Prompt

```text
Please use hard mode.

Observed data:
O=(Y,A,X), A binary, X continuous.

Target:
\[
\tau(x_0)=E[Y(1)-Y(0)\mid X=x_0].
\]

Assume consistency, exchangeability, and positivity.
Derive the EIF if it exists. If no standard EIF exists, explain why and propose a regular alternative.
```

### Expected route

```text
Target triage:
conditional point target / nonregular in fully nonparametric model

Conclusion:
No standard root-n EIF exists under the fully nonparametric model because P(X=x0)=0 for continuous X.

Regular alternatives:
- fixed subgroup ATE E[Y(1)-Y(0)|X in G], P(X in G)>0
- smoothed CATE with fixed bandwidth
- parametric or semiparametric model for tau(x)
```

The correct answer should not write the subgroup EIF with \(G=I(X=x_0)\).

---

## Example 4: Smoothed CATE as a regularized target

### Prompt

```text
Please use research mode if needed.

Observed data:
O=(Y,A,X), A binary, X continuous.

For fixed bandwidth h and fixed kernel K_h, define
\[
\psi_h =
\frac{
E[K_h(X-x_0)\{m_1(X)-m_0(X)\}]
}{
E[K_h(X-x_0)]
},
\]
where \(m_a(X)=E(Y\mid A=a,X)\).

Assume consistency, exchangeability, positivity, and fixed h.
Derive the IF/EIF under the nonparametric observed-data model.
```

### Expected route

```text
Target triage:
ratio target built from weighted ATE primitives

Let:
alpha = E[K_h(X-x0){m_1(X)-m_0(X)}]
beta = E[K_h(X-x0)]
psi_h = alpha / beta

Derive D_alpha and D_beta, then:
D_psi = (D_alpha - psi_h D_beta) / beta
```

The answer should state that fixed \(h\) is regular under conditions, while \(h\to0\) requires nonstandard smoothing-rate analysis.

---

## Example 5: Restricted treatment model

### Prompt

```text
Please use the EIF toolkit and pay attention to restricted-model efficiency.

Observed data:
O=(Y,A,X), A binary.

Target:
psi=E[Y(1)-Y(0)].

Assumptions:
consistency, exchangeability, positivity.

Restricted model:
P(A=1|X)=expit(gamma^T X), with finite-dimensional unknown gamma.

Question:
Derive the full nonparametric IF and discuss whether it is the EIF under the restricted model.
If a projection is required, state the tangent space issue clearly.
```

### Expected route

```text
Target triage:
causal ATE + restricted semiparametric model / projection route

Expected behavior:
- derive or state the full nonparametric ATE IF
- identify treatment-mechanism tangent space span of score_gamma
- check whether projection changes the full IF
- do not call the full IF the restricted-model EIF unless projection is verified
```

This example tests whether the agent distinguishes full-model IF from restricted-model EIF.

---

## Example 6: Research problem with nuisance-dependent weights

### Prompt

```text
Please use research mode. This target may not have a registry formula.

Observed data:
O=(Y,A,X), A binary.

Let
\[
m_a(X)=E(Y\mid A=a,X), \qquad e(X)=P(A=1\mid X).
\]

Define a nuisance-dependent weighted treatment effect
\[
\psi(P)=
\frac{
E[w(e(X))\{m_1(X)-m_0(X)\}]
}{
E[w(e(X))]
},
\]
where \(w(u)=u(1-u)\).

Assume consistency, exchangeability, and positivity.
Derive a candidate IF/EIF under the nonparametric observed-data model.
Clearly separate proved steps from candidate or unresolved steps.
```

### Expected route

```text
Target triage:
ratio target with nuisance-dependent weights / research mode

Important:
w(e(X)) depends on P through e(X), so the derivative of the treatment mechanism may contribute.
Do not use the fixed-weight subgroup/weighted ATE formula unless w is treated as fixed.

Research output should include:
- assumption ledger
- derivative of numerator
- derivative of denominator
- treatment-mechanism score contribution
- candidate representer
- mean-zero and score identity checks
- unresolved steps if the projection/verification is incomplete
```

This is the kind of problem where analogy with ordinary weighted ATE can be wrong.

---

## Example 7: Survival with right censoring

### Prompt

```text
Please use hard mode.

Observed data:
\[
O=(\tilde T,\Delta,X),\quad \tilde T=\min(T,C),\quad \Delta=I(T\le C).
\]

Target:
\[
\psi=P(T>t).
\]

Assume independent censoring given X and appropriate positivity.
Derive the EIF, or explain what additional censoring-model specification is needed.
```

### Expected route

```text
Target triage:
censoring/survival problem

Expected behavior:
- do not use I(tilde T > t)-psi as if T were fully observed
- state whether using status-at-t MAR representation or full right-censoring counting-process representation
- specify censoring assumptions and filtration
- avoid claiming full efficiency unless the censoring model matches the derivation
```

---

## Example 8: Minimal research-mode request template

Use this when you are unsure how to state the problem:

```text
Please use EIF research mode.

Here is my proposed target:
[paste LaTeX]

Please do not jump to a formula. First:
1. parse the notation
2. state observed data and target
3. state what assumptions are needed for identification
4. state whether the target seems pathwise differentiable
5. propose a derivation route
6. then derive a candidate IF/EIF if possible
7. clearly mark unresolved steps
```

