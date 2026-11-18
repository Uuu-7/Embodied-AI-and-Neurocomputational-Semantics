# Integrated dataset v2: source and adjudication record

**Scope:** 20 Chinese and 20 English selected spatial senses. The original candidate proposals under `candidates/` and the v1 release remain unchanged. This v2 is a reconciled working dataset, **not** a record of three independent seven-channel ratings or unanimous team approval.

## Inputs and exact changes

1. `spatial_relations_zh20_en20_v1.csv` is the selected 40-sense inventory and prior-score baseline.
2. [Chen Fengru's updated PR #14](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/14) supplied a complete AI-assisted C re-audit draft, a 26-row change log, and rationale. Its three source files are preserved under `data/reviews/`. The narrowed `EN19 balance` bodily sense and S=NA were retained.
3. [Hu Jinnan's PR #14 review](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/14#issuecomment-6961983401) prompted Chen to revise eight feature values: Social 1→0 for ZH11/ZH12 and Motor 1→0 for ZH02, ZH03, ZH16, EN04, EN12, and EN17. Chen's updated draft implements all eight; the route-noun decisions remain proposals awaiting independent review. The integrator adopted the updated draft without further feature-score edits.

The resulting v2 matches Chen's **updated** draft in all 280 feature cells and differs from v1 in **42 feature cells across 26 rows**. `C_sum` and `C_unit` were recomputed. `feature_provenance_v2.csv` tracks all **280** channel values with the v1, Chen-draft, and final values, source, reason, confidence, and review status. `build_v2.py` reproduces both output CSVs from the preserved inputs.

## Sense and S safeguards

- ZH18 geometric `接触` retains Tactile=1. Its exact Chinese lexical sense should be checked against a dictionary or mathematical corpus; a material contact example is not by itself proof of the geometric lexicalization.
- EN11 `posture` retains Proprioceptive=2. The robot sentence illustrates joint-state feedback as a bodily-position analogue; the construct interpretation remains reviewable.
- EN19 `balance` has the narrower bodily-upright definition and illustrative climber sentence. Its previous taxonomy path belonged to a broader or different sense; S, synset, and path remain NA until a compatible source is found.
- **25** other S depths and paths are carried from v1/PR #12 and have not been independently revalidated here. The remaining **15** senses have S=NA. NA is missing evidence, not minimum specificity.

## C×S coverage

The old descriptive raw cutoffs (`C_sum >= 5`, `S_depth >= 6`) give low/low **12**, low/high **12**, high/low **1**, high/high **0**, and S=NA **15**. The course HA1 graph uses separate min–max normalization and boundaries at 0.5; its counts are **8**, **10**, **5**, **2**, and **15**. These are different definitions of quadrants. Neither is a basis for changing sense-specific scores solely to fill a cell.

## Reproduce and next review

Run `python data/final/build_v2.py` to regenerate the 40-row dataset and 280-row feature provenance file from the preserved inputs. The team should independently verify the C rubric, the disputed lexical senses, and the 25 carried S paths before treating this as final validated annotation or submitting it as joint work.
