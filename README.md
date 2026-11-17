# Spatial Relations Lexicon

A bilingual concept dataset prepared by **Xia Yuqi, Chen Fengru, and Hu Jinnan** for Embodied AI and Neurocomputational Semantics.

The [selected vocabulary database](data/final/spatial_relations_zh20_en20_v1.csv) contains **20 Chinese and 20 English senses**, with definitions, illustrative examples, source proposal IDs, seven-feature reference ratings, C values, and available taxonomy paths for S. The [selection and annotation record](data/final/SELECTION_NOTES.md) explains the merge decisions, score provenance, C×S coverage, and remaining verification work.

The three original candidate pools and proposals are preserved under [`candidates/`](candidates/). The selected 40-item inventory is the current repository version. Reference C ratings, reported S paths, and constructed examples should be independently checked before being treated as agreed team annotations.

## Next checks

1. Reconcile source sense and part-of-speech differences flagged in the CSV.
2. Check English definitions and usage against Oxford Learner's Dictionaries; check Chinese senses and taxonomy with COW or NTU Chinese WordNet and suitable corpora.
3. Obtain independent seven-feature ratings, review S paths, and publish a new version if any entries change.
