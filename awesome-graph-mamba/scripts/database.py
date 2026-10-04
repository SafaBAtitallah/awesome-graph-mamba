"""Resolve the curated database against the bibliography and manuscript.

The result (``data/generated/papers.json`` / ``papers.csv``) is the
machine-readable, fully denormalised view of every reviewed work. It is
*generated*; edit ``data/papers.yaml`` or ``source/references.bib``
instead.
"""
from __future__ import annotations

import csv
import io
import re
from pathlib import Path

from common import (
    GENERATED, NR, bib_links, bib_venue, dump_json, format_authors, latex_to_text, scholar_search,
)

# Display order of categories
SETTING_ORDER = ["static_general", "dynamic_spatiotemporal", "heterogeneous_higher_order"]
ROLE_ORDER = ["taxonomy", "application", "discussed"]


def lookup(taxonomy: dict) -> dict:
    """Convenient id -> label lookups built from taxonomy.yaml."""
    lk = {
        "setting": {s["id"]: s["label"] for s in taxonomy["graph_settings"]},
        "pattern": {p["id"]: p["label"] for p in taxonomy["design_patterns"]},
        "domain": {d["id"]: d["label"] for d in taxonomy["application_domains"]},
        "subdomain": {},
        "subdomain_parent": {},
        "level": {},
        "type": {},
        "role": {r["id"]: r["label"] for r in taxonomy["roles"]},
    }
    for d in taxonomy["application_domains"]:
        for s in d["subdomains"]:
            lk["subdomain"][s["id"]] = s["label"]
            lk["subdomain_parent"][s["id"]] = d["id"]
    for dim in taxonomy["dimensions"]:
        for lv in dim.get("levels", []):
            lk["level"][lv["id"]] = lv["label"]
        for ty in dim.get("types", []):
            lk["type"][ty["id"]] = ty["label"]
    return lk


def paper_benchmarks(key: str, benchmarks: dict) -> list[dict]:
    return [b for b in benchmarks["benchmarks"] if key in b["models"]]


def paper_results(key: str, results: list[dict]) -> list[str]:
    """IDs of result tables in which the paper appears as a row."""
    out = []
    for t in results:
        if any(key in str(r.get("key", "")).split(",") for r in t["rows"]):
            out.append(t["id"])
    return out


def paper_challenges(key: str, challenges: list[dict]) -> list[str]:
    return [c["id"] for c in challenges if any(e["key"] == key for e in c["early_work"])]


def resolve(data: dict, bib: dict, extraction: dict) -> list[dict]:
    taxonomy = data["taxonomy"]
    labels = extraction.get("section_labels", {})
    cite_secs = extraction.get("cited_keys", {})
    resolved = []
    for p in data["papers"]:
        e = bib.get(p["key"], {})
        title = latex_to_text(e.get("title")) or NR
        links = bib_links(e) if e else {}
        primary = links.get("doi") or links.get("arxiv") or links.get("url")
        rec = {
            "key": p["key"],
            "model": p["model"],
            "aliases": p.get("aliases", []),
            "title": title,
            "authors": format_authors(e.get("author")),
            "year": e.get("year", NR),
            "venue": bib_venue(e) if e else NR,
            "entry_type": e.get("ENTRYTYPE", NR),
            "doi": links.get("doi", NR),
            "arxiv": links.get("arxiv", NR),
            "url": links.get("url", NR),
            "primary_link": primary or NR,
            "search_link": scholar_search(title) if title != NR else NR,
            "code": p.get("code", NR),
            "roles": p["roles"],
            "precursor": bool(p.get("precursor", False)),
            "multimodal": bool(p.get("multimodal", False)),
            "taxonomy": p.get("taxonomy"),
            "application": p.get("application"),
            "methodology": p.get("methodology", NR),
            "contributions": p.get("contributions", []),
            "complexity": p.get("complexity", NR),
            "efficiency": p.get("efficiency"),
            "expressivity": p.get("expressivity"),
            "benchmarks": [b["id"] for b in paper_benchmarks(p["key"], data["benchmarks"])],
            "datasets": [d for b in paper_benchmarks(p["key"], data["benchmarks"]) for d in b["datasets"]],
            "metrics": sorted({m for b in paper_benchmarks(p["key"], data["benchmarks"]) for m in b["metrics"]}),
            "result_tables": paper_results(p["key"], data["results"]),
            "challenges": paper_challenges(p["key"], data["challenges"]),
            "advantages": p.get("advantages", []),
            "limitations": p.get("limitations", []),
            "notes": p.get("notes", []),
            "manuscript_labels": p["sections"],
            "manuscript_sections": [
                f"{labels[l]['number']} {labels[l]['title']}" for l in p["sections"] if l in labels
            ],
            "cited_in_sections": cite_secs.get(p["key"], []),
            "verification": p["verification"],
            "in_bib": bool(e),
        }
        resolved.append(rec)
    return resolved


