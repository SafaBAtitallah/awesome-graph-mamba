# Static and General-Purpose Graph Models

*Survey section: Sec. 3.2. 7 work(s).* [← Catalogue index](README.md) · [← Repository home](../README.md)

> **Design emphasis in this setting:** Ordering is decisive because nodes have no natural sequence.

**Contents**

- [GSSC](#huang2024can) (2024)
- [GMN](#behrouz2024graph) (2024)
- [Graph-Mamba](#wang2024graph) (2024)
- [GrassNet](#zhao2024grassnet) (2026)
- [MbaGCN](#he2025mamba) (2025)
- [DMbaGCN](#he2026dual) (2026)
- [GLADMamba](#fu2025gladmamba) (2025)

<a id="huang2024can"></a>
### GSSC
**What Can We Learn from State Space Models for Machine Learning on Graphs?**  
Yinan Huang, Siqi Miao, Pan Li — *arXiv preprint arXiv:2406.05815*, 2024  
[arXiv](https://arxiv.org/abs/2406.05815) · Code: NR · BibTeX: `huang2024can` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Static and General-Purpose Graph Models | Node features and graph positional information | Order-free | Operator-level | Standalone |

**Methodology.** Extends state-space convolution to graphs with global permutation-equivariant set aggregation and factorizable graph kernels built from structural and relative positional information; avoids explicit graph-to-sequence serialization.

**Key contributions (as characterized in the survey)**
- Operator-level incorporation of graph structure into the state-space convolution rather than through a node ordering.
- Permutation equivariance identified as a property of the operator (architectural guarantee).
- Proof that a graph-kernel parameterization exists for which the gradient between two node representations does not decay with shortest-path distance.

- **Reported complexity:** $O(nmd)$ for the graph state-space convolution ($n$ nodes; $m$ hidden and $d$ positional-encoding dimensions)
- **Efficiency:** Linear-time structured state-space propagation; extra costs: Graph-kernel and positional/spectral preprocessing; evidence: Reports graph-size-dependent linear propagation complexity; preprocessing evaluated separately (Laplacian PE eigendecomposition can be non-negligible; only required eigenpairs computed iteratively for larger graphs)
- **Expressive power:** Strictly more powerful than 1-WL and not more powerful than 3-WL; counts 3-paths and 3-cycles, and 4-paths and 4-cycles when the selection mechanism is added *(permutation: Equivariant by construction; caveat: Not a serialization-based model; relies on a factorizable distance kernel built from PE)*
- **Benchmarks in the survey:** Peptides-func, Peptides-struct (AP, MAE)

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- Permutation equivariant and long-range without node serialization (order sensitivity S(G)=0 by construction).

**Limitations (stated in the survey)**
- Laplacian positional-encoding eigendecomposition can become a non-negligible preprocessing cost.

**Notes**
- Cited as early work for end-to-end scalability, serialization/permutation, and expressive power (tab:future-directions).

**Cited as early work for challenges:** `scalability`, `serialization`, `expressivity`

**Discussed in:** 3.2 Static and General-Purpose Graph Models; 4.1 Node Relabeling and Ordering Sensitivity; 4.2 Long-Range Dependency Modeling and State Retention; 4.3 Computational Complexity and Scalability; 6.4 Efficiency and Scalability; 7.2 Expressive Power and Theoretical Understanding; 7.7 Future Research Directions

</details>

---

<a id="behrouz2024graph"></a>
### GMN
*Also referred to as: Graph Mamba Network*  
**Graph mamba: Towards learning on graphs with state space models**  
Ali Behrouz, Farnoosh Hashemi — *Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*, 2024  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Graph+mamba%3A+Towards+learning+on+graphs+with+state+space+models%22)) · Code: NR · BibTeX: `behrouz2024graph` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Static and General-Purpose Graph Models | Neighborhood/subgraph tokens | Ordered, bidirectional | Input-level | Parallel |

**Methodology.** Framework of neighborhood tokenization, token ordering, local encoding, and a bidirectional selective SSM encoder; sampled neighborhood structures become graph tokens; optional message-passing module adds local inductive bias.

**Key contributions (as characterized in the survey)**
- Graph structure introduced primarily through token construction (D1) and ordering with bidirectional scanning (D2).
- Complexity analysis that explicitly includes token construction.

- **Reported complexity:** $O(Ms(m+1)\lvert V\rvert + \lvert E\rvert)$ in the subgraph-token setting ($M$, $s$, $m$ control sampling and token construction); linear in $\lvert V\rvert$ with node tokens; $O(\lvert V\rvert + \lvert E\rvert)$ with the optional message-passing component
- **Efficiency:** Linear in processed graph-token sequence length; extra costs: Neighborhood sampling and optional message passing; evidence: Complexity depends on sampling parameters and graph size
- **Expressive power:** Universal approximator of permutation-equivariant functions given PE; with suitable PE/SE more expressive than any WL test, matching graph Transformers; unbounded power without PE/SE when a random-walk neighborhood encoder is used *(permutation: Not guaranteed (ordered tokens, bidirectional scan); caveat: Part of the power is attributed by the authors to neighborhood sampling and encoding rather than to the selective SSM)*
- **Benchmarks in the survey:** Peptides-func, Peptides-struct (AP, MAE)

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- Bidirectional processing removes the privileged causal direction of a single forward scan.

**Limitations (stated in the survey)**
- Computation still operates on a particular token sequence (no permutation guarantee).
- Improvements cannot be attributed to the SSM independently of the tokenization procedure.
- Explicit trade-off between richer/longer token sequences and computational cost.

**Cited as early work for challenges:** `serialization`, `expressivity`

**Discussed in:** 3.2 Static and General-Purpose Graph Models; 4.1 Node Relabeling and Ordering Sensitivity; 4.2 Long-Range Dependency Modeling and State Retention; 4.3 Computational Complexity and Scalability; 6.4 Efficiency and Scalability; 7.1 Serialization, Permutation, and Robustness; 7.2 Expressive Power and Theoretical Understanding; 7.7 Future Research Directions

</details>

---

<a id="wang2024graph"></a>
### Graph-Mamba
**Graph-mamba: Towards long-range graph sequence modeling with selective state spaces**  
Chloe Wang, Oleksii Tsepa, Jun Ma, Bo Wang — *arXiv preprint arXiv:2402.00789*, 2024  
[arXiv](https://arxiv.org/abs/2402.00789) · Code: NR · BibTeX: `wang2024graph` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Static and General-Purpose Graph Models | Node representations | Degree-based prioritization and permutation | Input-level | Parallel |

**Methodology.** Graph-centric node prioritization (degree by default; ties randomly permuted during training) followed by a Graph-Mamba Block that replaces the global attention of GraphGPS, with an MPNN branch for local processing; multiple permuted outputs averaged at inference.

**Key contributions (as characterized in the survey)**
- Serialization and scanning (D2) with local–global graph–SSM integration (D4).
- Ablation showing node-level permutation with degree-based prioritization outperforms the alternatives evaluated.

- **Reported complexity:** $O(L)$ for the Graph-Mamba Block with respect to input sequence length $L$ (hardware-aware Mamba implementation)
- **Efficiency:** Linear Mamba global block; extra costs: Node prioritization, permutation, sequence construction; evidence: Reports reduced GPU memory usage on large-graph experiments (up to 74%); binning strategy splits long node sequences for larger graphs
- **Benchmarks in the survey:** Peptides-func, Peptides-struct (AP, MAE)

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- Permutation-based training reduces sequence-related bias and improves stability (empirical strategy).

**Limitations (stated in the survey)**
- Empirical, not architectural, mitigation of order dependence.
- Practical cost includes binning, prioritization, and permutation beyond the selective scan.

**Cited as early work for challenges:** `serialization`

**Discussed in:** 3.2 Static and General-Purpose Graph Models; 4.1 Node Relabeling and Ordering Sensitivity; 4.2 Long-Range Dependency Modeling and State Retention; 4.3 Computational Complexity and Scalability; 6.4 Efficiency and Scalability; 7.1 Serialization, Permutation, and Robustness; 7.7 Future Research Directions

</details>

---

<a id="zhao2024grassnet"></a>
### GrassNet
**Grassnet: State space model meets graph neural network**  
Gongpei Zhao, Tao Wang, Yi Jin, Congyan Lang, Yidong Li, Haibin Ling — *Pattern Recognition*, 2026  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Grassnet%3A+State+space+model+meets+graph+neural+network%22)) · Code: NR · BibTeX: `zhao2024grassnet` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Static and General-Purpose Graph Models | Graph spectrum embeddings | Frequency-ordered, bidirectional | Operator-level | Standalone |

**Methodology.** Spectral decomposition of the graph; spectrum embeddings ordered by graph frequency and scanned in both directions by an SSM graph filter.

**Key contributions (as characterized in the survey)**
- Spectral representation (D1), frequency-based bidirectional scanning (D2), and SSM-based spectral filtering (D3).

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Cited as early work for challenges:** `serialization`

**Discussed in:** 3.2 Static and General-Purpose Graph Models; 7.1 Serialization, Permutation, and Robustness; 7.7 Future Research Directions

</details>

---

<a id="he2025mamba"></a>
### MbaGCN
**Mamba-Based Graph Convolutional Networks: Tackling Over-Smoothing with Selective State Space**  
Xin He, Yili Wang, Wenqi Fan, Xu Shen, Xin Juan, Rui Miao, Xin Wang — *Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI)*, 2025  
[DOI](https://doi.org/10.24963/ijcai.2025/595) · Code: NR · BibTeX: `he2025mamba` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Static and General-Purpose Graph Models | Neighborhood representations across layers | No explicit node serialization | Dynamics-level | Embedded |

**Methodology.** Integrates the Mamba paradigm into graph convolution through a Message Aggregation Layer (MAL), a Selective State Space Transition Layer (S3TL), and a Node State Prediction Layer (NSPL).

**Key contributions (as characterized in the survey)**
- Couples selective state evolution (D3) with graph message propagation (D4) instead of serializing nodes.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 3.2 Static and General-Purpose Graph Models

</details>

---

<a id="he2026dual"></a>
### DMbaGCN
**Dual Mamba for Node-Specific Representation Learning: Tackling Over-Smoothing with Selective State Space Modeling**  
Xin He, Yili Wang, Yiwei Dai, Xin Wang — *Proceedings of the AAAI Conference on Artificial Intelligence*, 2026  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Dual+Mamba+for+Node-Specific+Representation+Learning%3A+Tackling+Over-Smoothing+with+Selective+State+Space+Modeling%22)) · Code: NR · BibTeX: `he2026dual` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Static and General-Purpose Graph Models | Layer-wise node states and node sequence | Bidirectional global scan | Dynamics-level | Parallel, Embedded |

**Methodology.** Local State-Evolution Mamba (LSEMba) models layer-wise evolution of node states after stacked graph convolution; Global Context-Aware Mamba (GCAMba) applies bidirectional Mamba to a node sequence; both representations combined.

**Key contributions (as characterized in the survey)**
- Combines local state evolution with global contextual modeling.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 3.2 Static and General-Purpose Graph Models

</details>

---

<a id="fu2025gladmamba"></a>
### GLADMamba
**GLADMamba: Unsupervised Graph-Level Anomaly Detection Powered by Selective State Space Model**  
Yali Fu, Jindong Li, Qi Wang, Qianli Xing — *Joint European Conference on Machine Learning and Knowledge Discovery in Databases*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22GLADMamba%3A+Unsupervised+Graph-Level+Anomaly+Detection+Powered+by+Selective+State+Space+Model%22)) · Code: NR · BibTeX: `fu2025gladmamba` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Static and General-Purpose Graph Models | Multi-view graph representations | No central graph serialization | Dynamics-level | Parallel |

**Methodology.** Unsupervised graph-level anomaly detection with a View-Fused Mamba (VFM) and a Spectrum-Guided Mamba (SGM) that parameterizes B, C, and Δ from Rayleigh-quotient spectral information.

**Key contributions (as characterized in the survey)**
- Multi-view graph representation (D1), direct spectrum-guided state-space conditioning (D3), and multi-view fusion (D4).

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- Self-supervised objective does not produce an encoder reused on other graphs (sec:ch-pretraining).

**Cited as early work for challenges:** `pretraining`

**Discussed in:** 3.2 Static and General-Purpose Graph Models; 7.5 Pre-training, Transfer, and Graph Foundation Models; 7.7 Future Research Directions

</details>

---

<sub>Generated by `scripts/generate_catalogue.py` from `data/papers.yaml` and `source/references.bib`. Do not edit by hand.</sub>
