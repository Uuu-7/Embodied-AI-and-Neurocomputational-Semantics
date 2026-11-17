# Final bilingual spatial relation concept selection

**Selection version:** v0.1, 2026-11-17. **Source snapshot:** `main` after merging [Chen's PR #1](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/1), [Xia's PR #2](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/2), and [Hu's standardized PR #4](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/4), commit `d56870b33726ec0185dd2a224ab07f3c5eb75e77`.

The team working set in [`concepts_zh20_en20_v01.csv`](concepts_zh20_en20_v01.csv) has **20 Chinese and 20 English senses**. [`nomination_counts_v01.csv`](nomination_counts_v01.csv) records all nominations, counts, contributors, and decisions. This is the final **selection of concepts** for subsequent team annotation; the seven feature scores, C, S, and examples remain pending review.

## Counting rule

- Count one vote per contributor for the same **language and normalized term**. Normalize Unicode with NFKC, trim and collapse whitespace, and case-fold English. Do not combine votes across languages.
- Retain the target-sense definitions beside each term. Near synonyms with different wording or part of speech remain separate nominations; they do not acquire extra votes by being semantically related.
- There are 60 nomination rows per language, 55 unique terms per language: **five terms with two votes, none with three votes, and fifty with one vote** in each language.
- Include every two-vote term. Fill the remaining fifteen places per language from one-vote candidates using spatial-relation scope, distinct relation types, clear target senses, reported lexical anchors, and variation in grounding channels. The tie-break is editorial and is recorded below; a one-vote selection is not presented as a majority choice.

## Chinese selection

| Term | Votes | Proposed by | Selection reason |
|---|---:|---|---|
| 内部 | 2 | xiayuqi, hujinnan | Nominated independently by two contributors. |
| 环绕 | 2 | chenfengru, xiayuqi | Nominated independently by two contributors. |
| 边界 | 2 | chenfengru, hujinnan | Nominated independently by two contributors. |
| 阴 | 2 | chenfengru, xiayuqi | Nominated independently by two contributors. |
| 阳 | 2 | chenfengru, xiayuqi | Nominated independently by two contributors. |
| 上方 | 1 | xiayuqi | Vertical relation; pairs with 下方. |
| 下方 | 1 | xiayuqi | Vertical relation; pairs with 上方. |
| 前方 | 1 | xiayuqi | Front/back reference frame; pairs with 后方. |
| 后方 | 1 | xiayuqi | Front/back reference frame; pairs with 前方. |
| 左侧 | 1 | xiayuqi | Lateral reference frame; pairs with 右侧. |
| 右侧 | 1 | xiayuqi | Lateral reference frame; pairs with 左侧. |
| 外部 | 1 | xiayuqi | Containment contrast with 内部. |
| 中心 | 1 | hujinnan | Center relation with a reported noun-sense path. |
| 边缘 | 1 | xiayuqi | Periphery contrast with 中心. |
| 之间 | 1 | xiayuqi | Intervening spatial relation. |
| 相邻 | 1 | xiayuqi | Adjacency relation distinct from distance alone. |
| 距离 | 1 | hujinnan | Measurable spatial interval with a reported noun-sense path. |
| 路径 | 1 | hujinnan | Route relation with a reported noun-sense path. |
| 接触 | 1 | hujinnan | Tactile topological relation with a reported noun-sense path. |
| 失衡 | 1 | chenfengru | Adds proprioceptive force/balance variation; noun sense clarified manually. |

## English selection

| Term | Votes | Proposed by | Selection reason |
|---|---:|---|---|
| boundary | 2 | chenfengru, hujinnan | Nominated independently by two contributors. |
| center | 2 | chenfengru, hujinnan | Nominated independently by two contributors. |
| contact | 2 | chenfengru, hujinnan | Nominated independently by two contributors. |
| path | 2 | chenfengru, hujinnan | Nominated independently by two contributors. |
| proximity | 2 | chenfengru, hujinnan | Nominated independently by two contributors. |
| inside | 1 | xiayuqi | Containment relation; pairs with outside. |
| outside | 1 | xiayuqi | Containment relation; pairs with inside. |
| above | 1 | xiayuqi | Vertical relation; pairs with below. |
| below | 1 | xiayuqi | Vertical relation; pairs with above. |
| in front of | 1 | xiayuqi | Front/back reference frame; pairs with behind. |
| behind | 1 | xiayuqi | Front/back reference frame; pairs with in front of. |
| to the left of | 1 | xiayuqi | Lateral reference frame; pairs with to the right of. |
| to the right of | 1 | xiayuqi | Lateral reference frame; pairs with to the left of. |
| between | 1 | xiayuqi | Intervening spatial relation. |
| adjacency | 1 | hujinnan | Topological relation with a reported noun-sense path. |
| earshot | 1 | hujinnan | Adds a direct auditory spatial range. |
| balance | 1 | chenfengru | Adds proprioceptive force/balance variation. |
| across | 1 | xiayuqi | Path relation crossing an intervening region. |
| through | 1 | xiayuqi | Path relation traversing an interior. |
| at the edge of | 1 | xiayuqi | Periphery contrast with center. |

## How to use the dataset

- `source_proposals` and `source_candidate_ids` trace each selected word to its nominations. The chosen definition is identified separately; the source may have other suggested senses.
- `category_parent_proposed` and `channels_to_review` are **provisional labels**, not a validated taxonomy or numeric ratings.
- The seven `*_0_2` fields, `feature_provenance`, `C_score`, and `S_score` are intentionally blank. Hu's source workbook contains AI preliminary C estimates and reported noun-taxonomy paths, but these are not substituted for independent group annotations.
- `lexical_source_reported=YES` reports what the chosen candidate row says; it is not a fresh verification by all three members. Before calculating S, recheck the actual noun sense, parent path, and cross-language comparability. Record missing or incomparable S as NA.
- Some selected terms are prepositions, locatives, or a force/balance extension. Their S may require a documented domain taxonomy instead of a noun-only WordNet depth. Do not invent comparable depths or tune features just to fill C × S quadrants.
- The selection is frozen as v0.1 for team work. Revise it through a versioned change with a recorded reason if review reveals a sense error, duplicate, or missing relation type.

## Checks

- 20 Chinese and 20 English selected rows; all five two-vote terms in each language are included.
- No duplicate normalized term within a language in the final CSV.
- Every selected row has a definition, source candidate ID, nomination count, and selection reason.
- No unreviewed C/S or seven-channel numeric score is presented as final.

