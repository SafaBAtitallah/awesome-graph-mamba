# Healthcare and Biomedical Applications

*Survey section: Sec. 5.1. 19 work(s).* [← Catalogue index](README.md) · [← Repository home](../README.md)

**Contents**

- *Neural and physiological signals*: [GraphS4mer](#tang2023modeling), [BrainMamba](#behrouz2024brain), [Brain-GM](#wang2024learning), [Brain Network Mamba](#zhang2026brainnetworkmamba), [MSGM](#liu2026msgm)
- *Clinical, biological, and molecular data*: [MGSSM-SAKI](#xu2024identifying), [Aghaee et al.](#aghaee2024graph), [ExPath](#kotoge2026expath), [MGDTA](#han2024innovative), [MKHCNet](#lu2025mamba)
- *Histopathology*: [GAT–Mamba](#ding2024combining), [GraphMamba (WSI)](#zheng2025graphmamba), [MGCM](#cui2026mgcm), [TopoMamSurv](#chen2026graph), [CGAM](#qu2025cgam)
- *Medical imaging*: [GM-UNet](#zhang2024gm), [GGVMamba](#zhou2024efficient), [HGM](#zhu2025hybrid), [GMMN](#zhang2026graph)

## Neural and physiological signals

<a id="tang2023modeling"></a>
### GraphS4mer
**Modeling multivariate biosignals with graph neural networks and structured state space models**  
Siyi Tang, Jared A Dunnmon, Qu Liangqiong, Khaled K Saab, Tina Baykaner, Christopher Lee-Messer, Daniel L Rubin — *Conference on Health, Inference, and Learning*, 2023  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Modeling+multivariate+biosignals+with+graph+neural+networks+and+structured+state+space+models%22)) · Code: NR · BibTeX: `tang2023modeling` `† precursor`

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Neural and physiological signals | Seizure, sleep, ECG classification | Physiological channels; dynamically learned edges | Relational--temporal (RT) |

**Graph–SSM division of labor.** GIN captures graph relations; S4 models long-range temporal dependencies.

**Methodology.** Learns dynamic relationships among physiological variables, combining Graph Structure Learning and GIN with S4 layers.

- **Benchmarks in the survey:** BVFC-MEG, HCP-Mental, HCP-Age (Accuracy)
- **Published results:** [perf_brain](../tables/markdown/perf_brain.md)

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- Falls below several non-SSM baselines on HCP-Mental and HCP-Age (results as reported in the BrainMamba paper).

**Notes**
- Non-selective S4 formulation (structured-SSM precursor).

**Discussed in:** 5.1 Healthcare and Biomedical Applications; 6.2 Benchmark Datasets and Tasks; 6.3 Performance Comparison; A Detailed Performance Comparisons

</details>

---

<a id="behrouz2024brain"></a>
### BrainMamba
**Brain-Mamba: Encoding Brain Activity via Selective State Space Models.**  
Ali Behrouz, Farnoosh Hashemi — *CHIL*, 2024  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Brain-Mamba%3A+Encoding+Brain+Activity+via+Selective+State+Space+Models.%22)) · Code: NR · BibTeX: `behrouz2024brain` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Neural and physiological signals | Brain encoding; attention-deficit/hyperactivity disorder and seizure detection | Brain-unit tokens and multivariate time series | Relational--temporal (RT); secondary: Graph-guided sequence (GS) |

**Graph–SSM division of labor.** Message passing models local relations; selective SSM captures node and temporal dependencies.

**Methodology.** Separates brain-network modeling (BNMamba) from temporal modeling (BTMamba).

- **Benchmarks in the survey:** BVFC-MEG, HCP-Mental, HCP-Age (Accuracy)
- **Published results:** [perf_brain](../tables/markdown/perf_brain.md)

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- Higher mean accuracy than GraphS4mer on BVFC-MEG, HCP-Mental, and HCP-Age; clearest advantage on BVFC-MEG.

**Limitations (stated in the survey)**
- Margin over BrainMixer on HCP benchmarks is small relative to the reported variability.

**Notes**
- Cited as early work for cross-modal graph modeling (tab:future-directions).

