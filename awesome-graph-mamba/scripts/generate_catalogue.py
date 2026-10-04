#!/usr/bin/env python3
"""Generate the Markdown paper catalogue.

* ``papers/<category>.md``  – one card per paper, grouped by the survey
  classification (graph setting for architectures, application domain
  for applications, plus models discussed only in Sec. 7)
* ``papers/README.md``      – catalogue index
* ``docs/FLAGS.md``         – open verification flags and data-quality findings
* ``README.md``             – the blocks between ``<!-- BEGIN:X -->`` and
  ``<!-- END:X -->`` markers are regenerated; everything else is kept.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DOCS, NR, PAPERS_DIR, README, md_text  # noqa: E402
from database import SETTING_ORDER, lookup  # noqa: E402

PAGES = {
    "static_general": ("static-general.md", "Static and General-Purpose Graph Models", "Sec. 3.2"),
    "dynamic_spatiotemporal": ("dynamic-spatiotemporal.md", "Dynamic and Spatio-Temporal Graph Models", "Sec. 3.3"),
    "heterogeneous_higher_order": ("heterogeneous-higher-order.md", "Heterogeneous and Higher-Order Graph Models", "Sec. 3.4"),
    "healthcare": ("healthcare.md", "Healthcare and Biomedical Applications", "Sec. 5.1"),
    "remote_visual": ("remote-sensing-visual.md", "Remote Sensing and Structured Visual Applications", "Sec. 5.2"),
    "other": ("other-applications.md", "Other Application Areas", "Sec. 5.3"),
    "discussed": ("discussed-models.md", "Graph Mamba Models Discussed in the Research Agenda", "Sec. 7"),
}
PAGE_ORDER = list(PAGES)


def category_of(rec: dict) -> str:
    if rec["taxonomy"]:
        return rec["taxonomy"]["setting"]
    if rec["application"]:
        return rec["application"]["domain"]
    return "discussed"


def page_for(rec: dict) -> str:
    return PAGES[category_of(rec)][0]


def anchor(rec: dict) -> str:
    return rec["key"].lower().replace("+", "").replace(".", "")


def badges(rec: dict) -> str:
    b = []
    if rec["precursor"]:
        b.append("`† precursor`")
    if rec["multimodal"]:
        b.append("`◆ multimodal`")
    if rec["verification"]["status"] == "needs_verification":
        b.append("`⚠ needs verification`")
    elif rec["verification"]["status"] == "verified":
        b.append("`✔ verified`")
    return " ".join(b)


def links_line(rec: dict) -> str:
    parts = []
    if rec["doi"] != NR:
        parts.append(f"[DOI]({rec['doi']})")
    if rec["arxiv"] != NR:
        parts.append(f"[arXiv]({rec['arxiv']})")
    if rec["url"] != NR:
        parts.append(f"[Publisher]({rec['url']})")
    if not parts:
        parts.append(f"Link: NR ([Scholar search]({rec['search_link']}))")
    parts.append(f"[Code]({rec['code']})" if rec["code"] != NR else "Code: NR")
    return " · ".join(parts)


def bullet_list(items: list[str]) -> list[str]:
    return [f"- {md_text(i)}" for i in items] if items else ["- NR"]


def card(rec: dict, lk: dict, benchmarks_by_id: dict) -> str:
    out = [f'<a id="{anchor(rec)}"></a>', f"### {md_text(rec['model'])}"]
    if rec["aliases"]:
        out.append(f"*Also referred to as: {', '.join(md_text(a) for a in rec['aliases'])}*  ")
    out.append(f"**{md_text(rec['title'])}**  ")
    out.append(f"{md_text(rec['authors'])} — *{md_text(rec['venue'])}*, {rec['year']}  ")
    out.append(f"{links_line(rec)} · BibTeX: `{rec['key']}` {badges(rec)}")
    out.append("")
    t, a = rec["taxonomy"], rec["application"]
    if t:
        out += ["| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |",
                "| :--- | :--- | :--- | :--- | :--- |",
                f"| {md_text(lk['setting'][t['setting']])} | {md_text(t['d1'])} | {md_text(t['d2'])} | "
                f"{', '.join(lk['level'][x] for x in t['d3'])} | {', '.join(lk['type'][x] for x in t['d4'])} |", ""]
    if a:
        pat = lk["pattern"][a["dominant_pattern"]] + f" ({a['dominant_pattern']})"
        if a.get("secondary_pattern"):
            pat += f"; secondary: {lk['pattern'][a['secondary_pattern']]} ({a['secondary_pattern']})"
        out += ["| Data setting | Task | Graph construction | Design pattern |", "| :--- | :--- | :--- | :--- |",
                f"| {md_text(lk['subdomain'][a['subdomain']])} | {md_text(a['task'])} | {md_text(a['graph_construction'])} | {pat} |", "",
                f"**Graph–SSM division of labor.** {md_text(a['division_of_labor'])}", ""]
    out.append(f"**Methodology.** {md_text(rec['methodology'])}")
    out.append("")
    if rec["contributions"]:
        out += ["**Key contributions (as characterized in the survey)**"] + bullet_list(rec["contributions"]) + [""]
    details = []
    if rec["complexity"] != NR:
        details.append(f"- **Reported complexity:** {md_text(rec['complexity'])}")
    if rec["efficiency"]:
        e = rec["efficiency"]
        details.append(f"- **Efficiency:** {md_text(e['scaling'])}; extra costs: {md_text(e['additional_costs'])}; "
                       f"evidence: {md_text(e['evidence'])}")
    if rec["expressivity"]:
        x = rec["expressivity"]
        details.append(f"- **Expressive power:** {md_text(x['result'])} *(permutation: {md_text(x['permutation_property'])}; "
                       f"caveat: {md_text(x['caveat'])})*")
    if rec["benchmarks"]:
        ds = "; ".join(f"{', '.join(benchmarks_by_id[b]['datasets'])} ({', '.join(benchmarks_by_id[b]['metrics'])})" for b in rec["benchmarks"])
        details.append(f"- **Benchmarks in the survey:** {md_text(ds)}")
    else:
        details.append("- **Benchmarks in the survey:** NR")
    if rec["result_tables"]:
        details.append("- **Published results:** " + ", ".join(f"[{t}](../tables/markdown/{t}.md)" for t in rec["result_tables"]))
    if details:
        out += details + [""]
    out += ["<details><summary>Advantages, limitations, and notes</summary>", "", "**Advantages (stated in the survey)**"]
    out += bullet_list(rec["advantages"]) + ["", "**Limitations (stated in the survey)**"] + bullet_list(rec["limitations"])
    if rec["notes"]:
        out += ["", "**Notes**"] + bullet_list(rec["notes"])
    if rec["challenges"]:
        out += ["", "**Cited as early work for challenges:** " + ", ".join(f"`{c}`" for c in rec["challenges"])]
    out += ["", "**Discussed in:** " + ("; ".join(md_text(s) for s in rec["manuscript_sections"]) or NR), "", "</details>", ""]
    for fl in rec["verification"].get("flags", []):
        out += [f"> [!WARNING]", f"> {md_text(fl)}", ""]
    out.append("---")
    return "\n".join(out)


def category_pages(data: dict, resolved: list[dict]) -> dict[Path, str]:
    lk = lookup(data["taxonomy"])
    bmap = {b["id"]: b for b in data["benchmarks"]["benchmarks"]}
    out = {}
    for cat in PAGE_ORDER:
        fname, title, sec = PAGES[cat]
        recs = [r for r in resolved if category_of(r) == cat]
        lines = [f"# {title}", "", f"*Survey section: {sec}. {len(recs)} work(s).* "
                 "[← Catalogue index](README.md) · [← Repository home](../README.md)", ""]
        if cat in SETTING_ORDER:
            emph = next(s["emphasis"] for s in data["taxonomy"]["graph_settings"] if s["id"] == cat)
            lines += [f"> **Design emphasis in this setting:** {emph}", ""]
            groups = [("", recs)]
        elif cat == "discussed":
            lines += ["> These Graph Mamba models are cited in Section 7 (challenges and research agenda) but are **not** "
                      "classified in the survey taxonomy. No D1–D4 or design-pattern label is assigned.", ""]
            groups = [("", recs)]
        else:
            dom = next(d for d in data["taxonomy"]["application_domains"] if d["id"] == cat)
            groups = [(s["label"], [r for r in recs if r["application"]["subdomain"] == s["id"]]) for s in dom["subdomains"]]
        lines += ["**Contents**", ""]
        for g, rs in groups:
            if g and rs:
                lines.append(f"- *{g}*: " + ", ".join(f"[{md_text(r['model'])}](#{anchor(r)})" for r in rs))
            elif rs:
                lines += [f"- [{md_text(r['model'])}](#{anchor(r)}) ({r['year']})" for r in rs]
        lines.append("")
        for g, rs in groups:
            if not rs:
                continue
            if g:
                lines += [f"## {g}", ""]
            for r in rs:
                lines += [card(r, lk, bmap), ""]
        lines.append("<sub>Generated by `scripts/generate_catalogue.py` from `data/papers.yaml` and "
                     "`source/references.bib`. Do not edit by hand.</sub>")
        out[PAPERS_DIR / fname] = "\n".join(lines) + "\n"
    # index
    idx = ["# Paper catalogue", "", "[← Repository home](../README.md)", "",
           "| Category | Survey section | Works |", "| :--- | :--- | :---: |"]
    for cat in PAGE_ORDER:
        fname, title, sec = PAGES[cat]
        n = sum(category_of(r) == cat for r in resolved)
        idx.append(f"| [{title}]({fname}) | {sec} | {n} |")
    out[PAPERS_DIR / "README.md"] = "\n".join(idx) + "\n"
    return out


# ---------------------------------------------------------------------------
# README blocks
# ---------------------------------------------------------------------------
def _mm(s: str) -> str:
    return '"' + s.replace('"', "'").replace("--", "–") + '"'


def mermaid_taxonomy(data: dict, resolved: list[dict]) -> str:
    tx = data["taxonomy"]
    lines = ["```mermaid", "flowchart LR", f"  GM{_mm('Graph Mamba architectures')}"]
    for d in tx["dimensions"]:
        lines.append(f"  GM --> {d['id']}{_mm(d['id'] + ' · ' + d['name'] + '<br/><i>' + d['question'] + '</i>')}")
        for c in d.get("levels", []) + d.get("types", []):
            lines.append(f"  {d['id']} --> {d['id']}_{c['id']}{_mm(c['label'])}")
    lines += ["  classDef dim fill:#1f3b73,color:#fff,stroke:#1f3b73;", "  class D1,D2,D3,D4 dim;", "```"]
    return "\n".join(lines)


def mermaid_settings(data: dict, resolved: list[dict]) -> str:
    lk = lookup(data["taxonomy"])
    lines = ["```mermaid", "flowchart TB", f"  R{_mm('Reviewed Graph Mamba literature')}"]
    for i, s in enumerate(SETTING_ORDER):
        recs = [r for r in resolved if r["taxonomy"] and r["taxonomy"]["setting"] == s]
        lines.append(f"  R --> S{i}{_mm(lk['setting'][s] + ' (' + str(len(recs)) + ')')}")
        lines.append(f"  S{i} --- S{i}m{_mm(' · '.join(r['model'] for r in recs))}")
    for j, d in enumerate(data["taxonomy"]["application_domains"]):
        recs = [r for r in resolved if r["application"] and r["application"]["domain"] == d["id"]]
        lines.append(f"  R --> A{j}{_mm(d['label'] + ' (' + str(len(recs)) + ')')}")
        for k, sub in enumerate(d["subdomains"]):
            rs = [r for r in recs if r["application"]["subdomain"] == sub["id"]]
            if rs:
                lines.append(f"  A{j} --- A{j}s{k}{_mm(sub['label'] + ': ' + ', '.join(r['model'] for r in rs))}")
    lines += ["  classDef set fill:#e8eef9,stroke:#1f3b73;", "  classDef app fill:#fdf1e3,stroke:#b46b12;",
              "  class " + ",".join(f"S{i}" for i in range(len(SETTING_ORDER))) + " set;",
              "  class " + ",".join(f"A{j}" for j in range(len(data['taxonomy']['application_domains']))) + " app;", "```"]
    return "\n".join(lines)


def stats_block(data: dict, resolved: list[dict], extraction: dict, n_tables: int) -> str:
    tax = [r for r in resolved if r["taxonomy"]]
    app = [r for r in resolved if r["application"]]
    dis = [r for r in resolved if "discussed" in r["roles"]]
    years = Counter(str(r["year"]) for r in resolved)
    yrs = " · ".join(f"{y}: {n}" for y, n in sorted(years.items()))
    pending = sum(r["verification"]["status"] != "verified" for r in resolved)
    return "\n".join([
        "| Works in database | Architectures (D1–D4) | Applications | Discussed only (Sec. 7) | Cited references | Comparison tables |",
        "| :---: | :---: | :---: | :---: | :---: | :---: |",
        f"| **{len(resolved)}** | {len(tax)} | {len(app)} | {len(dis)} | {extraction['n_cited_keys']} | "
        f"{n_tables} |",
        "", f"**Publication years (BibTeX):** {yrs}  ",
        f"**Verification status:** {pending} of {len(resolved)} records await author verification "
        "([open flags](docs/FLAGS.md)).",
    ])


def catalogue_block(data: dict, resolved: list[dict]) -> str:
    lk = lookup(data["taxonomy"])
    out = []
    for cat in PAGE_ORDER:
        fname, title, sec = PAGES[cat]
        recs = [r for r in resolved if category_of(r) == cat]
        if not recs:
            continue
        out += [f"<details{' open' if cat == 'static_general' else ''}>",
                f"<summary><b>{title}</b> · {sec} · {len(recs)} works</summary>", ""]
        if cat in SETTING_ORDER:
            out += ["| Model | Paper | Venue | Year | D1 · D2 | D3 | D4 | Links |",
                    "| :--- | :--- | :--- | :---: | :--- | :--- | :--- | :--- |"]
            for r in recs:
                t = r["taxonomy"]
                out.append(f"| [{md_text(r['model'])}](papers/{fname}#{anchor(r)}) | {md_text(r['title'])} | "
                           f"{md_text(r['venue'])} | {r['year']} | {md_text(t['d1'])} · {md_text(t['d2'])} | "
                           f"{', '.join(lk['level'][x] for x in t['d3'])} | {', '.join(lk['type'][x] for x in t['d4'])} | "
                           f"{_short_links(r)} |")
        elif cat == "discussed":
            out += ["| Model | Paper | Venue | Year | Discussed in | Links |", "| :--- | :--- | :--- | :---: | :--- | :--- |"]
            for r in recs:
                out.append(f"| [{md_text(r['model'])}](papers/{fname}#{anchor(r)}) | {md_text(r['title'])} | {md_text(r['venue'])} | "
                           f"{r['year']} | {', '.join(s.split(' ')[0] for s in r['manuscript_sections'])} | {_short_links(r)} |")
        else:
            out += ["| Model | Paper | Data setting | Task | Pattern | Year | Links |",
                    "| :--- | :--- | :--- | :--- | :---: | :---: | :--- |"]
            for r in recs:
                a = r["application"]
                pat = a["dominant_pattern"] + (f"+{a['secondary_pattern']}" if a.get("secondary_pattern") else "")
                mk = ("†" if r["precursor"] else "") + ("◆" if r["multimodal"] else "")
                out.append(f"| [{md_text(r['model'])}](papers/{fname}#{anchor(r)}){mk} | {md_text(r['title'])} | "
                           f"{md_text(lk['subdomain'][a['subdomain']])} | {md_text(a['task'])} | {pat} | {r['year']} | {_short_links(r)} |")
        out += ["", f"➡ Full cards: [papers/{fname}](papers/{fname})", "", "</details>", ""]
    return "\n".join(out)


def _short_links(r: dict) -> str:
    p = []
    if r["doi"] != NR:
        p.append(f"[DOI]({r['doi']})")
    if r["arxiv"] != NR:
        p.append(f"[arXiv]({r['arxiv']})")
    if r["url"] != NR:
        p.append(f"[URL]({r['url']})")
    if not p:
        p.append(f"[🔎]({r['search_link']})")
    return " ".join(p)


def tables_block(tables) -> str:
    rows = ["| # | Table | Formats |", "| :--- | :--- | :--- |"]
    for i, (tid, tb) in enumerate(tables.items(), 1):
        rows.append(f"| {i} | [{tb.title}](tables/markdown/{tid}.md) | "
                    f"[Markdown](tables/markdown/{tid}.md) · [LaTeX](tables/latex/{tid}.tex) · [CSV](tables/csv/{tid}.csv) |")
    return "\n".join(rows)


def replace_block(text: str, name: str, content: str) -> str:
    pat = re.compile(rf"(<!-- BEGIN:{name} -->)(.*?)(<!-- END:{name} -->)", re.S)
    if not pat.search(text):
        raise ValueError(f"README marker BEGIN:{name}/END:{name} not found")
    return pat.sub(lambda m: m.group(1) + "\n" + content.strip() + "\n" + m.group(3), text)


def readme_output(data, resolved, extraction, tables, findings) -> dict[Path, str]:
    text = README.read_text(encoding="utf-8")
    text = replace_block(text, "STATS", stats_block(data, resolved, extraction, len(tables)))
    text = replace_block(text, "MERMAID_TAXONOMY", mermaid_taxonomy(data, resolved))
    text = replace_block(text, "MERMAID_SETTINGS", mermaid_settings(data, resolved))
    text = replace_block(text, "CATALOGUE", catalogue_block(data, resolved))
    text = replace_block(text, "TABLES", tables_block(tables))
    sev = Counter(f.severity for f in findings)
    text = replace_block(text, "FLAGS", f"Current status: **{sev.get('error', 0)} errors**, "
                                        f"**{sev.get('warning', 0)} warnings**, {sev.get('info', 0)} informational notes "
                                        "— see [docs/FLAGS.md](docs/FLAGS.md).")
    return {README: text}


def flags_output(findings, resolved) -> dict[Path, str]:
    names = {r["key"]: r["model"] for r in resolved}
    order = {"error": 0, "warning": 1, "info": 2}
    lines = ["# Open flags and data-quality findings", "",
             "Generated by `scripts/build.py` (checks in `scripts/quality.py`). Errors fail `validate.py`; warnings and "
             "informational notes require author attention but do not block the build.", ""]
    for sev in ("error", "warning", "info"):
        fs = sorted([f for f in findings if f.severity == sev], key=lambda f: (f.code, f.key))
        lines += [f"## {sev.capitalize()}s ({len(fs)})", ""]
        if not fs:
            lines += ["None.", ""]
            continue
        lines += ["| Code | Work | Finding |", "| :--- | :--- | :--- |"]
        for f in fs:
            who = f"{names.get(f.key, '')} (`{f.key}`)" if f.key in names else f"`{f.key}`"
            lines.append(f"| `{f.code}` | {md_text(who)} | {md_text(f.message)} |")
        lines.append("")
    return {DOCS / "FLAGS.md": "\n".join(lines) + "\n"}


def catalogue_outputs(data, resolved, extraction, tables, findings) -> dict[Path, str]:
    out = category_pages(data, resolved)
    out.update(flags_output(findings, resolved))
    out.update(readme_output(data, resolved, extraction, tables, findings))
    return out


if __name__ == "__main__":
    from build import build

    build(only=["catalogue"])
