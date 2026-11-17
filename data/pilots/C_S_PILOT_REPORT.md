# C × S pilot and alternative vocabulary v0.2 (NOT FINAL)

**Date:** 2026-11-17. **Source:** `main:data/final/concepts_zh20_en20_v01.csv`. **Status:** AI-generated exploratory feature ratings; not independent human annotations. No source data were overwritten.

## Executive diagnostic

- Source inventory: **40 rows (20 ZH + 20 EN)**, all original seven-channel scores and S scores blank.
- Seven channels here follow Lecture 2: visual, auditory, tactile, motor, proprioceptive, interoceptive, social.
- Provisional `C_sum = sum(seven ordinal scores)`, `C_raw_mean=C_sum/7`, `C_unit=C_sum/14`. Across-dataset `C_minmax = (C_sum-min)/(max-min)`, using observed 40-row min/max. **These are model outputs, not independent measures of human experience.**
- **Current C_sum distribution:** {"2":23,"3":15,"6":2}. With min 2 and max 6, the relative high-C threshold (`C_minmax >= 0.5`) admits **2 / 40**. Consequently, **even if every S value were known**, there cannot be at least three concepts in each of the *two high-C quadrants* (at least six high-C points needed). This failure is conditional on the pilot ratings and normalization rule, not a confirmed empirical result.
- **S cannot be computed reliably yet.** `category_parent_proposed` only contains coarse labels. A single-parent category name is not a validated lexical-taxonomic path; the mix of nouns, verbs, prepositions, locatives, and phrases makes WordNet depth invalid for many entries. All S values intentionally stay **NA**. Therefore **no genuine four-quadrant plot or valid quadrant count is currently possible**.

## Preliminary C bins (current)

| Seven-feature sum | C_unit (0–1 theoretical) | C_minmax (observed) | Concepts |
|---:|---:|---:|---:|
| 2 | 0.143 | 0.000 | 23 |
| 3 | 0.214 | 0.250 | 15 |
| 6 | 0.429 | 1.000 | 2 |

## Optional alternative 40-row inventory (review, not approved)

The proposed changes replace eight heavily redundant or overlapping entries with six more physically grounded concepts and two social-metaphorical extensions. **This deliberately broadens the concept family beyond strict static spatial relations, and requires team agreement.**

| Replaces | Proposed candidate | Source | Reason |
|---|---|---|---|
| ZH08 | ZH21 托住 | chenfengru:ZH08 | Adds tactile+motor+proprioceptive force grounding while preserving other orientation pairs |
| ZH09 | ZH22 抓握 | chenfengru:ZH09 | Adds CONTACT/CONTROL action and concrete embodied anchor |
| ZH16 | ZH23 推开 | chenfengru:ZH10 | Adds physical FORCE/PATH action grounding |
| ZH17 | ZH24 隔阂 | chenfengru:ZH16 | Adds social/interoceptive metaphor target linked to SEPARATION |
| EN10 | EN21 support | chenfengru:EN09 | Adds force-supported physical action and metaphor bridge |
| EN11 | EN22 grasp | chenfengru:EN11 | Adds highly tactile/manual action and grasp-understanding metaphor |
| EN15 | EN23 lift | chenfengru:EN12 | Adds UP/DOWN physical action and proprioceptive contribution |
| EN20 | EN24 exclusion | chenfengru:EN17 | Adds social/interoceptive target linked to CONTAINER/OUTSIDE |

With these **hypothetical** replacements and their separately drafted scores, `C_sum` bins become {"2":19,"3":13,"6":3,"7":5}; across-set min 2 and max 7, relative high-C counts rise **2 → 8**. This makes six high-C points numerically possible but **does not prove the teacher's quadrant criterion**: S remains NA, and balanced S coverage must be independently verified.

Keep `data/final/concepts_zh20_en20_v01.csv` as immutable baseline. The alternative is in `data/pilots/concepts_zh20_en20_v02_PROPOSED.csv`; it MUST NOT be merged as final without the three contributors' explicit review and a defensible ontology/sense mapping.

## Next experiments

1. Have each of three team members independently rate the 40 current concepts on seven 0–2 channels using the same sense-level guide. Preserve rater-level values. Compare inter-rater disagreement (quadratic-weighted kappa where there is variation) and record uncertain cases.
2. Resolve concrete-versus-metaphorical senses explicitly, especially `失衡/balance`, `阴/阳`, `earshot`, `接触/contact`. Language-specific conventional rules should not automatically inflate the social channel.
3. Add external lexical anchors: <https://wordnet.princeton.edu/> (noun senses and their hypernym paths; prepositions absent), FrameNet (event frames where relevant), Chinese Open Wordnet and/or a documented domain ontology. Select actual **sense IDs**, parent paths and coverage status. Do not infer noun depth for a preposition from a thematically related noun.
4. Once S is validated, compute C and S separately for Chinese and English first, and optionally assess a harmonized bilingual plot. Account for near-translation pairs so they do not overstate independent concept diversity.
5. For HA1 run sensitivity: mean/sum/max C aggregation, dataset min–max versus rank normalization, S depth versus breadth-aware method (when valid), and w = 0.2, 0.5, 0.8. Preserve missing S as NA rather than substituting pseudo-values.

## External resource mismatch

Lancaster norms (<https://www.lancaster.ac.uk/psychology/lsnorms/>) offer six perceptual and five action-effector measurements (0–5), **not** the exact course seven-channel 0–2 scheme. No individual candidate was externally matched to Lancaster in this PR. These pilot scores are **generated, not sourced**.

## Required human review

- [ ] All three contributors review sense definitions and the current 40 ratings.
- [ ] At least one independent source verifies some lexical senses and taxonomy edges.
- [ ] Two or more independent annotators score each pilot item.
- [ ] Joint decision whether a broadened family with social-metaphorical targets remains within assignment scope.
- [ ] Verify at least three genuine **C×S** points per quadrant **before** replacing the v0.1 official list.
