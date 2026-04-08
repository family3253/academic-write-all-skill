from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_DIR.parent


def run(module_script: str, *args: str) -> int:
    cmd = [sys.executable, str(SCRIPT_DIR / module_script), *args]
    return subprocess.call(cmd)


def cmd_bootstrap(_args: argparse.Namespace) -> int:
    bootstrap = SKILL_ROOT / "bootstrap_cycwrite_runtime.bat"
    return subprocess.call(["cmd", "/c", str(bootstrap)])


def cmd_ipubmed(args: argparse.Namespace) -> int:
    extra: list[str] = ["--output", args.output, "--query", args.query]
    if args.download_dir:
        extra.extend(["--download-dir", args.download_dir])
    if args.validate_only:
        extra.append("--validate-only")
    return run("ipubmed_browser_adapter.py", *extra)


def cmd_cnki(args: argparse.Namespace) -> int:
    extra: list[str] = ["--output", args.output, "--query", args.query]
    if args.institution_filter:
        extra.extend(["--institution-filter", args.institution_filter])
    if args.download_dir:
        extra.extend(["--download-dir", args.download_dir])
    if args.validate_only:
        extra.append("--validate-only")
    return run("cnki_browser_adapter.py", *extra)


def cmd_doi_flow(args: argparse.Namespace) -> int:
    candidate = args.candidate_output
    acquisition = args.acquisition_output
    text = args.text_output
    exit_code = run(
        "doi_acquisition_adapter.py",
        args.doi,
        "--candidate-output",
        candidate,
        "--acquisition-output",
        acquisition,
        "--text-output",
        text,
    )
    if exit_code != 0:
        return exit_code
    return run(
        "classify_acquisition_artifact.py",
        "--acquisition-csv",
        acquisition,
        "--text-file",
        text,
    )


def cmd_handoff(args: argparse.Namespace) -> int:
    return run(
        "handoff_acquisition_to_project.py",
        "--project-dir",
        args.project_dir,
        "--candidate-csv",
        args.candidate_csv,
        "--acquisition-csv",
        args.acquisition_csv,
        "--text-file",
        args.text_file,
    )


def cmd_project_init(args: argparse.Namespace) -> int:
    extra: list[str] = [args.project_dir]
    if args.force:
        extra.append("--force")
    return run("init_review_project.py", *extra)


def cmd_project_status(args: argparse.Namespace) -> int:
    return run("session_state_driver.py", args.project_dir)


def cmd_project_gate(args: argparse.Namespace) -> int:
    return run("generate_gate_report.py", args.project_dir)


def cmd_awas_export_zotero_metadata(args: argparse.Namespace) -> int:
    extra: list[str] = ["--config", args.config, "--output-dir", args.output_dir]
    for item in args.item:
        extra.extend(["--item", item])
    for output_format in args.format or []:
        extra.extend(["--format", output_format])
    return run("awas_export_zotero_metadata.py", *extra)


def cmd_awas_fetch_zotero_items(args: argparse.Namespace) -> int:
    extra: list[str] = ["--output", args.output]
    for item in args.item:
        extra.extend(["--item", item])
    if args.api_key:
        extra.extend(["--api-key", args.api_key])
    if args.user_id:
        extra.extend(["--user-id", args.user_id])
    if args.library_type:
        extra.extend(["--library-type", args.library_type])
    return run("awas_fetch_zotero_items.py", *extra)


def cmd_awas_write_zotero_items(args: argparse.Namespace) -> int:
    extra: list[str] = ["--input", args.input]
    if args.api_key:
        extra.extend(["--api-key", args.api_key])
    if args.user_id:
        extra.extend(["--user-id", args.user_id])
    if args.library_type:
        extra.extend(["--library-type", args.library_type])
    return run("awas_write_zotero_items.py", *extra)


def cmd_awas_analyze_markdown_refs(args: argparse.Namespace) -> int:
    extra: list[str] = [args.markdown_path, "--section-marker", args.section_marker]
    extra.extend(["--preview-count", str(args.preview_count)])
    return run("awas_analyze_markdown_refs.py", *extra)


