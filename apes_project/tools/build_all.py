import sys,os,glob
sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from s4s_book import *
C=f"{ROOT}/content"
def md(b,p,pb=False):
    if os.path.exists(p):
        if pb: b.pagebreak()
        b.add_markdown(p)
BOOKS={}
def c2(b):
    md(b,f"{C}/front/b2_intro.md")
    for n in range(1,10): md(b,f"{C}/book2/U{n}.md")
    b.heading(1,"Four Complete AP Environmental Science Predicted Practice Exams")
    b.para("The four exams that follow each contain 80 multiple-choice questions and 3 free-response questions, built to the 2026 exam blueprint. They are original practice exams written by Success4Sure Academy; they are not official, leaked or guaranteed College Board questions. Complete answer keys and solutions are in Book Three, Part III.",11)
    for k in range(1,5): md(b,f"{C}/book2/PE{k}.md")
BOOKS[2]=dict(short="Practice Questions & Predicted Exams",num="Book Two",title_lines=["CLASSIFIED PRACTICE QUESTIONS","& FOUR PREDICTED EXAMS"],
 tagline="Unit-by-unit MCQ and FRQ practice, then four complete exams built for the 2026 format.",
 backtext="Original multiple-choice and free-response questions for all nine units, followed by four full-length predicted examinations. Complete solutions are in Book Three.",
 out_base="APES_Classified_Practice_4_Predicted_Exams",_content=c2,
 legal=["All questions in this book are original works written for Success4Sure Academy. No solutions appear in this book; complete solutions are in Book Three."])
def c3(b):
    md(b,f"{C}/front/b3_intro.md")
    b.heading(1,"Part I — Book One Classroom Example Solutions")
    b.para("Worked solutions to every unsolved classroom example in Book One, organized by unit.",11)
    for n in range(1,10): md(b,f"{C}/book3/SG_U{n}_sol.md",pb=True)
    b.heading(1,"Part II — Book Two Classified Question Solutions")
    b.para("For each unit: MCQ answers and explanations first, then complete FRQ solutions.",11)
    for n in range(1,10): md(b,f"{C}/book3/QB_U{n}_sol.md",pb=True)
    b.heading(1,"Part III — Four Predicted Exam Solutions")
    b.para("For each exam: MCQ answers and explanations first, then complete FRQ solutions.",11)
    for k in range(1,5): md(b,f"{C}/book3/PE{k}_sol.md",pb=True)
BOOKS[3]=dict(short="Complete Solutions",num="Book Three",title_lines=["COMPLETE SOLUTIONS"],
 tagline="Every classroom example, every classified question and every predicted-exam question — fully solved.",
 backtext="Complete solutions for Book One classroom examples, Book Two classified questions, and all four predicted examinations.",
 out_base="APES_Complete_Solutions",_content=c3,
 legal=["This book contains solutions for Books One and Two only. Solutions to the College Board questions in Book Four are printed at the end of Book Four."])
def c4(b):
    md(b,f"{C}/front/b4_intro.md")
    md(b,f"{C}/book4/gen/Part1_questions.md")
    md(b,f"{C}/book4/gen/Part2_solutions.md")
BOOKS[4]=dict(short="College Board Questions & Solutions",num="Book Four",title_lines=["COLLEGE BOARD RELEASED QUESTIONS","& COMPLETE SOLUTIONS","CLASSIFIED BY UNIT"],
 tagline="Released-exam questions sorted by unit, with the verified year on every item and all solutions at the end.",
 backtext="College Board released questions classified by the nine units, MCQ first and FRQ second, with original complete solutions at the end of the book.",
 out_base="APES_College_Board_Questions_And_Solutions",_content=c4,show_ids=False,
 legal=["AP® is a registered trademark of the College Board. This book is independently produced by Success4Sure Academy and is not endorsed by the College Board. Success4Sure Academy is responsible for the classification, organization and original explanations.","Question text and figures from College Board released materials are not reproduced; each entry gives the verified examination year and an original description of the task."])
if __name__=="__main__":
    n=int(sys.argv[1]); out=sys.argv[2] if len(sys.argv)>2 else f"{ROOT}/build/book{n}"
    d,p,b=build_book(BOOKS[n],out); print(d,p)
    from pypdf import PdfReader; print("pages",len(PdfReader(p).pages))
