# Prediction-Model Review

## Purpose
This file supports review-grade writing and appraisal when the target literature is about clinical prediction tools rather than general disease description.

Use it when the corpus contains scores, nomograms, risk scores, machine-learning models, or clinical prediction tools.

## 1. When To Route Here

Use this workflow when the user asks for any of the following:
- prediction model review
- nomogram review
- risk-score review
- model appraisal
- transportability / external validation discussion
- comparison of prediction tools for a disease, resistance phenotype, or clinical syndrome

## 2. First Question: Is This Really a Prediction Model Corpus?

Before writing, separate these categories:
- true prediction model studies
- risk-factor association studies
- descriptive epidemiology papers
- treatment/outcome prediction models unrelated to the infection-acquisition question
- pathogen-specific mortality models vs infection-acquisition models

Do not mix these casually.

## 3. Minimum Extraction Dimensions

For each included study, try to extract:
- citation / identifier
- target population
- clinical setting
- organism or resistance phenotype target
- predicted outcome
- model type (`score`, `nomogram`, `ML`, `other`)
- candidate predictors
- final predictors retained
- derivation / internal validation / external validation
- discrimination metric(s) if reported
- calibration information if reported
- decision utility / threshold analysis if reported
- key limitations or transportability risks

If any field is missing, mark it explicitly rather than filling it by guesswork.

## 4. Recommended Review Structure

### A. Why prediction is needed
Explain the clinical decision problem first.
Examples:
- empiric antibiotic selection
- early risk stratification
- identifying high-risk carriers or high-risk ICU admissions
- selecting patients for intensified surveillance

### B. Model landscape map
Group studies by:
- target setting (CAP, HAP/VAP, ICU, oncology, colonized patients, etc.)
- outcome type (MDR pathogen, carbapenem-requiring infection, CR-GNB carriage, bacteremia, specific pathogen infection)
- model form (simple score, nomogram, ML model)

### C. Methodological appraisal
Discuss:
- whether predictors are available at point of care
- whether the model was externally validated
- whether calibration was reported
- whether transportability is plausible across hospitals or countries
- whether the endpoint is clinically coherent

### D. Clinical usefulness
Discuss what the model can realistically support and what it cannot.
Do not assume a model is clinically useful just because the AUC looks respectable.

### E. Evidence gaps
Highlight:
- lack of external validation
- narrow single-center cohorts
- over-specialized populations
- mixed pathogen definitions
- mismatch between predicted outcome and bedside decision need

## 5. Hard Rules

- do not treat a risk-factor paper as a finished prediction model paper
- do not assume a nomogram figure proves adequate model reporting
- do not compare models head-to-head unless outcomes and settings are genuinely comparable
- do not overstate clinical adoption readiness when external validation is weak or absent
- when appraisal requirements exceed native coverage, explicitly borrow stronger local-skill logic or external reporting/appraisal patterns and label the borrowing

## 6. Safe Appraisal Language

Preferred phrases:
- `the available models are highly setting-specific`
- `external validation appears limited`
- `reported discrimination is not enough to establish transportability`
- `the evidence base supports a review-grade synthesis, not a universal implementation recommendation`
- `the current literature is better viewed as a set of scenario-specific tools than a unified prediction framework`

## 7. Output-Level Guidance

Use the strongest honest level:
- `submission-grade review draft` only if coverage, appraisal, and model comparison are already mature
- `review-grade evidence synthesis` when there is enough to compare families of models but not enough for final claims
- `evidence map` when studies are too heterogeneous to synthesize tightly
- `framework memo` when the corpus is still incomplete

## 8. Suggested Evidence Matrix Columns

A good matrix usually includes:
- Study
- Population
- Setting
- Organism / resistance target
- Outcome
- Model type
- Predictors
- Validation type
- Discrimination
- Calibration
- Utility / DCA
- Main limitations
- Review note

## 9. Borrowed External Standards

If methodological appraisal becomes the bottleneck, it is acceptable to borrow external reporting or appraisal patterns, but only with explicit labeling.

Preferred external standards for this situation:
- `TRIPOD / TRIPOD+AI` for reporting completeness of prediction-model studies and reviews
- `PROBAST / PROBAST+AI` for risk-of-bias and applicability appraisal
- `CHARMS`-style extraction logic when the review needs a structured data-extraction frame for prediction-model studies

Good phrasing:
- `For model-appraisal structure, I am borrowing a prediction-model review pattern from external reporting/appraisal standards such as TRIPOD/PROBAST.`
- `This appraisal scaffold is borrowed and should not be mistaken for native fully implemented runtime support.`
- `I am using a CHARMS-like extraction frame to organize study characteristics, but that external structure is being applied explicitly rather than presented as a native built-in methodology.`
