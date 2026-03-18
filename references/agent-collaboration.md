# Agent Collaboration for cycwrite

## Purpose

This file defines how companion agents, scripts, and the `cycwrite` skill collaborate without collapsing into one monolithic system.

## Layering Rule

- provider adapters handle source-specific access, retries, browser automation, and export capture
- agents execute stage work
- scripts normalize or compute
- templates record state and handoffs
- `cycwrite` defines writing rules, safety, routing, and evidence-faithful transformation

## Recommended Stage Order

1. retrieval
2. screening
3. evidence extraction
4. decision loop
5. writing
6. final gate / packaging

## State Driver

Use `scripts/session_state_driver.py <project_dir>` to inspect the current stage and missing required files.

Use `scripts/session_state_driver.py <project_dir> --advance` only after the current stage is ready and you intentionally want to move the manifest to the next stage.

This keeps the ecosystem lightweight while still giving it a concrete staged state machine.

## Recommended File Contracts

### Retrieval -> Screening
- `candidate_pool.csv`
- `session_manifest.md`
- `search_strategy.md`
- provider adapter config or workflow file when retrieval depends on a browser workstation or API signature

### Screening -> Evidence Extraction
- `title_abstract_screening.csv`
- `fulltext_acquisition.csv`
- `fulltext_screening.csv`
- `fulltext_review_register.csv`
- `gate_report.md`

### Evidence Extraction -> Writing
- `gate_report.md`
- `decision_packet.md`
- `proceed_case.md`
- `refine_case.md`
- `pivot_case.md`
- `decision_record.md`
- `evidence_extraction.csv`
- `claim_mapping.md`
- `outline.md`
- `visual_evidence_pack.md`

### Writing -> Final Gate
- `draft_sections.md`
- `deliverables_manifest.md`
- `gate_checklist.md`
- `sentinel_watch_report.md`
- `citation_authenticity_report.md`

## Interaction Rule

The writing coordinator should not redo retrieval or screening work.
The retrieval and screening agents should not pretend to write final scholarly prose.
The retrieval layer may use official APIs, authorized browser sessions, or manual export/import loops, but it must hand downstream agents normalized artifacts rather than brittle click-by-click state.
Each agent updates the session manifest so downstream agents know which artifacts are authoritative.

## Practical Mapping to scitex / AutoResearchClaw Style Systems

The closest mapping is:

- retrieval/scholar subsystem -> `cycwrite-retrieval-orchestrator`
- provider-specific API or browser access layer -> retrieval adapters coordinated by `cycwrite-retrieval-orchestrator`
- screening / evidence-state subsystem -> `cycwrite-screening-analyst`
- structured knowledge extraction -> `cycwrite-evidence-extractor`
- proceed / refine / pivot debate -> `cycwrite-proceed-advocate`, `cycwrite-refine-advocate`, `cycwrite-pivot-advocate`, `cycwrite-decision-synthesizer`
- sentinel / consistency watchdog -> `cycwrite-sentinel-watchdog`
- citation authenticity audit -> `cycwrite-citation-authenticity-auditor`
- downstream manuscript writer / reviewer -> `cycwrite-writing-coordinator` + `cycwrite`

This preserves the valuable part of those systems: staged artifact-driven collaboration.

For a fully auditable debate loop, do not stop at `decision_record.md`; keep all three stance files so later reviewers can inspect why a project proceeded, refined, or pivoted.

## Boundary

Do not turn `cycwrite` into a full autonomous experiment platform.
Do not turn `cycwrite` into a browser-automation monolith either.
Use this collaboration model to keep writing standards strong while execution remains modular.

When browser automation is required, keep selectors, login/profile assumptions, and download behavior in adapter config files rather than scattering them through the writing-facing skill text.
