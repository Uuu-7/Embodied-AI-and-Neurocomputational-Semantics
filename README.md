# Embodied AI and Neurocomputational Semantics

EAINS 2026 team project on **spatial relation vocabulary**. Our target is a reviewed dataset of **20 Chinese and 20 English concept senses**. Hu Jinnan has completed one 20-Chinese/20-English candidate selection and seven-channel rating pass in [PR #12](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/12); team approval and C × S analysis remain pending.

## Team

- Xia Yuqi
- Chen Fengru
- Hu Jinnan

## Current contributions

| Member | Candidate contribution | Status |
| --- | --- | --- |
| Xia Yuqi | [Candidate pool](candidates/xiayuqi/candidate_pool_zh20_en20_v01.csv) and [proposal](candidates/xiayuqi/PROPOSAL.md) | Merged; 20 Chinese and 20 English candidates |
| Chen Fengru | [Candidate pool](candidates/chenfengru/candidate_pool_zh20_en20_v01.csv) and [proposal](candidates/chenfengru/PROPOSAL.md) | Merged; 20 Chinese and 20 English candidates |
| Hu Jinnan | [Candidate pool](candidates/hujinnan/candidate_pool_zh20_en20_v01.csv) and [proposal](candidates/hujinnan/PROPOSAL.md) | Merged; 20 Chinese and 20 English candidates |

## Current work

The [nomination comparison](data/audit/term_vote_counts_v01.csv) contains 120 nominations and 110 distinct language-specific written forms. A matching written form is only a possible overlap until its intended senses are checked. The [12-concept pilot audit](data/audit/pilot_concept_audit_v01.csv) samples geometry, direction, path, force, and social extension. Its decisions are provisional. The [pilot report](data/pilots/C_S_PILOT_REPORT.md) explains the review sequence and current limits.

Hu's [S audit of 120 nominations](data/audit/candidate_S_combined_v01.xlsx) found 57 nominations with a comparable noun depth and 63 with `S=NA`. Hu retained eight `NA` nominations and removed same-sense duplicate nominations, yielding a [58-term reviewed pool](data/audit/candidate_S_reviewed_unique_v01.xlsx). Hu then rated all 58 terms on seven horizontal 0–2 channels and marked 40 as `keep` (20 Chinese, 20 English). The [completed C workbook](data/audit/candidate_C_horizontal_scoring_v01.xlsx) includes the full 58-term rating table, an English evaluation summary, and the user-selected 40. This is one contributor's evaluation, not a team consensus dataset.

## Roadmap

| Stage | Work | Reviewable output |
| --- | --- | --- |
| 1. Concept selection audit | Compare the three proposals; check definition, part of speech, intended sense, and external evidence for 10–12 representative concepts. Mark keep, revise, or replace. | Nomination comparison and pilot decision table |
| 2. Seven-feature annotation | Three members independently score the same pilot senses on seven 0–2 channels, recording provenance, reason, and confidence. Resolve disagreements before extending to the remaining candidates. | Separate rater forms, revised scoring guide, pairwise agreement when complete |
| 3. Taxonomy validation | Verify sense-specific parent edges in suitable lexical or domain resources. Record source references; use `NA` where no defensible comparable path exists. | Taxonomy edges and reviewed S values |
| 4. C × S feasibility | Calculate C from actual ratings and S from reviewed paths. Inspect both languages and four-quadrant counts; review sense duplication and any coverage gaps. | Scatter plot, counts, and replacement proposals if needed |
| 5. Final dataset | Agree on 20 Chinese and 20 English senses, examples, seven-feature annotations, and source notes. | Versioned team dataset and data dictionary |
| 6. Course prototype and evaluation | Build the simulator, semantic graph, contrast cases, and reproducible evaluation required by later assignments. | Notebook or app, figures, report, and limitations |

The pilot form files are under [`data/audit/raters/`](data/audit/raters/). Xia has proposed and reviewed all 84 pilot ratings; Chen's and Hu's **pilot forms** remain blank. Hu's separate 58-term C workbook has one completed rating pass, while the S audit supplies noun depths for only the covered senses. Do not report team consensus C, inter-rater agreement, or C × S quadrant counts until the required independent ratings, scope decisions, and S normalization are complete.

## Repository layout

```text
candidates/                  three independent 20-ZH + 20-EN proposals
data/audit/                  nomination comparison, pilot audit, independent rating forms
data/pilots/                 pilot report and workflow status
scripts/                     reproducible comparison and form preparation
```