**Cited as early work for challenges:** `crossmodal`

**Discussed in:** 5.1 Healthcare and Biomedical Applications; 6.2 Benchmark Datasets and Tasks; 6.3 Performance Comparison; 7.7 Future Research Directions; A Detailed Performance Comparisons

</details>

---

<a id="wang2024learning"></a>
### Brain-GM
**Learning dynamic brain network representation based on graph mamba architecture**  
Jingjie Wang, Jinwei Lang, Li-Zhuang Yang, Hai Li — *2024 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)*, 2024  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Learning+dynamic+brain+network+representation+based+on+graph+mamba+architecture%22)) · Code: NR · BibTeX: `wang2024learning` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Neural and physiological signals | Brain decoding and disease classification | Dynamic brain networks | Relational--temporal (RT) |

**Graph–SSM division of labor.** Graph learning models time-varying connectivity; SSM captures temporal evolution.

**Methodology.** Models time-varying brain connectivity.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.1 Healthcare and Biomedical Applications

</details>

---

<a id="zhang2026brainnetworkmamba"></a>
### Brain Network Mamba
**Brain Network Mamba: A Bi-Directional State-Space Model for Brain Network Analysis on rs-fMRI**  
Li Zhang, Shuo Huang, Di Ma, Daoqiang Zhang, Li Zhang — *Machine Learning in Medical Imaging: 16th International Workshop, MLMI 2025, Held in Conjunction with MICCAI 2025, Daejeon, South Korea, September 23, 2025, Proceedings*, 2026  
[DOI](https://doi.org/10.1007/978-3-032-09513-8_22) · Code: NR · BibTeX: `zhang2026brainnetworkmamba` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Neural and physiological signals | Resting-state fMRI analysis | Functional brain networks | Local-to-global (LG) |

**Graph–SSM division of labor.** Graph structure captures regional interactions; bidirectional SSM models broader dependencies.

**Methodology.** Bidirectional state-space processing of resting-state fMRI network representations.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.1 Healthcare and Biomedical Applications

</details>

---

<a id="liu2026msgm"></a>
### MSGM
**Msgm: A multi-scale spatiotemporal graph mamba for eeg emotion recognition**  
Hanwen Liu, Yifeng Gong, Zuwei Yan, Zeheng Zhuang, Jiaxuan Lu — *Frontiers in Neuroscience*, 2026  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Msgm%3A+A+multi-scale+spatiotemporal+graph+mamba+for+eeg+emotion+recognition%22)) · Code: NR · BibTeX: `liu2026msgm` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Neural and physiological signals | EEG emotion recognition | Local–global brain graphs | Relational--temporal (RT) |

**Graph–SSM division of labor.** Graph modules model brain relations; SSM captures spatio-temporal dependencies.

**Methodology.** Combines multi-scale temporal segmentation with local–global brain graphs.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.1 Healthcare and Biomedical Applications

</details>

---

## Clinical, biological, and molecular data

<a id="xu2024identifying"></a>
### MGSSM-SAKI
**Identifying Subphenotypes for Sepsis with Acute Kidney Injury via Multimodal Graph State Space Models**  
Haowei Xu, Tongyue Shi, Wentie Liu, Huiying Zhao, Guilan Kong — *Artificial Intelligence and Data Science for Healthcare: Bridging Data-Centric AI and People-Centric Healthcare*, 2024  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Identifying+Subphenotypes+for+Sepsis+with+Acute+Kidney+Injury+via+Multimodal+Graph+State+Space+Models%22)) · Code: NR · BibTeX: `xu2024identifying` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Clinical, biological, and molecular data | Sepsis-AKI subphenotyping | Adaptive graph from multimodal clinical variables | Relational--temporal (RT); secondary: Dual-view (DV) |

**Graph–SSM division of labor.** Graph aggregation models patient-state relations; SSM captures temporal evolution.

**Methodology.** Adaptively infers latent graphs from multimodal clinical variables, combining graph-based local relationships with temporal patient-state modeling.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.1 Healthcare and Biomedical Applications

</details>

