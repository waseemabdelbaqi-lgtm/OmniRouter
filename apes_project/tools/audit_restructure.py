"""Audit the restructured Book One against the 2026 CED and against the old nine-unit guide."""
import re, sys, glob, json, os, collections
sys.path.insert(0, "/home/user/OmniRouter/apes_project/tools")
from structure import *
R = "/home/user/OmniRouter/apes_project"; C = f"{R}/content"
OUT = f"{R}/reports"; os.makedirs(OUT, exist_ok=True)

ced_text = open(f"{R}/02_curriculum/CED_full.txt").read()
EK = set(re.findall(r"\b([A-Z]{3}-\d\.[A-Z]\.\d+)\b", ced_text)); LO = set(re.findall(r"\b([A-Z]{3}-\d\.[A-Z])\b(?!\.)", ced_text))
chap = {n: open(f"{C}/book1/C{n}.md").read() for n in range(1, 12) if os.path.exists(f"{C}/book1/C{n}.md")}
all_new = "\n".join(chap.values())

def tags(text):
    topics, eks, los = set(), set(), set(); secmap = collections.defaultdict(set)
    cur = None
    for ln in text.splitlines():
        m = re.match(r"^## (\d+)\.(\d+)", ln)
        if m: cur = (int(m.group(1)), int(m.group(2)))
        if ln.startswith("%% CED:"):
            body = ln[len("%% CED:"):]
            parts = [p.strip() for p in body.split("|")]
            for t in re.findall(r"\b(\d\.\d{1,2})\b", parts[0] if parts else ""):
                topics.add(t); secmap[t].add(cur)
            eks |= set(re.findall(r"[A-Z]{3}-\d\.[A-Z]\.\d+", body)); los |= set(re.findall(r"\b[A-Z]{3}-\d\.[A-Z]\b(?!\.)", body))
            # expand ranges like ERT-4.A.1–5
            for m2 in re.finditer(r"([A-Z]{3}-\d\.[A-Z])\.(\d+)\s*[–-]\s*(\d+)", body):
                for k in range(int(m2.group(2)), int(m2.group(3)) + 1): eks.add(f"{m2.group(1)}.{k}")
    return topics, eks, los, secmap
topics, eks, los, secmap = tags(all_new)
rep = ["# Cross-reference map and restructuring audit (academy chapters ↔ 2026 College Board CED)\n"]
# 1 topic mapping
rows = ["| CED topic | Academy chapter.section (planned) | Chapter file tags it? | Sections tagged |", "|---|---|---|---|"]
unplaced = []
for t, (ch, sec, others) in CED.items():
    tagged_in = sorted({s for s in secmap.get(t, set()) if s})
    ok = any(s[0] == ch for s in tagged_in)
    if not ok: unplaced.append(t)
    rows.append(f"| {t} | {ch}.{sec}{(' (+' + ', '.join(str(o) for o in others) + ')') if others else ''} | {'yes' if ok else 'NO'} | {', '.join(f'{a}.{b}' for a, b in tagged_in)} |")
rep += ["## 1. Every CED topic → location in the new structure\n"] + rows
rep.append(f"\nCED topics (99): placed under their planned chapter: {99 - len(unplaced)}; not tagged in the planned chapter: {unplaced}\n")
# 2 EK / LO
miss_ek = sorted(EK - eks); miss_lo = sorted(LO - los)
rep.append(f"## 2. Essential-knowledge and learning-objective codes\n\n- Essential-knowledge codes found in the CED text: {len(EK)}; tagged in Book One sections: {len(EK & eks)}; **not tagged: {len(miss_ek)}** {miss_ek}\n- Learning-objective codes found in the CED text: {len(LO)}; tagged: {len(LO & los)}; **not tagged: {len(miss_lo)}** {miss_lo}\n")
# 3 examples
ids_new = re.findall(r"(?m)^id: (SG-[A-Z0-9-]+)", all_new); cnt = collections.Counter(ids_new)
loc = json.load(open(f"{C}/restructure/example_old_topic.json"))
missing_old = sorted(set(loc) - set(ids_new)); dup = sorted(i for i, c in cnt.items() if c > 1)
rep.append(f"## 3. Classroom examples\n\n- Original examples expected: {len(loc)}; present: {len(set(loc) & set(ids_new))}; missing: {missing_old}\n- Duplicated ids: {dup}\n- New examples added during restructuring: {len([i for i in cnt if i.startswith('SG-C')])}\n- Total examples now: {len(cnt)}\n")
# 4 preservation: bold terms + formula lines of old units
old = "\n".join(open(f"{C}/book1/U{n}.md").read() for n in range(1, 10))
terms = set(t.strip().lower() for t in re.findall(r"\*\*([^*\n]{3,60})\*\*", old))
new_l = all_new.lower()
lost = sorted(t for t in terms if t not in new_l)
rep.append(f"## 4. Content preservation (old nine-unit guide → new chapters)\n\n- Bold key terms in the old guide: {len(terms)}; still present (case-insensitive) in the new guide: {len(terms) - len(lost)} ({100 * (len(terms) - len(lost)) / len(terms):.1f}%).\n- Terms not found verbatim (review: may be reworded, merged or intentionally dropped): {len(lost)}\n")
rep.append("  " + "; ".join(lost[:200]) + ("; …" if len(lost) > 200 else "") + "\n")
fm_old = re.findall(r":::box formula\n(.*?)\n:::", old, re.S); fm_new = all_new.lower()
fm_lost = [f.split("\n")[0][:70] for f in fm_old if f.split("\n")[0][:25].lower() not in fm_new]
rep.append(f"- Old formula boxes: {len(fm_old)}; first line not found in the new guide: {len(fm_lost)} {fm_lost[:15]}\n")
# 5 stale references and figures
stale = []
for n, t in chap.items():
    for m in re.finditer(r"\b(Unit \d|Topic \d\.\d+|Figure \d+\.\d+[a-z]?)\b", t):
        s = m.group(1)
        if s.startswith("Figure"):
            if f"— " in t and not re.search(rf"!\[{re.escape(s)}\b", t): stale.append((n, s))
        else: stale.append((n, s))
rep.append(f"## 5. Possibly stale cross-references inside chapter files\n\n{len(stale)} found (old 'Unit n' / 'Topic x.y' wording or figure numbers that are not captions in the same chapter): {stale[:60]}\n")
open(f"{OUT}/crossref_and_restructuring_audit.md", "w").write("\n".join(rep))
print("\n".join(rep[-12:]))
print("unplaced topics:", unplaced, "| missing EK:", len(miss_ek), "| missing LO:", len(miss_lo), "| missing old examples:", missing_old, "| lost terms:", len(lost), "| stale refs:", len(stale))
