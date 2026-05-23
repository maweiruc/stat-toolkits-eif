# Problem 001 Solution: Restricted Moment Model

## 1. Normalized Problem

Observed data:

\[
O=(Y,X).
\]

The model is

\[
Y=m(X,\beta)+\varepsilon,
\qquad
E(\varepsilon\mid X)=0,
\]

where \(m(x,\beta)\) is known and smooth in the finite-dimensional parameter
\(\beta\in\mathbb R^d\). Let

\[
\varepsilon=Y-m(X,\beta),
\qquad
\dot m_\beta(X)=\frac{\partial m(X,\beta)}{\partial\beta}.
\]

The target is the true value \(\beta_0\) satisfying the conditional moment
restriction

\[
E\{Y-m(X,\beta_0)\mid X\}=0.
\]

In what follows \(\beta\) denotes this true value.

## 2. Identification and Assumptions

The parameter \(\beta\) is identified if the conditional mean restriction has a
unique solution in the parameter space. A sufficient local condition is that
the efficient information matrix displayed below is nonsingular.

Regularity assumptions used in the derivation:

1. \(m(x,\beta)\) is differentiable in \(\beta\).
2. The conditional error density is regular enough for integration by parts.
3. \(E(\varepsilon\mid X)=0\) at the true \(\beta\).
4. \(0<\sigma^2(X)<\infty\) almost surely, where
   \[
   \sigma^2(X)=E(\varepsilon^2\mid X).
   \]
5. The efficient information matrix is finite and nonsingular.
6. The tangent space is the closure of the nuisance spaces described below.

## 3. Nuisance Functions

The observed density can be written as

\[
p(x,y)=p_X(x)\eta\{y-m(x,\beta),x\}
=p_X(x)\eta(\varepsilon,x),
\]

where:

- \(p_X(x)\) is the unrestricted covariate law;
- \(\eta(\varepsilon,x)\) is the conditional error density;
- \(\eta\) is restricted by normalization and
  \[
  \int \varepsilon\eta(\varepsilon,x)d\varepsilon=0.
  \]

The nuisance functions are \(p_X\) and \(\eta\).

## 4. Tangent Spaces

The covariate-law nuisance tangent space is

\[
\Lambda_1=\{a(X):E(a(X))=0\}.
\]

The conditional error-law nuisance tangent space is

\[
\Lambda_2=
\left\{
a(\varepsilon,X):
E(a\mid X)=0,\,
E(a\varepsilon\mid X)=0
\right\}.
\]

The nuisance tangent space is

\[
\Lambda=\Lambda_1\oplus\Lambda_2.
\]

The orthocomplement is

\[
\Lambda^\perp
=
\{a(X)\varepsilon:a(X)\text{ square-integrable}\}.
\]

This is the key geometric fact. Any efficient score for \(\beta\) must be a
conditional-error residual \(\varepsilon\) multiplied by a function of \(X\).

## 5. Raw Score

Let

\[
\ell_\varepsilon(\varepsilon,X)
=
\frac{\partial}{\partial\varepsilon}\log\eta(\varepsilon,X),
\qquad
\rho(\varepsilon,X)=-\ell_\varepsilon(\varepsilon,X).
\]

Since

\[
\frac{\partial\varepsilon}{\partial\beta}
=-\dot m_\beta(X),
\]

the raw score for \(\beta\) is

\[
S_\beta(O)
=
\rho(\varepsilon,X)\dot m_\beta(X)
=
-\ell_\varepsilon(\varepsilon,X)\dot m_\beta(X).
\]

This is a candidate score, not the efficient score, because it generally has a
component in the nuisance tangent space \(\Lambda_2\).

## 6. Projection and Efficient Score

Project the raw score onto

\[
\Lambda^\perp=\{a(X)\varepsilon\}.
\]

Conditionally on \(X\), the projection of
\(\rho(\varepsilon,X)\dot m_\beta(X)\) onto the span of \(\varepsilon\) is

