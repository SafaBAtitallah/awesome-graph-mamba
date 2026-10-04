<div align="center">

# Exploring Graph Mamba

### A Comprehensive Survey on State-Space Models for Graph Learning — Companion Repository

**Safa Ben Atitallah · Chaima Ben Rabah · Maha Driss · Wadii Boulila · Anis Koubaa**

*ACM Computing Surveys (under revision)*

[![Validate](https://github.com/SafaBAtitallah/awesome-graph-mamba/actions/workflows/update.yml/badge.svg)](https://github.com/SafaBAtitallah/awesome-graph-mamba/actions/workflows/update.yml)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

**[Open the interactive explorer](https://OWNER.github.io/awesome-graph-mamba/)**

[Overview](#overview) · [Taxonomy](#taxonomy) · [Catalogue](#paper-catalogue) · [Tables](#comparison-tables) · [Reproduce](#reproduce-the-repository) · [Contribute](#contributing) · [Cite](#citation)

</div>

---

## Overview

Graph Mamba extends selective State-Space Models (SSMs) to graph-structured data with the aim of efficiently capturing long-range dependencies. Because Mamba is designed for ordered sequences, every Graph Mamba architecture must decide how a graph becomes something an SSM can read. The survey organizes the field around **four design questions**:

| | Design question | What it asks |
| :---: | :--- | :--- |
| **D1** | **Tokenization** | *What* does the state-space model read? |
| **D2** | **Ordering** | In *what order* does it read it? |
| **D3** | **Coupling** | *How deeply* does graph structure shape the state dynamics? (input-, dynamics-, operator-level) |
| **D4** | **Integration** | *How* does the SSM work alongside graph propagation? (standalone, sequential, parallel, embedded) |

This repository turns the survey's literature review into a **living, taxonomy-driven resource**: a curated, machine-readable paper database, auto-generated comparison tables (Markdown, LaTeX, CSV), and a validated build pipeline that keeps everything consistent with the manuscript.

<!-- BEGIN:STATS -->
| Works in database | Architectures (D1–D4) | Applications | Discussed only (Sec. 7) | Cited references | Comparison tables |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **55** | 21 | 30 | 4 | 123 | 17 |

**Publication years (BibTeX):** 2023: 1 · 2024: 19 · 2025: 21 · 2026: 14  
**Verification status:** 55 of 55 records await author verification ([open flags](docs/FLAGS.md)).
<!-- END:STATS -->

### Research questions

| | Question | Survey sections |
| :---: | :--- | :--- |
| **RQ1** | How is graph structure incorporated into selective state-space modeling? | §3, §5 |
| **RQ2** | What architectural, structural, and computational implications follow from these design choices? | §4 |
| **RQ3** | Under which graph settings, tasks, datasets, and evaluation conditions are the reported advantages of Graph Mamba supported? | §6 |
| **RQ4** | Which unresolved challenges currently limit reliable progress in Graph Mamba? | §7 |

### Contributions of the survey

1. A **unified architectural perspective** on Graph Mamba, clarifying how graph information is transformed, serialized, and integrated into selective state-space computation.
2. A **taxonomy based on four design questions** — tokenization, ordering, coupling, and integration — with input-, dynamics-, and operator-level coupling.
3. A **synthesis** of applications, structural and computational trade-offs, evaluation practices, and reported performance across graph-learning settings.
4. **Open research directions** on robustness, scalability, interpretability, reproducibility, and future Graph Mamba designs.

### Scope and inclusion criteria

Studies published from 2023 to September 2026 were collected from IEEE Xplore, ACM DL, Scopus, Web of Science, and Google Scholar, complemented by backward/forward citation search. Included works explicitly integrate Mamba, selective SSMs, or closely related structured SSMs with graph-structured representations; earlier structured-SSM approaches are retained when they are direct architectural foundations (marked **†**). Mamba applied only to sequences or images without an explicit graph component is excluded.

---

## Taxonomy

The four design questions form a multi-label taxonomy: each architecture receives a D1 and D2 description and one or more D3/D4 labels.

<!-- BEGIN:MERMAID_TAXONOMY -->
```mermaid
flowchart LR
  GM"Graph Mamba architectures"
  GM --> D1"D1 · Tokenization<br/><i>What information is presented to the state-space model?</i>"
  GM --> D2"D2 · Ordering<br/><i>How are graph-derived representations ordered and traversed?</i>"
  GM --> D3"D3 · Coupling<br/><i>Does graph information directly affect the selective state dynamics?</i>"
  D3 --> D3_input"Input-level"
  D3 --> D3_dynamics"Dynamics-level"
  D3 --> D3_operator"Operator-level"
  GM --> D4"D4 · Integration<br/><i>How is the SSM combined with other graph-learning mechanisms?</i>"
  D4 --> D4_standalone"Standalone"
  D4 --> D4_sequential"Sequential"
  D4 --> D4_parallel"Parallel"
  D4 --> D4_embedded"Embedded"
  classDef dim fill:#1f3b73,color:#fff,stroke:#1f3b73;
  class D1,D2,D3,D4 dim;
```
<!-- END:MERMAID_TAXONOMY -->

The reviewed literature is presented in three **graph settings** (architectures, §3) and three **application areas** (§5). Each setting emphasizes a different design question: in static graphs the decisive question is *ordering*; in dynamic graphs time largely answers ordering, so effort shifts to *coupling*; in heterogeneous and higher-order graphs most structure is carried by *tokenization*.

<!-- BEGIN:MERMAID_SETTINGS -->
```mermaid
flowchart TB
  R"Reviewed Graph Mamba literature"
  R --> S0"Static and General-Purpose Graph Models (7)"
  S0 --- S0m"GSSC · GMN · Graph-Mamba · GrassNet · MbaGCN · DMbaGCN · GLADMamba"
  R --> S1"Dynamic and Spatio-Temporal Graph Models (10)"
  S1 --- S1m"GraphSSM · GSSM · DG-Mamba · DyGMamba · DyG-Mamba · STG-Mamba · SpoT-Mamba · PS-Mamba · FuzzMamba · STMAGRN"
  R --> S2"Heterogeneous and Higher-Order Graph Models (4)"
  S2 --- S2m"HeteGraph-Mamba · Mamba-GTC · TopoMamba · CCMamba"
  R --> A0"Healthcare and Biomedical Applications (19)"
  A0 --- A0s0"Neural and physiological signals: GraphS4mer, BrainMamba, Brain-GM, Brain Network Mamba, MSGM"
  A0 --- A0s1"Clinical, biological, and molecular data: MGSSM-SAKI, Aghaee et al., ExPath, MGDTA, MKHCNet"
  A0 --- A0s2"Histopathology: GAT–Mamba, GraphMamba (WSI), MGCM, TopoMamSurv, CGAM"
  A0 --- A0s3"Medical imaging: GM-UNet, GGVMamba, HGM, GMMN"
  R --> A1"Remote Sensing and Structured Visual Applications (7)"
  A1 --- A1s0"Remote sensing: GraphMamba (HSI), MGF-GCN, GraphMamba (tok.), TGMN, GM-HAD"
  A1 --- A1s1"Articulated and human motion: Hamba, Tang et al."
  R --> A2"Other Application Areas (4)"
  A2 --- A2s0"Financial forecasting: SAMBA"
  A2 --- A2s1"Industrial prognostics: Ren et al."
  A2 --- A2s2"Cybersecurity and intrusion detection: IDS–GraphMamba"
  A2 --- A2s3"Language and semantic modeling: MambaForGCN"
  classDef set fill:#e8eef9,stroke:#1f3b73;
  classDef app fill:#fdf1e3,stroke:#b46b12;
  class S0,S1,S2 set;
  class A0,A1,A2 app;
```
<!-- END:MERMAID_SETTINGS -->

**Application design patterns (§5).** Each application is assigned a dominant (and optionally secondary) graph–SSM pattern: **DV** dual-view (graph and SSM process complementary views), **RT** relational–temporal (graph captures relations, SSM models temporal evolution), **GS** graph-guided sequence (graph structure guides tokenization, ordering, or scanning), **LG** local-to-global (local graph processing combined with broader SSM context).

---

## Paper catalogue

Click a model to open its full card (methodology, D1–D4 or pattern assignment, contributions, complexity, benchmarks, stated limitations, and the survey sections that discuss it). Markers: **†** structured-SSM precursor without input-dependent selection · **◆** multimodal input · 🔎 no DOI/arXiv in the bibliography (Scholar search link).

<!-- BEGIN:CATALOGUE -->
<details open>
<summary><b>Static and General-Purpose Graph Models</b> · Sec. 3.2 · 7 works</summary>

| Model | Paper | Venue | Year | D1 · D2 | D3 | D4 | Links |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| [GSSC](papers/static-general.md#huang2024can) | What Can We Learn from State Space Models for Machine Learning on Graphs? | arXiv preprint arXiv:2406.05815 | 2024 | Node features and graph positional information · Order-free | Operator-level | Standalone | [arXiv](https://arxiv.org/abs/2406.05815) |
| [GMN](papers/static-general.md#behrouz2024graph) | Graph mamba: Towards learning on graphs with state space models | Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining | 2024 | Neighborhood/subgraph tokens · Ordered, bidirectional | Input-level | Parallel | [🔎](https://scholar.google.com/scholar?q=%22Graph+mamba%3A+Towards+learning+on+graphs+with+state+space+models%22) |
| [Graph-Mamba](papers/static-general.md#wang2024graph) | Graph-mamba: Towards long-range graph sequence modeling with selective state spaces | arXiv preprint arXiv:2402.00789 | 2024 | Node representations · Degree-based prioritization and permutation | Input-level | Parallel | [arXiv](https://arxiv.org/abs/2402.00789) |
| [GrassNet](papers/static-general.md#zhao2024grassnet) | Grassnet: State space model meets graph neural network | Pattern Recognition | 2026 | Graph spectrum embeddings · Frequency-ordered, bidirectional | Operator-level | Standalone | [🔎](https://scholar.google.com/scholar?q=%22Grassnet%3A+State+space+model+meets+graph+neural+network%22) |
| [MbaGCN](papers/static-general.md#he2025mamba) | Mamba-Based Graph Convolutional Networks: Tackling Over-Smoothing with Selective State Space | Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI) | 2025 | Neighborhood representations across layers · No explicit node serialization | Dynamics-level | Embedded | [DOI](https://doi.org/10.24963/ijcai.2025/595) |
| [DMbaGCN](papers/static-general.md#he2026dual) | Dual Mamba for Node-Specific Representation Learning: Tackling Over-Smoothing with Selective State Space Modeling | Proceedings of the AAAI Conference on Artificial Intelligence | 2026 | Layer-wise node states and node sequence · Bidirectional global scan | Dynamics-level | Parallel, Embedded | [🔎](https://scholar.google.com/scholar?q=%22Dual+Mamba+for+Node-Specific+Representation+Learning%3A+Tackling+Over-Smoothing+with+Selective+State+Space+Modeling%22) |
| [GLADMamba](papers/static-general.md#fu2025gladmamba) | GLADMamba: Unsupervised Graph-Level Anomaly Detection Powered by Selective State Space Model | Joint European Conference on Machine Learning and Knowledge Discovery in Databases | 2025 | Multi-view graph representations · No central graph serialization | Dynamics-level | Parallel | [🔎](https://scholar.google.com/scholar?q=%22GLADMamba%3A+Unsupervised+Graph-Level+Anomaly+Detection+Powered+by+Selective+State+Space+Model%22) |

➡ Full cards: [papers/static-general.md](papers/static-general.md)

</details>

<details>
<summary><b>Dynamic and Spatio-Temporal Graph Models</b> · Sec. 3.3 · 10 works</summary>

| Model | Paper | Venue | Year | D1 · D2 | D3 | D4 | Links |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| [GraphSSM](papers/dynamic-spatiotemporal.md#li2024state) | State space models on temporal graphs: A first-principles study | Advances in Neural Information Processing Systems | 2024 | Sequence of graph snapshots · Temporal snapshot order | Operator-level | Standalone | [🔎](https://scholar.google.com/scholar?q=%22State+space+models+on+temporal+graphs%3A+A+first-principles+study%22) |
| [GSSM](papers/dynamic-spatiotemporal.md#zhou2024graph) | Graph Convolution Network Based State Space Model for Wireless Traffic Prediction | 2024 IEEE Wireless Communications and Networking Conference (WCNC) | 2024 | Base-station node time series · Temporal order | Dynamics-level | Sequential | [🔎](https://scholar.google.com/scholar?q=%22Graph+Convolution+Network+Based+State+Space+Model+for+Wireless+Traffic+Prediction%22) |
| [DG-Mamba](papers/dynamic-spatiotemporal.md#yuan2025dg) | Dg-mamba: Robust and efficient dynamic graph structure learning with selective state space models | Proceedings of the AAAI Conference on Artificial Intelligence | 2025 | Successive dynamic graph states · Selective scan across graph snapshots | Dynamics-level | Parallel | [🔎](https://scholar.google.com/scholar?q=%22Dg-mamba%3A+Robust+and+efficient+dynamic+graph+structure+learning+with+selective+state+space+models%22) |
| [DyGMamba](papers/dynamic-spatiotemporal.md#ding2024dygmamba) | DyGMamba: Efficiently Modeling Long-Term Temporal Dependency on Continuous-Time Dynamic Graphs with State Space Models | arXiv preprint arXiv:2408.04713 | 2024 | Historical node interactions and temporal patterns · Chronological interaction order | Input-level | Standalone | [arXiv](https://arxiv.org/abs/2408.04713) |
| [DyG-Mamba](papers/dynamic-spatiotemporal.md#li2024dyg) | Dyg-mamba: Continuous state space modeling on dynamic graphs | Advances in Neural Information Processing Systems | 2026 | Timestamped interaction sequences · Irregular chronological event order | Dynamics-level | Standalone | [🔎](https://scholar.google.com/scholar?q=%22Dyg-mamba%3A+Continuous+state+space+modeling+on+dynamic+graphs%22) |
| [STG-Mamba](papers/dynamic-spatiotemporal.md#li2024stg) | Stg-mamba: Spatial-temporal graph learning via selective state space model | arXiv preprint arXiv:2403.12418 | 2024 | Graph-aware node time-series representations · Temporal processing across multiple granularities | Dynamics-level | Parallel | [arXiv](https://arxiv.org/abs/2403.12418) |
| [SpoT-Mamba](papers/dynamic-spatiotemporal.md#choi2024spot) | SpoT-Mamba: Learning Long-Range Dependency on Spatio-Temporal Graphs with Selective State Spaces | arXiv preprint arXiv:2406.11244 | 2024 | Graph-derived neighborhood sequences · BFS, DFS, random-walk, and temporal scanning | Input-level | Standalone | [arXiv](https://arxiv.org/abs/2406.11244) |
| [PS-Mamba](papers/dynamic-spatiotemporal.md#dong2025ps) | PS-Mamba: Spatial-Temporal Graph Mamba for Pose Sequence Refinement | 2025 IEEE/CVF International Conference on Computer Vision (ICCV) | 2025 | Human joints across pose sequences · Four graph-guided bidirectional spatial–temporal scans | Input-level | Parallel | [🔎](https://scholar.google.com/scholar?q=%22PS-Mamba%3A+Spatial-Temporal+Graph+Mamba+for+Pose+Sequence+Refinement%22) |
| [FuzzMamba](papers/dynamic-spatiotemporal.md#chen2026modeling) | Modeling Spatiotemporal Dynamic Shifts for Traffic Cognition: A Fuzzy-based Graph-Mamba Approach | 2026 IEEE International Conference on Fuzzy Systems (FUZZ-IEEE) | 2026 | Node-centric spatial neighborhoods with contextual features · Adaptive spatial ordering varying over time | Dynamics-level | Standalone | [🔎](https://scholar.google.com/scholar?q=%22Modeling+Spatiotemporal+Dynamic+Shifts+for+Traffic+Cognition%3A+A+Fuzzy-based+Graph-Mamba+Approach%22) |
| [STMAGRN](papers/dynamic-spatiotemporal.md#zhang2025spatio) | Spatio-temporal mamba dynamic graph convolutional recurrent network for traffic prediction | IEEE Transactions on Artificial Intelligence | 2025 | Traffic sequences and dynamic graph representations · Temporal sequence processing | Input-level | Sequential | [🔎](https://scholar.google.com/scholar?q=%22Spatio-temporal+mamba+dynamic+graph+convolutional+recurrent+network+for+traffic+prediction%22) |

➡ Full cards: [papers/dynamic-spatiotemporal.md](papers/dynamic-spatiotemporal.md)

</details>

<details>
<summary><b>Heterogeneous and Higher-Order Graph Models</b> · Sec. 3.4 · 4 works</summary>

| Model | Paper | Venue | Year | D1 · D2 | D3 | D4 | Links |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| [HeteGraph-Mamba](papers/heterogeneous-higher-order.md#pan2024hetegraph) | HeteGraph-Mamba: Heterogeneous Graph Learning via Selective State Space Model | arXiv preprint arXiv:2405.13915 | 2024 | Metapath-based heterogeneous graph tokens · Hierarchical within-type and across-type processing | Input-level | Standalone | [arXiv](https://arxiv.org/abs/2405.13915) |
| [Mamba-GTC](papers/heterogeneous-higher-order.md#meng2026mamba-gtc) | Mamba-GTC: Cross-view contrastive learning with state space modeling for heterogeneous graph representation | Knowledge-Based Systems | 2025 | Multi-hop neighborhood tokens · Hop-evolution ordering | Input-level | Parallel | [🔎](https://scholar.google.com/scholar?q=%22Mamba-GTC%3A+Cross-view+contrastive+learning+with+state+space+modeling+for+heterogeneous+graph+representation%22) |
| [TopoMamba](papers/heterogeneous-higher-order.md#montagna2024topological) | Topological deep learning with state-space models: A mamba approach for simplicial complexes | 2025 International Joint Conference on Neural Networks (IJCNN) | 2025 | Incident simplices aggregated by rank · Rank-ordered sequence | Input-level | Standalone | [🔎](https://scholar.google.com/scholar?q=%22Topological+deep+learning+with+state-space+models%3A+A+mamba+approach+for+simplicial+complexes%22) |
| [CCMamba](papers/heterogeneous-higher-order.md#chen2026ccmamba) | CCMamba: Topologically-Informed Selective State-Space Networks on Combinatorial Complexes for Higher-Order Graph Learning | arXiv preprint arXiv:2601.20518 | 2026 | Multi-rank incidence representations · Rank- and incidence-aware linearization | Input-level | Standalone | [arXiv](https://arxiv.org/abs/2601.20518) |

➡ Full cards: [papers/heterogeneous-higher-order.md](papers/heterogeneous-higher-order.md)

</details>

<details>
<summary><b>Healthcare and Biomedical Applications</b> · Sec. 5.1 · 19 works</summary>

| Model | Paper | Data setting | Task | Pattern | Year | Links |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| [GraphS4mer](papers/healthcare.md#tang2023modeling)† | Modeling multivariate biosignals with graph neural networks and structured state space models | Neural and physiological signals | Seizure, sleep, ECG classification | RT | 2023 | [🔎](https://scholar.google.com/scholar?q=%22Modeling+multivariate+biosignals+with+graph+neural+networks+and+structured+state+space+models%22) |
| [BrainMamba](papers/healthcare.md#behrouz2024brain) | Brain-Mamba: Encoding Brain Activity via Selective State Space Models. | Neural and physiological signals | Brain encoding; attention-deficit/hyperactivity disorder and seizure detection | RT+GS | 2024 | [🔎](https://scholar.google.com/scholar?q=%22Brain-Mamba%3A+Encoding+Brain+Activity+via+Selective+State+Space+Models.%22) |
| [Brain-GM](papers/healthcare.md#wang2024learning) | Learning dynamic brain network representation based on graph mamba architecture | Neural and physiological signals | Brain decoding and disease classification | RT | 2024 | [🔎](https://scholar.google.com/scholar?q=%22Learning+dynamic+brain+network+representation+based+on+graph+mamba+architecture%22) |
| [Brain Network Mamba](papers/healthcare.md#zhang2026brainnetworkmamba) | Brain Network Mamba: A Bi-Directional State-Space Model for Brain Network Analysis on rs-fMRI | Neural and physiological signals | Resting-state fMRI analysis | LG | 2026 | [DOI](https://doi.org/10.1007/978-3-032-09513-8_22) |
| [MSGM](papers/healthcare.md#liu2026msgm) | Msgm: A multi-scale spatiotemporal graph mamba for eeg emotion recognition | Neural and physiological signals | EEG emotion recognition | RT | 2026 | [🔎](https://scholar.google.com/scholar?q=%22Msgm%3A+A+multi-scale+spatiotemporal+graph+mamba+for+eeg+emotion+recognition%22) |
| [MGSSM-SAKI](papers/healthcare.md#xu2024identifying) | Identifying Subphenotypes for Sepsis with Acute Kidney Injury via Multimodal Graph State Space Models | Clinical, biological, and molecular data | Sepsis-AKI subphenotyping | RT+DV | 2024 | [🔎](https://scholar.google.com/scholar?q=%22Identifying+Subphenotypes+for+Sepsis+with+Acute+Kidney+Injury+via+Multimodal+Graph+State+Space+Models%22) |
| [Aghaee et al.](papers/healthcare.md#aghaee2024graph)† | Graph Neural Network Representation of State Space Models of Metabolic Pathways | Clinical, biological, and molecular data | Metabolic-pathway modeling | RT | 2024 | [🔎](https://scholar.google.com/scholar?q=%22Graph+Neural+Network+Representation+of+State+Space+Models+of+Metabolic+Pathways%22) |
| [ExPath](papers/healthcare.md#kotoge2026expath) | Targeted pathway inference for biological knowledge bases via graph learning and explanation | Clinical, biological, and molecular data | Pathway inference and explanation | GS | 2026 | [🔎](https://scholar.google.com/scholar?q=%22Targeted+pathway+inference+for+biological+knowledge+bases+via+graph+learning+and+explanation%22) |
| [MGDTA](papers/healthcare.md#han2024innovative)◆ | Innovative Mamba and graph transformer framework for superior protein-ligand affinity prediction | Clinical, biological, and molecular data | Drug–target affinity prediction | DV | 2024 | [🔎](https://scholar.google.com/scholar?q=%22Innovative+Mamba+and+graph+transformer+framework+for+superior+protein-ligand+affinity+prediction%22) |
| [MKHCNet](papers/healthcare.md#lu2025mamba)◆ | Mamba-enhanced disease semantic knowledge graph for interpretable automatic ICD coding | Clinical, biological, and molecular data | Automatic ICD coding | DV | 2025 | [🔎](https://scholar.google.com/scholar?q=%22Mamba-enhanced+disease+semantic+knowledge+graph+for+interpretable+automatic+ICD+coding%22) |
| [GAT–Mamba](papers/healthcare.md#ding2024combining) | Combining graph neural network and Mamba to capture local and global tissue spatial relationships in whole slide images | Histopathology | Lung-cancer survival prediction | LG | 2025 | [🔎](https://scholar.google.com/scholar?q=%22Combining+graph+neural+network+and+Mamba+to+capture+local+and+global+tissue+spatial+relationships+in+whole+slide+images%22) |
| [GraphMamba (WSI)](papers/healthcare.md#zheng2025graphmamba) | GraphMamba: Whole slide image classification meets graph-driven selective state space model | Histopathology | WSI classification | GS | 2025 | [🔎](https://scholar.google.com/scholar?q=%22GraphMamba%3A+Whole+slide+image+classification+meets+graph-driven+selective+state+space+model%22) |
| [MGCM](papers/healthcare.md#cui2026mgcm)◆ | MGCM: Multi-modal graph convolutional mamba for cancer survival prediction | Histopathology | Multimodal cancer survival prediction | DV | 2026 | [🔎](https://scholar.google.com/scholar?q=%22MGCM%3A+Multi-modal+graph+convolutional+mamba+for+cancer+survival+prediction%22) |
| [TopoMamSurv](papers/healthcare.md#chen2026graph) | Graph Mamba Survival Analysis Based on Topology-Aware ordering | Histopathology | WSI survival analysis | GS | 2026 | [arXiv](https://arxiv.org/abs/2606.02602) |
| [CGAM](papers/healthcare.md#qu2025cgam) | CGAM: An end-to-end causality graph attention Mamba network for esophageal pathology grading | Histopathology | Esophageal pathology grading | LG | 2025 | [🔎](https://scholar.google.com/scholar?q=%22CGAM%3A+An+end-to-end+causality+graph+attention+Mamba+network+for+esophageal+pathology+grading%22) |
| [GM-UNet](papers/healthcare.md#zhang2024gm) | GM-UNet: Graph Mamba UNet for Medical Image Segmentation | Medical imaging | Image segmentation | LG | 2024 | [🔎](https://scholar.google.com/scholar?q=%22GM-UNet%3A+Graph+Mamba+UNet+for+Medical+Image+Segmentation%22) |
| [GGVMamba](papers/healthcare.md#zhou2024efficient) | Efficient and Gender-Adaptive Graph Vision Mamba for Pediatric Bone Age Assessment | Medical imaging | Bone-age assessment | GS | 2024 | [🔎](https://scholar.google.com/scholar?q=%22Efficient+and+Gender-Adaptive+Graph+Vision+Mamba+for+Pediatric+Bone+Age+Assessment%22) |
| [HGM](papers/healthcare.md#zhu2025hybrid) | Hybrid graph mamba: Unlocking non-euclidean potential for accurate polyp segmentation | Medical imaging | Polyp segmentation | LG | 2025 | [🔎](https://scholar.google.com/scholar?q=%22Hybrid+graph+mamba%3A+Unlocking+non-euclidean+potential+for+accurate+polyp+segmentation%22) |
| [GMMN](papers/healthcare.md#zhang2026graph) | Graph mapping mamba network for automated macular edema diagnosis from fundus images | Medical imaging | Macular edema diagnosis | LG | 2026 | [🔎](https://scholar.google.com/scholar?q=%22Graph+mapping+mamba+network+for+automated+macular+edema+diagnosis+from+fundus+images%22) |

➡ Full cards: [papers/healthcare.md](papers/healthcare.md)

</details>

<details>
<summary><b>Remote Sensing and Structured Visual Applications</b> · Sec. 5.2 · 7 works</summary>

| Model | Paper | Data setting | Task | Pattern | Year | Links |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| [GraphMamba (HSI)](papers/remote-sensing-visual.md#yang2024graphmamba) | GraphMamba: An efficient graph structure learning vision mamba for hyperspectral image classification | Remote sensing | Hyperspectral classification | DV | 2024 | [🔎](https://scholar.google.com/scholar?q=%22GraphMamba%3A+An+efficient+graph+structure+learning+vision+mamba+for+hyperspectral+image+classification%22) |
| [MGF-GCN](papers/remote-sensing-visual.md#zhao2025mgf)◆ | MGF-GCN: Multimodal interaction Mamba-aided graph convolutional fusion network for semantic segmentation of remote sensing images | Remote sensing | Multimodal remote-sensing segmentation | DV | 2025 | [🔎](https://scholar.google.com/scholar?q=%22MGF-GCN%3A+Multimodal+interaction+Mamba-aided+graph+convolutional+fusion+network+for+semantic+segmentation+of+remote+sensing+images%22) |
| [GraphMamba (tok.)](papers/remote-sensing-visual.md#ahmad2025graphmamba) | Graphmamba: Graph tokenization mamba for hyperspectral image classification | Remote sensing | Hyperspectral classification | GS | 2025 | [🔎](https://scholar.google.com/scholar?q=%22Graphmamba%3A+Graph+tokenization+mamba+for+hyperspectral+image+classification%22) |
| [TGMN](papers/remote-sensing-visual.md#chu2025tgmn) | TGMN: Two-stage graph convolutional mamba network for hyperspectral image classification | Remote sensing | Hyperspectral classification | LG | 2025 | [🔎](https://scholar.google.com/scholar?q=%22TGMN%3A+Two-stage+graph+convolutional+mamba+network+for+hyperspectral+image+classification%22) |
| [GM-HAD](papers/remote-sensing-visual.md#tang2026graph) | Graph Mamba for Fast Hyperspectral Anomaly Detection | Remote sensing | Hyperspectral anomaly detection | GS | 2026 | [🔎](https://scholar.google.com/scholar?q=%22Graph+Mamba+for+Fast+Hyperspectral+Anomaly+Detection%22) |
| [Hamba](papers/remote-sensing-visual.md#dong2024hamba) | Hamba: Single-view 3D Hand Reconstruction with Graph-guided Bi-Scanning Mamba | Articulated and human motion | 3D hand reconstruction | GS | 2024 | [🔎](https://scholar.google.com/scholar?q=%22Hamba%3A+Single-view+3D+Hand+Reconstruction+with+Graph-guided+Bi-Scanning+Mamba%22) |
| [Tang et al.](papers/remote-sensing-visual.md#tang2025spatial) | Spatial-temporal graph mamba for music-guided dance video synthesis | Articulated and human motion | Music-guided dance synthesis | RT+GS | 2025 | [🔎](https://scholar.google.com/scholar?q=%22Spatial-temporal+graph+mamba+for+music-guided+dance+video+synthesis%22) |

➡ Full cards: [papers/remote-sensing-visual.md](papers/remote-sensing-visual.md)

</details>

<details>
<summary><b>Other Application Areas</b> · Sec. 5.3 · 4 works</summary>

| Model | Paper | Data setting | Task | Pattern | Year | Links |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| [SAMBA](papers/other-applications.md#mehrabian2024mamba) | Mamba meets financial markets: A graph-mamba approach for stock price prediction | Financial forecasting | Stock-return forecasting | RT | 2025 | [🔎](https://scholar.google.com/scholar?q=%22Mamba+meets+financial+markets%3A+A+graph-mamba+approach+for+stock+price+prediction%22) |
| [Ren et al.](papers/other-applications.md#ren2026spatio) | Spatio-temporal hypergraph-driven evolutionary graph-mamba method for remaining useful life prediction | Industrial prognostics | Aero-engine remaining useful life (RUL) prediction | RT | 2026 | [🔎](https://scholar.google.com/scholar?q=%22Spatio-temporal+hypergraph-driven+evolutionary+graph-mamba+method+for+remaining+useful+life+prediction%22) |
| [IDS–GraphMamba](papers/other-applications.md#atitallah2025ids) | IDS–GraphMamba: A Markov-Enhanced Graph Mamba Framework for Real-Time Intrusion Detection in IoMT Edge Networks | Cybersecurity and intrusion detection | IoMT intrusion detection | RT | 2025 | [🔎](https://scholar.google.com/scholar?q=%22IDS%E2%80%93GraphMamba%3A+A+Markov-Enhanced+Graph+Mamba+Framework+for+Real-Time+Intrusion+Detection+in+IoMT+Edge+Networks%22) |
| [MambaForGCN](papers/other-applications.md#lawan2024mambaforgcn) | Enhancing long-range dependency with state space model and Kolmogorov-Arnold networks for aspect-based sentiment analysis | Language and semantic modeling | Aspect-based sentiment analysis | DV | 2025 | [🔎](https://scholar.google.com/scholar?q=%22Enhancing+long-range+dependency+with+state+space+model+and+Kolmogorov-Arnold+networks+for+aspect-based+sentiment+analysis%22) |

➡ Full cards: [papers/other-applications.md](papers/other-applications.md)

</details>

<details>
<summary><b>Graph Mamba Models Discussed in the Research Agenda</b> · Sec. 7 · 4 works</summary>

| Model | Paper | Venue | Year | Discussed in | Links |
| :--- | :--- | :--- | :---: | :--- | :--- |
| [GSM++](papers/discussed-models.md#behrouz2024best) | Best of both worlds: Advantages of hybrid graph sequence models | arXiv preprint arXiv:2411.15671 | 2024 | 7.2, 7.6, 7.7 | [arXiv](https://arxiv.org/abs/2411.15671) |
| [MapsTSF](papers/discussed-models.md#wang2025mapstsf) | MapsTSF: efficient traffic prediction via hybrid Mamba 2-transformer spatiotemporal modeling and cross adaptive periodic sparse forecasting | The Journal of Supercomputing | 2025 | 7.6, 7.7 | [🔎](https://scholar.google.com/scholar?q=%22MapsTSF%3A+efficient+traffic+prediction+via+hybrid+Mamba+2-transformer+spatiotemporal+modeling+and+cross+adaptive+periodic+sparse+forecasting%22) |
| [Transfer-Mamba](papers/discussed-models.md#cheng2025transfer) | Transfer-Mamba: Selective state space models with spatio-temporal knowledge transfer for few-shot traffic prediction across cities | Simulation Modelling Practice and Theory | 2025 | 7.5, 7.7 | [🔎](https://scholar.google.com/scholar?q=%22Transfer-Mamba%3A+Selective+state+space+models+with+spatio-temporal+knowledge+transfer+for+few-shot+traffic+prediction+across+cities%22) |
| [M3-HGMA](papers/discussed-models.md#gubbala2026m3) | M3-HGMA: A Multi-modal, Multi-agent Hierarchical Graph-Mamba Architecture for Explainable and Adaptive Clinical Intelligence | International Conference on Frontiers in Advanced Computing and Emerging Intelligent Technologies | 2026 | 7.7 | [🔎](https://scholar.google.com/scholar?q=%22M3-HGMA%3A+A+Multi-modal%2C+Multi-agent+Hierarchical+Graph-Mamba+Architecture+for+Explainable+and+Adaptive+Clinical+Intelligence%22) |

➡ Full cards: [papers/discussed-models.md](papers/discussed-models.md)

</details>
<!-- END:CATALOGUE -->

---

## Comparison tables

All tables are generated from the database — never edited by hand — and exist in three synchronized formats. LaTeX tables keep the manuscript's BibTeX keys (`\cite{...}`) and can be `\input` directly. See [tables/README.md](tables/README.md).

<!-- BEGIN:TABLES -->
| # | Table | Formats |
| :--- | :--- | :--- |
| 1 | [T1 · Taxonomy dimensions](tables/markdown/taxonomy_dimensions.md) | [Markdown](tables/markdown/taxonomy_dimensions.md) · [LaTeX](tables/latex/taxonomy_dimensions.tex) · [CSV](tables/csv/taxonomy_dimensions.csv) |
| 2 | [T2 · Unified D1–D4 taxonomy of Graph Mamba architectures](tables/markdown/unified_taxonomy.md) | [Markdown](tables/markdown/unified_taxonomy.md) · [LaTeX](tables/latex/unified_taxonomy.tex) · [CSV](tables/csv/unified_taxonomy.csv) |
| 3 | [T3 · Structural and computational trade-offs per dimension](tables/markdown/structural_tradeoffs.md) | [Markdown](tables/markdown/structural_tradeoffs.md) · [LaTeX](tables/latex/structural_tradeoffs.tex) · [CSV](tables/csv/structural_tradeoffs.csv) |
| 4 | [T4 · Cross-domain applications and graph–SSM design patterns](tables/markdown/cross_domain_applications.md) | [Markdown](tables/markdown/cross_domain_applications.md) · [LaTeX](tables/latex/cross_domain_applications.tex) · [CSV](tables/csv/cross_domain_applications.csv) |
| 5 | [T5 · Distribution of dominant design patterns across application settings (derived)](tables/markdown/pattern_distribution.md) | [Markdown](tables/markdown/pattern_distribution.md) · [LaTeX](tables/latex/pattern_distribution.tex) · [CSV](tables/csv/pattern_distribution.csv) |
| 6 | [T6 · Coupling depth × integration type (derived)](tables/markdown/coupling_integration.md) | [Markdown](tables/markdown/coupling_integration.md) · [LaTeX](tables/latex/coupling_integration.tex) · [CSV](tables/csv/coupling_integration.csv) |
| 7 | [T7 · Benchmarks used in the comparative analysis](tables/markdown/benchmark_summary.md) | [Markdown](tables/markdown/benchmark_summary.md) · [LaTeX](tables/latex/benchmark_summary.tex) · [CSV](tables/csv/benchmark_summary.csv) |
| 8 | [T8 · Reported complexity, efficiency, and scalability evidence](tables/markdown/efficiency_summary.md) | [Markdown](tables/markdown/efficiency_summary.md) · [LaTeX](tables/latex/efficiency_summary.tex) · [CSV](tables/csv/efficiency_summary.csv) |
| 9 | [T9 · Theoretical expressive-power results](tables/markdown/expressivity.md) | [Markdown](tables/markdown/expressivity.md) · [LaTeX](tables/latex/expressivity.tex) · [CSV](tables/csv/expressivity.csv) |
| 10 | [T10 · Open challenges and research directions](tables/markdown/future_directions.md) | [Markdown](tables/markdown/future_directions.md) · [LaTeX](tables/latex/future_directions.tex) · [CSV](tables/csv/future_directions.csv) |
| 11 | [T11 · Evidence coverage and reporting gaps (derived)](tables/markdown/evidence_coverage.md) | [Markdown](tables/markdown/evidence_coverage.md) · [LaTeX](tables/latex/evidence_coverage.tex) · [CSV](tables/csv/evidence_coverage.csv) |
| 12 | [T12 · Index of reviewed works](tables/markdown/paper_index.md) | [Markdown](tables/markdown/paper_index.md) · [LaTeX](tables/latex/paper_index.tex) · [CSV](tables/csv/paper_index.csv) |
| 13 | [Published results · Mean classification accuracy (%) on brain benchmarks](tables/markdown/perf_brain.md) | [Markdown](tables/markdown/perf_brain.md) · [LaTeX](tables/latex/perf_brain.tex) · [CSV](tables/csv/perf_brain.csv) |
| 14 | [Published results · Hyperspectral image classification](tables/markdown/perf_hsi.md) | [Markdown](tables/markdown/perf_hsi.md) · [LaTeX](tables/latex/perf_hsi.tex) · [CSV](tables/csv/perf_hsi.csv) |
| 15 | [Published results · Spatio-temporal forecasting benchmarks](tables/markdown/perf_spatiotemporal.md) | [Markdown](tables/markdown/perf_spatiotemporal.md) · [LaTeX](tables/latex/perf_spatiotemporal.tex) · [CSV](tables/csv/perf_spatiotemporal.csv) |
| 16 | [Published results · Financial forecasting (RMSE) and training time](tables/markdown/perf_financial.md) | [Markdown](tables/markdown/perf_financial.md) · [LaTeX](tables/latex/perf_financial.tex) · [CSV](tables/csv/perf_financial.csv) |
| 17 | [Published results · Aspect-based sentiment analysis](tables/markdown/perf_absa.md) | [Markdown](tables/markdown/perf_absa.md) · [LaTeX](tables/latex/perf_absa.tex) · [CSV](tables/csv/perf_absa.csv) |
<!-- END:TABLES -->

### Table conventions

* **NR** = not reported in the survey. Nothing is filled in from outside the manuscript.
* **Published results are never pooled across sources.** Each performance table reproduces one comparison from the survey's appendix (same source paper, datasets, and protocol). Bold marks the best value *within that table only*; ★ marks the Graph Mamba row. All numbers are as reported in the original publications and were not reproduced.
* **Evidence levels** follow §6.1: *comparable* published results vs. *contextual* results.
* **Derived tables** (T5, T6, T11) are computed from the database and are labelled as such; they are not manuscript tables.
* Terminology, abbreviations, and category labels are taken verbatim from the manuscript (`data/taxonomy.yaml`).

---

## Interactive explorer

`docs/index.html` is a self-contained literature explorer generated on every build: full-text search; filters by role, graph setting, application area, design pattern, and year; a clickable **coupling × integration** matrix of all architectures and a **data setting × pattern** matrix of all applications; per-paper detail panels; and CSV export of the current selection. It embeds the resolved database, so it also works offline.

**Publish it:** *Settings → Pages → Build and deployment → Deploy from a branch → `main` / `/docs`.* Then set `survey.repository` in `data/taxonomy.yaml` to your repository URL (used for links back to the catalogue) and replace `OWNER` in this README.

---

## Repository structure

```text
awesome-graph-mamba/
├── README.md                  ← this page (blocks between BEGIN/END markers are generated)
├── CITATION.cff · LICENSE · CONTRIBUTING.md · requirements.txt
├── source/
│   ├── main.tex               ← manuscript (primary scientific source)
│   └── references.bib         ← bibliography (bibliographic source of truth)
├── data/
│   ├── papers.yaml            ← curated paper database (edit this)
│   ├── taxonomy.yaml          ← dimensions, settings, domains, patterns, RQs
│   ├── benchmarks.yaml        ← benchmark groups (tab:benchmark-summary)
│   ├── results.yaml           ← published results (Appendix A)
│   ├── challenges.yaml        ← open challenges (tab:future-directions)
│   ├── schema.json            ← JSON schema for papers.yaml
│   └── generated/             ← papers.json · papers.csv · tex_extraction.json
├── papers/                    ← generated per-category catalogue pages
├── tables/{markdown,latex,csv}/ ← generated comparison tables
├── docs/index.html            ← generated interactive explorer (GitHub Pages)
├── docs/FLAGS.md              ← generated verification flags & data-quality report
├── scripts/                   ← extract · database · quality · tables · catalogue · build · validate
├── tests/                     ← pytest suite
└── .github/workflows/update.yml
```

**Single source of truth.** Survey-derived information lives once in `data/*.yaml`; bibliographic metadata (title, authors, venue, year, DOI/arXiv) lives once in `source/references.bib`. Every table, catalogue page, and README block is generated from these files.

---

## Reproduce the repository

```bash
pip install -r requirements.txt
python scripts/build.py        # parse sources, resolve database, regenerate tables + catalogue + README blocks
python scripts/validate.py     # schema, references, categories, manuscript consistency, stale outputs
pytest -q                      # unit and integration tests
```

| Command | Purpose |
| :--- | :--- |
| `python scripts/extract_papers.py` | Parse `main.tex`/`references.bib`; write `data/generated/tex_extraction.json` (citations per section, rows of the taxonomy and application tables, design-pattern figure). |
| `python scripts/extract_papers.py --merge` | Additionally append **stubs** for works classified in the manuscript but absent from `papers.yaml`. Existing records — and in particular `verified` ones — are never modified. |
| `python scripts/generate_site.py` | Rebuild only the explorer `docs/index.html`. |
| `python scripts/build.py --check` | Exit 1 if any generated file is out of date (used in CI). |
| `python scripts/validate.py --strict -v` | Fail on warnings too and print informational findings. |

**How regeneration works.** `build.py` loads `data/*.yaml` and the bibliography, resolves each record (adding bibliographic metadata and manuscript section numbers), runs the checks in `scripts/quality.py`, and renders every table and page from the same in-memory objects. Adding or editing a record in `data/papers.yaml` and re-running `build.py` updates every affected table, the catalogue page, the README statistics, and the Mermaid diagram. On GitHub, the workflow in `.github/workflows/update.yml` does this automatically.

### Data quality and verification

The initial database was extracted from the manuscript. Classifications are cross-checked automatically against `tab:unified-taxonomy`, `tab:cross-domain-applications`, and `fig:design-patterns`; any disagreement fails validation. Ambiguities found in the manuscript are recorded as flags rather than silently resolved.

<!-- BEGIN:FLAGS -->
Current status: **0 errors**, **7 warnings**, 53 informational notes — see [docs/FLAGS.md](docs/FLAGS.md).
<!-- END:FLAGS -->

---

## Contributing

New Graph Mamba papers, corrections, and links to official code are welcome. In short:

1. Add the BibTeX entry to `source/references.bib`.
2. Add a record to `data/papers.yaml` (template and field guide in [CONTRIBUTING.md](CONTRIBUTING.md)) using only categories defined in `data/taxonomy.yaml`.
3. Run `python scripts/build.py && python scripts/validate.py && pytest -q`.
4. Open a pull request. CI re-runs the pipeline and rejects stale or inconsistent outputs.

Papers not (yet) covered by the survey are welcome and are marked `extracted`/`needs_verification` until reviewed by the authors.

---

## Citation

If this survey or repository is useful in your research, please cite:

```bibtex
@article{benatitallah2026graphmamba,
  title   = {Exploring Graph Mamba: A Comprehensive Survey on State-Space Models for Graph Learning},
  author  = {Ben Atitallah, Safa and Ben Rabah, Chaima and Driss, Maha and Boulila, Wadii and Koubaa, Anis},
  journal = {ACM Computing Surveys},
  note    = {Under revision},
  year    = {2026}
}
```

> The entry will be updated with volume, pages, and DOI upon publication. Machine-readable metadata: [CITATION.cff](CITATION.cff).

## Acknowledgement

The authors gratefully acknowledge Prince Sultan University, Riyadh, Saudi Arabia, for its support of this research.

## License

Code is released under the [MIT License](LICENSE). Curated data in `data/` is released under CC BY 4.0. Bibliographic metadata and reported results belong to their respective authors and publishers.
