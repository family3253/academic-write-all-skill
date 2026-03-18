# External Project Absorption Map for cycwrite

## Guiding Rule

The following external projects can be absorbed into `cycwrite` at the level of:
- capability patterns
- routing intelligence
- workflow design
- quality standards
- safe operating rules

They should **not** be absorbed as wholesale copied systems.

## 1. scitex-python

### What can be absorbed
- reproducible research mindset
- session-based organization of analysis and writing artifacts
- connection between data / stats / figures / writing
- tool-platform awareness for end-to-end academic workflows
- manuscript support that respects upstream evidence and generated outputs

### What should not be copied wholesale
- full Python platform architecture
- broad module namespace design
- MCP server internals
- optional dependency sprawl

### How it strengthens cycwrite
- makes `Methods`, `Results`, and figure-aware writing more evidence-grounded
- reinforces the rule that manuscript drafting should respect upstream analytical artifacts
- strengthens the concept that academic writing is downstream of structured research outputs, not isolated prose generation

## 2. Auto-claude-code-research-in-sleep (ARIS)

### What can be absorbed
- research -> review -> revise automation mindset
- iterative paper improvement loops
- skill-chaining / workflow composition thinking
- idea-discovery to experiment-plan to paper-writing continuity
- external-review-aware revision logic

### What should not be copied wholesale
- exact orchestration commands
- environment-specific automation assumptions
- overnight autonomous execution claims
- model-specific operational dependencies

### How it strengthens cycwrite
- upgrades `cycwrite` from writing skill to lifecycle-aware writing skill
- strengthens revision, re-review, and reviewer-response subworkflows
- improves stage diagnosis for users who are somewhere between idea, draft, review, and revision

## 3. academic-research-skills

### What can be absorbed
- rigorous academic workflow framing
- explicit integrity and citation discipline
- paper writing / review / pipeline separation of concerns
- guided planning and paper-structure coaching
- stronger academic quality gates before output

### What should not be copied wholesale
- full agent-team design
- exact pipeline internals and all modes verbatim
- large prompt blocks without adaptation

### How it strengthens cycwrite
- improves paper-mode routing
- strengthens bilingual abstract and paper-planning awareness
- improves editorial-review and revision-roadmap logic
- reinforces integrity-first drafting and stage-aware writing

## 4. research-plugins

### What can be absorbed
- plugin-style breadth of academic micro-capabilities
- modular research skill taxonomy
- large-scope resource organization mindset
- distinction between reusable skills, API wrappers, and reference-only configs

### What should not be copied wholesale
- all plugin contents as one giant mega-skill
- reference-only configs pretending to be executable guarantees
- count-driven breadth without coherent routing

### How it strengthens cycwrite
- justifies splitting heavy capabilities into reference files and future subskills
- improves modularization of review, submission, translation, and citation operations
- supports treating `cycwrite` as a hub skill rather than a monolith

## 5. humanizer (local skill source)

### What can be absorbed
- pattern-based detection of AI-sounding prose
- avoidance of inflated symbolism, promo tone, vague attributions, and formulaic cadence
- rhythm variation and voice repair
- anti-pattern inventory for late-stage polishing

### What should not be copied wholesale
- full personality-writing philosophy in contexts requiring strict neutrality
- over-humanization that changes technical precision

### How it strengthens cycwrite
- sharpens `Revision / Polishing Mode`
- strengthens anti-AI-tone rewriting without sacrificing academic accuracy
- helps distinguish clean, human academic prose from generic LLM polish

## 6. PRISMA / PRISMA-S guidance sources

### What can be absorbed
- reporting awareness for search documentation
- record-flow thinking across identification, screening, eligibility, and inclusion
- explicit recoverability of exclusion reasons and source lists
- distinction between doing a search and reporting a search transparently

### What should not be copied wholesale
- pretending cycwrite is a standards-compliance engine
- claiming PRISMA or PRISMA-S compliance without the underlying records

### How it strengthens cycwrite
- improves literature-search-and-screening outputs for review-grade work
- adds traceable project-artifact expectations without turning cycwrite into a full review platform

## 7. scitex-python

### What can be absorbed
- modular research-system thinking: scholar -> stats -> figures -> writer -> verify
- session-based artifact organization from upstream evidence to downstream manuscript outputs
- strong separation between tool substrate and orchestration layer
- reproducibility-aware handoff between retrieval, analysis, visualization, and writing
- agent-facing interface design where tools expose structured outputs and writing happens downstream of those outputs

### What should not be copied wholesale
- the full Python platform scope
- the entire MCP server/tool surface
- environment-heavy installation and configuration assumptions
- statistics / plotting / dataset subsystems unrelated to cycwrite's core mission

### How it strengthens cycwrite
- clarifies that `cycwrite` should sit above retrieval / analysis / figure tools as the writing-and-evidence coordination layer
- strengthens project-session thinking so writing outputs stay linked to search, screening, extraction, and figure artifacts
- justifies pairing `cycwrite` with agent orchestration instead of bloating the skill itself into a monolithic automation stack

## 8. academic-write (legacy repository)

### What can be absorbed
- research-lifecycle continuity from idea discovery to paper planning
- novelty-check framing before premature drafting
- stronger linkage between literature review, experiment/result packaging, and manuscript writing
- iterative review and paper-improvement mindset
- paper-plan, paper-write, paper-compile, and figure-aware workflow coordination patterns

### What should not be copied wholesale
- the entire old repository as a second monolith
- all vendored skills as separate subskills inside the main package
- external tool wrappers pretending to be guaranteed runtime support
- environment-specific orchestration assumptions from the legacy project

### How it strengthens academic-write-all-skill
- upgrades the skill from writing-aware to research-lifecycle-aware
- improves stage diagnosis before a manuscript fully exists
- supports idea -> literature -> experiment/result -> paper transitions without overpromising automation

## Absorption Outcome for cycwrite

After absorbing these projects conceptually, `cycwrite` becomes:
- more lifecycle-aware (`ARIS`, `academic-research-skills`)
- more reproducibility-aware (`scitex-python`)
- more modular and extensible (`research-plugins`)
- more natural in late-stage prose cleanup (`humanizer`)
- more transparent in review-grade literature-search reporting (`PRISMA`, `PRISMA-S`)
- better positioned as an orchestration-ready writing layer above a broader research tool substrate (`scitex-python`)

## Non-Negotiable Boundary

`cycwrite` must remain coherent.
It should absorb:
- standards
- routing
- heuristics
- quality controls
- reference structures

It should not become:
- a full coding platform
- a giant copy of multiple skill repos
- an unreadable prompt warehouse
