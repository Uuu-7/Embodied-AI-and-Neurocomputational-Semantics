# Shared HA0/HA1 submission package

This folder packages the course materials for the instructor-accepted 20 Chinese + 20 English sense inventory. HA1 is a **reproducible submission version** with executed cells and regenerated outputs. Xia Yuqi confirmed the original lexical inventory. The EN15 movement-sense wording and nine feature-review decisions are recorded in `data/reviews/HA1_ADJUDICATION_V4.md`. No LMS upload or three-person agreement is claimed.

| Artifact | Purpose |
|---|---|
| `HA0/ha0_zh20_en20.csv` | Forty senses, one defined category parent each, example sentences, seven 0–2 channels, per-value provenance, and an explicit uncertainty row |
| `HA0/ha0_review.ipynb` | Executed notebook showing the 40-sense inventory, parent choices, 280-score audit, uncertainty, and testable question |
| `HA0/HA0_METHOD.md` | Parent policy, scoring rubric, provenance limits, testable question, and falsifying result |
| `HA1/ha1_simulator.ipynb` | Self-contained executed notebook with visible C/S functions, min–max scaling, C×S scatter, adjustable A(w), three required weights, and sensitivity diagnostics |
| `HA1/ha1_scores_zh20_en20.csv` | Raw/normalized C and S, quadrants, and A values for all 40 senses; missing S and A stay blank |
| `HA1/ha1_weight_sensitivity_details.csv` | Weight-change and fragility explanations for the 25 scorable senses |
| `HA1/figures/` | C×S and weight-sensitivity PNGs |
| `HA1/INTERPRETATION.md` | Approximately 300-word interpretation, embedded in the notebook |

## Reproduce

Open `HA0/ha0_review.ipynb` and `HA1/ha1_simulator.ipynb` in Jupyter and run all cells from within the repository. Both notebooks contain their own processing code and need no project `.py` import. The versioned v4 CSV is the fixed input; HA1 writes its score CSVs and two PNG figures to its folder. The runtime needs NumPy, pandas, Matplotlib, IPython, and Jupyter; ipywidgets enables the optional live weight slider. The archived data-builder code under `data/final/` documents how v4 was derived but is not required to run either submission notebook.

The submission CSVs use UTF-8 with a BOM so Windows spreadsheet software recognizes the Chinese characters. The HA1 notebook uses the same encoding when exporting new CSVs.

The HA0 table and HA1 results use the same v4 input. Four feature values were changed and five flagged values were retained with reasons; the 25 reported S paths have their edge counts checked but have not all been independently revalidated against source synsets. If the team changes scores or target senses, record the decision in a new version and rerun HA1. Submit the notebook, HA0 CSV and method, and interpretation to the course LMS according to the instructor's requirements.
