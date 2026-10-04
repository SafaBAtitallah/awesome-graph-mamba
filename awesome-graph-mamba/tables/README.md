# Comparison tables

All tables are generated from `data/` by `scripts/generate_tables.py`. Each is available in three formats.

| Table | Description | Markdown | LaTeX | CSV |
| :--- | :--- | :---: | :---: | :---: |
| T1 · Taxonomy dimensions | Taxonomy dimensions used to classify Graph Mamba architectures (manuscript tab:taxonomy-dimensions). | [md](markdown/taxonomy_dimensions.md) | [tex](latex/taxonomy_dimensions.tex) | [csv](csv/taxonomy_dimensions.csv) |
| T2 · Unified D1–D4 taxonomy of Graph Mamba architectures | Unified taxonomy of representative Graph Mamba architectures according to tokenization (D1), ordering (D2), coupling (D3), and integration (D4) (manuscript tab:… | [md](markdown/unified_taxonomy.md) | [tex](latex/unified_taxonomy.tex) | [csv](csv/unified_taxonomy.csv) |
| T3 · Structural and computational trade-offs per dimension | Structural and computational implications of the Graph Mamba taxonomy dimensions (manuscript tab:structural-tradeoffs), with the cost term of eq:end-to-end-cost… | [md](markdown/structural_tradeoffs.md) | [tex](latex/structural_tradeoffs.tex) | [csv](csv/structural_tradeoffs.csv) |
| T4 · Cross-domain applications and graph–SSM design patterns | Cross-domain Graph Mamba applications and recurring graph–SSM design patterns (manuscript tab:cross-domain-applications and fig:design-patterns). | [md](markdown/cross_domain_applications.md) | [tex](latex/cross_domain_applications.tex) | [csv](csv/cross_domain_applications.csv) |
| T5 · Distribution of dominant design patterns across application settings (derived) | Number of reviewed applications per data setting and dominant design pattern. Derived automatically from the dominant-pattern labels of fig:design-patterns; sec… | [md](markdown/pattern_distribution.md) | [tex](latex/pattern_distribution.tex) | [csv](csv/pattern_distribution.csv) |
| T6 · Coupling depth × integration type (derived) | Number of architectures in tab:unified-taxonomy per graph setting, coupling level (D3) and integration type (D4). Derived automatically; an architecture with se… | [md](markdown/coupling_integration.md) | [tex](latex/coupling_integration.tex) | [csv](csv/coupling_integration.csv) |
| T7 · Benchmarks used in the comparative analysis | Representative benchmarks used to evaluate Graph Mamba models (manuscript tab:benchmark-summary). | [md](markdown/benchmark_summary.md) | [tex](latex/benchmark_summary.tex) | [csv](csv/benchmark_summary.csv) |
| T8 · Reported complexity, efficiency, and scalability evidence | Reported complexity (sec. 4.3) and efficiency/scalability evidence (manuscript tab:efficiency-summary). Scan complexity and end-to-end scalability are reported … | [md](markdown/efficiency_summary.md) | [tex](latex/efficiency_summary.tex) | [csv](csv/efficiency_summary.csv) |
| T9 · Theoretical expressive-power results | Theoretical expressive-power results reported for SSM-based graph models, with message-passing GNNs and graph Transformers as references (manuscript tab:express… | [md](markdown/expressivity.md) | [tex](latex/expressivity.tex) | [csv](csv/expressivity.csv) |
| T10 · Open challenges and research directions | Open challenges and future research directions for Graph Mamba (manuscript tab:future-directions). | [md](markdown/future_directions.md) | [tex](latex/future_directions.tex) | [csv](csv/future_directions.csv) |
| T11 · Evidence coverage and reporting gaps (derived) | Kinds of evidence the survey reports for each architecture-level work (taxonomy and discussed models). Derived automatically; it exposes the reporting gaps disc… | [md](markdown/evidence_coverage.md) | [tex](latex/evidence_coverage.tex) | [csv](csv/evidence_coverage.csv) |
| T12 · Index of reviewed works | All works in the paper database with bibliographic metadata resolved from references.bib. | [md](markdown/paper_index.md) | [tex](latex/paper_index.tex) | [csv](csv/paper_index.csv) |
| Published results · Mean classification accuracy (%) on brain benchmarks | Mean classification accuracy (%) on brain benchmarks. Results as reported in the BrainMamba paper and transcribed in manuscript tab:Healthcompare; not reproduce… | [md](markdown/perf_brain.md) | [tex](latex/perf_brain.tex) | [csv](csv/perf_brain.csv) |
| Published results · Hyperspectral image classification | Hyperspectral image classification. Results as reported in the GraphMamba (HSI) paper and transcribed in manuscript tab:RScomparison; not reproduced. | [md](markdown/perf_hsi.md) | [tex](latex/perf_hsi.tex) | [csv](csv/perf_hsi.csv) |
| Published results · Spatio-temporal forecasting benchmarks | Spatio-temporal forecasting benchmarks. Results as reported in the STG-Mamba paper and transcribed in manuscript tab:TRperformance_comparison; not reproduced. | [md](markdown/perf_spatiotemporal.md) | [tex](latex/perf_spatiotemporal.tex) | [csv](csv/perf_spatiotemporal.csv) |
| Published results · Financial forecasting (RMSE) and training time | Financial forecasting (RMSE) and training time. Results as reported in the SAMBA paper and transcribed in manuscript tab:FMcomparison; not reproduced. | [md](markdown/perf_financial.md) | [tex](latex/perf_financial.tex) | [csv](csv/perf_financial.csv) |
| Published results · Aspect-based sentiment analysis | Aspect-based sentiment analysis. Results as reported in the MambaForGCN paper and transcribed in manuscript tab:SAperformance; not reproduced. | [md](markdown/perf_absa.md) | [tex](latex/perf_absa.tex) | [csv](csv/perf_absa.csv) |

## Using the LaTeX tables

```latex
\usepackage{booktabs,longtable,multirow,array,graphicx,amsmath,pifont}
\newcommand{\cmark}{\ding{51}}
\input{tables/latex/unified_taxonomy}
```

`tables/latex/all_tables.tex` is a compilable demo document that inputs every table.
