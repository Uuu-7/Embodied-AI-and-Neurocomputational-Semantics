# Full 40-Concept Seven-Feature Grounding Draft

**Date:** 2026-11-17  
**Author / working set:** Chen Fengru — 20 Chinese + 20 English concepts  
**Status:** AI-assisted scores awaiting human review. This is a standalone 40-concept working dataset, not externally validated independent manual annotation.

## Scope

This submission contains **only 40 selected legacy concept candidates**, with no separate smaller subset and no additional concepts. The vocabulary was retained from the earlier 20 Chinese + 20 English selection (preserved in `archive/chenfengru-pr7-original-40word-pilot-20261117:data/final/concepts_zh20_en20_v01.csv`). The current team `main` retains only the three contributor proposal pools, so the selection represented here is a **working draft for review**, not a newly ratified team final list.

- **40/40** concepts have seven numeric feature scores in the integer range 0–2.
- **280/280** long-format feature decisions have confidence, per-feature reasoning and explicitly labeled semantic layers.
- **10** source definitions are clarified in `scored_target_definition_en`; their original definitions are preserved alongside the refinements, and `sense_review_status` flags this. These clarifications are proposals rather than independently validated dictionary changes.
- `S_score` stays empty (status `NA_taxonomy_not_verified`). Do not report actual C×S quadrant coverage until independently sourced taxonomy paths exist.

## Seven-channel rubric

Score only the specified **Layer 1 (target literal / physical or social sense)**: **0** = no typical direct contribution; **1** = context-dependent or secondary direct grounding; **2** = characteristic direct mode of identifying or enacting the meaning.

The columns are Visual, Auditory, Tactile, Motor, Proprioceptive, Interoceptive, Social, each scored 0–2. `C_unit = sum(features) / 14` uses the theoretical score range (0–14), **not** min–max normalization across the concepts.

A **Layer 2 (metaphorical or extended sense)** is retained in each explanation but never silently included in the Layer 1 score. Example: physical boundary = Social 0, while interpersonal boundary is a separately documented abstract extension.

### Decisions needing review
- **阴 / 阳**: Proprioceptive=0. Social=1 is **low confidence** and refers to cultural conventions for geographic naming, not their philosophical/symbolic extensions. If Social is restricted to interpersonal relationships, re-evaluate these scores.
- **失衡 / balance**: Proprioceptive=2 for the refined bodily-stability target sense. Vestibular perception is not automatically synonymous with interoception.
- **boundary / contact / balance / 失衡**: Social=0 for the physical target sense; relevant social/affective metaphors are Layer 2 only.
- **earshot**: Auditory=2 because the audible range of a voice is definitional.
- **Body-relative prepositions and regions**: some Proprioceptive=1 are context-dependent and require review under a common ego/allocentric frame rule.

## Score grid

| ID | Term | V | A | T | M | P | I | S | Sum | C_unit |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ZH01 | 内部 | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 5 | 0.357 |
| ZH02 | 环绕 | 2 | 0 | 0 | 2 | 1 | 0 | 0 | 5 | 0.357 |
| ZH03 | 边界 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 |
| ZH04 | 阴 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0.143 |
| ZH05 | 阳 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0.143 |
| ZH06 | 上方 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 |
| ZH07 | 下方 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 |
| ZH08 | 前方 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 |
| ZH09 | 后方 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 |
| ZH10 | 左侧 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 |
| ZH11 | 右侧 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 |
| ZH12 | 外部 | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 5 | 0.357 |
| ZH13 | 中心 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0.143 |
| ZH14 | 边缘 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 |
| ZH15 | 之间 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0.143 |
| ZH16 | 相邻 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0.143 |
| ZH17 | 距离 | 2 | 0 | 0 | 1 | 1 | 0 | 0 | 4 | 0.286 |
| ZH18 | 路径 | 2 | 0 | 0 | 1 | 1 | 0 | 0 | 4 | 0.286 |
| ZH19 | 接触 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 |
| ZH20 | 失衡 | 1 | 0 | 1 | 1 | 2 | 0 | 0 | 5 | 0.357 |
| EN01 | boundary | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 |
| EN02 | center | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0.143 |
| EN03 | contact | 1 | 0 | 2 | 1 | 0 | 0 | 0 | 4 | 0.286 |
| EN04 | path | 2 | 0 | 0 | 1 | 1 | 0 | 0 | 4 | 0.286 |
| EN05 | proximity | 2 | 0 | 0 | 1 | 1 | 0 | 0 | 4 | 0.286 |
| EN06 | inside | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 5 | 0.357 |
| EN07 | outside | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 5 | 0.357 |
| EN08 | above | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 |
| EN09 | below | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 |
| EN10 | in front of | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 |
| EN11 | behind | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 |
| EN12 | to the left of | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 |
| EN13 | to the right of | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 |
| EN14 | between | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0.143 |
| EN15 | adjacency | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0.143 |
| EN16 | earshot | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0.143 |
| EN17 | balance | 1 | 0 | 1 | 2 | 2 | 0 | 0 | 6 | 0.429 |
| EN18 | across | 2 | 0 | 0 | 1 | 1 | 0 | 0 | 4 | 0.286 |
| EN19 | through | 2 | 0 | 0 | 2 | 1 | 0 | 0 | 5 | 0.357 |
| EN20 | at the edge of | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 |

Score-sum frequencies: 2: 9; 3: 17; 4: 6; 5: 7; 6: 1.

## Submitted files

- `data/ratings/chenfengru_40concepts_scores_v01_DRAFT.csv` — exactly 40 rows, original and clarified sense definitions, seven scores, C, missing S, provenance, and two-layer semantic notes.
- `data/ratings/chenfengru_40concepts_feature_rationales_v01_DRAFT.csv` — exactly 280 detailed feature-scoring decisions, each with individual reason, confidence and both semantic layers.
- `data/ratings/chenfengru_40concepts_method_and_review.md` — this document.

## Research integrity and remaining work

1. AI-assisted estimates are **not** independent blinded human ratings; don't compute independent-annotator agreement treating these rows as such.
2. The precise sense definitions, especially those clarified for scoring, still need review by the team. Seven-point profiles are not lexical norms extracted from OpenHowNet, Chinese Open Wordnet, or Princeton WordNet.
3. Check consistency among near-translation pairs, static position vs movement event interpretations, and culturally learned conventions.
4. Derive specificity **S** only from inspectable sense-specific taxonomic paths; unsupported senses remain NA.
5. Only after those checks should the group decide the final 20+20 inventory, generate normalized C×S plots, run quadrant coverage and sensitivity analyses. Do not edit ratings merely to force an even plot.

**Only the three full-40-concept files above are proposed in this change.**
