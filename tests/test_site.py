"""Regression tests for the GitHub Pages explorer (docs/index.html).

Static tests inspect the generated page and its embedded payload. Browser
tests drive the real page in headless Chrome/Chromium (skipped when no
browser is installed): a probe script is appended to a copy of the page,
performs the interactions, and writes its observations as JSON into the DOM,
which ``--dump-dom`` returns.
"""
import json
import re
import shutil
import subprocess

import pytest

from common import DOCS, TABLES, load_yaml, ROOT

INDEX = DOCS / "index.html"


def payload():
    html = INDEX.read_text(encoding="utf-8")
    return json.loads(re.search(r'<script id="data" type="application/json">(.*?)</script>', html, re.S).group(1))


# ---------------------------------------------------------------------------
# Static checks
# ---------------------------------------------------------------------------
def test_navigation_sections_present():
    html = INDEX.read_text(encoding="utf-8")
    for sid, label in [("overview", "Overview"), ("taxonomy", "Architecture Taxonomy"), ("applications", "Applications"),
                       ("explorer", "Literature Explorer"), ("tables", "Comparison Tables")]:
        assert f'id="{sid}"' in html
        assert f'<a href="#{sid}">{label}</a>' in html


def test_embedded_tables_match_generated_csv():
    tables = payload()["tables"]
    assert len(tables) == len(list((TABLES / "csv").glob("*.csv")))
    for t in tables:
        assert t["csv"] == (TABLES / "csv" / f"{t['id']}.csv").read_text(encoding="utf-8"), t["id"]
        width = len(t["headers"])
        assert all(len(r) == width for r in t["rows"] if isinstance(r, list)), t["id"]


def test_table_cells_keep_survey_markers():
    t = next(t for t in payload()["tables"] if t["id"] == "paper_index")
    models = [r[0]["t"] for r in t["rows"] if isinstance(r, list)]
    assert any(m.endswith("†") for m in models)


def test_definitions_come_from_taxonomy_yaml():
    tx = load_yaml(ROOT / "data" / "taxonomy.yaml")
    p = payload()
    assert p["dimensions"] == tx["dimensions"]
    assert p["patterns"] == tx["design_patterns"]
    assert p["abbreviations"] == tx["abbreviations"]


def test_verification_note_matches_readme_definition():
    html = INDEX.read_text(encoding="utf-8")
    assert 'p.verification.status !== "verified"' in html
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    pending = sum(p["verification"]["status"] != "verified" for p in payload()["papers"])
    assert f"{pending} of {len(payload()['papers'])} records await author verification" in readme


def test_comparison_page_redirects_to_tables_section():
    html = (DOCS / "comparison.html").read_text(encoding="utf-8")
    assert 'http-equiv="refresh"' in html and 'href="./#tables"' in html


# ---------------------------------------------------------------------------
# Browser checks
# ---------------------------------------------------------------------------
CHROME = next((shutil.which(b) for b in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser")
               if shutil.which(b)), None)
needs_browser = pytest.mark.skipif(CHROME is None, reason="no headless Chrome/Chromium available")

