# Section Workflows

## Purpose
This file contains the heavy reference rules for drafting and revising academic manuscript sections.

## 1. Introduction Workflow

### Use when
- the paper topic is known but the narrative opening is weak
- the user has background notes, references, or partial methods/results
- the introduction needs to be rebuilt around a sharper gap

### Canonical structure
1. broad background and significance
2. state of the art / what is already known
3. unresolved gap, contradiction, or limitation
4. study aim, research question, hypothesis, or contribution

### Hard rules
- every paragraph must have a distinct rhetorical job
- move from broad field to exact question
- avoid fake comprehensiveness (“many studies”, “numerous scholars”) without visible support
- do not spoil detailed results in the final paragraph
- if the venue is journal-specific, align with its tone and scope

### Typical input bundle
- topic or working title
- target journal or discipline
- 3-8 core references or evidence summary
- one-sentence gap statement
- method and data summary
- innovation claim

### Missing-info fallback
If references are incomplete:
- draft the structure anyway
- mark unsupported claims with `[待核实文献]`
- do not fabricate author-year citations

### Literature review rule for thesis work
When the user is writing a thesis literature review rather than a short paper introduction:
- require both `综述` and `评述`
- do not stop at listing what prior work studied
- explicitly state where the literature converges, diverges, or leaves a usable gap
- prefer moving from broad significance -> research status -> controversy/defect -> exact thesis question

## 2. Methods Workflow

### Use when
- the user has data, figures, legends, analysis outputs, or procedure notes
- the user needs a methods section ready for manuscript insertion

### Canonical structure
1. study design
2. setting / cohort / corpus / sample source
3. data collection or experimental procedure
4. variables / materials / instruments / measures
5. preprocessing / quality control
6. statistical or analytic methods
7. ethics / approval / registration if relevant

### Hard rules
- never invent parameter values, dosages, sample sizes, catalog numbers, or software versions
- infer subsection headings from available evidence, but mark missing technical details explicitly
- separate what was done from why it was done
- keep method reproducibility higher than stylistic elegance
- if tables, figure legends, or analysis scripts reveal procedure details, use them carefully as evidence for wording, but do not infer hidden settings as fact

### Recommended placeholder style
- `[待补：样本量]`
- `[待补：试剂货号]`
- `[待核实：软件版本]`
- `[待补：伦理审批编号]`

## 3. Results Workflow

### Use when
- there are tables, figure legends, statistical outputs, key findings, or hypothesis results

### Canonical structure
- organize by hypothesis, figure order, model family, or research question
- start each block with the tested objective
- report key values faithfully
- reserve interpretation for the discussion unless a brief orienting sentence is unavoidable

### Hard rules
- no inflated language (“remarkable”, “groundbreaking”) unless user explicitly wants promotional tone
- keep statistical wording aligned with actual evidence
- if only summary findings are available, say so and avoid pretending to see the full raw output

### Figure / table driven writing protocol
When figures, legends, tables, or stats outputs are the main evidence source:
1. identify the organizing order: hypothesis, figure order, table order, or research question
2. extract only visible facts first: variable names, groups, directions, magnitudes, uncertainty markers, test labels, units
3. write one orienting sentence per block to tell the reader what comparison or test is being reported
4. report the result faithfully in prose without adding interpretation that belongs in Discussion
5. if a number, unit, sample size, p-value, CI, or subgroup label is not visible, mark `[待核实]` instead of guessing

### Recommended result sentence pattern
- orienting sentence: what was compared or tested
- primary finding sentence: the main direction / contrast / estimate
- secondary detail sentence: supporting statistics or subgroup details if visible
- figure/table anchor sentence: `As shown in Figure X` / `Table X summarizes ...` when appropriate

### Do / do not for result prose from artifacts
Do:
- follow figure/table order when that is the clearest narrative order
- convert legend language into readable prose while preserving meaning
- state contrasts explicitly (`higher than`, `lower than`, `no clear difference`, `mixed pattern`)
- distinguish descriptive results from inferential statistics

