"""Build the versioned HA0/HA1 submission input from the preserved v3 review."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
V3 = ROOT / "data/final/spatial_relations_zh20_en20_v3_working.csv"
V4 = ROOT / "data/final/spatial_relations_zh20_en20_v4_ha1.csv"
PARENTS_V3 = ROOT / "data/final/category_parent_nodes_v1.csv"
PARENTS_V4 = ROOT / "data/final/category_parent_nodes_v2.csv"
AUDIT_V3 = ROOT / "data/reviews/feature_score_audit_v3.csv"
AUDIT_V4 = ROOT / "data/reviews/feature_score_audit_v4.csv"
HA0 = ROOT / "submissions/team/HA0/ha0_zh20_en20.csv"
OXFORD = "https://www.oxfordlearnersdictionaries.com/definition/english/across_1"
CHEN_REVIEW = "https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/17#issuecomment-6976080360"
CHEN_PARENT = "https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/17#issuecomment-6976372653"
FEATURES = (
    "visual_0_2", "auditory_0_2", "tactile_0_2", "motor_0_2",
    "proprioceptive_0_2", "interoceptive_0_2", "social_0_2",
)
CHANGES = {
    ("ZH02", "proprioceptive_0_2"): (0, "A static interior region does not entail a body-position cue."),
    ("ZH03", "proprioceptive_0_2"): (0, "A static exterior region does not entail a body-position cue."),
    ("EN12", "proprioceptive_0_2"): (0, "Static containment does not entail a body-position cue."),
    ("EN15", "motor_0_2"): (2, "The narrowed crossing sense directly involves movement through the region."),
}
CHANGED_NOTES = {
    "ZH02": "Static interior region: Visual=2, Tactile=1 if a physical boundary is present, Motor=0, Proprioceptive=0 because no body-position cue is entailed.",
    "ZH03": "Static exterior region: Visual=2, Tactile=1 conditionally for a physical boundary, Motor=0, Proprioceptive=0 because no body-position cue is entailed.",
    "EN12": "Static inside relation: Visual=2, Tactile=1 conditionally for an enclosing physical surface, Motor=0, Proprioceptive=0 because no body-position cue is entailed.",
    "EN15": "Crossing sense: Visual=2, Motor=2 for movement across a region, Proprioceptive=1 for conditional body-relative feedback; S remains NA without a defensible taxonomic path.",
}
RETAINED = {
    ("ZH16", "proprioceptive_0_2"): "A route can conditionally guide egocentric orientation; traversal is not entailed, so Motor remains 0.",
    ("EN17", "proprioceptive_0_2"): "A route can conditionally guide egocentric orientation; traversal is not entailed, so Motor remains 0.",
    ("EN11", "proprioceptive_0_2"): "Body or robot joint-position feedback directly realizes posture; the robot is an engineering analogue.",
    ("ZH18", "tactile_0_2"): "Tactile contact is conditional in a material realization; ideal geometric tangency alone does not entail touch.",
    ("EN15", "proprioceptive_0_2"): "Body-relative feedback can conditionally accompany crossing, but is not required for every traversal.",
}


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def write(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    inventory = read(V3)
    ha0 = read(HA0)
    audit = read(AUDIT_V3)
    parents = read(PARENTS_V3)
    assert len(inventory) == len(ha0) == 40 and len(audit) == 280
    assert {row["concept_id"] for row in inventory} == {row["concept_id"] for row in ha0}

    definitions = {
        "spatial_arrangement": "A spatial configuration or geometric property of surfaces, lines, entities, or body parts.",
        "spatial_interval_relation": "A measurable or perceptible separation or opening between entities.",
    }
    for parent in parents:
        if parent["category_parent"] in definitions:
            parent["definition_en"] = definitions[parent["category_parent"]]
        parent["selection_status"] = "HA1_submission_editorial_choice; team_signoff_not_recorded"
    write(PARENTS_V4, parents)
    parent_definitions = {row["category_parent"]: row["definition_en"] for row in parents}

    for row in inventory:
        cid = row["concept_id"]
        if cid == "EN15":
            row["target_sense_definition_en"] = (
                "From one side of a spatial region to the other along a path that crosses it."
            )
            row["target_definition_origin"] = f"editorial_narrowing_after_Chen_review; Oxford crossing sense: {OXFORD}"
            row["lexical_check_status"] = "Oxford_crossing_sense_checked; new_wording_not_separately_human_confirmed"
            row["lexical_review_source"] = OXFORD
            row["uncertainty_note"] = ""
        if cid == "ZH18":
            row["uncertainty_note"] = (
                "Geometric tangency can be idealized without material touch; Tactile=1 assumes a possible physical instance."
            )
        for feature in FEATURES:
            decision = CHANGES.get((cid, feature))
            if decision:
                row[feature] = str(decision[0])
        total = sum(int(row[feature]) for feature in FEATURES)
        row["C_sum"] = str(total)
        row["C_unit"] = f"{total / 14:.6f}"
        row["C_S_quadrant_reference"] = (
            "NA_S" if not row["S_depth"] else
            ("high_C" if total >= 5 else "low_C") + "_" +
            ("high_S" if int(row["S_depth"]) >= 6 else "low_S")
        )
        row["C_rating_status"] = "HA1_submission_editorial_adjudication; team_signoff_not_recorded"
        row["C_audit_status"] = "nine_review_flags_resolved_for_HA1; see_feature_score_audit_v4"
        row["category_parent_status"] = "HA1_submission_editorial_choice; team_signoff_not_recorded"
        if cid in CHANGED_NOTES:
            row["C_rating_note"] = CHANGED_NOTES[cid]
            row["C_rating_source"] += "; Chen PR17 review; HA1 editorial decision"
            row["C_rating_confidence"] = "medium"
    write(V4, inventory)

    by_id = {row["concept_id"]: row for row in inventory}
    for row in audit:
        key = (row["concept_id"], row["feature"])
        concept = by_id[key[0]]
        row["target_definition_en"] = concept["target_sense_definition_en"]
        row["reviewed_score"] = concept[key[1]]
        if key in CHANGES:
            row["score_disagreement_status"] = "adopted_for_HA1_submission"
            row["provenance_label"] = "generated"
            row["provenance_detail"] = "editorial_adjudication_after_Chen_PR17_review"
            row["source"] = CHEN_REVIEW + (f"; {OXFORD}" if key[0] == "EN15" else "")
            row["source_limit"] = "Reviewed proposal adopted for HA1; independent three-person agreement not recorded."
            row["reason_or_source"] = CHANGES[key][1]
            row["confidence"] = "medium"
        elif key in RETAINED:
            row["score_disagreement_status"] = "retained_with_explicit_reason_for_HA1"
            row["reason_or_source"] = RETAINED[key]
            row["source"] += "; " + CHEN_REVIEW
            row["confidence"] = "low" if key[0] in {"ZH16", "ZH18", "EN17"} else "medium"
        else:
            row["score_disagreement_status"] = "retained_no_PR17_change_proposed"
        row["reviewer_status"] = "HA1_editorial_review; no_independent_three_rater_claim"
    write(AUDIT_V4, audit)

    for row in ha0:
        cid = row["concept_id"]
        concept = by_id[cid]
        row["definition_en"] = concept["target_sense_definition_en"]
        if cid == "EN15":
            row["definition_provenance"] = "generated"
            row["definition_source"] = concept["lexical_review_source"]
            row["definition_original_source"] = concept["target_definition_origin"]
        row["category_parent_definition"] = parent_definitions[row["category_parent"]]
        row["category_parent_source"] = CHEN_PARENT + "; editorial application to HA1"
        row["uncertainty_note"] = concept["uncertainty_note"]
        row["review_status"] = "HA1_submission_aligned; team_signoff_not_recorded"
        for feature in FEATURES:
            short = feature.removesuffix("_0_2")
            row[feature] = concept[feature]
            key = (cid, feature)
            if key in CHANGES:
                row[short + "_provenance"] = "generated"
                row[short + "_source"] = CHEN_REVIEW + (f"; {OXFORD}" if cid == "EN15" else "")
                row[short + "_confidence"] = "medium"
    write(HA0, ha0)
    print("Built 40 HA0/HA1 input rows, 280 reviewed score records, and 12 parent nodes.")


if __name__ == "__main__":
    main()