PROBE = r"""
<script>
(async function(){
  const R = {}, $ = id => document.getElementById(id);
  const tick = () => new Promise(r => setTimeout(r, 0));
  const key = (el, k) => el.dispatchEvent(new KeyboardEvent("keydown", {key: k, bubbles: true}));
  const D = JSON.parse($("data").textContent), P = D.papers;
  try {
    R.overflowX = document.documentElement.scrollWidth - window.innerWidth;
    // --- architecture matrix: counts, multi-label, cell panel, explorer filter ---
    const archCell = (lv, ty) => document.querySelector(`#mxArch button.cell[data-lv="${lv}"][data-ty="${ty}"]`);
    R.archCounts = {};
    document.querySelectorAll("#mxArch button.cell").forEach(b => R.archCounts[b.dataset.lv + "|" + b.dataset.ty] = +b.querySelector(".num").textContent);
    R.archTabStops = [...document.querySelectorAll("#mxArch button.cell")].filter(b => b.tabIndex === 0).length;
    archCell("input", "standalone").focus();
    key(document.activeElement, "ArrowRight");
    R.arrowRight = document.activeElement.dataset.fid;
    key(document.activeElement, "ArrowDown");
    R.arrowDown = document.activeElement.dataset.fid;
    archCell("dynamics", "parallel").focus();
    archCell("dynamics", "parallel").click();
    R.archPressed = archCell("dynamics", "parallel").getAttribute("aria-pressed");
    R.focusKeptAfterClick = document.activeElement.dataset.fid;
    R.archPanelKeys = [...document.querySelectorAll("#archPanel .mitem")].map(b => b.dataset.key);
    R.archListKeys = [...document.querySelectorAll("#list button[data-key]")].map(b => b.dataset.key);
    R.archChip = [...document.querySelectorAll("#chips .fchip")].map(c => c.dataset.clear);
    R.panelCellsPerKey = {};
    for (const [lv, ty] of [["dynamics","parallel"],["dynamics","embedded"]]) {
      archCell(lv, ty).click();
      if (archCell(lv, ty).getAttribute("aria-pressed") !== "true") archCell(lv, ty).click();
      R.panelCellsPerKey[lv + "|" + ty] = [...document.querySelectorAll("#archPanel .mitem")].map(b => b.dataset.key);
    }
    document.querySelector('#chips .fchip[data-clear="arch"]').click();
    R.afterChipClear = {d3pressed: document.querySelectorAll('#mxArch button.cell[aria-pressed="true"]').length,
                        list: document.querySelectorAll("#list button[data-key]").length};

    // --- applications matrix ---
    const app = P.filter(p => p.application);
    const ap = app[0].application;
    const appBtn = document.querySelector(`#mxApp button.cell[data-sub="${ap.subdomain}"][data-pt="${ap.dominant_pattern}"]`);
    appBtn.click();
    R.appExpected = app.filter(p => p.application.subdomain === ap.subdomain && p.application.dominant_pattern === ap.dominant_pattern).map(p => p.key).sort();
    R.appPanelKeys = [...document.querySelectorAll("#appPanel .mitem")].map(b => b.dataset.key).sort();
    R.appListKeys = [...document.querySelectorAll("#list button[data-key]")].map(b => b.dataset.key).sort();
    R.appCellSum = [...document.querySelectorAll("#mxApp button.cell .num")].reduce((s, n) => s + +n.textContent, 0);
    document.querySelector('#appPanel [data-act="clear-app"]').click();

    // --- search, filters, sorting ---
    const q = $("q"); q.value = "GSSC"; q.dispatchEvent(new Event("input", {bubbles: true}));
    R.searchKeys = [...document.querySelectorAll("#list button[data-key]")].map(b => b.dataset.key);
    $("reset").click();
    R.afterReset = document.querySelectorAll("#list .card").length;
    document.querySelector('.tg[data-role="discussed"]').click();
    R.discussedOnly = [...document.querySelectorAll("#list button[data-key]")].map(b => b.dataset.key).sort();
    $("reset").click();
    $("sort").value = "new"; $("sort").dispatchEvent(new Event("change", {bubbles: true}));
    R.sortedYears = [...document.querySelectorAll("#list .cmeta")].map(m => +m.textContent.trim().slice(-4));
    $("sort").value = "survey"; $("sort").dispatchEvent(new Event("change", {bubbles: true}));
    const y = document.querySelector("#years .ybar"); y.click();
    R.yearFilter = {year: y.dataset.year, select: $("fy").value, n: document.querySelectorAll("#list .card").length,
                    expected: P.filter(p => String(p.year) === y.dataset.year).length};
    $("reset").click();

    // --- long names never overflow their card ---
    R.overflowingNames = [...document.querySelectorAll("#list .card h3")].filter(h => h.scrollWidth > h.clientWidth + 1).map(h => h.textContent);

    // --- detail drawer: open from card, hash, next, close returns focus ---
    const first = document.querySelector("#list button[data-key]");
    first.focus(); first.click(); await tick();
    R.dialogOpen = $("paper").open;
    R.dialogTitle = $("dTitle").textContent;
    R.hash = decodeURIComponent(location.hash.slice(1));
    R.firstKey = first.dataset.key;
    $("dNext").click();
    R.afterNext = decodeURIComponent(location.hash.slice(1));
    R.prevDisabled = $("dPrev").disabled;
    $("paper").close(); await tick();
    R.dialogClosed = !$("paper").open;
    R.focusReturned = document.activeElement && document.activeElement.dataset.fid;
    R.hashAfterClose = location.hash;

    // --- open from matrix panel, glossary from drawer ---
    archCell("input", "standalone").click();
    document.querySelector("#archPanel .mitem").click(); await tick();
    R.panelOpens = $("paper").open && $("dTitle").textContent.length > 0;
    document.querySelector("#detail [data-gloss]").click(); await tick();
    R.glossaryOpen = $("glossary").open && $("glossBody").textContent.includes(D.dimensions[0].question);
    $("glossary").close(); $("paper").close(); await tick();
    document.querySelector('#chips .fchip[data-clear="arch"]').click();

    // --- comparison tables ---
    const tb = D.tables.find(t => t.id === "coupling_integration");
    document.querySelector(`#tbNav button[data-tb="${tb.id}"]`).click();
    R.tableHeading = $("tbH").textContent;
    R.tableRows = document.querySelectorAll("#tbView tbody tr:not(.grp)").length;
    R.tableExpectedRows = tb.rows.filter(r => Array.isArray(r)).length;
    R.tableCurrent = document.querySelector('#tbNav [aria-current="true"]').dataset.tb;
    R.tableTitle = tb.title;

    // --- accessible names ---
    R.unnamedButtons = [...document.querySelectorAll("button")].filter(b => !(b.getAttribute("aria-label") || b.textContent.trim())).length;
    R.unlabelledControls = [...document.querySelectorAll("input,select")].filter(c => !(c.labels && c.labels.length) && !c.getAttribute("aria-label")).length;
    R.overflowXEnd = document.documentElement.scrollWidth - window.innerWidth;
  } catch (e) { R.error = String(e && e.stack || e); }
  const pre = document.createElement("pre"); pre.id = "probe-result"; pre.textContent = JSON.stringify(R);
  document.body.appendChild(pre);
})();
</script>
"""


