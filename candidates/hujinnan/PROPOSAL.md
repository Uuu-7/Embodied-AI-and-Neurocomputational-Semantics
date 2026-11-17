# Bilingual spatial relation concept candidate pool — proposal v0.1

**Status:** candidate nomination for team review. **Source author:** Hu Jinnan. **Standardized:** 2026-11-17 from [the original estimates workbook](Spatial_Relations_estimates.xlsx). This is not the approved final group dataset.

The source workbook contains 20 Chinese and 20 English recommended noun senses. This CSV adopts the same 14-column candidate schema as the other two proposals. Definitions below are concise manual paraphrases of the target senses in the workbook. The workbook's preliminary seven-channel C ratings, C mean, noun synset mappings, taxonomic paths, and S alternatives remain in the original file; the candidate CSV leaves C and S blank until team review.

## Chinese candidates (20)

| ID | Term | Subfamily | Target sense (English draft) | Schema hypothesis | Channels to inspect |
|---|---|---|---|---|---|
| ZH01 | **位置** (wèizhì) | relative_position | A specified point or extent in a reference space. | LOCATION | visual |
| ZH02 | **中心** (zhōngxīn) | region_part | A central point fixed by the limits of a reference figure. | CENTER_PERIPHERY | visual |
| ZH03 | **内部** (nèibù) | containment | The region enclosed by a reference entity. | CONTAINER | visual · tactile |
| ZH04 | **外围** (wàiwéi) | boundary_relation | The outer boundary or surface of an entity. | BOUNDARY | visual |
| ZH05 | **边界** (biānjiè) | boundary_relation | A line delimiting the extent of an area. | BOUNDARY | visual |
| ZH06 | **周界** (zhōujiè) | boundary_relation | The line enclosing a plane area. | BOUNDARY | visual |
| ZH07 | **前面** (qiánmiàn) | front_back_orientation | The part of an entity facing a specified observer or direction. | FRONT_BACK | visual |
| ZH08 | **后面** (hòumiàn) | front_back_orientation | The rear part of an entity under a specified orientation. | FRONT_BACK | visual |
| ZH09 | **左边** (zuǒbiān) | lateral_orientation | The region to the left of an observer or oriented entity. | LEFT_RIGHT | visual · proprioceptive |
| ZH10 | **右边** (yòubiān) | lateral_orientation | The region to the right of an observer or oriented entity. | LEFT_RIGHT | visual · proprioceptive |
| ZH11 | **朝向** (cháoxiàng) | orientation | The direction that the front of an entity faces. | ORIENTATION | visual |
| ZH12 | **路径** (lùjìng) | path_relation | A route along which motion could occur. | PATH | visual · motor |
| ZH13 | **距离** (jùlí) | distance_relation | The measurable interval between two places. | NEAR_FAR | visual |
| ZH14 | **间距** (jiānjù) | distance_relation | The empty space separating two entities or points. | SEPARATION | visual |
| ZH15 | **空隙** (kòngxì) | distance_relation | A narrow opening between nearby surfaces or objects. | SEPARATION | visual · tactile |
| ZH16 | **对称** (duìchèn) | arrangement | An arrangement whose parts correspond across a line, point, or plane. | ALIGNMENT | visual |
| ZH17 | **排列** (páiliè) | arrangement | The spatial ordering of entities in a configuration. | ALIGNMENT | visual |
| ZH18 | **姿态** (zītài) | body_position | The way a person's body and limbs are positioned. | BODY_CONFIGURATION | visual · proprioceptive |
| ZH19 | **坡度** (pōdù) | orientation | The degree to which a surface inclines relative to horizontal. | ANGLE | visual |
| ZH20 | **接触** (jiēchù) | topological_relation | A tangent relation where surfaces meet at a point or line without crossing. | CONTACT | visual · tactile |

## English candidates (20)

