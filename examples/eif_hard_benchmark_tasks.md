# EIF hard benchmark tasks

These benchmarks are designed to test whether an agent can handle difficult EIF problems without blindly applying familiar formulas. Many tasks are expected to produce warnings, projections, or regularity failures rather than a simple EIF.

For each task, require the agent to return:

```text
1. Normalized problem statement
2. Target triage label
3. Identification status
4. Regularity status
5. Model and tangent-space status
6. Likelihood factorization
7. Component ledger
8. EIF, full IF, projection requirement, or nonregularity conclusion
9. Mean-zero and pathwise derivative checks when applicable
10. Special-case check or failure-mode explanation
```

---

## Task H1: Known randomization versus observational ATE

Observed data:

\[
O=(Y,A,X).
\]

Treatment is randomized with known probability:

\[
P(A=1\mid X)=p
\]

where \(p\) is known by design.

Target:

\[
\psi=E\{Y(1)-Y(0)\}.
\]

Expected behavior:

- Identify the target by consistency and randomization.
- Derive or state the full nonparametric ATE IF.
- Check whether projection onto the known-treatment-mechanism tangent space changes the IF.
- Explain why for the usual ATE the treatment-mechanism projection is zero.

Common failure:

- Saying "known propensity means no propensity appears." The known \(p\) still appears in inverse-probability residual terms.

---

## Task H2: ATT is not ATE

Observed data:

\[
O=(Y,A,X).
\]

Target:

\[
\psi=E\{Y(1)-Y(0)\mid A=1\}.
\]

Assumptions:

- consistency
- exchangeability for \(Y(0)\) among treated/control support
- positivity for controls among treated covariate support

Expected behavior:

- Use ATT-specific nuisances \(m_0(X)\), \(e(X)\), and \(p=P(A=1)\).
- Include the treated-population weighting.
- Do not use the ATE EIF.

Common failure:

- Differencing two mean-potential-outcome EIFs and calling it ATT.

---

## Task H3: Pointwise CATE with continuous covariates

Observed data:

\[
O=(Y,A,X),
\]

where \(X\) is continuous.

Target:

\[
\tau(x_0)=E\{Y(1)-Y(0)\mid X=x_0\}.
\]

Expected behavior:

- Conclude that the target is generally not pathwise differentiable in the fully nonparametric model.
- Refuse to give a standard root-\(n\) EIF.
- Suggest a fixed subgroup target, smoothed target, or parametric restriction.

Common failure:

- Using subgroup ATE with \(G=I(X=x_0)\).

---

## Task H4: Smoothed CATE target

Observed data:

\[
O=(Y,A,X),
\]

where \(X\) is continuous.

Target with fixed bandwidth \(h\):

\[
\psi_h
=
\frac{
E[K_h(X-x_0)\{m_1(X)-m_0(X)\}]
}{
E[K_h(X-x_0)]
}.
\]

Expected behavior:

- Recognize this as a regular ratio target for fixed \(h\).
- Derive numerator and denominator IFs.
- Apply the ratio delta method.
- State that \(h\to0\) creates a separate nonstandard smoothing problem.

Common failure:

- Treating this as identical to pointwise CATE.

---

## Task H5: Survival under right censoring

Observed data:

\[
O=(\tilde T,\Delta,X),
\qquad
\tilde T=\min(T,C),
\qquad
\Delta=I(T\le C).
\]

Target:

\[
\psi=P(T>t).
\]

Expected behavior:

- State the censoring model and filtration.
- Do not use the no-censoring EIF \(I(T>t)-\psi\) directly.
- Either derive under a status-at-\(t\) MAR representation or state that a full right-censoring EIF requires counting-process martingale machinery.
- State independent censoring and positivity assumptions.

Common failure:

- Replacing \(T\) by \(\tilde T\) in the no-censoring formula.

---

## Task H6: Stochastic intervention with continuous treatment

Observed data:

\[
O=(Y,A,X),
\]

where \(A\) is continuous.

Target:

\[
\psi
=
E_X\left[\int m(a,X)g^\star(a\mid X)\,da\right],
\]

