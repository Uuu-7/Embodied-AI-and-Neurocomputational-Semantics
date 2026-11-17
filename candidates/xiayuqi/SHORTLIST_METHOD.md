# Xia Yuqi's provisional 20 Chinese + 20 English shortlist

This is an individual shortlist for discussion under [issue #10](https://github.com/Uuu-7/Embodied-AI-and-Neurocomputational-Semantics/issues/10). It is not the final team dataset. The three original candidate pools and proposals are unchanged.

The accompanying 40-row CSV uses the same wide-table style as the other members' drafts: one row per proposed target sense, with a stable ID, language, term, part of speech, target definition, subfamily, source proposal IDs, nomination count, alignment flag, and selection reason. The seven channel, example, C, S, evidence, and confidence cells are intentionally blank pending annotation. Definitions and parts of speech are copied from the candidate named in `definition_source_candidate_id`; they are provisional until lexical checks.

## Selection method

- Select 20 Chinese and 20 English items separately. Exact translation pairs are not required.
- Include all ten forms nominated by two members, while flagging differences in part of speech or sense scope for review. A shared word form is not yet proof of a shared sense.
- Fill the remaining slots for coverage of position, containment, boundary, direction, distance, path, configuration, contact, and embodied force. The draft has 19 directly spatial Chinese senses and one force sense; the English side has 18 directly spatial senses and two force senses.
- Preserve the original candidate IDs so each nomination can be checked against the three source proposals. Selection reasons are provisional and open to team revision.

## Checks before team approval

1. Confirm the target sense and part of speech. Use COW or NTU Chinese WordNet for Chinese sense and taxonomy checks; use Oxford Learner's Dictionaries for English definitions and usage.
2. Apply the agreed seven-feature rubric independently. C is blank until those ratings exist. Verify S against a documented sense-specific taxonomy path, or retain NA.
3. Inspect the actual C×S distribution and replace items only for a stated semantic or evidence reason. Do not tune scores or hierarchy depth to fill a quadrant.
4. Compare this shortlist with the selections in PR #11 and PR #12, record disagreements in issue #10, and obtain all three members' sign-off before a final dataset is merged.
