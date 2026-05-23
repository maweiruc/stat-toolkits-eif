# EIF research problem protocol

This document is for novel EIF problems where the target is not in the formula registry and may not be treated explicitly in the literature. These are not merely "trap" problems. They are research derivations: the agent must build the argument from first principles, expose assumptions, and separate proved steps from conjectural or unresolved steps.

Use this protocol when:

- the target is new or nonstandard;
- no exact registry or reference formula applies;
- the estimand is defined by nested counterfactuals, stochastic interventions, transport maps, adaptive rules, constraints, or implicit equations;
- the statistical model has unusual restrictions;
- the user asks for a derivation rather than formula retrieval;
- correctness depends on tangent-space, operator, or identification arguments.

---

## 1. Research-mode principle

In research mode, the output is a derivation record, not just an EIF formula.

Research mode is maximum-effort mode. A candidate IF, unresolved projection, or full-model IF is not an acceptable stopping point if the next mathematical step is clear enough to attempt. The agent should push toward a final IF/EIF, or toward a precise impossibility / nonregularity / unidentified conclusion.

The agent must make clear which status applies:

```text
Status:
- Derived and verified under stated assumptions
- Candidate IF requiring one unresolved verification step
- Valid IF but efficiency/projection not completed
- Full-model IF only; restricted-model projection unresolved
- Identified but pathwise differentiability unclear
- Not identified under stated assumptions
- Nonregular under stated model
```

Do not present a candidate expression as a final EIF until the pathwise derivative identity has been checked against all allowed scores.

Do not present an unresolved status until the maximum-effort loop in Section 2 has been attempted or the obstruction is immediate and fundamental.

---

## 2. Maximum-effort loop before unresolved status

After deriving a candidate representer, the agent must try the following escalation steps before reporting `candidate`, `projection unresolved`, or `full-model IF only`:

1. Verify mean zero and the pathwise derivative identity against every score component.
2. If the model is restricted, write the tangent-space projection problem explicitly.
3. Formulate the projection as normal equations, constrained least squares, an adjoint equation, or an operator inverse.
4. Try to solve the projection. If a closed form is hard, try finite-dimensional or discrete support versions, special cases, reparameterizations, and implicit-function differentiation.
5. Check whether special cases reduce to known EIFs or reveal missing components.
6. If the solution still cannot be completed, give an obstruction ledger:

```text
Attempted step | What was derived | Why it does not complete the EIF
---------------|------------------|----------------------------------
Score check | ... | ...
Projection equations | ... | ...
Closed-form solve | ... | ...
Special cases | ... | ...
```

Stopping with `unresolved` is valid only when this ledger identifies a real mathematical obstacle: nonidentification, nonregularity, missing model specification, non-invertible operator, unverified completeness, or a projection equation the agent cannot solve.

---

## 3. Research derivation ledger

Every research-mode derivation should maintain this ledger:

```text
Step | Object | Result | Status | Notes
-----|--------|--------|--------|------
1 | Observed law P | ... | fixed | ...
2 | Full-data/scientific target | ... | fixed | ...
3 | Identification map | ... | proved/assumed/open | ...
4 | Observed-data functional psi(P) | ... | fixed | ...
5 | Model tangent space T | ... | proved/assumed/open | ...
6 | Pathwise derivative dot psi_P(S) | ... | derived/open | ...
7 | Candidate representer D | ... | candidate | ...
8 | Mean-zero check | ... | pass/fail/open | ...
9 | Score identity E[D S]=dot psi(S) | ... | pass/fail/open | ...
10 | Efficiency/projection | ... | pass/open | ...
11 | Maximum-effort escalation | ... | attempted/not needed | ...
12 | Special-case reductions | ... | pass/fail/open | ...
```

The ledger should be concise, but it must distinguish what has been shown from what is assumed.

---

## 4. Formalization phase

Before differentiating, define:

```text
Observed data:
O = ...

Dominating measure / density notation:
p(o) = ...

Scientific target:
...

Observed-data target after identification:
psi(P) = ...

Statistical model:
...

Tangent space:
...

Regularity assumptions:
...
```

For causal or missing-data targets, the identification map is part of the research problem. Do not skip it.

---

## 5. Assumption ledger

Research problems often require assumptions not present in the original prompt. Track them explicitly.

```text
Assumption | Type | Needed for | Can be weakened?
-----------|------|------------|----------------
Consistency | identification | causal target | no
Exchangeability | identification | g-formula | maybe
Positivity | regularity | inverse weights | maybe
Smooth density | differentiability | quantile/density target | maybe
Unique optimizer | regularity | argmax/value target | maybe
Bounded weights | asymptotics | EIF variance | maybe
```

Separate:

- identification assumptions
- pathwise differentiability assumptions
- efficiency/model assumptions
- implementation/asymptotic assumptions

---

## 6. Pathwise differentiability program

To show pathwise differentiability:

1. Choose an arbitrary regular parametric submodel \(P_\varepsilon\) through \(P\).
2. Write its score decomposition according to the likelihood factorization.
3. Differentiate \(\psi(P_\varepsilon)\) at \(\varepsilon=0\).
4. Show the derivative is a continuous linear functional of the score.
5. Find its Riesz representer in the model tangent space.

If step 4 fails, the target may be nonregular. If the derivative exists only under special submodels, that is not enough.

