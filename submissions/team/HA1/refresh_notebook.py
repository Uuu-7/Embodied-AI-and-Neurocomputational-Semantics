"""Keep the shared HA1 notebook aligned with the current working HA0 data."""

from pathlib import Path

import nbformat


HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE / "ha1_simulator.ipynb"
INTERPRETATION = HERE / "INTERPRETATION.md"
DATA = "data/final/spatial_relations_zh20_en20_v3_working.csv"


def main() -> None:
    nb = nbformat.read(NOTEBOOK, as_version=4)
    assert len(nb.cells) == 17
    nb.cells[0].source = """# HA1 — Graded abstractness simulator (team working draft)

This notebook runs on the instructor-accepted **20 Chinese + 20 English** working HA0 dataset in `data/final/spatial_relations_zh20_en20_v3_working.csv`. Xia Yuqi manually confirmed the selected lexical senses. The seven-feature score audit is AI-assisted and flags nine value-level questions for team discussion; no new independent human rating is claimed. The 25 numeric S paths are reported from prior work and have not been independently revalidated. Fifteen S values remain NA.

Run all cells from a directory inside the repository. The output table and figures are saved in `submissions/team/HA1/`. The HA0 table is in `submissions/team/HA0/`, and score-level reasons are in `data/reviews/feature_score_audit_v3.csv`."""
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
    nb.cells[3].source = nb.cells[3].source.replace("data/final/spatial_relations_zh20_en20_v2.csv", DATA)
    nb.cells[5].source = """## 2. C×S plane

Dashed boundaries are at 0.5 on the normalized axes. The graph shows 25 senses with reported S paths; 15 S=NA rows remain in the CSV and are excluded from the plot. The taxonomy sources still need independent sense-by-sense verification."""
    nb.cells[9].source = """## 4. Sensitivity and error analysis

The line plot varies w from 0 to 1 in steps of 0.1. A sense is weight-sensitive when A changes by more than 0.1 between w=0.2 and 0.8. Pair crossings count rank reversals. We also compare mean, sum, maximum, and active-channel C aggregation rules. Nine disputed feature cells are documented separately; their retained values are not team-adjudicated."""
    nb.cells[14].source = """## 5. Export

The CSV keeps all 40 senses, including 15 with S=NA, and records raw/normalized C and S plus three A weight settings. Two PNG figures and a sensitivity-detail CSV are also saved. The 280-value source and review audit remains in `data/reviews/feature_score_audit_v3.csv`."""
    nb.cells[16].source = INTERPRETATION.read_text(encoding="utf-8")
    for cell in nb.cells:
        if cell.cell_type == "code":
            cell.outputs = []
            cell.execution_count = None
    nbformat.write(nb, NOTEBOOK)


if __name__ == "__main__":
    main()
