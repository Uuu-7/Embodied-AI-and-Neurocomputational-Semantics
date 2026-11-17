"""Verify noun senses against pinned Wordnets and build the review dataset.

Install wn==1.1.1 and the omw-en:2.0 and cow:1.1 lexicons first.
The script never treats a different part of speech as a noun match.
"""

from __future__ import annotations

import csv
from pathlib import Path

import wn


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/final/concepts_zh20_en20_v02.csv"
DECISIONS = ROOT / "data/review/sense_decisions_v01.csv"
PATHS = ROOT / "data/review/taxonomic_paths_v01.csv"
OUTPUT = ROOT / "data/review/concepts_review_v03.csv"
ENTITY = "omw-en-00001740-n"


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    base_fields, base = read_csv(BASE)
    _, decisions = read_csv(DECISIONS)
    if len(base) != 40 or len(decisions) != 40:
        raise ValueError("Expected forty selected concepts and forty decisions")
    selected = {r["concept_id"]: r for r in base}
    decided = {r["concept_id"]: r for r in decisions}
    if len(selected) != 40 or len(decided) != 40 or selected.keys() != decided.keys():
        raise ValueError("Review IDs are duplicated or do not match the selected set")

    english = wn.Wordnet("omw-en:2.0")
    chinese = wn.Wordnet("cow:1.1")
    path_rows: list[dict[str, str]] = []
    reviewed: list[dict[str, str]] = []
    depths: dict[str, int] = {}
    for source in base:
        row = dict(source)
        concept_id = row["concept_id"]
        decision = decided[concept_id]
        status = decision["decision"]
        if status not in {"verified", "NA"} or not decision["reason"]:
            raise ValueError(f"Invalid review decision for {concept_id}")
        row.update(
            S_evidence_status=status,
            S_source_synset_id=decision["source_synset_id"],
            S_shared_english_synset_id=decision["shared_english_synset_id"],
            S_review_reason=decision["reason"],
            annotation_status="manual_C_pending_three_rater_review",
        )
        if status == "NA":
            if decision["source_synset_id"] or decision["shared_english_synset_id"]:
                raise ValueError(f"NA row retains a synset: {concept_id}")
            row.update(
                S_score="NA",
                S_norm_0_1="NA",
                specificity_parent="",
                specificity_path="",
                specificity_method="no_comparable_verified_noun_path",
            )
        else:
            if row["language"] == "ZH":
                lexicon = chinese
                if decision["source_lexicon"] != "cow:1.1":
                    raise ValueError(f"Wrong source lexicon for {concept_id}")
            else:
                lexicon = english
                if decision["source_lexicon"] != "omw-en:2.0":
                    raise ValueError(f"Wrong source lexicon for {concept_id}")
            source_synset = lexicon.synset(decision["source_synset_id"])
            shared_synset = english.synset(decision["shared_english_synset_id"])
            if source_synset.id not in {s.id for s in lexicon.synsets(row["term"], pos="n")}:
                raise ValueError(f"The term lacks the recorded noun sense: {concept_id}")
            if source_synset.ili != shared_synset.ili:
                raise ValueError(f"Chinese and English ILIs differ: {concept_id}")
            if source_synset.pos != "n" or shared_synset.pos != "n":
                raise ValueError(f"Non-noun sense in S audit: {concept_id}")
            paths = shared_synset.hypernym_paths()
            if not paths:
                raise ValueError(f"No hypernym path: {concept_id}")
            best = min(paths, key=lambda path: (len(path), [s.id for s in path]))
            if best[-1].id != ENTITY:
                raise ValueError(f"Path does not reach entity: {concept_id}")
            complete = [shared_synset, *best]
            depth = len(best)
            if depth != shared_synset.min_depth():
                raise ValueError(f"Inconsistent noun depth: {concept_id}")
            depths[concept_id] = depth
            row.update(
                S_score=str(depth),
                specificity_parent=best[0].id,
                specificity_path=" > ".join(s.id for s in complete),
                specificity_method="omw_en_2_0_shortest_noun_hypernym_to_entity",
            )
            path_rows.append(
                dict(
                    concept_id=concept_id,
                    term=row["term"],
                    source_lexicon=decision["source_lexicon"],
                    source_synset_id=source_synset.id,
                    source_gloss=source_synset.definition() or "",
                    shared_english_synset_id=shared_synset.id,
                    shared_english_gloss=shared_synset.definition() or "",
                    S_depth=str(depth),
                    hypernym_path_ids=" > ".join(s.id for s in complete),
                    hypernym_path_lemmas=" > ".join(s.lemmas()[0] if s.lemmas() else "" for s in complete),
                )
            )
        reviewed.append(row)

    if len(depths) != 15:
        raise ValueError(f"Expected 15 independently checked noun paths; got {len(depths)}")
    lo, hi = min(depths.values()), max(depths.values())
    if lo == hi:
        raise ValueError("Cannot normalize a constant noun depth")
    for row in reviewed:
        if row["concept_id"] in depths:
            row["S_norm_0_1"] = f"{(depths[row['concept_id']] - lo) / (hi - lo):.4f}"

    write_csv(
        PATHS,
        ["concept_id", "term", "source_lexicon", "source_synset_id", "source_gloss", "shared_english_synset_id", "shared_english_gloss", "S_depth", "hypernym_path_ids", "hypernym_path_lemmas"],
        path_rows,
    )
    write_csv(
        OUTPUT,
        base_fields + ["S_evidence_status", "S_source_synset_id", "S_shared_english_synset_id", "S_review_reason"],
        reviewed,
    )
    print(f"Verified noun S paths: {len(depths)}; NA: {len(reviewed) - len(depths)}; depth: {lo}..{hi}")


if __name__ == "__main__":
    main()
