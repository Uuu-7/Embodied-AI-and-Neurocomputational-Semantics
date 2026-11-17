"""Create blank independent seven-channel forms for a reviewed pilot shortlist."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "data/audit/pilot_concept_audit_v01.csv"
OUT = ROOT / "data/audit/raters"
RATERS = ("xiayuqi", "chenfengru", "hujinnan")
FEATURES = ("visual", "auditory", "tactile", "motor", "proprioceptive", "interoceptive", "social")
FIELDS = ("rater", "pilot_id", "language", "term", "target_part_of_speech", "proposed_definition_en", "feature", "score_0_2", "provenance", "reason_or_source", "confidence")


def main() -> None:
    with PILOT.open("r", encoding="utf-8-sig", newline="") as stream:
        concepts = list(csv.DictReader(stream))
    if len(concepts) != 12 or len({r["pilot_id"] for r in concepts}) != 12:
        raise ValueError("Expected twelve distinct pilot concepts")
    OUT.mkdir(parents=True, exist_ok=True)
    for rater in RATERS:
        path = OUT / f"{rater}_pilot_v01.csv"
        if path.exists():
            with path.open("r", encoding="utf-8-sig", newline="") as stream:
                if any(r["score_0_2"] for r in csv.DictReader(stream)):
                    raise ValueError(f"Refusing to overwrite a started rating form: {path}")
        with path.open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=FIELDS, lineterminator="\n")
            writer.writeheader()
            for concept in concepts:
                for feature in FEATURES:
                    writer.writerow(
                        dict(
                            rater=rater,
                            pilot_id=concept["pilot_id"],
                            language=concept["language"],
                            term=concept["term"],
                            target_part_of_speech=concept["target_part_of_speech"],
                            proposed_definition_en=concept["proposed_definition_en"],
                            feature=feature,
                            score_0_2="",
                            provenance="",
                            reason_or_source="",
                            confidence="",
                        )
                    )
        print(f"Created {path.relative_to(ROOT)} with 84 blank decisions")


if __name__ == "__main__":
    main()