---

<a id="aghaee2024graph"></a>
### Aghaee et al.
**Graph Neural Network Representation of State Space Models of Metabolic Pathways**  
Mohammad Aghaee, Stephane Krau, Melih Tamer, Hector Budman — *IFAC-PapersOnLine*, 2024  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Graph+Neural+Network+Representation+of+State+Space+Models+of+Metabolic+Pathways%22)) · Code: NR · BibTeX: `aghaee2024graph` `† precursor`

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Clinical, biological, and molecular data | Metabolic-pathway modeling | Metabolic-pathway graphs | Relational--temporal (RT) |

**Graph–SSM division of labor.** Graph models pathway interactions; structured SSM captures temporal evolution.

**Methodology.** Represents metabolic pathways as graphs and uses structured state-space modeling for their temporal evolution.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.1 Healthcare and Biomedical Applications

</details>

---

<a id="kotoge2026expath"></a>
### ExPath
*Also referred to as: PathMamba, ExPath / PathMamba*  
**Targeted pathway inference for biological knowledge bases via graph learning and explanation**  
Rikuto Kotoge, Ziwei Yang, Zheng Chen, Yushun Dong, Yasuko Matsubara, Jimeng Sun, Yasushi Sakurai — *Proceedings of the AAAI Conference on Artificial Intelligence*, 2026  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Targeted+pathway+inference+for+biological+knowledge+bases+via+graph+learning+and+explanation%22)) · Code: NR · BibTeX: `kotoge2026expath` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Clinical, biological, and molecular data | Pathway inference and explanation | Molecular network and sampled pathway sequences | Graph-guided sequence (GS) |

**Graph–SSM division of labor.** GIN captures local pathway structure; Mamba processes graph-derived pathways.

**Methodology.** Converts sampled molecular pathways into sequences for Mamba (PathMamba) while retaining graph-based pathway structure; PathExplainer learns pathway-level masks.

**Key contributions (as characterized in the survey)**
- Explicit explanation via pathway-level masks identifying the biological subgraphs most responsible for a prediction.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Cited as early work for challenges:** `interpretability`

**Discussed in:** 5.1 Healthcare and Biomedical Applications; 7.4 Interpretability and Explainability; 7.7 Future Research Directions

</details>

---

<a id="han2024innovative"></a>
### MGDTA
**Innovative Mamba and graph transformer framework for superior protein-ligand affinity prediction**  
Kaitai Han, Chaojing Shi, Zijun Wang, Wu Liu, Zhenxing Li, Zhenghui Wang, Lixin Lei, Ruoyan Dai, Mengqiu Wang, Zhiwei Zhang, et al. — *Microchemical Journal*, 2024  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Innovative+Mamba+and+graph+transformer+framework+for+superior+protein-ligand+affinity+prediction%22)) · Code: NR · BibTeX: `han2024innovative` `◆ multimodal`

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Clinical, biological, and molecular data | Drug–target affinity prediction | Drug graph and protein sequence | Dual-view (DV) |

**Graph–SSM division of labor.** Graph encoder models molecular structure; Mamba models protein sequence before fusion.

**Methodology.** Combines drug molecular graphs with Mamba-encoded protein sequences.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.1 Healthcare and Biomedical Applications

</details>

---

<a id="lu2025mamba"></a>
### MKHCNet
**Mamba-enhanced disease semantic knowledge graph for interpretable automatic ICD coding**  
Pengli Lu, Chao Dong, Jingjin Xue, Fentang Gao — *Journal of biomedical informatics*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Mamba-enhanced+disease+semantic+knowledge+graph+for+interpretable+automatic+ICD+coding%22)) · Code: NR · BibTeX: `lu2025mamba` `◆ multimodal`

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Clinical, biological, and molecular data | Automatic ICD coding | Disease knowledge graph linked to ICD labels | Dual-view (DV) |

**Graph–SSM division of labor.** Graph enriches label semantics; Mamba captures long-range EHR-text dependencies.

**Methodology.** Integrates a disease semantic knowledge graph with Mamba-based modeling of electronic health records for interpretable ICD coding.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.1 Healthcare and Biomedical Applications

