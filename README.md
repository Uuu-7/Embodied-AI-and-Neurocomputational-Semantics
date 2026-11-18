# Spatial Relations Lexicon

A bilingual concept dataset prepared by **Xia Yuqi, Chen Fengru, and Hu Jinnan** for Embodied AI and Neurocomputational Semantics.

The [current 40-sense working database](data/final/spatial_relations_zh20_en20_v3_working.csv) contains **20 Chinese and 20 English senses**, definitions, examples, one category parent per sense, seven-feature scores, and available taxonomy paths for S. Xia Yuqi confirmed the lexical senses manually. The [v3 feature audit](data/reviews/FEATURE_SCORE_AUDIT_V3.md) records provenance and nine score questions that still require team discussion. The [v2 reconciliation record](data/final/V2_RECONCILIATION.md), [v2 database](data/final/spatial_relations_zh20_en20_v2.csv), and [v1 selection notes](data/final/SELECTION_NOTES.md) preserve earlier decisions.

The three original candidate pools and proposals are preserved under [`candidates/`](candidates/). The [shared HA0/HA1 working submission](submissions/team/) contains a 40-row HA0 export, an executed HA1 notebook, derived scores, figures, and an interpretation. The numerical C ratings are still provisional, the 25 reported S paths need independent verification, and the constructed examples are illustrative. This is not three independent annotations or a team sign-off.

## Next checks

1. Resolve the nine feature-level questions in the audit and review the proposed category-parent nodes.
2. Verify the 25 carried S paths against sense-specific sources; retain NA when no compatible path is available.
3. Re-run HA1 after any agreed change and submit the approved materials to the course LMS.
