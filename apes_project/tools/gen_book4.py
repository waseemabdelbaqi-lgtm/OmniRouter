"""Raw CB registers -> Book 4 markdown (questions first, all solutions at end) + internal source register."""
import json,glob,re,collections,csv,os
R="/home/user/OmniRouter/apes_project"
UNITS={1:"The Living World: Ecosystems",2:"The Living World: Biodiversity",3:"Populations",4:"Earth Systems and Resources",5:"Land and Water Use",6:"Energy Resources and Consumption",7:"Atmospheric Pollution",8:"Aquatic and Terrestrial Pollution",9:"Global Change"}
FRQT={"design":"Design an investigation","data":"Analyze and interpret quantitative data","calc":"Analyze an environmental problem doing calculations","other":"Free-response"}
def load():
    items=[]
    for f in sorted(glob.glob(f"{R}/content/book4/raw/*.json")):
        for i,x in enumerate(json.load(open(f))):
            x["_src"]=os.path.basename(f); x["_i"]=i; items.append(x)
    return items
def dedupe(items):
    seen={}; out=[]; dups=[]
    for x in items:
        k=(x["year"],x["type"],re.sub(r"\W+","",x["descriptor"].lower())[:60])
        if k in seen: dups.append((x["_src"],x["orig_ref"],seen[k])); continue
        seen[k]=x["orig_ref"]; out.append(x)
    return out,dups
def clean(t):
    t=re.sub(r"\s+(\*\*\([a-z]\)(?:\([ivx]+\))?)",r"\n\n\1",t.strip())
    t=re.sub(r"^\s*\n","",t)
    return re.sub(r"\n{3,}","\n\n",t)
def main():
    items=load(); items,dups=dedupe(items)
    inc=[x for x in items if x.get("in_2026_scope",True) and x.get("year") and x.get("unit") in UNITS]
    exc=[x for x in items if x not in inc]
    # stable order: unit, type, year, source order
    order=lambda x:(x["year"],x["_src"],x["_i"])
    qmd=[];smd=[];reg=[]
    qmd.append("[[pagebreak]]") if False else None
    counts={}
    for u in range(1,10):
        for typ in ("MCQ","FRQ"):
            xs=sorted([x for x in inc if x["unit"]==u and x["type"]==typ],key=order)
            for n,x in enumerate(xs,1): x["_id"]=f"CB-U{u}-{typ}{n:03d}"; x["_n"]=n
            counts[(u,typ)]=len(xs)
    # Part I questions
    qmd.append("# Part I — Classified Questions\n")
    qmd.append(":::box note\nEvery entry below corresponds to a question from a College Board released AP Environmental Science examination. To protect College Board copyright, the question text and figures are not reproduced: each entry gives the verified examination year and an original description of the task. Use the official released exam or free-response materials from College Board (apcentral.collegeboard.org) alongside this book. Original solutions to every entry are in Part II at the end of this book.\n:::\n")
    for u in range(1,10):
        qmd.append(f"# Unit {u} — {UNITS[u]}\n")
        for typ,sec,title in (("MCQ","A","Multiple-Choice Questions"),("FRQ","B","Free-Response Questions")):
            xs=sorted([x for x in inc if x["unit"]==u and x["type"]==typ],key=order)
            qmd.append(f"## Section {sec} — {title}\n")
            if not xs: qmd.append("*No verified released items of this type were available for this unit in the source collection.*\n")
            for x in xs:
                head=f":::q {x['_id']} | year={x['year']} | unit={u} | topic={x['topic']}"
                body=x["descriptor"].strip()
                if typ=="FRQ":
                    body+=f" *({FRQT.get(x.get('frqtype','other'),'Free-response')}; {x.get('points',10)} points)*"
                qmd.append(head+"\n"+body+"\n:::\n")
    # Part II
    smd.append("# Part II — Complete Solutions\n")
    smd.append(":::box note\nSolutions are written by Success4Sure Academy. For multiple-choice items, the official answer key letter refers to the choices printed in the original exam (older exams used five choices, A–E; the 2026 exam uses four). Free-response solutions show complete reasoning and the scoring ideas.\n:::\n")
    for u in range(1,10):
        smd.append(f"## Unit {u} — {UNITS[u]}\n")
        for typ,sec,title in (("MCQ","A","MCQ Answers and Explanations"),("FRQ","B","FRQ Solutions")):
            xs=sorted([x for x in inc if x["unit"]==u and x["type"]==typ],key=order)
            smd.append(f"### Section {sec} — {title}\n")
            for x in xs:
                label=f"Question {x['_n']}"
                body=clean(x["solution"])
                if typ=="MCQ" and x.get("key") not in (None,"n/a"):
                    body=f"**Official key: {x['key']}.** "+body
                smd.append(f":::sol {x['_id']} | label={label} | year={x['year']}\n{body}\n:::\n")
    os.makedirs(f"{R}/content/book4/gen",exist_ok=True)
    open(f"{R}/content/book4/gen/Part1_questions.md","w").write("\n".join(qmd))
    open(f"{R}/content/book4/gen/Part2_solutions.md","w").write("\n".join(smd))
    os.makedirs(f"{R}/reports",exist_ok=True)
    with open(f"{R}/reports/book4_source_register.csv","w",newline="") as f:
        w=csv.writer(f); w.writerow(["book4_id","year","exam","type","unit","topic","secondary_units","orig_ref","key","points","status","notes"])
        for x in inc+exc:
            w.writerow([x.get("_id",""),x["year"],x["exam"],x["type"],x["unit"],x["topic"],",".join(map(str,x.get("secondary_units",[]))),x["orig_ref"],x.get("key",""),x.get("points",""),"included" if x in inc else "excluded (outside 2026 scope or unverifiable)",x.get("notes","")])
    print("included",len(inc),"excluded",len(exc),"dup",len(dups))
    for u in range(1,10): print(u,counts[(u,"MCQ")],counts[(u,"FRQ")])
if __name__=="__main__": main()
