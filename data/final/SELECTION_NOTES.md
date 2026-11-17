# Selection and annotation record

## Scope

`spatial_relations_zh20_en20_v1.csv` is the selected vocabulary database: 20 Chinese and 20 English concept senses. It is the repository owner's final **selection v1**, assembled from the three original candidate proposals. It is not a claim that all three contributors independently approved every sense or score.

## Selection rule

The three pools contain 120 nominations and 110 distinct language-plus-word-form combinations. Ten forms occur in two members' pools and none in all three; all ten are included. This count is by **word form**. The CSV flags repeated forms whose original parts of speech or sense boundaries differ; these remain review items and are not silently treated as identical senses.

The remaining 30 places were filled for coverage of position, containment, boundary, center/periphery, orientation, betweenness, distance, configuration, path, contact, and support. The final list contains 37 directly spatial senses and three embodied-force senses. Chinese and English were selected separately; exact translation pairs were not required.

Four changes from Xia's draft shortlist improve coverage:

| Removed | Added | Reason |
|---|---|---|
| 后面 | 左侧 | Retains a front relation and adds lateral orientation. |
| 朝向 | 坡度 | Adds a measurable surface gradient alongside the direction terms. |
| intersection | separation | Adds an interval relation that contrasts with adjacency and contact. |
| perimeter | posture | Adds body configuration and reduces overlap with boundary. |

Each selected row records the source candidate IDs, the number of proposing members by word form, a target definition, its origin, and a selection reason. The three original proposal files remain intact.

## Seven-feature C and taxonomy S

All 40 rows have seven 0–2 channel values and `C_unit = sum(channel values)/14`. These are **reference annotations**, with per-row provenance: 28 were taken from the single rating pass in [PR #12](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/12), ten from the draft in [PR #11](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/11), and two are initial estimates for previously unrated force terms. They have not been reconciled as a three-rater team score. The two newly scored terms need independent review.

A numeric `S_depth` is reported for 26 rows where the chosen definition exactly matches a row with a recorded root-to-sense path in PR #12. The path, synset ID, and source version are copied into the CSV. The other 14 rows have `S_depth` blank and `S_status=NA_no_matching_supported_taxonomic_path`; blank does not mean zero. The PR #12 paths use COW 1.1 with OMW English 2.0 for Chinese and OMW English 2.0 for English. This is a reported audit, not a new independent ontology verification.

For a descriptive C×S coverage check, `high C` means at least five of the 14 possible channel points, and `high S` means reported depth at least six. Among the 26 rows with numeric S:

| Quadrant | Chinese | English | Total |
|---|---:|---:|---:|
| Low C / low S | 4 | 4 | 8 |
| Low C / high S | 4 | 3 | 7 |
| High C / low S | 2 | 3 | 5 |
| High C / high S | 2 | 4 | 6 |

There are eight Chinese and six English rows with S unavailable. The displayed spread is a feasibility check based on provisional source annotations; no score or taxonomy depth was altered to populate a quadrant.

## Definition and example status

Definitions originate in the candidate pools, except two narrowed physical-sense definitions taken from PR #11 and identified in `target_definition_origin`. The example sentences were constructed to illustrate the chosen sense; they are not quoted Oxford or corpus examples. English definitions and use should still be checked against [Oxford Learner's Dictionaries](https://www.oxfordlearnersdictionaries.com/). Chinese senses should be checked against [Chinese Open Wordnet](https://bond-lab.github.io/cow/) or [NTU Chinese WordNet](https://lopen.linguistics.ntu.edu.tw/index_en.html), with usage examples from a suitable corpus. OpenHowNet sememes should not be substituted for taxonomy edges. Record any correction in a new version rather than silently replacing a source sense.
