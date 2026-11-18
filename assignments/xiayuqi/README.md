# Xia Yuqi — HA0 and HA1 working submission

The instructor accepted **20 Chinese + 20 English** senses for this bilingual dataset. These files are Xia's working assignment materials derived from the integrated v2 vocabulary in `data/final/`. They are separate from the team's final annotation sign-off.

| File | Purpose |
|---|---|
| `ha0_zh20_en20_xiayuqi.csv` | 40-row HA0 export with one parent, example, seven features, value-level provenance, and one uncertainty note |
| `HA0_GUIDE.md` | Feature rubric, category-parent meanings, testable question, falsifying result, and provenance limits |
| `ha1_simulator.ipynb` | Executed HA1 notebook: separate C and S, min–max normalization, scatter, adjustable A(w), and sensitivity checks |
| `ha1_model.py` | Functions called by the notebook |
| `ha1_scores_zh20_en20.csv` | Raw and normalized C/S, quadrants, and A at three weights for all 40 rows; S and A remain blank where unsupported |
| `ha1_weight_sensitivity_details.csv` | Every scorable concept's weight change, fragile flag, and one-sentence explanation |
| `figures/*.png` | Standalone C×S and weight-sensitivity plots |
| `HA1_INTERPRETATION.md` | Approximately 300-word interpretation, also embedded in the notebook |
| `TEAM_REVIEW_UPDATE.md` | Status of the v2 integration and pending verification |
| `refresh_ha0.py`, `refresh_notebook.py` | Rebuild HA0 from v2 and refresh the notebook input/text |

## Reproduce

Open `ha1_simulator.ipynb` in Jupyter and run all cells. It finds the repository root from the current directory. Python with NumPy, pandas, Matplotlib, IPython, and Jupyter is required. The notebook records its runtime versions and rewrites the derived CSV and figures. There is no random step.

The C ratings reconcile Chen's draft and Hu's review. Their exact origins are recorded in `data/final/feature_provenance_v2.csv`; the S paths still require independent review. The example sentences are constructed illustrations. No LMS submission or three-person approval is represented by this folder.
