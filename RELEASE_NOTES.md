# academic-write-all-skill Release Notes

## Release Title

`academic-write-all-skill` - unified academic writing, review, and research-lifecycle skill

## Summary

This release consolidates the former `cycwrite` skill into the new `academic-write-all-skill` identity and expands it into a broader academic workflow package.

It now combines:
- paper-production routing
- review-project gating
- revision-coach behavior
- research-lifecycle routing from idea discovery to paper planning
- reusable live-routing eval prompts
- repository-level smoke testing
- one-command install guidance for OpenCode and OpenClaw

## Highlights

### New public identity
- renamed the published skill to `academic-write-all-skill`
- published at: `https://github.com/family3253/academic-write-all-skill`
- added migration notice in the old `cycwrite-skill` repo

### Expanded academic workflow coverage
- added research-lifecycle mode for:
  - idea discovery
  - novelty-check framing
  - literature-to-gap narrowing
  - experiment/result packaging
  - paper-plan handoff
- preserved paper-production and review-project routing from earlier absorbed skills

### Better installability
- OpenCode one-command install:
  - `npx skills add family3253/academic-write-all-skill -a opencode`
- OpenClaw one-command install:
  - `npx skills add family3253/academic-write-all-skill -a openclaw`
- renamed Windows runtime launchers to:
  - `bootstrap_academic_write_all_skill_runtime.bat`
  - `academic-write-all-skill.bat`

### Testing improvements
- added `evals/evals.json` with three live-routing regression prompts
- added `scripts/smoke_test.py` for repeatable repository smoke tests
- verified live harness routing for:
  - outline-only behavior
  - revision-coach behavior
  - review-output downgrade behavior

## Verification Performed

### Harness-level behavior checks
Confirmed correct routing on these prompts:
- outline-only prompt
- revision-coach prompt
- weak-corpus review downgrade prompt

### Repository/runtime checks
Confirmed passing:
- `python -m compileall scripts`
- `python scripts/cycwrite_cli.py --help`
- `python scripts/smoke_test.py`
- project scaffold initialization
- project status inspection
- gate report generation

## Migration Notes

If you previously used the old `cycwrite` repository or OpenCode install directory:
- switch to `academic-write-all-skill`
- reinstall using the new repo name
- use the new runtime launcher names in local Windows workflows

## Suggested GitHub Release Body

`academic-write-all-skill` is the new published home for the former `cycwrite` workflow skill.

This release upgrades the project from a writing router into a broader academic workflow router that can handle:
- idea and novelty stages
- literature and review-project stages
- paper drafting and revision stages
- evidence-sensitive downgrade behavior when source support is weak

It also adds reusable eval prompts, a smoke-test script, OpenCode/OpenClaw install guidance, and renamed Windows launchers for cleaner public distribution.
