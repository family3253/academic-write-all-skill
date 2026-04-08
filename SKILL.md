---
name: academic-write-all-skill
description: Use when planning, ideating, checking novelty, outlining, drafting, revising, translating, reviewing, formatting, or preparing submission materials for an academic paper, thesis chapter, literature review, scoping review, systematic review, journal manuscript, or reviewer-response package. Especially useful when the user has scattered notes, partial sections, evidence gaps, target-journal constraints, reviewer comments, or needs a stage-based academic writing workflow with citation discipline, anti-hallucination safeguards, claim-to-evidence traceability, review-grade corpus gating, journal-fit triage, format-convert awareness, reviewer-response packaging, experiment-to-writing handoff, and re-review readiness checks.
---

# academic-write-all-skill

## Overview

`academic-write-all-skill` is a unified academic-writing orchestration skill.

Its governing principle is: **write in stages, route by task type, and never let polished prose outrun verified evidence**. High-quality academic writing depends on structure, evidence control, genre routing, journal fit, revision logic, and submission readiness—not just elegant sentences.

This skill supports Chinese, English, and bilingual workflows across journal manuscripts, theses, proposals, literature reviews, evidence reviews, cover letters, reviewer-response packages, outline-first paper planning, abstract-only work, citation-check passes, late-stage format-convert tasks, and idea-to-paper lifecycle planning.

It also supports a guarded self-update behavior: when its own absorbed capability set is not enough, it should first route to stronger local skills and bundled references, then learn cautiously from GitHub or official external implementations, while keeping all new outputs evidence-bound and clearly labeled.

## When to Use

Use this skill when the user needs help with any of the following:

- topic ideation, research-question refinement, or proposal framing
- research idea discovery, novelty-check framing, or literature-to-idea narrowing
- literature reading, literature search strategy, evidence synthesis, or review-article planning
- Chinese thesis retrieval, CNKI/Wanfang/university repository discovery, or learning from authorized thesis exports and PDFs
- thesis statement sharpening, outline building, and argument structuring
- master's thesis / dissertation chapter planning, chapter-level drafting, or thesis-to-manuscript adaptation
- section drafting: `Introduction`, `Methods`, `Results`, `Discussion`, abstract, conclusion
- title, keywords, highlights, graphical abstract copy, or cover letter drafting
- thesis title optimization, thesis abstract pair drafting, acknowledgment drafting, or defense-PPT storyline planning
- experiment-to-writing handoff, result interpretation planning, or figure/compile-aware writing coordination
- translation, polishing, shortening, rewriting, anti-AI-tone revision, or style repair
- similarity-reduction rewriting, paragraph-level diagnosis-first polishing, or staged reference-format checking
- pre-submission review, journal-fit evaluation, or acceptance-risk triage
- reviewer comment response, revision mapping, and rebuttal writing
- paper outline generation, chapter-by-chapter planning, abstract-only drafting, citation-check, or format-convert requests
- review-type routing for narrative, scoping, systematic, umbrella, critical, or prediction-model reviews
- literature-search and screening workflows for related work, review corpora, evidence matrices, and prediction-model appraisal tables
- literature-search and screening workflows for related work, review corpora, evidence matrices, PRISMA-style record tracking, and review-project artifacts
- high-frequency academic microtasks such as grammar checks, reference-format checks, logic repair, and statistics-to-prose conversion

Do **not** use this skill for purely mechanical formatting if a narrower formatting skill already covers the task fully.

## Core Operating Rule

Always determine **what stage the user is actually in** before generating text.

Bad pattern:
- user asks for polished prose
- assistant skips missing evidence, structure, and genre decisions
- output sounds academic but is weak, generic, or unverifiable

Good pattern:
1. identify genre and stage
2. inspect available materials
3. locate missing critical information
4. choose the right subworkflow
5. draft or revise only at the right level
6. run integrity and overclaim checks

When tables, figures, legends, or statistical outputs are available, treat them as first-class evidence artifacts rather than background attachments.

## Routing Flow