Do not:
- infer significance from a visual trend alone if the statistical test is not shown
- explain mechanisms here; move that to Discussion
- hide uncertainty, missing labels, or invisible denominators
- repeat every number in the table when the pattern can be summarized faithfully

## 4. Discussion Workflow

### Use when
- the results are already reasonably stable
- the user needs interpretation, literature comparison, limitations, and implications

### Canonical structure
1. restate study aim and core findings
2. interpret the main findings
3. compare with prior literature
4. explain consistencies or discrepancies
5. limitations and their consequences
6. implications and future work

### Common high-quality pattern
- finding -> interpretation -> literature anchor -> implication -> caution

### Hard rules
- discussion is not a second results section
- do not merely repeat figure-level descriptions
- do not overclaim causality if design is observational
- limitations should be honest but proportionate
- future work should be specific, not ceremonial

## 4B. Conclusion / Future Work Workflow

### Use when
- the body results and discussion are already stable enough to summarize
- the user needs a final conclusion section, a final outlook section, or both

### Canonical structure
1. restate the thesis question or objective briefly
2. summarize the most defensible findings or contributions
3. clarify what those findings mean within the thesis scope
4. separate future work from already established conclusions

### Hard rules
- do not introduce any new result, citation, or factual claim in the conclusion
- do not merge conclusion and future work into one vague closing paragraph unless the venue explicitly expects that style
- derive future work from visible limitations, unresolved mechanisms, missing data, or scope boundaries
- avoid ceremonial phrases such as `future research is needed` without concrete direction

### Bridge from Results to Discussion
If Results were drafted from figures/tables, Discussion should:
- start from the already established result blocks rather than redescribing every panel
- explain meaning, comparison with literature, and implications
- explicitly distinguish visual pattern from supported inference

## 5. Abstract Workflow

### Use when
- the manuscript body or at least the core result logic is already known

### Canonical structure
1. problem / background
2. objective
3. methods
4. key findings
5. conclusion / significance

### Hard rules
- no new claims absent from the manuscript
- no fake citations in abstract
- if target journal has structured abstract rules, follow them
- keep results numerically anchored when appropriate

### Paper-production variants
Choose the narrowest useful abstract task:
- `abstract-first draft` — when the body logic is already stable enough to summarize
- `abstract rewrite` — when the manuscript exists but the abstract is weak, generic, or misaligned
- `bilingual abstract pair` — when Chinese + English abstracts must align conceptually without becoming mechanical translation

### Bilingual abstract rule
If the workflow is bilingual, preserve alignment of problem, objective, methods, findings, and conclusion across both language versions, but allow natural wording differences. Do not force literal sentence-by-sentence translation.

### Thesis abstract note
For a master's thesis or dissertation abstract, preserve the same logic but allow slightly more context-setting than in a journal abstract when institutional rules require it.

### Chinese -> English abstract rule
When both Chinese and English abstracts are requested:
- finalize the Chinese abstract structure first
- generate the English abstract from the finalized Chinese abstract plus thesis terminology
- do not let the English version introduce claims, methods, or conclusions absent from the Chinese abstract
- check title / keywords / abstract alignment across both languages before returning

## 6. Thesis / Dissertation Chapter Workflow

### Use when
- the user is writing a master's thesis, dissertation, or chapter-based graduate manuscript
- the output needs chapter boundaries, wrapper text, or thesis-level transitions
- the user is converting papers, figures, or analysis outputs into a thesis chapter

### Typical chapter families
1. thesis introduction / background chapter
2. literature review chapter
3. methods chapter
4. findings / results chapter
5. general discussion chapter
6. conclusion / implications / future work chapter

### Core rules
- a thesis chapter must have a clear chapter job, not just copied paper prose
- explain cross-chapter transitions explicitly
- allow broader context in introduction and discussion chapters than most journals would
- keep findings/results chapters evidence-led and non-interpretive where required by the discipline
- if the thesis is article-based, add wrapper text that explains what each paper/chapter contributes to the whole thesis argument
- if the user is still choosing among multiple topic directions, narrow by feasibility before polishing titles or drafting sections
- prefer small-scope executable topics over impressive but weakly supported topics

