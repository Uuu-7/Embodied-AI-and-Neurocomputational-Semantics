"""Compare the three independent candidate pools without selecting a final set."""

from __future__ import annotations

import csv
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MEMBERS = ("xiayuqi", "chenfengru", "hujinnan")
OUTPUT = ROOT / "data/audit"


def normalize(term: str, language: str) -> str:
    value = " ".join(unicodedata.normalize("NFKC", term).split())
    return value.casefold() if language == "EN" else value


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    nominations: list[dict[str, str]] = []
    for member in MEMBERS:
        path = ROOT / f"candidates/{member}/candidate_pool_zh20_en20_v01.csv"
        with path.open("r", encoding="utf-8-sig", newline="") as stream:
            rows = list(csv.DictReader(stream))
        if len(rows) != 40 or Counter(r["language"] for r in rows) != {"ZH": 20, "EN": 20}:
            raise ValueError(f"Expected 20 ZH and 20 EN nominations from {member}")
        if len({r["candidate_id"] for r in rows}) != 40:
            raise ValueError(f"Duplicate candidate ID in {member}")
        for row in rows:
            nominations.append(
                dict(
                    contributor=member,
                    candidate_id=row["candidate_id"],
                    language=row["language"],
                    term=row["term"],
                    normalized_term=normalize(row["term"], row["language"]),
                    part_of_speech=row["part_of_speech"],
                    target_sense_definition_en=row["target_sense_definition_en"],
                    subfamily=row["subfamily"],
                    image_schema_candidate=row["image_schema_candidate"],
                    metaphorical_extension_or_scope=row["metaphorical_extension_or_scope"],
                    lexical_source_reported=row["individual_lexical_source_verified"],
                    review_status=row["review_status"],
                )
            )

    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in nominations:
        grouped[(row["language"], row["normalized_term"])].append(row)
    counts = []
    for (language, normalized), rows in sorted(grouped.items()):
        contributors = [member for member in MEMBERS if any(r["contributor"] == member for r in rows)]
        if len(contributors) != len(rows):
            raise ValueError(f"A contributor nominated {language}:{normalized} twice")
        counts.append(
            dict(
                language=language,
                normalized_term=normalized,
                nomination_count=str(len(contributors)),
                contributors=";".join(contributors),
                source_candidate_ids=";".join(f"{r['contributor']}:{r['candidate_id']}" for r in rows),
                term_spellings=";".join(dict.fromkeys(r["term"] for r in rows)),
                sense_alignment="pending_review",
            )
        )
    if len(nominations) != 120 or len(counts) != 110:
        raise ValueError("Unexpected union size for the three proposals")
    write_csv(OUTPUT / "nomination_rows_v01.csv", list(nominations[0]), nominations)
    write_csv(OUTPUT / "term_vote_counts_v01.csv", list(counts[0]), counts)
    print("120 nomination rows; 110 language-specific normalized terms")
    print("Vote counts are surface-form overlaps until target senses are reviewed")


if __name__ == "__main__":
    main()
