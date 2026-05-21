# Notes for problem 001

Topic:
Restricted Moment Model.

Source image:
\[
Y=m(X,\beta)+\epsilon,
\qquad
E(\epsilon\mid X)=0.
\]

Density factorization:
\[
f_{X,Y}(x,y)
=
f_X(x)f_{\epsilon\mid X}\{y-m(x,\beta),x\}
=
\eta_1(x)\eta_2\{y-m(x,\beta),x\}.
\]

Preferred mode:
Research mode / restricted semiparametric model.

Why this is hard:
- The model restricts the conditional mean but leaves the conditional error distribution otherwise unspecified.
- The nuisance tangent space includes the covariate law \(f_X\) and conditional error-law perturbations preserving both normalization and \(E(\epsilon\mid X)=0\).
- The efficient score is obtained by projecting the raw score onto the orthocomplement of the nuisance tangent space.

Expected workflow:
1. Let
   \[
   \epsilon=Y-m(X,\beta),
   \qquad
   \dot m_\beta(X)=\partial m(X,\beta)/\partial\beta.
   \]
2. Define the conditional error score
   \[
   \ell_\epsilon(\epsilon,X)
   =
   \partial \log f_{\epsilon\mid X}(\epsilon\mid X)/\partial \epsilon.
   \]
3. Raw score for \(\beta\) should have the form
   \[
   S_\beta=-\ell_\epsilon(\epsilon,X)\dot m_\beta(X).
   \]
4. Project away the conditional error-law nuisance. Under standard regularity,
   the efficient score should reduce to a form involving
   \[
   \epsilon\sigma^{-2}(X)\dot m_\beta(X),
   \qquad
   \sigma^2(X)=E(\epsilon^2\mid X).
   \]
5. The EIF should be information-inverse times the efficient score.

Important warning:
Do not confuse the raw parametric score with the efficient score. The projection is the main step.

Worked reference now available:
`theory/eif_restricted_moment_worked_derivation.md`
