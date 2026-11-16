# Bilingual spatial relation concept candidate pool — proposal v0.2

**Status:** candidate nomination only. **Author:** xiayuqi, prepared with AI assistance; group validation required. **Date:** 2026-11-16.

This is a **40-item proposal: 20 Chinese and 20 English candidates**, not the final HA0 20-concept submission. The candidate family is **spatial relations**, including orientation, containment, distance, adjacency, region parts, and paths. Teammates can compare candidate senses before selecting the final set.

## Chinese candidates (20)

| ID | Term | Subfamily | Target sense (English draft) | Schema hypothesis | Channels to inspect |
|---|---|---|---|---|---|
| ZH01 | **阴** (yīn) | topographic_orientation | The north side of a mountain or south side of a river in traditional geographic usage | ORIENTATION | visual · social |
| ZH02 | **阳** (yáng) | topographic_orientation | The south side of a mountain or north side of a river in traditional geographic usage | ORIENTATION | visual · social |
| ZH03 | **内部** (nèibù) | containment | A region enclosed by the boundary of a reference entity | CONTAINER | visual · tactile |
| ZH04 | **外部** (wàibù) | containment | A region beyond the boundary of a reference entity | CONTAINER | visual |
| ZH05 | **上方** (shàngfāng) | vertical_orientation | A region higher than a reference entity along the relevant vertical axis | UP_DOWN | visual · proprioceptive |
| ZH06 | **下方** (xiàfāng) | vertical_orientation | A region lower than a reference entity along the relevant vertical axis | UP_DOWN | visual · proprioceptive |
| ZH07 | **前方** (qiánfāng) | front_back_orientation | A region ahead of a reference entity under a specified facing direction | FRONT_BACK | visual · motor |
| ZH08 | **后方** (hòufāng) | front_back_orientation | A region behind a reference entity under a specified facing direction | FRONT_BACK | visual · motor |
| ZH09 | **左侧** (zuǒcè) | lateral_orientation | A region on the left of a reference entity under a specified viewpoint | LEFT_RIGHT | visual · proprioceptive |
| ZH10 | **右侧** (yòucè) | lateral_orientation | A region on the right of a reference entity under a specified viewpoint | LEFT_RIGHT | visual · proprioceptive |
| ZH11 | **中央** (zhōngyāng) | region_part | The central region of a bounded area or arrangement | CENTER_PERIPHERY | visual |
| ZH12 | **边缘** (biānyuán) | region_part | A peripheral part adjoining the limit of an area or surface | CENTER_PERIPHERY | visual · tactile |
| ZH13 | **之间** (zhījiān) | relative_position | An intervening region bounded by two specified reference entities | BETWEEN | visual |
| ZH14 | **旁边** (pángbiān) | relative_position | A region beside a reference entity without a fixed distance threshold | NEAR_FAR | visual |
| ZH15 | **附近** (fùjìn) | distance_relation | A region at relatively short distance from a reference entity | NEAR_FAR | visual · auditory |
| ZH16 | **远处** (yuǎnchù) | distance_relation | A region at relatively long distance from an observer or reference entity | NEAR_FAR | visual · auditory |
| ZH17 | **对面** (duìmiàn) | relative_position | A region facing a reference entity across an intervening space | OPPOSITION | visual |
| ZH18 | **相邻** (xiānglín) | topological_relation | Occupying positions next to each other with no relevant region between them | ADJACENCY | visual · tactile |
| ZH19 | **环绕** (huánrào) | path_relation | To extend or move around a reference entity on multiple sides | CYCLE;PATH | visual · motor |
| ZH20 | **交界** (jiāojiè) | topological_relation | The shared boundary at which two regions meet | BOUNDARY;CONTACT | visual · tactile |

## English candidates (20)

