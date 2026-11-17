# Target-sense ↔ C grounding consistency re-audit (proposed v1.1)

**2026-11-17. Scope: 20 Chinese + 20 English concepts, no additions or deletions.**  
**Status: AI-assisted proposed corrections, awaiting independent human/team review. No direct edits to main and no merge.**

## Source and change control

- Baseline dataset: `main:data/final/spatial_relations_zh20_en20_v1.csv` @ `b9c73dcca9ec03f0041c90dba9a06eb479bfd938`.
- Original v1 remains unchanged; the proposed complete 40-row replacement candidate is `data/reviews/chenfengru_spatial_relations_zh20_en20_v1_1_C_reaudit_DRAFT.csv`.
- Every changed row appears in `data/reviews/chenfengru_C_reaudit_change_log_v1_1.csv`, including prior/new 7D vector, C, source, rationale, target sense and metaphorical extension.
- **24** rows have revised scores; **16** unchanged. **1** target-sense definition narrowed (EN19 balance), with its previous S path intentionally cleared pending sense-specific revalidation.
- **All seven channels still use** `0` no typical direct grounding, `1` conditional/secondary direct grounding, `2` characteristic/direct grounding. `C_unit = C_sum / 14`. Raters and word senses have not been independently validated.

## Critical semantic issues corrected

1. **Non-core senses vs mere contexts**: a place or left side is not inherently auditory/tactile; conditional direct cues must not receive automatic 2. E.g. `位置` and `左侧`.
2. **Static state vs action**: `alignment`, `proximity`, and `separation` are spatial states or relations, not the events 'align', 'approach', or 'separate'. Active motor values were lowered where the selected noun definition did not entail an action.
3. **Physical vs social polysemy**: Social for physical `边界`, `接触`, `contact`, `distance`, `proximity`, and `separation` was adjusted to reflect the specified target sense. Metaphorical/social extensions are documented as Layer 2, not included in the score.
4. **Bodily vs mechanical equilibrium**: `EN19 balance` is proposed as bodily upright balance to match the climber example. Its old reported S=6 and synset path were **not reused**; S=NA must be independently reverified. `托住` and `support` can be static material support and therefore do not require human proprioception or motor=2.
5. **Cross-language parallel semantics**: `位置/location`, `距离/distance`, and `路径/path` are treated consistently where target meanings match; this is an internal consistency check, **not proof of equal empirically observed grounding**.
6. **Culture-specific geography**: `阴/阳` remain Social=1 (low confidence) for learned conventional geographic labeling and Proprioceptive=0; Visual is conditional=1 because geographic side recognition alone does not establish the traditional name. This is disputed if the team defines Social as only interpersonal relations.

## Full revised C grid (proposal)

| ID | Term | V | A | T | M | P | I | S | Sum | C_unit | S_depth |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| ZH01 | 位置 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 4 | 0.286 | 3 |
| ZH02 | 内部 | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 5 | 0.357 | 5 |
| ZH03 | 外部 | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 5 | 0.357 | NA |
| ZH04 | 边界 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 5 |
| ZH05 | 中心 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 5 |
| ZH06 | 前面 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 6 |
| ZH07 | 左侧 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 4 | 0.286 | 6 |
| ZH08 | 坡度 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 4 | 0.286 | 5 |
| ZH09 | 上方 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 | NA |
| ZH10 | 下方 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 | NA |
| ZH11 | 阴 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0.143 | NA |
| ZH12 | 阳 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0.143 | NA |
| ZH13 | 之间 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0.143 | NA |
| ZH14 | 距离 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 0.214 | 6 |
| ZH15 | 空隙 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 6 |
| ZH16 | 路径 | 2 | 0 | 0 | 1 | 1 | 0 | 0 | 4 | 0.286 | 5 |
| ZH17 | 环绕 | 2 | 0 | 0 | 2 | 1 | 0 | 0 | 5 | 0.357 | NA |
| ZH18 | 接触 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 7 |
| ZH19 | 对称 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 7 |
| ZH20 | 托住 | 2 | 0 | 2 | 1 | 0 | 0 | 0 | 5 | 0.357 | NA |
| EN01 | location | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 4 | 0.286 | 3 |
| EN02 | boundary | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 6 |
| EN03 | center | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 5 |
| EN04 | proximity | 2 | 1 | 0 | 1 | 0 | 0 | 0 | 4 | 0.286 | 8 |
| EN05 | distance | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 0.214 | 6 |
| EN06 | gap | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 5 |
| EN07 | adjacency | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 8 |
| EN08 | alignment | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 5 |
| EN09 | angle | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.214 | 5 |
| EN10 | separation | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0.143 | 7 |
| EN11 | posture | 2 | 0 | 0 | 2 | 2 | 0 | 0 | 6 | 0.429 | 5 |
| EN12 | inside | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 5 | 0.357 | NA |
| EN13 | above | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 | NA |
| EN14 | below | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0.214 | NA |
| EN15 | across | 2 | 0 | 0 | 1 | 1 | 0 | 0 | 4 | 0.286 | NA |
| EN16 | through | 2 | 0 | 0 | 2 | 1 | 0 | 0 | 5 | 0.357 | NA |
| EN17 | path | 2 | 0 | 0 | 1 | 1 | 0 | 0 | 4 | 0.286 | 5 |
| EN18 | contact | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 4 | 0.286 | 6 |
| EN19 | balance | 1 | 0 | 1 | 2 | 2 | 0 | 0 | 6 | 0.429 | NA |
| EN20 | support | 1 | 0 | 2 | 1 | 0 | 0 | 0 | 4 | 0.286 | NA |

