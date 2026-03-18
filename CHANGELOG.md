# Changelog

All notable changes to this repository are documented in this file.

## 2026-03-18

### Added
- published `cycwrite` to GitHub as a standalone repository
- added a detailed `README.md` covering:
  - repository purpose
  - capability areas
  - repository layout
  - installation paths
  - CLI usage
  - testing guidance
  - known limitations
- added `scripts/smoke_test.py` for repeatable repository-level smoke checks

### Changed
- expanded `SKILL.md` routing to include stronger paper-production and review-project distinctions
- added `paper-production family` routing language
- added paper submodes including:
  - `outline-only`
  - `abstract-only`
  - `citation-check`
  - `format-convert`
  - `revision-coach`
- added review-project output-level gating to distinguish:
  - `submission-grade review draft`
  - `review-grade evidence synthesis`
  - `evidence map / scoping output`
  - `framework memo / review outline`

### Updated references
- `references/literature-search-and-screening.md`
- `references/section-workflows.md`
- `references/review-routing-and-gates.md`
- `references/review-and-submission.md`

### Verification
- repository-level smoke checks were rerun successfully for:
  - Python script compilation
  - CLI help output
  - project scaffold initialization
  - project status inspection
  - gate report generation

### Notes
- harness-level live skill-routing regression was retried separately through an alternate agent path and produced successful route-specific outputs for:
  - outline-only behavior
  - revision-coach behavior
  - review-output downgrading behavior
