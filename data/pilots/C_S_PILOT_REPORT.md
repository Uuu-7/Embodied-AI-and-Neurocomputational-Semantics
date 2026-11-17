# Concept selection and C × S pilot (IN PROGRESS)

**Date:** 2026-11-17. **Source:** the three individual candidate pools in `candidates/`. **Status:** nomination comparison and a 12-concept audit are prepared; an AI-assisted draft in Xia's assigned form awaits her review. Team decisions, independent human ratings, taxonomy verification, and C × S analysis are pending.

## Executive diagnostic

- Each member proposed 20 Chinese and 20 English candidates: **120 nomination rows** in total. Normalizing written forms within each language gives **110 distinct forms**, including **10 forms nominated twice** and none nominated three times. These are form counts, not confirmed shared senses.
- There is **no approved final 40-concept set** after restarting from the three proposals. The pilot samples the union before a full selection.
- The [pilot audit](../audit/pilot_concept_audit_v01.csv) has **12 concepts** (6 ZH, 6 EN) across geometry, direction, path, force, and social extension. Each definition and provisional decision has been checked against the three proposals and the linked dictionary sense. **Seven are marked keep and five revise**; `team_decision` remains blank.
- The [three assigned rating forms](../audit/raters/) each contain 84 rows (12 senses × 7 features). Xia's contains an **AI-assisted draft pending her review**; Chen's and Hu's remain blank. Thus there are **no three-person independent human ratings, consensus C scores, or inter-rater agreement values**.
- No sense-specific taxonomy edge has yet been independently verified. **S is NA for all pilot concepts**, so a genuine C × S scatter plot and quadrant count cannot yet be produced.

## Concept selection audit

The [nomination rows](../audit/nomination_rows_v01.csv) retain each person's original ID, definition, part of speech, subfamily, schema candidate, lexical-source flag, and review status. The [vote-count table](../audit/term_vote_counts_v01.csv) records written-form overlap. A shared spelling gets a shared concept vote only after the team confirms that its sense and grammatical role align.

| Pilot group | Coverage | Proposed action | Reason to review |
| --- | --- | --- | --- |
| P01–P03 | Containment and geographic direction | Keep | Dictionary senses support the definitions; part-of-speech labels are standardized |
| P04–P06 | Path, force, and social extension | Revise | Fix movement, bodily equilibrium, and group membership readings |
| P07–P10 | Boundary, vertical direction, route, contact | Keep | Dictionary senses support physical readings; taxonomy remains unchecked |
| P11–P12 | Bodily balance and social extension | Revise | Separate bodily from mechanical stability and felt from recognized membership |

The complete keep/revise/replace table, including terms, candidate IDs, and dictionary links, is in the CSV. `keep` means the target dictionary sense is plausible for this pilot; it does not validate a taxonomy path or approve final selection. The pilot currently has no proposed `replace` case; the team may set one after evidence review.

## Seven-feature annotation

The seven channels match the course scheme and PR #7's table structure: **visual, auditory, tactile, motor, proprioceptive, interoceptive, social**. Rate the *specified sense* on the same scale for each channel:

| Score | Operational rule |
| ---: | --- |
| 0 | The channel does not contribute to the target sense; incidental cues in an example do not count. |
| 1 | The channel can directly instantiate the sense, but depends on context or is secondary. |
| 2 | The channel is a characteristic, direct way to identify or enact the sense. |

Each member fills only their own file in `data/audit/raters/`, without seeing the others' ratings first. The existing Xia file is labeled `AI_assisted_draft_pending_Xia_review` on every row and must not be reported as her independent human annotation until she has reviewed or replaced it. `provenance` identifies manual judgment, AI assistance, or a specific source; `reason_or_source` gives a short explanation or citation; `confidence` records high/medium/low. Keep the proposed definition fixed during the independent pass. If an item needs a new sense definition, revise the audit table and repeat that item's rating.

After the three forms are complete, compare disagreements feature by feature. Quadratic-weighted Cohen's κ can be calculated for each rater pair and feature, where its chance-agreement denominator is defined; report `NA` otherwise. Then discuss disagreements and version any adjudicated ratings. Do not label the initial pass as consensus.

## Taxonomy validation

For each approved sense, fill the [pilot taxonomy worksheet](../audit/pilot_taxonomy_v01.csv) with its part of speech, lexical or ontology identifier, direct parent, full root-to-sense path, edge type, and exact source reference. WordNet hypernym paths are suitable only where the selected lexical sense and part of speech actually support them, especially nouns. Event or relation senses may require FrameNet or a documented domain ontology. A thematically similar noun does not give a preposition or verb an inherited WordNet depth. Mark `S=NA` and state why when a reliable comparable path is unavailable. Do not turn the candidate `subfamily` label into a verified taxonomy edge.

## C × S feasibility check

After independent rating and adjudication, compute `C_raw_mean = sum(seven scores)/7` and `C_unit = sum(seven scores)/14` for a complete sense. Keep both the raw channel vector and provenance. Define an S method and normalization only after the taxonomy has been checked, and publish the formula and range. Plot ZH and EN separately before any combined view; count all four quadrants using a declared threshold. The target shown in the workflow image is at least **three concepts per quadrant**. Check whether near-translations or sense duplicates inflate counts. If coverage fails, propose replacements from the original pools and repeat the relevant annotation and taxonomy checks; do not adjust ratings to fill a quadrant.

## Required team work

- [ ] Review the 12 pilot definitions, grammatical roles, and provisional keep/revise/replace decisions; record external evidence and final team decisions.
- [ ] Complete three separate seven-feature rating forms with reasons, provenance, and confidence.
- [ ] Compare ratings and document disagreement, agreement statistics, and adjudication.
- [ ] Verify taxonomy edges and source references; leave unsupported S values as `NA`.
- [ ] Compute actual C × S coverage, then agree on the final 20-ZH + 20-EN dataset and examples.

PR #7 is a **format and methodological reference** for the pilot report, seven-channel names, and honest `NA` handling. Its generated/scenario ratings and proposed alternative final list are not imported into this restart.