## C×S descriptive coverage (not validated outcomes)

Thresholds carried forward unchanged from v1: High C when `C_sum >= 5`, High S when `S_depth >= 6`. These are discretionary cutoffs, not empirically calibrated thresholds.

| Group | Before (v1) | Proposed (v1.1) |
|---|---:|---:|
| low_C_low_S | 8 | 11 |
| low_C_high_S | 7 | 12 |
| high_C_low_S | 5 | 2 |
| high_C_high_S | 6 | 0 |
| NA_S | 14 | 15 |

Proposed quadrants by language: Chinese {"low_C_low_S":5,"low_C_high_S":6,"high_C_low_S":1,"high_C_high_S":0,"NA_S":8}; English {"low_C_low_S":6,"low_C_high_S":6,"high_C_low_S":1,"high_C_high_S":0,"NA_S":7}. Counts reflect *only* reported paths and provisional C. `NA_S` is missingness, not low specificity.

Sensitivity of proposed coverage:
- C>=4, S>=6: {"LL":6,"LH":9,"HL":7,"HH":3}
- C>=5, S>=6: {"LL":11,"LH":12,"HL":2,"HH":0}
- C>=6, S>=6: {"LL":12,"LH":12,"HL":1,"HH":0}
- C>=5, S>=7: {"LL":18,"LH":5,"HL":2,"HH":0}

**Do not restore questionable C scores just to increase quadrant counts.** Check whether the revised inventory remains viable, and if necessary later reselect senses or obtain better-documented measures.

## Known limitations and human-review checklist

- The revised scores are AI-assisted reasoning grounded in the **selected definitions and examples**, not downloaded perceptual norm measurements, nor three independent human annotations.
- `ZH18 接触` is a *geometrical point/line tangency* in the current target/example. Is this lexicalized as `接触` rather than `相切`? Review against a Chinese dictionary or mathematical corpus. A material tangency may justify Tactile=1, but not automatically Tactile=2 or Social=1.
- `EN19 balance` has a newly narrowed definition and now S=NA. Verify the English lexical sense and find a real compatible taxonomy source before restoring S.
- `EN11 posture` Motor=2/Proprioceptive=2 reflects bodily pose control and position feedback, but the example is a robot; make clear whether robot joint sensing qualifies as proprioceptive analogue.
- `阴/阳` Social=1 is explicitly low-confidence and requires a team-wide definition of the Social axis.
- 25 previously documented S paths were **carried forward from main without independently verifying them**. Confirm actual source sense and hierarchy before claiming the S values are validated.
- Data contains only direct spatial/force senses; strong visual dominance and low interoceptive variability remain potential construct-coverage limitations.
- Seek independent rating and adjudication. When a definition is changed, preserve the original identity, review evidence and recompute specificity instead of silently keeping an unrelated old S path.

### File list
1. `data/reviews/chenfengru_spatial_relations_zh20_en20_v1_1_C_reaudit_DRAFT.csv` — complete 40-concept corrected candidate, same original columns.
2. `data/reviews/chenfengru_C_reaudit_change_log_v1_1.csv` — exact row-by-row changes with both semantic layers and preserved old sources.
3. `data/reviews/chenfengru_C_reaudit_report_v1_1.md` — this method/review report.
