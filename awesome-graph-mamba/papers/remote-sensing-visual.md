# Remote Sensing and Structured Visual Applications

*Survey section: Sec. 5.2. 7 work(s).* [← Catalogue index](README.md) · [← Repository home](../README.md)

**Contents**

- *Remote sensing*: [GraphMamba (HSI)](#yang2024graphmamba), [MGF-GCN](#zhao2025mgf), [GraphMamba (tok.)](#ahmad2025graphmamba), [TGMN](#chu2025tgmn), [GM-HAD](#tang2026graph)
- *Articulated and human motion*: [Hamba](#dong2024hamba), [Tang et al.](#tang2025spatial)

## Remote sensing

<a id="yang2024graphmamba"></a>
### GraphMamba (HSI)
**GraphMamba: An efficient graph structure learning vision mamba for hyperspectral image classification**  
Aitao Yang, Min Li, Yao Ding, Leyuan Fang, Yaoming Cai, Yujie He — *IEEE Transactions on Geoscience and Remote Sensing*, 2024  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22GraphMamba%3A+An+efficient+graph+structure+learning+vision+mamba+for+hyperspectral+image+classification%22)) · Code: NR · BibTeX: `yang2024graphmamba` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Remote sensing | Hyperspectral classification | Spatial neighborhoods and spectral representations | Dual-view (DV) |

**Graph–SSM division of labor.** SpatialGCN captures local spatial relations; HyperMamba models global spectral dependencies.

**Methodology.** Assigns high-dimensional spectral representations to HyperMamba and spatial neighborhoods to SpatialGCN.

- **Benchmarks in the survey:** Indian Pines, Salinas, UH2013 (OA, AA, Kappa)
- **Published results:** [perf_hsi](../tables/markdown/perf_hsi.md)

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- Higher OA, AA, and Kappa than the compared recurrent, convolutional, and Transformer baselines on Indian Pines, Salinas, and UH2013 (as reported).

**Limitations (stated in the survey)**
- NR

**Notes**
- One of three unrelated models published as 'GraphMamba'; disambiguated as GraphMamba (HSI).

**Discussed in:** 5.2 Remote Sensing and Structured Visual Data; 6.2 Benchmark Datasets and Tasks; 6.3 Performance Comparison; A Detailed Performance Comparisons

</details>

---

<a id="zhao2025mgf"></a>
### MGF-GCN
**MGF-GCN: Multimodal interaction Mamba-aided graph convolutional fusion network for semantic segmentation of remote sensing images**  
Yanfeng Zhao, Linwei Qiu, Zhenjian Yang, Yadong Chen, Yunjie Zhang — *Information Fusion*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22MGF-GCN%3A+Multimodal+interaction+Mamba-aided+graph+convolutional+fusion+network+for+semantic+segmentation+of+remote+sensing+images%22)) · Code: NR · BibTeX: `zhao2025mgf` `◆ multimodal`

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Remote sensing | Multimodal remote-sensing segmentation | Height-aware multimodal graph | Dual-view (DV) |

**Graph–SSM division of labor.** Graph convolution captures spatial/elevation relations; Mamba models cross-modal interactions.

**Methodology.** Height-aware graph convolution with hierarchical cross-modal Mamba processing.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.2 Remote Sensing and Structured Visual Data

</details>

---

<a id="ahmad2025graphmamba"></a>
### GraphMamba (tok.)
**Graphmamba: Graph tokenization mamba for hyperspectral image classification**  
Muhammad Ahmad, Manuel Mazzara, Salvatore Distefano, Adil Mehmood Khan, Muhammad Hassaan Farooq Butt, Muhammad Usama, Danfeng Hong — *IEEE Transactions on Emerging Topics in Computing*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Graphmamba%3A+Graph+tokenization+mamba+for+hyperspectral+image+classification%22)) · Code: NR · BibTeX: `ahmad2025graphmamba` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Remote sensing | Hyperspectral classification | Graph-guided spectral–spatial tokens | Graph-guided sequence (GS) |

**Graph–SSM division of labor.** Graph constructs and prioritizes tokens; Mamba models their global dependencies.

