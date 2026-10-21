# APES Collection — Content Spec (shared by all writers)

Project root: `/home/user/OmniRouter/apes_project/`. Curriculum authority: `02_curriculum/CED_full.txt`
(text of the 2026 College Board Course & Exam Description; page order is scrambled between pieces, so search by unit/topic number).
Publisher: Success4Sure Academy. Sole author/preparer: Mr. Waseem Allabadi (never name any other author, textbook or editor in content).

## Absolute content rules
1. **Original writing only.** Textbooks in the upload folder (prep books, College Board material) may be read for topic coverage and to check facts. Never copy or closely paraphrase their sentences, figures, examples or questions. Write fresh explanations, fresh examples, fresh numbers, fresh scenarios.
2. **American English only.** No Arabic. Metric units (use US units only where AP itself does).
3. **Scientific accuracy first.** Use CED terminology and the CED's unit/topic numbering (e.g. "Topic 1.4"). If a fact is uncertain, leave it out. Numbers in worked data must be internally consistent.
4. No mention of AI, Claude, "as an assistant", sources or file names in the content.
5. MCQ have exactly **four** choices A–D (2026 exam format). Exam = 80 MCQ (60%) + 3 FRQ (40%): FRQ1 Design an investigation, FRQ2 Analyze & interpret quantitative data, FRQ3 Analyze an environmental problem doing calculations; 10 points each. Calculator allowed. Task verbs: Calculate, Describe, Explain, Identify, Justify, Make a claim, Propose a solution.
6. Unit weights: U1 6–8%, U2 6–8%, U3 10–15%, U4 10–15%, U5 10–15%, U6 10–15%, U7 7–10%, U8 7–10%, U9 15–20%.
7. Keep to the page budget you are given. A rendered page holds ≈ 380 words of body text; a figure takes ≈ 0.35 page; a callout box takes its text plus ≈ 2 lines.

## Markup (a custom Markdown subset — my builder parses exactly this)
- `# Unit title` (one per unit file), `## Topic 1.4 — The Carbon Cycle`, `### Sub-heading`. No `####`.
- Paragraphs separated by blank lines. Inline: `**bold**`, `*italic*`. Write chemistry/maths with Unicode: CO₂, H₂O, NOₓ, SO₂, 10⁶, ×, ÷, ≈, →, ≥, ≤, °C, µ, %. **No LaTeX, no HTML.**
- Bullets `- text`; numbered `1. text`. One nesting level max (two-space indent).
- Tables: pipe tables with a header row and a `|---|---|` separator line. Keep ≤ 5 columns.
- Callout boxes (Book 1 only):
```
:::box objectives
- Bullet list of learning objectives
:::
```
  Box kinds: `objectives`, `simple` (Concept Made Simple), `define` (Key Definitions – use `**Term** — meaning` lines), `process` (cause-and-effect chain, use `→`), `formula` (formula + variable definitions + units), `mistake` (Common Student Mistakes), `strategy` (AP Exam Strategy), `apply` (Real-World Example), `summary` (Quick Concept Summary).
- Unsolved classroom example (Book 1): first line `id: SG-U1-E003`, then the full problem. The builder adds working space automatically. Never put an answer or hint of the answer in the box.
```
:::box example
id: SG-U1-E003
Problem text...
:::
```
- Figure: `![Figure 1.3 — Caption text](figs/U1_carbon_cycle.png)` on its own line (path relative to your book folder). Optional width: `{w=0.7}` (fraction of text width, default 0.85) right after the closing parenthesis.
- Extra working lines inside text: `[[space 4]]`.
- Page break: `[[pagebreak]]` (use sparingly).

## Questions (Books 2, 3, 4)
```
:::q QB-U1-MCQ001 | unit=1 | topic=1.4 | diff=2
Stem (may include a table or a figure line).
A) option text
B) option text
C) option text
D) option text
:::
```
FRQ: `:::q QB-U1-FRQ001 | unit=1 | topic=1.4 | diff=3 | frqtype=2 | pts=10` followed by the stem and lettered parts `(a)`, `(b)`, … each on its own line; sub-parts on indented `(i)`. Parts carry points in square brackets at the end, e.g. `(a) Identify … [1]`. Give 8–10 points total.
IDs are permanent: `SG-Un-Ennn` (Book 1 examples), `QB-Un-MCQnnn` / `QB-Un-FRQnnn` (Book 2 classified), `PEk-MCQnnn` / `PEk-FRQnnn` (predicted exam k=1..4), `CB-Un-MCQnnn` / `CB-Un-FRQnnn` (Book 4). Numbers are three digits and unique within their series.
`diff` = 1 easy, 2 medium, 3 hard. Order questions progressively by diff inside a unit.

## Solutions (Book 3 and Book 4)
```
:::sol QB-U1-MCQ001
**Answer: C.** Two-to-four sentence explanation that teaches why C is right and names the specific flaw in each other option when useful.
:::
```
FRQ solutions: `:::sol QB-U1-FRQ001` then `(a) …`, `(b) …` with the scoring idea in italics, e.g. `*(1 point: names X)*`. Calculations: formula → substitution with units → answer with units (and sig figs).

## Figures
Write a Python script next to the figures (`figs/make_<unit>.py`) that imports `/home/user/OmniRouter/apes_project/tools/figstyle.py` (palette, `canvas`, `box`, `arrow`, `save`) and saves PNGs (≈ 6 in wide). Every figure must be original, labeled, readable at 6 in wide, and scientifically correct. Run the script, open the PNGs (Read tool) and fix overlaps/clipping before finishing. Use the brand maroon `#7A1424` for emphasis; use natural colors where the science needs it.

## Deliverable hygiene
Write only to your assigned files. Do not edit other files. Do not run git. When done, reply with a short report: files written, rendered-page estimate (words ÷ 380 + figures×0.35), any scientific doubts, and anything you could not do.
