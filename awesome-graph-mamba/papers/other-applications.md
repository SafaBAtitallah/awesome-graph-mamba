# Other Application Areas

*Survey section: Sec. 5.3. 4 work(s).* [← Catalogue index](README.md) · [← Repository home](../README.md)

**Contents**

- *Financial forecasting*: [SAMBA](#mehrabian2024mamba)
- *Industrial prognostics*: [Ren et al.](#ren2026spatio)
- *Cybersecurity and intrusion detection*: [IDS–GraphMamba](#atitallah2025ids)
- *Language and semantic modeling*: [MambaForGCN](#lawan2024mambaforgcn)

## Financial forecasting

<a id="mehrabian2024mamba"></a>
### SAMBA
**Mamba meets financial markets: A graph-mamba approach for stock price prediction**  
Ali Mehrabian, Ehsan Hoseinzade, Mahdi Mazloum, Xiaohong Chen — *ICASSP 2025-2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Mamba+meets+financial+markets%3A+A+graph-mamba+approach+for+stock+price+prediction%22)) · Code: NR · BibTeX: `mehrabian2024mamba` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Financial forecasting | Stock-return forecasting | Adaptive inter-asset graph | Relational--temporal (RT) |

**Graph–SSM division of labor.** Graph convolution models asset relations; bidirectional Mamba captures price dynamics.

**Methodology.** Adaptive Graph Convolution over inter-asset relationships with Bidirectional Mamba over historical price sequences.

- **Benchmarks in the survey:** NASDAQ, NYSE, DJIA (RMSE, training time)
- **Published results:** [perf_financial](../tables/markdown/perf_financial.md)

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- Lower RMSE than LSTM, Transformer, and FourierGNN on NASDAQ, NYSE, and DJIA; training time lower than Transformer and FourierGNN (higher than LSTM).

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.3 Other Application Areas; 6.2 Benchmark Datasets and Tasks; 6.3 Performance Comparison; A Detailed Performance Comparisons

</details>

---

## Industrial prognostics

<a id="ren2026spatio"></a>
### Ren et al.
**Spatio-temporal hypergraph-driven evolutionary graph-mamba method for remaining useful life prediction**  
Yonglei Ren, Zong Meng, Kai Chen, Weiliang Sun, Haoze Chen — *Advanced Engineering Informatics*, 2026  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Spatio-temporal+hypergraph-driven+evolutionary+graph-mamba+method+for+remaining+useful+life+prediction%22)) · Code: NR · BibTeX: `ren2026spatio` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Industrial prognostics | Aero-engine remaining useful life (RUL) prediction | Spatio-temporal sensor hypergraph | Relational--temporal (RT) |

**Graph–SSM division of labor.** Hypergraph models higher-order sensor relations; Graph Mamba captures temporal degradation.

**Methodology.** Spatio-temporal hypergraph from multi-sensor degradation signals and prior engine knowledge.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.3 Other Application Areas

</details>

---

## Cybersecurity and intrusion detection

<a id="atitallah2025ids"></a>
### IDS–GraphMamba
**IDS–GraphMamba: A Markov-Enhanced Graph Mamba Framework for Real-Time Intrusion Detection in IoMT Edge Networks**  
Safa Ben Atitallah, Maha Driss, Wadii Boulila — *Computer Networks*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22IDS%E2%80%93GraphMamba%3A+A+Markov-Enhanced+Graph+Mamba+Framework+for+Real-Time+Intrusion+Detection+in+IoMT+Edge+Networks%22)) · Code: NR · BibTeX: `atitallah2025ids` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Cybersecurity and intrusion detection | IoMT intrusion detection | Flow transition graph | Relational--temporal (RT) |

**Graph–SSM division of labor.** Graph modules capture directional flow relations; SSM models sequential dependencies.

**Methodology.** IoMT communication flows represented by a row-stochastic transition matrix; directional graph convolution, Markov-based message passing, and a selective state-space module.

- **Benchmarks in the survey:** NR

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- NR

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.3 Other Application Areas

</details>

---

## Language and semantic modeling

<a id="lawan2024mambaforgcn"></a>
### MambaForGCN
**Enhancing long-range dependency with state space model and Kolmogorov-Arnold networks for aspect-based sentiment analysis**  
Adamu Lawan, Juhua Pu, Haruna Yunusa, Aliyu Umar, Muhammad Lawan — *Proceedings of the 31st international conference on computational linguistics*, 2025  
Link: NR ([Scholar search](https://scholar.google.com/scholar?q=%22Enhancing+long-range+dependency+with+state+space+model+and+Kolmogorov-Arnold+networks+for+aspect-based+sentiment+analysis%22)) · Code: NR · BibTeX: `lawan2024mambaforgcn` 

| Data setting | Task | Graph construction | Design pattern |
| :--- | :--- | :--- | :--- |
| Language and semantic modeling | Aspect-based sentiment analysis | Syntactic dependency graph | Dual-view (DV) |

**Graph–SSM division of labor.** SynGCN models syntax; Mamba models broader semantic context before fusion.

**Methodology.** Syntactic dependency graph (SynGCN) combined with Mamba-based contextual modeling, fused afterwards.

- **Benchmarks in the survey:** Restaurant14, Laptop14, Twitter14 (Accuracy, F1-score)
- **Published results:** [perf_absa](../tables/markdown/perf_absa.md)

<details><summary>Advantages, limitations, and notes</summary>

**Advantages (stated in the survey)**
- Higher accuracy and F1 than the compared graph-based baselines on Restaurant14, Laptop14, and Twitter14 (as reported).

**Limitations (stated in the survey)**
- NR

**Discussed in:** 5.3 Other Application Areas; 6.2 Benchmark Datasets and Tasks; 6.3 Performance Comparison; A Detailed Performance Comparisons

</details>

---

<sub>Generated by `scripts/generate_catalogue.py` from `data/papers.yaml` and `source/references.bib`. Do not edit by hand.</sub>
