# Bilingual concept candidate pool — proposal v0.1

**Status:** candidate nomination only. **Author:** chenfengru, prepared with AI assistance; group validation required. **Date:** 2026-11-16.

This is a **40-item proposal: 20 Chinese and 20 English candidates**, not the final HA0 20-concept submission. It proposes expanding the original narrow spatial-relation family to **Spatial, Force, and Embodied Relational Concepts with Metaphorical Extensions**. Teammates should submit independent candidate files, then choose a final set after comparing evidence.

## Chinese candidates (20)

| ID | Term | Subfamily | Target sense (English draft) | Schema hypothesis | Channels to inspect |
|---|---|---|---|---|---|
| ZH01 | **容纳** (róngnà) | spatial_schema | To have capacity to hold an entity within a bounded region. | CONTAINER | visual · tactile |
| ZH02 | **边界** (biānjiè) | spatial_schema | A line or surface separating two regions or domains. | BOUNDARY | visual · tactile |
| ZH03 | **正中** (zhèngzhōng) | spatial_schema | At the geometric center of a specified region or arrangement. | CENTER | visual |
| ZH04 | **环绕** (huánrào) | spatial_schema | To form or follow a route surrounding a reference entity. | CYCLE;PATH | visual · motor |
| ZH05 | **隔着** (gézhe) | spatial_schema | With a third entity intervening between two referents. | BLOCKAGE;SEPARATION | visual |
| ZH06 | **阴** (yīn) | topographic_convention | North of a mountain or south of a river under a traditional geographic convention. | ORIENTATION | visual |
| ZH07 | **阳** (yáng) | topographic_convention | South of a mountain or north of a river under a traditional geographic convention. | ORIENTATION | visual |
| ZH08 | **托住** (tuōzhù) | force_action | To bear an object's load so that it does not fall. | SUPPORT;FORCE | tactile · motor · proprioceptive · visual |
| ZH09 | **抓握** (zhuāwò) | force_action | To secure an object by closing a hand around it. | CONTACT;CONTROL | tactile · motor · proprioceptive · visual |
| ZH10 | **推开** (tuīkāi) | force_action | To exert force so that an entity moves away or an opening widens. | FORCE;PATH | tactile · motor · proprioceptive · visual |
| ZH11 | **跨越** (kuàyuè) | force_action | To move from one side of a boundary or obstacle to the other. | PATH;BOUNDARY | motor · proprioceptive · visual |
| ZH12 | **阻挡** (zǔdǎng) | force_action | To impede motion by placing a barrier in its course. | BLOCKAGE;FORCE | visual · motor · tactile |
| ZH13 | **失衡** (shīhéng) | force_action | To lose mechanical stability or bodily equilibrium. | BALANCE | proprioceptive · motor · visual |
| ZH14 | **越界** (yuèjiè) | metaphor_bridge | To move beyond a specified physical or normative limit. | BOUNDARY;PATH | motor · visual · social |
| ZH15 | **分寸** (fēncùn) | metaphor_target | A contextually appropriate limit on behavior or expression. | BOUNDARY;SCALE | social · interoceptive |
| ZH16 | **隔阂** (géhé) | metaphor_target | A barrier in mutual understanding or interpersonal connection. | BARRIER;SEPARATION | social · interoceptive |
| ZH17 | **进退两难** (jìntuìliǎngnán) | metaphor_target | A dilemma where advancing and withdrawing both have undesirable outcomes. | PATH;OPPOSITION | interoceptive · social |
| ZH18 | **立场** (lìchǎng) | metaphor_target | A position adopted toward an issue or disagreement. | POSITION;ORIENTATION | social |
| ZH19 | **归属** (guīshǔ) | metaphor_target | A recognized or felt connection to a person or group. | CONTAINER;INCLUSION | social · interoceptive |
| ZH20 | **退路** (tuìlù) | metaphor_bridge | A route or option permitting withdrawal from a situation. | PATH;EXIT | motor · visual |

## English candidates (20)

