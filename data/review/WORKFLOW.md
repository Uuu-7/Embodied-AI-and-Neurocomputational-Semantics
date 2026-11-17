# Four-step concept review

This review uses the selected-set snapshot at `699396ec098ba9dbc69794b8b968c2acbcc219ab` and follows the requested sequence without treating the existing AI-generated draft scores as three-person consensus. The selected 20 Chinese and 20 English terms in `data/final/` remain unchanged until the team resolves replacements.

## 1. Concept selection audit

[`pilot_concept_audit_v01.csv`](pilot_concept_audit_v01.csv) records **12 representative concepts from the current 40**. It spans geometry and topology, direction, path, force, and an auditory range. Each row checks target sense, part of speech, and external evidence, then records `keep`, `revise`, or `replace_proposed`. Nine are kept as written, one gets a narrower movement-sense definition in the pilot form, and two one-vote adjacency items are proposed for replacement, subject to team review.

There is **no explicit social-metaphor target sense among the selected 40**. Reinterpreting a literal row as a metaphor would silently change its annotation target. [`replacement_candidates_v01.csv`](replacement_candidates_v01.csv) therefore lists one Chinese and one English proposal already present in Chen's original pool. They are **outside the 12 pilot rows**, have no assigned C/S values, and are not yet part of the 20+20 dataset. If the team approves them, rerun selection and annotation on a new version.

## 2. Independent seven-feature annotation

The [three rater forms](raters/) contain the same 12 concepts × seven channels, or **84 blank decisions per person**. Xia Yuqi, Chen Fengru, and Hu Jinnan should fill their own forms independently using the 0–2 rules in the [annotation guide](../annotation/ANNOTATION.md). For every channel, record the score, `sourced` / `manual` / `generated` provenance, a reason or source, and `high` / `medium` / `low` confidence. Review the definitions and examples before rating; do not copy the existing v0.2 values into a form.

`python scripts/check_pilot_agreement.py` validates all three forms and, **only after all 252 decisions are present**, writes quadratic weighted Cohen's κ and exact agreement by channel and rater pair, plus a disagreement list. When a channel has no expected variation, κ is `NA`. The current forms are blank, so no agreement statistic or consensus C exists. Resolve disagreements with a recorded decision before extending the forms to the remaining concepts.

## 3. Evidence-backed taxonomy

[`sense_decisions_v01.csv`](sense_decisions_v01.csv) checks all **40 target senses**, not merely spelling matches. [`taxonomic_paths_v01.csv`](taxonomic_paths_v01.csv) gives **15 verified paths** with source sense ID, shared English noun sense, gloss, every hypernym ID, and depth. Chinese senses use [Chinese Open Wordnet 1.1](https://bond-lab.github.io/cow/) aligned by ILI to [OMW English 2.0](https://omwn.org/); English senses use OMW directly. Paths end at the noun `entity` root and choose the shortest hypernym path. The script checks lemma membership, noun part of speech, shared ILI, path connectivity, and computed depth. See the [Wn taxonomy documentation](https://wn.readthedocs.io/en/v1.1.1/api/wn.taxonomy.html) for path semantics.

The remaining **25 S values are `NA`** in [`concepts_review_v03.csv`](concepts_review_v03.csv). Reasons include absent or mismatched target senses, prepositions and other parts of speech, or the lack of a comparable noun hierarchy. Berkeley FrameNet's published [spatial-relation analysis](https://aclanthology.org/W18-1405/) offers useful frame candidates for some prepositions, but frame inheritance and noun hypernym depth cannot be mixed into one S scale without an independently validated mapping. The v0.2 hand-built depths remain historical exploratory values and are **superseded for this evidence audit**.

To reproduce the Wordnet audit, install `wn==1.1.1`, download `omw-en:2.0` and the `cow:1.1` package linked from the COW page, then run `python scripts/build_evidence_review.py`. The generated path table and v0.3 review CSV are committed so users can inspect the evidence without installing the lexicons.

## 4. C×S feasibility check

[`quadrant_counts_v01.csv`](quadrant_counts_v01.csv) and the [scatter plot](../../reports/pilot_cxs_feasibility_v01.png) use **AI-generated v0.2 C** and only the **15 checked noun S** values. They are provisional. C is min–max normalized over all 40 generated rows; S is min–max normalized over the 15 verified noun rows (raw depth 5–8). Values at exactly 0.5 count as high. The exploratory target is at least three concepts per quadrant **within each language**.

| Language | Low C / Low S | Low C / High S | High C / Low S | High C / High S | Checked S / 20 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Chinese | 1 | 0 | 5 | 2 | 8 |
| English | 1 | 2 | 4 | 0 | 7 |

Neither language currently reaches the four-quadrant target. At least 12 comparable S values per language are mathematically necessary to have three in each quadrant, while only 8 Chinese and 7 English are verified. Do **not** alter feature ratings merely to populate quadrants. The team should first adjudicate the pilot, validate more comparable S paths or revise the concept inventory, then rerun the feasibility check. The two proposed social additions address a semantic-coverage gap; they are **not** claimed to repair the numerical quadrant gap.