**Methodology.** Uses graph structure to construct and prioritize spectral–spatial tokens before Mamba processing.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Notes**
- One of three unrelated models published as 'GraphMamba'; disambiguated as GraphMamba (tok.).

**Discussed in:** 5.2 Remote Sensing and Structured Visual Data

</details>

---

<a id="chu2025tgmn"></a>
### TGMN
**TGMN: Two-stage graph convolutional mamba network for hyperspectral image classification**  
Yonghe Chu, Jun Cao, Junshi Xia, Weiping Ding — *IEEE Transactions on Neural Networks and Learning Systems*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22TGMN%3A+Two-stage+graph+convolutional+mamba+network+for+hyperspectral+image+classification%22)) · Code: NR · BibTeX: `chu2025tgmn` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Remote sensing | Hyperspectral classification | Superpixel subgraphs | Local-to-global (LG) |

**Graph–SSM division of labor.** GCN models local superpixel relations; Mamba captures broader dependencies.

**Methodology.** Aggregates superpixel subgraphs with graph convolution before a Mamba encoder.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.2 Remote Sensing and Structured Visual Data

</details>

---

<a id="tang2026graph"></a>
### GM-HAD
**Graph Mamba for Fast Hyperspectral Anomaly Detection**  
Sida Tang, Le Sun, Zhuojun Xie, Ting Xie, Xudong Kang, Puhong Duan — *IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing*, 2026  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Graph+Mamba+for+Fast+Hyperspectral+Anomaly+Detection%22)) · Code: NR · BibTeX: `tang2026graph` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Remote sensing | Hyperspectral anomaly detection | Superpixel region-adjacency graph | Graph-guided sequence (GS) |

**Graph–SSM division of labor.** Graph guides local aggregation and ordering; SSM processes the resulting sequence.

**Methodology.** Superpixel region-adjacency graph used for local aggregation and to order regions for the selective SSM.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.2 Remote Sensing and Structured Visual Data

</details>

---

## Articulated and human motion

<a id="dong2024hamba"></a>
### Hamba
**Hamba: Single-view 3D Hand Reconstruction with Graph-guided Bi-Scanning Mamba**  
Haoye Dong, Aviral Chharia, Wenbo Gou, Francisco Vicente Carrasco, Fernando De la Torre — *Advances in Neural Information Processing Systems*, 2024  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Hamba%3A+Single-view+3D+Hand+Reconstruction+with+Graph-guided+Bi-Scanning+Mamba%22)) · Code: NR · BibTeX: `dong2024hamba` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Articulated and human motion | 3D hand reconstruction | Hand-joint graph | Graph-guided sequence (GS) |

**Graph–SSM division of labor.** Graph structure determines the bidirectional scan; SSM models the joint sequence.

**Methodology.** Joint relations determine a Graph-guided Bidirectional Scan aligned with the hand's structural topology.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.2 Remote Sensing and Structured Visual Data; 7.1 Serialization, Permutation, and Robustness

</details>

---

<a id="tang2025spatial"></a>
### Tang et al.
**Spatial-temporal graph mamba for music-guided dance video synthesis**  
Hao Tang, Ling Shao, Zhenyu Zhang, Luc Van Gool, Nicu Sebe — *IEEE transactions on pattern analysis and machine intelligence*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Spatial-temporal+graph+mamba+for+music-guided+dance+video+synthesis%22)) · Code: NR · BibTeX: `tang2025spatial` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Articulated and human motion | Music-guided dance synthesis | Dynamic human-skeleton graph | Relational--temporal (RT); secondary: Graph-guided sequence (GS) |

**Graph–SSM division of labor.** Graph models joint relations; Graph Mamba captures spatial and temporal dependencies.

**Methodology.** Models human skeletons as joint sequences within a spatio-temporal Graph Mamba framework.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.2 Remote Sensing and Structured Visual Data

</details>

---

<sub>Generated by `scripts/generate_catalogue.py` from `data/papers.yaml` and `source/references.bib`. Do not edit by hand.</sub>
