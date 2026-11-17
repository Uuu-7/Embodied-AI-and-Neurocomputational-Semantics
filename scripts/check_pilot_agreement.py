"""Validate three independent pilot forms and calculate quadratic weighted kappa."""

from __future__ import annotations

import csv
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "data/review/pilot_concept_audit_v01.csv"
FORMS = ROOT / "data/review/raters"
RATERS = ("xiayuqi", "chenfengru", "hujinnan")
FEATURES = ("visual", "auditory", "tactile", "motor", "proprioceptive", "interoceptive", "social")
RESULT = ROOT / "data/review/pilot_agreement_v01.csv"
DISAGREEMENTS = ROOT / "data/review/pilot_disagreements_v01.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def kappa(a: list[int], b: list[int]) -> tuple[str, str]:
    n = len(a)
    exact = sum(x == y for x, y in zip(a, b)) / n
    observed = sum((x - y) ** 2 / 4 for x, y in zip(a, b)) / n
    left = [a.count(k) / n for k in (0, 1, 2)]
    right = [b.count(k) / n for k in (0, 1, 2)]
    expected = sum(left[i] * right[j] * (i - j) ** 2 / 4 for i in range(3) for j in range(3))
    return (f"{1 - observed / expected:.4f}" if expected else "NA", f"{exact:.4f}")


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    pilot_ids = {r["concept_id"] for r in read_csv(PILOT)}
    expected = {(concept_id, feature) for concept_id in pilot_ids for feature in FEATURES}
    if len(pilot_ids) != 12:
        raise ValueError("Pilot list must contain 12 distinct concepts")
    forms: dict[str, dict[tuple[str, str], dict[str, str]]] = {}
    pending: list[str] = []
    for rater in RATERS:
        rows = read_csv(FORMS / f"{rater}_pilot_v01.csv")
        keyed = {(r["concept_id"], r["feature"]): r for r in rows}
        if len(rows) != 84 or set(keyed) != expected:
            raise ValueError(f"Pilot coverage or duplicate-key error for {rater}")
        for key, row in keyed.items():
            if row["rater"] != rater:
                raise ValueError(f"Rater ID mismatch for {rater}: {key}")
            if not row["score_0_2"]:
                pending.append(f"{rater}:{key[0]}:{key[1]}")
                continue
            if row["score_0_2"] not in {"0", "1", "2"}:
                raise ValueError(f"Invalid score for {rater}: {key}")
            if row["provenance"] not in {"sourced", "manual", "generated"}:
                raise ValueError(f"Missing provenance for {rater}: {key}")
            if row["confidence"] not in {"high", "medium", "low"} or not row["reason"].strip():
                raise ValueError(f"Missing reason or confidence for {rater}: {key}")
        forms[rater] = keyed
    if pending:
        print(f"Agreement pending: {len(pending)} of 252 scores are blank. No kappa computed.")
        return

    agreement: list[dict[str, str]] = []
    differences: list[dict[str, str]] = []
    for left_name, right_name in combinations(RATERS, 2):
        for feature in (*FEATURES, "ALL"):
            keys = sorted(k for k in expected if k[1] == feature or feature == "ALL")
            left = [int(forms[left_name][k]["score_0_2"]) for k in keys]
            right = [int(forms[right_name][k]["score_0_2"]) for k in keys]
            weighted, exact = kappa(left, right)
            agreement.append(dict(rater_a=left_name, rater_b=right_name, feature=feature, n=str(len(keys)), quadratic_weighted_kappa=weighted, exact_agreement=exact))
            if feature == "ALL":
                for key, x, y in zip(keys, left, right):
                    if x != y:
                        differences.append(dict(concept_id=key[0], feature=key[1], rater_a=left_name, score_a=str(x), rater_b=right_name, score_b=str(y)))
    write_csv(RESULT, ["rater_a", "rater_b", "feature", "n", "quadratic_weighted_kappa", "exact_agreement"], agreement)
    write_csv(DISAGREEMENTS, ["concept_id", "feature", "rater_a", "score_a", "rater_b", "score_b"], differences)
    print(f"Agreement ready: {len(agreement)} comparisons; {len(differences)} pairwise disagreements")


if __name__ == "__main__":
    main()
