# Heterogeneous and Higher-Order Graph Models

*Survey section: Sec. 3.4. 4 work(s).* [← Catalogue index](README.md) · [← Repository home](../README.md)

> **Design emphasis in this setting:** Most structure is carried by tokenization.

**Contents**

- [HeteGraph-Mamba](#pan2024hetegraph) (2024)
- [Mamba-GTC](#meng2026mamba-gtc) (2025)
- [TopoMamba](#montagna2024topological) (2025)
- [CCMamba](#chen2026ccmamba) (2026)

<a id="pan2024hetegraph"></a>
### HeteGraph-Mamba
**HeteGraph-Mamba: Heterogeneous Graph Learning via Selective State Space Model**  
Zhenyu Pan, Yoonsung Jeong, Xiaoda Liu, Han Liu — *arXiv preprint arXiv:2405.13915*, 2024  
[arXiv](https://arxiv.org/abs/2405.13915) · Code: NR · BibTeX: `pan2024hetegraph` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Heterogeneous and Higher-Order Graph Models | Metapath-based heterogeneous graph tokens | Hierarchical within-type and across-type processing | Input-level | Standalone |

**Methodology.** Metapath-based instances form graph tokens per target node; node-type representations aligned in a common latent space; selective processing first within type, then across types.

**Key contributions (as characterized in the survey)**
- Heterogeneous semantics through token construction (D1) and hierarchical type-aware ordering (D2).

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Cited as early work for challenges:** `complex_graphs`

**Discussed in:** 3.4 Heterogeneous and Higher-Order Graph Models; 7.3 Dynamic, Heterogeneous, and Higher-Order Graphs; 7.7 Future Research Directions

</details>

---

<a id="meng2026mamba-gtc"></a>
### Mamba-GTC
**Mamba-GTC: Cross-view contrastive learning with state space modeling for heterogeneous graph representation**  
Fanchao Meng, Shuo Zhao, Zhongwen Guo, Yujun Lan, Bo Pang — *Knowledge-Based Systems*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Mamba-GTC%3A+Cross-view+contrastive+learning+with+state+space+modeling+for+heterogeneous+graph+representation%22)) · Code: NR · BibTeX: `Meng2026Mamba-GTC` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Heterogeneous and Higher-Order Graph Models | Multi-hop neighborhood tokens | Hop-evolution ordering | Input-level | Parallel |

**Methodology.** Enhanced Hop2Token converts multi-hop neighborhoods into hop-evolution sequences ordered by distance; a GNN branch (local, unordered topology) and a Mamba branch (ordered hop sequence) are aligned by a cross-view contrastive objective.

**Key contributions (as characterized in the survey)**
- Hop-structured tokenization and ordering (D1–D2) with explicit GNN–Mamba integration (D4).

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- Self-supervision used within a single dataset; no reusable encoder.

**Cited as early work for challenges:** `pretraining`

**Discussed in:** 3.4 Heterogeneous and Higher-Order Graph Models; 7.5 Pre-training, Transfer, and Graph Foundation Models; 7.7 Future Research Directions

</details>

---

<a id="montagna2024topological"></a>
### TopoMamba
**Topological deep learning with state-space models: A mamba approach for simplicial complexes**  
Marco Montagna, Simone Scardapane, Lev Telyatnikov — *2025 International Joint Conference on Neural Networks (IJCNN)*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Topological+deep+learning+with+state-space+models%3A+A+mamba+approach+for+simplicial+complexes%22)) · Code: NR · BibTeX: `montagna2024topological` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Heterogeneous and Higher-Order Graph Models | Incident simplices aggregated by rank | Rank-ordered sequence | Input-level | Standalone |

**Methodology.** Extends state-space processing to simplicial complexes: incident simplices of each target node are grouped and aggregated by rank, and the rank-level sequence is processed by Mamba.

**Key contributions (as characterized in the survey)**
- Higher-order token construction (D1) and rank-based serialization (D2) without a dedicated higher-order message-passing rule.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Cited as early work for challenges:** `complex_graphs`

**Discussed in:** 3.4 Heterogeneous and Higher-Order Graph Models; 7.3 Dynamic, Heterogeneous, and Higher-Order Graphs; 7.7 Future Research Directions

</details>

---

<a id="chen2026ccmamba"></a>
### CCMamba
**CCMamba: Topologically-Informed Selective State-Space Networks on Combinatorial Complexes for Higher-Order Graph Learning**  
Jiawen Chen, Qi Shao, Mingtong Zhou, Duxin Chen, Wenwu Yu — *arXiv preprint arXiv:2601.20518*, 2026  
[arXiv](https://arxiv.org/abs/2601.20518) · Code: NR · BibTeX: `chen2026ccmamba` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Heterogeneous and Higher-Order Graph Models | Multi-rank incidence representations | Rank- and incidence-aware linearization | Input-level | Standalone |

**Methodology.** Organizes multi-rank incidence relationships of combinatorial complexes into rank-aware sequences processed by selective SSMs, reformulating higher-order message propagation as sequential state-space processing.

**Key contributions (as characterized in the survey)**
- Rank-aware representation construction (D1) and incidence-aware linearization (D2).

- **Expressive power:** Upper-bounded by the 1-dimensional combinatorial-complex WL (1-CCWL) test *(permutation: Rank-aware sequences over incidence neighborhoods; caveat: An upper bound only: the selective SSM does not exceed higher-order message passing)*
- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Cited as early work for challenges:** `expressivity`, `complex_graphs`

**Discussed in:** 3.4 Heterogeneous and Higher-Order Graph Models; 7.2 Expressive Power and Theoretical Understanding; 7.3 Dynamic, Heterogeneous, and Higher-Order Graphs; 7.7 Future Research Directions

</details>

---

<sub>Generated by `scripts/generate_catalogue.py` from `data/papers.yaml` and `source/references.bib`. Do not edit by hand.</sub>
