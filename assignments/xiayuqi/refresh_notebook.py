"""Point the executed HA1 notebook at the reconciled v2 inventory."""

from pathlib import Path

import nbformat


HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE / "ha1_simulator.ipynb"
INTERPRETATION = HERE / "HA1_INTERPRETATION.md"
V1 = "data/final/spatial_relations_zh20_en20_v1.csv"
V2 = "data/final/spatial_relations_zh20_en20_v2.csv"


def main() -> None:
    nb = nbformat.read(NOTEBOOK, as_version=4)
    nb.cells[0].source = """# HA1 — Graded abstractness simulator

**Xia Yuqi's working submission; 20 Chinese + 20 English senses.** The instructor accepted the bilingual 40-row scope. Source: `data/final/spatial_relations_zh20_en20_v2.csv`. The integrated C values reconcile Chen's PR #14 draft with Hu's review; previous v1 scores are retained as traceable inputs. S paths remain reported and need independent source validation. This computational notebook does not claim three independent ratings or team sign-off.

Run all cells from any directory inside the repository. The notebook saves a 40-row derived table and two figures in this folder. The exact feature provenance is in `data/final/feature_provenance_v2.csv`."""
    nb.cells[1].source = nb.cells[1].source.replace(V1, V2)
    nb.cells[3].source = nb.cells[3].source.replace(V1, V2)
    nb.cells[4].source = nb.cells[4].source.replace("== 14", "== 15")
    nb.cells[5].source = """## 2. C×S plane

The dashed dividers are at **0.5 on the normalized axes**. Only the 25 senses with a reported S path appear. The 15 remaining rows stay in the exported table with S and A missing. IDs on the figure match the table. The reported paths still need independent validation."""
    nb.cells[12].source = """### Provenance and cutoff sensitivity

The integrated dataset has already removed the incompatible balance path. This check contrasts the lecture's **dataset-relative min–max C threshold** against the earlier team's fixed raw threshold `C_sum >= 5`, with the same `S_depth >= 6` rule. These cutoffs answer different descriptive questions and should not be merged into a single claim about coverage."""
    nb.cells[13].source = """raw_cutoff = scores.copy()
raw_cutoff["raw_quadrant"] = np.where(
    raw_cutoff.S_raw.isna(), "NA_S",
    np.where(raw_cutoff[list(FEATURES)].sum(axis=1) >= 5, "high_C", "low_C")
    + "_" + np.where(raw_cutoff.S_raw >= 6, "high_S", "low_S")
)
display(pd.concat([
    scores.quadrant.value_counts().rename("HA1_minmax_0.5"),
    raw_cutoff.raw_quadrant.value_counts().rename("fixed_raw_cutoff")
], axis=1).fillna(0).astype(int))
print("S=NA is excluded from both four-quadrant comparisons.")"""
    nb.cells[14].source = """## 5. Export

The derived CSV preserves all 40 rows, including the 15 with S=NA, and records raw and normalized values plus three composite weight settings. Plots are saved as PNGs. Exact score origins are documented in `data/final/feature_provenance_v2.csv`."""
    nb.cells[16].source = INTERPRETATION.read_text(encoding="utf-8")
    nbformat.write(nb, NOTEBOOK)


if __name__ == "__main__":
    main()
