"""Build the versioned AI-generated draft C/S annotations from CSV inputs."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/final/concepts_zh20_en20_v01.csv"
RATINGS = ROOT / "data/annotation/generated_ratings_v01.csv"
TAXONOMY = ROOT / "data/annotation/taxonomy_v01.csv"
OUTPUT = ROOT / "data/final/concepts_zh20_en20_v02.csv"
FEATURES = (
    "visual_0_2",
    "auditory_0_2",
    "tactile_0_2",
    "motor_0_2",
    "proprioceptive_0_2",
    "interoceptive_0_2",
    "social_0_2",
)
EXTRA_FIELDS = (
    "C_norm_0_1",
    "S_norm_0_1",
    "specificity_parent",
    "specificity_path",
    "specificity_method",
    "feature_confidence",
    "annotation_note",
    "example_provenance",
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def assert_unique(rows: list[dict[str, str]], key: str) -> None:
    counts = Counter(row[key] for row in rows)
    duplicates = [item for item, count in counts.items() if count != 1]
    if duplicates:
        raise ValueError(f"Duplicate {key}: {duplicates}")


def main() -> None:
    base = read_csv(BASE)
    ratings = read_csv(RATINGS)
    taxonomy = read_csv(TAXONOMY)
    assert_unique(base, "concept_id")
    assert_unique(ratings, "concept_id")
    assert_unique(taxonomy, "node_id")
    if len(base) != 40 or Counter(r["language"] for r in base) != {"ZH": 20, "EN": 20}:
        raise ValueError("Expected 20 Chinese and 20 English concepts")
    rating_by_id = {r["concept_id"]: r for r in ratings}
    if set(rating_by_id) != {r["concept_id"] for r in base}:
        raise ValueError("Ratings and selected concept IDs differ")

    parent = {r["node_id"]: r["parent_id"] for r in taxonomy}
    if parent.get("spatial_relation") != "":
        raise ValueError("The taxonomy must start at spatial_relation")

    def path_to_root(node: str) -> list[str]:
        result: list[str] = []
        while node:
            if node not in parent or node in result:
                raise ValueError(f"Missing parent or cycle at {node}")
            result.append(node)
            node = parent[node]
        result.reverse()
        if result[0] != "spatial_relation":
            raise ValueError(f"Disconnected taxonomy path: {result}")
        return result

    for node in parent:
        path_to_root(node)

    built: list[dict[str, str]] = []
    c_raw: dict[str, float] = {}
    s_raw: dict[str, int] = {}
    for source in base:
        row = dict(source)
        concept_id = row["concept_id"]
        annotation = rating_by_id[concept_id]
        scores = [int(annotation[field]) for field in FEATURES]
        if any(score not in (0, 1, 2) for score in scores):
            raise ValueError(f"Invalid 0-2 score: {concept_id}")
        if not annotation["annotation_note"] or annotation["confidence"] not in {"high", "medium", "low"}:
            raise ValueError(f"Missing annotation note or confidence: {concept_id}")
        example = annotation["example_sentence"]
        if row["term"].casefold() not in example.casefold():
            raise ValueError(f"Example omits target term: {concept_id}")
        route = path_to_root(annotation["specificity_parent"])
        c_raw[concept_id] = sum(scores) / 7
        s_raw[concept_id] = len(route)  # root has depth 0; concept is one edge below parent
        row.update({field: str(value) for field, value in zip(FEATURES, scores)})
        row.update(
            example_sentence=example,
            feature_provenance="generated",
            C_score=f"{c_raw[concept_id]:.4f}",
            S_score=str(s_raw[concept_id]),
            annotation_status="generated_unreviewed_pending_team_annotation",
            specificity_parent=annotation["specificity_parent"],
            specificity_path=" > ".join([*route, concept_id]),
            specificity_method="curated_taxonomy_edge_depth_v01",
            feature_confidence=annotation["confidence"],
            annotation_note=annotation["annotation_note"],
            example_provenance="generated",
        )
        built.append(row)

    c_min, c_max = min(c_raw.values()), max(c_raw.values())
    s_min, s_max = min(s_raw.values()), max(s_raw.values())
    if c_min == c_max or s_min == s_max:
        raise ValueError("Cannot min-max normalize a constant score")
    for row in built:
        concept_id = row["concept_id"]
        row["C_norm_0_1"] = f"{(c_raw[concept_id] - c_min) / (c_max - c_min):.4f}"
        row["S_norm_0_1"] = f"{(s_raw[concept_id] - s_min) / (s_max - s_min):.4f}"

    with BASE.open("r", encoding="utf-8-sig", newline="") as handle:
        fields = list(csv.DictReader(handle).fieldnames or [])
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields + list(EXTRA_FIELDS), lineterminator="\n")
        writer.writeheader()
        writer.writerows(built)
    print(f"Wrote {OUTPUT.relative_to(ROOT)}: {len(built)} rows")
    print(f"C mean range: {c_min:.4f}..{c_max:.4f}; S depth range: {s_min}..{s_max}")


if __name__ == "__main__":
    main()