```text
Need help with topic or proposal?
  -> ideation / proposal mode
Need to go from idea discovery or novelty check into a paper plan?
  -> research lifecycle mode
Need help organizing paper logic?
  -> outline / argument mode
Need a paper plan, abstract, citation check, or format convert?
  -> paper-production submode selection
Need one manuscript section?
  -> section drafting mode
Need a review article?
  -> review-type routing first
Need a clinical prediction model review or nomogram/risk-score appraisal?
  -> prediction-model review mode
Already have a draft?
  -> revision / polishing mode
Ready to submit?
  -> submission / pre-review mode
Received reviewer comments?
  -> rebuttal / revision-response mode
Need a narrow late-stage operation?
  -> microtask / operations mode
```

## Stage 0: Intake and Constraints

Collect as much of the following as available:

- document type: article / thesis / proposal / review / rebuttal / cover letter
- discipline and subfield
- target journal / conference / degree context / funding context
- language: Chinese / English / bilingual
- citation style if required
- current stage: idea / outline / partial draft / full draft / revision after review
- available materials: title, abstract, notes, figures, legends, tables, methods, results, references, reviewer comments
- available materials: title, abstract, notes, figures, legends, tables, methods, results, references, reviewer comments, thesis outline, school template examples, OCR lecture notes, or chapter summaries
- retrieval assets if applicable: export CSVs, EndNote/Zotero libraries, institutional access, authorized browser sessions, or provider workstations
- thesis context if applicable: monograph thesis / article-based thesis / chapter-based thesis, degree level, university or department rules, required front matter / back matter, chapter order
- hard constraints: word count, section rules, journal scope, deadline, audience

If key information is missing, ask only for the minimum needed to move to the correct subworkflow.

## Stage 1: Non-Negotiable Safeguards

Always enforce these rules:

1. **No fabricated references, statistics, or factual claims.**
2. **Separate verified facts from inferred placeholders.**
3. **If a citation cannot be verified, mark it for confirmation instead of inventing it.**
4. **Do not overclaim novelty, causality, robustness, or policy/clinical impact.**
5. **Prefer explicit uncertainty over confident hallucination.**
6. **Maintain traceability between user evidence and drafted prose.**
7. **Maintain comment -> action -> location traceability** whenever drafting rebuttals, revision roadmaps, or resubmission materials.
8. **Reduce obvious AI writing patterns** instead of simply making the text longer or fancier.
9. **Do not describe unstable or unauthorized retrieval as verified source access.**

### Integrity Red Flags

Stop and verify when you see:
- exact numbers with no visible source
- broad literature claims with no anchors
- `first`, `novel`, `robust`, `significant`, `effective` claims lacking support
- methods prose that appears more detailed than the provided material
- reviewer responses claiming revisions not actually made
- journal-fit judgments based only on prestige or impact factor

**REQUIRED REFERENCE:** Use `references/quality-and-integrity.md` whenever the task involves citation-sensitive writing, statistical interpretation, translation, polishing, or reviewer-response drafting.

## Stage 2: Choose the Working Mode

Before choosing the detailed mode, decide which of these three families the task belongs to:
- **paper-production family** — article, thesis chapter, abstract, outline, format conversion, or revision roadmap for a manuscript
- **review-project family** — narrative / scoping / systematic / umbrella / critical review with corpus, screening, and evidence-gate questions
- **late-stage operations family** — polishing, citation cleanup, reviewer response, or submission preparation

If the user is still moving from idea -> novelty -> literature -> experiment/result framing -> paper drafting, treat that as a research-lifecycle task first rather than jumping straight into manuscript prose.

### A. Ideation / Proposal Mode
Use when the user is still defining the project.

Typical outputs:
- topic directions
- proposal skeleton
- opening report structure
- research gap statement
- contribution options
- thesis statement candidates

### A2. Research Lifecycle Mode
Use when the user is not merely asking for prose, but for help moving through the broader academic pipeline from early idea to paper-ready writing inputs.

Typical outputs:
- idea shortlist
- novelty-check plan
- literature-to-gap memo
- experiment/result packaging memo
- paper plan handoff
- review loop recommendation

This mode is where absorbed `academic-write` capabilities matter most. It should connect:
- idea discovery
- novelty checks
- literature review
- result analysis
- figure / compile awareness
- iterative review and polishing

