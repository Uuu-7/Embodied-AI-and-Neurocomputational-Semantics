"""Synchronize the submitted HA1 notebook with its versioned source and commentary."""

from pathlib import Path

import nbformat


HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE / "ha1_simulator.ipynb"
INTERPRETATION = HERE / "INTERPRETATION.md"
DATA = "data/final/spatial_relations_zh20_en20_v4_ha1.csv"


def main() -> None:
    nb = nbformat.read(NOTEBOOK, as_version=4)
    assert len(nb.cells) == 17
    nb.cells[0].source = """# HA1 — Graded abstractness simulator

**Submission version, 20 Chinese + 20 English selected senses.** This executed notebook uses `data/final/spatial_relations_zh20_en20_v4_ha1.csv`, aligned with the HA0 export. Xia Yuqi confirmed the original lexical inventory; the narrowed EN15 crossing wording is an editorial decision checked against Oxford Learner's Dictionaries. Nine feature questions from the earlier audit have explicit decisions in `data/reviews/feature_score_audit_v4.csv`, informed by Chen Fengru's PR17 review. This is not a claim of three independent human ratings or team sign-off.

Twenty-five S paths are carried from earlier work and their edge counts are checked here. Fifteen senses without a defensible path remain S=NA. The inherited paths have **not** all been independently checked against source synsets. Run all cells from within the repository to regenerate the score tables and figures. See `submissions/team/HA0/` for the input table and rubric, and `submissions/team/HA1/INTERPRETATION.md` for the interpretation."""
    nb.cells[1].source = f"""from pathlib import Path
import platform, sys
import numpy as np
import pandas as pd
from IPython.display import display, Image

current = Path.cwd().resolve()
repo = next((p for p in (current, *current.parents)
             if (p / {DATA!r}).is_file()), None)
if repo is None:
    raise FileNotFoundError("Open this notebook inside the repository or run it from its root")
work = repo / "submissions/team/HA1"
sys.path.insert(0, str(work))
from ha1_model import (
    FEATURES, abstractness, add_weight_settings, compute_c_raw, compute_s_raw,
    crossing_pairs, load_inventory, prepare_scores, scatter_plot, weight_sensitivity_plot
)
print("Python", platform.python_version(), "| NumPy", np.__version__,
      "| pandas", pd.__version__)
"""
    nb.cells[2].source = """## 1. Separate C and S

`C_raw` is the **mean** of the seven 0–2 scores. `S_raw` counts edges in a reported root-to-sense path. A missing path stays **NA**. Both measures receive dataset-level min–max scaling; adding or changing senses can move existing normalized coordinates."""
    nb.cells[3].source = 'inventory = load_inventory(repo / "' + DATA + '")' + nb.cells[3].source.split(')', 1)[1]
    nb.cells[5].source = """## 2. C×S plane

Dashed boundaries are at 0.5 on the normalized axes. The graph shows 25 senses with reported S paths; 15 S=NA rows remain in the CSV and are excluded from the plot. The path lengths are reproducible from the recorded node sequences; sense-to-synset matching remains an evidence limit."""
    nb.cells[7].source = """## 3. Adjustable composite

`show_weight(w)` accepts any weight from 0 to 1 and keeps normalized C and S alongside `A(w)=w(1−C)+(1−w)(1−S)`. The scored exports include w=0.2, 0.5, and 0.8. The slider works in a live Jupyter session; the static table below remains readable on GitHub."""
    nb.cells[8].source = """def show_weight(w=0.5, top_n=10):
    table = scores[["concept_id", "language", "term", "C_norm", "S_norm"]].copy()
    table["A"] = abstractness(scores, w)
    return table.dropna(subset=["A"]).sort_values("A", ascending=False).head(top_n)

display(show_weight(0.5))
try:
    from ipywidgets import interact, FloatSlider
    interact(show_weight, w=FloatSlider(value=0.5, min=0, max=1, step=0.1,
                                        description="C weight"), top_n=(5, 25, 5))
except ImportError:
    print("Install ipywidgets for the live slider; show_weight(w) works without it.")
"""
    nb.cells[9].source = """## 4. Sensitivity and error analysis

The line plot varies w from 0 to 1 in steps of 0.1. A sense is called weight-sensitive when A changes by more than 0.1 between w=0.2 and 0.8; this is a descriptive threshold. Pair crossings count rank reversals. Mean, sum, maximum, and active-channel C aggregation rules expose model dependence. Nine earlier feature questions have recorded editorial decisions in `data/reviews/feature_score_audit_v4.csv`."""
    nb.cells[11].source = """sum_scaled = prepare_scores(inventory, c_aggregation="sum")
max_scaled = prepare_scores(inventory, c_aggregation="max")
active_scaled = prepare_scores(inventory, c_aggregation="active_count")
print("Mean vs sum normalized C, largest absolute difference:",
      (scores.C_norm - sum_scaled.C_norm).abs().max())
print("Max aggregation unique raw values:", sorted(compute_c_raw(inventory, "max").unique()))
print("Quadrant changes with max-channel C:",
      (scores.quadrant != max_scaled.quadrant).sum())
print("Mean vs active-channel-count Spearman rho:",
      scores.C_norm.corr(active_scaled.C_norm, method="spearman"))
print("Quadrant changes with active-channel-count C:",
      (scores.quadrant != active_scaled.quadrant).sum())
print("A(0.5) rank association with C-only:",
      scores["A_0.5"].corr(abstractness(scores, 1), method="spearman"))
print("A(0.5) rank association with S-only:",
      scores["A_0.5"].corr(abstractness(scores, 0), method="spearman"))
"""
    nb.cells[14].source = """## 5. Export

The CSV keeps all 40 senses, including 15 with S=NA, and records raw/normalized C and S plus three A weight settings. Two PNG figures and a sensitivity-detail CSV are also saved. Every channel score and its reason appears in the 280-row `data/reviews/feature_score_audit_v4.csv`."""
    nb.cells[16].source = INTERPRETATION.read_text(encoding="utf-8")
    for cell in nb.cells:
        if cell.cell_type == "code":
            cell.outputs = []
            cell.execution_count = None
    nbformat.write(nb, NOTEBOOK)


if __name__ == "__main__":
    main()
