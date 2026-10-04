# Graph Mamba Models Discussed in the Research Agenda

*Survey section: Sec. 7. 4 work(s).* [← Catalogue index](README.md) · [← Repository home](../README.md)

> These Graph Mamba models are cited in Section 7 (challenges and research agenda) but are **not** classified in the survey taxonomy. No D1–D4 or design-pattern label is assigned.

**Contents**

- [GSM++](#behrouz2024best) (2024)
- [MapsTSF](#wang2025mapstsf) (2025)
- [Transfer-Mamba](#cheng2025transfer) (2025)
- [M3-HGMA](#gubbala2026m3) (2026)

<a id="behrouz2024best"></a>
### GSM++
*Also referred to as: Graph sequence models, Best of both worlds*  
**Best of both worlds: Advantages of hybrid graph sequence models**  
Ali Behrouz, Ali Parviz, Mahdi Karami, Clayton Sanford, Bryan Perozzi, Vahab Mirrokni — *arXiv preprint arXiv:2411.15671*, 2024  
[arXiv](https://arxiv.org/abs/2411.15671) · Code: NR · BibTeX: `behrouz2024best` `⚠ needs verification`

**Methodology.** Applies Mamba layers followed by a Transformer block to hierarchically tokenized graphs; accompanying task-based analysis of graph sequence models.

**Key contributions (as characterized in the survey)**
- Reports improvements over both pure backbones on most of its benchmarks (hybrid attention–SSM).
- Comparison of sequence backbones including Mamba and Mamba-2 within one graph pipeline found none uniformly best.

- **Expressive power:** Task-based analysis beyond WL: recurrent backbones can count node colors when the state width is at least the number of colors, which non-causal Transformers without PE cannot; worst-case connectivity favors Transformers (logarithmic depth), whereas recurrent models need polynomial depth or width unless the ordering is locality-preserving *(permutation: Depends on tokenizer and backbone; caveat: Sensitivity of SSM outputs decays with token distance and deep stacks exhibit representational collapse; no single backbone dominates)*
- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Cited as early work for challenges:** `expressivity`, `hybrid`

**Discussed in:** 7.2 Expressive Power and Theoretical Understanding; 7.6 Hybrid Attention–SSM Designs and Mamba-2/SSD Backbones; 7.7 Future Research Directions

</details>

> [!WARNING]
> Not classified in tab:unified-taxonomy; D1–D4 left unassigned.

---

<a id="wang2025mapstsf"></a>
### MapsTSF
**MapsTSF: efficient traffic prediction via hybrid Mamba 2-transformer spatiotemporal modeling and cross adaptive periodic sparse forecasting**  
Bing Wang, Chaoqi Cai, Xingpeng Zhang, Chunlan Zhao, Chi Zhang, Youming Zhang — *The Journal of Supercomputing*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22MapsTSF%3A+efficient+traffic+prediction+via+hybrid+Mamba+2-transformer+spatiotemporal+modeling+and+cross+adaptive+periodic+sparse+forecasting%22)) · Code: NR · BibTeX: `wang2025mapstsf` `⚠ needs verification`

**Methodology.** Couples a Mamba-2 backbone with Transformer attention over road-network traversals.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Cited as early work for challenges:** `hybrid`

**Discussed in:** 7.6 Hybrid Attention–SSM Designs and Mamba-2/SSD Backbones; 7.7 Future Research Directions

</details>

> [!WARNING]
> Not classified in tab:unified-taxonomy; D1–D4 left unassigned.

---

<a id="cheng2025transfer"></a>
### Transfer-Mamba
**Transfer-Mamba: Selective state space models with spatio-temporal knowledge transfer for few-shot traffic prediction across cities**  
Shaokang Cheng, Shiru Qu, Junxi Zhang — *Simulation Modelling Practice and Theory*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Transfer-Mamba%3A+Selective+state+space+models+with+spatio-temporal+knowledge+transfer+for+few-shot+traffic+prediction+across+cities%22)) · Code: NR · BibTeX: `cheng2025transfer` `⚠ needs verification`

**Methodology.** Pre-trains a Mamba and adaptive-GCN encoder by masked reconstruction on traffic data from several source cities and transfers it to a data-scarce target city.

**Key contributions (as characterized in the survey)**
- Domain-specific exception to single-dataset self-supervision in Graph Mamba (cross-city transfer).

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Cited as early work for challenges:** `pretraining`

**Discussed in:** 7.5 Pre-training, Transfer, and Graph Foundation Models; 7.7 Future Research Directions

</details>

> [!WARNING]
> Not classified in tab:unified-taxonomy; D1–D4 left unassigned.

---

<a id="gubbala2026m3"></a>
### M3-HGMA
**M3-HGMA: A Multi-modal, Multi-agent Hierarchical Graph-Mamba Architecture for Explainable and Adaptive Clinical Intelligence**  
Somasekhar Gubbala — *International Conference on Frontiers in Advanced Computing and Emerging Intelligent Technologies*, 2026  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22M3-HGMA%3A+A+Multi-modal%2C+Multi-agent+Hierarchical+Graph-Mamba+Architecture+for+Explainable+and+Adaptive+Clinical+Intelligence%22)) · Code: NR · BibTeX: `gubbala2026m3` `⚠ needs verification`

**Methodology.** NR (cited only as early work for cross-modal graph modeling in tab:future-directions).

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Cited as early work for challenges:** `crossmodal`

**Discussed in:** 7.7 Future Research Directions

</details>

> [!WARNING]
> Only cited in tab:future-directions; the survey gives no architectural description.

---

<sub>Generated by `scripts/generate_catalogue.py` from `data/papers.yaml` and `source/references.bib`. Do not edit by hand.</sub>