without pretending all of those steps are fully automated inside one prompt.

### B. Outline / Argument Mode
Use when the topic exists but the manuscript logic is not stable.

Typical outputs:
- IMRaD outline
- review-article outline
- thesis chapter structure
- paragraph plan
- claim-to-evidence map
- chapter purposes and transition logic

### C. Section Drafting Mode
Use when the user requests one concrete section.

Available section families:
- `Introduction`
- `Methods`
- `Results`
- `Discussion`
- `Abstract`
- `Conclusion`
- `Thesis chapter introduction / findings / general discussion / thesis conclusion`
- `Title / Keywords / Highlights`
- `Acknowledgments`
- `Defense PPT storyline / speaking outline`

**REQUIRED REFERENCE:** Use `references/section-workflows.md` for deep section rules.

### C2. Thesis / Dissertation Mode
Use when the requested output is a master's thesis chapter, dissertation chapter, thesis proposal chapter, article-based thesis wrapper chapter, or thesis-level restructuring task.

Typical outputs:
- thesis architecture memo
- chapter-by-chapter outline
- chapter purpose map
- thesis introduction or literature review chapter
- methods chapter adapted from paper-style materials
- findings/results chapter from tables, figures, or coding outputs
- general discussion chapter
- final conclusion, implications, limitations, and future-work chapter
- thesis abstract / executive summary

Core distinctions to keep in mind:
- a thesis is not just a longer paper
- chapter purpose and cross-chapter transitions matter explicitly
- thesis chapters can tolerate more context-setting than journal sections, but still need evidence discipline
- article-based theses need wrapper logic that explains how chapters connect

**REQUIRED REFERENCES:**
- `references/section-workflows.md`
- `references/review-and-submission.md` when the thesis is being converted into papers or submission materials

### D. Literature Search / Screening Mode
Use when the user needs literature retrieval planning, query design, candidate corpus construction, screening logic, or evidence extraction before or during writing.

Typical outputs:
- search strategy memo
- concept groups and keyword expansion
- database/source routing
- candidate paper table
- screening criteria
- evidence matrix
- DOI cleanup and citation-governance prep

**REQUIRED REFERENCES:**
- `references/literature-search-and-screening.md`
- `references/quality-and-integrity.md`
- `references/review-routing-and-gates.md` when the search supports a review article

### D1. Chinese Thesis Retrieval / Learning Mode
Use when the user needs Chinese dissertation or master's-thesis discovery, institution-filtered thesis search, browser-assisted export workflows, or wants to learn from authorized thesis full text before writing.

Typical outputs:
- provider plan distinguishing official API, authorized browser workflow, and manual export fallback
- CNKI / Wanfang / institutional repository search strategy
- candidate pool with thesis metadata such as degree level, granting institution, advisor, and thesis type
- access-state notes separating metadata discovery, authorized full-text access, export availability, and manual follow-up
- thesis-to-manuscript learning memo showing what structures, methods descriptions, result framing, or chapter patterns are worth reusing

Hard rules:
- prefer official APIs and direct exports before browser automation
- use browser automation only with an existing authorized session, institution access, or user-owned workstation
- keep anti-bot, retries, and session persistence in the retrieval layer rather than inside writing logic
- never claim full-text learning succeeded unless the acquired artifact is present and readable

**REQUIRED REFERENCES:**
- `references/literature-search-and-screening.md`
- `references/agent-collaboration.md`
- `references/quality-and-integrity.md`

### D2. Review-Article Mode
Use when the requested document is a review, evidence map, scoping review, systematic review, umbrella review, critical/theoretical review, or prediction-model review.

Before writing prose, decide:
- what type of review it is
- whether strong evidence claims are justified
- what body framework should organize the review
- whether the evidence base is sufficient for a submission-grade draft
- whether the task is actually a prediction-model appraisal/review rather than a generic topic synthesis

**REQUIRED REFERENCES:**
- `references/review-routing-and-gates.md`
- `references/review-and-submission.md`
- `references/section-workflows.md`
- `references/prediction-model-review.md` when the review centers on scores, nomograms, clinical prediction, or risk stratification tools

