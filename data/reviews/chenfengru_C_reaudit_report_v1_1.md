# HW1 — Target-Sense & C Grounding Re-audit (v1.1, after Hu review)

**Updated: 2026-11-18.** Full selected set remains 20 Chinese + 20 English, **no additions or removals**. This is an AI-assisted, human-review-pending draft; `main` is unchanged and the PR is not to be merged automatically.

## Review source

This revision follows [Hu Jinnan's PR #14 comments](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/14#issuecomment-6961983401). Hu **did not approve** the previous PR as-is. This update addresses the requested changes but does **not** claim new approval or independent manual annotations.

| Concept | Channel | Previous PR #14 | Updated | Decision rationale |
|---|---|---:|---:|---|
| 阴 (ZH11) | Social | 1 | 0 | Traditional geographic naming does not directly instantiate a social relationship |
| 阳 (ZH12) | Social | 1 | 0 | Same scope restriction |
| 内部 (ZH02) | Motor | 1 | 0 | Spatial region need not be entered or explored |
| 外部 (ZH03) | Motor | 1 | 0 | Static region does not entail exiting |
| proximity (EN04) | Motor | 1 | 0 | Static short distance does not entail approaching |
| inside (EN12) | Motor | 1 | 0 | Static containment relation does not entail entering |
| 路径 (ZH16) | Motor | 1 | 0 | Route noun is not an enacted movement |
| path (EN17) | Motor | 1 | 0 | Same rule for matched English sense |

**Confirmed without changing their scores:** `接触` ZH18 Tactile=1 and Social=0 (but geometric lexical usage needs checking); `posture` EN11 Proprioceptive=2 (robot's joint-position feedback is an engineering analogue of bodily proprioception); `balance` EN19 has a narrowed bodily target sense, with S=NA until its correct path is independently verified.

**Semantic policy:** Layer 1 is the **exact target sense** and determines each 0/1/2 score. Layer 2 records metaphorical or extended meanings, including social meanings of physical terms, **without adding those values to the selected sense**.

## Scoring scheme and provenance

0: not a typical direct grounding route; 1: conditional/secondary direct contribution; 2: characteristic/direct route of identifying or enacting the chosen sense. Columns: Visual, Auditory, Tactile, Motor, Proprioceptive, Interoceptive, Social. `C_sum = sum(seven)`; `C_unit = C_sum / 14`.

Relative to `main` baseline @ `b9c73dcca9ec03f0041c90dba9a06eb479bfd938`, **26/40** concept rows have changed vectors or target sense; 14 do not. Relative to the prior PR #14 version, **8 rows** received additional changes: ZH02, ZH03, ZH11, ZH12, ZH16, EN04, EN12, EN17. Only one target sense was narrowed (`EN19 balance`). Historical C provenance is preserved in the change log, and modified rows are labeled AI-assisted and pending team review.

There are **25** rows with previously **reported** S paths, **15** with S=NA; no newly verified S depth is claimed. The `balance` path was cleared because the narrowed bodily sense requires a new matched taxonomy check.

## Full 40-item proposed scoring matrix

| ID | Term | Visual | Auditory | Tactile | Motor | Proprio. | Intero. | Social | C sum | C unit | S depth |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| ZH01 | 位置 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 4 | 0.286 | 3 |
| ZH02 | 内部 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 4 | 0.286 | 5 |
| ZH03 | 外部 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 4 | 0.286 | NA |
| ZH04 | 边界 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 5 |
| ZH05 | 中心 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 5 |
| ZH06 | 前面 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 6 |
| ZH07 | 左侧 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 4 | 0.286 | 6 |
| ZH08 | 坡度 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 4 | 0.286 | 5 |
| ZH09 | 上方 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 | NA |
| ZH10 | 下方 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 | NA |
| ZH11 | 阴 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0.071 | NA |
| ZH12 | 阳 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0.071 | NA |
| ZH13 | 之间 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0.143 | NA |
| ZH14 | 距离 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 0.214 | 6 |
| ZH15 | 空隙 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 6 |
| ZH16 | 路径 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 | 5 |
| ZH17 | 环绕 | 2 | 0 | 0 | 2 | 1 | 0 | 0 | 5 | 0.357 | NA |
| ZH18 | 接触 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 7 |
| ZH19 | 对称 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 7 |
| ZH20 | 托住 | 2 | 0 | 2 | 1 | 0 | 0 | 0 | 5 | 0.357 | NA |
| EN01 | location | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 4 | 0.286 | 3 |
| EN02 | boundary | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 6 |
| EN03 | center | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 5 |
| EN04 | proximity | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 0.214 | 8 |
| EN05 | distance | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 0.214 | 6 |
| EN06 | gap | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 5 |
| EN07 | adjacency | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 8 |
| EN08 | alignment | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 5 |
| EN09 | angle | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 5 |
| EN10 | separation | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0.143 | 7 |
| EN11 | posture | 2 | 0 | 0 | 2 | 2 | 0 | 0 | 6 | 0.429 | 5 |
| EN12 | inside | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 4 | 0.286 | NA |
| EN13 | above | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 | NA |
| EN14 | below | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 | NA |
| EN15 | across | 2 | 0 | 0 | 1 | 1 | 0 | 0 | 4 | 0.286 | NA |
| EN16 | through | 2 | 0 | 0 | 2 | 1 | 0 | 0 | 5 | 0.357 | NA |
| EN17 | path | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 | 5 |
| EN18 | contact | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 4 | 0.286 | 6 |
| EN19 | balance | 1 | 0 | 1 | 2 | 2 | 0 | 0 | 6 | 0.429 | NA |
| EN20 | support | 1 | 0 | 2 | 1 | 0 | 0 | 0 | 4 | 0.286 | NA |

## C × S feasibility (descriptive only)

For direct comparability with `main`, first use its **raw-score** descriptive thresholds `C_sum ≥ 5` and `S_depth ≥ 6`. These are **different** from HA1's dataset min–max normalization with 0.5 axes.

| Quadrant | Main v1 | Revised PR #14 |
|---|---:|---:|
| low_C_low_S | 8 | 12 |
| low_C_high_S | 7 | 12 |
| high_C_low_S | 5 | 1 |
| high_C_high_S | 6 | 0 |
| NA_S | 14 | 15 |

Revised Chinese: {"low_C_low_S":6,"low_C_high_S":6,"high_C_low_S":0,"high_C_high_S":0,"NA_S":8}. Revised English: {"low_C_low_S":6,"low_C_high_S":6,"high_C_low_S":1,"high_C_high_S":0,"NA_S":7}.

Sensitivity counts on supported S rows, listed as `LL/LH/HL/HH`:
- Raw C≥4, S≥6: {"LL":8,"LH":10,"HL":5,"HH":2}
- Raw C≥5, S≥6: {"LL":12,"LH":12,"HL":1,"HH":0}
- Raw C≥6, S≥6: {"LL":12,"LH":12,"HL":1,"HH":0}
- Raw C≥5, S≥7: {"LL":19,"LH":5,"HL":1,"HH":0}

**HW1/HA1-compatible diagnostic:** After min–max scaling the *revised dataset*, the observed score sum range is 1–6 (equivalent to C mean 0.143–0.857) and supported S range is 3–8. A 0.5 cutoff produces {"LL":8,"LH":10,"HL":5,"HH":2} quadrants for the 25 supported S senses. This result is **not** the same metric as the raw-threshold table. Recompute against any later team-approved dataset; do not mix these two views.

No scores were inflated to fill the four quadrants. In particular, failure of the raw-threshold four-quadrant coverage is a genuine finding, not a computation error.

## HW1 follow-up checks (remaining)

1. [ ] Obtain teammate confirmation of the 8 revised values; Hu's written requests were followed, but **no new sign-off has been recorded**.
2. [ ] Independently review `路径/path` Proprioceptive=1 despite Motor=0, and other egocentric positional aids.
3. [ ] Verify whether strict tangent contact should be labelled `接触` or `相切`; keep Tactile=1 as a provisional score.
4. [ ] Verify the narrowed `balance` target and a matching noun taxonomy path; missing S is **NA**, not zero.
5. [ ] Confirm the 25 reported S paths and independently review the other provisional 7D ratings; current source is a mixture of single-pass, AI-assisted, and draft data.
6. [ ] Once scores are approved, rerun the HA1 notebook against the approved version and keep raw-threshold vs min–max quadrant methods distinct. Do not claim that a draft PR or working notebook is an LMS submission.

## Files
- `data/reviews/chenfengru_spatial_relations_zh20_en20_v1_1_C_reaudit_DRAFT.csv` — complete 40-row proposed scores and C/S status;
- `data/reviews/chenfengru_C_reaudit_change_log_v1_1.csv` — detailed comparison to immutable original `main` with Layer 1 and Layer 2 notes;
- `data/reviews/chenfengru_C_reaudit_report_v1_1.md` — this report.
