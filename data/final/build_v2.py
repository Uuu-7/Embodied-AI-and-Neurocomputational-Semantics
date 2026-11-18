"""Rebuild the integrated 20 ZH + 20 EN dataset and score provenance."""

from __future__ import annotations

import csv
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
FINAL = ROOT / "data" / "final"
REVIEWS = ROOT / "data" / "reviews"
BASE = FINAL / "spatial_relations_zh20_en20_v1.csv"
DRAFT = REVIEWS / "chenfengru_spatial_relations_zh20_en20_v1_1_C_reaudit_DRAFT.csv"
LOG = REVIEWS / "chenfengru_C_reaudit_change_log_v1_1.csv"
OUT = FINAL / "spatial_relations_zh20_en20_v2.csv"
PROVENANCE = FINAL / "feature_provenance_v2.csv"

FEATURES = (
    "visual_0_2", "auditory_0_2", "tactile_0_2", "motor_0_2",
    "proprioceptive_0_2", "interoceptive_0_2", "social_0_2",
)

# Chen's updated PR #14 implemented these eight changes after Hu's review.
HU_REVIEW_IMPLEMENTED = {
    ("ZH02", "motor_0_2"), ("ZH03", "motor_0_2"),
    ("ZH11", "social_0_2"), ("ZH12", "social_0_2"),
    ("ZH16", "motor_0_2"), ("EN04", "motor_0_2"),
    ("EN12", "motor_0_2"), ("EN17", "motor_0_2"),
}
HU_REVIEW = "https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/14#issuecomment-6961983401"
CHEN_PR = "https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/14"


def main() -> None:
    base = pd.read_csv(BASE, keep_default_na=False).set_index("concept_id")
    draft = pd.read_csv(DRAFT, keep_default_na=False).set_index("concept_id")
    log = pd.read_csv(LOG, keep_default_na=False).set_index("concept_id")
    assert len(base) == len(draft) == 40
    assert base.index.equals(draft.index)
    assert set(log.index).issubset(draft.index)

    out = draft.copy()
    for concept, feature in HU_REVIEW_IMPLEMENTED:
        assert int(out.loc[concept, feature]) == 0, (concept, feature)

    out["C_sum"] = out[list(FEATURES)].astype(int).sum(axis=1)
    out["C_unit"] = (out["C_sum"] / 14).round(6)
    for concept in out.index:
        if concept in log.index:
            out.loc[concept, "C_rating_status"] = "integrated_provisional_pending_team_validation"
        if not str(out.loc[concept, "S_depth"]).strip():
            out.loc[concept, "C_S_quadrant_reference"] = "NA_S"
        else:
            c = "high_C" if int(out.loc[concept, "C_sum"]) >= 5 else "low_C"
            s = "high_S" if int(float(out.loc[concept, "S_depth"])) >= 6 else "low_S"
            out.loc[concept, "C_S_quadrant_reference"] = f"{c}_{s}"

    # The narrowed bodily sense cannot inherit the former mechanical-equilibrium path.
    assert not str(out.loc["EN19", "S_depth"]).strip()
    assert not str(out.loc["EN19", "S_taxonomy_path"]).strip()
    assert int(out.loc["ZH18", "tactile_0_2"]) == 1
    assert int(out.loc["EN11", "proprioceptive_0_2"]) == 2
    assert out.groupby("language").size().to_dict() == {"ZH": 20, "EN": 20}
    out.reset_index().to_csv(OUT, index=False, encoding="utf-8", float_format="%.6f")

    records = []
    for concept in out.index:
        for feature in FEATURES:
            old_value = int(base.loc[concept, feature])
            draft_value = int(draft.loc[concept, feature])
            value = int(out.loc[concept, feature])
            if (concept, feature) in HU_REVIEW_IMPLEMENTED:
                origin = "Chen_PR14_revision_after_Hu_review"
                kind = "generated"
                source = CHEN_PR + " ; " + HU_REVIEW
                reason = str(log.loc[concept, "layer_1_reason"])
                confidence = str(log.loc[concept, "review_confidence"])
            elif value != old_value:
                origin = "Chen_PR14_AI_assisted_draft"
                kind = "generated"
                source = CHEN_PR
                reason = str(log.loc[concept, "layer_1_reason"]) if concept in log.index else "Chen PR #14 revised feature."
                confidence = str(log.loc[concept, "review_confidence"]) if concept in log.index else "medium"
            else:
                origin = str(base.loc[concept, "C_rating_source"])
                kind = "reported_prior_rating" if "PR12" in origin else "generated"
                source = "data/final/spatial_relations_zh20_en20_v1.csv"
                reason = "Carried from v1; no new independent rating."
                confidence = str(base.loc[concept, "C_rating_confidence"])
            records.append({
                "concept_id": concept, "language": out.loc[concept, "language"],
                "term": out.loc[concept, "term"], "feature": feature,
                "v1_score": old_value, "chen_draft_score": draft_value,
                "v2_score": value, "provenance": kind, "origin": origin,
                "source": source, "reason_or_source": reason,
                "confidence": confidence,
                "review_status": "integrated_provisional_pending_team_validation",
            })
    assert len(records) == 280
    pd.DataFrame(records).to_csv(PROVENANCE, index=False, encoding="utf-8", quoting=csv.QUOTE_MINIMAL)
    print("Wrote", OUT.relative_to(ROOT), "and", PROVENANCE.relative_to(ROOT))
    print("C/S descriptive quadrants:", out["C_S_quadrant_reference"].value_counts().to_dict())


if __name__ == "__main__":
    main()