### D3. Review-Project Output Level
When the user wants a review, explicitly choose the strongest honest output level before drafting:

- `submission-grade review draft` — only when scope, corpus, framework, and claim-to-evidence support are visibly strong
- `review-grade evidence synthesis` — evidence is substantial enough for frameworked synthesis, but not yet for a polished submission draft
- `evidence map / scoping output` — useful mapping of what exists, where clusters sit, and where the gaps are
- `framework memo / review outline` — structure and writing logic are ready, but the evidence base is not yet stable

If the corpus, screening record, or evidence coverage is weak, downgrade explicitly instead of writing a pseudo-submission-grade review.

### D4. Prediction-Model Review Mode
Use when the user is reviewing clinical scores, nomograms, machine-learning models, or other prediction tools rather than a disease topic alone.

Typical outputs:
- prediction-model evidence map
- model appraisal table
- review-grade synthesis of model families
- gap memo on validation / calibration / transportability
- structure for a later full review

Core extraction dimensions:
- target population and clinical setting
- organism or resistance phenotype target
- predicted outcome
- model type (`score`, `nomogram`, `ML`, `other`)
- predictors used
- derivation vs internal validation vs external validation
- discrimination / calibration / clinical utility if reported
- major bias or transportability concerns

Hard rules:
- do not merge all prediction studies into one narrative if targets and settings differ too much
- distinguish risk-factor studies from actual deployable prediction models
- do not infer good model quality from a nomogram figure alone
- if methodological appraisal exceeds native coverage, explicitly borrow a local skill or external reporting/appraisal pattern and label it

### E. Revision / Polishing Mode
Use when a draft already exists.

Revision dimensions may include:
- logic repair
- claim-evidence alignment
- paragraph coherence
- style upgrade
- de-redundancy / shortening
- translation
- de-AI-ification
- grammar / terminology normalization
- anti-pattern cleanup for obvious AI-generated prose
- similarity-reduction rewriting that preserves facts, citations, and terminology
- diagnosis-first paragraph revision with explicit rationale

**REQUIRED REFERENCES:**
- `references/microtasks-and-operations.md`
- `references/quality-and-integrity.md`
- `references/humanization-rules.md`

### F. Submission / Review Mode
Use when the user is near submission or already in revision after review.

Outputs may include:
- journal shortlist
- journal-fit memo
- desk-reject risk memo
- pre-submission review
- acceptance-risk heuristic assessment
- cover letter
- reviewer response matrix
- response letter skeleton or full draft
- revision roadmap
- claim-evidence-citation matrix
- re-review verification memo

**REQUIRED REFERENCE:** Use `references/review-and-submission.md`.

### F2. Paper-Production Submodes
Use these submodes when the task is clearly paper-centric rather than review-corpus-centric:

- `full-draft` — build or extend a full paper or chapter set from available materials
- `outline-only` — stabilize structure, section jobs, and evidence allocation before drafting
- `abstract-only` — write or rewrite the abstract once the paper logic is sufficiently known
- `citation-check` — audit citation consistency, metadata completeness, and obvious orphan / missing-source issues
- `format-convert` — adapt between Markdown / LaTeX / DOCX expectations, citation-style expectations, or journal-facing packaging needs
- `revision-coach` — convert reviewer comments into a revision roadmap, response matrix, and execution bundle
- `figure-and-compile-aware` — keep drafting aligned with figure planning, visual evidence packs, and later paper-compilation constraints

These are routing labels, not a promise of full automation. Use the narrowest honest submode that matches the user’s stage.

### H. Paper-Workflow Awareness Mode
Use when the user is not asking for one isolated writing task, but is clearly somewhere in the broader manuscript lifecycle.

Examples:
- manuscript drafted but not integrity-checked
- reviewer comments received and revision strategy needed
- revised manuscript needs verification-style re-review
- the user needs stage diagnosis before deciding whether to write, review, revise, or finalize

This mode should think in terms of:
- draft
- integrity
- review
- revise
- re-review
- finalize

and should explicitly surface when the user really needs a handoff to a narrower specialist skill instead of more generic writing help.

