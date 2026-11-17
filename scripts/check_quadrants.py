"""Report provisional C×S coverage from single-rater C and checked noun S."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/review/concepts_review_v03.csv"
OUTPUT = ROOT / "data/review/quadrant_counts_v01.csv"
PLOT = ROOT / "reports/pilot_cxs_feasibility_v01.png"
QUADRANTS = ("Low C / Low S", "Low C / High S", "High C / Low S", "High C / High S")


def main() -> None:
    with INPUT.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    mapped = [r for r in rows if r["S_evidence_status"] == "verified"]
    if len(mapped) != 15:
        raise ValueError("Expected 15 checked noun S values")
    counts = defaultdict(int)
    for row in mapped:
        c = "High C" if float(row["C_norm_0_1"]) >= 0.5 else "Low C"
        s = "High S" if float(row["S_norm_0_1"]) >= 0.5 else "Low S"
        for language in (row["language"], "ALL"):
            counts[(language, f"{c} / {s}")] += 1

    output_rows = []
    for language in ("ZH", "EN", "ALL"):
        n = sum(r["language"] == language or language == "ALL" for r in mapped)
        for quadrant in QUADRANTS:
            count = counts[(language, quadrant)]
            output_rows.append(
                dict(
                    language=language,
                    quadrant=quadrant,
                    count=str(count),
                    verified_S_rows=str(n),
                    target_minimum="3",
                    meets_target="YES" if count >= 3 else "NO",
                    C_status="single_rater_manual",
                    S_status="checked_OMW_noun_path",
                )
            )
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output_rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print(f"Wrote counts; matplotlib unavailable, so no plot at {PLOT}")
        return

    fig, axes = plt.subplots(1, 2, figsize=(11, 5), sharex=True, sharey=True)
    for ax, language, color in zip(axes, ("ZH", "EN"), ("#3567A3", "#C15C3D")):
        subset = [r for r in mapped if r["language"] == language]
        points = defaultdict(list)
        for row in subset:
            point = (float(row["C_norm_0_1"]), float(row["S_norm_0_1"]))
            points[point].append(row["concept_id"])
        for (x, y), ids in points.items():
            ax.scatter([x], [y], s=90 + 30 * (len(ids) - 1), color=color, alpha=0.8, edgecolor="white", linewidth=1)
            ax.annotate(", ".join(ids), (x, y), xytext=(5, 5), textcoords="offset points", fontsize=8)
        ax.axvline(0.5, color="#777777", linewidth=0.8, linestyle="--")
        ax.axhline(0.5, color="#777777", linewidth=0.8, linestyle="--")
        ax.set(xlim=(-0.05, 1.12), ylim=(-0.05, 1.08), title=f"{language}: {len(subset)} mapped, {20 - len(subset)} S=NA", xlabel="C normalized (single rater)")
        ax.grid(alpha=0.18)
        ax.text(0.02, 0.96, f"LL {counts[(language, 'Low C / Low S')]}  LH {counts[(language, 'Low C / High S')]}\nHL {counts[(language, 'High C / Low S')]}  HH {counts[(language, 'High C / High S')]}", transform=ax.transAxes, fontsize=9, va="top", bbox=dict(facecolor="white", alpha=0.85, edgecolor="none"))
    axes[0].set_ylabel("S normalized (checked noun depth)")
    fig.suptitle("Provisional C × S coverage: verified noun paths only", fontsize=13)
    fig.tight_layout()
    PLOT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(PLOT, dpi=180)
    plt.close(fig)
    print(f"Wrote {OUTPUT.relative_to(ROOT)} and {PLOT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
