# HA0 — Data and feature design (team working draft)

The instructor accepted the bilingual scope of **20 Chinese and 20 English selected senses**. The 40-row `ha0_zh20_en20.csv` is derived from `data/final/spatial_relations_zh20_en20_v3_working.csv`. Xia Yuqi confirmed the target lexical senses manually in the project conversation on 18 November 2026. This confirmation is recorded as manual review; it is **not** represented as a dictionary citation. Definitions and examples remain short sense-specific paraphrases and constructed illustrations, respectively.

## One category parent per sense

Each row has exactly one `category_parent`. The eleven parent nodes and their short definitions are in `data/final/category_parent_nodes_v1.csv`; they sit below the defined root `spatial_or_embodied_relation`. A parent denotes the broader relation type, not a second name for the word. For example, an interval concept is placed under `spatial_interval_relation`, whereas a bodily stability concept is under `load_or_stability_relation`. These pedagogical parents are **not** substituted for COW/OMW hypernym paths when calculating S. Parent choices are AI-assisted proposals for team review.

## Seven-feature scale

For Visual, Auditory, Tactile, Motor, Proprioceptive, Interoceptive, and Social, score the selected literal sense: `0` means no typical direct grounding, `1` means conditional or secondary direct grounding, and `2` means characteristic direct grounding. Do not import social or philosophical metaphorical extensions into a literal spatial score. The 280-row `data/reviews/feature_score_audit_v3.csv` provides the value, source, feature-specific reason, confidence, and review flag for every score.

Every feature value in the 40-row export is labelled `manual` or `generated`. The 156 `manual` labels refer to a **reported earlier single pass with no recorded rater identity**; the 124 `generated` labels refer to prior AI-assisted proposals. No score is marked `sourced`, because no published sensory norm was verified for a selected value. This is an honest provenance classification, not a claim that Xia, Chen, and Hu independently scored all 280 cells. Term/definition confirmation is Xia's manual check; category parents and examples are generated proposals.

## Explicit uncertainty and testable question

`EN15` is the required uncertainty row. Its definition allows a static opposite-side reading and a directional reading; the one-line note in the CSV explains why its Motor and Proprioceptive scores may depend on the reading. The score audit flags both cells. The team should either justify a combined-sense policy or narrow the target before final sign-off.

**Question:** In held-out paired spatial scenes, does reversing the observer viewpoint change orientation labels more often than containment labels, while the objects and their physical relation remain fixed?

**Prediction:** Orientation labels change under viewpoint reversal more often than containment labels. **Result that would weaken the claim:** the reversal rates are equal, or containment labels change more often, after excluding scenes where the containment relation itself changed. This is a proposed future test; the current 40-word CSV contains no scene-pair observations and does not establish the prediction.

## Reproduce and limits

Run `python data/final/build_v3.py` from the repository root to regenerate the 40-row HA0 export, parent-node table, v3 working dataset, and 280-row audit. There is no random sampling or seed in this step. The nine flagged C values and 25 inherited S paths require team adjudication/source checking before calling this a validated joint submission. Upload to the LMS must be done separately; GitHub publication does not prove course submission.
