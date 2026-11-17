# Embodied AI and Neurocomputational Semantics

EAINS 2026 team project on **spatial relation vocabulary**. We are building a bilingual concept dataset and a reproducible computational prototype for studying grounding, category specificity, image schemas, and related semantic extensions. Model scores are transparent estimates based on documented inputs; they are not direct measurements of human understanding.

## Team

- Xia Yuqi
- Chen Fengru
- Hu Jinnan

## Scope

The selected working set contains **20 Chinese and 20 English concept senses** from three independent candidate pools. A record represents a specified sense in context, so similar spellings, translations, and literal or extended uses are reviewed separately. The two languages need not form 20 exact translation pairs. A complete manual first pass of seven feature ratings, examples, and C/S scores is available for peer review.

## Current contributions

| Member | Candidate contribution | Status |
| --- | --- | --- |
| Xia Yuqi | [Candidate pool](candidates/xiayuqi/candidate_pool_zh20_en20_v01.csv) and [proposal](candidates/xiayuqi/PROPOSAL.md) | Merged; 20 Chinese and 20 English candidates |
| Chen Fengru | [Candidate pool](candidates/chenfengru/candidate_pool_zh20_en20_v01.csv) and [proposal](candidates/chenfengru/PROPOSAL.md) | Merged; 20 Chinese and 20 English candidates |
| Hu Jinnan | [Candidate pool](candidates/hujinnan/candidate_pool_zh20_en20_v01.csv), [proposal](candidates/hujinnan/PROPOSAL.md), and [source workbook](candidates/hujinnan/Spatial_Relations_estimates.xlsx) | Merged; 20 Chinese and 20 English candidates |

The [scored working dataset](data/final/concepts_zh20_en20_v02.csv) extends the [v0.1 selection](data/final/concepts_zh20_en20_v01.csv), [nomination audit](data/final/nomination_counts_v01.csv), and [selection method](data/final/SELECTION.md). All repeated nominations were included; single-vote ties were resolved with documented scope and coverage criteria. See the [annotation guide](data/annotation/ANNOTATION.md) for the scoring scale, hierarchy, provenance, and review status.

## Roadmap

Stages 1–2 are complete. The v0.2 manual annotation is complete as a first pass; team review and the modelling stages follow.

| Stage | Work | Reviewable output |
| --- | --- | --- |
| 1. Collect candidates | Bring all three contributions into a comparable sense-level format. Check language, part of speech, definitions, and source status. | Three candidate pools and a comparison table |
| 2. Select the final set | Compare overlapping senses, choose 20 Chinese and 20 English entries, and record why each was included or excluded. Keep spatial relations as the core scope. | Versioned final concept list and selection notes |
| 3. Complete HA0 annotations | Write non-circular definitions, natural examples, one category parent per sense, and seven 0–2 grounding ratings: visual, auditory, tactile, motor, proprioceptive, interoceptive, and social. Record provenance and uncertainty for each value. | Final CSV/JSON, annotation guide, source notes |
| 4. Build the HA1 simulator | Compute grounding `C` and specificity `S` separately from reviewed features and documented category edges. Normalize them, plot the C × S plane, and test an adjustable composite score across several weights. | Notebook, scatter plot, sensitivity plot, short interpretation |
| 5. Add semantic structure | Build a typed category graph and annotate image schemas such as CONTAINER, PATH, BOUNDARY, BALANCE, and FORCE where the sense supports them. | Graph, schema annotations, simple rule baseline |
| 6. Test extensions | Implement metaphor-relation coherence and compare graph or feature estimates with a frozen embedding baseline where feasible. Preserve separate literal and extended senses. | Scoring code, contrast cases, baseline comparison |
| 7. Evaluate robustness | Test held-out concepts or expression families, inspect errors, quantify information lost under abstraction, and audit an embodied-AI example under controlled perturbations. | Evaluation tables, error analysis, limitations |
| 8. Package the capstone | Integrate the dataset, C/S simulator, graph, and held-out tests into a runnable and documented project. | Reproducible notebook or app, data dictionary, figures, report, demo |

Stages 5–8 follow the course's cumulative HA2–HA9 sequence. The team can revise their implementation order as the dataset and available materials become clearer.

## Data and review rules

- Keep candidate proposals separate from the selected and scored working datasets. Every current C/S value follows the documented manual feature matrix and curated taxonomy.
- Label feature values as `sourced`, `manual`, or `generated`; provide a source or annotation note and record low confidence where appropriate.
- Derive `S` from an inspectable hierarchy. If a sense has no defensible comparable parent path, keep its `S` value missing and explain why.
- Inspect C × S coverage **after** annotation. Do not adjust ratings solely to populate quadrants.
- Version the final data, document normalization and weights, keep random seeds where used, and report baselines, failed cases, and limits of the conclusions.

## Repository layout

The candidate pools and selected concept set are in `main`. Modelling and report directories are planned for later stages:

```text
candidates/<contributor>/    three independent proposals; Hu's source workbook
data/annotation/            manual ratings, taxonomy, annotation guide
data/final/                 selected and scored bilingual versions, vote audit
scripts/                    reproducible scoring build
notebooks/                  planned scoring, graphs, and evaluation
reports/                    planned figures, results, and limitations
```

