"""Build the four books in the academy's 7-unit / 11-chapter structure."""
import sys, os, glob, json
sys.path.insert(0, "/home/user/OmniRouter/apes_project/tools")
from s4s_book import *
from structure import *
C = f"{ROOT}/content"
PRACTICE = json.load(open(f"{C}/restructure/practice_info.json")) if os.path.exists(f"{C}/restructure/practice_info.json") else {}
PRACTICE = {int(k): v for k, v in PRACTICE.items()}
UNIT_ART = lambda u: f"{ART}/unit{u}.png"

def md(b, p, pb=False, skip_h1=False):
    if os.path.exists(p): b.add_markdown(p, skip_h1=skip_h1)

def unit_label(u): return f"{UNITS[u][0]} — {UNITS[u][1]}"

def structured(b, chapter_file):
    """Unit openers + chapter openers; chapter_file(ch) -> path of the chapter's markdown (or None)."""
    for u, (lab, ttl, chs) in UNITS.items():
        b.unit_opener(lab, ttl, [(c, CHAPTERS[c][0]) for c in chs], art=UNIT_ART(u))
        for ch in chs:
            title, secs = CHAPTERS[ch]
            b.chapter_opener(ch, title, [(f"{ch}.{k}", s) for k, s in enumerate(secs, 1)], unit_label(u))
            p = chapter_file(ch)
            if p and os.path.exists(p): b.add_markdown(p, skip_h1=True)

def grouped(b, chapter_file, part_title, part_intro):
    """Solutions-style layout: one part divider, then one band per chapter (no per-chapter page break)."""
    b.heading(1, part_title)
    if part_intro: b.para(part_intro, 11, after=6)
    for u, (lab, ttl, chs) in UNITS.items():
        for ch in chs:
            title, secs = CHAPTERS[ch]
            b.heading(2, f"Chapter {ch} — {title}   ({lab.title()})")
            p = chapter_file(ch)
            if p and os.path.exists(p):
                lines = open(p, encoding="utf-8").read().splitlines()
                lines = [l for l in lines if not l.startswith("## Chapter")]
                b.render_blocks(lines)

BOOKS = {}
FEATURES = {1: ["7 Units · 11 Chapters", "Original Diagrams & Models", "Aligned to the 2026 CED"],
            2: ["MCQs then FRQs by Chapter", "Four Full Predicted Exams", "2026 Exam Format"],
            3: ["Every Example Solved", "All Questions & Four Exams", "Step-by-Step Reasoning"],
            4: ["Verified Years on Every Item", "MCQs First, FRQs Second", "Solutions at the End"]}

def c1(b):
    b.base = f"{C}/book1"
    structured(b, lambda ch: f"{C}/book1/C{ch}.md")
BOOKS[1] = dict(short="Complete Study Guide", num="BOOK 1 OF 4", title_lines=["COMPLETE", "STUDY GUIDE"], subtitle="Seven units · eleven chapters · every concept explained simply, with original diagrams and unsolved classroom examples",
    hero="hero1", features=FEATURES[1], tagline="", backtext="Every topic of the AP Environmental Science course explained simply, accurately and completely — from the structure of the Earth to global change — with original diagrams, formulas and exam strategies.",
    bullets=["**Simple first, then complete:** each topic starts in plain English and builds to the full science.", "**Original diagrams** and worked formulas for every major process.", "**Unsolved classroom examples** in every chapter; full solutions are in Book Three.", "**Complete College Board coverage** through an internal topic cross-reference."],
    out_base="APES_Complete_Study_Guide", _content=c1, toc_depth=3, practice_info=PRACTICE,
    legal=["Book One teaches the complete course in the academy's seven-unit, eleven-chapter order. Classroom examples are intentionally unsolved; complete worked solutions are in Book Three."])

def c2(b):
    b.base = f"{C}/book2"
    md(b, f"{C}/front/b2_intro.md")
    structured(b, lambda ch: f"{C}/book2/C{ch}.md")
    b.heading(1, "Four Complete AP Environmental Science Predicted Practice Exams")
    b.para("The four exams that follow each contain 80 multiple-choice questions and 3 free-response questions, built to the 2026 exam blueprint. They are original practice exams written by Success4Sure Academy; they are not official, leaked or guaranteed College Board questions. Complete answer keys and solutions are in Book Three, Part III.", 11)
    for k in range(1, 5): md(b, f"{C}/book2/PE{k}.md")
