# HA0 — Data and feature design (aligned HA1 submission)

The instructor accepted the bilingual scope of **20 Chinese and 20 English selected senses**. The 40-row `ha0_zh20_en20.csv` is derived from `data/final/spatial_relations_zh20_en20_v4_ha1.csv`. Xia Yuqi confirmed the original target lexical inventory manually in the project conversation on 18 November 2026. The newly narrowed EN15 crossing definition is an editorial paraphrase checked against [Oxford Learner's Dictionaries](https://www.oxfordlearnersdictionaries.com/definition/english/across_1), not a second human confirmation. Examples are constructed illustrations.

## One category parent per sense

Each row has exactly one `category_parent`. The eleven parent nodes and their short definitions are in `data/final/category_parent_nodes_v2.csv`; they sit below the defined root `spatial_or_embodied_relation`. A parent denotes the broader relation type, not a second name for the word. For example, an interval or opening concept is placed under `spatial_interval_relation`, whereas a bodily stability concept is under `load_or_stability_relation`. `spatial_arrangement` includes geometric properties such as slope and angle. These pedagogical parents are **not** substituted for COW/OMW hypernym paths when calculating S. Parent choices are editorial proposals; three-person agreement is not recorded.

## Seven-feature scale

For Visual, Auditory, Tactile, Motor, Proprioceptive, Interoceptive, and Social, score the selected literal sense: `0` means no typical direct grounding, `1` means conditional or secondary direct grounding, and `2` means characteristic direct grounding. Do not import social or philosophical metaphorical extensions into a literal spatial score. The 280-row `data/reviews/feature_score_audit_v4.csv` provides the value, source, feature-specific reason, confidence, and review decision for every score. The nine flagged v3 decisions and links to the teammate review are explained in `data/reviews/HA1_ADJUDICATION_V4.md`.

Every feature value in the 40-row export is labelled `manual` or `generated`. The 155 `manual` labels refer to a **reported earlier single pass with no recorded rater identity**; the 125 `generated` labels include prior AI-assisted proposals and one revised value that had originally carried a `manual` label. No score is marked `sourced`, because no published sensory norm was verified for a selected value. This is a provenance classification, not a claim that Xia, Chen, and Hu independently scored all 280 cells. Category parents and examples are generated proposals.

## Explicit uncertainty and testable question

`ZH18` is the explicit uncertainty row. A mathematical tangency can exist without felt contact, whereas physical surface meeting may provide tactile evidence. The one-line CSV note explains why its Tactile score of 1 is conditional and low confidence. EN15 was narrowed to the movement sense before HA1 computation.

**Question:** In held-out paired spatial scenes, does reversing the observer viewpoint change orientation labels more often than containment labels, while the objects and their physical relation remain fixed?

**Prediction:** Orientation labels change under viewpoint reversal more often than containment labels. **Result that would weaken the claim:** the reversal rates are equal, or containment labels change more often, after excluding scenes where the containment relation itself changed. This is a proposed future test; the current 40-word CSV contains no scene-pair observations and does not establish the prediction.

## Reproduce and limits

Run `python data/final/build_v4.py` from the repository root to regenerate the 40-row HA0 export, parent-node table, v4 input, and 280-row audit from the preserved v3 sources. There is no random sampling or seed. The nine flagged C cells have explicit HA1 decisions; the 25 inherited S paths have only node-count validation here and still need full source-synset checks before being called independently validated. Upload to the LMS must be done separately; GitHub publication does not prove course submission.
