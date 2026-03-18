# academic-write-all-skill

`academic-write-all-skill` is an academic writing orchestration skill for OpenCode and OpenClaw.

It is designed to route users to the right writing workflow before generating prose. Instead of behaving like a single long prompt, it acts as a standards and routing layer for staged academic work: paper planning, section drafting, literature search and screening, review-project gating, revision coaching, submission preparation, and evidence-aware writing.

## What It Does

`academic-write-all-skill` is built around one core rule:

> Do not let polished prose outrun verified evidence.

In practice, that means the skill tries to answer three questions before drafting:

1. What stage is the user actually in?
2. What type of academic artifact are they trying to produce?
3. How strong is the evidence or material they already have?

From there, it routes into the narrowest honest workflow instead of defaulting to full-body drafting.

## Main Capability Areas

### 1. Paper-production workflows
Use these when the task is article- or thesis-centric:

- topic framing and proposal support
- paper outline generation
- chapter-by-chapter planning
- section drafting for `Introduction`, `Methods`, `Results`, `Discussion`, `Abstract`, and `Conclusion`
- thesis / dissertation chapter workflows
- abstract rewriting
- citation checks
- format-convert awareness
- revision-coach mode for messy reviewer comments

### 2. Review-project workflows
Use these when the task is review-corpus-centric:

- review-type routing
- search strategy planning
- candidate-pool design
- title / abstract screening
- full-text screening and evidence extraction
- claim-to-evidence mapping
- review output-level downgrading when the corpus is weak

### 3. Late-stage operations
Use these when the paper already exists and the job is narrower:

- polishing and rewriting
- translation
- anti-AI-tone cleanup
- reviewer response packages
- response matrices
- re-review checks
- journal-fit triage
- pre-submission review

## Why This Skill Exists

Many academic writing assistants fail in predictable ways:

- they draft full prose too early
- they invent citation-like content
- they overstate novelty or certainty
- they treat a review article like a normal section-writing task
- they confuse full drafting with revision planning
- they ignore whether the user has enough evidence for the deliverable they asked for

`academic-write-all-skill` is designed to reduce those failure modes by treating academic writing as a staged workflow with explicit integrity constraints.

## Skill Design Philosophy

The repository follows a layered design:

- `SKILL.md` contains the lightweight routing layer
- `references/` contains the heavy rules and deeper workflows
- `scripts/` contains reusable project and retrieval helpers
- `assets/templates/` contains artifact templates for structured review and writing workflows

This separation keeps the main skill readable while still supporting complex academic workflows.

## Repository Layout

```text
academic-write-all-skill/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── evals/
├── requirements-cycwrite.txt
├── bootstrap_cycwrite_runtime.bat
├── cycwrite.bat
├── references/
├── scripts/
└── assets/templates/
```

### Important files

#### Core skill
- `SKILL.md`
  - Main routing logic
  - Trigger coverage
  - stage-aware workflow selection
  - integrity rules
  - default subworkflow mapping

#### Evals
- `evals/evals.json`
  - reusable live routing prompts for regression testing
  - currently covers outline-only, revision-coach, and review-output downgrade behavior

#### Reference guides
- `references/literature-search-and-screening.md`
  - search planning, source routing, screening, extraction, citation governance
- `references/section-workflows.md`
  - deep rules for section drafting and section-specific constraints
- `references/review-routing-and-gates.md`
  - review-type routing and evidence thresholds
- `references/review-and-submission.md`
  - journal fit, pre-review, revision-coach, response packages, submission logic
- `references/quality-and-integrity.md`
  - anti-hallucination and evidence-discipline rules
- `references/microtasks-and-operations.md`
  - smaller high-frequency writing tasks

#### Scripts
- `scripts/cycwrite_cli.py`
  - unified CLI entrypoint for runtime helpers
- `scripts/init_review_project.py`
  - initialize a review-writing project scaffold
- `scripts/import_and_dedupe_candidates.py`
  - normalize candidate-pool inputs and mark duplicates
- `scripts/generate_gate_report.py`
  - compute gate status for a cycwrite project
- `scripts/session_state_driver.py`
  - inspect staged project readiness
- `scripts/citation_authenticity_sentinel.py`
  - run citation-authenticity checks against project artifacts

#### Templates
- `assets/templates/*.csv`
  - candidate pool, screening, and evidence extraction tables
- `assets/templates/*.md`
  - outlines, claim maps, decision packets, gate checklists, review artifacts
- `assets/templates/*.json`
  - browser workflow examples and provider configs

## Recently Integrated Capabilities

This version explicitly absorbs capability families from `cycwrite`, the earlier paper/review skills, and the legacy `academic-write` repository:

### From paper-production systems
- stronger outline-first routing
- abstract-only and abstract-rewrite handling
- citation-check awareness
- format-convert awareness
- revision-coach behavior for reviewer-comment triage

### From review-project systems
- review output-level gating
- corpus-first review logic
- stronger downgrade honesty when evidence is insufficient
- candidate pool -> screening -> extraction -> framework -> writing sequencing

The result is that the skill is no longer only a writing router. It is now a more complete academic workflow router that can distinguish:

- full drafting vs outline-only work
- manuscript revision vs revision-roadmap planning
- submission-grade review vs evidence map / framework memo
- early research lifecycle work vs stable manuscript work

## Installation

### One-command install for OpenCode

Project-scoped install:

```bash
npx skills add family3253/academic-write-all-skill -a opencode
```

Global install:

```bash
npx skills add family3253/academic-write-all-skill -a opencode -g
```

### One-command install for OpenClaw

