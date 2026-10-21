# New practice questions for the academy's new chapter topics (Book Two) + solutions (Book Three)

Read BOOK2_SPEC.md (question/solution rules, MCQ and FRQ format, quality rules) and BUILD_SPEC.md (markup) in /home/user/OmniRouter/apes_project/ first. Everything in BOOK2_SPEC.md applies EXCEPT the file names, IDs and headers given here.

Context: the book is now organized in 7 units / 11 chapters (tools/structure.py lists every chapter and section title). Existing verified questions were re-sorted into chapters, but the sections listed in your assignment have NO questions yet (they are new academy topics: geology, hurricanes, aquifers, ice, oceans, sulfur cycle, wildfires, rangelands, transportation, public lands, mineral reserves, economics, energy concepts, transport/mass transit, groundwater, water testing/purification, contaminated-site cleanup, perpetual storage, environmental economics, climate mitigation...). Write original questions at AP exam level and style (4-choice MCQ; 2026 FRQ format), scientifically accurate, unambiguous, one best answer, balanced key letters (≈25% each across your set), figures/tables where natural (≥ 25% data/diagram items, ≥ 15% calculations where the topic allows). Do not read College Board exam PDFs or prep books. Do not copy any published question.

## IDs and headers (different from BOOK2_SPEC)
`:::q QB-C{N}-MCQ001 | chapter={N} | sec={k} | unit={nearest 2026 CED unit 1-9 or 0} | topic={nearest CED topic like 4.1 or ext} | diff=2`
FRQ: `:::q QB-C{N}-FRQ001 | chapter={N} | sec={k} | unit=… | topic=… | diff=3 | frqtype=1|2|3 | pts=10`
N = chapter number; `sec` = the section number inside that chapter (from structure.py) the question mainly assesses. Numbering restarts per chapter, three digits. Order each chapter's MCQs by sec then diff. Sections to cover and counts are in your assignment: write exactly that many.

## Files (write only these)
- Questions (no answers anywhere): /home/user/OmniRouter/apes_project/content/book2/N_C{N}.md — ONLY the `:::q` blocks (MCQs first, then FRQs); no headings.
- Solutions: /home/user/OmniRouter/apes_project/content/book3/QB_C{N}_sol.md — ONLY `:::sol QB-C{N}-…` blocks in the same order (BOOK2_SPEC format: `**Answer: C.** …`; FRQ parts with italic scoring ideas).
- Figures: content/book2/figs/QBC{N}_*.png + script QBC{N}_make.py (tools/figstyle.py). View each PNG; make it correct, labelled, readable, original.
Validate before finishing: block counts match 1:1; no answers in the question file; every figure exists; re-derive every calculation twice. Final reply ≤ 6 lines (counts, key-letter spread, figures, doubts).
