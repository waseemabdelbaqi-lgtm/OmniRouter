"""Assemble one Success4Sure APES book: cover, front matter, TOC (2-pass), chapters, contact page, back cover; PDF export with translucent panels."""
import sys, os, re, subprocess, json, secrets, shutil
sys.path.insert(0, "/home/user/OmniRouter/apes_project/tools")
import s4s_docx as D
from s4s_docx import *
import segno
from PIL import Image, ImageDraw

LINKS = {
    "web": ("SUCCESS4SURE ACADEMY WEBSITE", "https://www.success4sureacademy.com", "www.success4sureacademy.com"),
    "waseem": ("MR. WASEEM ALLABADI — INSTAGRAM", "https://www.instagram.com/waseemabed19/", "instagram.com/waseemabed19"),
    "academy": ("SUCCESS4SURE ACADEMY — INSTAGRAM", "https://www.instagram.com/success4surejo/", "instagram.com/success4surejo"),
}
COPYRIGHT = "© 2026 Success4Sure Academy | All Rights Reserved | Unauthorized Printing, Copying, Reproduction & Distribution Prohibited."
OUT = f"{ROOT}/build"
ART = f"{OUT}/art"
SERIES = [("BOOK ONE", "Complete Study Guide", "Seven units, eleven chapters, clear explanations and unsolved classroom examples."),
          ("BOOK TWO", "Classified Practice & Four Predicted Exams", "MCQs then FRQs for every chapter, plus four full-length exams."),
          ("BOOK THREE", "Complete Solutions", "Worked solutions for Books One and Two and all four predicted exams."),
          ("BOOK FOUR", "College Board Questions & Solutions", "Released-exam questions classified by chapter, with solutions at the end.")]
DARK_HEX = "#4A0D14"

