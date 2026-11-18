# Team review update — 18 November 2026

This note records **review status**, not a change to the published 40-sense inventory or to Xia's HA1 baseline input.

- [Chen Fengru's draft PR #14](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/14) proposes sense-specific C corrections in 24 of 40 rows. It also narrows the target sense of `EN19 balance` and clears its previous S depth/path to NA. Main remains on v1.
- [Hu Jinnan's review comment](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/pull/14#issuecomment-6961983401) supports the re-audit direction but requests further changes: Social=0 for the two geographic convention terms, Motor=0 for four static region/location senses, a fresh check of the two noun route senses, Tactile=1 for geometric `接触`, Proprioceptive=2 for `posture`, and S=NA for the narrowed bodily `balance` sense. Hu explicitly does not approve PR #14 as it stands.
- PR #14's stated quadrant counts use its **fixed raw-score thresholds**, not the HA1 lecture's min–max axes with 0.5 dividers. Recomputing the current PR #14 draft under the HA1 method gives 6 low-C/low-S, 9 low-C/high-S, 7 high-C/low-S, 3 high-C/high-S, and 15 S=NA. These are scenario results, not accepted team results. Hu's requested edits would change them again.

The executed HA1 notebook and its figures intentionally use the current **main v1** data. Re-run them against an approved later version only after the score and target-sense changes are reconciled. The old 8/7/5/6 spread is a baseline, not an assertion that the ratings are correct or final.