without turning cycwrite into a mandatory heavyweight pipeline.

**REQUIRED REFERENCES:**
- `references/review-and-submission.md`
- `references/opencode-skill-absorption-map.md`
- `references/external-project-absorption-map.md`

### G. Microtask / Operations Mode
Use when the user needs a narrower high-frequency task rather than full drafting.

Examples:
- grammar-only check
- reference-format check
- logic repair between paragraphs
- logic repair within paragraphs
- de-duplication or paraphrase
- academic translation
- title candidates
- abstract compression
- stats-to-prose conversion
- reviewer vulnerability scan
- reference-format staging check
- thesis defense slide storyline generation
- topic feasibility filtering and reviewer-style outline logic check

**REQUIRED REFERENCE:** Use `references/microtasks-and-operations.md`.

## Default Subworkflow by Task

| User request | Default route |
|---|---|
| `帮我想选题` | Ideation / Proposal Mode |
| `帮我找研究idea` | A2 -> Research Lifecycle Mode |
| `帮我查新` | A2 -> Research Lifecycle Mode |
| `帮我写开题` | Ideation / Proposal Mode |
| `帮我搭框架` | Outline / Argument Mode |
| `帮我列论文提纲` | F2 -> `outline-only` |
| `帮我缩小选题范围` | Ideation / Proposal Mode |
| `帮我筛选最可行的论文题目` | Ideation / Proposal Mode |
| `帮我优化论文标题` | Thesis / Dissertation Mode |
| `帮我写引言` | Section Drafting -> Introduction |
| `帮我写文献综述` | Thesis / Dissertation Mode |
| `帮我写方法` | Section Drafting -> Methods |
| `帮我写结果` | Section Drafting -> Results |
| `帮我写讨论` | Section Drafting -> Discussion |
| `帮我写摘要` | Section Drafting -> Abstract |
| `帮我写英文摘要` | Section Drafting -> Abstract |
| `帮我写致谢` | Section Drafting -> Acknowledgments |
| `帮我写结论和展望` | Section Drafting -> Conclusion |
| `帮我重写摘要` | F2 -> `abstract-only` |
| `帮我写硕士论文` | Thesis / Dissertation Mode |
| `帮我搭硕士论文框架` | Thesis / Dissertation Mode |
| `帮我写论文结果章` | Thesis / Dissertation Mode |
| `帮我把实验结果整理成写作输入` | A2 -> Research Lifecycle Mode |
| `根据图表写结果` | Section Drafting -> Results |
| `根据表格写结果` | Section Drafting -> Results |
| `帮我检索文献` | Literature Search / Screening Mode |
| `帮我做文献到选题的收敛` | A2 -> Research Lifecycle Mode |
| `帮我做相关工作检索` | Literature Search / Screening Mode |
| `帮我搭检索式` | Literature Search / Screening Mode |
| `帮我筛文献` | Literature Search / Screening Mode |
| `帮我检索某院校毕业论文` | Chinese Thesis Retrieval / Learning Mode |
| `帮我学习知网/万方学位论文` | Chinese Thesis Retrieval / Learning Mode |
| `帮我做综述` | Review-Article Mode |
| `帮我做预测模型综述` | D4 -> Prediction-Model Review Mode |
| `帮我评估一个nomogram` | D4 -> Prediction-Model Review Mode |
| `帮我评估一个风险评分模型` | D4 -> Prediction-Model Review Mode |
| `帮我翻译全文` | Revision / Polishing Mode |
| `帮我润色` | Revision / Polishing Mode |
| `帮我降重` | Revision / Polishing Mode |
| `帮我收到审稿意见不知道先干嘛` | Paper-Workflow Awareness Mode |
| `帮我检查这篇稿子现在处在哪个阶段` | Paper-Workflow Awareness Mode |
| `帮我把审稿意见整理成修订路线图` | F2 -> `revision-coach` |
| `帮我做重审验证` | Submission / Review Mode |
| `帮我写response letter` | Submission / Review Mode |
| `帮我做返修说明` | Submission / Review Mode |
| `帮我做claim-evidence表` | Submission / Review Mode |
| `帮我做response matrix` | Submission / Review Mode |
| `帮我检查引用` | F2 -> `citation-check` |
| `帮我转LaTeX` | F2 -> `format-convert` |
| `帮我转换引用格式` | F2 -> `format-convert` |
| `帮我做答辩PPT提纲` | Microtask / Operations Mode |
| `帮我生成答辩讲稿` | Microtask / Operations Mode |
| `帮我根据图表推进论文写作` | F2 -> `figure-and-compile-aware` |
| `帮我检查逻辑` | Microtask / Operations Mode |
| `帮我改参考文献格式` | Microtask / Operations Mode |
| `帮我选刊` | Submission / Review Mode |
| `帮我预审稿` | Submission / Review Mode |
| `帮我回审稿意见` | Submission / Review Mode |

