# HA1 interpretation — Xia Yuqi

The simulator keeps sensorimotor grounding (C) and taxonomic specificity (S) separate before forming an abstractness score. Raw C is the mean of seven 0–2 channel ratings. For 26 senses with a documented path, raw S counts taxonomy edges. Both axes receive dataset-level min–max scaling. The 14 senses without a supported path retain S=NA and have no composite score; assigning zero would falsely make them broad categories.

The normalized C×S plot contains eight low-C/low-S, seven low-C/high-S, five high-C/low-S, and six high-C/high-S senses. This spread is descriptive, not evidence of balanced human semantic representation. The raw ranges are C=0.286–1.000 and S=3–8. Different inventory choices could move concepts across the 0.5 dividers. Chinese supplies 12 plotted senses and leaves eight S values missing; English supplies 14 and leaves six missing. Removing the disputed balance S path leaves five high-C/high-S senses and raises S=NA to 15. These coverage limits constrain interpretation.

Weight sensitivity is substantial. Between w=0.2 and w=0.8, 21 of 26 scorable senses change A by more than 0.1, and 82 pairs reverse rank. ZH01 (position) has maximal C but minimal S, so A changes by 0.60. EN07 (adjacency) shows the opposite pattern and changes by 0.48. A single ranking therefore needs both axes and a stated weight.

Two other choices matter. Mean and sum C normalize identically because they differ by a constant factor. Maximum-channel C fails: every concept's maximum is two, leaving no variation. Counting active channels changes five quadrants. The noun path receives the lowest normalized C despite possible motor associations; this reflects the chosen literal route sense and rating policy.

This is exploratory, not a validated human measurement. Ratings mix imported and draft values; S paths lack independent audit. A newer team re-audit remains under review. Independent ratings, sense verification, and another S definition remain necessary; no held-out accuracy is claimed without labels.
