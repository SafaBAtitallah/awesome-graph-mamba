# Dynamic and Spatio-Temporal Graph Models

*Survey section: Sec. 3.3. 10 work(s).* [← Catalogue index](README.md) · [← Repository home](../README.md)

> **Design emphasis in this setting:** Time largely answers the ordering question, so design effort shifts to coupling.

**Contents**

- [GraphSSM](#li2024state) (2024)
- [GSSM](#zhou2024graph) (2024)
- [DG-Mamba](#yuan2025dg) (2025)
- [DyGMamba](#ding2024dygmamba) (2024)
- [DyG-Mamba](#li2024dyg) (2026)
- [STG-Mamba](#li2024stg) (2024)
- [SpoT-Mamba](#choi2024spot) (2024)
- [PS-Mamba](#dong2025ps) (2025)
- [FuzzMamba](#chen2026modeling) (2026)
- [STMAGRN](#zhang2025spatio) (2025)

<a id="li2024state"></a>
### GraphSSM
**State space models on temporal graphs: A first-principles study**  
Jintang Li, Ruofan Wu, Xinzhou Jin, Boqun Ma, Liang Chen, Zibin Zheng — *Advances in Neural Information Processing Systems*, 2024  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22State+space+models+on+temporal+graphs%3A+A+first-principles+study%22)) · Code: NR · BibTeX: `li2024state` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Dynamic and Spatio-Temporal Graph Models | Sequence of graph snapshots | Temporal snapshot order | Operator-level | Standalone |

**Methodology.** State-space formulation for discrete-time temporal graphs; GHIPPO incorporates structure through Laplacian regularization and a mixed discretization accounts for changes between snapshots.

**Key contributions (as characterized in the survey)**
- Integrates evolving topology directly into state evolution rather than reducing the graph to an arbitrary node sequence.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Cited as early work for challenges:** `scalability`, `complex_graphs`

**Discussed in:** 3.3 Dynamic and Spatio-Temporal Graph Models; 7.3 Dynamic, Heterogeneous, and Higher-Order Graphs; 7.7 Future Research Directions

</details>

---

<a id="zhou2024graph"></a>
### GSSM
**Graph Convolution Network Based State Space Model for Wireless Traffic Prediction**  
Hao Zhou, Dunyuan Yao, Binbin Chen, Ke Yu, Xiaofei Wu — *2024 IEEE Wireless Communications and Networking Conference (WCNC)*, 2024  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Graph+Convolution+Network+Based+State+Space+Model+for+Wireless+Traffic+Prediction%22)) · Code: NR · BibTeX: `zhou2024graph` `† precursor` `⚠ needs verification`

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Dynamic and Spatio-Temporal Graph Models | Base-station node time series | Temporal order | Dynamics-level | Sequential |

**Methodology.** Graph convolution over fixed and adaptive base-station graphs estimates the parameters of an SSM for wireless traffic prediction.

**Key contributions (as characterized in the survey)**
- Shows how spatial graph information can parameterize temporal state-space modeling.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Notes**
- Predates Mamba's input-dependent selection; described as a graph–SSM precursor.

**Discussed in:** 3.3 Dynamic and Spatio-Temporal Graph Models

</details>

> [!WARNING]
> Precursor status stated in the text of subsec:dynamic-models but not marked with a dagger in tab:unified-taxonomy (the dagger convention is only used in tab:cross-domain-applications).

---

<a id="yuan2025dg"></a>
### DG-Mamba
**Dg-mamba: Robust and efficient dynamic graph structure learning with selective state space models**  
Haonan Yuan, Qingyun Sun, Zhaonan Wang, Xingcheng Fu, Cheng Ji, Yongjian Wang, Bo Jin, Jianxin Li — *Proceedings of the AAAI Conference on Artificial Intelligence*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Dg-mamba%3A+Robust+and+efficient+dynamic+graph+structure+learning+with+selective+state+space+models%22)) · Code: NR · BibTeX: `yuan2025dg` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Dynamic and Spatio-Temporal Graph Models | Successive dynamic graph states | Selective scan across graph snapshots | Dynamics-level | Parallel |

**Methodology.** Dynamic message passing combined with selective state-space modeling across successive graph states; structural information enters the discretization; a self-supervised information objective regularizes the learned structure.

**Key contributions (as characterized in the survey)**
- Temporal graph representations (D1), temporal state-space processing (D2), structure-aware selective dynamics (D3), and dynamic graph propagation (D4).
- Explicitly evaluates structural and feature perturbations and evasion/poisoning attacks.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- Robustness evaluation does not isolate the robustness of the selective SSM itself.
- Self-supervision used within a single dataset; no reusable encoder.

**Cited as early work for challenges:** `robustness`, `pretraining`

**Discussed in:** 3.3 Dynamic and Spatio-Temporal Graph Models; 7.1 Serialization, Permutation, and Robustness; 7.3 Dynamic, Heterogeneous, and Higher-Order Graphs; 7.5 Pre-training, Transfer, and Graph Foundation Models; 7.7 Future Research Directions

</details>

---

<a id="ding2024dygmamba"></a>
### DyGMamba
**DyGMamba: Efficiently Modeling Long-Term Temporal Dependency on Continuous-Time Dynamic Graphs with State Space Models**  
Zifeng Ding, Yifeng Li, Yuan He, Antonio Norelli, Jingcheng Wu, Volker Tresp, Yunpu Ma, Michael Bronstein — *arXiv preprint arXiv:2408.04713*, 2024  
[arXiv](https://arxiv.org/abs/2408.04713) · Code: NR · BibTeX: `ding2024dygmamba` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Dynamic and Spatio-Temporal Graph Models | Historical node interactions and temporal patterns | Chronological interaction order | Input-level | Standalone |

**Methodology.** Continuous-time dynamic graphs; a node-level Mamba SSM encodes long interaction histories and a time-level Mamba SSM models edge-specific temporal patterns used to select relevant history.

**Key contributions (as characterized in the survey)**
- Designed to exploit extensive historical interaction information.

- **Efficiency:** Scales to long temporal interaction histories; extra costs: Historical-neighbor retrieval and temporal sequence construction; evidence: Processes more than 8192 temporal neighbors on a 48 GB NVIDIA A40 GPU vs. up to 2048 for the compared DyGFormer configuration (specific to that paper's setup)
- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- Stronger performance when substantial long-term temporal information is available.

**Limitations (stated in the survey)**
- Limited historical context may reduce effectiveness.

**Cited as early work for challenges:** `complex_graphs`

**Discussed in:** 3.3 Dynamic and Spatio-Temporal Graph Models; 4.2 Long-Range Dependency Modeling and State Retention; 4.3 Computational Complexity and Scalability; 6.4 Efficiency and Scalability; 7.7 Future Research Directions

</details>

---

<a id="li2024dyg"></a>
### DyG-Mamba
**Dyg-mamba: Continuous state space modeling on dynamic graphs**  
Dongyuan Li, Shiyin Tan, Ying Zhang, Ming Jin, Shirui Pan, Manabu Okumura, Renhe Jiang — *Advances in Neural Information Processing Systems*, 2026  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Dyg-mamba%3A+Continuous+state+space+modeling+on+dynamic+graphs%22)) · Code: NR · BibTeX: `li2024dyg` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Dynamic and Spatio-Temporal Graph Models | Timestamped interaction sequences | Irregular chronological event order | Dynamics-level | Standalone |

**Methodology.** Timespan-informed continuous SSM in which elapsed time between events controls the step size (decay of history); input-dependent parameters retain useful history and suppress noisy events.

**Key contributions (as characterized in the survey)**
- Incorporates irregular timespans directly into the state transition.
- Spectral(-norm) constraints limit the influence of noisy historical interactions.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- Robustness mechanism does not isolate the robustness of the selective SSM itself.

**Cited as early work for challenges:** `robustness`

**Discussed in:** 3.3 Dynamic and Spatio-Temporal Graph Models; 7.1 Serialization, Permutation, and Robustness; 7.7 Future Research Directions

</details>

---

<a id="li2024stg"></a>
### STG-Mamba
**Stg-mamba: Spatial-temporal graph learning via selective state space model**  
Lincan Li, Hanchen Wang, Wenjie Zhang, Adelle Coster — *arXiv preprint arXiv:2403.12418*, 2024  
[arXiv](https://arxiv.org/abs/2403.12418) · Code: NR · BibTeX: `li2024stg` `⚠ needs verification`

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Dynamic and Spatio-Temporal Graph Models | Graph-aware node time-series representations | Temporal processing across multiple granularities | Dynamics-level | Parallel |

**Methodology.** Spatial–Temporal Selective State Space Module combined with Kalman Filtering Graph Neural Networks (KFGN) for spatial relationships.

**Key contributions (as characterized in the survey)**
- Structural conditioning (D3) and graph–SSM integration (D4).

- **Benchmarks in the survey:** PeMS04, HZMetro, KnowAir (RMSE, MAE, MAPE)
- **Published results:** [perf_spatiotemporal](../tables/markdown/perf_spatiotemporal.md)

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- Lowest RMSE and MAE among compared methods on PeMS04, HZMetro, and KnowAir (RMSE reductions of ~2.2%, 2.4%, 7.4% vs. STAEformer).

**Limitations (stated in the survey)**
- Slightly higher MAPE than STAEformer on PeMS04; no uncertainty estimates or component-level ablations, so the SSM contribution is not isolated.

**Discussed in:** 3.3 Dynamic and Spatio-Temporal Graph Models; 6.2 Benchmark Datasets and Tasks; 6.3 Performance Comparison; 7.3 Dynamic, Heterogeneous, and Higher-Order Graphs; A Detailed Performance Comparisons

</details>

> [!WARNING]
> Integration conflict: tab:unified-taxonomy marks D4 = Parallel, whereas sec:performance-comparison describes STG-Mamba as 'dynamics-level coupling and embedded integration'. The table value is stored; please confirm.

---

<a id="choi2024spot"></a>
### SpoT-Mamba
**SpoT-Mamba: Learning Long-Range Dependency on Spatio-Temporal Graphs with Selective State Spaces**  
Jinhyeok Choi, Heehyeon Kim, Minhyeong An, Joyce Jiyoung Whang — *arXiv preprint arXiv:2406.11244*, 2024  
[arXiv](https://arxiv.org/abs/2406.11244) · Code: NR · BibTeX: `choi2024spot` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Dynamic and Spatio-Temporal Graph Models | Graph-derived neighborhood sequences | BFS, DFS, random-walk, and temporal scanning | Input-level | Standalone |

**Methodology.** Constructs multiple spatial sequences per node via BFS, DFS, and random walks, processed by Mamba; temporal state-space processing captures long-range dependencies over time.

**Key contributions (as characterized in the survey)**
- Graph-derived token construction (D1) with multi-way spatial scanning and temporal ordering (D2).

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 3.3 Dynamic and Spatio-Temporal Graph Models; 7.1 Serialization, Permutation, and Robustness; 7.3 Dynamic, Heterogeneous, and Higher-Order Graphs

</details>

---

<a id="dong2025ps"></a>
### PS-Mamba
**PS-Mamba: Spatial-Temporal Graph Mamba for Pose Sequence Refinement**  
Haoye Dong, Gim Hee Lee — *2025 IEEE/CVF International Conference on Computer Vision (ICCV)*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22PS-Mamba%3A+Spatial-Temporal+Graph+Mamba+for+Pose+Sequence+Refinement%22)) · Code: NR · BibTeX: `dong2025ps` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Dynamic and Spatio-Temporal Graph Models | Human joints across pose sequences | Four graph-guided bidirectional spatial–temporal scans | Input-level | Parallel |

**Methodology.** Spatial–Temporal Graph State Space (ST-GSS) block with a graph branch (graph convolution, temporal convolution, dynamic graph-weight matrix) and a Spatial–Temporal SSM; Graph-guided Spatial–Temporal Scanning builds four bidirectional sequences.

**Key contributions (as characterized in the survey)**
- Graph-guided scanning (D2) with adaptive joint-interaction modeling and graph–SSM fusion (D4) for human pose sequence refinement.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 3.3 Dynamic and Spatio-Temporal Graph Models

</details>

---

<a id="chen2026modeling"></a>
### FuzzMamba
**Modeling Spatiotemporal Dynamic Shifts for Traffic Cognition: A Fuzzy-based Graph-Mamba Approach**  
Guojin Chen, Qingqin Liu, Jiyao An, Md Sohel Rana, Yuchen Huang, Zihang Yi — *2026 IEEE International Conference on Fuzzy Systems (FUZZ-IEEE)*, 2026  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Modeling+Spatiotemporal+Dynamic+Shifts+for+Traffic+Cognition%3A+A+Fuzzy-based+Graph-Mamba+Approach%22)) · Code: NR · BibTeX: `chen2026modeling` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Dynamic and Spatio-Temporal Graph Models | Node-centric spatial neighborhoods with contextual features | Adaptive spatial ordering varying over time | Dynamics-level | Standalone |

**Methodology.** Node-centric neighborhood orderings from node distances, dynamically adjusted by time-varying environmental information; fuzzy role representations and disturbance signals guide Mamba-based sequence modeling for traffic.

**Key contributions (as characterized in the survey)**
- Adaptive graph-derived serialization (D2) and dynamic contextual guidance of selective processing (D3).
- Fuzzy role memberships and rule-based reasoning expose how node behavior and environment influence predictions.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Cited as early work for challenges:** `interpretability`

**Discussed in:** 3.3 Dynamic and Spatio-Temporal Graph Models; 7.4 Interpretability and Explainability; 7.7 Future Research Directions

</details>

---

<a id="zhang2025spatio"></a>
### STMAGRN
**Spatio-temporal mamba dynamic graph convolutional recurrent network for traffic prediction**  
Xiaoyan Zhang, Yongqin Zhang, Xiangfu Meng — *IEEE Transactions on Artificial Intelligence*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Spatio-temporal+mamba+dynamic+graph+convolutional+recurrent+network+for+traffic+prediction%22)) · Code: NR · BibTeX: `zhang2025spatio` 

| Setting | D1 Tokenization | D2 Ordering | D3 Coupling | D4 Integration |
| :--- | :--- | :--- | :--- | :--- |
| Dynamic and Spatio-Temporal Graph Models | Traffic sequences and dynamic graph representations | Temporal sequence processing | Input-level | Sequential |

**Methodology.** Mamba encoder extracts spatio-temporal features; a Spatio-Temporal Memory (STM) module generates dynamic graph embeddings; a GCN-recurrent decoder produces traffic predictions.

**Key contributions (as characterized in the survey)**
- Sequential graph–SSM integration (D4) in which Mamba precedes dynamic graph construction and graph-based decoding.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 3.3 Dynamic and Spatio-Temporal Graph Models

</details>

---

<sub>Generated by `scripts/generate_catalogue.py` from `data/papers.yaml` and `source/references.bib`. Do not edit by hand.</sub>
