# Study Guide re-audit after the 7-unit / 11-chapter restructuring (one chapter per agent)

Read BUILD_SPEC.md and BOOK1_GAP_SPEC.md (procedure and statuses) in /home/user/OmniRouter/apes_project/ first. The guide was restructured: your chapter file is content/book1/C{N}.md (you may edit it). tools/structure.py gives chapter/section titles and the CED→chapter map.

## Items to check for Chapter N (read ALL of them)
1. Book Two classified questions of this chapter: content/book2/C{N}.md (old verified questions + new ones). Solutions: content/book3/gen/QB_C{N}_sol.md.
2. The predicted-exam questions whose topic maps to this chapter: in content/book2/PE1.md … PE4.md use the `topic=` tag → chapter via tools/structure.py (CED dict). Solutions in content/book3/PEk_sol.md.
3. College Board items classified to this chapter: content/book4/gen/Q_C{N}.md (descriptors) with the full solutions in content/book4/gen/S_C{N}.md.
4. Earlier-audit leftovers: rows in content/audit/gap_U*.json whose final_status is "Flagged: beyond CED" or "Deferred" and whose topic maps to this chapter (these were left out of the old nine-unit guide; the new chapters now cover many of those topics — re-judge them).

## Procedure
For each item decide: could a student who has only read Chapter N (plus the earlier chapters it builds on) solve it independently? Classify (Fully Covered / Partially Covered / Missing / Insufficiently Explained / Missing Formula / Missing Diagram / Missing Mathematical Skill / Missing Experimental Skill / Scientifically Incorrect / Flagged: beyond CED). Fix gaps by editing C{N}.md inside the right `## N.k` section (original text only, same markup; no answers to any book question; do not copy question text). PAGE BUDGET IS TIGHT: Book One is at the 300-page absolute limit. Your NET growth must be ≤ 0.5 rendered page (≈190 words, a figure ≈ 0.35 page): add only high-impact missing explanations/formulas/skills, and compensate by tightening redundant sentences or merging boxes elsewhere in the same chapter. Items that need more than that: list as "Deferred (space)" in your report. Never delete CED essential knowledge, required examples (ids are permanent) or `%%` tags. Keep every figure path valid; if you add a figure, make it small and necessary.
Write content/audit/reaudit_C{N}.json (array: {"qid","source","required_concept","status_before","action","status_after"}) and content/audit/reaudit_C{N}_summary.md (counts by status, additions, deferrals). Final reply ≤ 6 lines: items assessed, gaps found/fixed, net words added, deferred.
