"""Reproducible HA1 calculations for the selected spatial-relation senses."""

from __future__ import annotations

from itertools import combinations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


FEATURES = (
    "visual_0_2",
    "auditory_0_2",
    "tactile_0_2",
    "motor_0_2",
    "proprioceptive_0_2",
    "interoceptive_0_2",
    "social_0_2",
)


def load_inventory(path: Path) -> pd.DataFrame:
    data = pd.read_csv(path, dtype={"concept_id": str, "language": str, "term": str})
    if len(data) != 40 or data["language"].value_counts().to_dict() != {"ZH": 20, "EN": 20}:
        raise ValueError("Expected exactly 20 Chinese and 20 English senses")
    if data["concept_id"].duplicated().any():
        raise ValueError("concept_id must be unique")
    if data[list(FEATURES)].isna().any().any():
        raise ValueError("Every selected sense needs seven channel scores")
    if not data[list(FEATURES)].isin([0, 1, 2]).all().all():
        raise ValueError("Channel scores must be 0, 1, or 2")
    return data


def compute_c_raw(data: pd.DataFrame, aggregation: str = "mean") -> pd.Series:
    """Keep C separate from S; the default raw C is the mean of seven 0–2 scores."""
    profile = data.loc[:, FEATURES].astype(float)
    if aggregation == "mean":
        return profile.mean(axis=1).rename("C_raw")
    if aggregation == "sum":
        return profile.sum(axis=1).rename("C_raw")
    if aggregation == "max":
        return profile.max(axis=1).rename("C_raw")
    if aggregation == "active_count":
        return profile.gt(0).sum(axis=1).astype(float).rename("C_raw")
    raise ValueError("aggregation must be mean, sum, max, or active_count")


def compute_s_raw(data: pd.DataFrame) -> pd.Series:
    """Count root-to-sense hypernym edges; unsupported paths remain NaN."""
    depths = []
    for row in data.itertuples(index=False):
        path = row.S_taxonomy_path
        reported = row.S_depth
        if pd.isna(path) or not str(path).strip():
            if not pd.isna(reported):
                raise ValueError(f"{row.concept_id}: S depth without taxonomy path")
            depths.append(np.nan)
            continue
        edges = len([node.strip() for node in str(path).split(">") if node.strip()]) - 1
        if pd.isna(reported) or edges != int(reported):
            raise ValueError(f"{row.concept_id}: path depth differs from reported S")
        depths.append(float(edges))
    return pd.Series(depths, index=data.index, name="S_raw")


def minmax_scale(values: pd.Series, name: str) -> pd.Series:
    """Scale observed, nonmissing values to [0, 1], preserving missing S."""
    valid = values.dropna().astype(float)
    if valid.empty or valid.max() == valid.min():
        raise ValueError(f"{name}: min–max scaling is undefined for these values")
    return ((values.astype(float) - valid.min()) / (valid.max() - valid.min())).rename(name)


def prepare_scores(data: pd.DataFrame, c_aggregation: str = "mean") -> pd.DataFrame:
    result = data.copy()
    result["C_raw"] = compute_c_raw(result, c_aggregation)
    result["S_raw"] = compute_s_raw(result)
    result["C_norm"] = minmax_scale(result["C_raw"], "C_norm")
    result["S_norm"] = minmax_scale(result["S_raw"], "S_norm")
    result["quadrant"] = np.where(
        result["S_norm"].isna(),
        "NA_S",
        np.where(result["C_norm"] >= 0.5, "high_C", "low_C")
        + "_"
        + np.where(result["S_norm"] >= 0.5, "high_S", "low_S"),
    )
    return result


def abstractness(scores: pd.DataFrame, w: float) -> pd.Series:
    """A(w) = w(1-C_norm) + (1-w)(1-S_norm); S=NA stays missing."""
    if not 0 <= w <= 1:
        raise ValueError("w must be between 0 and 1")
    return (w * (1 - scores["C_norm"]) + (1 - w) * (1 - scores["S_norm"])).rename(
        f"A_{w:.1f}"
    )


def add_weight_settings(scores: pd.DataFrame) -> pd.DataFrame:
    result = scores.copy()
    for weight in (0.2, 0.5, 0.8):
        result[f"A_{weight:.1f}"] = abstractness(result, weight)
    return result


