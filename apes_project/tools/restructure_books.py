"""Re-sort the verified Book 2 questions / Book 3 solutions into the academy's 11 chapters and prepare per-chapter files."""
import re, os, sys, json, glob, collections
sys.path.insert(0, "/home/user/OmniRouter/apes_project/tools")
from structure import *
R = "/home/user/OmniRouter/apes_project"
C = f"{R}/content"
UNIT_DEFAULT_CH = {1: 4, 2: 4, 3: 6, 4: 1, 5: 7, 6: 8, 7: 9, 8: 9, 9: 11}

def parse_blocks(text, kind):
    """Return list of (id, header_meta_str, body_text) for ':::q' or ':::sol' blocks."""
    out = []; lines = text.splitlines(); i = 0
    while i < len(lines):
        m = re.match(rf"^:::{kind} (\S+)\s*(\|.*)?$", lines[i])
        if m:
            j = i + 1
            while j < len(lines) and lines[j].strip() != ":::": j += 1
            out.append((m.group(1), (m.group(2) or "").strip(" |"), "\n".join(lines[i + 1:j]), "\n".join(lines[i:j + 1])))
            i = j + 1
        else: i += 1
    return out

def meta_of(h):
    d = {}
    for part in h.split("|"):
        if "=" in part:
            k, v = part.split("=", 1); d[k.strip()] = v.strip()
    return d

def load_questions():
    qs = {}
    for f in sorted(glob.glob(f"{C}/book2/U?.md")):
        for qid, h, body, raw in parse_blocks(open(f).read(), "q"):
            m = meta_of(h); topic = m.get("topic", ""); unit = int(m.get("unit", "0") or 0)
            if topic in CED: ch, sec = CED[topic][0], CED[topic][1]
            else: ch, sec = UNIT_DEFAULT_CH.get(unit, 4), 1
            qs[qid] = dict(raw=raw, ch=ch, sec=sec, unit=unit, topic=topic, diff=int(m.get("diff", "2") or 2), src=os.path.basename(f), new=False, kind="FRQ" if "FRQ" in qid else "MCQ")
    for f in sorted(glob.glob(f"{C}/book2/N_C*.md")):
        for qid, h, body, raw in parse_blocks(open(f).read(), "q"):
            m = meta_of(h)
            qs[qid] = dict(raw=raw, ch=int(m["chapter"]), sec=int(m.get("sec", "1")), unit=int(m.get("unit", "0") or 0), topic=m.get("topic", "ext"), diff=int(m.get("diff", "2") or 2), src=os.path.basename(f), new=True, kind="FRQ" if "FRQ" in qid else "MCQ")
    return qs

def load_solutions():
    sols = {}
    for f in sorted(glob.glob(f"{C}/book3/QB_U?_sol.md")) + sorted(glob.glob(f"{C}/book3/QB_C*_sol.md")):
        for qid, h, body, raw in parse_blocks(open(f).read(), "sol"): sols[qid] = raw
    return sols

def load_sg():
    sols = {}
    for f in sorted(glob.glob(f"{C}/book3/SG_U?_sol.md")) + sorted(glob.glob(f"{C}/book3/SG_C*_sol.md")):
        for qid, h, body, raw in parse_blocks(open(f).read(), "sol"): sols[qid] = raw
    return sols

def main():
    qs = load_questions(); sols = load_solutions(); sg = load_sg()
    os.makedirs(f"{C}/book3/gen", exist_ok=True)
    info = {}; classification = {}
    missing_sol = [q for q in qs if q not in sols]
    if missing_sol: print("WARNING questions without solution:", missing_sol[:10], len(missing_sol))
    for ch in range(1, 12):
        title, secs = CHAPTERS[ch]
        mcq = sorted([q for q, v in qs.items() if v["ch"] == ch and v["kind"] == "MCQ"], key=lambda q: (qs[q]["sec"], qs[q]["diff"], q))
        frq = sorted([q for q, v in qs.items() if v["ch"] == ch and v["kind"] == "FRQ"], key=lambda q: (qs[q]["sec"], qs[q]["diff"], q))
        u = unit_of_chapter(ch)
        topics = sorted({f"{qs[q]['sec']}" for q in mcq + frq}, key=lambda x: int(x))
        note = (f":::box note\n**Chapter {ch} — {title}.** {len(mcq)} multiple-choice questions (Section A) and {len(frq)} free-response questions (Section B) "
                f"classified under Unit {UNITS[u][0].split()[-1]} of the academy structure. Questions are ordered by section of the chapter and then by difficulty. "
                f"Complete solutions are in Book Three, Part II, Chapter {ch}.\n:::\n")
        body = [f"# Chapter {ch} — {title}", "", note, "## Section A — Multiple-Choice Questions", ""]
        body += [qs[q]["raw"] + "\n" for q in mcq]
        body += ["## Section B — Free-Response Questions", ""]
        body += [qs[q]["raw"] + "\n" for q in frq] if frq else ["*No free-response questions are classified under this chapter; see the neighbouring chapters and the predicted exams for free-response practice.*", ""]
        open(f"{C}/book2/C{ch}.md", "w").write("\n".join(body))
        # solutions (Book 3 Part II)
        sb = [f"## Chapter {ch} — {title}", "", "### Section A — MCQ Answers and Explanations", ""]
        sb += [sols.get(q, f":::sol {q}\n(solution missing)\n:::") + "\n" for q in mcq]
        sb += ["### Section B — FRQ Solutions", ""]
        sb += [sols.get(q, f":::sol {q}\n(solution missing)\n:::") + "\n" for q in frq] if frq else ["*No free-response questions in this chapter.*", ""]
        open(f"{C}/book3/gen/QB_C{ch}_sol.md", "w").write("\n".join(sb))
        # Book One examples (order of appearance in the guide) -> Part I
        p = f"{C}/book1/C{ch}.md"
        ids = re.findall(r"(?m)^id: (SG-[A-Z0-9-]+)", open(p).read()) if os.path.exists(p) else []
        sg_blocks = [sg.get(i, f":::sol {i}\n(solution missing)\n:::") + "\n" for i in ids]
        open(f"{C}/book3/gen/SG_C{ch}_sol.md", "w").write("\n".join([f"## Chapter {ch} — {title}", ""] + (sg_blocks or ["*No classroom examples in this chapter.*", ""])))
        info[ch] = dict(examples=ids, mcq=len(mcq), frq=len(frq), sg_missing=[i for i in ids if i not in sg])
        for q in mcq + frq: classification[q] = dict(chapter=ch, section=qs[q]["sec"], ced_unit=qs[q]["unit"], ced_topic=qs[q]["topic"], new=qs[q]["new"])
    json.dump(info, open(f"{C}/restructure/practice_info.json", "w"), indent=1)
    json.dump(classification, open(f"{C}/restructure/question_classification.json", "w"), indent=1)
    tot = sum(v["mcq"] + v["frq"] for v in info.values())
    print("questions placed:", tot, "of", len(qs), "| per chapter (MCQ/FRQ):", {k: (v["mcq"], v["frq"]) for k, v in info.items()})
    print("examples:", sum(len(v["examples"]) for v in info.values()), "| missing SG solutions:", {k: v["sg_missing"] for k, v in info.items() if v["sg_missing"]})

if __name__ == "__main__":
    main()
