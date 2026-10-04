"""Unit tests for the LaTeX/BibTeX parsing utilities."""
from common import (bib_links, cite_keys, format_authors, latex_to_text, md_text, strip_comments,
                    tex_text)
from extract_papers import parse_cross_domain, parse_design_pattern_figure, parse_unified_taxonomy

TAXONOMY = {
    "graph_settings": [{"id": "static_general", "label": "Static and General-Purpose Graph Models"}],
    "application_domains": [{"id": "healthcare", "label": "Healthcare and Biomedical Applications",
                             "subdomains": [{"id": "histopathology", "label": "Histopathology"}]}],
}


def test_strip_comments_keeps_escaped_percent():
    assert strip_comments("a 50\\% b % comment") == "a 50\\% b "


def test_cite_keys_multiple_and_macro_params():
    assert cite_keys("x \\cite{a,b} y \\citep{c} \\cite{#3}") == ["a", "b", "c"]


def test_latex_to_text_accents_and_braces():
    assert latex_to_text("Ve{\\'e}lickovi{\\'c} -- {GNN}") == "Veélicković – GNN"


def test_format_authors():
    assert format_authors("Wang, Chloe and Ma, Jun and others") == "Chloe Wang, Jun Ma, et al."


def test_bib_links_from_journal_arxiv_and_doi():
    assert bib_links({"journal": "arXiv preprint arXiv:2402.00789"})["arxiv"] == "https://arxiv.org/abs/2402.00789"
    assert bib_links({"doi": "10.1/x"})["doi"] == "https://doi.org/10.1/x"
    assert bib_links({"journal": "Pattern Recognition"}) == {}


def test_text_conversion_preserves_math():
    assert tex_text("a & b $O(n\\lvert V\\rvert)$") == "a \\& b $O(n\\lvert V\\rvert)$"
    assert md_text("a -- b | c") == "a – b \\| c"


UNIFIED = r"""
\begin{table*}[h]\caption{x}\label{tab:unified-taxonomy}
\begin{tabular}{lll}
\toprule
\multirow{2}{*}{\textbf{Model}} & a \\
\midrule
\multicolumn{10}{l}{\textbf{Static and General-Purpose Graph Models}} \\
\midrule
GSSC~\cite{huang2024can} & Node features & Order-free & & & \cmark & \cmark & & & \\
DMbaGCN~\cite{he2026dual} & States & Bidirectional & & \cmark & & & & \cmark & \cmark \\
\bottomrule
\end{tabular}
\end{table*}
"""


def test_parse_unified_taxonomy():
    rows = parse_unified_taxonomy(UNIFIED, TAXONOMY)
    assert [r["key"] for r in rows] == ["huang2024can", "he2026dual"]
    assert rows[0]["setting"] == "static_general"
    assert rows[0]["d3"] == ["operator"] and rows[0]["d4"] == ["standalone"]
    assert rows[1]["d3"] == ["dynamics"] and rows[1]["d4"] == ["parallel", "embedded"]


CROSS = r"""
\begin{longtable}{llll}
\caption{x}\label{tab:cross-domain-applications}\\
\endlastfoot
\multicolumn{8}{l}{\textbf{Healthcare and Biomedical Applications}}\\
\rowcolor{gray!12}
\multicolumn{8}{l}{\textbf{\textit{Histopathology}}} \\
GraphS4mer$^{\dagger}$~\cite{tang2023modeling} & Task & Graph & Labor. & & \cmark & & \\
\end{longtable}
"""


def test_parse_cross_domain():
    rows = parse_cross_domain(CROSS, TAXONOMY)
    assert rows[0]["key"] == "tang2023modeling"
    assert rows[0]["precursor"] is True
    assert rows[0]["subdomain"] == "histopathology" and rows[0]["patterns"] == ["RT"]


FIG = r"""
\begin{figure*}
 \phd{dB}{Clinical}
 \gw{RT}{MGSSM-SAKI$^{+\mathrm{DV}}$}{xu2024identifying}\\
 \gw{DV}{MGDTA$^{\blacklozenge}$}{han2024innovative}\\
\caption{x}\label{fig:design-patterns}
\end{figure*}
"""


def test_parse_design_pattern_figure():
    rows = {r["key"]: r for r in parse_design_pattern_figure(FIG)}
    assert rows["xu2024identifying"]["dominant"] == "RT" and rows["xu2024identifying"]["secondary"] == "DV"
    assert rows["han2024innovative"]["multimodal"] is True