# ---------------------------------------------------------------- assets
def icon_globe(path, col=(122, 20, 36, 255)):
    S = 360; im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im); w = 16
    d.ellipse([20, 20, S - 20, S - 20], outline=col, width=w)
    d.ellipse([110, 20, S - 110, S - 20], outline=col, width=w // 2 + 2)
    d.line([S // 2, 20, S // 2, S - 20], fill=col, width=w // 2 + 2)
    d.line([20, S // 2, S - 20, S // 2], fill=col, width=w // 2 + 2)
    d.arc([40, 80, S - 40, 280], 0, 180, fill=col, width=w // 2 + 2); d.arc([40, 80, S - 40, 280], 180, 360, fill=col, width=w // 2 + 2)
    im.save(path)

def icon_instagram(path, col=(122, 20, 36, 255)):
    S = 360; im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([24, 24, S - 24, S - 24], radius=90, outline=col, width=22)
    d.ellipse([100, 100, S - 100, S - 100], outline=col, width=22)
    d.ellipse([S - 118, 70, S - 78, 110], fill=col)
    im.save(path)

def make_qrs():
    d = f"{OUT}/qr"; os.makedirs(d, exist_ok=True)
    for k, (_, url, _) in LINKS.items():
        segno.make(url, error="m").save(f"{d}/{k}.png", scale=12, border=2, dark=DARK_HEX)
    icon_globe(f"{d}/icon_web.png"); icon_instagram(f"{d}/icon_ig.png")
    return d

def _centered(b, text, size, bold=False, color=None, before=0, after=4, italic=False):
    return b.para(text, size=size, bold=bold, color=color, align=WD_ALIGN_PARAGRAPH.CENTER, before=before, after=after, italic=italic)

def _logo(b, width_cm):
    p = b.d.add_paragraph(); para_fmt(p, 0, 0, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
    p.add_run().add_picture(f"{BRAND}/logo_on_white.png", width=Cm(width_cm))

def _spaced(text): return "  ".join(text)

# ---------------------------------------------------------------- covers
def cover(b, cfg):
    sp = b.d.add_paragraph(); para_fmt(sp, 0, 6, 0.5)
    _logo(b, 6.4)
    p = b.d.add_paragraph(); para_fmt(p, 6, 6, 1.0); para_border(p, "bottom", RED, 12, 4)
    _centered(b, _spaced("AP® ENVIRONMENTAL SCIENCE"), 11, bold=True, color=RED, before=4, after=6)
    t = b.d.add_table(rows=1, cols=1); table_fixed(t, [16.4]); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]; set_cell_fill(c, RED); cell_margins(c, 230, 230, 240, 240)
    cell_borders(c, bottom=("single", 30, DARK))
    p = c.paragraphs[0]; para_fmt(p, 0, 8, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
    r = p.add_run(f"  {cfg['num']}  "); set_run_font(r, size=12, bold=True, color=RED); run_shade(r, "FFFFFF")
    for line in cfg["title_lines"]:
        p = c.add_paragraph(); para_fmt(p, 0, 2, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
        r = p.add_run(line); set_run_font(r, size=cfg.get("title_size", 27), bold=True, color="FFFFFF")
    p = c.add_paragraph(); para_fmt(p, 6, 0, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
    r = p.add_run(cfg["subtitle"]); set_run_font(r, size=11.5, italic=True, color="F2D7DA")
    sp = b.d.add_paragraph(); para_fmt(sp, 0, 6, 0.5)
    art = f"{ART}/{cfg['hero']}.png"
    if os.path.exists(art):
        ht = b.d.add_table(rows=1, cols=1); table_fixed(ht, [16.4]); ht.alignment = WD_TABLE_ALIGNMENT.CENTER
        hc = ht.rows[0].cells[0]; cell_margins(hc, 0, 0, 0, 0)
        cell_borders(hc, top=("single", 12, RED), left=("single", 12, RED), bottom=("single", 12, RED), right=("single", 12, RED))
        hp = hc.paragraphs[0]; para_fmt(hp, 0, 0, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
        hp.add_run().add_picture(art, width=Cm(16.2))
    sp = b.d.add_paragraph(); para_fmt(sp, 0, 5, 0.5)
    ft = b.d.add_table(rows=1, cols=3); table_fixed(ft, [5.46, 5.46, 5.48]); ft.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, txt in enumerate(cfg["features"]):
        cell = ft.rows[0].cells[i]; cell_margins(cell, 70, 70, 60, 60)
        cell_borders(cell, left=("single", 6, RED) if i else None, top=("single", 6, RED), bottom=("single", 6, RED), right=("single", 6, RED) if i == 2 else None)
        p = cell.paragraphs[0]; para_fmt(p, 0, 0, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
        r = p.add_run(txt); set_run_font(r, size=9.5, bold=True, color=DARK)
    _centered(b, "Prepared by", 10, color="6B6B6B", before=10, after=0)
    _centered(b, "Mr. Waseem Allabadi", 19, bold=True, color=DARK, after=1)
    _centered(b, "Published by Success4Sure Academy", 11.5, color="333333", after=1)
    _centered(b, "2026–2027 Edition  ·  www.success4sureacademy.com", 9.5, color=RED, before=2)

def title_page(b, cfg):
    for _ in range(3): b.d.add_paragraph()
    _logo(b, 7.0)
    _centered(b, "AP® ENVIRONMENTAL SCIENCE", 23, bold=True, color=RED, before=30, after=4)
    for line in cfg["title_lines"]:
        _centered(b, line.title() if line.isupper() else line, 17, bold=True, color=DARK, after=2)
    p = b.d.add_paragraph(); para_fmt(p, 10, 10); para_border(p, "bottom", RED, 12, 1)
    _centered(b, cfg["subtitle"], 12, italic=True, after=26)
    _centered(b, "Prepared by", 11, color="6B6B6B", after=0)
    _centered(b, "Mr. Waseem Allabadi", 20, bold=True, color=DARK, after=18)
    _centered(b, "Published by", 11, color="6B6B6B", after=0)
    _centered(b, "Success4Sure Academy", 16, bold=True, color=RED, after=18)
    _centered(b, "2026–2027 Edition", 11.5, color="333333")

def copyright_page(b, cfg):
    b.heading(1, "Copyright & Important Information", front=True)
    b.para(COPYRIGHT, 10.5, bold=True, color=DARK, after=8)
    for t in cfg.get("legal", []):
        b.para(t, 10, after=6)
    b.para("AP® and Advanced Placement® are registered trademarks of the College Board. This publication was produced independently by Success4Sure Academy and is not endorsed by, affiliated with, or sponsored by the College Board.", 10, after=6)
    b.para("All explanations, diagrams, examples, practice questions and solutions identified as original were written for Success4Sure Academy. Unless a page states otherwise, no College Board question text or figure is reproduced in this book.", 10, after=6)
    b.para("The chapter order follows the Success4Sure Academy textbook structure (7 units, 11 chapters). The complete content of the official AP Environmental Science Course and Exam Description is covered; an internal cross-reference map links every College Board topic to its chapter.", 10, after=6)
    b.para("Prepared by Mr. Waseem Allabadi. Published by Success4Sure Academy. First edition, 2026–2027.", 10, after=6)

def contents_page(b, entries, pages, depth):
    b.heading(1, "Table of Contents", pagebreak=True, front=True)
    for (lvl, text, bm, *_rest) in entries:
        if lvl > depth: continue
        p = b.d.add_paragraph()
        if lvl == 1:
            para_fmt(p, 9, 2, 1.0, left=0); para_border(p, "top", RED, 6, 3)
            size, col, bold = 11.5, RED, True
        elif lvl == 2:
            para_fmt(p, 3, 1, 1.0, left=0.3); size, col, bold = 10.5, DARK, True
        else:
            para_fmt(p, 0, 0.5, 1.0, left=1.0); size, col, bold = 9, "222222", False
        p.paragraph_format.tab_stops.add_tab_stop(Cm(16.5), alignment=2, leader=1 if lvl > 1 else 0)
        add_internal_link(p, bm, text, size=size, color=col)
        for r in p.runs: pass
        r = p.add_run("\t" + str(pages.get(bm, ""))); set_run_font(r, size=size, bold=bold, color=col)

def contact_page(b):
    b.heading(1, "Connect with Success4Sure Academy", front=True)
    b.para("Scan a code or click a link to reach the academy and the author.", 11, align=WD_ALIGN_PARAGRAPH.CENTER, after=14)
    qd = make_qrs()
    t = b.d.add_table(rows=3, cols=1); table_fixed(t, [16.4]); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, k in enumerate(("web", "waseem", "academy")):
        label, url, shown = LINKS[k]
        c = t.rows[i].cells[0]; cell_margins(c, 120, 120, 200, 200)
        set_cell_fill(c, "F8F1F2"); cell_borders(c, left=("single", 36, RED), top=("single", 4, "D9C4C7"), bottom=("single", 4, "D9C4C7"), right=("single", 4, "D9C4C7"))
        inner = c.add_table(rows=1, cols=3); table_fixed(inner, [1.8, 10.9, 3.3])
        I, L, R = inner.rows[0].cells
        ip = I.paragraphs[0]; para_fmt(ip, 8, 0, 1.0)
        ip.add_run().add_picture(f"{qd}/{'icon_web' if k == 'web' else 'icon_ig'}.png", width=Cm(1.4))
        p = L.paragraphs[0]; para_fmt(p, 12, 4, 1.0)
        r = p.add_run(label); set_run_font(r, size=10.5, bold=True, color=RED)
        p = L.add_paragraph(); para_fmt(p, 0, 0, 1.0)
        add_hyperlink(p, url, url, size=10.5)
        pr = R.paragraphs[0]; para_fmt(pr, 0, 0, 1.0, align=WD_ALIGN_PARAGRAPH.RIGHT)
        pr.add_run().add_picture(f"{qd}/{k}.png", width=Cm(3.1))
        c.paragraphs[0]._p.getparent().remove(c.paragraphs[0]._p)
        sp = c.add_paragraph(); para_fmt(sp, 0, 0, 0.5)
        sp2 = b.d.add_paragraph(); para_fmt(sp2, 0, 8, 0.5)
    b.para("Success4Sure Academy — international academic programs, exam preparation and professional training.", 10.5, align=WD_ALIGN_PARAGRAPH.CENTER, before=10, color="555555")

def back_cover(b, cfg):
    sp = b.d.add_paragraph(); para_fmt(sp, 0, 14, 0.5)
    _logo(b, 7.4)
    _centered(b, _spaced("AP® ENVIRONMENTAL SCIENCE SERIES"), 10.5, bold=True, color=RED, before=6, after=10)
    t = b.d.add_table(rows=1, cols=1); table_fixed(t, [16.0]); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]; set_cell_fill(c, RED); cell_margins(c, 200, 200, 220, 220); cell_borders(c, bottom=("single", 24, DARK))
    p = c.paragraphs[0]; para_fmt(p, 0, 3, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
    r = p.add_run(cfg["num"]); set_run_font(r, size=11, bold=True, color="F2D7DA")
    for line in cfg["title_lines"]:
        p = c.add_paragraph(); para_fmt(p, 0, 1, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
        r = p.add_run(line); set_run_font(r, size=17, bold=True, color="FFFFFF")
    _centered(b, cfg["backtext"], 11, italic=True, color="333333", before=14, after=8)
    for bl in cfg.get("bullets", []):
        p = b.d.add_paragraph(); para_fmt(p, 0, 3, 1.05, left=1.6, first=-0.5)
        r = p.add_run("■  "); set_run_font(r, size=8, color=RED)
        add_inline(p, bl, 10.5)
    sp = b.d.add_paragraph(); para_fmt(sp, 0, 4, 0.5)
    st = b.d.add_table(rows=len(SERIES), cols=2); table_fixed(st, [3.4, 12.6]); st.alignment = WD_TABLE_ALIGNMENT.CENTER
    me = cfg["num"].upper()
    for i, (n, ttl, desc) in enumerate(SERIES):
        a, bcell = st.rows[i].cells
        cur = (n == me)
        cell_margins(a, 50, 50, 80, 60); cell_margins(bcell, 50, 50, 100, 60)
        cell_borders(a, top=("single", 4, "D9C4C7"), bottom=("single", 4, "D9C4C7")); cell_borders(bcell, top=("single", 4, "D9C4C7"), bottom=("single", 4, "D9C4C7"))
        if cur: set_cell_fill(a, RED)
        p = a.paragraphs[0]; para_fmt(p, 0, 0, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
        r = p.add_run(n); set_run_font(r, size=8.5, bold=True, color="FFFFFF" if cur else RED)
        p = bcell.paragraphs[0]; para_fmt(p, 0, 0, 1.0)
        r = p.add_run(ttl); set_run_font(r, size=9.5, bold=True, color=DARK)
        r = p.add_run("  —  " + desc); set_run_font(r, size=8.5, color="444444")
    sp = b.d.add_paragraph(); para_fmt(sp, 0, 8, 0.5)
    qd = make_qrs()
    bt = b.d.add_table(rows=1, cols=2); table_fixed(bt, [4.0, 12.0]); bt.alignment = WD_TABLE_ALIGNMENT.CENTER
    q, tx = bt.rows[0].cells
    qp = q.paragraphs[0]; para_fmt(qp, 0, 0, 1.0); qp.add_run().add_picture(f"{qd}/web.png", width=Cm(3.2))
    cell_margins(tx, 60, 60, 160, 60)
    p = tx.paragraphs[0]; para_fmt(p, 10, 2, 1.0)
    r = p.add_run("Prepared by Mr. Waseem Allabadi"); set_run_font(r, size=13, bold=True, color=DARK)
    p = tx.add_paragraph(); para_fmt(p, 0, 2, 1.0); r = p.add_run("Published by Success4Sure Academy"); set_run_font(r, size=10.5, color="333333")
    p = tx.add_paragraph(); para_fmt(p, 0, 0, 1.0); add_hyperlink(p, "https://www.success4sureacademy.com", "www.success4sureacademy.com", size=10.5)
    _centered(b, COPYRIGHT, 7.5, color="6B6B6B", before=10)

# ---------------------------------------------------------------- page finding via PDF text
def find_pages(pdf, entries, start_page=1):
    """entries: (level, text, bm, find) ; find = None | ('re', pattern). Sequential search from the last found page."""
    from pypdf import PdfReader
    rd = PdfReader(pdf)
    texts = [re.sub(r"\s+", " ", (pg.extract_text() or "")) for pg in rd.pages]
    # content starts at the first page that is not front matter: first 'IN THIS UNIT' / 'CHAPTER' banner or first heading
    out = {}; cur = start_page - 1
    for ent in entries:
        lvl, text, bm = ent[0], ent[1], ent[2]
        find = ent[3] if len(ent) > 3 else None
        pat = re.compile(find[1]) if find else re.compile(re.escape(re.sub(r"\s+", " ", text).strip()[:60]))
        found = None
        for i in range(cur, len(texts)):
            if pat.search(texts[i]): found = i; break
        if found is None: continue
        out[bm] = found + 1; cur = found
    return out, len(texts)

def first_content_page(pdf):
    from pypdf import PdfReader
    rd = PdfReader(pdf)
    for i, pg in enumerate(rd.pages):
        t = re.sub(r"\s+", " ", pg.extract_text() or "")
        if "Table of Contents" in t: toc0 = i
    # content begins after the last contents page: first page after toc0 that has no dotted leaders
    for i in range(toc0 + 1, len(rd.pages)):
        t = rd.pages[i].extract_text() or ""
        if "....." not in t and "Table of Contents" not in t: return i + 1
    return toc0 + 2

# ---------------------------------------------------------------- assembly
def assemble(cfg, toc_pages, fills=True):
    D.FILLS = fills
    b = Book(cfg["short"], ROOT)
    b.show_ids = cfg.get("show_ids", True)
    b.practice_info = cfg.get("practice_info", {})
    b.new_section(None, numbers=False, first=True)         # cover (frame + watermark, no footer)
    cover(b, cfg)
    b.new_section("AP Environmental Science  |  " + cfg["short"], numbers=True)
    title_page(b, cfg)
    copyright_page(b, cfg)
    contents_page(b, cfg["_entries"], toc_pages or {}, cfg.get("toc_depth", 2))
    b.reset_numbering()
    cfg["_content"](b)
    b.new_section("AP Environmental Science  |  " + cfg["short"], numbers=True)
    contact_page(b)
    b.new_section(None, numbers=False)
    back_cover(b, cfg)
    return b

def dry_entries(cfg):
    b = Book(cfg["short"], ROOT); b.show_ids = cfg.get("show_ids", True); b.practice_info = cfg.get("practice_info", {})
    b.new_section(None, numbers=False, first=True)
    cfg["_content"](b)
    return list(b.headings)

def to_pdf(docx, outdir):
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", outdir, docx], check=True, capture_output=True, timeout=2400)
    return os.path.join(outdir, os.path.basename(docx)[:-5] + ".pdf")

def build_book(cfg, outdir):
    from pdf_alpha import make_translucent
    os.makedirs(outdir, exist_ok=True)
    base = cfg["out_base"]
    ent = dry_entries(cfg); cfg["_entries"] = ent
    tmp = f"{outdir}/_tmp"; os.makedirs(tmp, exist_ok=True)
    docx_fill = f"{tmp}/{base}.docx"
    b = assemble(cfg, {}, fills=True); b.save(docx_fill); pdf = to_pdf(docx_fill, tmp)
    start = first_content_page(pdf)
    pages, total = find_pages(pdf, ent, start)
    b = assemble(cfg, pages, fills=True); b.save(docx_fill); pdf = to_pdf(docx_fill, tmp)
    final_pdf = f"{outdir}/{base}.pdf"
    make_translucent(pdf, final_pdf)
    docx_final = f"{outdir}/{base}.docx"
    b2 = assemble(cfg, pages, fills=False); b2.save(docx_final)
    D.FILLS = True
    return docx_final, final_pdf, b2

def protect_pdf(src, dst):
    from pypdf import PdfReader, PdfWriter
    from pypdf.constants import UserAccessPermissions as P
    r = PdfReader(src); w = PdfWriter(clone_from=r)
    w.add_metadata({"/Title": r.metadata.title if r.metadata and r.metadata.title else "AP Environmental Science", "/Author": "Mr. Waseem Allabadi", "/Publisher": "Success4Sure Academy"})
    w.encrypt(user_password="", owner_password=secrets.token_urlsafe(24), algorithm="AES-256", permissions_flag=P(0))
    with open(dst, "wb") as f: w.write(f)
