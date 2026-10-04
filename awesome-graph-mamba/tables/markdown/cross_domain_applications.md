## T4 · Cross-domain applications and graph–SSM design patterns

*Cross-domain Graph Mamba applications and recurring graph–SSM design patterns (manuscript tab:cross-domain-applications and fig:design-patterns).*

| Work | Year | Task | Graph construction | Graph–SSM division of labor | DV | RT | GS | LG | Dominant (secondary) |
| :--- | :---: | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Healthcare and Biomedical Applications — Neural and physiological signals** | | | | | | | | | |
| GraphS4mer† | 2023 | Seizure, sleep, ECG classification | Physiological channels; dynamically learned edges | GIN captures graph relations; S4 models long-range temporal dependencies. |  | ✓ |  |  | RT |
| BrainMamba | 2024 | Brain encoding; attention-deficit/hyperactivity disorder and seizure detection | Brain-unit tokens and multivariate time series | Message passing models local relations; selective SSM captures node and temporal dependencies. |  | ✓ | ✓ |  | RT (+GS) |
| Brain-GM | 2024 | Brain decoding and disease classification | Dynamic brain networks | Graph learning models time-varying connectivity; SSM captures temporal evolution. |  | ✓ |  |  | RT |
| [Brain Network Mamba](https://doi.org/10.1007/978-3-032-09513-8_22) | 2026 | Resting-state fMRI analysis | Functional brain networks | Graph structure captures regional interactions; bidirectional SSM models broader dependencies. |  |  |  | ✓ | LG |
| MSGM | 2026 | EEG emotion recognition | Local–global brain graphs | Graph modules model brain relations; SSM captures spatio-temporal dependencies. |  | ✓ |  |  | RT |
| **Healthcare and Biomedical Applications — Clinical, biological, and molecular data** | | | | | | | | | |
| MGSSM-SAKI | 2024 | Sepsis-AKI subphenotyping | Adaptive graph from multimodal clinical variables | Graph aggregation models patient-state relations; SSM captures temporal evolution. | ✓ | ✓ |  |  | RT (+DV) |
| Aghaee et al.† | 2024 | Metabolic-pathway modeling | Metabolic-pathway graphs | Graph models pathway interactions; structured SSM captures temporal evolution. |  | ✓ |  |  | RT |
| ExPath | 2026 | Pathway inference and explanation | Molecular network and sampled pathway sequences | GIN captures local pathway structure; Mamba processes graph-derived pathways. |  |  | ✓ |  | GS |
| MGDTA◆ | 2024 | Drug–target affinity prediction | Drug graph and protein sequence | Graph encoder models molecular structure; Mamba models protein sequence before fusion. | ✓ |  |  |  | DV |
| MKHCNet◆ | 2025 | Automatic ICD coding | Disease knowledge graph linked to ICD labels | Graph enriches label semantics; Mamba captures long-range EHR-text dependencies. | ✓ |  |  |  | DV |
| **Healthcare and Biomedical Applications — Histopathology** | | | | | | | | | |
| GAT–Mamba | 2025 | Lung-cancer survival prediction | WSI tissue-region graph | GAT models local tissue relations; Mamba captures global contextual dependencies. |  |  |  | ✓ | LG |
| GraphMamba (WSI) | 2025 | WSI classification | Multi-level instance/group graphs | Graph hierarchy defines groups; Mamba models intra- and cross-group dependencies. |  |  | ✓ |  | GS |
| MGCM◆ | 2026 | Multimodal cancer survival prediction | Transcriptomic and pathology graphs | Graph convolution models within-modality structure; Mamba captures cross-modal dependencies. | ✓ |  |  |  | DV |
| [TopoMamSurv](https://arxiv.org/abs/2606.02602) | 2026 | WSI survival analysis | Topology-aware WSI graph | Graph convolution models local structure; bidirectional Mamba processes topology-ordered nodes. |  |  | ✓ |  | GS |
| CGAM | 2025 | Esophageal pathology grading | Tumor and microenvironment graph | Graph attention models local topology; Mamba captures broader dependencies. |  |  |  | ✓ | LG |
| **Healthcare and Biomedical Applications — Medical imaging** | | | | | | | | | |
| GM-UNet | 2024 | Image segmentation | Dynamic feature graph within U-Net | Graph modules model feature relations; Mamba provides broader contextual modeling. |  |  |  | ✓ | LG |
| GGVMamba | 2024 | Bone-age assessment | Gender-adaptive inter-region graph | Graph models inter-region relations; graph-guided bidirectional Mamba captures context. |  |  | ✓ |  | GS |
| HGM | 2025 | Polyp segmentation | Graph over image regions | GCN captures local topology; multi-directional Mamba models global context. |  |  |  | ✓ | LG |
| GMMN | 2026 | Macular edema diagnosis | Graph over fundus representations | GCN captures local spatial correlations; Mamba models long-range dependencies. |  |  |  | ✓ | LG |
| **Remote Sensing and Structured Visual Applications — Remote sensing** | | | | | | | | | |
| GraphMamba (HSI) | 2024 | Hyperspectral classification | Spatial neighborhoods and spectral representations | SpatialGCN captures local spatial relations; HyperMamba models global spectral dependencies. | ✓ |  |  |  | DV |
| MGF-GCN◆ | 2025 | Multimodal remote-sensing segmentation | Height-aware multimodal graph | Graph convolution captures spatial/elevation relations; Mamba models cross-modal interactions. | ✓ |  |  |  | DV |
| GraphMamba (tok.) | 2025 | Hyperspectral classification | Graph-guided spectral–spatial tokens | Graph constructs and prioritizes tokens; Mamba models their global dependencies. |  |  | ✓ |  | GS |
| TGMN | 2025 | Hyperspectral classification | Superpixel subgraphs | GCN models local superpixel relations; Mamba captures broader dependencies. |  |  |  | ✓ | LG |
| GM-HAD | 2026 | Hyperspectral anomaly detection | Superpixel region-adjacency graph | Graph guides local aggregation and ordering; SSM processes the resulting sequence. |  |  | ✓ |  | GS |
| **Remote Sensing and Structured Visual Applications — Articulated and human motion** | | | | | | | | | |
| Hamba | 2024 | 3D hand reconstruction | Hand-joint graph | Graph structure determines the bidirectional scan; SSM models the joint sequence. |  |  | ✓ |  | GS |
| Tang et al. | 2025 | Music-guided dance synthesis | Dynamic human-skeleton graph | Graph models joint relations; Graph Mamba captures spatial and temporal dependencies. |  | ✓ | ✓ |  | RT (+GS) |
| **Other Application Areas — Financial forecasting** | | | | | | | | | |
| SAMBA | 2025 | Stock-return forecasting | Adaptive inter-asset graph | Graph convolution models asset relations; bidirectional Mamba captures price dynamics. |  | ✓ |  |  | RT |
| **Other Application Areas — Industrial prognostics** | | | | | | | | | |
| Ren et al. | 2026 | Aero-engine remaining useful life (RUL) prediction | Spatio-temporal sensor hypergraph | Hypergraph models higher-order sensor relations; Graph Mamba captures temporal degradation. |  | ✓ |  |  | RT |
| **Other Application Areas — Cybersecurity and intrusion detection** | | | | | | | | | |
| IDS–GraphMamba | 2025 | IoMT intrusion detection | Flow transition graph | Graph modules capture directional flow relations; SSM models sequential dependencies. |  | ✓ |  |  | RT |
| **Other Application Areas — Language and semantic modeling** | | | | | | | | | |
| MambaForGCN | 2025 | Aspect-based sentiment analysis | Syntactic dependency graph | SynGCN models syntax; Mamba models broader semantic context before fusion. | ✓ |  |  |  | DV |

> Patterns: DV = dual-view; RT = relational–temporal; GS = graph-guided sequence; LG = local-to-global. Multiple check marks indicate combined patterns; the dominant/secondary assignment follows fig:design-patterns.  
> Markers: † structured-SSM precursor without input-dependent selection; ◆ multimodal input; ⚠ record flagged for author verification (see docs/FLAGS.md). NR = not reported in the survey.  

<sub>Generated by `scripts/generate_tables.py` from `data/`. Do not edit by hand. Formats: [LaTeX](../latex/cross_domain_applications.tex) · [CSV](../csv/cross_domain_applications.csv)</sub>
