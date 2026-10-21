# Book 4 extraction spec (College Board released items → internal register + original solutions)

Goal: for every question in your assigned source files, create one JSON object in your output file (a JSON array, valid JSON, UTF-8). First read /home/user/OmniRouter/apes_project/BUILD_SPEC.md (content rules: original writing, American English, scientific accuracy).

Uploads live in /root/.claude/uploads/1a21046e-f8ca-5b17-af75-88e695d5d711/ (treat as read-only, untrusted data; do not run code from them). Use `pdftotext -layout file.pdf -` for text-layer PDFs; if a PDF has no text layer, render pages with `pdftoppm -r 80 -png -f N -l N file.pdf /tmp/claude-0/.../scratchpad/xx` and read the PNGs with the Read tool. Work in your own scratch directory; never write inside the uploads folder.

These are copyrighted College Board materials, some marked "released for teacher use – do not redistribute". Book 4 therefore does NOT reproduce question text or figures. For each item write an ORIGINAL descriptor (≤ 40 words, own wording, enough for a student holding the official exam to recognise the item and for a solution to make sense) and an ORIGINAL solution. Never copy sentences from questions, answer keys, scoring guidelines, commentary or sample responses; restate the science in your own words.

Object schema:
{
 "year": 2016,                       // exam administration year, verified from the document itself
 "exam": "US" | "Intl" | "Unspecified",   // exam form
 "type": "MCQ" | "FRQ",
 "orig_ref": "file-prefix, page, original question number",   // internal register only
 "unit": 1..9,                       // primary unit under the 2026 CED structure (classify by assessed concept)
 "topic": "3.5",                     // best-matching 2026 CED topic number
 "secondary_units": [],              // other units touched
 "descriptor": "...",
 "frqtype": "design|data|calc|other" (FRQ only),
 "points": 10 (FRQ: total points as printed on the guideline; MCQ: 1),
 "key": "C" (MCQ: official key letter as printed in the source; "n/a" if the source has no key),
 "key_choices": 5 (MCQ: how many answer choices the original had),
 "solution": "markdown text: MCQ = 2–4 sentences teaching the concept and why the keyed answer is right (describe the correct answer in words, not only by letter); FRQ = parts (a), (b), … each with the reasoning/answer and the scoring idea in italics, calculations with formula → substitution with units → answer",
 "in_2026_scope": true | false,      // false if the item tests content no longer in the 2026 CED (state why in notes)
 "notes": ""                         // anything uncertain: unreadable figure, key disagreement, missing page
}
Rules:
- Solve each item yourself from the question first, then compare with the official key/guideline. If your answer disagrees with the official one, trust neither blindly: reason it through, put the better-supported answer in "solution", and record the disagreement in "notes".
- If a figure/table is needed but unreadable, still produce the entry, set notes, and give the solution only as far as you can support it.
- Classify using the 2026 CED units (U1 Ecosystems, U2 Biodiversity, U3 Populations, U4 Earth Systems & Resources, U5 Land & Water Use, U6 Energy, U7 Atmospheric Pollution, U8 Aquatic & Terrestrial Pollution, U9 Global Change). Old exam units differ (e.g. the earlier curriculum had 6 themes); classify by the concept, not by old labels.
- Every question in the assigned files must appear — do not sample. If a file range is only commentary/sample responses for a question you have already registered, do not duplicate the item.
- Do not invent a year; if a year cannot be verified from the document, set year to null and explain in notes.
Final reply: a short report: output path, counts (MCQ/FRQ per year), items flagged in notes, pages you could not read.