---

## 7. Operator and adjoint viewpoint

For novel targets, it is often useful to write the derivative as an operator equation.

If

\[
\dot\psi_P(S)=L(S),
\]

then the IF is \(D\) satisfying

\[
L(S)=E\{D(O)S(O)\}
\]

for every allowed score \(S\).

Common adjoint identities:

### 7.1 Marginal law component

If \(S_X(X)\) is a marginal score with \(E(S_X)=0\), then

\[
E\{a(X)S_X(X)\}
=
E\{[a(X)-E(a(X))]S_X(X)\}.
\]

Representer:

\[
a(X)-E\{a(X)\}.
\]

### 7.2 Conditional outcome-law component

If \(S_Y(Y\mid A,X)\) satisfies \(E(S_Y\mid A,X)=0\), and the derivative contains

\[
E_X\left[\int b(y,a,x)S_Y(y\mid a,x)p(y\mid a,x)dy\right],
\]

then rewrite it as an observed-data inner product using weights that map from the target intervention distribution to the observed conditional law.

For point treatment, this often creates factors such as:

\[
\frac{I(A=a)}{P(A=a\mid X)}.
\]

For continuous treatments or stochastic interventions, it often creates density ratios such as:

\[
\frac{g^\star(A\mid X)}{g(A\mid X)}.
\]

### 7.3 Coarsening component

If a full-data residual is observed only when \(R=1\), the adjoint often creates:

\[
\frac{R}{\pi(X)}
\]

where \(\pi(X)=P(R=1\mid X)\). The exact conditioning set depends on the coarsening model.

### 7.4 Restricted tangent-space component

If allowed scores lie in a smaller tangent space \(\mathcal T\), solve

\[
D_{\mathrm{EIF}}=\Pi_{\mathcal T}D_{\mathrm{full}}.
\]

Do not assume the full-model representer is efficient.

---

## 8. Candidate construction strategies

Use these strategies when no formula is available.

### 8.1 Decompose the target

Write the target as a composition:

\[
\psi(P)=h(\theta(P)).
\]

Derive primitive IFs first, then apply the chain rule.

### 8.2 Use recursive nuisance maps

For longitudinal or nested targets, define sequential regressions or bridge functions. Then differentiate the recursion from the last stage backward.

### 8.3 Use implicit-function differentiation

If the target \(\beta(P)\) solves

\[
\Psi(P,\beta)=0,
\]

then

\[
D_\beta
=
-
\left[
\frac{\partial}{\partial\beta}\Psi(P,\beta)
\right]^{-1}
D_{\Psi(\cdot,\beta)}.
\]

This covers many M-estimators, optimality conditions, and parameters defined by estimating equations.

### 8.4 Use ratio normalization

If the target is a weighted mean

\[
\psi=\frac{E\{W_P(O)H_P(O)\}}{E\{W_P(O)\}},
\]

check whether \(W_P\) and \(H_P\) depend on \(P\). If they do, their derivatives must be included. Do not use the fixed-weight ratio IF unless the weights are fixed.

### 8.5 Derive bridge equations

If identification uses bridge functions, proximal causal assumptions, calibration equations, or conditional moment restrictions, first derive the IF of the bridge function or the moment solution. This often becomes an operator inverse problem.

State when the inverse operator exists and whether the candidate depends on completeness, uniqueness, or boundedness assumptions.

---

## 9. Verification beyond formula matching

For research problems, formula matching is weak evidence. Verification should include:

1. Mean-zero proof.
2. Pathwise derivative identity for arbitrary scores in each tangent component.
3. Orthogonality to nuisance tangent components when claiming efficiency.
4. Special-case reductions to known EIFs.
5. Degenerate-case checks, such as no missingness, no censoring, randomized treatment, no covariates, fixed weights, or identity intervention.
6. Dimensional and support checks for all weights and densities.
7. Numerical finite-difference checks in simulated submodels when feasible.

---

## 10. Research-mode answer skeleton

```text
# Research EIF derivation

## 1. Problem normalization

## 2. Target triage

## 3. Identification map

## 4. Model and tangent space

## 5. Assumption ledger

## 6. Pathwise differentiability analysis

## 7. Derivative-by-component ledger

## 8. Candidate IF / Valid IF / EIF

## 9. Verification

## 10. Special-case reductions

## 11. Efficiency status

## 12. Maximum-effort escalation attempts

## 13. Remaining open steps or caveats

## 14. Implementation sketch, if requested
```

---

## 11. Safe research language

Use:

```text
candidate IF
valid IF but not efficient
full-model IF
observed-data gradient
efficient gradient under the stated model
projection remains unresolved
pathwise differentiability remains to be shown
```

Avoid:

```text
obviously the EIF is ...
by analogy with ATE ...
this should be efficient ...
```

unless the identity has actually been checked.

---

## 12. When to stop

Stop and report partial progress if:

- the target cannot be identified from observed data;
- the derivative is not continuous in the model tangent norm;
- the tangent space is not specified enough to define efficiency;
- an operator inverse is required but existence/uniqueness is unknown;
- the candidate representer cannot be verified against all score components.

Before stopping for an unresolved projection or candidate IF, include the maximum-effort obstruction ledger from Section 2. Stopping with a precise unresolved mathematical obstacle is a valid research output; stopping at the first intermediate answer is not.
