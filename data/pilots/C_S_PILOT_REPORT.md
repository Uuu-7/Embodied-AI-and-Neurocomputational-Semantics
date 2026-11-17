# Concept selection and C × S pilot (IN PROGRESS)

**Date:** 2026-11-17. **Source:** the three individual candidate pools in `candidates/`. **Status:** nomination comparison and a 12-concept audit are prepared; team decisions, independent ratings, taxonomy verification, and C × S analysis are pending.

## Executive diagnostic

- Each member proposed 20 Chinese and 20 English candidates: **120 nomination rows** in total. Normalizing written forms within each language gives **110 distinct forms**, including **10 forms nominated twice** and none nominated three times. These are form counts, not confirmed shared senses.
- There is **no approved final 40-concept set** after restarting from the three proposals. The pilot samples the union before a full selection.
- The [pilot audit](../audit/pilot_concept_audit_v01.csv) has **12 concepts** (6 ZH, 6 EN) across geometry, direction, path, force, and social extension. Its `provisional_decision` is a review suggestion; `team_decision` remains blank.
- The three [independent rating forms](../audit/raters/) each have **84 blank decisions** (12 senses × 7 features). Thus there are **no observed C scores or inter-rater agreement values**.
- No sense-specific taxonomy edge has yet been independently verified. **S is NA for all pilot concepts**, so a genuine C × S scatter plot and quadrant count cannot yet be produced.

## Concept selection audit

The [nomination rows](../audit/nomination_rows_v01.csv) retain each person's original ID, definition, part of speech, subfamily, schema candidate, lexical-source flag, and review status. The [vote-count table](../audit/term_vote_counts_v01.csv) records written-form overlap. A shared spelling gets a shared concept vote only after the team confirms that its sense and grammatical role align.

| Pilot group | Coverage | Proposed action | Reason to review |
| --- | --- | --- | --- |
| P01–P04 | Containment, geographic direction, path | Revise | Align part of speech or distinguish static and moving senses |
| P05–P06 | Force and social extension | Revise | Fix the target sense and confirm project scope |
| P07–P12 | Boundary, vertical direction, route, contact, force, social extension | Keep | Defined senses are usable pilot targets; source and taxonomy checks remain |

The complete keep/revise/replace table, including terms and candidate IDs, is in the CSV. `keep` does not mean externally validated. The pilot currently has no proposed `replace` case; the team may set one after evidence review.

## Seven-feature annotation

The seven channels match the course scheme and PR #7's table structure: **visual, auditory, tactile, motor, proprioceptive, interoceptive, social**. Rate the *specified sense* on the same scale for each channel:

| Score | Operational rule |
| ---: | --- |
| 0 | The channel does not contribute to the target sense; incidental cues in an example do not count. |
| 1 | The channel can directly instantiate the sense, but depends on context or is secondary. |
| 2 | The channel is a characteristic, direct way to identify or enact the sense. |

Each member fills only their own file in `data/audit/raters/`, without seeing the others' ratings first. `provenance` identifies manual judgment or a specific source; `reason_or_source` gives a short explanation or citation; `confidence` records high/medium/low. Keep the proposed definition fixed during the independent pass. If an item needs a new sense definition, revise the audit table and repeat that item's rating.

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
