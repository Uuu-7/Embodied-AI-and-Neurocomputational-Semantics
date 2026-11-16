# Spatial relation candidate pool — proposal v0.1

**Status:** independent nomination for group review, not the final HA0 dataset. **Contributor path:** `candidates/Uuu-7/`. **Date:** 2026-11-16.

This proposal stays within **spatial relations**. It contains 20 Chinese and 20 English candidate senses in [`candidate_pool_zh20_en20_v01.csv`](candidate_pool_zh20_en20_v01.csv). The inventory covers geographic and viewer-relative orientation, containment, distance, adjacency, region parts, and paths.

## Candidate inventory

| Chinese ID | Term | Spatial relation | Chinese ID | Term | Spatial relation |
|---|---|---|---|---|---|
| ZH01 | 阴 | mountain north / river south | ZH11 | 中央 | center of region |
| ZH02 | 阳 | mountain south / river north | ZH12 | 边缘 | edge of region |
| ZH03 | 内部 | inside a bounded entity | ZH13 | 之间 | between two referents |
| ZH04 | 外部 | outside a bounded entity | ZH14 | 旁边 | beside a referent |
| ZH05 | 上方 | above | ZH15 | 附近 | near |
| ZH06 | 下方 | below | ZH16 | 远处 | far away |
| ZH07 | 前方 | in front | ZH17 | 对面 | opposite |
| ZH08 | 后方 | behind | ZH18 | 相邻 | adjacent |
| ZH09 | 左侧 | to the left | ZH19 | 环绕 | around |
| ZH10 | 右侧 | to the right | ZH20 | 交界 | shared boundary |

| English ID | Term | Spatial relation | English ID | Term | Spatial relation |
|---|---|---|---|---|---|
| EN01 | inside | containment | EN11 | between | intervening region |
| EN02 | outside | exteriority | EN12 | beside | lateral proximity |
| EN03 | above | vertical orientation | EN13 | near | short distance |
| EN04 | below | vertical orientation | EN14 | far from | long distance |
| EN05 | in front of | facing orientation | EN15 | opposite | facing across space |
| EN06 | behind | facing orientation | EN16 | adjacent to | adjacency |
| EN07 | to the left of | viewpoint orientation | EN17 | around | encircling route |
| EN08 | to the right of | viewpoint orientation | EN18 | across | opposite side / span |
| EN09 | at the center of | center of region | EN19 | through | route via interior |
| EN10 | at the edge of | edge of region | EN20 | beyond | farther side of limit |

The bilingual lists provide comparison opportunities, not 20 asserted translation equivalences. The unit is a **sense in a specified spatial use**, not an undifferentiated word form. Several English multiword expressions and Chinese locative nouns will require a consistent part-of-speech and taxonomy policy before final selection.

## Sense scope and limited extensions

Two geographic orientation senses have independently checked dictionary anchors, linked in the CSV. Their English definitions are manual paraphrases. Other lexical anchors remain unverified.

Some spatial forms can also express philosophical contrasts. This is a limited extension for later comparison: any non-spatial use would need its own sense record and examples. It should not inherit the spatial sense's feature profile or C/S scores.

## Proposed feature schema and taxonomy

The CSV's `channels_to_review` field is a **hypothesis**, not a score. For final HA0/HA1 annotation, rate each of seven channels on 0–2 with a written rationale: **0** no direct contribution in the specified sense, **1** context-dependent or secondary contribution, **2** diagnostic contribution. Channels: visual, auditory, tactile, motor, proprioceptive, interoceptive, and social. Record each individual rating's source class (`sourced`, `manual`, or `generated`), a source or annotation note, and low confidence where appropriate. `C_score` is intentionally blank in this nomination pool.

The proposed `category_parent_proposed` values are **manual grouping labels**, not verified WordNet or FrameNet parents. Candidate relation types are topographic orientation, containment, vertical orientation, front/back orientation, lateral orientation, region part, relative position, distance, topology, and path. A later domain ontology could represent the common root `spatial_relation`, but it must document each parent edge and a consistent depth rule before calculating S. If a relational word or historical locative use cannot be placed comparably, record `S = NA` rather than inventing a depth. `S_score` is intentionally blank.

## Testable claim for the seminar

**Claim:** viewpoint-dependent terms such as `左侧/右侧` and `to the left/right of` will change labels more often under a controlled viewpoint reversal than containment terms such as `内部/外部` and `inside/outside`.

**Weakening result:** if both groups change at similar rates under matched scenes, the proposed distinction is not supported by this test. Geographic orientation offers a further contrast because its reference frame follows a mountain or river convention rather than the viewer's facing direction. This is a prediction to test, not a claim about model understanding.

## Review and handoff

1. Review the 40 senses for natural usage, part of speech, and near-duplicates. Pay special attention to the historical register of geographic orientation terms, reference frames for front/back/left/right, contextual scale for near/far, and static versus path senses for `环绕/around/across`.
2. Check lexical anchors for more rows using independent dictionaries or spatial-language resources. Only two rows have individually checked anchors here. Keep external ratings and the course's seven 0–2 channels distinct unless a conversion rule is documented.
3. Select a final 20-concept HA0 set as a group. Give each row a non-circular definition, one documented category parent, seven rated features with per-value provenance, an example, and at least one honest uncertainty note.
4. For HA1, compute C from reviewed feature values and S from verified taxonomy edges, retain both axes, draw the C×S plot, and test the adjustable composite and at least three weight choices. Quadrant coverage can only be evaluated after real C/S calculation.

This proposal does not claim that its draft labels, channel hypotheses, or source checks already satisfy the final HA0 rubric.

