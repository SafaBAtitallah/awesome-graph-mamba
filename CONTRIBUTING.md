# Contributing

Thank you for helping keep this resource current. Contributions of three kinds are welcome:

* **New Graph Mamba papers** (published after or missed by the survey),
* **Corrections** to existing records (classification, metadata, links),
* **Links to official implementations** (`code` field).

Every table, catalogue page, and README block is generated. **Never edit files in `tables/`, `papers/`, `docs/FLAGS.md`, `data/generated/`, or the README blocks between `<!-- BEGIN:... -->` and `<!-- END:... -->` by hand** — edit the data and rebuild.

## Inclusion criteria

A work is in scope if it explicitly integrates Mamba, a selective state-space model, or a closely related structured SSM with a graph-structured representation (survey §1.4). Mamba applied only to sequences or images without an explicit graph-modeling component is out of scope. Structured-SSM precursors without input-dependent selection are accepted when they are direct architectural foundations and must be marked `precursor: true`.

## Workflow

```bash
git checkout -b add-<model-name>
# 1. add the BibTeX entry to source/references.bib (with doi = {...} if available)
# 2. add the record to data/papers.yaml (template below)
pip install -r requirements.txt
python scripts/build.py
python scripts/validate.py
pytest -q
git add -A && git commit -m "Add <model name>" && git push
```

Open a pull request. CI rebuilds the repository and fails if the database is invalid or if committed outputs are stale.

## Record template

Use only identifiers defined in `data/taxonomy.yaml`. Write `NR` (or omit an optional field) when information is not available — never guess.

```yaml
- key: smith2026example            # must match the BibTeX key
  model: ExampleMamba              # name used in the paper
  roles: [taxonomy]                # taxonomy | application | discussed (one or more)
  sections: []                     # manuscript labels; leave empty for papers not in the survey
  taxonomy:                        # required when roles contains taxonomy
    setting: static_general        # static_general | dynamic_spatiotemporal | heterogeneous_higher_order
    d1: "What the SSM reads (tokenization)"
    d2: "How tokens are ordered and scanned"
    d3: [input]                    # input | dynamics | operator   (several allowed)
    d4: [parallel]                 # standalone | sequential | parallel | embedded (several allowed)
  # application:                   # required when roles contains application
  #   domain: healthcare           # healthcare | remote_visual | other
  #   subdomain: neural_signals    # see taxonomy.yaml
  #   task: "..."
  #   graph_construction: "..."
  #   division_of_labor: "Graph does X; SSM does Y."
  #   patterns: [RT]               # DV | RT | GS | LG (several allowed)
  #   dominant_pattern: RT
  #   secondary_pattern: GS        # optional; must also appear in patterns
  methodology: "One or two sentences."
  contributions: ["..."]
  complexity: "$O(\\cdot)$ as reported"   # optional, inline math allowed
  efficiency: {scaling: "...", additional_costs: "...", evidence: "..."}   # optional
  expressivity: {permutation_property: "...", result: "...", caveat: "..."} # optional
  advantages: ["As stated by the authors"]
  limitations: ["As stated by the authors"]
  code: "https://github.com/..."   # optional, official implementation only
  precursor: false                 # optional
  multimodal: false                # optional
  verification:
    status: extracted              # extracted | needs_verification | verified
    flags: []
```

### Classification guidance (D1–D4)

| Dimension | Ask | Notes |
| :--- | :--- | :--- |
| D1 Tokenization | What information is presented to the SSM? | nodes, neighborhoods, walks, metapaths, spectral components, snapshots, higher-order cells |
| D2 Ordering | How are tokens ordered and traversed? | structural ranking, traversal, temporal, type-/rank-aware; uni-/bi-/multi-directional |
| D3 Coupling | Does graph information affect the selective dynamics? | **input**: graph only shapes tokens/order · **dynamics**: graph conditions $B_t$, $C_t$, $\Delta_t$ or the transition · **operator**: the SSM operator is defined on the graph |
| D4 Integration | How is the SSM combined with graph propagation? | **standalone**, **sequential**, **parallel**, **embedded**; attention–SSM hybrids are classified by how the SSM branch is integrated |

### Verification status

* `extracted` — transcribed from a source, not yet checked by a survey author.
* `needs_verification` — ambiguous or conflicting; explain in `flags`.
* `verified` — checked by a survey author (add `verified_by` and `date`). The scripts never overwrite records; `extract_papers.py --merge` only appends stubs for missing works. If a verified record intentionally deviates from a manuscript table, add `override_reason` — validation then reports a warning instead of an error.

## Adding a published-results table

Append a block to `data/results.yaml` with `columns`, `better` (`higher`/`lower` per column), and `rows`. Only add numbers that come from **one source paper under one protocol**; results from different papers must go in separate tables. Use `null` for missing values (rendered `NR`).

## Questions

Open an issue with the label `question` or `paper-suggestion`.