</details>

---

## Histopathology

<a id="ding2024combining"></a>
### GAT–Mamba
**Combining graph neural network and Mamba to capture local and global tissue spatial relationships in whole slide images**  
Ruiwen Ding, Kha-Dinh Luong, Erika Rodriguez, Ana Cristina Araujo Lemos Da Silva, William Hsu — *Scientific Reports*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Combining+graph+neural+network+and+Mamba+to+capture+local+and+global+tissue+spatial+relationships+in+whole+slide+images%22)) · Code: NR · BibTeX: `ding2024combining` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Histopathology | Lung-cancer survival prediction | WSI tissue-region graph | Local-to-global (LG) |

**Graph–SSM division of labor.** GAT models local tissue relations; Mamba captures global contextual dependencies.

**Methodology.** Combines graph attention with Mamba for progression-free survival prediction in early-stage lung adenocarcinoma.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.1 Healthcare and Biomedical Applications

</details>

---

<a id="zheng2025graphmamba"></a>
### GraphMamba (WSI)
**GraphMamba: Whole slide image classification meets graph-driven selective state space model**  
Tingting Zheng, Hongxun Yao, Sicheng Zhao, Kui Jiang, Yi Xiao — *Pattern Recognition*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22GraphMamba%3A+Whole+slide+image+classification+meets+graph-driven+selective+state+space+model%22)) · Code: NR · BibTeX: `zheng2025graphmamba` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Histopathology | WSI classification | Multi-level instance/group graphs | Graph-guided sequence (GS) |

**Graph–SSM division of labor.** Graph hierarchy defines groups; Mamba models intra- and cross-group dependencies.

**Methodology.** Multi-level graph construction with intra- and cross-group Graph Mamba modules.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Notes**
- One of three unrelated models published as 'GraphMamba'; disambiguated as GraphMamba (WSI).

**Discussed in:** 5.1 Healthcare and Biomedical Applications

</details>

---

<a id="cui2026mgcm"></a>
### MGCM
**MGCM: Multi-modal graph convolutional mamba for cancer survival prediction**  
Jiaqi Cui, Yilun Li, Dinggang Shen, Yan Wang — *Pattern Recognition*, 2026  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22MGCM%3A+Multi-modal+graph+convolutional+mamba+for+cancer+survival+prediction%22)) · Code: NR · BibTeX: `cui2026mgcm` `◆ multimodal`

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Histopathology | Multimodal cancer survival prediction | Transcriptomic and pathology graphs | Dual-view (DV) |

**Graph–SSM division of labor.** Graph convolution models within-modality structure; Mamba captures cross-modal dependencies.

**Methodology.** Combines transcriptomic co-expression and pathology patch graphs with interactive Mamba modules.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.1 Healthcare and Biomedical Applications

</details>

---

<a id="chen2026graph"></a>
### TopoMamSurv
**Graph Mamba Survival Analysis Based on Topology-Aware ordering**  
Yuanfang Chen, Peiqiang Yan, Yuntao Shou, Qian Zhao, Xiangyong Cao — *arXiv preprint arXiv:2606.02602*, 2026  
[arXiv](https://arxiv.org/abs/2606.02602) · Code: NR · BibTeX: `chen2026graph` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Histopathology | WSI survival analysis | Topology-aware WSI graph | Graph-guided sequence (GS) |

**Graph–SSM division of labor.** Graph convolution models local structure; bidirectional Mamba processes topology-ordered nodes.

**Methodology.** Topology-aware node ordering before bidirectional Mamba processing.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.1 Healthcare and Biomedical Applications

</details>

---

<a id="qu2025cgam"></a>
### CGAM
**CGAM: An end-to-end causality graph attention Mamba network for esophageal pathology grading**  
Yingbo Qu, Xiangli Zhou, Pan Huang, Yanan Liu, Francesco Mercaldo, Antonella Santone, Peng Feng — *Biomedical Signal Processing and Control*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22CGAM%3A+An+end-to-end+causality+graph+attention+Mamba+network+for+esophageal+pathology+grading%22)) · Code: NR · BibTeX: `qu2025cgam` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Histopathology | Esophageal pathology grading | Tumor and microenvironment graph | Local-to-global (LG) |

