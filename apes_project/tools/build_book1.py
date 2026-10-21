import sys,os,glob
sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from s4s_book import *
C=f"{ROOT}/content/book1"
def content(b):
    for n in range(1,10):
        p=f"{C}/U{n}.md"
        if os.path.exists(p): b.add_markdown(p)
    for extra in sorted(glob.glob(f"{C}/Z_*.md")): b.add_markdown(extra)
cfg=dict(short="Complete Study Guide",num="Book One",title_lines=["COMPLETE STUDY GUIDE","All Nine Units • Skills • Unsolved Classroom Examples"],
 tagline="Clear explanations, original diagrams and the math skills every AP Environmental Science student needs.",
 backtext="Every unit of the 2026 curriculum explained simply, accurately and completely — with original diagrams and unsolved classroom examples whose full solutions are in Book Three.",
 out_base="APES_Complete_Study_Guide",_content=content,
 legal=["Book One teaches all nine units of AP Environmental Science. Classroom examples are intentionally unsolved; complete worked solutions are provided in Book Three of this collection."])
if __name__=="__main__":
    out=sys.argv[1] if len(sys.argv)>1 else f"{ROOT}/build/book1"
    d,p,b=build_book(cfg,out); print(d,p)
    from pypdf import PdfReader; print("pages",len(PdfReader(p).pages))