BOOKS[2] = dict(short="Practice Questions & Predicted Exams", num="BOOK 2 OF 4", title_lines=["CLASSIFIED PRACTICE QUESTIONS", "& FOUR PREDICTED EXAMS"], title_size=24, subtitle="Chapter-by-chapter MCQs and FRQs, then four complete exams built for the 2026 format",
    hero="hero2", features=FEATURES[2], tagline="", backtext="Original multiple-choice and free-response practice for all eleven chapters, followed by four full-length predicted examinations. Complete solutions are in Book Three.",
    bullets=["**In every chapter:** Section A (multiple choice) first, Section B (free response) second.", "**Four predicted exams** of 80 MCQ + 3 FRQ each, at the very end of the book.", "**Data, graphs and calculations** in the style of the 2026 exam.", "**No answers printed here** — solutions are in Book Three."],
    out_base="APES_Classified_Practice_4_Predicted_Exams", _content=c2, toc_depth=2,
    legal=["All questions in this book are original works written for Success4Sure Academy. No solutions appear in this book; complete solutions are in Book Three."])

def c3(b):
    b.base = f"{C}/book3"
    md(b, f"{C}/front/b3_intro.md")
    grouped(b, lambda ch: f"{C}/book3/gen/SG_C{ch}_sol.md", "Part I — Book One Classroom Example Solutions", "Worked solutions to every unsolved classroom example in Book One, organized by chapter in the order the examples appear in the guide.")
    grouped(b, lambda ch: f"{C}/book3/gen/QB_C{ch}_sol.md", "Part II — Book Two Classified Question Solutions", "For each chapter: MCQ answers and explanations first, then complete FRQ solutions.")
    b.heading(1, "Part III — Four Predicted Practice Exam Solutions")
    b.para("For each exam: MCQ answers and explanations first, then complete FRQ solutions.", 11)
    for k in range(1, 5): md(b, f"{C}/book3/PE{k}_sol.md")
BOOKS[3] = dict(short="Complete Solutions", num="BOOK 3 OF 4", title_lines=["COMPLETE", "SOLUTIONS"], subtitle="Every classroom example, every classified question and all four predicted exams — fully solved",
    hero="hero3", features=FEATURES[3], tagline="", backtext="Complete solutions for the Book One classroom examples, the Book Two classified questions and all four predicted examinations, organized by the same eleven chapters.",
    bullets=["**Part I:** every Book One classroom example, solved step by step.", "**Part II:** every classified question — MCQ explanations first, then FRQ solutions.", "**Part III:** complete solutions to the four predicted exams.", "**Consistent IDs:** each solution carries the ID printed beside its question."],
    out_base="APES_Complete_Solutions", _content=c3, toc_depth=2,
    legal=["This book contains solutions for Books One and Two only. Solutions to the College Board questions in Book Four are printed at the end of Book Four."])

def c4(b):
    b.base = f"{C}/book4/gen"
    md(b, f"{C}/front/b4_intro.md")
    b.heading(1, "Part I — Classified Questions")
    b.para("Every entry corresponds to a question from a College Board released AP Environmental Science examination. To protect College Board copyright, question text and figures are not reproduced: each entry gives the verified examination year and an original description of the task. Original solutions are in Part II at the end of this book.", 11, after=6)
    structured(b, lambda ch: f"{C}/book4/gen/Q_C{ch}.md")
    grouped(b, lambda ch: f"{C}/book4/gen/S_C{ch}.md", "Part II — Complete Solutions", "Solutions are written by Success4Sure Academy and classified by the same chapters as Part I: MCQ first, FRQ second. For multiple-choice items the official key letter refers to the choices printed in the original exam (older exams used five choices; the 2026 exam uses four).")
BOOKS[4] = dict(short="College Board Questions & Solutions", num="BOOK 4 OF 4", title_lines=["COLLEGE BOARD", "RELEASED QUESTIONS", "& COMPLETE SOLUTIONS"], title_size=24, subtitle="Verified released-exam questions classified by chapter — MCQs first, FRQs second — with every solution at the end",
    hero="hero4", features=FEATURES[4], tagline="", backtext="College Board released questions classified by the academy's seven units and eleven chapters, MCQs first and FRQs second, with original complete solutions at the end of the book.",
    bullets=["**Verified year** shown beside every question.", "**MCQs first, FRQs second** in every chapter.", "**All solutions at the end** of this book, classified the same way.", "**Independent publication:** not endorsed by the College Board."],
    out_base="APES_College_Board_Questions_And_Solutions", _content=c4, toc_depth=2, show_ids=False,
    legal=["AP® is a registered trademark of the College Board. This book is independently produced by Success4Sure Academy and is not endorsed by the College Board. Success4Sure Academy is responsible for the classification, organization and original explanations.", "Question text and figures from College Board released materials are not reproduced; each entry gives the verified examination year and an original description of the task."])

if __name__ == "__main__":
    n = int(sys.argv[1]); out = sys.argv[2] if len(sys.argv) > 2 else f"{ROOT}/build/book{n}"
    d, p, b = build_book(BOOKS[n], out); print(d, p)
    from pypdf import PdfReader; print("pages", len(PdfReader(p).pages))
