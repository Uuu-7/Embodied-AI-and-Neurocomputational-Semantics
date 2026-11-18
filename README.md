# Spatial Relations Lexicon

A bilingual concept dataset prepared by **Xia Yuqi, Chen Fengru, and Hu Jinnan** for Embodied AI and Neurocomputational Semantics.

The [integrated vocabulary database](data/final/spatial_relations_zh20_en20_v2.csv) contains **20 Chinese and 20 English senses**, with definitions, illustrative examples, source proposal IDs, seven-feature ratings, C values, and available taxonomy paths for S. The [v2 reconciliation record](data/final/V2_RECONCILIATION.md) explains how Chen Fengru's re-audit and Hu Jinnan's review were integrated; [feature provenance](data/final/feature_provenance_v2.csv) records the source of every rating. The [v1 database](data/final/spatial_relations_zh20_en20_v1.csv) and [selection notes](data/final/SELECTION_NOTES.md) remain as history.

The three original candidate pools and proposals are preserved under [`candidates/`](candidates/). The v2 ratings are a provisional integration, not three independent annotations or a team sign-off. Reported S paths and constructed examples need independent verification.

## Next checks

1. Reconcile source sense and part-of-speech differences flagged in the CSV.
2. Check English definitions and usage against Oxford Learner's Dictionaries; check Chinese senses and taxonomy with COW or NTU Chinese WordNet and suitable corpora.
3. Obtain independent seven-feature ratings, review S paths, and revise v2 if evidence changes any entry.
