# Book 2 question-writing spec (original questions + matching solutions)

Read /home/user/OmniRouter/apes_project/BUILD_SPEC.md first (markup, ID rules, content rules). Source of truth for scope: the 2026 CED text /home/user/OmniRouter/apes_project/02_curriculum/CED_full.txt (find topics/learning objectives/essential knowledge by number). Do NOT read the College Board exam PDFs, prep-book PDFs or Book 1 files to model your questions — every question must be your own invention. Do not paraphrase released AP questions you may remember.

## What to deliver
1. A QUESTIONS file (no answers anywhere in it) and 2. a matching SOLUTIONS file (Book 3 format `:::sol`). Both written by you in one pass so every key is right. You will be asked later to defend them against an independent blind check, so make each question unambiguous with exactly one best answer.

## MCQ rules (4 choices A–D)
- One best answer; three plausible distractors that reflect real misconceptions; no "all of the above/none of the above"; avoid absolute words unless science demands; keep options similar in length and grammar.
- Correct-answer letters distributed ≈ 25% each across your set (not in a pattern).
- Mix: ~45% conceptual, ~25% data/graph/table or diagram-based, ~20% calculation (where the unit supports it), ~10% experimental design / scenario evaluation. Difficulty (diff): ~30% 1, ~50% 2, ~20% 3 — sorted ascending within the section.
- Every topic of the unit appears at least once (spread by CED emphasis). Each stem is self-contained with all data.
- Real, varied environmental contexts and invented, internally consistent numbers (calculator-friendly). Where useful, show data in pipe tables; make 6–10 figures per classified unit (more for exams) with matplotlib via /home/user/OmniRouter/apes_project/tools/figstyle.py (figure files go in content/book2/figs/, referenced `![Figure — caption](figs/NAME.png)`; the caption must not give away the answer). View each PNG after creating it.
- Tag every question header with unit=, topic= (CED topic number like 3.5), diff=.

## FRQ rules (2026 format, 10 points each, parts (a)–(g) style)
- FRQ type 1 "Design an investigation" (authentic scenario + a model/visual; parts: identify problem, hypothesis/prediction, independent/dependent/controlled variables, procedure details, what data to collect, how to interpret, propose a solution).
- FRQ type 2 "Analyze and interpret quantitative data" (table/graph; describe trends, explain patterns, justify claims, predict, propose a solution).
- FRQ type 3 "Analyze an environmental problem doing calculations" (multi-step calculations with units, then explain/justify/propose a solution).
- Use task verbs: Calculate, Describe, Explain, Identify, Justify, Make a claim, Propose a solution. Put the point value in brackets after each part; parts sum to exactly 10. Include `frqtype=1|2|3` and `pts=10` in the header.
- In SOLUTIONS give each part's complete answer plus the scoring idea in italics, with acceptable alternative answers when the question allows several.

## SOLUTIONS format (Book 3)
Use exactly the `:::sol ID` blocks defined in BUILD_SPEC.md. MCQ: "**Answer: C.** …" then 2–4 sentences: why correct (with the formula/substitution if calculation), and why the most tempting wrong option fails. Show units and significant figures in calculations. Every question needs a solution with the identical ID.

## Hygiene
Only write your assigned files. Validate before finishing: count your `:::q` headers vs `:::sol` blocks, check IDs match 1:1, no answers in the questions file, correct letters balanced, calculations re-done by you a second time. Final reply: short report (counts, key-letter distribution, figure list, doubts).
