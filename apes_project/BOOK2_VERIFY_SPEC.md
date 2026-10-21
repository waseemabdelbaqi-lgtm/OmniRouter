# Independent verification of Book 2 / Book 3 (blind answer check + FRQ audit)

Read /home/user/OmniRouter/apes_project/BUILD_SPEC.md for markup/ID rules. You are an experienced AP Environmental Science teacher and exam reviewer. You did NOT write these items.

## Step 1 — BLIND solve (do this BEFORE opening any solutions file)
Open only the QUESTIONS file(s) assigned. Do not open content/book3/*, content/book4/*, or content/audit/* until Step 1 is saved. For every MCQ decide the single best answer yourself (use the 2026 CED at /home/user/OmniRouter/apes_project/02_curriculum/CED_full.txt as scope authority; compute every calculation; read every table and figure PNG referenced — view the image files with the Read tool when a question depends on a figure). Also note any MCQ that is ambiguous, has two defensible answers, has zero defensible answers, is scientifically wrong, depends on missing data, or where a figure contradicts the stem.
Save /home/user/OmniRouter/apes_project/content/audit/blind_<TAG>.json : [{"qid":"QB-U1-MCQ001","my_answer":"C","confidence":"high|medium|low","issue":"" }, …] for every MCQ in your files.

## Step 2 — compare and audit
Open the matching solutions file(s) (content/book3/…_sol.md). Then:
1. For each MCQ where my_answer ≠ keyed answer, or issue ≠ "": re-derive carefully, decide who is right, and FIX the question or the solution (Edit tool, minimal change: correct the keyed explanation, or revise stem/options so exactly one answer is defensible; if you change an option letter or correct answer, keep letters balanced ≈ 25% each where possible, and update the solution to match). Never leave a question with two defensible answers.
2. FRQs: check every part's arithmetic, units/significant figures, scientific accuracy, that point values sum to 10, that the solution answers every part, and that the scoring idea is sensible. Fix errors in place.
3. Check that every question has exactly one solution block with the same ID, every referenced figure file exists and is not clipped/overlapping (view each PNG), and that no question text gives away its answer.
4. Distractor quality: where the correct option is conspicuously the longest or the only specific/hedged one, rebalance by editing wording (limit to ~8 edits).
Write /home/user/OmniRouter/apes_project/content/audit/verify_<TAG>.md summarizing: items checked, disagreements found (qid, who was right, fix made), FRQ errors fixed, figure problems, and anything unresolved.
Do not restructure files; keep IDs and markup unchanged. Final reply: counts (MCQ blind-agreement rate, number of fixes, unresolved issues) in ≤ 8 lines.
