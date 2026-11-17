# Embodied AI and Neurocomputational Semantics

EAINS 2026 team project on **spatial relation vocabulary**. We are building a bilingual concept dataset and a reproducible computational prototype for studying grounding, category specificity, image schemas, and related semantic extensions. Model scores are transparent estimates based on documented inputs; they are not direct measurements of human understanding.

## Team

- Xia Yuqi
- Chen Fengru
- Hu Jinnan

## Scope

The agreed final dataset target is **20 Chinese and 20 English concept senses**. We will select them from three independent candidate pools. A record represents a specified sense in context, so similar spellings, translations, and literal or extended uses are reviewed separately. The two languages need not form 20 exact translation pairs.

## Current contributions

| Member | Working contribution | Status |
| --- | --- | --- |
| Xia Yuqi | [Spatial relation candidate proposal, PR #2](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/2) | Draft; 20 Chinese and 20 English candidates |
| Chen Fengru | [Candidate proposal, PR #1](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/1) | Draft; 20 Chinese and 20 English candidates |
| Hu Jinnan | [Estimates workbook on the `40words` branch](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/blob/40words/Spatial_Relations_estimates.xlsx) | Working file uploaded; candidate format and review still pending |

As of 2026-11-17, these are separate contributions. No final group dataset has been selected or merged into `main`.

## Roadmap

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

- Keep candidate proposals separate from the approved final dataset. Do not fill missing `C` or `S` scores by guesswork.
- Label feature values as `sourced`, `manual`, or `generated`; provide a source or annotation note and record low confidence where appropriate.
- Derive `S` from an inspectable hierarchy. If a sense has no defensible comparable parent path, keep its `S` value missing and explain why.
- Inspect C × S coverage **after** annotation. Do not adjust ratings solely to populate quadrants.
- Version the final data, document normalization and weights, keep random seeds where used, and report baselines, failed cases, and limits of the conclusions.

## Planned repository layout

Candidate files currently live on contributor branches. After group review, the repository can add:

```text
candidates/<contributor>/    independent proposals
data/final/                 approved bilingual dataset and annotation guide
notebooks/                  scoring, graphs, and evaluation
reports/                    figures, results, and limitations
```

The proposed directories are a roadmap, not a claim that the files already exist.
