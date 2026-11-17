"""Create independent, initially blank seven-channel pilot forms for the team."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/final/concepts_zh20_en20_v01.csv"
PILOT = ROOT / "data/review/pilot_concept_audit_v01.csv"
OUT = ROOT / "data/review/raters"
FEATURES = ("visual", "auditory", "tactile", "motor", "proprioceptive", "interoceptive", "social")
RATERS = ("xiayuqi", "chenfengru", "hujinnan")
FIELDS = ("rater", "concept_id", "term", "language", "definition_en", "feature", "score_0_2", "provenance", "reason", "confidence")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    concepts = {r["concept_id"]: r for r in read_csv(DATA)}
    pilot = read_csv(PILOT)
    if len(pilot) != 12 or len({r["concept_id"] for r in pilot}) != 12:
        raise ValueError("Expected 12 distinct pilot concepts")
    OUT.mkdir(parents=True, exist_ok=True)
    for rater in RATERS:
        path = OUT / f"{rater}_pilot_v01.csv"
        if path.exists():
            existing = read_csv(path)
            if any(r["score_0_2"] for r in existing):
                print(f"Kept started form: {path.relative_to(ROOT)}")
                continue
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
            writer.writeheader()
            for item in pilot:
                c = concepts[item["concept_id"]]
                for feature in FEATURES:
                    writer.writerow(
                        dict(
                            rater=rater,
                            concept_id=c["concept_id"],
                            term=c["term"],
                            language=c["language"],
                            definition_en=item.get("proposed_definition_en") or c["definition_en"],
                            feature=feature,
                            score_0_2="",
                            provenance="",
                            reason="",
                            confidence="",
                        )
                    )
        print(f"Created {path.relative_to(ROOT)}: {len(pilot) * len(FEATURES)} blank decisions")


if __name__ == "__main__":
    main()