| ID | Term | Subfamily | Target sense (English draft) | Schema hypothesis | Channels to inspect |
|---|---|---|---|---|---|
| EN01 | **location** | spatial_schema | The place or region occupied by an entity in a reference space. | LOCATION | visual |
| EN02 | **boundary** | spatial_schema | A line or surface separating regions or domains. | BOUNDARY | visual · tactile |
| EN03 | **containment** | spatial_schema | A relation in which one entity is enclosed within a bounded region. | CONTAINER | visual · tactile |
| EN04 | **proximity** | spatial_schema | A relatively short distance under a specified spatial scale. | NEAR_FAR | visual · auditory |
| EN05 | **path** | spatial_schema | A continuous route connecting positions through space. | PATH | visual · motor |
| EN06 | **center** | spatial_schema | A geometric reference point determined by a specified region. | CENTER | visual |
| EN07 | **overlap** | spatial_schema | An intersection of spatial regions with positive area or volume. | OVERLAP | visual |
| EN08 | **contact** | spatial_schema | A relation in which two surfaces physically meet. | CONTACT | tactile · visual |
| EN09 | **support** | force_action | To bear a load or counter a force that would displace an entity. | SUPPORT;FORCE | tactile · motor · proprioceptive · visual |
| EN10 | **balance** | force_action | A state of bodily or mechanical stability under competing forces. | BALANCE | proprioceptive · motor · visual |
| EN11 | **grasp** | force_action | To hold an object by closing the hand or fingers around it. | CONTACT;CONTROL | tactile · motor · proprioceptive · visual |
| EN12 | **lift** | force_action | To raise an object to a higher position against gravity. | UP_DOWN;FORCE | tactile · motor · proprioceptive · visual |
| EN13 | **push** | force_action | To exert force moving an entity away or along a direction. | FORCE;PATH | tactile · motor · proprioceptive · visual |
| EN14 | **pull** | force_action | To draw an entity toward an agent using force. | FORCE;PATH | tactile · motor · proprioceptive · visual |
| EN15 | **squeeze** | force_action | To compress an entity with forces from opposing directions. | FORCE;CONSTRAINT | tactile · motor · proprioceptive |
| EN16 | **obstacle** | metaphor_bridge | An entity or condition that impedes motion along a route. | BLOCKAGE;PATH | visual · motor |
| EN17 | **exclusion** | metaphor_target | A social condition in which access or membership is denied. | CONTAINER;OUTSIDE | social · interoceptive |
| EN18 | **belonging** | metaphor_target | A recognized or felt connection to a group or community. | CONTAINER;INCLUSION | social · interoceptive |
| EN19 | **constraint** | metaphor_target | A restriction that reduces possible actions or states. | BLOCKAGE;BOUNDARY | social · motor |
| EN20 | **progress** | metaphor_target | Advancement through ordered stages toward a specified goal. | PATH;FORWARD | social · motor |

## Teacher's four ideal dataset conditions (2026-11-16 message)

1. **Quadrant coverage:** target at least three FINAL concepts in each quadrant of the C × S plane, assessed using observed annotation/taxonomy calculations, never assigned in advance.
2. **Defensible taxonomy:** derive S from verified sense-specific hierarchy in WordNet, FrameNet frame relations, or a documented domain ontology. Do not fabricate taxonomy depth. Mixed nouns/verbs/prepositions/idioms may make S incomparable; use a clearly scoped domain taxonomy or POS-conditional checks.
3. **Grounding feature variation:** annotate seven features: visual, auditory, tactile, motor, proprioceptive, interoceptive, social. Proposed channels above are **hypotheses to review**, not 0–2 scored values.
4. **External anchor:** verify at least some final terms against independent resources. The candidate rows have NOT individually been verified; `individual_lexical_source_verified=NO` is intentional.

## External resources to consult — candidate mapping not yet validated

- Lancaster Sensorimotor Norms (English): https://www.lancaster.ac.uk/psychology/lsnorms/
- Princeton WordNet (sense-specific taxonomic relations, chiefly English nouns; verbs use a different relation system): https://wordnet.princeton.edu/
- Berkeley FrameNet (frame and lexical-unit relations): https://berkeleyfn.framenetbr.ufjf.br/
- Chinese Open Wordnet: https://bond-lab.github.io/cow/
- OpenHowNet: https://hownet.thunlp.org/

The Lancaster norms are NOT a native seven-column match: its scales and modalities differ from the course's seven-feature 0–2 schema. English phrases and all Chinese items may be missing, and Chinese/English estimates must not be treated as directly comparable without a documented harmonization method.

## Review procedure for three contributors

1. Each teammate contributes **their own** `candidates/<github-username>/candidate_pool_zh20_en20_v01.csv` on a personal feature branch, with a draft PR to `main`. Do not commit over another member's file.
2. Keep this CSV as a **nomination pool**, deduplicate by sense rather than spelling alone, and identify each row's POS, original-language sense, and whether it is a literal source or an abstract metaphor target.
3. Before selecting the final 20, draft a **real** miniature taxonomy with documented parent edges and independent anchors; mark missing S as NA. Compute provisional C from independently reviewed seven-feature ratings (0–2, plus provenance and confidence).
4. Make a C×S scatter plot and count actual occupied quadrants. If any quadrant has fewer than three **validly placed** concepts, reconsider nominations or argue for a broader domain. Do not tune annotations solely to fill quadrants.
5. Aim for multiple image schemas (CONTAINER, PATH, BALANCE, FORCE, BOUNDARY) and 2D/3D and literal/metaphor examples. Keep translation pairs traceable but avoid duplicating equivalent senses merely to meet count targets.
6. Record at least two independent raters and disagreements; consider weighted Cohen's kappa where appropriate. Obtain final group approval before merging nominated items into the official dataset.
7. For HA1, `compute_C` and `compute_S` must be reproducible from raw features/verified edges. Keep C and S separate and document normalization, adjustable weight `w`, and sensitivity to alternatives.

## Review risks to keep visible

- The Chinese idiom `进退两难`, function words `隔着/阴/阳`, and abstract targets such as `belonging` may lack a comparable WordNet taxonomic depth.
- Words with literal and figurative senses must receive **separate sense records** before scoring; one ambiguous score is not a clean training/evaluation datum.
- Some source and target terms may have similar spellings across languages but different usage distributions; bilingual matching is a research question, not a guaranteed equivalence.
- Do not claim that this proposal already satisfies the quadrant test. That can be determined only after annotation and hierarchy verification.
