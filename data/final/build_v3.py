"""Build the shared HA0 data and an explicit, provisional 280-value C audit."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "data/final/spatial_relations_zh20_en20_v2.csv"
PROVENANCE = ROOT / "data/final/feature_provenance_v2.csv"
V3 = ROOT / "data/final/spatial_relations_zh20_en20_v3_working.csv"
PARENTS = ROOT / "data/final/category_parent_nodes_v1.csv"
AUDIT = ROOT / "data/reviews/feature_score_audit_v3.csv"
HA0 = ROOT / "submissions/team/HA0/ha0_zh20_en20.csv"

FEATURES = (
    "visual_0_2", "auditory_0_2", "tactile_0_2", "motor_0_2",
    "proprioceptive_0_2", "interoceptive_0_2", "social_0_2",
)

# These pedagogical parent nodes are deliberately separate from the external
# COW/OMW paths used for S. Each selected sense receives exactly one parent.
PARENT_BY_FAMILY = {
    "position": ("spatial_location", "A place specified relative to a reference space."),
    "containment": ("bounded_region_relation", "A location defined by being within or beyond an enclosing boundary."),
    "boundary": ("spatial_limit", "A spatial divider that marks where a region ends."),
    "center_periphery": ("reference_point_relation", "A position determined by a figure's extent or limits."),
    "orientation": ("oriented_location", "A place specified using a direction, axis, or viewpoint."),
    "betweenness": ("intervening_region_relation", "A region located with respect to two bounding references."),
    "distance": ("spatial_interval_relation", "A measurable or perceptible separation between entities."),
    "configuration": ("spatial_arrangement", "An arrangement of surfaces, lines, entities, or body parts."),
    "path": ("route_or_traversal_relation", "A route or cross-region relation, whether static or traversed."),
    "contact": ("nearness_or_touch_relation", "A relation of immediate nearness or surface meeting."),
    "force_support": ("load_or_stability_relation", "A force or bodily-stability relation that resists displacement."),
}

# Score alternatives are review questions, not silent changes to the dataset.
FLAGS = {
    ("ZH02", "proprioceptive_0_2"): ("0", "A region exists without a body; decide whether optional body-inside experience warrants 1."),
    ("ZH03", "proprioceptive_0_2"): ("0", "An exterior region exists without a body; decide whether embodied viewpoint warrants 1."),
    ("ZH16", "proprioceptive_0_2"): ("0", "The route noun does not entail a traveler; distinguish potential traversal from direct grounding."),
    ("ZH18", "tactile_0_2"): ("0", "A geometrical tangent can be defined without felt contact; 1 depends on material realization."),
    ("EN11", "proprioceptive_0_2"): ("0", "The robot example uses joint sensors as an analogue; decide whether the C rubric includes this analogue."),
    ("EN12", "proprioceptive_0_2"): ("0", "A containment relation exists without a body; optional embodied use may justify 1."),
    ("EN15", "motor_0_2"): ("0 or 2", "The confirmed definition allows static 'on' and directional 'toward' readings; fix a scoring policy for the mixture."),
    ("EN15", "proprioceptive_0_2"): ("0", "The static reading does not require body orientation; the movement reading may."),
    ("EN17", "proprioceptive_0_2"): ("0", "The route noun does not entail a traveler; conditional embodied traversal needs explicit justification."),
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def score_reason(concept: dict[str, str], feature: str, score: int) -> str:
    definition = concept["target_sense_definition_en"].rstrip(".")
    channel = feature.removesuffix("_0_2")
    explanations = {
        "visual": {
            0: "the selected relation is not characteristically visible",
            1: "visual observation may help, but the relation also needs a learned convention or force cue",
            2: "the reference entities, line, region, or body arrangement can be inspected visually",
        },
        "auditory": {
            0: "the literal relation does not entail a characteristic sound",
            1: "a spatialized sound can conditionally indicate the relation, but sound is not required",
            2: "auditory information is characteristic of the selected sense",
        },
        "tactile": {
            0: "the selected relation does not entail a felt surface or pressure cue",
            1: "touch can conditionally reveal a physical instance, but is not part of every instance",
            2: "physical contact or load pressure directly realizes the selected sense",
        },
        "motor": {
            0: "the relation can hold without performing an action",
            1: "an action can instantiate the relation, but is not required by every use",
            2: "movement or controlled bodily action is part of realizing this sense",
        },
        "proprioceptive": {
            0: "body position or effort is not entailed by the literal relation",
            1: "a body-relative viewpoint or effort can conditionally help realize the relation",
            2: "bodily position or joint/effort feedback is characteristic of this sense",
        },
        "interoceptive": {
            0: "no internal bodily state is entailed by the target sense",
            1: "an internal bodily cue can contribute conditionally",
            2: "internal bodily state is characteristic of the target sense",
        },
        "social": {
            0: "the selected literal sense does not encode an interpersonal relation",
            1: "social interaction can conditionally ground the selected sense",
            2: "an interpersonal relation is characteristic of this sense",
        },
    }
    return f"For the selected sense ('{definition}'), {explanations[channel][score]}."


def main() -> None:
    base = read_csv(SOURCE)
    prior = {(r["concept_id"], r["feature"]): r for r in read_csv(PROVENANCE)}
    assert len(base) == 40 and len(prior) == 280
    assert {r["language"] for r in base} == {"ZH", "EN"}
    assert {r["semantic_family"] for r in base} == set(PARENT_BY_FAMILY)

    parent_rows = [{
        "category_parent": "spatial_or_embodied_relation",
        "definition_en": "A relation involving location, arrangement, route, contact, or physical force.",
        "supercategory": "",
        "selection_status": "AI_assisted_proposal_pending_team_review",
    }] + [
        {"category_parent": name, "definition_en": definition,
         "supercategory": "spatial_or_embodied_relation", "selection_status": "AI_assisted_proposal_pending_team_review"}
        for name, definition in PARENT_BY_FAMILY.values()
    ]
    write_csv(PARENTS, parent_rows, list(parent_rows[0]))

    v3_rows: list[dict[str, object]] = []
    audit_rows: list[dict[str, object]] = []
    ha0_rows: list[dict[str, object]] = []
    for row in base:
        cid = row["concept_id"]
        parent, parent_definition = PARENT_BY_FAMILY[row["semantic_family"]]
        assert parent.casefold() != row["term"].casefold()
        v3 = dict(row)
        v3["lexical_check_prior_status"] = row["lexical_check_status"]
        v3["lexical_check_status"] = "manual_confirmation_by_Xia_2026-11-18"
        v3["lexical_review_source"] = "Xia Yuqi confirmation in project chat on 2026-11-18; no dictionary citation asserted"
        v3["category_parent"] = parent
        v3["category_parent_source"] = "AI_assisted_category_proposal_from_target_definition"
        v3["category_parent_status"] = "pending_team_review"
        v3["uncertainty_note"] = (
            "The definition permits static and directional readings; Motor/Proprioceptive scores depend on which reading is used."
            if cid == "EN15" else ""
        )
        v3["C_audit_status"] = "AI_assisted_value_review_completed; 9 flagged values require team decision"
        v3_rows.append(v3)

        ha0 = {
            "concept_id": cid, "language": row["language"], "term": row["term"],
            "term_provenance": "manual", "term_source": row["source_candidate_ids"],
            "part_of_speech": row["part_of_speech"],
            "part_of_speech_provenance": "manual", "part_of_speech_source": row["target_definition_origin"],
            "definition_en": row["target_sense_definition_en"],
            "definition_provenance": "manual", "definition_source": v3["lexical_review_source"],
            "definition_original_source": row["target_definition_origin"],
            "category_parent": parent, "category_parent_definition": parent_definition,
            "category_parent_provenance": "generated", "category_parent_source": v3["category_parent_source"],
            "category_parent_confidence": "medium",
            "example_sentence": row["example_sentence"], "example_provenance": "generated",
            "example_source": "constructed_illustration_from_v2",
            "uncertainty_note": v3["uncertainty_note"],
            "review_status": "AI_assisted_HA0_draft_pending_team_validation",
        }
        for feature in FEATURES:
            score = int(row[feature])
            assert score in (0, 1, 2)
            p = prior[(cid, feature)]
            assert int(p["v2_score"]) == score
            flagged = FLAGS.get((cid, feature))
            source_label = "manual" if p["provenance"] == "reported_prior_rating" else "generated"
            source_note = (
                "Reported one-pass rating from PR12; rater identity not recorded, not independently rerated here"
                if source_label == "manual" else "AI-assisted draft or re-audit, not independent human rating"
            )
            confidence = str(p["confidence"]).lower()
            if confidence not in {"high", "medium", "low"}:
                confidence = "low"
            if flagged:
                confidence = "low"
            reason = score_reason(row, feature, score)
            if flagged:
                reason += " Review question: " + flagged[1]
            audit_rows.append({
                "concept_id": cid, "language": row["language"], "term": row["term"],
                "target_definition_en": row["target_sense_definition_en"], "feature": feature,
                "v2_score": score, "reviewed_score": score,
                "alternative_for_discussion": flagged[0] if flagged else "",
                "score_disagreement_status": "potential_disagreement_pending_team_decision" if flagged else "no_change_proposed_by_AI_audit",
                "provenance_label": source_label, "provenance_detail": p["origin"],
                "source": p["source"], "source_limit": source_note,
                "reason_or_source": reason, "confidence": confidence,
                "reviewer_status": "AI_assisted_check; no independent team rating claimed",
            })
            short = feature.removesuffix("_0_2")
            ha0[feature] = score
            ha0[short + "_provenance"] = source_label
            ha0[short + "_source"] = p["source"]
            ha0[short + "_confidence"] = confidence
        ha0_rows.append(ha0)
    assert len(v3_rows) == len(ha0_rows) == 40

    write_csv(V3, v3_rows, list(v3_rows[0]))
    write_csv(AUDIT, audit_rows, list(audit_rows[0]))
    write_csv(HA0, ha0_rows, list(ha0_rows[0]))
    print(f"Wrote {len(v3_rows)} senses, {len(audit_rows)} feature reviews, {len(ha0_rows)} HA0 rows")


if __name__ == "__main__":
    main()
