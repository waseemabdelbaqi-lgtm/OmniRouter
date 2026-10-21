"""Raw CB registers -> Book 4 markdown (questions first, all solutions at end) + internal source register."""
import sys, json,glob,re,collections,csv,os
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
    sys.path.insert(0,"/home/user/OmniRouter/apes_project/tools")
    from structure import CED, CHAPTERS, UNITS as NU, unit_of_chapter
    DEFAULT={1:4,2:4,3:6,4:1,5:7,6:8,7:9,8:9,9:11}
    items=load(); items,dups=dedupe(items)
    LOWCONF={("Intl",n) for n in (12,20,32,50,54,60,67,74)}|{("US",n) for n in (12,55,60)}
    def bad(x):
        if "dup-of-compilation" in x.get("notes",""): return True
        if x["_src"]=="2024.json" and x["type"]=="MCQ":
            m=re.search(r"Q(\d+)\s*$",x["orig_ref"])
            if m and (x["exam"],int(m.group(1))) in LOWCONF: return True
        return False
    inc=[x for x in items if x.get("in_2026_scope",True) and x.get("year") and x.get("unit") in UNITS and not bad(x)]
    exc=[x for x in items if x not in inc]
    for x in inc:
        t=str(x.get("topic",""))
        if t in CED: x["_ch"],x["_sec"]=CED[t][0],CED[t][1]
        else: x["_ch"],x["_sec"]=DEFAULT[x["unit"]],1
    order=lambda x:(x["_sec"],x["year"],x["_src"],x["_i"])
    os.makedirs(f"{R}/content/book4/gen",exist_ok=True)
    counts={}
    for ch in range(1,12):
        qmd=[];smd=[]
        for typ,sec,title,stitle in (("MCQ","A","Multiple-Choice Questions","MCQ Answers and Explanations"),("FRQ","B","Free-Response Questions","FRQ Solutions")):
            xs=sorted([x for x in inc if x["_ch"]==ch and x["type"]==typ],key=order)
            for n,x in enumerate(xs,1): x["_id"]=f"CB-C{ch}-{typ}{n:03d}"; x["_n"]=n
            counts[(ch,typ)]=len(xs)
            qmd.append(f"## Section {sec} — {title}\n")
            smd.append(f"### Section {sec} — {stitle}\n")
            if not xs:
                qmd.append("*No verified released items of this type were available for this chapter in the source collection.*\n")
                smd.append("*No items of this type in this chapter.*\n")
            for x in xs:
                body=x["descriptor"].strip()
                if typ=="FRQ": body+=f" *({FRQT.get(x.get('frqtype','other'),'Free-response')}; {x.get('points',10)} points)*"
                qmd.append(f":::q {x['_id']} | year={x['year']} | chapter={ch}\n{body}\n:::\n")
                sb=clean(x["solution"])
                if typ=="MCQ" and x.get("key") not in (None,"n/a"): sb=f"**Official key: {x['key']}.** "+sb
                elif typ=="MCQ" and x.get("_src")=="2024.json": sb="*(The source copy had no published key; this answer was derived by Success4Sure Academy.)* "+sb
                smd.append(f":::sol {x['_id']} | label=Question {x['_n']} | year={x['year']}\n{sb}\n:::\n")
        open(f"{R}/content/book4/gen/Q_C{ch}.md","w").write("\n".join(qmd))
        open(f"{R}/content/book4/gen/S_C{ch}.md","w").write("\n".join(smd))
    os.makedirs(f"{R}/reports",exist_ok=True)
    with open(f"{R}/reports/book4_source_register.csv","w",newline="") as f:
        w=csv.writer(f); w.writerow(["book4_id","chapter","section","year","exam","type","ced_unit","ced_topic","secondary_units","orig_ref","key","points","status","notes"])
        for x in inc+exc:
            w.writerow([x.get("_id",""),x.get("_ch",""),x.get("_sec",""),x["year"],x["exam"],x["type"],x["unit"],x["topic"],",".join(map(str,x.get("secondary_units",[]))),x["orig_ref"],x.get("key",""),x.get("points",""),"included" if x in inc else "excluded (outside 2026 scope, duplicate or unverifiable)",x.get("notes","")])
    print("included",len(inc),"excluded",len(exc),"dup",len(dups))
    print({ch:(counts[(ch,"MCQ")],counts[(ch,"FRQ")]) for ch in range(1,12)})
if __name__=="__main__": main()
