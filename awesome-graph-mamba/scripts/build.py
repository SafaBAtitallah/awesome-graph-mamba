#!/usr/bin/env python3
"""Rebuild every generated artefact of the repository.

Pipeline
  1. parse source/main.tex and source/references.bib  (extract_papers)
  2. resolve data/papers.yaml against the bibliography (database)
  3. run consistency checks                              (quality)
  4. generate comparison tables (Markdown, LaTeX, CSV)  (generate_tables)
  5. generate catalogue pages, docs/FLAGS.md, README     (generate_catalogue)
  6. generate the GitHub Pages explorer docs/index.html  (generate_site)

Usage
  python scripts/build.py            # rebuild everything
  python scripts/build.py --merge    # also append stubs for newly classified works
  python scripts/build.py --check    # do not write; exit 1 if outputs are stale
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import GENERATED, ROOT, SOURCE_BIB, bib_duplicate_ids, dump_json, load_bib, load_data, write_outputs  # noqa: E402
import extract_papers  # noqa: E402
from database import database_outputs, resolve  # noqa: E402
from generate_catalogue import catalogue_outputs  # noqa: E402
from generate_tables import table_outputs  # noqa: E402
from generate_site import site_outputs  # noqa: E402
from quality import all_findings  # noqa: E402


def collect_outputs(merge: bool = False):
    """Return (outputs, context) without writing anything except merges."""
    extraction = extract_papers.run(merge=merge, write=False)
    extraction.pop("merged_stubs", None)
    data = load_data()
    bib = load_bib()
    resolved = resolve(data, bib, extraction)
    findings = all_findings(data, bib, extraction, resolved, bib_duplicate_ids(SOURCE_BIB))
    outputs = {GENERATED / "tex_extraction.json": dump_json(extraction)}
    outputs.update(database_outputs(resolved))
    tab_out, tables = table_outputs(data, resolved)
    outputs.update(tab_out)
    outputs.update(catalogue_outputs(data, resolved, extraction, tables, findings))
    outputs.update(site_outputs(data, resolved))
    ctx = {"data": data, "bib": bib, "extraction": extraction, "resolved": resolved, "findings": findings, "tables": tables}
    return outputs, ctx


def stale_outputs(outputs) -> list[Path]:
    return [p for p, c in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != c]


def build(merge: bool = False, check: bool = False, only: list[str] | None = None, quiet: bool = False) -> int:
    outputs, ctx = collect_outputs(merge=merge)
    if only:
        keep = {"tables": "tables", "catalogue": ("papers", "docs/FLAGS.md", "README.md"), "site": "docs/index.html"}
        prefixes = []
        for o in only:
            v = keep[o]
            prefixes += [v] if isinstance(v, str) else list(v)
        outputs = {p: c for p, c in outputs.items() if str(p.relative_to(ROOT)).startswith(tuple(prefixes))}
    if check:
        stale = stale_outputs(outputs)
        for p in stale:
            print(f"STALE: {p.relative_to(ROOT)}")
        print("outputs up to date" if not stale else f"{len(stale)} stale output(s); run python scripts/build.py")
        return 1 if stale else 0
    written = write_outputs(outputs)
    if not quiet:
        sev = {s: sum(f.severity == s for f in ctx["findings"]) for s in ("error", "warning", "info")}
        print(f"papers: {len(ctx['resolved'])} | tables: {len(ctx['tables'])} | files generated: {len(outputs)} "
              f"| files changed: {len(written)}")
        print(f"findings: {sev['error']} errors, {sev['warning']} warnings, {sev['info']} info (see docs/FLAGS.md)")
    return 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--merge", action="store_true", help="append stubs for works classified in the manuscript but missing from papers.yaml")
    ap.add_argument("--check", action="store_true", help="exit 1 if generated outputs are not up to date")
    a = ap.parse_args()
    sys.exit(build(merge=a.merge, check=a.check))


if __name__ == "__main__":
    main()
