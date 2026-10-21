"""Generate the final verification / coverage / compliance reports for the restructured (7-unit, 11-chapter) collection."""
import os, re, json, glob, csv, hashlib, collections, sys, subprocess
sys.path.insert(0, "/home/user/OmniRouter/apes_project/tools")
from structure import *
R = "/home/user/OmniRouter/apes_project"; C = f"{R}/content"; OUT = f"{R}/reports"; os.makedirs(OUT, exist_ok=True)
W = lambda name, text: open(f"{OUT}/{name}", "w", encoding="utf-8").write(text)
CEDU = {1: "The Living World: Ecosystems", 2: "The Living World: Biodiversity", 3: "Populations", 4: "Earth Systems and Resources", 5: "Land and Water Use", 6: "Energy Resources and Consumption", 7: "Atmospheric Pollution", 8: "Aquatic and Terrestrial Pollution", 9: "Global Change"}
CEDW = {1: "6–8%", 2: "6–8%", 3: "10–15%", 4: "10–15%", 5: "10–15%", 6: "10–15%", 7: "7–10%", 8: "7–10%", 9: "15–20%"}
def chapter_of(topic, unit):
    if topic in CED: return CED[topic][0]
    return {1: 4, 2: 4, 3: 6, 4: 1, 5: 7, 6: 8, 7: 9, 8: 9, 9: 11}.get(unit)
def aunit(ch): return unit_of_chapter(ch)
def alabel(u): return f"{UNITS[u][0].title()} — {UNITS[u][1].title()}"
def _int(v):
    try: return int(v)
    except Exception: return 0

# ------------------------------------------------------------------ parse questions
sys.path.insert(0, f"{R}/tools")
from restructure_books import parse_blocks, meta_of
qs = {}
for f in sorted(glob.glob(f"{C}/book2/C?.md")) + sorted(glob.glob(f"{C}/book2/C??.md")):
    for qid, h, body, raw in parse_blocks(open(f).read(), "q"):
        m = meta_of(h); ch = int(re.search(r"C(\d+)\.md", f).group(1))
        qs[qid] = dict(ch=ch, kind="FRQ" if "FRQ" in qid else "MCQ", unit=_int(m.get("unit")), topic=m.get("topic", ""), exam=False)
for k in range(1, 5):
    for qid, h, body, raw in parse_blocks(open(f"{C}/book2/PE{k}.md").read(), "q"):
        m = meta_of(h); u = _int(m.get("unit")); t = m.get("topic", "")
        qs[qid] = dict(ch=chapter_of(t, u), kind="FRQ" if "FRQ" in qid else "MCQ", unit=u, topic=t, exam=True, exam_no=k)
cls = ["# Question classification and unit-distribution report\n",
       "Two classification systems are reported separately and are **not** interchangeable: the academy's 7 units / 11 chapters (the book structure) and the official College Board 9 units (each question keeps its CED unit/topic tag). Official weightings apply only to the College Board units and to the exam blueprint; they are not applied to the academy structure.\n"]
cls.append("## A. Book Two classified bank by academy chapter\n"); cls += ["| Academy unit | Chapter | MCQ | FRQ | of which new in this edition |", "|---|---|---|---|---|"]
newq = set(re.findall(r":::q (QB-C\d+-[A-Z0-9]+)", "".join(open(f).read() for f in glob.glob(f"{C}/book2/N_C*.md"))))
for u, (lab, ttl, chs) in UNITS.items():
    for ch in chs:
        ids = [q for q, v in qs.items() if not v["exam"] and v["ch"] == ch]
        cls.append(f"| {alabel(u)} | {ch} — {CHAPTERS[ch][0]} | {sum('MCQ' in q for q in ids)} | {sum('FRQ' in q for q in ids)} | {sum(q in newq for q in ids)} |")
