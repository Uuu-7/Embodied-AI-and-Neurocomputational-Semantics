# Shared HA0/HA1 working submission

This folder packages the team's current course materials for the instructor-accepted 20 Chinese + 20 English sense inventory. It is a **working draft**. Xia Yuqi manually confirmed the lexical senses; the parent nodes and seven-feature audit were prepared with AI assistance and remain open to team review. No LMS upload or three-person agreement is claimed.

| Artifact | Purpose |
|---|---|
| `HA0/ha0_zh20_en20.csv` | Forty senses, one defined category parent each, example sentences, seven 0–2 channels, per-value provenance, and an explicit uncertainty row |
| `HA0/HA0_METHOD.md` | Parent policy, scoring rubric, provenance limits, testable question, and falsifying result |
| `HA1/ha1_simulator.ipynb` | Executed notebook with separate C/S functions, min–max scaling, C×S scatter, adjustable A(w), three required weights, and sensitivity diagnostics |
| `HA1/ha1_scores_zh20_en20.csv` | Raw/normalized C and S, quadrants, and A values for all 40 senses; missing S and A stay blank |
| `HA1/ha1_weight_sensitivity_details.csv` | Weight-change and fragility explanations for the 25 scorable senses |
| `HA1/figures/` | C×S and weight-sensitivity PNGs |
| `HA1/INTERPRETATION.md` | Approximately 300-word interpretation, embedded in the notebook |

## Reproduce

From the repository root, run `python data/final/build_v3.py`, then open `submissions/team/HA1/ha1_simulator.ipynb` and run all cells. The builder uses the preserved v2 table and 280-value provenance file; it has no random step. The notebook requires Python, NumPy, pandas, Matplotlib, IPython, and Jupyter/nbclient. It writes the score CSVs and figures in its own folder. `HA1/refresh_notebook.py` synchronizes the notebook's input description and interpretation after a deliberate source update; run all notebook cells again afterward.

The shared HA0 table is a submission candidate, not an independently agreed team annotation. Nine feature values are flagged in `data/reviews/feature_score_audit_v3.csv`; the 25 reported S paths have not been independently revalidated. If the team changes scores or target senses, record the decision in a new version and rerun HA1.