def scatter_plot(scores: pd.DataFrame, output: Path) -> None:
    valid = scores.dropna(subset=["S_norm"])
    groups = list(valid.groupby(["C_norm", "S_norm"], sort=True))
    fig, (ax, key) = plt.subplots(1, 2, figsize=(15, 8),
                                  gridspec_kw={"width_ratios": [1.7, 1]},
                                  constrained_layout=True)
    key_lines = ["ID      (C, S)    Concept IDs", ""]
    for n, ((x, y), part) in enumerate(groups, 1):
        group_id = f"G{n:02d}"
        languages = set(part["language"])
        color = "#2465a5" if languages == {"ZH"} else "#d4772a" if languages == {"EN"} else "#7856a4"
        ax.scatter([x], [y], s=100 + 45 * (len(part) - 1), color=color,
                   edgecolors="white", linewidths=0.8, zorder=3)
        ax.annotate(group_id, (x, y), xytext=(6, 6), textcoords="offset points",
                    fontsize=8, color="#263238")
        ids = ", ".join(part["concept_id"])
        key_lines.append(f"{group_id}   ({x:.1f}, {y:.1f})   {ids}")
    ax.axvline(0.5, color="#555", linestyle="--", linewidth=1)
    ax.axhline(0.5, color="#555", linestyle="--", linewidth=1)
    ax.set(xlim=(-0.06, 1.12), ylim=(-0.06, 1.08), xlabel="C normalized (min–max)",
           ylabel="S normalized (min–max)", title=f"C × S: {len(valid)} reported paths")
    ax.grid(alpha=0.18)
    key.axis("off")
    key.text(0, 1, "\n".join(key_lines), va="top", ha="left", fontsize=9,
             fontfamily="monospace", linespacing=1.5)
    key.text(0, 0.05, "Blue: Chinese     Orange: English     Purple: shared coordinates\n"
             "Point size indicates how many concepts share a coordinate.\n"
             f"{scores['S_norm'].isna().sum()} S=NA rows are excluded from this plot.",
             va="bottom", fontsize=9)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=170, bbox_inches="tight")
    plt.close(fig)


def weight_sensitivity_plot(scores: pd.DataFrame, output: Path) -> None:
    valid = scores.dropna(subset=["S_norm"])
    weights = np.linspace(0, 1, 11)
    fig, axes = plt.subplots(1, 2, figsize=(16, 8), sharey=True, constrained_layout=True)
    for ax, language in zip(axes, ("ZH", "EN")):
        part = valid.loc[valid["language"] == language]
        colors = plt.cm.tab20(np.linspace(0, 1, len(part)))
        for color, row in zip(colors, part.itertuples(index=False)):
            values = [w * (1 - row.C_norm) + (1 - w) * (1 - row.S_norm) for w in weights]
            ax.plot(weights, values, label=row.concept_id, color=color, linewidth=1.7)
        ax.set(title=f"{language} ({len(part)} senses)", xlabel="Weight w on (1 − C)",
               xlim=(0, 1), ylim=(-0.02, 1.02))
        ax.grid(alpha=0.2)
        ax.legend(title="Concept ID", loc="center left", bbox_to_anchor=(1.01, 0.5),
                  fontsize=8, frameon=False)
    axes[0].set_ylabel("Composite abstractness A(w)")
    fig.suptitle("Weight sensitivity: one line per concept with a reported S path")
    fig.text(0.5, 0.01, "Some concepts have identical C and S profiles, so their lines coincide.",
             ha="center", fontsize=9)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=170, bbox_inches="tight")
    plt.close(fig)


def crossing_pairs(scores: pd.DataFrame, low_weight: float = 0.2, high_weight: float = 0.8):
    valid = scores.dropna(subset=["S_norm"]).set_index("concept_id")
    first = abstractness(valid, low_weight)
    last = abstractness(valid, high_weight)
    crossing = []
    for left, right in combinations(valid.index, 2):
        delta_first = first.loc[left] - first.loc[right]
        delta_last = last.loc[left] - last.loc[right]
        if delta_first * delta_last < -1e-10:
            crossing.append((left, right))
    return crossing