## Output Patterns

### Pattern 1: Minimal Missing-Info Request
Use when input is insufficient.

Ask only for the most blocking items, usually from:
- topic / working title
- target output type
- key findings or materials
- target journal or discipline

### Pattern 2: Outline First
Use when structure is unstable.

Return:
- section hierarchy
- function of each section
- missing information needed per section

### Pattern 3: Draft with Explicit Placeholders
Use when the user wants progress but materials are incomplete.

Examples:
- `[待补：样本量]`
- `[待核实：文献来源]`
- `[待补：试剂货号 / 参数 / 页码]`
- `[待确认：目标期刊格式要求]`

### Pattern 3B: Figure/Table-Driven Results Draft
Use when the user has tables, figure legends, model outputs, coding summaries, or statistical results and wants prose drafted from them.

Return in this order:
- result block heading aligned to hypothesis / figure / table / question
- one orienting sentence explaining what was tested or compared
- faithful result sentences with numbers, directions, contrasts, and uncertainty preserved
- explicit `[待核实]` markers for any hidden statistic, label, sample size, or unit not visible in the source artifact
- optional carry-forward note for what belongs in Discussion rather than Results

### Pattern 4: Revision Matrix
Use for polishing, review, or rebuttal.

Return a table with:
- issue
- why it matters
- suggested revision
- revised wording
- evidence/check needed

### Pattern 5: Claim-Evidence-Citation Matrix
Use when the user needs argument stabilization, pre-submission review, review writing, or reviewer response drafting.

Return a table with:
- claim / point
- evidence currently available
- citation or source status
- weakness / overclaim risk
- revision action
- manuscript location or intended location

### Pattern 6: Reviewer Response Package
Use when the user has editor or reviewer feedback.

Return a bundle containing:
- comment ID
- reviewer/editor point
- response stance (`accept`, `partially accept`, `reasoned disagreement`, `cannot implement`)
- action taken
- revised text or revision summary
- manuscript location
- evidence still needed
- tone risk if any

## Skill Handoff / Specialist Boundary

`academic-write-all-skill` is the routing-and-standards layer for academic writing work. It has now absorbed core paper-production patterns, review-project routing patterns, and selected research-lifecycle patterns from the older `academic-write` repository, but it still should not pretend to be every specialist tool at once. When a task becomes clearly specialist, keep the writing workflow coherent but hand off mentally to the narrower capability pattern:

- use `citation-management` logic when the bottleneck is DOI lookup, metadata normalization, deduplication, or export-ready references
- use `academic-paper-reviewer` logic when the user needs a structured external-style review rather than drafting help
- use `latex-compile-qa` logic when the bottleneck is LaTeX compilation or bibliography build failure
- use `venue-templates` logic when the user needs venue-specific formatting constraints rather than generic prose help
- use `humanizer` logic when the late-stage need is de-AI-ification or voice repair without changing evidence content
- use research-pipeline style logic when the user is still doing idea discovery, novelty checking, or broad research-to-paper planning before a stable manuscript exists
- use `research-lit`, `arxiv`, or `pubmed-database` logic when the bottleneck is active retrieval depth rather than writing-stage synthesis
- use `cycwrite-retrieval-orchestrator` logic when the bottleneck is provider routing, authorized browser workflows, export normalization, or access-state management