def category_of(rec: dict) -> str:
    """File-level category used for the per-category catalogue pages."""
    if rec["taxonomy"]:
        return rec["taxonomy"]["setting"]
    if rec["application"]:
        return rec["application"]["domain"]
    return "discussed"


CSV_FIELDS = [
    "key", "model", "title", "authors", "year", "venue", "doi", "arxiv", "url", "code", "roles",
    "setting", "d1_tokenization", "d2_ordering", "d3_coupling", "d4_integration",
    "domain", "subdomain", "task", "graph_construction", "dominant_pattern", "secondary_pattern", "patterns",
    "precursor", "multimodal", "datasets", "metrics", "complexity", "result_tables", "challenges",
    "manuscript_sections", "verification_status",
]


def to_csv_rows(resolved: list[dict]) -> list[dict]:
    rows = []
    for r in resolved:
        t = r["taxonomy"] or {}
        a = r["application"] or {}
        rows.append({
            "key": r["key"], "model": r["model"], "title": r["title"], "authors": r["authors"],
            "year": r["year"], "venue": r["venue"], "doi": r["doi"], "arxiv": r["arxiv"], "url": r["url"],
            "code": r["code"], "roles": ";".join(r["roles"]),
            "setting": t.get("setting", NR), "d1_tokenization": t.get("d1", NR), "d2_ordering": t.get("d2", NR),
            "d3_coupling": ";".join(t.get("d3", [])) or NR, "d4_integration": ";".join(t.get("d4", [])) or NR,
            "domain": a.get("domain", NR), "subdomain": a.get("subdomain", NR), "task": a.get("task", NR),
            "graph_construction": a.get("graph_construction", NR),
            "dominant_pattern": a.get("dominant_pattern", NR), "secondary_pattern": a.get("secondary_pattern", NR),
            "patterns": ";".join(a.get("patterns", [])) or NR,
            "precursor": r["precursor"], "multimodal": r["multimodal"],
            "datasets": ";".join(r["datasets"]) or NR, "metrics": ";".join(r["metrics"]) or NR,
            "complexity": re.sub(r"\\l?r?vert", "|", r["complexity"]).replace("$", ""),
            "result_tables": ";".join(r["result_tables"]) or NR, "challenges": ";".join(r["challenges"]) or NR,
            "manuscript_sections": ";".join(s.split(" ")[0] for s in r["manuscript_sections"]),
            "verification_status": r["verification"]["status"],
        })
    return rows


def csv_string(rows: list[dict], fields: list[str]) -> str:
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    for row in rows:
        w.writerow({k: row.get(k, NR) for k in fields})
    return buf.getvalue()


def database_outputs(resolved: list[dict]) -> dict[Path, str]:
    return {
        GENERATED / "papers.json": dump_json({"n_papers": len(resolved), "papers": resolved}),
        GENERATED / "papers.csv": csv_string(to_csv_rows(resolved), CSV_FIELDS),
    }
