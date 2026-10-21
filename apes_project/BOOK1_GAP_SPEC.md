# Study Guide gap audit (question-to-explanation coverage) — one unit per agent

Read /home/user/OmniRouter/apes_project/BUILD_SPEC.md (markup + rules) first.

## Your inputs for Unit N
1. Book 1 unit file (you will edit it): /home/user/OmniRouter/apes_project/content/book1/UN.md and its figures folder content/book1/figs/.
2. Questions that assess Unit N (read ALL of them):
   - Book 2 classified bank: content/book2/UN.md (IDs QB-UN-…); solutions in content/book3/QB_UN_sol.md.
   - Book 2 predicted exams: content/book2/PE1.md … PE4.md — only the questions whose header says unit=N (solutions in content/book3/PEk_sol.md).
   - Book 4 College Board items for unit N: the JSON registers /home/user/OmniRouter/apes_project/content/book4/raw/*.json (fields unit, topic, secondary_units, descriptor, solution, orig_ref, type, year). Use items where unit == N or N is in secondary_units. These are descriptors, not full questions: work out the concept each needs from the descriptor + solution.
3. The CED: 02_curriculum/CED_full.txt (scope authority).

## Procedure
A. For EVERY question above, identify: primary unit/topic, concept assessed, required background knowledge, terminology, formulas/maths, graph skill, experimental/data-analysis skill, environmental process, reasoning strategy.
B. Compare with the Book 1 unit file. Do not assume coverage because a heading exists: could a student who has only read Book 1 solve it? Classify as one of: Fully Covered; Partially Covered; Missing; Scientifically Incorrect; Insufficiently Explained; Missing Formula; Missing Diagram; Missing Mathematical Skill; Missing Experimental Skill.
C. Fix the gaps by EDITING UN.md (use the Edit tool; insert inside the correct `## Topic N.x` section, before that topic's closing summary box; fix any incorrect statement in place). Add what the gap needs: concept explanation, definitions, mechanism, a diagram (new figure script `figs/gap_UN_make.py`, PNGs `figs/UN_gap_*.png`), formula with variable definitions and units, maths method, graph-reading guide, data-analysis/experimental-design technique, real-world application, misconception warning, and a NEW original unsolved classroom example where useful (continue the id sequence after the file's last `SG-UN-Ennn`; unsolved — no answers or hints). Write original text only; never insert a question or its answer from the banks. Teach the concept so the student can solve the question independently.
D. Re-check every question after editing; set final status Fully Covered (or, if a question goes beyond the verified CED scope, "Flagged: beyond CED" and do NOT expand the guide for it).
E. Page budget: your net addition to the unit is ≤ {PAGES} rendered pages (≈ 380 words/page, figure ≈ 0.35 page). Prioritise gaps by how many questions they affect and by exam weight. Prefer tightening existing text to make room. If gaps exceed the budget, cover the highest-impact ones and list the rest as "deferred" in your report — never pad.
F. Do not restructure the file, do not delete topics, keep the markup valid, keep every existing example ID unchanged.

## Required output
Write /home/user/OmniRouter/apes_project/content/audit/gap_UN.json — a JSON array, one object per question assessed:
{"qid":"QB-U3-MCQ014" (for Book 4 use "CB:<year>:<orig_ref>"), "source":"Book2-QB|Book2-PE|Book4", "unit":N, "topic":"3.5", "required_concept":"…", "original_status":"Partially Covered", "missing":"what was missing (or '')", "action":"what you added/changed (or 'none')", "updated_section":"Topic 3.5 — … (SG-U3-E013 …)", "final_status":"Fully Covered|Flagged: beyond CED|Deferred"}
Also write content/audit/gap_UN_summary.md: counts by original and final status, list of everything added (section, ~words, figures, new example ids), deferred and flagged items. Final reply: 8-line report (counts, pages added estimate, new example ids, doubts).