Within `cycwrite`, do not fake execution of those specialist functions. Instead, adopt their standards, ask for the minimum missing material, keep outputs traceable, and downgrade the output level when the evidence or runtime substrate is not actually present.

## Capability Gap / Self-Update Handling

When the requested task exceeds what `academic-write-all-skill` can safely do with its current absorbed capability set, use this escalation order:

1. **Check bundled references and templates first**
   - read the relevant material in `references/`
   - use `references/capability-map.md`, `references/opencode-skill-absorption-map.md`, and `references/external-project-absorption-map.md` to understand what is already absorbed versus deliberately omitted
   - inspect `assets/templates/lessons_memory.md` when the task suggests a recurring gap or an improvable pattern

2. **Borrow from stronger local skills before inventing a new approach**
   - if the gap is retrieval-heavy, use `research-lit`, `pubmed-database`, `arxiv`, or `citation-management` logic
   - if the gap is review-heavy, use `academic-paper-reviewer` or review-pipeline style logic
   - if the gap is format / compile / venue specific, use `latex-compile-qa` or `venue-templates` logic
   - if the gap is install / distribution / skill-structure related, use `skill-creator`, `add-skill`, or `opencode-agent-creator` logic

3. **Only then learn from external projects or GitHub examples**
   - prefer official docs, maintained GitHub repositories, or clearly implementable patterns
   - absorb concepts and implementation patterns, not entire projects blindly
   - treat external examples as provisional learning until they are reconciled with this skill's integrity rules and routing model

4. **Record the gap and what was learned**
   - if a new pattern materially improves future handling, store it in the lessons-memory style format
   - update routing or references only when the learned pattern is stable enough to improve future outputs

### Hard rules for self-update
- never claim a new capability is native just because an external project demonstrates it
- never fabricate local-skill behavior that was not actually invoked or available
- never import GitHub patterns that weaken citation verification, evidence provenance, or downgrade honesty
- never let self-update bypass integrity gates, placeholder rules, or claim-evidence-citation traceability

### Good self-update language
- `This part exceeds the current core skill; I am borrowing the retrieval pattern from a stronger local research skill.`
- `The current package does not natively implement this step, so I am using a GitHub/official-doc pattern as a bounded reference, not as guaranteed runtime support.`
- `I can continue with a downgraded evidence-aware output now, and treat the missing capability as a future improvement target.`

## External Reference Files

- `references/literature-search-and-screening.md` — literature search strategy, screening, evidence extraction, and citation-governance handoff
- `references/humanization-rules.md` — anti-AI-tone cleanup rules adapted from local humanizer skill
- `references/opencode-skill-absorption-map.md` — absorbed capabilities from existing OpenCode skills
- `references/external-project-absorption-map.md` — absorbed capabilities from external GitHub projects and local non-OpenCode skill sources
- `references/capability-map.md` — synthesis of absorbed source families and architecture rationale
- `references/section-workflows.md` — deep section drafting rules
- `references/review-routing-and-gates.md` — review-type routing and evidence gates
- `references/review-and-submission.md` — review writing, journal selection, pre-review, rebuttal, and submission workflows
- `references/prediction-model-review.md` — prediction-model review/appraisal workflow for scores, nomograms, and risk models
- `references/microtasks-and-operations.md` — high-frequency late-stage academic operations
- `references/quality-and-integrity.md` — anti-hallucination, citation, evidence, translation, and polishing rules
- `references/agent-collaboration.md` — how companion agents, scripts, templates, and cycwrite collaborate
- `references/literature-authenticity-sentinel.md` — four-layer citation authenticity verification before writing handoff

## Bundled Concrete Assets

`cycwrite` now includes reusable concrete assets for review-grade literature workflows.