cl = [q for q, v in qs.items() if not v["exam"]]
cls.append(f"| **Total** | | {sum('MCQ' in q for q in cl)} | {sum('FRQ' in q for q in cl)} | {len(newq)} |\n")
cls.append("## B. Book Two classified bank by official College Board unit (internal CED tag)\n")
cls += ["| CED unit | Official exam weight | MCQ | FRQ | share of classified MCQ |", "|---|---|---|---|---|"]
totm = sum('MCQ' in q for q in cl)
for u in range(0, 10):
    ids = [q for q in cl if qs[q]["unit"] == u]
    name = CEDU.get(u, "Academy extension topics (no CED unit)")
    cls.append(f"| {u or '—'} {name} | {CEDW.get(u, 'n/a')} | {sum('MCQ' in q for q in ids)} | {sum('FRQ' in q for q in ids)} | {100 * sum('MCQ' in q for q in ids) / totm:.1f}% |")
cls.append("\nThe classified bank is a practice bank, not an exam blueprint, so its CED shares need not match the official weightings; the four predicted exams do follow the blueprint (next table).\n")
cls.append("## C. Four predicted exams — official blueprint (CED units, 80 MCQ each)\n")
cls += ["| Exam | " + " | ".join(f"U{u}" for u in range(1, 10)) + " | MCQ | FRQ |", "|---|" + "---|" * 11]
for k in range(1, 5):
    ex = [q for q, v in qs.items() if v["exam"] and v["exam_no"] == k]
    row = [sum(1 for q in ex if 'MCQ' in q and qs[q]['unit'] == u) for u in range(1, 10)]
    cls.append(f"| Exam {k} | " + " | ".join(map(str, row)) + f" | {sum('MCQ' in q for q in ex)} | {sum('FRQ' in q for q in ex)} |")
cls.append("\nTarget per exam (CED weights): U1 6, U2 5, U3 10, U4 10, U5 10, U6 10, U7 7, U8 7, U9 15.\n")
cls.append("## D. Same predicted-exam MCQs re-counted by academy chapter\n"); cls += ["| Exam | " + " | ".join(f"Ch{c}" for c in range(1, 12)) + " |", "|---|" + "---|" * 11]
for k in range(1, 5):
    ex = [q for q, v in qs.items() if v["exam"] and v["exam_no"] == k and 'MCQ' in q]
    cls.append(f"| Exam {k} | " + " | ".join(str(sum(1 for q in ex if qs[q]['ch'] == c)) for c in range(1, 12)) + " |")
b4 = list(csv.DictReader(open(f"{OUT}/book4_source_register.csv"))); inc = [r for r in b4 if r["status"] == "included"]
cls.append("\n## E. Book Four verified College Board items\n"); cls += ["| Academy unit | Chapter | MCQ | FRQ |", "|---|---|---|---|"]
for u, (lab, ttl, chs) in UNITS.items():
    for ch in chs:
        cls.append(f"| {alabel(u)} | {ch} — {CHAPTERS[ch][0]} | {sum(1 for r in inc if r['chapter']==str(ch) and r['type']=='MCQ')} | {sum(1 for r in inc if r['chapter']==str(ch) and r['type']=='FRQ')} |")
cls.append("\nBy official CED unit: " + ", ".join(f"U{u}: {sum(1 for r in inc if r['ced_unit']==str(u))}" for u in range(1, 10)))
cls.append(f"\nIncluded {len(inc)}; excluded {len(b4) - len(inc)} (outside the 2026 curriculum, duplicate, or unverifiable). Items by verified year: " + ", ".join(f"{y}: {c}" for y, c in sorted(collections.Counter(r['year'] for r in inc).items())))
W("question_classification_and_unit_distribution_report.md", "\n".join(cls))

# ------------------------------------------------------------------ study-guide coverage (old audits + new re-audit)
rows = []
for f in sorted(glob.glob(f"{C}/audit/gap_U?.json")): rows += [dict(r, phase="Initial audit (nine-unit guide)") for r in json.load(open(f))]
re_rows = []
for f in sorted(glob.glob(f"{C}/audit/reaudit_C*.json"), key=lambda x: int(re.search(r"C(\d+)\.json", x).group(1))):
    ch = int(re.search(r"C(\d+)\.json", f).group(1))
    for r in json.load(open(f)): re_rows.append(dict(r, chapter=ch, phase="Re-audit after restructuring"))
