"""Refresh Xia's HA0 export from the integrated dataset and per-score record."""

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SOURCE = ROOT / "data/final/spatial_relations_zh20_en20_v2.csv"
PROVENANCE = ROOT / "data/final/feature_provenance_v2.csv"
OUTPUT = HERE / "ha0_zh20_en20_xiayuqi.csv"


def main() -> None:
    source = pd.read_csv(SOURCE, keep_default_na=False).set_index("concept_id")
    provenance = pd.read_csv(PROVENANCE, keep_default_na=False).set_index(["concept_id", "feature"])
    old = pd.read_csv(OUTPUT, keep_default_na=False).set_index("concept_id")
    assert source.index.equals(old.index)
    result = old.copy()
    for concept in source.index:
        result.loc[concept, "definition_en"] = source.loc[concept, "target_sense_definition_en"]
        result.loc[concept, "part_of_speech"] = source.loc[concept, "part_of_speech"]
        result.loc[concept, "example_sentence"] = source.loc[concept, "example_sentence"]
        result.loc[concept, "definition_source"] = source.loc[concept, "target_definition_origin"]
        if concept == "EN19":
            result.loc[concept, "definition_provenance"] = "generated"
            result.loc[concept, "uncertainty_note"] = (
                "The bodily balance sense has no verified compatible S path; leave S=NA."
            )
        for feature in ("visual", "auditory", "tactile", "motor", "proprioceptive", "interoceptive", "social"):
            field = feature + "_0_2"
            p = provenance.loc[(concept, field)]
            result.loc[concept, field] = int(source.loc[concept, field])
            result.loc[concept, feature + "_provenance"] = p["provenance"]
            result.loc[concept, feature + "_source"] = p["source"]
            result.loc[concept, feature + "_confidence"] = p["confidence"]
        result.loc[concept, "review_status"] = "integrated_provisional_pending_team_validation"
    result["category_parent_source"] = "data/final/spatial_relations_zh20_en20_v2.csv:semantic_family"
    result["example_source"] = "data/final/spatial_relations_zh20_en20_v2.csv:constructed_example"
    result.reset_index().to_csv(OUTPUT, index=False, encoding="utf-8")
    print("Refreshed", OUTPUT.relative_to(ROOT), "with", len(result), "senses")


if __name__ == "__main__":
    main()