- `scripts/review_project_schema.py` — canonical field definitions for review-project CSV artifacts
- `scripts/init_review_project.py` — initialize a staged review-writing project scaffold
- `scripts/import_and_dedupe_candidates.py` — normalize external search exports into the candidate-pool schema and flag duplicates
- `scripts/generate_gate_report.py` — compute a lightweight gate report from populated project files
- `scripts/session_state_driver.py` — validate stage readiness and advance the staged workflow via `session_manifest.md`
- `scripts/build_decision_packet.py` — build a proceed/refine/pivot debate packet from current artifacts
- `scripts/synthesize_debate_loop.py` — materialize stance files and synthesize a decision record from gate/authenticity artifacts
- `scripts/sentinel_watchdog.py` — audit gate consistency and unsafe handoff states before final delivery
- `scripts/citation_authenticity_sentinel.py` — generate a four-layer citation authenticity report from project artifacts
- `assets/templates/` — ready-to-use CSV and Markdown templates for candidate pool, screening, evidence extraction, claim mapping, outline, and figure planning
- `assets/templates/research_pipeline_config.yaml` — pipeline-style stage config for cycwrite-centered multi-agent workflows
- `assets/templates/gate_checklist.md` — staged human/quality gate checklist
- `assets/templates/deliverables_manifest.md` — final output and handoff manifest
- `assets/templates/debate_packet.md` — input brief for proceed/refine/pivot debate
- `assets/templates/proceed_case.md` — persisted proceed stance output
- `assets/templates/refine_case.md` — persisted refine stance output
- `assets/templates/pivot_case.md` — persisted pivot stance output
- `assets/templates/decision_record.md` — judge/synthesizer output for debate loops
- `assets/templates/sentinel_watch_report.md` — watchdog audit output
- `assets/templates/lessons_memory.md` — lightweight self-learning memory log with time-decay metadata
- `assets/templates/citation_authenticity_report.md` — literature authenticity audit output

These assets can also track Chinese-thesis source fields and access-mode state when the project relies on CNKI, Wanfang, institutional repositories, or browser-assisted exports.

These concrete assets make `cycwrite` suitable as the standards-and-writing layer inside a larger multi-agent research workflow.

Use these when the task is concrete enough that loose notes are no longer sufficient.

## Companion Agents

`cycwrite` can now pair with companion OpenCode agents stored under `C:\Users\chenyechao\.config\opencode\agent\`:

- `cycwrite-retrieval-orchestrator`
- `cycwrite-screening-analyst`
- `cycwrite-evidence-extractor`
- `cycwrite-proceed-advocate`
- `cycwrite-refine-advocate`
- `cycwrite-pivot-advocate`
- `cycwrite-decision-synthesizer`
- `cycwrite-sentinel-watchdog`
- `cycwrite-citation-authenticity-auditor`
- `cycwrite-writing-coordinator`

Recommended split:
- agents execute and maintain project state
- the retrieval orchestrator owns provider routing, source-specific access strategy, and authorized browser handoff when needed
- debate agents stress-test whether the project should proceed, refine, or pivot
- authenticity audit checks whether citations are real, supportable, and safely bound to claims
- scripts normalize and compute
- templates record intermediate artifacts
- `cycwrite` provides the writing standards, routing logic, and evidence-faithful drafting rules

## Common Mistakes

- drafting polished prose before the outline is stable
- treating a master's thesis as if it were just a journal article with extra pages
- writing Introduction without a real gap statement
- writing Methods without adequate source details
- writing Results from memory instead of from tables, figures, legends, or statistical outputs
- mixing Results and Discussion
- translating vague Chinese into elegant but inaccurate English
- polishing style while argument structure remains weak
- recommending journals by impact factor alone
- pretending to estimate acceptance probability with false precision
- writing a review article without first deciding review type and body framework
- ignoring manuscript lifecycle stage and jumping into the wrong task mode
- treating high-frequency microtasks as if they require full-manuscript rewriting every time
- confusing metadata discovery with verified full-text access
- burying browser-access logic inside the writing stage instead of the retrieval layer

## Final Check Before Returning Output

Before delivering, verify:
- Does every strong claim have visible support?
- Is the structure right for the requested genre?
- Is any fabricated citation-like content present?
- Did Results stay separate from Discussion?
- If figures/tables were the evidence source, did the prose stay faithful to what those artifacts actually show?
- If this is a thesis task, do chapter boundaries and transitions make sense at thesis scale rather than paper scale?
- Are placeholders visible where evidence is missing?
- Did polishing introduce new facts?
- Did the output match the user’s real stage rather than the most tempting stage?