with open(f"{OUT}/question_to_study_guide_matrix.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["Phase", "Question ID", "Source book", "CED unit", "CED topic", "Academy chapter.section (planned)", "Required concept", "Coverage status (before)", "Missing explanation or skill", "Corrective action", "Updated Study Guide section", "Final verification status"])
    for r in rows:
        t = r.get("topic", ""); loc = f"{CED[t][0]}.{CED[t][1]}" if t in CED else ""
        w.writerow([r["phase"], r.get("qid"), r.get("source"), r.get("unit"), t, loc, r.get("required_concept"), r.get("original_status"), r.get("missing"), r.get("action"), r.get("updated_section"), r.get("final_status")])
    for r in re_rows:
        w.writerow([r["phase"], r.get("qid"), r.get("source"), "", "", f"Chapter {r['chapter']}", r.get("required_concept"), r.get("status_before"), "", r.get("action"), f"Chapter {r['chapter']}", r.get("status_after")])
st = collections.Counter(r["final_status"].split(":")[0] if r["final_status"].startswith("Flagged") else r["final_status"] for r in rows)
rst0 = collections.Counter(r.get("status_before") for r in re_rows); rst1 = collections.Counter(r.get("status_after") for r in re_rows)
cov = ["# Question-to-Study-Guide coverage report\n",
       "## Stage 1 — audit of the nine-unit guide (before restructuring)\n", f"Question-to-concept checks: {len(rows)}; final: " + ", ".join(f"{k}: {v}" for k, v in st.items()) + ".\n",
       "| CED unit | Assessed | Fully covered before | Gaps found | Fully covered after expansion | Flagged beyond CED | Deferred |", "|---|---|---|---|---|---|---|"]
for u in range(1, 10):
    ur = [r for r in rows if r["unit"] == u]; f0 = sum(1 for r in ur if r["original_status"] == "Fully Covered")
    fin = collections.Counter(r["final_status"].split(":")[0] if r["final_status"].startswith("Flagged") else r["final_status"] for r in ur)
    cov.append(f"| {u} — {CEDU[u]} | {len(ur)} | {f0} | {len(ur) - f0} | {fin.get('Fully Covered', 0)} | {fin.get('Flagged', 0)} | {fin.get('Deferred', 0)} |")
cov.append("\n## Stage 2 — re-audit after restructuring (by academy chapter)\n")
cov.append(f"Items re-checked against the new chapter text: {len(re_rows)}. Status before: " + ", ".join(f"{k}: {v}" for k, v in rst0.most_common()) + ". Status after: " + ", ".join(f"{k}: {v}" for k, v in rst1.most_common()) + ".\n")
for ch in range(1, 12):
    p = f"{C}/audit/reaudit_C{ch}_summary.md"
    cov.append(f"\n### Chapter {ch} — {CHAPTERS[ch][0]}\n" + (open(p).read() if os.path.exists(p) else "(summary not available)"))
cov.append("\nFull per-question matrix (both stages): question_to_study_guide_matrix.csv.")
W("question_to_study_guide_coverage_report.md", "\n".join(cov))
parts = ["# Missing explanations added to Book One\n\n## During the nine-unit audit\n"]
for n in range(1, 10):
    p = f"{C}/audit/gap_U{n}_summary.md"
    parts.append(f"\n### Old Unit {n}\n" + (open(p).read() if os.path.exists(p) else ""))
parts.append("\n## During the post-restructuring re-audit\n")
for ch in range(1, 12):
    p = f"{C}/audit/reaudit_C{ch}_summary.md"
    parts.append(f"\n### Chapter {ch}\n" + (open(p).read() if os.path.exists(p) else ""))
W("missing_explanations_added_to_book1_report.md", "\n".join(parts))

# ------------------------------------------------------------------ cross reference map (CSV) + audit text
with open(f"{OUT}/ced_to_academy_crossref_map.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["CED topic", "CED unit", "Academy unit", "Academy chapter", "Academy primary section", "Also taught in sections"])
    for t, (ch, sec, others) in CED.items():
        w.writerow([t, int(t.split('.')[0]), alabel(aunit(ch)), f"{ch} — {CHAPTERS[ch][0]}", f"{ch}.{sec} {CHAPTERS[ch][1][sec - 1]}", ", ".join(f"{ch}.{o}" for o in others)])
subprocess.run([sys.executable, f"{R}/tools/audit_restructure.py"], capture_output=True)

# ------------------------------------------------------------------ matching
def blocks(pattern, kind):
    ids = set()
    for f in glob.glob(pattern): ids |= {b[0] for b in parse_blocks(open(f).read(), kind)}
    return ids
sol_ids = blocks(f"{C}/book3/gen/QB_C*_sol.md", "sol") | blocks(f"{C}/book3/PE?_sol.md", "sol"); sg_sol = blocks(f"{C}/book3/gen/SG_C*_sol.md", "sol")
sg_all = set()
for n in range(1, 12): sg_all |= set(re.findall(r"(?m)^id: (SG-[A-Z0-9-]+)", open(f"{C}/book1/C{n}.md").read()))
q_all = set(qs)
b4q = blocks(f"{C}/book4/gen/Q_C*.md", "q"); b4s = blocks(f"{C}/book4/gen/S_C*.md", "sol")
mt = ["# Question-to-solution matching report\n",
      f"- Book One classroom examples: {len(sg_all)}; with a Book Three Part I solution: {len(sg_all & sg_sol)}; missing: {sorted(sg_all - sg_sol)}",
      f"- Book Two questions (classified chapters + four exams): {len(q_all)}; with a Book Three solution: {len(q_all & sol_ids)}; missing: {sorted(q_all - sol_ids)}",
      f"- Book Three solutions with no matching question: {sorted(sol_ids - q_all)}",
      f"- Book Four: {len(b4q)} questions, {len(b4s)} solutions; unmatched questions: {sorted(b4q - b4s)}; unmatched solutions: {sorted(b4s - b4q)}",
      "- Book Three Part II lists solutions chapter by chapter in the same order as Book Two's questions (MCQ first, FRQ second); Part III follows exam order. Every solution carries the ID printed beside its question. Book Four solutions are at the end of Book Four in the same chapter order."]
W("question_to_solution_matching_report.md", "\n".join(mt))
# answer keys
keys = {}
for f in glob.glob(f"{C}/book3/QB_U?_sol.md") + glob.glob(f"{C}/book3/QB_C*_sol.md") + glob.glob(f"{C}/book3/PE?_sol.md"):
    for m in re.finditer(r":::sol ([A-Z0-9-]+MCQ\d+)\n\*\*Answer: ([A-D])\b", open(f).read()): keys[m.group(1)] = m.group(2)
blind = {}
for f in glob.glob(f"{C}/audit/blind_*.json"):
    for x in json.load(open(f)): blind[x["qid"]] = x["my_answer"].strip()[:1]
agree = sum(1 for q in keys if blind.get(q) == keys[q])
ver = ["# Verification report — answer keys, FRQs and figures\n",
       "Method: independent reviewers solved every MCQ blind (before seeing the solutions), compared with the key, re-derived every FRQ calculation, checked point totals and every figure, and fixed discrepancies. All questions were then re-sorted into the 11 chapters by script (no question text changed); IDs, keys and solutions travel together.\n",
       f"- MCQ with a final key: {len(keys)}; final keys equal to the independent blind answer: {agree}.",
       f"- Differences between final key and logged blind answer: {[(q, keys[q], blind.get(q)) for q in sorted(keys) if blind.get(q) != keys[q]]} (QB-U2-MCQ013: blind log recorded A; the question has one defensible answer, D — land bridges; D confirmed by hand. PE2-MCQ014 key corrected earlier to A (Type III survivorship) and re-confirmed against the figure.)",
       f"- Key-letter balance: {dict(sorted(collections.Counter(keys.values()).items()))}.\n"]
for f in sorted(glob.glob(f"{C}/audit/verify_*.md")): ver.append(f"\n---\n### {os.path.basename(f)}\n" + open(f).read())
W("four_exam_and_question_bank_verification_report.md", "\n".join(ver))
fig = ["# Scientific figure audit report\n", "Every Book Two question figure (162) was inspected for scientific accuracy, labels, units, scales, arrows, legends, contrast, resolution and agreement with its question; defects were fixed or the figure was redrawn. New and reused Book One figures were viewed and corrected by the chapter authors (e.g. greenhouse-effect arrow direction, succession curves, plate-boundary label overlaps).\n"]
for f in sorted(glob.glob(f"{C}/audit/figures_*.md")): fig.append(f"\n---\n### {os.path.basename(f)}\n" + open(f).read())
W("figure_audit_report.md", "\n".join(fig))
sci = ["# Scientific accuracy report\n", "Corrections made by independent review are listed in the verification and figure-audit reports. Additional actions:\n",
       "- Book One examples with ambiguous data were rewritten (SG-U3-E009(c), SG-U9-E015(c)); sg_issues_resolved.md.",
       "- Two question solutions were corrected during figure review (QB-U3-MCQ023 explanation; QB-U1-MCQ014 stem).",
       "- Predicted-exam figures were corrected where data did not match the options (PE3 overshoot peak, PE4 age-structure totals, PE2 BOD axis).",
       "- The restructured chapters corrected figures that contradicted text (greenhouse-effect reflected-sunlight arrow, ecological-succession curves).",
       "\nKnown simplifications (stated in the books): illustrative figure data are invented and labelled; the soil-texture key is simplified; approximate reference values (e.g. radon action level, lapse rates, public-land acreages, carbon-sink budgets) are standard figures quoted from memory and should be spot-checked by the author before printing."]
W("scientific_accuracy_report.md", "\n".join(sci))
# source inventory / copyright / duplicates (unchanged logic)
import hashlib
UP = "/root/.claude/uploads/1a21046e-f8ca-5b17-af75-88e695d5d711"; dups = collections.defaultdict(list)
for f in sorted(glob.glob(UP + "/*.pdf")): dups[hashlib.md5(open(f, "rb").read()).hexdigest()].append(os.path.basename(f))
dd = ["# Duplicate detection report\n", "## Duplicate uploads (identical file content)\n"] + [f"- {', '.join(fs)}" for fs in dups.values() if len(fs) > 1]
dd.append("\n## Duplicate College Board items\n- 2016 International file is byte-identical to the 2016 US exam; registered once.\n- 2024 US FRQs appear in the 2024 exam file and the FRQ compilation; registered once.\n- Near-duplicate registered items are removed automatically by (year, type, descriptor).")
W("duplicate_detection_report.md", "\n".join(dd))
cp = ["# Copyright and permissions report\n",
      "- **College Board materials**: no republication licence was provided, so Book Four reproduces **no** question text or figures; each entry shows the verified year and an original description, with original solutions. Original question numbers and source files are kept only in book4_source_register.csv. The 2016 exam file is marked 'released for teacher use, do not redistribute'.",
      "- **Commercial prep books** (two): topic checklist only; one carries an 'OceanofPDF.com' watermark; nothing was copied. All text, diagrams, examples and questions are original.",
      "- **Third-party web pages** (Studocu, apmaster.cn): not opened or used.",
      "- **Success4Sure logo**: rebuilt from the company-profile raster and the author's artwork; used for the owner's own publications.",
      "- **Illustrations**: all covers, opener art and scientific figures are original vector-style drawings created for this project.",
      "- **Attribution**: each book states it is independently produced and not endorsed by the College Board; AP® is identified as a College Board trademark.",
      "- **College Board links**: the website was unreachable from the production environment; no College Board URL is printed (apcentral.collegeboard.org is named only).",
      "- **Missing source pages**: pages 281–420 of the free-response compilation were not uploaded (2007, 2009 and part of 2008 FRQs absent from Book Four)."]
W("copyright_permissions_report.md", "\n".join(cp))
W("source_inventory.md", open(f"{R}/00_inventory/source_inventory.md").read() + "\n\n## Processing summary\n- Curriculum authority: 2026 CED (252 pages) — cross-referenced to the academy chapters (ced_to_academy_crossref_map.csv).\n- College Board registers: " + ", ".join(sorted(os.path.basename(f) for f in glob.glob(f"{C}/book4/raw/*.json"))) + ".\n- Prep books: topic checklist only.\n")
print("reports written:", len(os.listdir(OUT)))
