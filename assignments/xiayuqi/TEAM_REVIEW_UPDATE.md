# Review status — 18 November 2026

The [integrated v2 dataset](../../data/final/spatial_relations_zh20_en20_v2.csv) adopts Chen Fengru's updated [PR #14 C re-audit](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/14), in which Chen implemented Hu Jinnan's [review corrections](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/14#issuecomment-6961983401). Xia Yuqi generated the integrated HA0/HA1 outputs without further feature-score changes. The [reconciliation record](../../data/final/V2_RECONCILIATION.md) and [per-feature provenance](../../data/final/feature_provenance_v2.csv) document exact changes.

This is an integrated working dataset. It does **not** certify three independent ratings or a team consensus. Hu had objected to merging PR #14 as written; v2 incorporates the specified corrections rather than merging that draft unchanged. The 25 retained taxonomy paths, especially the exact sense of geometric contact, still need independent source checks. The narrowed bodily balance sense has S=NA.

The HA1 notebook and figures now use v2. Its normalized C×S quadrant counts are 8 low/low, 10 low/high, 5 high/low, and 2 high/high; 15 senses have S=NA. The earlier draft's fixed raw-cutoff counts must not be substituted for these plotted results.
