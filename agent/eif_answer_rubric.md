# EIF answer rubric

This rubric defines the minimum standard for accepting an EIF derivation or implementation answer. It is designed for grading coding-agent outputs on both routine and hard semiparametric problems.

---

## 1. Pass/fail checklist

An answer should not be accepted as correct unless it satisfies all applicable items.

```text
[ ] The observed-data unit O is stated.
[ ] The target parameter is a population-level functional, not an estimator.
[ ] Scientific targets are separated from observed-data identification formulas.
[ ] Identification assumptions are stated when the target is causal, missing-data, censored, latent, or coarsened.
[ ] The statistical model is stated.
[ ] The answer says whether the EIF is for the nonparametric observed-data model or a restricted semiparametric model.
[ ] The target is checked for pathwise differentiability.
[ ] Nonregular targets are flagged instead of forced into standard EIF form.
[ ] Nuisance functions are defined at the population level.
[ ] Support, positivity, density, and denominator conditions are stated.
[ ] The likelihood is factorized correctly.
[ ] The score is decomposed correctly.
[ ] Each score component has its conditional mean-zero property stated.
[ ] The pathwise derivative is matched to the EIF by inner products with scores.
[ ] The final IF/EIF is centered and mean-zero.
[ ] The answer verifies the pathwise derivative identity, at least symbolically.
[ ] The expression reduces to known special cases.
[ ] If a formula registry entry is used, applicability is checked rather than assumed.
[ ] If the model is restricted, tangent-space projection is done or explicitly deferred.
[ ] The estimator uses the correct pseudo-outcome.
[ ] Standard error uses the empirical variance of estimated EIF values.
[ ] Cross-fitting is recommended or used when nuisance functions are flexibly estimated.
[ ] Positivity diagnostics are recommended for inverse-probability weights.
[ ] Remaining warnings and limitations are stated.
```

---

## 2. Severity levels for mistakes

### Critical errors

These invalidate the answer.

- Deriving an EIF for an estimator rather than the target parameter.
- Failing to identify a causal or missing-data target before deriving.
- Using an ATE EIF for ATT, QTE, policy value, mediation, IV, survival, or transportability without checking the target.
- Giving a standard EIF for a nonregular target without regularization.
- Calling a full nonparametric IF efficient under a restricted model without projection.
- Missing a likelihood component that affects the target.
- Omitting a required denominator such as \(e(X)\), \(1-e(X)\), \(\pi(X)\), \(g(a\mid X)\), \(\beta\), or \(f(q_\tau)\).
- Producing an expression that is not mean-zero.

### Major errors

These make the answer unreliable.

- Ambiguous observed-data structure.
- Unclear nuisance definitions.
- Positivity assumptions not stated for inverse weights.
- Sign error in a ratio, contrast, or quantile IF.
- Incorrect conditioning set in a nuisance function.
- Treating a learned policy as fixed without sample splitting or assumptions.
- Using in-sample nuisance predictions with flexible learners and no caveat.
- No special-case checks for a complex formula.

### Minor errors

These should be corrected but may not change the core derivation.

- Notational inconsistency after the target is otherwise clear.
- Missing implementation details when the request was derivation-only.
- Lack of numerical validation suggestions for an otherwise correct symbolic derivation.
- Incomplete citation to a known formula when the derivation is correct.

---

## 3. Required answer types

### 3.1 Regular identified target

The answer should end with:

```text
Conclusion:
The target is identified and pathwise differentiable under the stated model.
The EIF is ...
```

Then provide the estimator and diagnostics if implementation is requested.

### 3.2 Identified but restricted-model target

The answer should distinguish:

```text
Full nonparametric IF:
...

Restricted-model EIF:
obtained by projecting onto the restricted tangent space ...
```

If the projection is not performed, say so explicitly.

### 3.3 Unidentified target

The answer should end with:

```text
Conclusion:
The scientific target is not identified from the observed-data law under the stated assumptions.
No observed-data EIF is available until additional identification assumptions are added.
```

### 3.4 Nonregular target

The answer should end with:

```text
Conclusion:
The target is not pathwise differentiable under the stated nonparametric model.
A standard root-n EIF does not exist.
```

Then suggest a regular alternative if possible.

---

## 4. Component ledger grading

For hard problems, the answer should include a table like:

```text
Likelihood component | Score | Target depends on it? | IF component
```

Grade the derivation by asking:

- Does every likelihood component appear?
- Is each score's conditional mean-zero restriction correct?
- Are components with no direct target dependence justified, not merely ignored?
- Are inverse weights used only when needed to express conditional derivatives in observed-data form?
- Does the sum of components have mean zero?

---

## 5. Formula registry grading

The formula registry is useful, but it is not proof.

Accept registry use only if the answer also states:

```text
Why this registry entry matches:
- same observed data
- same target
- same model
- same identification assumptions
- same nuisance definitions
- same positivity requirements
```

Reject registry use if the answer only relies on superficial similarity.

---

## 6. Implementation grading

For implementation outputs, require:

- pseudo-outcome construction
- \(\hat\psi\) as the sample mean of the pseudo-outcome when applicable
- \(\hat\phi_i=\text{pseudo_outcome}_i-\hat\psi\)
- standard error \(sd(\hat\phi_i)/\sqrt n\)
- confidence interval
- clipping or diagnostics for probabilities, with a warning that clipping is not a substitute for positivity
- cross-fitting for flexible nuisance estimators
- clear handling of unobserved outcomes, censoring, or missing values

---

## 7. Minimum final verification block

Every final EIF answer should include a short verification block:

```text
Checks:
1. Mean zero: ...
2. Pathwise derivative: ...
3. Special case: ...
4. Positivity/regularity: ...
```

If any check is not available, the answer should say why.

