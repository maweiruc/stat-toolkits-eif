# EIF references

This file lists references useful for semiparametric theory, efficient influence functions, causal inference, missing data, TMLE, DML, quantile treatment effects, and longitudinal treatment regimes.

The list is organized by topic.

---

## 1. General semiparametric theory

### Bickel, Klaassen, Ritov, and Wellner

```text
Bickel, P. J., Klaassen, C. A. J., Ritov, Y., and Wellner, J. A. (1993).
Efficient and Adaptive Estimation for Semiparametric Models.
Johns Hopkins University Press.
```

Classic reference for semiparametric efficiency, tangent spaces, and efficient influence functions.

---

### van der Vaart

```text
van der Vaart, A. W. (1998).
Asymptotic Statistics.
Cambridge University Press.
```

Important general asymptotic theory reference. Useful for differentiability, asymptotic linearity, and delta method.

---

### Tsiatis

```text
Tsiatis, A. A. (2006).
Semiparametric Theory and Missing Data.
Springer.
```

Very useful for missing data, semiparametric efficiency, and influence functions.

---

### Kosorok

```text
Kosorok, M. R. (2008).
Introduction to Empirical Processes and Semiparametric Inference.
Springer.
```

Useful for empirical process foundations and semiparametric inference.

---

## 2. Missing data and causal inference foundations

### Robins, Rotnitzky, and Zhao

```text
Robins, J. M., Rotnitzky, A., and Zhao, L. P. (1994).
Estimation of regression coefficients when some regressors are not always observed.
Journal of the American Statistical Association.
```

Classic paper on inverse probability weighting, augmentation, and missing data.

---

### Robins and Rotnitzky

```text
Robins, J. M. and Rotnitzky, A. (1995).
Semiparametric efficiency in multivariate regression models with missing data.
Journal of the American Statistical Association.
```

Important for semiparametric efficiency with missing data.

---

### Robins, Rotnitzky, and Zhao

```text
Robins, J. M., Rotnitzky, A., and Zhao, L. P. (1995).
Analysis of semiparametric regression models for repeated outcomes in the presence of missing data.
Journal of the American Statistical Association.
```

Influential for repeated outcomes and missing data.

---

## 3. Propensity scores and treatment effects

### Hahn

```text
Hahn, J. (1998).
On the role of the propensity score in efficient semiparametric estimation of average treatment effects.
Econometrica.
```

Classic reference for semiparametric efficiency bounds for ATE and the role of the propensity score.

---

### Hirano, Imbens, and Ridder

```text
Hirano, K., Imbens, G. W., and Ridder, G. (2003).
Efficient estimation of average treatment effects using the estimated propensity score.
Econometrica.
```

Important for efficient ATE estimation with estimated propensity scores.

---

### Imbens

```text
Imbens, G. W. (2004).
Nonparametric estimation of average treatment effects under exogeneity: A review.
Review of Economics and Statistics.
```

Review of treatment effect estimation under unconfoundedness.

---

## 4. Targeted learning and TMLE

### van der Laan and Robins

```text
van der Laan, M. J. and Robins, J. M. (2003).
Unified Methods for Censored Longitudinal Data and Causality.
Springer.
```

Core reference for longitudinal data, causal inference, censoring, and EIF-based estimation.

---

### van der Laan and Rose

```text
van der Laan, M. J. and Rose, S. (2011).
Targeted Learning: Causal Inference for Observational and Experimental Data.
Springer.
```

Main reference for targeted maximum likelihood estimation.

---

### van der Laan and Rose

```text
van der Laan, M. J. and Rose, S. (2018).
Targeted Learning in Data Science.
Springer.
```

Updated targeted learning reference.

---

## 5. Double machine learning and orthogonal scores

### Chernozhukov et al.

```text
Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E.,
Hansen, C., Newey, W., and Robins, J. (2018).
Double/debiased machine learning for treatment and structural parameters.
The Econometrics Journal.
```

Important for Neyman orthogonality, cross-fitting, and machine learning nuisance estimation.

---

### Newey

```text
Newey, W. K. (1994).
The asymptotic variance of semiparametric estimators.
Econometrica.
```

Important for semiparametric variance and influence function calculations.

---

## 6. Quantile treatment effects

### Firpo

```text
Firpo, S. (2007).
Efficient semiparametric estimation of quantile treatment effects.
Econometrica.
```

Key reference for QTE and semiparametric efficiency.

---

### Chernozhukov and Hansen

```text
Chernozhukov, V. and Hansen, C. (2005).
An IV model of quantile treatment effects.
Econometrica.
```

Important for quantile treatment effects with instrumental variables.

---

## 7. Longitudinal treatment regimes

### Murphy

```text
Murphy, S. A. (2003).
Optimal dynamic treatment regimes.
Journal of the Royal Statistical Society: Series B.
```

Classic reference for dynamic treatment regimes.

---

### Robins

```text
Robins, J. M. (1986).
A new approach to causal inference in mortality studies with a sustained exposure period.
Mathematical Modelling.
```

Foundational work for g-methods and longitudinal causal inference.

---

### Robins

```text
Robins, J. M. (1999).
Association, causation, and marginal structural models.
Synthese.
```

Important for marginal structural models.

---

## 8. Survival and censoring

### Andersen, Borgan, Gill, and Keiding

```text
Andersen, P. K., Borgan, Ø., Gill, R. D., and Keiding, N. (1993).
Statistical Models Based on Counting Processes.
Springer.
```

Core reference for counting-process martingales and survival analysis.

---

### Fleming and Harrington

```text
Fleming, T. R. and Harrington, D. P. (1991).
Counting Processes and Survival Analysis.
Wiley.
```

Classic survival analysis reference.

---

### van der Laan and Robins

```text
van der Laan, M. J. and Robins, J. M. (2003).
Unified Methods for Censored Longitudinal Data and Causality.
Springer.
```

Also central for censoring and EIFs in survival settings.

---

## 9. Instrumental variables and local treatment effects

### Imbens and Angrist

```text
Imbens, G. W. and Angrist, J. D. (1994).
Identification and estimation of local average treatment effects.
Econometrica.
```

Classic reference for LATE.

---

### Abadie

```text
Abadie, A. (2003).
Semiparametric instrumental variable estimation of treatment response models.
Journal of Econometrics.
```

Semiparametric IV treatment effect estimation.

---

## 10. Suggested reading path

For a coding agent or researcher new to EIFs:

1. Start with simple full-data examples:
   - Mean
   - Variance
   - CDF
   - Quantile

2. Then study missing data:
   - Tsiatis (2006)
   - Robins, Rotnitzky, and Zhao

3. Then treatment effects:
   - Hahn (1998)
   - Hirano, Imbens, and Ridder (2003)

4. Then targeted learning:
   - van der Laan and Robins (2003)
   - van der Laan and Rose (2011)

5. Then machine-learning nuisance estimation:
   - Chernozhukov et al. (2018)

6. Then specialized topics:
   - Firpo (2007) for QTE
   - Andersen et al. (1993) for survival
   - Murphy (2003) for dynamic treatment regimes
