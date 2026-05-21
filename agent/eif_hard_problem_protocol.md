# EIF hard problem protocol

This document defines the workflow for difficult EIF problems where formula lookup is unsafe. It should be used when the target is unfamiliar, written in dense LaTeX, involves coarsening/censoring, has longitudinal structure, uses continuous treatments, imposes restricted models, or may be nonregular.

Hard mode includes two different situations:

1. Safety/trap problems, where a familiar formula is tempting but wrong.
2. Research problems, where no known formula may exist and the derivation must be built from first principles.

For research problems, also use:

```text
eif_research_problem_protocol.md
```

In hard mode, the registry is not the source of truth. It can be used only as a final comparison check after the derivation logic is complete.

---

## 1. When to enter hard mode

Use hard mode if any of the following are true:

- The target is not an exact match to the registry.
- The prompt uses counterfactuals, missing data, censoring, or longitudinal regimes.
- The target involves a conditional mean at a point, density at a point, maximum, argmax, optimal rule, threshold selected from the data, or unknown support boundary.
- The treatment, censoring, sampling, or missingness mechanism is known or restricted.
- The model imposes parametric, structural, conditional moment, monotonicity, or independence restrictions beyond the usual nonparametric observed-data model.
- The target is a ratio, quantile, mediation parameter, stochastic intervention, transportability parameter, IV estimand, or survival parameter.
- The question asks for an efficient IF specifically, not just any IF.

---

## 2. Hard gates before derivation

The agent must pass these gates before writing a final EIF.

### Gate 1: Identification

Can the scientific target be written as a functional of the observed-data law?

If no, stop:

```text
The target is not identified from the observed-data law under the stated assumptions, so an observed-data EIF cannot be derived without additional assumptions.
```

### Gate 2: Pathwise differentiability

Is the target pathwise differentiable in the stated model?

If likely no, stop or offer a regularized alternative:

```text
This target is not pathwise differentiable under the nonparametric model. A standard root-n EIF does not exist. A smoothed or restricted target would be needed.
```

### Gate 3: Model and tangent space

Is the requested EIF for:

- the full nonparametric observed-data model, or
- a restricted semiparametric model?

If restricted, identify the tangent space. If projection is not performed, the answer must say:

```text
The expression below is the full nonparametric influence function. The efficient influence function under the restricted model requires projection onto the restricted tangent space.
```

### Gate 4: Support and denominators

List every inverse probability, ratio denominator, density denominator, or weight denominator. State the positivity or bounded-away-from-zero condition.

---

## 3. Derivation ledger

Hard-mode derivations must use a component ledger. This prevents missing likelihood components.

```text
Likelihood component | Score | Mean-zero restriction | Target depends on it? | Derivative | IF component
---------------------|-------|-----------------------|-----------------------|------------|-------------
p(y | a,x)           | S_Y   | E(S_Y | A,X)=0        | yes/no                | ...        | ...
p(a | x)             | S_A   | E(S_A | X)=0          | yes/no                | ...        | ...
p(x)                 | S_X   | E(S_X)=0             | yes/no                | ...        | ...
```

For other data structures, replace rows with the appropriate factorization:

- missing data: \(p(y\mid x)^r p(r\mid x)p(x)\)
- two-phase sampling: sampling law, phase-one data law, phase-two data law
- censoring: event law, censoring law, covariate law
- longitudinal treatment: baseline law, treatment mechanisms, time-varying covariate laws, final outcome law
- transportability: source indicator law, site-specific outcome/treatment/covariate laws

The final IF is the sum of the component representers, centered if needed.

---

## 4. Likelihood factorization rule

The agent must factorize the observed-data likelihood in a way that matches the actual observed data.

Examples:

Point treatment:

\[
p(o)=p(y\mid a,x)p(a\mid x)p(x).
\]

Missing outcome:

\[
p(o)=p(y\mid x)^r p(r\mid x)p(x).
\]

Longitudinal regime:

\[
p(o)=p(l_0)\prod_{t=0}^K p(a_t\mid h_t)p(l_{t+1}\mid h_t,a_t).
\]