| ID | Term | Subfamily | Target sense (English draft) | Schema hypothesis | Channels to inspect |
|---|---|---|---|---|---|
| EN01 | **proximity** | distance_relation | A short distance between entities relative to a specified scale. | NEAR_FAR | visual |
| EN02 | **distance** | distance_relation | The measurable separation between two locations. | NEAR_FAR | visual |
| EN03 | **gap** | distance_relation | An open interval or space between bounded entities. | SEPARATION | visual |
| EN04 | **boundary** | boundary_relation | A line or surface marking the limit of a region. | BOUNDARY | visual |
| EN05 | **adjacency** | topological_relation | A relation in which entities lie immediately next to each other. | ADJACENCY | visual · tactile |
| EN06 | **separation** | topological_relation | The spatial interval keeping two entities apart. | SEPARATION | visual |
| EN07 | **orientation** | orientation | The direction in which an entity is aligned relative to a reference frame. | ORIENTATION | visual |
| EN08 | **alignment** | arrangement | The arrangement of entities along a common line or direction. | ALIGNMENT | visual |
| EN09 | **angle** | orientation | The amount of turn between intersecting lines or planes. | ANGLE | visual |
| EN10 | **intersection** | topological_relation | The set of points shared by two spatial configurations. | INTERSECTION | visual |
| EN11 | **juxtaposition** | arrangement | The placement of entities side by side. | JUXTAPOSITION | visual |
| EN12 | **interior** | containment | The region enclosed by an entity's boundary. | CONTAINER | visual · tactile |
| EN13 | **exterior** | containment | The region outside an entity's boundary. | CONTAINER | visual · tactile |
| EN14 | **contact** | topological_relation | A state in which two physical surfaces meet. | CONTACT | visual · tactile |
| EN15 | **earshot** | sensory_range | The region within which a voice can be heard. | NEAR_FAR | auditory |
| EN16 | **posture** | body_position | The spatial arrangement of a body and its limbs. | BODY_CONFIGURATION | visual · proprioceptive |
| EN17 | **path** | path_relation | A route connecting positions through space. | PATH | visual · motor |
| EN18 | **vicinity** | distance_relation | The region near a reference place. | NEAR_FAR | visual |
| EN19 | **center** | region_part | A point equally distant from specified limits of a figure. | CENTER_PERIPHERY | visual |
| EN20 | **perimeter** | boundary_relation | The line enclosing a plane region. | BOUNDARY | visual |

## Four dataset checks for team discussion

1. **Quadrant coverage:** calculate C and S from reviewed data before assessing whether the final 20 Chinese and 20 English senses cover the C × S plane. Do not assign quadrants from candidate labels.
2. **Defensible taxonomy:** the source workbook reports COW 1.1 to OMW English noun-synset mappings and shortest hypernym paths to `entity`. Preserve the exact sense IDs and paths in the workbook. The team should independently recheck disputed mappings and comparability across languages before treating S as final.
3. **Grounding feature variation:** the workbook has seven 0–2 channels, but its methods sheet describes new scores as AI estimates without two independent human ratings. The CSV lists nonzero channels for review, not accepted ratings.
4. **External anchors:** `YES` in this CSV means the source workbook reports an individually checked lexical mapping. It does not mean the whole team has validated the mapping or the C rating.

## External resources to consult — candidate mapping not yet team-validated

- [Chinese Open Wordnet](https://bond-lab.github.io/cow/) for the reported Chinese noun senses and ILI mappings.
- [Open Multilingual Wordnet](https://omwn.org/) for the shared English synsets and noun hypernym paths.
- [Cygnet releases](https://github.com/omwn/cygnet/releases), [STREUSLE](https://github.com/nert-nlp/streusle), and [Chinese SNACS](https://github.com/nert-nlp/Chinese-SNACS) are listed in the workbook as additional lexical or spatial-relation evidence. Their categories are not substituted for taxonomy depth.

The workbook's `方法和来源` sheet records versions, methods, and limits. Keep COW/OMW and Cygnet paths distinct rather than combining incompatible depths.

## Review procedure for three contributors

1. Keep this contribution under `candidates/hujinnan/` and compare it with the other two 20-Chinese plus 20-English pools by language and target sense.
2. Inspect overlaps and semantic mismatches. Some apparent translations use different noun senses; do not count them as interchangeable solely by spelling.
3. Recheck the reported noun synset and definition for every retained sense. Record the source version, sense ID, and parent path in the final dataset.
4. Have at least two members independently review seven-channel ratings. Resolve disagreements before computing a group C score; retain the workbook's AI ratings as preliminary evidence only.
5. Select the final 20 Chinese and 20 English senses after comparing nomination frequency and course criteria. Record tie breaks and reasons for exclusion.
6. Compute C and S separately, then inspect actual quadrant coverage and weight sensitivity for HA1. Keep missing or noncomparable values as NA rather than inventing a depth.

## Review risks to keep visible

- The 40 rows are all noun senses. This improves taxonomic comparability but may underrepresent ordinary spatial prepositions, locatives, and action relations.
- The preliminary C profile is heavily visual; the source summary gives zero direct interoceptive and social scores across these 40 target senses. Do not inflate those channels to meet a diversity target.
- `earshot` and body-posture terms add nonvisual evidence but may sit at the edge of the agreed spatial-relation family.
- The source workbook's Chinese and English noun senses sometimes share a synset but need separate usage checks. Treat similar translations as candidates for alignment, not established equivalents.
- This standardized proposal preserves the source workbook without claiming that its scores are independently replicated or team-approved.

