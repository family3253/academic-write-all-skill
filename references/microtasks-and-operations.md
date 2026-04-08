# Microtasks and Operations

## Purpose
This file captures high-frequency late-stage academic writing operations that appear repeatedly across prompt collections.

## 1. Polishing Operations

### Supported polishing targets
- sentence clarity
- paragraph coherence
- paragraph-to-paragraph transition
- terminology consistency
- reduction of repetition
- concise rewriting
- journal-style elevation
- anti-AI-tone rewriting

### Typical outputs
- revised passage only
- revised passage + explanation table
- issue list + revised version
- original / revised / rationale table

### Recommended workflow
- diagnose first
- then revise paragraph by paragraph
- then explain what changed and what still requires manual verification

## 2. Rewriting and De-duplication

### Use when
- the user wants paraphrasing or similarity reduction
- the text is too repetitive or template-like
- the user wants stronger academic tone without changing the claim

### Rules
- preserve meaning unless adaptation is explicitly requested
- do not replace field-specific terms casually
- do not distort citation relationships
- if asked to lower AI-detection risk, improve prose naturally rather than gaming detectors with nonsense variation
- if the user is responding to a similarity report, work on the flagged passages first instead of rewriting the whole thesis blindly

## 3. Translation Operations

### Modes
- literal academic translation
- journal-style translation
- bilingual aligned drafting
- translation + consistency normalization

### Rules
- preserve headings, citations, numbering, figure/table references
- preserve meaning first, elegance second
- maintain term consistency across sections

## 4. Logic Repair

### Levels
- sentence-internal coherence
- paragraph-internal coherence
- paragraph-to-paragraph flow
- section logic
- whole-manuscript argument logic

### Recommended output format
- issue
- why flow breaks
- specific fix
- improved version

## 5. Grammar / Style / Reference Checks

### Suitable checks
- grammar and spelling only
- formatting consistency
- reference formatting conformity
- punctuation / abbreviation / capitalization consistency
- SCI / SSCI manuscript detail checks

### Rules
- do not silently rewrite the manuscript if the user asked only for checking
- distinguish error correction from substantive rewriting

### Staged reference check workflow
1. classify reference type
2. check completeness of metadata fields
3. check punctuation and field order against the target standard
4. provide corrected version
5. flag anything that still requires manual verification from the original source

## 6. Abstract / Title / Cover Letter Operations

### Abstract tasks
- draft from manuscript
- revise using context-content-conclusion structure
- align with structured abstract requirements
- compress or sharpen abstract

### Thesis front-matter additions
- produce Chinese abstract from structured thesis inputs first
- derive English abstract from the finalized Chinese abstract plus controlled terminology
- generate multiple title options and compare by scope accuracy and feasibility
- draft acknowledgments from real contributor notes with restrained tone

### Title tasks
- generate multiple candidate titles
- adjust title for venue fit
- sharpen specificity and searchability

### Cover letter tasks
- editor-facing concise submission note
- fit statement
- contribution summary
- originality and exclusivity statement where needed

## 7. Statistical Interpretation Microtasks

### Suitable inputs
- regression outputs
- ANOVA summaries
- descriptive statistics
- correlation results
- figure/table result summaries

### Output rules
- convert numbers to accurate academic prose
- preserve sign, magnitude, significance, and model framing
- do not over-interpret beyond the design

## 8. Review and Re-Review Operations

### Review layers to support
- methodology review
- domain review
- perspective review
- devil's-advocate review
- editorial synthesis

### Re-review use case
Use when a revised manuscript needs verification against prior review comments.

Output options:
- revision response checklist
- residual issue list
- re-review memo
- accept / minor / major style heuristic recommendation

## 9. LaTeX / Venue / Finalization Awareness

### Use when
- the manuscript is heading toward LaTeX submission workflows
- venue constraints matter for page limits, section rules, citation format, or figure policies

### cycwrite should
- be venue-sensitive
- avoid claiming final LaTeX readiness unless build verification exists
- surface compile / citation / figure-path risks when relevant

## 10. Journal Match and Submission Readiness Microtasks

### Use when
- the user wants a shortlist fast
- the user wants a pre-submission weakness scan
- the user wants likely reviewer attack points identified

### Output options
- shortlist with rationale
- fit memo
- readiness checklist
- vulnerability matrix

## 11. Topic Narrowing and Outline Logic Checks

### Use when
- the user has a broad thesis direction but not a stable executable topic
- the outline exists but the chapter logic is weak or repetitive

### Typical outputs
- candidate topic comparison table
- feasibility filter table
- narrowed title set with rationale
- reviewer-style outline logic checklist

### Rules
- prefer small, executable topics over broad and fragile ones
- compare options by data/material availability, novelty level, workload, and chapter fit
- if the outline is already drafted, check whether each chapter has a distinct job and whether the order mirrors the thesis argument

## 12. Defense PPT Storyline Operations

### Use when
- the user needs a slide outline or speaking narrative for a thesis defense

### Typical outputs
- slide-by-slide storyline
- one-slide-one-message bullet structure
- speaker-note skeleton
- likely defense-question checklist

### Rules
- keep the output focused on narrative structure rather than slide aesthetics
- compress thesis content into background -> objective -> method -> core findings -> innovation/value -> limitations/future work -> thanks/Q&A
- prefer visual evidence suggestions over dense bullet dumping