**Graph–SSM division of labor.** Graph attention models local topology; Mamba captures broader dependencies.

**Methodology.** Combines graph attention and Mamba.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.1 Healthcare and Biomedical Applications

</details>

---

## Medical imaging

<a id="zhang2024gm"></a>
### GM-UNet
**GM-UNet: Graph Mamba UNet for Medical Image Segmentation**  
Chengcheng Zhang, Yihao He, Wei Li, Jiajia Zhang, Xiaohui Cui — *2024 5th International Seminar on Artificial Intelligence, Networking and Information Technology (AINIT)*, 2024  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22GM-UNet%3A+Graph+Mamba+UNet+for+Medical+Image+Segmentation%22)) · Code: NR · BibTeX: `zhang2024gm` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Medical imaging | Image segmentation | Dynamic feature graph within U-Net | Local-to-global (LG) |

**Graph–SSM division of labor.** Graph modules model feature relations; Mamba provides broader contextual modeling.

**Methodology.** Embeds dynamic feature graphs within a U-Net for medical image segmentation.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.1 Healthcare and Biomedical Applications

</details>

---

<a id="zhou2024efficient"></a>
### GGVMamba
**Efficient and Gender-Adaptive Graph Vision Mamba for Pediatric Bone Age Assessment**  
Lingyu Zhou, Zhang Yi, Kai Zhou, Xiuyuan Xu — *International Conference on Medical Image Computing and Computer-Assisted Intervention*, 2024  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Efficient+and+Gender-Adaptive+Graph+Vision+Mamba+for+Pediatric+Bone+Age+Assessment%22)) · Code: NR · BibTeX: `zhou2024efficient` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Medical imaging | Bone-age assessment | Gender-adaptive inter-region graph | Graph-guided sequence (GS) |

**Graph–SSM division of labor.** Graph models inter-region relations; graph-guided bidirectional Mamba captures context.

**Methodology.** Directed scanning, a Graph Mamba encoder, and gender-adaptive graph structures for pediatric bone-age assessment.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.1 Healthcare and Biomedical Applications

</details>

---

<a id="zhu2025hybrid"></a>
### HGM
**Hybrid graph mamba: Unlocking non-euclidean potential for accurate polyp segmentation**  
Yueyue Zhu, Haolin Lv, Geng Chen, Zhonghao Zhang, Haotian Jiang, Yong Xia — *International Conference on Medical Image Computing and Computer-Assisted Intervention*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Hybrid+graph+mamba%3A+Unlocking+non-euclidean+potential+for+accurate+polyp+segmentation%22)) · Code: NR · BibTeX: `zhu2025hybrid` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Medical imaging | Polyp segmentation | Graph over image regions | Local-to-global (LG) |

**Graph–SSM division of labor.** GCN captures local topology; multi-directional Mamba models global context.

**Methodology.** Graph convolution combined with multi-directional Mamba.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.1 Healthcare and Biomedical Applications

</details>

---

<a id="zhang2026graph"></a>
### GMMN
**Graph mapping mamba network for automated macular edema diagnosis from fundus images**  
Yiming Zhang, Hongqing Zhu, Tianwei Qian, Ning Chen, Xun Xu, Bingcang Huang — *Information Fusion*, 2026  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Graph+mapping+mamba+network+for+automated+macular+edema+diagnosis+from+fundus+images%22)) · Code: NR · BibTeX: `zhang2026graph` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Medical imaging | Macular edema diagnosis | Graph over fundus representations | Local-to-global (LG) |

**Graph–SSM division of labor.** GCN captures local spatial correlations; Mamba models long-range dependencies.

**Methodology.** Integrates graph convolution and Mamba for macular edema diagnosis from fundus images.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.1 Healthcare and Biomedical Applications

</details>

---

<sub>Generated by `scripts/generate_catalogue.py` from `data/papers.yaml` and `source/references.bib`. Do not edit by hand.</sub>