### Common thesis mistake patterns
- repeating the same background in every chapter
- copying a journal article into a thesis without wrapper transitions
- merging findings and discussion unintentionally because the thesis chapter feels long
- forgetting thesis-specific front matter, summary, or general conclusion requirements

### Thesis-level general discussion / conclusion synthesis
Use when the thesis has multiple result chapters, multiple studies, or article-based components that must be synthesized at the thesis level.

#### Core job
- do not merely concatenate per-chapter discussions
- synthesize what the whole thesis now shows that no single chapter shows alone
- restate the overarching research problem and answer it at thesis scale
- explain how chapters/studies connect, reinforce, qualify, or contradict one another

#### Recommended order
1. restate the overall thesis question / objective
2. synthesize the cross-chapter findings in 3-6 thesis-level claims
3. show how each claim is supported by one or more chapters / studies / figures / tables
4. explain theoretical, methodological, or practical implications at thesis scale
5. discuss thesis-level limitations, including boundaries shared across chapters
6. end with future work or application directions grounded in the synthesized evidence

#### Hard rules
- avoid chapter-by-chapter summary fatigue
- do not introduce new evidence absent from earlier chapters
- distinguish thesis-level synthesis from per-study interpretation
- acknowledge contradictions across chapters instead of smoothing them over
- keep implications proportional to the total evidence base, not the strongest single chapter

#### Useful output artifact
Before drafting, it is often useful to create a `chapter-to-thesis synthesis table` with:
- chapter / study
- its main finding
- what larger thesis claim it supports
- any limitation or contradiction it introduces
- where it should appear in the general discussion or conclusion

## 6. Title / Keywords / Highlights Workflow

### Title rules
- specific and searchable
- reflect topic and contribution
- avoid hype words unless standard in the field
- avoid claiming more than the study shows
- for thesis topic selection, prefer object + issue + angle/method + context over decorative wording
- when multiple titles are possible, compare them by feasibility, scope control, and alignment with actual data/materials

### Keyword rules
- balance precision and discoverability
- prefer field-standard terms
- include method/population/context when they materially define the paper

### Highlights rules
- each highlight should capture one contribution or finding
- avoid full-sentence fluff
- maintain factual traceability to the manuscript body

## 6B. Acknowledgments Workflow

### Use when
- the user needs a thesis acknowledgments section or a formal thank-you note inside an academic document

### Hard rules
- acknowledgments must be based on real contributors and real support
- keep the tone sincere, restrained, and non-theatrical
- avoid canned emotional language or generic gratitude blocks that could fit any thesis
- preserve institutional naming, supervisor titles, and contributor roles accurately

## 6C. Defense PPT Storyline Workflow

### Use when
- the user needs a thesis defense slide outline, speaking outline, or slide-by-slide talking structure

### Canonical structure
1. background / problem
2. research objective
3. method / data
4. core findings
5. innovation or value
6. limitations / future work
7. thanks / Q&A

### Hard rules
- one slide should carry one main message
- slides should compress the thesis narrative, not copy full thesis paragraphs
- prefer figures, tables, and findings already present in the thesis
- keep the output at storyline / speaker-outline level unless the user explicitly asks for visual deck production

## 7. Review-Article Workflow

### Use when
- the user is writing a narrative review, scoping review, evidence map, umbrella review, or theory review

### Key decision points
- what review type is this?
- is the output evidence-mapping or strong-claim synthesis?
- how reproducible must the search and screening process be?
- what framework best organizes the body: time, topic, method, application, dispute, mechanism?

### Strong recommendation
For review writing, do not start from prose. Start from:
1. type of review
2. search and inclusion logic
3. framework selection
4. evidence grouping
5. claim-to-evidence map