def run_probe(tmp_path, width):
    page = tmp_path / "index.html"
    page.write_text(INDEX.read_text(encoding="utf-8").replace("</body>", PROBE + "</body>"), encoding="utf-8")
    out = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--no-first-run",
                          f"--window-size={width},900", "--virtual-time-budget=5000", "--dump-dom", page.as_uri()],
                         capture_output=True, text=True, timeout=120)
    m = re.search(r'<pre id="probe-result">(.*?)</pre>', out.stdout, re.S)
    assert m, out.stderr[-2000:]
    import html as h
    r = json.loads(h.unescape(m.group(1)))
    assert "error" not in r, r["error"]
    return r


@pytest.fixture(scope="module", params=[1366, 390], ids=["desktop", "mobile"])
def probe(request, tmp_path_factory):
    if CHROME is None:
        pytest.skip("no headless Chrome/Chromium available")
    return run_probe(tmp_path_factory.mktemp(f"site{request.param}"), request.param)


@needs_browser
def test_no_horizontal_page_scroll(probe):
    assert probe["overflowX"] <= 0 and probe["overflowXEnd"] <= 0


@needs_browser
def test_arch_matrix_counts_and_multilabel(probe):
    P = payload()["papers"]
    arch = [p for p in P if p["taxonomy"]]
    for cell, n in probe["archCounts"].items():
        lv, ty = cell.split("|")
        assert n == sum(lv in p["taxonomy"]["d3"] and ty in p["taxonomy"]["d4"] for p in arch), cell
    # every assignment of a multi-label model appears in each of its cells
    for p in arch:
        for lv in p["taxonomy"]["d3"]:
            for ty in p["taxonomy"]["d4"]:
                key = f"{lv}|{ty}"
                if key in probe["panelCellsPerKey"]:
                    assert p["key"] in probe["panelCellsPerKey"][key]


@needs_browser
def test_arch_cell_selects_panel_and_filters_explorer(probe):
    P = payload()["papers"]
    expected = sorted(p["key"] for p in P if p["taxonomy"] and "dynamics" in p["taxonomy"]["d3"] and "parallel" in p["taxonomy"]["d4"])
    assert probe["archPressed"] == "true"
    assert sorted(probe["archPanelKeys"]) == expected
    assert sorted(probe["archListKeys"]) == expected
    assert "arch" in probe["archChip"]
    assert probe["afterChipClear"] == {"d3pressed": 0, "list": len(P)}


@needs_browser
def test_matrix_keyboard_navigation(probe):
    assert probe["archTabStops"] == 1
    assert probe["arrowRight"] == "arch-input-sequential"
    assert probe["arrowDown"] == "arch-dynamics-sequential"
    assert probe["focusKeptAfterClick"] == "arch-dynamics-parallel"


@needs_browser
def test_app_matrix_cell(probe):
    assert probe["appPanelKeys"] == probe["appExpected"] == probe["appListKeys"]
    assert probe["appCellSum"] == payload()["counts"]["application"]


@needs_browser
def test_search_filters_sort_and_year_chart(probe):
    P = payload()["papers"]
    assert "huang2024can" in probe["searchKeys"]
    assert probe["afterReset"] == len(P)
    assert probe["discussedOnly"] == sorted(p["key"] for p in P if "discussed" in p["roles"])
    assert probe["sortedYears"] == sorted(probe["sortedYears"], reverse=True)
    yf = probe["yearFilter"]
    assert yf["select"] == yf["year"] and yf["n"] == yf["expected"]


@needs_browser
def test_long_model_names_do_not_overflow(probe):
    assert probe["overflowingNames"] == []


@needs_browser
def test_detail_drawer(probe):
    assert probe["dialogOpen"] and probe["hash"] == probe["firstKey"]
    assert probe["afterNext"] != probe["firstKey"] and probe["prevDisabled"] is False
    assert probe["dialogClosed"] and probe["focusReturned"] == f"card-{probe['firstKey']}"
    assert probe["firstKey"] not in probe["hashAfterClose"]
    assert probe["panelOpens"] and probe["glossaryOpen"]


@needs_browser
def test_comparison_table_view(probe):
    assert probe["tableCurrent"] == "coupling_integration"
    assert probe["tableHeading"] == probe["tableTitle"]
    assert probe["tableRows"] == probe["tableExpectedRows"]


@needs_browser
def test_controls_have_accessible_names(probe):
    assert probe["unnamedButtons"] == 0
    assert probe["unlabelledControls"] == 0
