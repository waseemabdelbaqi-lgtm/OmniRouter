"""Assemble one Success4Sure APES book: cover, front matter, TOC (2-pass), content, contact page, back cover."""
import sys, os, re, subprocess, json, secrets, shutil
sys.path.insert(0, "/home/user/OmniRouter/apes_project/tools")
from s4s_docx import *
import segno

LINKS = {
    "web": ("SUCCESS4SURE ACADEMY WEBSITE", "https://www.success4sureacademy.com", "www.success4sureacademy.com"),
    "waseem": ("MR. WASEEM ALLABADI — INSTAGRAM", "https://www.instagram.com/waseemabed19/", "instagram.com/waseemabed19"),
    "academy": ("SUCCESS4SURE ACADEMY — INSTAGRAM", "https://www.instagram.com/success4surejo/", "instagram.com/success4surejo"),
}
COPYRIGHT = "© 2026 Success4Sure Academy | All Rights Reserved | Unauthorized Printing, Copying, Reproduction & Distribution Prohibited."
OUT = f"{ROOT}/build"

def make_qrs():
    d = f"{OUT}/qr"; os.makedirs(d, exist_ok=True)
    for k, (_, url, _) in LINKS.items():
        segno.make(url, error="m").save(f"{d}/{k}.png", scale=12, border=2, dark=DARK_HEX)
    return d
DARK_HEX = "#4A0D14"

def _centered(b, text, size, bold=False, color=None, before=0, after=4, italic=False):
    return b.para(text, size=size, bold=bold, color=color, align=WD_ALIGN_PARAGRAPH.CENTER, before=before, after=after, italic=italic)

