# EIF danger zone

This document lists cases where coding agents often produce incorrect efficient influence functions (EIFs) by blindly applying familiar formulas.

The central warning is:

```text
Do not force an EIF unless the target is pathwise differentiable under the stated model.
```

---

## 1. Pointwise CATE with continuous covariates

Target:

\[
\tau(x)=E\{Y(1)-Y(0)\mid X=x\}.
\]

If \(X\) is continuous and the model is fully nonparametric, this target is generally not root-\(n\) pathwise differentiable.

Why?

The event \(X=x\) has probability zero, so the conditional mean at a point is not a smooth functional of the observed-data distribution without additional structure.

Bad agent behavior:

```text
Writes the subgroup ATE EIF with G = I(X = x).
```

This is wrong when \(P(X=x)=0\).

Safer alternatives:

1. Fixed subgroup ATE:

\[
E\{Y(1)-Y(0)\mid X\in\mathcal G\},
\]

where

\[
P(X\in\mathcal G)>0.
\]

2. Kernel-smoothed CATE:

\[
\tau_h(x)
=
\frac{
E\left[K_h(X-x)\{m_1(X)-m_0(X)\}\right]
}{
E\left[K_h(X-x)\right]
}.
\]

3. Parametric or semiparametric model for \(\tau(x)\).

---

## 2. Density at a point

Target:

\[
p_Y(y_0).
\]

In a fully nonparametric model, the density at a point is generally not a regular root-\(n\) target.

Bad agent behavior:

```text
Writes something like I(Y = y0) - p(y0).
```

This is wrong for continuous \(Y\).

Safer alternative:

Use a smoothed target with fixed bandwidth:

\[
\psi_h=E\{K_h(Y-y_0)\}.
\]

Then the EIF is:

\[
D_{\psi_h}(O)=K_h(Y-y_0)-\psi_h.
\]

If \(h\to 0\), the analysis requires nonstandard smoothing-rate arguments.

---

## 3. Maximum or argmax targets

Targets:

\[
\max_x m(x),
\]

\[
\arg\max_x m(x),
\]

where

\[
m(x)=E(Y\mid X=x).
\]

These are generally nonregular without strong assumptions.

Problems include:

- Nonunique maximizers
- Flat regions near the maximum
- Boundary maximizers
- Nonsmooth dependence on \(P\)

Bad agent behavior:

```text
Takes the EIF of m(x) and plugs in x = argmax.
```

This is generally invalid.

Safer alternatives:

- Smoothed maximum
- Pre-specified fixed \(x\)
- Parametric model for \(m(x)\)
- Margin conditions and specialized nonregular theory

---

## 4. Optimal treatment rule

Target:

\[
d^\ast(x)=I\{m_1(x)>m_0(x)\}.
\]

Value:

\[
V(d^\ast)=E\{Y(d^\ast)\}.
\]

This can be nonregular when

\[
m_1(X)-m_0(X)
\]

is close to zero with positive probability.

Bad agent behavior:

```text
Uses the policy-value EIF with d replaced by estimated d_hat and ignores nonregularity.
```

The EIF for a fixed policy \(d\) is:

\[
D_{\psi_d}(O)
=
\frac{I\{A=d(X)\}}{P(A=d(X)\mid X)}
\{Y-m_d(X)\}
+
m_d(X)-\psi_d.
\]

But this is for fixed \(d\), not necessarily for an estimated or optimal rule without additional assumptions.

Safer alternatives:

- Evaluate a pre-specified policy.
- Use sample splitting for learned policies.
- State margin conditions.
- Use regret bounds instead of standard EIF inference.

---

## 5. Restricted semiparametric models

In a fully nonparametric model, the EIF is often the full gradient.

In a restricted semiparametric model, the efficient influence function is the projection of the full gradient onto the model tangent space:

\[
D_{\mathrm{EIF}}
=
\Pi_{\mathcal T}D_{\mathrm{full}}.
\]

Bad agent behavior:

```text
Uses the nonparametric EIF even though the model imposes restrictions.
```

Examples of restrictions:

- Parametric treatment model
- Parametric outcome model
- Known randomization probabilities
- Conditional moment restrictions
- Structural nested models
- Semiparametric transformation models

Safer behavior:

```text
State that the full nonparametric EIF has been derived, but the efficient EIF under the restricted model requires tangent-space projection.
```

---

## 6. Randomized trials with known treatment probabilities

In randomized trials, the treatment mechanism may be known by design.

Example:

\[
P(A=1\mid X)=p
\]

known.

The full nonparametric observational-data EIF may still be valid, but it may not be efficient under the smaller randomized-trial model.

Bad agent behavior:

```text
Automatically estimates e(X) and uses the observational ATE EIF.
```

Safer behavior:

- Use known randomization probability when available.
- Consider whether the efficiency bound differs under known design.
- State the model explicitly.

---

## 7. Survival with right censoring

Survival targets under right censoring require careful specification of the censoring model.

Target:

\[
S(t)=P(T>t).
\]

Bad agent behavior:

```text
Always uses the MAR-at-t missing-data EIF and claims full efficiency.
```

The status-at-\(t\) missing-data EIF can be useful:

\[
D_{S(t)}(O)
=
\frac{R_t}{\pi_t(X)}
\{Y_t-m_t(X)\}
+
m_t(X)-S(t).
\]

But fully efficient right-censoring EIFs are often expressed using counting-process martingales and depend on the censoring filtration.

Safer behavior:

- State whether using status-at-\(t\) MAR representation or full right-censoring model.
- Do not claim full efficiency unless the censoring model matches the derivation.
- Check independent censoring assumptions.

