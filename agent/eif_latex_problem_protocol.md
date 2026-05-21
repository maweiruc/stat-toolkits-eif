# EIF LaTeX problem intake protocol

This document defines how a coding agent should handle EIF questions that arrive as free-form prose or LaTeX. The goal is to translate the problem into a derivation-ready statistical specification before attempting any formula lookup or derivation.

The intake step is not cosmetic. For hard EIF problems, most mistakes happen before calculus starts: the agent misreads the observed data, silently adds assumptions, treats an estimator as the target, or confuses a full-data causal parameter with its observed-data identification formula.

---

## 1. Intake principle

Given a LaTeX problem statement, the agent must first produce a normalized problem specification:

```text
Original target:
[quote or restate the target exactly]

Observed data:
O = ...

Latent, missing, or counterfactual variables:
...

Statistical model:
...

Identification assumptions:
...

Target as a full-data or causal estimand:
...

Target as an observed-data functional:
...

Nuisance functions:
...

Support and positivity assumptions:
...

Regularity status:
...

Derivation mode:
fast registry lookup / hard derivation / nonregular warning / needs clarification
```

Only after this normalized specification is written should the agent derive, retrieve, or implement an EIF.

---

## 2. Do not silently repair the problem

If the problem statement is incomplete, the agent may make explicit provisional assumptions, but it must label them.

Allowed:

```text
I will derive the EIF under the nonparametric observed-data model and under conditional exchangeability, because the prompt states a causal ATE but does not specify randomization or ignorability.
```

Not allowed:

```text
The EIF is the AIPW EIF.
```

without first stating the model, identification assumptions, and target functional.

If several incompatible interpretations are plausible, the agent should list them and either ask for clarification or solve the most conservative version while clearly naming the assumption.

---

## 3. Symbol table

For every LaTeX problem, create a symbol table before derivation.

```text
Symbol | Meaning | Observed? | Role
Y      | outcome | yes/no    | endpoint
A      | treatment | yes     | exposure
X      | covariates | yes    | adjustment set
R      | missingness indicator | yes | coarsening
C      | censoring time | yes/no | censoring
T      | event time | possibly no | latent/event
d      | treatment rule | fixed/estimated | intervention
```

The agent must distinguish:

- observed variables
- latent full-data variables
- counterfactual variables
- nuisance functions
- user-defined constants
- estimated quantities
- fixed functions, such as a policy \(d\), threshold \(t\), or kernel \(K_h\)

---

## 4. Target classification from LaTeX

The agent should classify targets using the following cues.

### 4.1 Full-data smooth functional

Examples:

\[
\psi(P)=E_P\{h(O)\},\qquad
\psi(P)=\operatorname{Var}_P(Y).
\]

Usually derive by centering \(h(O)\), plus delta method if needed.

### 4.2 Conditional or pointwise target

Examples:

\[
E(Y\mid X=x),\qquad
E\{Y(1)-Y(0)\mid X=x\}.
\]

If \(X\) is continuous and no smoothing or parametric restriction is stated, flag as potentially nonregular.

### 4.3 Causal target

Examples:

\[
E\{Y(a)\},\qquad
E\{Y(1)-Y(0)\},\qquad
P\{Y(a)\le t\}.
\]

The agent must write the identification assumptions before the observed-data functional.

### 4.4 Missing-data or coarsening target

Examples:

\[
O=(R,RY,X),\qquad \psi=E(Y).
\]

The agent must state whether missingness is MCAR, MAR, monotone missingness, censoring, or another coarsening process.

### 4.5 Ratio or transformation target

Examples:

\[
\psi=\frac{\alpha(P)}{\beta(P)},\qquad
\psi=\log\{\alpha(P)\},\qquad
\psi=q_\tau.
\]

The agent should first derive EIFs for the primitive functionals and then apply the delta method.

### 4.6 Optimization or selected target

Examples:

\[
\arg\max_x m(x),\qquad
\max_x m(x),\qquad
E\{Y(d^\ast)\},\quad d^\ast(x)=I\{m_1(x)>m_0(x)\}.
\]

These require hard-problem mode and may be nonregular without extra conditions.

---

## 5. Normalize the target

Every target must be rewritten as a population-level functional. The agent must not derive an EIF for an estimator.

Bad target statement:

```text
\hat\psi = n^{-1}\sum_i \hat m_1(X_i)-\hat m_0(X_i)
```

Normalized target:

\[
\psi(P)=E_P\{m_1(X)-m_0(X)\},
\qquad
m_a(x)=E_P(Y\mid A=a,X=x).
\]

Then the estimator can be discussed later.

---

## 6. Identification checkpoint

If the target is causal, latent, missing-data, or censored, the agent must separate:

1. The scientific target
2. The assumptions that identify it
3. The observed-data functional after identification

Template:

```text
Scientific target:
...

Identification assumptions:
...

Observed-data functional:
...

EIF will be derived for:
the observed-data functional under the stated observed-data model.
```

If the target is not identified, the agent should stop and say so. An EIF for an unidentified causal target is not meaningful without first choosing an identified observed-data functional.

---

## 7. Model checkpoint

The agent must state which model the EIF belongs to:

```text
Model choice:
- Fully nonparametric observed-data model
- Semiparametric model with known treatment/censoring mechanism
- Restricted model with parametric nuisance submodel
- Randomized trial model
- Case-control or biased sampling model
- Longitudinal/sequential model
```

If the model is restricted, the nonparametric influence function may not be efficient. The agent must either perform the tangent-space projection or explicitly state that the full nonparametric IF is not necessarily the restricted-model EIF.

---

## 8. Positivity and support checkpoint

The intake must record denominators and support requirements before derivation.

Examples:

\[
P(A=a\mid X)>0,
\]

\[
P(R=1\mid X)>0,
\]

\[
g(a\mid X)>0 \text{ where } g^\ast(a\mid X)>0,
\]

\[
f(q_\tau)>0.
\]

If the target involves ratios, densities, quantiles, inverse probabilities, or kernel smoothing, the agent must explicitly list the denominator that could be unstable.

---

## 9. Ambiguity checklist

Before deriving, check whether the problem statement leaves any of these unresolved:

- Is the treatment binary, categorical, continuous, or longitudinal?
- Is a policy \(d\) fixed before seeing data, learned from the same data, or optimal?
- Is a subgroup fixed with positive probability, or a point \(X=x\)?
- Are censoring and competing risks present?
- Is a propensity or censoring mechanism known by design?
- Is the model nonparametric or restricted?
- Are nuisance functions part of the target or only used for estimation?
- Is the parameter scalar, vector-valued, or infinite-dimensional?

If unresolved ambiguity changes the EIF, the agent must not hide it.

---

## 10. Handoff to derivation

After intake, choose one of four routes.

```text
Fast route:
Exact match to a regular registry formula. Still verify assumptions.

Hard route:
No exact formula, restricted model, complex censoring, longitudinal structure,
continuous treatment, mediation, transportability, or selected/optimal target.

Failure route:
Target is unidentified or not pathwise differentiable under the stated model.

Clarification route:
Multiple materially different interpretations remain.
```

The handoff must include the normalized target, model, assumptions, and regularity status.

