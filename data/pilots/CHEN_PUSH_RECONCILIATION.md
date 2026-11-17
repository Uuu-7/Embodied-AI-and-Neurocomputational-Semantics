# Chen pilot PR reconciliation — 2026-11-17

**Status:** ready for team review, NOT a completed annotation or a four-quadrant result.

## Why the earlier PR #7 needed revision

The current `main` (commit `696287bbd97bedf66c7868495b60e4c55a3a2b5b`) restarted the project around **12 pilot senses** from the three independent candidate pools, not the previously drafted "final 20 Chinese + 20 English" list. Consequently, the old PR #7's 40-word AI-generated C results and eight-replacement scenario are **obsolete for the current workflow**.

For provenance, that full original PR branch was preserved at [`archive/chenfengru-pr7-original-40word-pilot-20261117`](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/tree/archive/chenfengru-pr7-original-40word-pilot-20261117) and is **not part of this revised change**.

## Changes in the revised PR

- Synchronize only Chen's `data/audit/raters/chenfengru_pilot_v01.csv` with the canonical intended senses in `data/audit/pilot_concept_audit_v01.csv`.
- **Nine pilot IDs corrected:** P01, P04, P05, P06, P08, P09, P10, P11, P12. Each has seven rows, so 63 individual rows receive only a target-definition update.
- Keep **all 84 `score_0_2` cells blank**. Nothing is masquerading as Chen's independent human rating. All provenance, rationale and confidence cells remain blank.
- Maintain 12 × 7 row coverage, the original row order, pilot IDs and language/term strings.
- Leave Xia's and Hu's files unchanged. Their annotation independence must be preserved.

## Remaining independent work

1. Chen should review these definitions in the pilot audit and independently fill the 84 feature scores, provenance, reason and confidence fields. Use the team's common 0–2 grounding criteria.
2. Hu's blank form still contains nine definitions inherited from the older candidate versions; **Hu should synchronize his own form** before annotating so all raters score identical senses. Xia's AI-assisted draft already matches the pilot audit, but must not be called independent human ratings before her review.
3. `data/audit/pilot_taxonomy_v01.csv` has no verified sense-specific paths yet. **S remains NA**, so **no valid C × S quadrant count exists**.
4. After independent annotation, compare disagreement, make reviewed C from the adjudicated seven-feature vectors, validate S from sourced edges, then test four-quadrant coverage on the eventual concept selection.
5. Do not restore or merge the old 40-term provisional C/S numbers or replace the concept inventory solely to make the scatter plot look balanced.

## Verification recorded for this PR

- Input: 12 canonical pilot definitions and 84 unchanged blank Chen ratings from `main`.
- Exactly 9 distinct senses and 63 row definitions updated.
- All 12 IDs have exactly seven unique features.
- No numeric rating, manual annotation, source validation, taxonomy score, or unapproved final vocabulary introduced.

The prior 40-term proposal remains available in the archive branch for reference, but the current pilot workflow is the authoritative team process.