def cmd_awas_word_probe(args: argparse.Namespace) -> int:
    extra: list[str] = [args.probe_command]
    if args.limit is not None:
        extra.extend(["--limit", str(args.limit)])
    if args.preview_chars is not None:
        extra.extend(["--preview-chars", str(args.preview_chars)])
    return run("awas_word_probe.py", *extra)


def cmd_awas_word_run_zotero_citation(args: argparse.Namespace) -> int:
    extra: list[str] = []
    if args.anchor_text is not None:
        extra.extend(["--anchor-text", args.anchor_text])
    return run("awas_word_run_zotero_citation.py", *extra)


def cmd_awas_extract_markdown_ref_candidates(args: argparse.Namespace) -> int:
    extra: list[str] = [args.markdown_path, "--section-marker", args.section_marker]
    for ref_id in args.ref_id:
        extra.extend(["--ref-id", ref_id])
    return run("awas_extract_markdown_ref_candidates.py", *extra)


def cmd_awas_ensure_zotero_collection(args: argparse.Namespace) -> int:
    extra: list[str] = ["--name", args.name]
    if args.api_key:
        extra.extend(["--api-key", args.api_key])
    if args.user_id:
        extra.extend(["--user-id", args.user_id])
    if args.library_type:
        extra.extend(["--library-type", args.library_type])
    return run("awas_ensure_zotero_collection.py", *extra)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Unified CLI for cycwrite runtime workflows."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    bootstrap = subparsers.add_parser(
        "bootstrap", help="Create/update the isolated cycwrite runtime."
    )
    bootstrap.set_defaults(func=cmd_bootstrap)

    ipubmed = subparsers.add_parser("ipubmed", help="Run the IPubMed browser workflow.")
    ipubmed.add_argument("--output", required=True)
    ipubmed.add_argument("--query", required=True)
    ipubmed.add_argument("--download-dir", default="")
    ipubmed.add_argument("--validate-only", action="store_true")
    ipubmed.set_defaults(func=cmd_ipubmed)

    cnki = subparsers.add_parser("cnki", help="Run the CNKI browser workflow.")
    cnki.add_argument("--output", required=True)
    cnki.add_argument("--query", required=True)
    cnki.add_argument("--institution-filter", default="")
    cnki.add_argument("--download-dir", default="")
    cnki.add_argument("--validate-only", action="store_true")
    cnki.set_defaults(func=cmd_cnki)

    doi_flow = subparsers.add_parser(
        "doi-flow", help="Run DOI acquisition + classification."
    )
    doi_flow.add_argument("doi")
    doi_flow.add_argument("--candidate-output", required=True)
    doi_flow.add_argument("--acquisition-output", required=True)
    doi_flow.add_argument("--text-output", required=True)
    doi_flow.set_defaults(func=cmd_doi_flow)

    handoff = subparsers.add_parser(
        "handoff", help="Attach acquisition artifacts into a cycwrite project."
    )
    handoff.add_argument("--project-dir", required=True)
    handoff.add_argument("--candidate-csv", required=True)
    handoff.add_argument("--acquisition-csv", required=True)
    handoff.add_argument("--text-file", required=True)
    handoff.set_defaults(func=cmd_handoff)

    project_init = subparsers.add_parser(
        "project-init", help="Initialize a cycwrite review/thesis project scaffold."
    )
    project_init.add_argument("project_dir")
    project_init.add_argument("--force", action="store_true")
    project_init.set_defaults(func=cmd_project_init)

    project_status = subparsers.add_parser(
        "project-status", help="Show current session state for a cycwrite project."
    )
    project_status.add_argument("project_dir")
    project_status.set_defaults(func=cmd_project_status)

    project_gate = subparsers.add_parser(
        "project-gate", help="Generate gate report for a cycwrite project."
    )
    project_gate.add_argument("project_dir")
    project_gate.set_defaults(func=cmd_project_gate)

    awas_export = subparsers.add_parser(
        "awas-export-zotero-metadata",
        help="Export Zotero item metadata through fastmcp into Markdown/BibTeX artifacts.",
    )
    awas_export.add_argument("--config", required=True)
    awas_export.add_argument("--item", action="append", required=True)
    awas_export.add_argument(
        "--format", action="append", choices=["markdown", "bibtex"]
    )
    awas_export.add_argument("--output-dir", default="outputs/awas-mcp-exports")
    awas_export.set_defaults(func=cmd_awas_export_zotero_metadata)

    awas_fetch = subparsers.add_parser(
        "awas-fetch-zotero-items",
        help="Fetch Zotero items by key through the Web API and save them as JSON.",
    )
    awas_fetch.add_argument("--item", action="append", required=True)
    awas_fetch.add_argument("--output", required=True)
    awas_fetch.add_argument("--api-key", default="")
    awas_fetch.add_argument("--user-id", default="")
    awas_fetch.add_argument("--library-type", default="")
    awas_fetch.set_defaults(func=cmd_awas_fetch_zotero_items)

    awas_write = subparsers.add_parser(
        "awas-write-zotero-items",
        help="Create Zotero items from a JSON payload through the Web API.",
    )
    awas_write.add_argument("--input", required=True)
    awas_write.add_argument("--api-key", default="")
    awas_write.add_argument("--user-id", default="")
    awas_write.add_argument("--library-type", default="")
    awas_write.set_defaults(func=cmd_awas_write_zotero_items)

    awas_refs = subparsers.add_parser(
        "awas-analyze-markdown-refs",
        help="Analyze citation coverage against a numbered markdown reference list.",
    )
    awas_refs.add_argument("markdown_path")
    awas_refs.add_argument("--section-marker", default="参考文献（前言部分）")
    awas_refs.add_argument("--preview-count", type=int, default=8)
    awas_refs.set_defaults(func=cmd_awas_analyze_markdown_refs)

    awas_extract_refs = subparsers.add_parser(
        "awas-extract-markdown-ref-candidates",
        help="Extract selected numbered reference entries from a markdown references section.",
    )
    awas_extract_refs.add_argument("markdown_path")
    awas_extract_refs.add_argument("--section-marker", default="参考文献（前言部分）")
    awas_extract_refs.add_argument("--ref-id", action="append", required=True)
    awas_extract_refs.set_defaults(func=cmd_awas_extract_markdown_ref_candidates)

    awas_collection = subparsers.add_parser(
        "awas-ensure-zotero-collection",
        help="Ensure a top-level Zotero collection exists and return its key.",
    )
    awas_collection.add_argument("--name", required=True)
    awas_collection.add_argument("--api-key", default="")
    awas_collection.add_argument("--user-id", default="")
    awas_collection.add_argument("--library-type", default="")
    awas_collection.set_defaults(func=cmd_awas_ensure_zotero_collection)

    awas_word_probe = subparsers.add_parser(
        "awas-word-probe",
        help="Inspect the current Word automation state used by AWAS Word/Zotero workflows.",
    )
    awas_word_probe.add_argument(
        "probe_command",
        choices=[
            "docmeta",
            "addins",
            "commandbars",
            "macros",
            "zotero-state",
            "dump-fields",
            "processes",
        ],
    )
    awas_word_probe.add_argument("--limit", type=int)
    awas_word_probe.add_argument("--preview-chars", type=int)
    awas_word_probe.set_defaults(func=cmd_awas_word_probe)

    awas_word_run = subparsers.add_parser(
        "awas-word-run-zotero-citation",
        help="Insert an optional anchor and invoke ZoteroAddEditCitation in Word.",
    )
    awas_word_run.add_argument(
        "--anchor-text", default="[AWAS-Zotero-citation-test-anchor]"
    )
    awas_word_run.set_defaults(func=cmd_awas_word_run_zotero_citation)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    raise SystemExit(args.func(args))


if __name__ == "__main__":
    main()