where

\[
m(a,x)=E(Y\mid A=a,X=x).
\]

Expected behavior:

- Identify nuisance functions \(m(a,X)\), observed density \(g(a\mid X)\), and fixed intervention density \(g^\star(a\mid X)\).
- State support condition \(g(a\mid X)>0\) wherever \(g^\star(a\mid X)>0\).
- Use the density-ratio residual correction.
- Warn that density estimation and integration can be difficult.

Common failure:

- Using binary-treatment AIPW form.

---

## Task H7: Modified treatment policy

Observed data:

\[
O=(Y,A,X),
\]

where \(A\) is continuous.

Policy:

\[
A^\star=d(A,X).
\]

Target:

\[
\psi=E\{Y(d(A,X))\}.
\]

Expected behavior:

- Enter hard mode.
- Derive the transformation-specific density ratio, including support and possible Jacobian terms.
- State that the stochastic-intervention formula with arbitrary \(g^\star\) is not automatically valid unless \(g^\star\) is the induced post-policy density.

Common failure:

- Writing \(g^\star(A\mid X)/g(A\mid X)\) without deriving \(g^\star\).

---

## Task H8: Natural direct effect

Observed data:

\[
O=(Y,A,M,X).
\]

Target:

\[
E\{Y(1,M(0))-Y(0,M(0))\}.
\]

Expected behavior:

- Enter hard mode.
- State cross-world identification assumptions if attempting identification.
- Distinguish natural effects from stochastic interventional effects.
- Include mediator-density components if deriving the natural direct effect under a nonparametric model.

Common failure:

- Using a fixed mediator intervention EIF and ignoring that the mediator distribution is part of the observed law.

---

## Task H9: Transported ATE

Observed data:

\[
O=(S,Y,A,X),
\]

where outcomes are observed in source population \(S=1\), and the target is for population \(S=0\).

Target:

\[
\psi=E\{Y(1)-Y(0)\mid S=0\}.
\]

Expected behavior:

- State transportability and exchangeability assumptions.
- Identify the target as a transported observed-data functional.
- Include source/target density ratio or selection mechanism components as needed.
- Do not use the ordinary single-population ATE EIF without modification.

Common failure:

- Ignoring the source indicator \(S\).

---

## Task H10: Restricted parametric treatment mechanism

Observed data:

\[
O=(Y,A,X).
\]

Assume

\[
P(A=1\mid X)=\operatorname{expit}(\gamma^\top X)
\]

for unknown finite-dimensional \(\gamma\).

Target:

\[
\psi=E\{Y(1)-Y(0)\}.
\]

Expected behavior:

- Derive the full nonparametric IF as a starting point.
- State the restricted treatment-mechanism tangent space.
- Check whether the full IF has a treatment-mechanism component.
- If projection is not completed, do not call the full IF the restricted-model EIF.

Common failure:

- Ignoring the restricted model after mentioning it.

---

## Task H11: Quantile with discrete outcome

Observed data:

\[
O=Y,
\]

where \(Y\) is binary.

Target:

\[
q_\tau=F^{-1}(\tau).
\]

Expected behavior:

- Flag that the continuous quantile EIF requiring \(f(q_\tau)>0\) is not applicable.
- Discuss nonregularity or set-valued behavior at jumps.
- Refuse to use \((\tau-I(Y\le q_\tau))/f(q_\tau)\).

Common failure:

- Applying the continuous quantile EIF to a binary outcome.

---

## Task H12: Weak Wald denominator

Observed data:

\[
O=(Y,A,Z,X).
\]

Target:

\[
\psi
=
\frac{
E[m_Y(1,X)-m_Y(0,X)]
}{
E[m_A(1,X)-m_A(0,X)]
}.
\]

Expected behavior:

- Derive numerator and denominator IFs separately.
- Apply the ratio delta method.
- Warn if the denominator is near zero.
- Separate the statistical Wald functional from causal LATE interpretation.

Common failure:

- Providing a causal LATE interpretation without IV assumptions or denominator diagnostics.