def _logo(b, width_cm):
    p = b.d.add_paragraph(); para_fmt(p, 0, 0, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
    p.add_run().add_picture(f"{BRAND}/logo_on_white.png", width=Cm(width_cm))

def cover(b, cfg):
    b.d.add_paragraph().paragraph_format.space_after = Pt(18)
    _logo(b, 8.2)
    _centered(b, "Success4Sure Academy", 12, color="6B6B6B", before=4, after=14)
    t = b.d.add_table(rows=1, cols=1); table_fixed(t, [16.5]); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]; set_cell_fill(c, RED); cell_margins(c, 260, 260, 200, 200)
    p = c.paragraphs[0]; para_fmt(p, 0, 6, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
    r = p.add_run(cfg["num"].upper()); set_run_font(r, size=14, bold=True, color="F2D7DA")
    p = c.add_paragraph(); para_fmt(p, 0, 4, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
    r = p.add_run("AP ENVIRONMENTAL SCIENCE"); set_run_font(r, size=31, bold=True, color="FFFFFF")
    for line in cfg["title_lines"]:
        p = c.add_paragraph(); para_fmt(p, 0, 2, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
        r = p.add_run(line); set_run_font(r, size=17, bold=True, color="FFFFFF")
    sp = b.d.add_paragraph(); para_fmt(sp, 0, 6)
    art = f"{OUT}/cover_art.png"
    if os.path.exists(art):
        p = b.d.add_paragraph(); para_fmt(p, 2, 4, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
        p.add_run().add_picture(art, width=Cm(16.0))
    _centered(b, cfg["tagline"], 12.5, italic=True, color=DARK, before=4, after=8)
    _centered(b, "Prepared by Mr. Waseem Allabadi", 15, bold=True, color=DARK, before=6, after=2)
    _centered(b, "Published by Success4Sure Academy", 12.5, color="333333", after=2)
    _centered(b, "2026–2027 Edition  |  Aligned to the 2026 Course and Exam Description", 10.5, color="6B6B6B", before=2)

def title_page(b, cfg):
    for _ in range(3): b.d.add_paragraph()
    _logo(b, 6.5)
    _centered(b, "AP ENVIRONMENTAL SCIENCE", 24, bold=True, color=RED, before=26, after=4)
    for line in cfg["title_lines"]:
        _centered(b, line, 17, bold=True, color=DARK, after=2)
    p = b.d.add_paragraph(); para_fmt(p, 10, 10); para_border(p, "bottom", RED, 12, 1)
    _centered(b, cfg["tagline"], 12, italic=True, after=26)
    _centered(b, "Prepared by", 11, color="6B6B6B", after=0)
    _centered(b, "Mr. Waseem Allabadi", 19, bold=True, color=DARK, after=18)
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
    b.para("Prepared by Mr. Waseem Allabadi. Published by Success4Sure Academy. First edition, 2026–2027.", 10, after=6)

def contents_page(b, toc_entries, pages):
    b.heading(1, "Table of Contents", pagebreak=True, front=True)
    for (lvl, text, bm) in toc_entries:
        p = b.d.add_paragraph()
        para_fmt(p, 5 if lvl == 1 else 0, 1.5, 1.0, left=0 if lvl == 1 else 0.6)
        p.paragraph_format.tab_stops.add_tab_stop(Cm(16.5), alignment=2, leader=1)  # dots
        add_internal_link(p, bm, text, size=11 if lvl == 1 else 10, color=DARK if lvl == 1 else "000000")
        if lvl == 1:
            for r in p.runs: pass
        r = p.add_run("\t" + str(pages.get(bm, "")))
        set_run_font(r, size=11 if lvl == 1 else 10, bold=(lvl == 1), color=DARK if lvl == 1 else "000000")

def contact_page(b):
    b.heading(1, "Connect with Success4Sure Academy", front=True)
    b.para("Scan a code or click a link to reach the academy and the author.", 11, align=WD_ALIGN_PARAGRAPH.CENTER, after=14)
    qd = make_qrs()
    t = b.d.add_table(rows=3, cols=1); table_fixed(t, [16.4]); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, k in enumerate(("web", "waseem", "academy")):
        label, url, shown = LINKS[k]
        c = t.rows[i].cells[0]; cell_margins(c, 120, 120, 200, 200)
        set_cell_fill(c, "F8F1F2"); cell_borders(c, left=("single", 36, RED), top=("single", 4, "D9C4C7"), bottom=("single", 4, "D9C4C7"), right=("single", 4, "D9C4C7"))
        inner = c.add_table(rows=1, cols=2); table_fixed(inner, [10.6, 4.4])
        L, R = inner.rows[0].cells
        p = L.paragraphs[0]; para_fmt(p, 14, 6, 1.0)
        r = p.add_run(label); set_run_font(r, size=11, bold=True, color=RED)
        p = L.add_paragraph(); para_fmt(p, 0, 0, 1.0)
        add_hyperlink(p, url, url, size=11.5)
        pr = R.paragraphs[0]; para_fmt(pr, 0, 0, 1.0, align=WD_ALIGN_PARAGRAPH.RIGHT)
        pr.add_run().add_picture(f"{qd}/{k}.png", width=Cm(3.6))
        c.paragraphs[0]._p.getparent().remove(c.paragraphs[0]._p)
        sp = c.add_paragraph(); para_fmt(sp, 0, 0, 0.5)
        sp2 = b.d.add_paragraph(); para_fmt(sp2, 0, 8, 0.5)
    b.para("Success4Sure Academy — International academic programs, exam preparation and professional training.", 10.5, align=WD_ALIGN_PARAGRAPH.CENTER, before=10, color="555555")

def back_cover(b, cfg):
    b.d.add_paragraph().paragraph_format.space_after = Pt(60)
    _logo(b, 9.5)
    _centered(b, "Success4Sure Academy", 17, bold=True, color=RED, before=10, after=26)
    t = b.d.add_table(rows=1, cols=1); table_fixed(t, [15.5]); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]; set_cell_fill(c, RED); cell_margins(c, 220, 220, 220, 220)
    p = c.paragraphs[0]; para_fmt(p, 0, 4, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
    r = p.add_run("AP ENVIRONMENTAL SCIENCE"); set_run_font(r, size=20, bold=True, color="FFFFFF")
    for line in cfg["title_lines"]:
        p = c.add_paragraph(); para_fmt(p, 0, 2, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
        r = p.add_run(line); set_run_font(r, size=13, bold=True, color="F2D7DA")
    _centered(b, cfg["backtext"], 11.5, italic=True, color="333333", before=24, after=24)
    _centered(b, "Prepared by Mr. Waseem Allabadi", 13, bold=True, color=DARK, after=4)
    _centered(b, "www.success4sureacademy.com", 11.5, color=RED, after=4)
    _centered(b, COPYRIGHT, 8.5, color="6B6B6B", before=40)

def find_pages(pdf, entries, first_content_page):
    """Locate each heading's PDF page (1-based) by sequential text search."""
    from pypdf import PdfReader
    rd = PdfReader(pdf); texts = [re.sub(r"\s+", " ", (pg.extract_text() or "")) for pg in rd.pages]
    out = {}; cur = first_content_page - 1
    for lvl, text, bm in entries:
        key = re.sub(r"\s+", " ", text).strip()[:60]
        found = None
        for i in range(cur, len(texts)):
            if key in texts[i]:
                found = i; break
        if found is None:
            continue
        out[bm] = found + 1; cur = found
    return out, len(texts)

def assemble(cfg, toc_pages=None):
    b = Book(cfg["short"], ROOT)
    b.show_ids = cfg.get("show_ids", True)
    b.new_section(None, numbers=False, first=True)         # cover (frame + watermark, no footer)
    cover(b, cfg)
    b.new_section("AP Environmental Science  |  " + cfg["short"], numbers=True)
    title_page(b, cfg)
    copyright_page(b, cfg)
    # reserve TOC: we need the heading list before writing it -> two-step: build content first in a scratch Book
    scratch_entries = cfg["_entries"]
    contents_page(b, [(l, t, bm) for (l, t, bm) in scratch_entries if l <= cfg.get("toc_depth", 2)], toc_pages or {})
    b.reset_numbering()
    cfg["_content"](b)
    contact_page(b)
    b.new_section(None, numbers=False)
    back_cover(b, cfg)
    return b

def dry_entries(cfg):
    """Run the content renderer on a throwaway book to learn heading names/bookmarks in order."""
    b = Book(cfg["short"], ROOT); b.show_ids = cfg.get("show_ids", True)
    b.new_section(None, numbers=False, first=True)
    cfg["_content"](b)
    return list(b.headings)

def to_pdf(docx, outdir):
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", outdir, docx], check=True, capture_output=True, timeout=1500)
    return os.path.join(outdir, os.path.basename(docx)[:-5] + ".pdf")

def build_book(cfg, outdir):
    os.makedirs(outdir, exist_ok=True)
    base = cfg["out_base"]
    # headings in content only need ordering: content bookmarks h1.. are numbered by order of creation, so the TOC
    # entries (which add one heading themselves: "Table of Contents", "Copyright") would shift numbering. Use a
    # stable approach: pass 1 builds without page numbers, content headings get their own bookmark names.
    cfg["_entries"] = []
    b1 = None
    # pass 0: learn entries from content only
    ent = dry_entries(cfg)
    cfg["_entries"] = ent
    docx = f"{outdir}/{base}.docx"
    b = assemble(cfg, {})
    b.save(docx); pdf = to_pdf(docx, outdir)
    # find pages: TOC entries refer to bookmarks created in dry run (h1..hn); in the real doc the numbering is offset
    pages, total = find_pages(pdf, ent, 5)
    mapping = pages
    b = assemble(cfg, mapping)
    b.save(docx); pdf = to_pdf(docx, outdir)
    return docx, pdf, b

def protect_pdf(src, dst):
    from pypdf import PdfReader, PdfWriter
    from pypdf.constants import UserAccessPermissions as P
    r = PdfReader(src); w = PdfWriter(clone_from=r)
    w.add_metadata({"/Title": r.metadata.title if r.metadata and r.metadata.title else "AP Environmental Science", "/Author": "Mr. Waseem Allabadi", "/Publisher": "Success4Sure Academy"})
    w.encrypt(user_password="", owner_password=secrets.token_urlsafe(24), algorithm="AES-256", permissions_flag=P(0))
    with open(dst, "wb") as f: w.write(f)
