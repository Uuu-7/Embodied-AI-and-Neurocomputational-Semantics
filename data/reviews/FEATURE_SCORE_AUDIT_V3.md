# Seven-feature audit of the 40-sense working dataset

The accompanying `feature_score_audit_v3.csv` checks all **280** selected-sense/channel cells against the stated 0–2 rubric. This is an **AI-assisted review of the existing scores**, not 280 new independent human annotations. No numeric score has been changed without new evidence. There are **271 retained cells** and **9 potential disagreements** requiring a team decision. No inter-rater agreement statistic is possible because this file is not a second independent human score sheet.

## Rubric and source labels

- `0`: no typical direct contribution from the channel in the specified literal sense.
- `1`: conditional or secondary direct contribution.
- `2`: characteristic direct contribution.
- `manual`: a value reported from the earlier single rating pass. That source did not record a rater name; it is **not** claimed as Xia's new rating.
- `generated`: a value carried from an AI-assisted draft or re-audit. No value is marked `sourced`, because none was established here from a published sensorimotor norm or published feature annotation.

The CSV records the exact prior source and a score-specific explanation for every cell. Where source confidence was not reported, the audit conservatively uses `low`. The previous `feature_provenance_v2.csv` remains intact so the original origin labels can be recovered.

## Potential disagreements to adjudicate

| Concept ID | Feature | Current | Alternative | Reason for discussion |
|---|---|---:|---|---|
| ZH02 | Proprioceptive | 1 | 0 | A static enclosed region can exist without a body. |
| ZH03 | Proprioceptive | 1 | 0 | An exterior region can exist without embodied viewpoint. |
| ZH16 | Proprioceptive | 1 | 0 | A route noun does not entail a traveler. |
| ZH18 | Tactile | 1 | 0 | Pure geometric tangency does not entail felt contact. |
| EN11 | Proprioceptive | 2 | 0 | Robot joint sensing is an analogue; decide whether the rubric includes it. |
| EN12 | Proprioceptive | 1 | 0 | Static containment does not entail bodily position. |
| EN15 | Motor | 1 | 0 or 2 | The confirmed definition includes static and directional readings. |
| EN15 | Proprioceptive | 1 | 0 | The static reading does not require body orientation. |
| EN17 | Proprioceptive | 1 | 0 | A route noun does not entail a traveler. |

These are review flags, not adopted replacements. The working v3 table and HA1 calculations keep the current values. The team should record the chosen sense policy and a reason for each decision, then rerun HA1 if a score changes. The 25 reported S paths also remain separate from this C audit and still need source verification.
