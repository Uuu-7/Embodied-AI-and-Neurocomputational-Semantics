# Grounding and specificity annotation guide

The [v0.2 working dataset](../final/concepts_zh20_en20_v02.csv) contains 20 Chinese and 20 English selected senses with seven grounding ratings, one usage example per sense, and separate C and S scores. It extends the unchanged [v0.1 selection](../final/concepts_zh20_en20_v01.csv).

**Review update:** v0.2's S values came from a hand-built hierarchy. The later [four-step evidence review](../review/WORKFLOW.md) supersedes those exploratory S values for taxonomy-based analysis: its [v0.3 review table](../review/concepts_review_v03.csv) records verified noun paths and sets unmatched S to `NA`. The v0.2 C values remain a single-rater first pass pending independent team annotation.

## Seven grounding channels

Each channel is a manually judged estimate for the **defined sense**, not for every possible use of the spelling. A cue is direct when a perceptual, bodily, or action event could instantiate it. Apply the same scale to all channels:

| Value | Operational rule |
| ---: | --- |
| 0 | The channel is not part of the target spatial sense; a coincidental cue in an example does not count. |
| 1 | The channel can directly instantiate the sense, but depends on context or is secondary. |
| 2 | The channel is a characteristic, direct way to identify or enact the sense. |

Visual covers visible form and layout; auditory covers sound and audible range; tactile covers surface contact and pressure; motor covers enacted movement; proprioceptive covers body position, direction, effort, and stability; interoceptive covers felt internal state; social covers interpersonal roles and norms. No selected literal spatial sense required social content, so its scores remain zero. The annotation input records a short justification and confidence for every row; low confidence invites peer review.

`C_score` is the **unweighted mean of the seven 0–2 ratings**, so its theoretical range is [0, 2]. Every channel stays visible beside it. This is a manual proxy, not a measured human concreteness norm. We have not frequency-adjusted C, and none of Hu's workbook estimates was copied into this scored output.

## Specificity hierarchy

`taxonomy_v01.csv` is an explicit, curated **is-a-type-of-spatial-relation** hierarchy. Its root, `spatial_relation`, has depth 0. Each concept is attached under exactly one `specificity_parent` in `manual_ratings_v01.csv`; `S_score` counts the edges from root to that concept. `specificity_path` prints every intermediate node. Broad senses can sit nearer the root; more constrained senses have longer paths. The category nodes and attachments are manual design choices, not verified WordNet hypernyms. A single shared taxonomy lets the two languages and mixed parts of speech use one operational definition; it sacrifices some lexical nuance.

For this version, `C_norm_0_1 = (C_score - min C_score) / (max C_score - min C_score)` and likewise for S. Minima and maxima are calculated over all 40 selected rows, without separate language scaling. The observed C range is **1/7 to 5/7** and S range is **2 to 4 edges**. This dataset-specific normalization magnifies small differences in a narrow sample; retain raw scores when comparing versions or adding concepts. These normalized fields support later C × S plots, but no composite abstractness score is asserted here.

## Provenance and review

- `manual_ratings_v01.csv` holds the seven values, category parent, sentence, note, and confidence for each selected concept ID. Examples are original hand-written sentences in the concept's language and target the spatial sense.
- `feature_provenance=manual` and `example_provenance=manual` apply to every row. `annotation_status=annotated_manual_pending_peer_review` states that this is a complete **single-pass** annotation, not agreement among all three team members.
- `scripts/build_scored_dataset.py` validates IDs, seven 0–2 scores, example-term presence, hierarchy connectivity and cycles, then derives C, S, and normalized scores. Run `python scripts/build_scored_dataset.py` from the repository root to rebuild the v0.2 CSV.
- For group review, have at least one other contributor score ambiguous rows independently, record differences, and version any corrections. Do not recast the current manual numbers as sourced norms or inter-rater consensus.