Project-scoped install:

```bash
npx skills add family3253/academic-write-all-skill -a openclaw
```

Global install:

```bash
npx skills add family3253/academic-write-all-skill -a openclaw -g
```

Fallback for environments still using the older package name:

```bash
npx add-skill family3253/academic-write-all-skill --agent opencode
```

Typical install targets:
- OpenCode project: `.agents/skills/`
- OpenCode global: `~/.config/opencode/skills/`
- OpenClaw project: `skills/`
- OpenClaw global: `~/.openclaw/skills/`

### Runtime helper setup

### Option 1: Use the Windows bootstrap scripts

If you want the runtime helpers available locally:

```bat
bootstrap_cycwrite_runtime.bat
```

This script:
- creates a local virtual environment in `.venv`
- upgrades `pip`
- installs pinned dependencies from `requirements-cycwrite.txt`
- installs Chromium for Playwright

Then use:

```bat
cycwrite.bat <command> [...args]
```

### Option 2: Manual Python setup

```bash
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements-cycwrite.txt
.venv\Scripts\python -m playwright install chromium
```

## CLI Usage

The runtime CLI is implemented in `scripts/cycwrite_cli.py`.

### Show help

```bash
python scripts/cycwrite_cli.py --help
```

### Available commands

- `bootstrap`
- `ipubmed`
- `cnki`
- `doi-flow`
- `handoff`
- `project-init`
- `project-status`
- `project-gate`

### Examples

Initialize a review project scaffold:

```bash
python scripts/cycwrite_cli.py project-init my-review-project
```

Generate a gate report for an existing project:

```bash
python scripts/cycwrite_cli.py project-gate my-review-project
```

Inspect current project state:

```bash
python scripts/cycwrite_cli.py project-status my-review-project
```

Run the DOI acquisition flow:

```bash
python scripts/cycwrite_cli.py doi-flow 10.1000/example-doi \
  --candidate-output candidate_pool.csv \
  --acquisition-output fulltext_acquisition.csv \
  --text-output artifact.txt
```

## How To Use The Skill In Practice

Typical user prompts that should route well now include:

- `我有研究结果，但还不知道论文怎么搭结构。请先帮我列一个论文提纲，不要直接写正文。`
- `我收到一堆审稿意见，很乱。先别帮我写回复信，先帮我整理成修订路线图和 response matrix 骨架。`
- `我想写一篇投稿级综述，但我现在只有十几篇文献和一个很粗的主题。你先判断应该写到什么层级。`
- `帮我检查这篇稿子的引用有没有明显问题。`
- `帮我把摘要重写得更贴合正文，不要新增事实。`

The expected behavior is not always to draft. Often the correct first move is to:

- stabilize the outline
- downgrade the output level
- request missing evidence
- build a revision roadmap
- produce a claim-to-evidence matrix

## Testing

### Live routing evals

The repository now includes `evals/evals.json`, which stores the three prompts already confirmed in harness-level live routing regression:

- outline-only routing
- revision-coach routing
- review-output downgrade routing

These are intended for rerunning assistant-level behavior checks in future sessions.


### What was re-tested for this repository

This repository was re-tested at the repository/runtime level using commands that are actually executable in this environment.

Recommended checks:

```bash
python -m compileall scripts
python scripts/cycwrite_cli.py --help
python scripts/cycwrite_cli.py project-init tmp-project --force
python scripts/cycwrite_cli.py project-status tmp-project
python scripts/cycwrite_cli.py project-gate tmp-project
```

These checks validate:
- Python syntax for bundled scripts
- CLI parser integrity
- project scaffold initialization
- session state inspection
- gate report generation

### Skill-behavior testing status

There is an important distinction between:

1. **repository/runtime tests**
2. **live skill-routing behavior tests inside the assistant harness**

Repository/runtime checks are executable locally.

The latest successful harness retry produced correct live routing behavior for three high-value prompts:
- outline-only behavior
- revision-coach behavior
- review-output downgrade behavior

Those prompts are now stored in `evals/evals.json` for reuse.

## Known Limitations

- This repository does not guarantee that external source access is available at runtime.
- Browser-assisted workflows still depend on real sessions, permissions, and environment health.
- The skill is strong at routing and standards, but it does not magically make weak evidence publication-ready.
- Review-grade work still depends on actual corpus quality, screening discipline, and evidence completeness.
- Harness-level skill-behavior testing may fail even when the repository code and skill files are valid, if the model backend is misconfigured.

## Safety and Integrity Rules

`cycwrite` is intentionally conservative in several areas:

- no fabricated references
- no invented statistics
- no unsupported novelty claims
- no fake journal-fit certainty
- no pretending a weak corpus is submission-grade
- no claiming access to full text unless the artifact is really present

If evidence is incomplete, the correct output is a downgraded or placeholder-bearing deliverable, not overconfident academic prose.

## Development Notes

### What is intentionally not in the repository root

The uploaded repository excludes:

- `.venv/`
- `__pycache__/`
- `*.pyc`

These are runtime artifacts, not source.

### Git publishing note

The public GitHub upload was prepared from a clean workspace copy so the repository would reflect source and templates rather than local environment noise.

## Recommended Next Steps

If you continue evolving this skill, the highest-value next steps are:

1. document provider-specific prerequisites for CNKI / Wanfang / browser workflows more explicitly
2. add sample review-project directories for end-to-end dry runs
3. add quantitative grading around `evals/evals.json`
4. package release artifacts for easier cross-agent distribution

## Repository

GitHub repository:

- `https://github.com/family3253/academic-write-all-skill`