If the likelihood factorization is not clear, do not derive yet.

---

## 5. Score matching rule

For each likelihood component:

1. Perturb only that component.
2. Compute the derivative of the observed-data target.
3. Rewrite the derivative as an inner product with that component's score.
4. Extract the component of the IF.

The component must satisfy the correct conditional mean-zero structure.

For example, if a component multiplies \(S_Y(Y\mid A,X)\), then the candidate part should be orthogonal to all irrelevant score components and should use the correct inverse-probability bridge when rewriting conditional derivatives in observed-data form.

---

## 6. Treatment mechanism warning

Do not assume the treatment or missingness mechanism has no derivative contribution.

For standard ATE under the nonparametric observed-data model, the target

\[
E\{m_1(X)-m_0(X)\}
\]

does not directly depend on \(p(a\mid x)\), although the propensity appears in the IF.

But in other targets, the mechanism may be part of the target:

- stochastic interventions depending on the observed treatment density
- incremental propensity-score interventions
- policy values where the policy is learned or data-adaptive
- sampling or transport parameters involving site probabilities
- restricted models where known or parametric mechanisms change the tangent space

Hard mode requires deciding this explicitly.

---

## 7. Delta-method layer

If the target is built from primitive functionals, derive primitives first.

For

\[
\psi=h(\theta),
\]

derive \(D_\theta\), then use

\[
D_\psi=\nabla h(\theta)^\top D_\theta.
\]

For

\[
\psi=\alpha/\beta,
\]

use

\[
D_\psi=\frac{D_\alpha-\psi D_\beta}{\beta}.
\]

For quantiles, derive the CDF IF first and then invert:

\[
D_{q_\tau}=-\frac{D_F(q_\tau)}{f(q_\tau)}.
\]

State the required differentiability and denominator conditions.

---

## 8. Restricted-model projection protocol

If the model is restricted:

1. Derive or state the full nonparametric gradient \(D_{\mathrm{full}}\).
2. Specify the model tangent space \(\mathcal T\).
3. Compute or describe the projection

\[
D_{\mathrm{EIF}}=\Pi_{\mathcal T}D_{\mathrm{full}}.
\]

4. Verify that the result lies in \(\mathcal T\).
5. Verify that the residual is orthogonal to \(\mathcal T\).

If these steps are not completed, the agent must not call the full-gradient expression the efficient influence function for the restricted model.

---

## 9. Failure answers are valid answers

For hard problems, a correct refusal to produce an EIF can be the right output.

Use this form:

```text
Conclusion:
No standard root-n EIF exists under the stated nonparametric model.

Reason:
[pointwise conditioning / density at a point / argmax / unidentified target / nonunique optimizer / boundary problem / unknown support]

Regular alternative:
[fixed subgroup / smoothed target / parametric restriction / sample-split fixed policy / margin condition / different estimand]
```

Do not give an AIPW-looking formula after declaring nonregularity unless a regularized alternative has been explicitly defined.

---

## 10. Hard-mode answer skeleton

A hard-mode EIF answer should use this structure:

```text
1. Normalized problem statement
2. Identification
3. Regularity and model status
4. Nuisance functions
5. Likelihood factorization
6. Score decomposition
7. Component ledger
8. Pathwise derivative calculation
9. Candidate IF / EIF
10. Mean-zero proof
11. Pathwise derivative identity check
12. Special-case reductions
13. Implementation pseudo-outcome, if regular
14. Positivity and denominator diagnostics
15. Warnings, unresolved projections, or nonregularity notes
```

The answer should be concise when the problem is simple, but no hard-mode answer may skip items 1 through 10.

---

## 11. Registry use in hard mode

The registry may be used only after deriving the result.

Allowed:

```text
The derived expression reduces to the registry ATE EIF when the target is the usual point-treatment ATE.
```

Not allowed:

```text
This looks like ATE, so use the registry ATE formula.
```

For hard problems, formula similarity is evidence, not proof.
