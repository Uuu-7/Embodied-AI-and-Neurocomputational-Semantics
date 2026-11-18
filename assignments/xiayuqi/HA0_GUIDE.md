# HA0: data and feature guide (Xia Yuqi)

The accompanying CSV exports the 20 Chinese and 20 English selected senses for HA0. The instructor has accepted this bilingual 40-row scope. The source table is `data/final/spatial_relations_zh20_en20_v1.csv`; the three original candidate pools remain under `candidates/`.

## Target sense and category

Score the **literal target sense** in `definition_en`, not a possible metaphorical extension. Each row has one `category_parent`, drawn from the following small, pedagogical grouping. These grouping edges are **not** the WordNet/COW hypernym paths used for S in HA1.

| Parent | Working meaning |
|---|---|
| `position` | Place occupied relative to a reference space |
| `containment` | Region inside or outside a boundary |
| `boundary` | Limit separating regions |
| `center_periphery` | Position relative to a region's middle or edge |
| `orientation` | Directional position relative to an axis or viewpoint |
| `betweenness` | Position between reference entities |
| `distance` | Separation or gap between entities |
| `configuration` | Arrangement of lines, surfaces, or bodies |
| `path` | Route or traversal through space |
| `contact` | Meeting or adjacency of surfaces or entities |
| `force_support` | Load bearing or physical stability |

## Seven-feature rubric

For every channel, `0` means absent from typical direct grounding of the target sense, `1` means conditional or secondary, and `2` means central or direct. Score the specified sense and an ordinary use, not every imaginable context. Keep a low-confidence annotation when direct grounding is uncertain. The CSV pairs **each score** with a provenance type and source.

| Feature | What counts as direct evidence |
|---|---|
| Visual | Visible position, shape, line, surface, or motion |
| Auditory | Spatial or action information directly carried by sound |
| Tactile | Pressure, texture, or physical contact |
| Motor | A bodily action needed to enact the relation |
| Proprioceptive | Body position, effort, or load awareness |
| Interoceptive | Internal bodily state or affect |
| Social | Interpersonal role, convention, or norm in the target sense |

The provenance enum is `manual` or `generated` for these rows. `manual` refers to the single rating pass imported from PR #12; the workbook's rater field was not filled, so it is **not** an independent Xia rating. `generated` refers to the PR #11 draft or two newly proposed estimates. Definitions copied from the members' proposals are labelled `manual`; two narrowed definitions derived in PR #11 are `generated`. The examples and category grouping were constructed for this export and are labelled `generated`. All rows are marked as drafts awaiting Xia's independent review.

One deliberately uncertain row is `EN20`, where motor and proprioceptive involvement depends on an active person versus a passive load-bearing structure. Its one-line note is in `uncertainty_note`.

## Modelling question

**Question:** After independent review, do path, contact, and force-support senses have a higher average tactile + motor + proprioceptive score than position and boundary senses across the bilingual inventory?

**Prediction:** The first group has a higher average sum of those three channels. **Result that would weaken it:** the difference disappears or reverses after the three members independently rescore the same target senses.

## Submission checks

- Review the seven channel values and their provenance before representing them as Xia's own ratings.
- Confirm that the target definitions, parts of speech, and single parent assignments match the intended senses.
- The illustrative examples are newly written; replace them with cited corpus examples if the instructor requires attested use.
- The export has no random step or seed. HA1's notebook records its computational environment and creates the plots deterministically.