---

## 8. Mediation: natural direct and indirect effects

Observed data:

\[
O=(Y,A,M,X).
\]

Natural direct and indirect effects often involve mediator distributions that are themselves functionals of the observed law.

Bad agent behavior:

```text
Uses the fixed mediator intervention EIF and ignores mediator-density components.
```

For a fixed known mediator intervention distribution \(q(m\mid X)\), the EIF may have the simple form:

\[
\frac{I(A=a)q(M\mid X)}
{P(A=a\mid X)p(M\mid A=a,X)}
\{Y-m_Y(a,M,X)\}
+
\int m_Y(a,m,X)q(m\mid X)dm
-
\psi.
\]

But if

\[
q(m\mid X)=p(M=m\mid A=a',X),
\]

then \(q\) is not fixed; it depends on the observed-data law and creates additional EIF components.

Safer behavior:

- Distinguish stochastic interventional effects from natural effects.
- Identify all nuisance functions, including mediator densities.
- Derive all components.

---

## 9. Continuous treatment modified treatment policies

For continuous \(A\), a stochastic intervention with known density \(g^\star(a\mid X)\) has a relatively standard EIF:

\[
D_\psi(O)
=
\frac{g^\star(A\mid X)}{g(A\mid X)}
\{Y-m(A,X)\}
+
\int m(a,X)g^\star(a\mid X)da
-
\psi.
\]

But modified treatment policies

\[
A^\star=d(A,X)
\]

are more delicate.

Bad agent behavior:

```text
Uses the stochastic-intervention density ratio without checking the transformation.
```

Issues:

- Is \(d\) invertible in \(A\)?
- Is there a Jacobian term?
- What is the support of \(A^\star\)?
- Does positivity hold?
- Does \(d\) depend on unknown features of \(P\)?

Safer behavior:

- Derive the density ratio for the specific transformation.
- Check support and Jacobian.
- Avoid generic formulas unless conditions are clear.

---

## 10. Overlap-weighted ATE with estimated weights

Weighted ATE with fixed known weight \(w(X)\):

\[
\psi_w
=
\frac{E\{w(X)[m_1(X)-m_0(X)]\}}{E\{w(X)\}}
\]

has EIF:

\[
D_{\psi_w}(O)
=
\frac{w(X)}{E\{w(X)\}}
\left[
\frac{A}{e(X)}\{Y-m_1(X)\}
-
\frac{1-A}{1-e(X)}\{Y-m_0(X)\}
+
m_1(X)-m_0(X)-\psi_w
\right].
\]

But if

\[
w(X)=e(X)\{1-e(X)\},
\]

then \(w\) depends on the observed law.

Bad agent behavior:

```text
Uses the fixed-weight EIF and ignores the derivative of w(X).
```

Safer behavior:

- State whether weights are fixed or nuisance-dependent.
- If nuisance-dependent, derive additional terms.

---

## 11. Ratio targets with weak denominators

For

\[
\psi=\frac{\alpha}{\beta},
\]

the EIF is

\[
D_\psi
=
\frac{D_\alpha-\psi D_\beta}{\beta}.
\]

This requires \(\beta\) bounded away from zero.

Examples:

- LATE with weak instrument
- Risk ratio when baseline risk is close to zero
- Ratio of means with small denominator

Bad agent behavior:

```text
Reports EIF and Wald CI without warning about denominator instability.
```

Safer behavior:

- Report denominator estimate.
- Warn if denominator is close to zero.
- Consider weak-instrument or Fieller-type issues where relevant.

---

## 12. Quantiles with zero or small density

For

\[
q_\tau=F^{-1}(\tau),
\]

the EIF is

\[
D_{q_\tau}(O)
=
\frac{\tau-I(Y\le q_\tau)}{f(q_\tau)}.
\]

This requires:

\[
f(q_\tau)>0.
\]

Bad agent behavior:

```text
Uses the quantile EIF without checking density positivity.
```

Safer behavior:

- Estimate or discuss \(f(q_\tau)\).
- Warn if density is small.
- Avoid standard inference at flat or discrete parts of the distribution.

---

## 13. Discrete outcomes and quantiles

Quantile EIF formulas usually assume a continuous distribution with positive density at the quantile.

If \(Y\) is discrete, the quantile functional can be nonregular.

Bad agent behavior:

```text
Uses the continuous quantile EIF for binary outcomes.
```

Safer behavior:

- State that the usual quantile EIF may not apply.
- Consider distribution-function targets instead.
- Use special methods for discrete quantiles.

---

## 14. Post-selection targets

If a target is chosen after looking at the data, such as:

```text
The subgroup with the largest estimated treatment effect.
```

then standard EIF inference for a pre-specified target is not directly valid.

Bad agent behavior:

```text
Treats the selected subgroup as if it were fixed in advance.
```

Safer behavior:

- Use sample splitting.
- Adjust for selection.
- Define a fixed target before inference.

---

## 15. Final danger-zone checklist

Before giving an EIF, ask:

- [ ] Is the target pathwise differentiable?
- [ ] Is the model fully nonparametric or restricted?
- [ ] Is the target pointwise in a continuous variable?
- [ ] Does the target involve a density at a point?
- [ ] Does the target involve max, argmax, or an optimal rule?
- [ ] Does the target involve right censoring?
- [ ] Does the target involve mediation with mediator density from the observed law?
- [ ] Does the target involve a continuous treatment transformation?
- [ ] Does a weight depend on unknown nuisance functions?
- [ ] Is the target a ratio with a possibly small denominator?
- [ ] Is the target a quantile with a small or zero density?
- [ ] Is there post-selection?