| ID | Term | Subfamily | Target sense (English draft) | Schema hypothesis | Channels to inspect |
|---|---|---|---|---|---|
| EN01 | **inside** | containment | In a region enclosed by the boundary of a reference entity | CONTAINER | visual · tactile |
| EN02 | **outside** | containment | Beyond the boundary of a reference entity | CONTAINER | visual |
| EN03 | **above** | vertical_orientation | At a higher position than a reference entity along a vertical axis | UP_DOWN | visual · proprioceptive |
| EN04 | **below** | vertical_orientation | At a lower position than a reference entity along a vertical axis | UP_DOWN | visual · proprioceptive |
| EN05 | **in front of** | front_back_orientation | Ahead of a reference entity under a specified facing direction | FRONT_BACK | visual · motor |
| EN06 | **behind** | front_back_orientation | To the rear of a reference entity under a specified facing direction | FRONT_BACK | visual · motor |
| EN07 | **to the left of** | lateral_orientation | On the left side of a reference entity under a specified viewpoint | LEFT_RIGHT | visual · proprioceptive |
| EN08 | **to the right of** | lateral_orientation | On the right side of a reference entity under a specified viewpoint | LEFT_RIGHT | visual · proprioceptive |
| EN09 | **at the center of** | region_part | In the central region of a bounded area or arrangement | CENTER_PERIPHERY | visual |
| EN10 | **at the edge of** | region_part | At a peripheral part adjoining the limit of an area | CENTER_PERIPHERY | visual · tactile |
| EN11 | **between** | relative_position | In an intervening region specified by two reference entities | BETWEEN | visual |
| EN12 | **beside** | relative_position | At the side of a reference entity without a fixed distance threshold | NEAR_FAR | visual |
| EN13 | **near** | distance_relation | At a relatively short distance from a reference entity | NEAR_FAR | visual · auditory |
| EN14 | **far from** | distance_relation | At a relatively long distance from a reference entity | NEAR_FAR | visual · auditory |
| EN15 | **opposite** | relative_position | Facing a reference entity across an intervening space | OPPOSITION | visual |
| EN16 | **adjacent to** | topological_relation | Next to a reference entity with no relevant region between them | ADJACENCY | visual · tactile |
| EN17 | **around** | path_relation | On multiple sides of a reference entity or along a route encircling it | CYCLE;PATH | visual · motor |
| EN18 | **across** | path_relation | On or toward the opposite side of an intervening region | PATH;BOUNDARY | visual · motor |
| EN19 | **through** | path_relation | Along a route entering and leaving a bounded region | PATH;CONTAINER | visual · motor |
| EN20 | **beyond** | relative_position | On the farther side of a boundary or reference location | BOUNDARY;PATH | visual |

## Four dataset checks for team discussion

1. **Quadrant coverage:** after annotation, inspect the actual C × S plane and aim for at least three final concepts in each quadrant if the verified data permits. Never assign quadrant membership in advance.
2. **Defensible taxonomy:** calculate S only from documented sense-specific parent edges in a suitable domain ontology or lexical resource. A single provisional family label does not establish taxonomic depth. Mark incomparable or missing S values as NA.
3. **Grounding feature variation:** annotate seven dimensions—visual, auditory, tactile, motor, proprioceptive, interoceptive, and social—on a defined 0–2 scale. The CSV's channel lists are hypotheses to review, not ratings.
4. **External anchors:** verify at least some final senses against independent resources. The CSV marks only two geographic dictionary senses as individually checked. Other rows remain unverified.

## External resources to consult — candidate mapping not yet validated

- [Princeton WordNet](https://wordnet.princeton.edu/) for English sense-specific lexical relations, where the part of speech permits a useful comparison.
- [Berkeley FrameNet](https://berkeleyfn.framenetbr.ufjf.br/) for frame and lexical-unit relations.
- [Chinese Open Wordnet](https://bond-lab.github.io/cow/) and [OpenHowNet](https://hownet.thunlp.org/) for candidate Chinese sense links; none are claimed as verified here.
- [Ministry of Education dictionary entry A](https://dict.revised.moe.edu.tw/dictView.jsp?ID=10442) and [entry B](https://dict.revised.moe.edu.tw/dictView.jsp?ID=11167) for the two checked geographic orientation senses in the table. The English definitions are manual paraphrases, not quotations.

These resources use different sense inventories and relation systems. A dictionary definition is not a seven-channel rating or a comparable taxonomic depth. Non-spatial and philosophical uses, when relevant, require separate sense records rather than inheriting the spatial sense's scores.

## Review procedure for three contributors

1. Each contributor submits an independent `candidates/<contributor>/candidate_pool_zh20_en20_v01.csv` and `PROPOSAL.md` on a separate draft PR. Compare by sense rather than spelling alone.
2. Check natural usage, part of speech, reference frame, and literal spatial scope for every row. Record a different sense separately if it will be tested.
3. Define each of the seven feature levels, collect independent 0–2 ratings with provenance, and record disagreements and low confidence. Do not turn channel hypotheses into numerical scores automatically.
4. Build a documented miniature taxonomy, then calculate C and S from reviewed values and verified parent edges. Missing S stays NA.
5. Plot C × S and count actually occupied quadrants. If coverage is uneven, reconsider the candidate set or document the limitation; do not tune ratings to fill quadrants.
6. Select the final 20-concept HA0 set with a non-circular definition, one category parent, example sentence, provenance for every feature value, and an explicit uncertainty note.
7. For HA1, keep C and S separate, test adjustable weights for A, and report sensitivity. A possible seminar test is whether viewpoint reversal changes left/right labels more often than inside/outside labels in matched scenes.

## Review risks to keep visible

- The inventory mixes locative nouns, prepositions, phrases, and one verb. A single WordNet-style depth may not compare them fairly; a documented domain taxonomy may be needed.
- Front/back and left/right relations need an explicit reference frame. Near/far depend on scale. Around/across can have static and path readings.
- Historical geographic usage may be less frequent than everyday locative expressions. Check the intended register before final selection.
- Equivalent-looking Chinese and English expressions may differ in use. Bilingual matching is a comparison question, not an assumed one-to-one translation.
- This proposal has no seven-channel scores or S depths. It does not claim to pass the quadrant check or to be an approved HA0 dataset.

