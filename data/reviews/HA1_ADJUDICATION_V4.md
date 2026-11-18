# HA1 v4 review decisions

This record turns the nine flagged v3 channel cells into explicit choices for the HA1 submission. The starting points are the [v3 audit](feature_score_audit_v3.csv), [Chen Fengru's C review](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/17#issuecomment-6976080360), and [Chen Fengru's parent/S review](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/17#issuecomment-6976372653). The choices are editorial integration of the available review, not a claim of a new three-rater consensus. The [v4 audit](feature_score_audit_v4.csv) gives every one of the 280 values, its reason, source, and confidence.

| Sense | Channel | v3 → v4 | Decision for selected literal sense |
|---|---|---:|---|
| ZH02 内部 | Proprioceptive | 1 → 0 | An enclosed region need not be perceived through body-position feedback. |
| ZH03 外部 | Proprioceptive | 1 → 0 | An exterior region need not be perceived through body-position feedback. |
| EN12 inside | Proprioceptive | 1 → 0 | A static containment relation does not entail body position. |
| ZH16 路径 | Proprioceptive | 1 → 1 | Egocentric route experience may conditionally contribute; traversing it is not entailed, so Motor stays 0. Confidence remains low. |
| EN17 path | Proprioceptive | 1 → 1 | The same route-noun policy as ZH16. Confidence remains low. |
| EN11 posture | Proprioceptive | 2 → 2 | Joint-position feedback is characteristic of posture; the robot example is an engineering analogue. |
| ZH18 接触 | Tactile | 1 → 1 | Material contact can conditionally supply touch, but ideal tangency does not require it. This is the explicit HA0 uncertainty row; confidence remains low. |
| EN15 across | Motor | 1 → 2 | The target sense is narrowed to crossing a region from one side to the other, matching the existing moving-robot example and [Oxford's movement sense](https://www.oxfordlearnersdictionaries.com/definition/english/across_1). |
| EN15 across | Proprioceptive | 1 → 1 | Body-relative feedback may accompany crossing, but is not required in every event. |

The EN15 wording is a new editorial paraphrase of the Oxford sense. It has not been separately confirmed by Xia Yuqi. The original 40-word inventory was confirmed by Xia in the project conversation; that earlier confirmation should not be stretched to the new wording.

The parent labels stay the same. `spatial_arrangement` now includes geometric properties such as slope and angle; `spatial_interval_relation` explicitly includes an opening. These are pedagogical category parents and do not generate S depths. Twenty-five inherited S paths retain their recorded depth after node-count validation in the notebook; fifteen S values remain NA. Chen's S comments were targeted triage, not exhaustive source verification. Sense-specific COW/OMW synset validation remains an evidence limit and is not represented as completed here.

Changes in C are made for sense fidelity, not quadrant balancing. Recompute all normalized C, A values, figures, and interpretation from v4; do not copy the v3 counts.