\[
E\{\rho(\varepsilon,X)\varepsilon\mid X\}
\sigma^{-2}(X)\varepsilon\dot m_\beta(X).
\]

Under the usual integration-by-parts identity,

\[
E\{\rho(\varepsilon,X)\varepsilon\mid X\}=1.
\]

Therefore the efficient score is

\[
\boxed{
S_{\mathrm{eff}}(O)
=
\varepsilon\sigma^{-2}(X)\dot m_\beta(X).
}
\]

## 7. Efficient Information and EIF

The efficient information matrix is

\[
I_{\mathrm{eff}}
=
E\{S_{\mathrm{eff}}S_{\mathrm{eff}}^\top\}
=
E\left[
\sigma^{-2}(X)\dot m_\beta(X)\dot m_\beta(X)^\top
\right].
\]

If \(I_{\mathrm{eff}}\) is nonsingular, the efficient influence function for
\(\beta\) is

\[
\boxed{
D_\beta(O)
=
I_{\mathrm{eff}}^{-1}S_{\mathrm{eff}}(O)
=
I_{\mathrm{eff}}^{-1}
\sigma^{-2}(X)\dot m_\beta(X)\{Y-m(X,\beta)\}.
}
\]

Status:

```text
derived and verified under stated assumptions
```

## 8. Verification

### Mean Zero

\[
E\{S_{\mathrm{eff}}\mid X\}
=
\sigma^{-2}(X)\dot m_\beta(X)E(\varepsilon\mid X)
=0.
\]

Hence \(E(S_{\mathrm{eff}})=0\) and \(E(D_\beta)=0\).

### Orthogonality to \(\Lambda_1\)

For any \(a(X)\in\Lambda_1\),

\[
E\{S_{\mathrm{eff}}a(X)\}
=
E\left[a(X)E\{S_{\mathrm{eff}}\mid X\}\right]
=0.
\]

### Orthogonality to \(\Lambda_2\)

For any \(a(\varepsilon,X)\in\Lambda_2\),

\[
E(a\varepsilon\mid X)=0.
\]

Therefore

\[
E\{S_{\mathrm{eff}}a\}
=
E\left[
\sigma^{-2}(X)\dot m_\beta(X)E(\varepsilon a\mid X)
\right]
=0.
\]

Thus \(S_{\mathrm{eff}}\in\Lambda^\perp\).

### Pathwise Derivative Identity

For every regular parametric submodel whose score component for \(\beta\) is
\(h^\top S_\beta\), the derivative of \(\beta\) in direction \(h\) is
represented by

\[
E\{D_\beta(O)S(O)\}.
\]

Equivalently, \(D_\beta=I_{\mathrm{eff}}^{-1}S_{\mathrm{eff}}\) is the
canonical gradient because \(S_{\mathrm{eff}}\) is the projection of the raw
parametric score onto \(\Lambda^\perp\).

## 9. Efficient Estimating Equation

The efficient estimating equation is

\[
\sum_{i=1}^n
\{Y_i-m(X_i,\beta)\}
\sigma^{-2}(X_i)\dot m_\beta(X_i)=0.
\]

More generally, equations of the form

\[
\sum_{i=1}^n
\{Y_i-m(X_i,\beta)\}a(X_i)=0
\]

can yield regular asymptotically linear estimators under suitable conditions,
but the efficient choice is

\[
a(X)=\sigma^{-2}(X)\dot m_\beta(X).
\]

## 10. Warnings

- The raw score
  \[
  -\ell_\varepsilon(\varepsilon,X)\dot m_\beta(X)
  \]
  is not generally efficient.
- The efficient score depends only on the conditional variance
  \(\sigma^2(X)\), not on the full conditional error density.
- If \(I_{\mathrm{eff}}\) is singular, \(\beta\) may not be locally regular in
  all directions.
- If the integration-by-parts identity or tangent-space closure fails, the
  expression should be treated as a candidate efficient score until those
  regularity conditions are verified.
