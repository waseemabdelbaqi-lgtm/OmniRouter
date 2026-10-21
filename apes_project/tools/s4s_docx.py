"""Success4Sure APES book engine: custom-Markdown -> DOCX with the one master page frame."""
import re, os, copy
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml, OxmlElement
from PIL import Image

ROOT = "/home/user/OmniRouter/apes_project"
BRAND = f"{ROOT}/01_brand"
RED, DARK = "7A1424", "4A0D14"
FONT = "Times New Roman"

BOX = {  # kind: (label, fill, edge)
    "objectives": ("LEARNING OBJECTIVES", "F4E9EA", RED),
    "simple":     ("CONCEPT MADE SIMPLE", "FFF6DD", "C99A2E"),
    "define":     ("KEY DEFINITIONS", "E8F1F8", "2F6690"),
    "process":    ("PROCESS & CAUSE-AND-EFFECT", "EAF5EC", "3E7D4F"),
    "formula":    ("FORMULA & MATH SKILL", "F4E9EA", DARK),
    "mistake":    ("COMMON STUDENT MISTAKES", "FCE9E9", "B3261E"),
    "strategy":   ("AP EXAM STRATEGY", "E8F1F8", "2F6690"),
    "apply":      ("REAL-WORLD EXAMPLE", "EAF5EC", "3E7D4F"),
    "summary":    ("QUICK CONCEPT SUMMARY", "F4E9EA", RED),
    "example":    ("CLASSROOM EXAMPLE", "FFFFFF", RED),
    "note":       ("NOTE", "F2F2F2", "6B6B6B"),
}

# ---------------------------------------------------------------- low-level helpers
def set_run_font(run, size=None, bold=None, italic=None, color=None, font=FONT):
    run.font.name = font
    rpr = run._element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts"); rpr.insert(0, rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(a), font)
    if size: run.font.size = Pt(size)
    if bold is not None: run.font.bold = bold
    if italic is not None: run.font.italic = italic
    if color: run.font.color.rgb = RGBColor.from_string(color)

def shade(el_pr, fill):
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
    el_pr.append(shd)

def para_fmt(p, before=0, after=4, line=1.08, align=None, keep_next=False, left=None, first=None, keep_lines=False):
    f = p.paragraph_format
    f.space_before = Pt(before); f.space_after = Pt(after)
    f.line_spacing = line
    if align is not None: p.alignment = align
    if keep_next: f.keep_with_next = True
    if keep_lines: f.keep_together = True
    if left is not None: f.left_indent = Cm(left)
    if first is not None: f.first_line_indent = Cm(first)

def para_border(p, side="bottom", color=RED, sz=8, space=2):
    ppr = p._p.get_or_add_pPr()
    b = ppr.find(qn("w:pBdr"))
    if b is None:
        b = OxmlElement("w:pBdr"); ppr.append(b)
    e = OxmlElement(f"w:{side}"); e.set(qn("w:val"), "single"); e.set(qn("w:sz"), str(sz)); e.set(qn("w:space"), str(space)); e.set(qn("w:color"), color)
    b.append(e)

def para_shade(p, fill):
    shade(p._p.get_or_add_pPr(), fill)

_bm = [100]
def add_bookmark(p, name):
    _bm[0] += 1
    s = OxmlElement("w:bookmarkStart"); s.set(qn("w:id"), str(_bm[0])); s.set(qn("w:name"), name)
    e = OxmlElement("w:bookmarkEnd"); e.set(qn("w:id"), str(_bm[0]))
    p._p.insert(1 if p._p.pPr is not None else 0, s); p._p.append(e)

def add_field(p, instr, size=9, color="444444", bold=False):
    for typ, txt in (("begin", None), (None, instr), ("separate", None), (None, "1"), ("end", None)):
        r = p.add_run(); set_run_font(r, size=size, color=color, bold=bold)
        if typ:
            fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), typ); r._r.append(fc)
        elif txt == instr:
            it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = f" {instr} "; r._r.append(it)
        else:
            t = OxmlElement("w:t"); t.text = txt; r._r.append(t)

def add_hyperlink(p, url, text, size=11, color="1F4E9E", underline=True, bold=False):
    part = p.part
    rid = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    h = OxmlElement("w:hyperlink"); h.set(qn("r:id"), rid)
    r = OxmlElement("w:r"); rpr = OxmlElement("w:rPr")
    rf = OxmlElement("w:rFonts")
    for a in ("w:ascii", "w:hAnsi", "w:cs"): rf.set(qn(a), FONT)
    rpr.append(rf)
    if bold: rpr.append(OxmlElement("w:b"))
    c = OxmlElement("w:color"); c.set(qn("w:val"), color); rpr.append(c)
    sz = OxmlElement("w:sz"); sz.set(qn("w:val"), str(int(size * 2))); rpr.append(sz)
    if underline:
        u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rpr.append(u)
    r.append(rpr); t = OxmlElement("w:t"); t.text = text; t.set(qn("xml:space"), "preserve"); r.append(t)
    h.append(r); p._p.append(h)

def add_internal_link(p, anchor, text, size=10.5, color="000000"):
    h = OxmlElement("w:hyperlink"); h.set(qn("w:anchor"), anchor)
    r = OxmlElement("w:r"); rpr = OxmlElement("w:rPr")
    rf = OxmlElement("w:rFonts")
    for a in ("w:ascii", "w:hAnsi", "w:cs"): rf.set(qn(a), FONT)
    rpr.append(rf)
    c = OxmlElement("w:color"); c.set(qn("w:val"), color); rpr.append(c)
    sz = OxmlElement("w:sz"); sz.set(qn("w:val"), str(int(size * 2))); rpr.append(sz)
    r.append(rpr); t = OxmlElement("w:t"); t.text = text; t.set(qn("xml:space"), "preserve"); r.append(t)
    h.append(r); p._p.append(h)

INLINE = re.compile(r"(\*\*.+?\*\*|\*[^*\s][^*]*?\*)")
def add_inline(p, text, size=11, color=None, bold=False, italic=False):
    for part in INLINE.split(text):
        if not part: continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            r = p.add_run(part[2:-2]); set_run_font(r, size=size, bold=True, italic=italic, color=color)
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            r = p.add_run(part[1:-1]); set_run_font(r, size=size, bold=bold, italic=True, color=color)
        else:
            r = p.add_run(part); set_run_font(r, size=size, bold=bold, italic=italic, color=color)

def cell_borders(cell, **kw):
    tcpr = cell._tc.get_or_add_tcPr()
    b = OxmlElement("w:tcBorders")
    for side in ("top", "left", "bottom", "right"):
        spec = kw.get(side)
        e = OxmlElement(f"w:{side}")
        if spec is None:
            e.set(qn("w:val"), "nil")
        else:
            val, sz, col = spec
            e.set(qn("w:val"), val); e.set(qn("w:sz"), str(sz)); e.set(qn("w:space"), "0"); e.set(qn("w:color"), col)
        b.append(e)
    tcpr.append(b)

def cell_margins(cell, top=60, bottom=60, left=120, right=120):
    tcpr = cell._tc.get_or_add_tcPr()
    m = OxmlElement("w:tcMar")
    for k, v in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        e = OxmlElement(f"w:{k}"); e.set(qn("w:w"), str(v)); e.set(qn("w:type"), "dxa"); m.append(e)
    tcpr.append(m)

def set_cell_fill(cell, fill):
    shade(cell._tc.get_or_add_tcPr(), fill)

def table_fixed(tbl, widths_cm):
    tblpr = tbl._tbl.tblPr
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblpr.append(lay)
    tbl.autofit = False
    for row in tbl.rows:
        for i, c in enumerate(row.cells):
            c.width = Cm(widths_cm[i])

def no_split_row(row):
    trpr = row._tr.get_or_add_trPr(); e = OxmlElement("w:cantSplit"); trpr.append(e)

def repeat_header(row):
    trpr = row._tr.get_or_add_trPr(); e = OxmlElement("w:tblHeader"); trpr.append(e)

# ---------------------------------------------------------------- anchored images (frame ornaments / watermark)
_pid = [5000]
def anchor_picture(par, img_path, width_cm, pos_h, pos_v, behind=True, rot=0):
    """pos_h/pos_v: ('align','center') or ('offset', cm) relative to page."""
    run = par.add_run()
    pic = run.add_picture(img_path, width=Cm(width_cm))
    inline = pic._inline
    cx, cy = inline.extent.cx, inline.extent.cy
    graphic = inline.graphic
    _pid[0] += 1
    def pos(tag, spec):
        kind, val = spec
        rel = "page"
        if kind == "align":
            return f'<wp:{tag} relativeFrom="{rel}"><wp:align>{val}</wp:align></wp:{tag}>'
        return f'<wp:{tag} relativeFrom="{rel}"><wp:posOffset>{int(Cm(val))}</wp:posOffset></wp:{tag}>'
    xml = (f'<wp:anchor {nsdecls("wp","a","pic","r")} distT="0" distB="0" distL="0" distR="0" simplePos="0" '
           f'relativeHeight="{_pid[0]}" behindDoc="{1 if behind else 0}" locked="0" layoutInCell="1" allowOverlap="1">'
           f'<wp:simplePos x="0" y="0"/>{pos("positionH", pos_h)}{pos("positionV", pos_v)}'
           f'<wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:wrapNone/>'
           f'<wp:docPr id="{_pid[0]}" name="frame{_pid[0]}"/><wp:cNvGraphicFramePr/></wp:anchor>')
    anchor = parse_xml(xml)
    anchor.append(graphic)
    inline.getparent().replace(inline, anchor)

def make_corner_png(path):
    """One corner ornament (top-left); rotated for the other corners."""
    S = 300
    from PIL import ImageDraw
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    red, dark = (122, 20, 36, 255), (74, 13, 20, 255)
    d.rectangle([0, 0, S, 22], fill=red); d.rectangle([0, 0, 22, S], fill=red)               # thick L
    d.rectangle([40, 40, S, 48], fill=dark); d.rectangle([40, 40, 48, S], fill=dark)         # thin inner L
    d.polygon([(70, 70), (110, 70), (70, 110)], fill=red)                                     # corner triangle
    d.ellipse([118, 12, 138, 32], fill=red); d.ellipse([12, 118, 32, 138], fill=red)          # dots
    im.save(path)

def build_assets():
    c = f"{BRAND}/corner_tl.png"
    if not os.path.exists(c): make_corner_png(c)
    base = Image.open(c)
    for name, ang in (("tr", -90), ("br", 180), ("bl", 90)):
        p = f"{BRAND}/corner_{name}.png"
        base.rotate(ang).save(p)

# ---------------------------------------------------------------- page frame (identical in every book)
FRAME_SPACE_PT = 20      # distance of border from page edge
def apply_master_frame(section):
    """Double maroon border + 4 corner ornaments + diagonal logo watermark. One definition for all four books."""
    sectpr = section._sectPr
    old = sectpr.find(qn("w:pgBorders"))
    if old is not None: sectpr.remove(old)
    pb = parse_xml(f'<w:pgBorders {nsdecls("w")} w:offsetFrom="page">'
                   + "".join(f'<w:{s} w:val="double" w:sz="12" w:space="{FRAME_SPACE_PT}" w:color="{RED}"/>' for s in ("top", "left", "bottom", "right"))
                   + "</w:pgBorders>")
    # pgBorders must come after pgMar in sectPr
    mar = sectpr.find(qn("w:pgMar")); mar.addnext(pb)
    hdr = section.header; hdr.is_linked_to_previous = False
    p = hdr.paragraphs[0]
    for r in list(p.runs): r._r.getparent().remove(r._r)
    off = FRAME_SPACE_PT / 28.3465 - 0.12   # cm: ornament sits on the border corner
    W, H, o = 21.0, 29.7, 1.05
    anchor_picture(p, f"{BRAND}/watermark.png", 15.5, ("align", "center"), ("align", "center"))
    for nm, (x, y) in {"tl": (off, off), "tr": (W - off - o, off), "bl": (off, H - off - o), "br": (W - off - o, H - off - o)}.items():
        anchor_picture(p, f"{BRAND}/corner_{nm}.png", o, ("offset", x), ("offset", y))

def page_setup(section):
    section.page_width, section.page_height = Cm(21.0), Cm(29.7)
    section.left_margin = section.right_margin = Cm(2.2)
    section.top_margin, section.bottom_margin = Cm(2.4), Cm(2.3)
    section.header_distance, section.footer_distance = Cm(1.2), Cm(1.15)

def clear_style_tabs(p):
    ppr = p._p.get_or_add_pPr()
    tabs = OxmlElement("w:tabs")
    for pos in (4680, 9360):
        t = OxmlElement("w:tab"); t.set(qn("w:val"), "clear"); t.set(qn("w:pos"), str(pos)); tabs.append(t)
    ppr.append(tabs)

def write_running_header(section, left_text, right_text):
    hdr = section.header
    p = hdr.paragraphs[0]
    clear_style_tabs(p)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(16.6), alignment=2)  # right
    r = p.add_run(left_text); set_run_font(r, size=8.5, color=DARK, bold=True)
    r = p.add_run("\t" + right_text); set_run_font(r, size=8.5, color="6B6B6B")
    para_border(p, "bottom", RED, 6, 3)

def write_footer(section, show_numbers=True, text="Success4Sure Academy  |  Prepared by Mr. Waseem Allabadi"):
    ft = section.footer; ft.is_linked_to_previous = False
    p = ft.paragraphs[0]
    clear_style_tabs(p)
    for r in list(p.runs): r._r.getparent().remove(r._r)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(16.6), alignment=2)
    if show_numbers:
        r = p.add_run(text); set_run_font(r, size=8.5, color="6B6B6B")
        r = p.add_run("\tPage "); set_run_font(r, size=8.5, color=DARK, bold=True)
        add_field(p, "PAGE", size=8.5, color=DARK, bold=True)
        para_border(p, "top", RED, 6, 3)

# ---------------------------------------------------------------- document
class Book:
    def __init__(self, short_title, base_dir):
        build_assets()
        self.d = Document()
        self.base = base_dir
        self.short = short_title
        self.headings = []     # (level, text, bookmark)
        self.qcount = {}       # per-section numbering
        self._hn = 0
        st = self.d.styles["Normal"]; st.font.name = FONT; st.font.size = Pt(11)
        st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
        sec = self.d.sections[0]; page_setup(sec)
        self.sec = sec

    # ---- sections
    def new_section(self, header_left=None, header_right="Success4Sure Academy", numbers=True, first=False):
        if not first:
            sec = self.d.add_section(WD_SECTION.NEW_PAGE)
        else:
            sec = self.d.sections[0]
        page_setup(sec)
        apply_master_frame(sec)
        if header_left: write_running_header(sec, header_left, header_right)
        write_footer(sec, numbers)
        self.sec = sec
        return sec

    def pagebreak(self):
        self.d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    # ---- text blocks
    def para(self, text, size=11, align=None, before=0, after=4, color=None, bold=False, italic=False, keep_next=False, left=None, container=None):
        p = (container or self.d).add_paragraph()
        para_fmt(p, before, after, align=align, keep_next=keep_next, left=left)
        add_inline(p, text, size, color, bold, italic)
        return p

    def heading(self, level, text, container=None, pagebreak=None, front=False):
        if front:
            bm = "fm" + str(len(text))
        else:
            self._hn += 1; bm = f"h{self._hn}"
        p = self.d.add_paragraph()
        if level == 1:
            if pagebreak is not False: p.paragraph_format.page_break_before = True
            para_fmt(p, 0, 10, 1.0, keep_next=True)
            para_shade(p, RED)
            r = p.add_run(" " + text); set_run_font(r, size=19, bold=True, color="FFFFFF")
            p.paragraph_format.left_indent = Cm(0.1)
        elif level == 2:
            para_fmt(p, 12, 5, 1.0, keep_next=True)
            r = p.add_run(text); set_run_font(r, size=14.5, bold=True, color=DARK)
            para_border(p, "bottom", RED, 8, 2)
        else:
            para_fmt(p, 8, 3, 1.0, keep_next=True)
            r = p.add_run(text); set_run_font(r, size=12, bold=True, color=RED)
        add_bookmark(p, bm)
        if not front: self.headings.append((level, text, bm))
        if level == 1 or (level == 2 and text.lower().startswith(("section", "part"))):
            self.qcount["n"] = 0
        return p

    def bullets(self, items, container=None, size=11, ordered=False, start=1):
        n = start
        for lvl, txt in items:
            p = (container or self.d).add_paragraph()
            ind = 0.55 + 0.6 * lvl
            para_fmt(p, 0, 2, 1.05, left=ind + 0.45, first=-0.45)
            mark = f"{n}." if ordered else ("•" if lvl == 0 else "–")
            r = p.add_run(mark + "\t"); set_run_font(r, size=size, bold=ordered, color=RED if not ordered else DARK)
            p.paragraph_format.tab_stops.add_tab_stop(Cm(ind + 0.45))
            add_inline(p, txt, size)
            n += 1

    def figure(self, path, caption, width=0.85, container=None):
        full = path if os.path.isabs(path) else os.path.join(self.base, path)
        if not os.path.exists(full):
            self.para(f"[missing figure: {path}]", color="B3261E"); return
        p = (container or self.d).add_paragraph(); para_fmt(p, 4, 1, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER, keep_next=True)
        w_cm = 16.6 * width
        im = Image.open(full)
        max_h = 11.5
        if w_cm * im.height / im.width > max_h: w_cm = max_h * im.width / im.height
        p.add_run().add_picture(full, width=Cm(w_cm))
        c = (container or self.d).add_paragraph(); para_fmt(c, 0, 6, 1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
        add_inline(c, caption, 9, "444444", italic=True)

    def table(self, rows, container=None):
        head, body = rows[0], rows[1:]
        n = len(head)
        tbl = (container or self.d).add_table(rows=1 + len(body), cols=n)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        total = 16.0 if container is None else 15.0
        lens = [max(len(str(r[i])) if i < len(r) else 0 for r in rows) for i in range(n)]
        lens = [min(max(l, 6), 40) for l in lens]; s = sum(lens)
        widths = [max(total * l / s, 1.6) for l in lens]; k = total / sum(widths); widths = [w * k for w in widths]
        tblpr = tbl._tbl.tblPr
        bd = parse_xml(f'<w:tblBorders {nsdecls("w")}>' + "".join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="B8A0A4"/>' for s in ("top", "left", "bottom", "right", "insideH", "insideV")) + "</w:tblBorders>")
        tblpr.append(bd)
        table_fixed(tbl, widths)
        for ri, row in enumerate([head] + body):
            for ci in range(n):
                cell = tbl.rows[ri].cells[ci]
                cell_margins(cell, 40, 40, 80, 80)
                txt = row[ci] if ci < len(row) else ""
                p = cell.paragraphs[0]; para_fmt(p, 0, 0, 1.0)
                if ri == 0:
                    set_cell_fill(cell, RED); add_inline(p, txt, 9.5, "FFFFFF", bold=True)
                else:
                    if ri % 2 == 0: set_cell_fill(cell, "F8F1F2")
                    add_inline(p, txt, 9.5)
            no_split_row(tbl.rows[ri])
        repeat_header(tbl.rows[0])
        sp = (container or self.d).add_paragraph(); para_fmt(sp, 0, 4, 0.6)

    # ---- callout box
    def box(self, kind, lines):
        label, fill, edge = BOX.get(kind, BOX["note"])
        tbl = self.d.add_table(rows=1, cols=1); tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        table_fixed(tbl, [16.5])
        cell = tbl.rows[0].cells[0]
        set_cell_fill(cell, fill); cell_margins(cell, 70, 70, 140, 120)
        cell_borders(cell, left=("single", 36, edge), top=("single", 4, edge), bottom=("single", 4, edge), right=("single", 4, edge))
        first = cell.paragraphs[0]; para_fmt(first, 0, 2, 1.0, keep_next=True)
        r = first.add_run(label); set_run_font(r, size=8.5, bold=True, color=edge)
        content = list(lines)
        qid = None
        if kind == "example" and content and content[0].startswith("id:"):
            qid = content.pop(0)[3:].strip()
            r = first.add_run(f"   {qid}"); set_run_font(r, size=8.5, bold=True, color="6B6B6B")
        self.render_blocks(content, container=cell, size=10.5)
        if kind == "example":
            for _ in range(5):
                p = cell.add_paragraph(); para_fmt(p, 0, 0, 1.0); p.paragraph_format.space_after = Pt(9)
                para_border(p, "bottom", "C9B5B8", 4, 1)
        no_split = False
        sp = self.d.add_paragraph(); para_fmt(sp, 0, 3, 0.5)

    # ---- generic block renderer (also used inside boxes / questions)
    def render_blocks(self, lines, container=None, size=11):
        i = 0
        c = container
        while i < len(lines):
            ln = lines[i]
            s = ln.strip()
            if not s:
                i += 1; continue
            if s.startswith("[[space"):
                n = int(re.findall(r"\d+", s)[0]) if re.findall(r"\d+", s) else 3
                for _ in range(n):
                    p = (c or self.d).add_paragraph(); para_fmt(p, 0, 0, 1.0); p.paragraph_format.space_after = Pt(11)
                i += 1; continue
            if s == "[[pagebreak]]":
                self.pagebreak(); i += 1; continue
            m = re.match(r"!\[(.*?)\]\((.*?)\)(\{w=([\d.]+)\})?", s)
            if m:
                self.figure(m.group(2), m.group(1), float(m.group(4) or 0.85), container=c); i += 1; continue
            if s.startswith("|"):
                rows = []
                while i < len(lines) and lines[i].strip().startswith("|"):
                    t = lines[i].strip().strip("|")
                    cells = [x.strip() for x in t.split("|")]
                    if not all(re.fullmatch(r":?-{2,}:?", x) for x in cells): rows.append(cells)
                    i += 1
                if rows: self.table(rows, container=c)
                continue
            m = re.match(r"^(\s*)([-*•])\s+(.*)", ln)
            m2 = re.match(r"^(\s*)(\d+)[.)]\s+(.*)", ln)
            if m or m2:
                items = []; ordered = bool(m2); start = int(m2.group(2)) if m2 else 1
                while i < len(lines):
                    a = re.match(r"^(\s*)([-*•])\s+(.*)", lines[i]); b = re.match(r"^(\s*)(\d+)[.)]\s+(.*)", lines[i])
                    mm = a or b
                    if not mm or (bool(b) != ordered and not a):
                        break
                    items.append((min(len(mm.group(1)) // 2, 1), mm.group(3))); i += 1
                self.bullets(items, container=c, size=size, ordered=ordered, start=start); continue
            if s.startswith("### "):
                self.heading(3, s[4:]); i += 1; continue
            if s.startswith("## "):
                self.heading(2, s[3:]); i += 1; continue
            if s.startswith("# "):
                self.heading(1, s[2:]); i += 1; continue
            if s.startswith(":::box"):
                kind = s.split()[1] if len(s.split()) > 1 else "note"
                body = []; i += 1
                while i < len(lines) and lines[i].strip() != ":::":
                    body.append(lines[i]); i += 1
                i += 1; self.box(kind, body); continue
            if s.startswith(":::q"):
                head = s[4:].strip(); body = []; i += 1
                while i < len(lines) and lines[i].strip() != ":::":
                    body.append(lines[i]); i += 1
                i += 1; self.question(head, body); continue
            if s.startswith(":::sol"):
                head = s[6:].strip(); body = []; i += 1
                while i < len(lines) and lines[i].strip() != ":::":
                    body.append(lines[i]); i += 1
                i += 1; self.solution(head, body); continue
            # plain paragraph: gather consecutive text lines
            buf = [s]; i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r"^(\s*[-*•]\s|\s*\d+[.)]\s|\|!|#|:::|!\[|\[\[)", lines[i]) and not lines[i].strip().startswith("|"):
                buf.append(lines[i].strip()); i += 1
            p = (c or self.d).add_paragraph(); para_fmt(p, 0, 4, 1.08)
            add_inline(p, " ".join(buf), size)

    # ---- questions & solutions
    def question(self, head, body):
        parts = [x.strip() for x in head.split("|")]
        qid = parts[0]
        meta = dict(x.split("=", 1) for x in parts[1:] if "=" in x)
        key = (qid.split("-")[0] + "-" + (qid.split("-")[1] if qid.count("-") > 1 else "")) if False else qid.rsplit("-", 1)[0] + ("MCQ" if "MCQ" in qid else "FRQ" if "FRQ" in qid else "")
        # numbering restarts per (section prefix) — caller may set self.qreset()
        n = self.qcount.get("n", 0) + 1; self.qcount["n"] = n
        year = meta.get("year")
        t = self.d.add_table(rows=1, cols=1); table_fixed(t, [16.5])
        cell = t.rows[0].cells[0]; cell_margins(cell, 40, 40, 60, 60)
        cell_borders(cell, left=("single", 24, RED));
        p = cell.paragraphs[0]; para_fmt(p, 0, 3, 1.0, keep_next=True)
        r = p.add_run(f"Question {n}"); set_run_font(r, size=11, bold=True, color=RED)
        if year:
            r = p.add_run(f" — {year}"); set_run_font(r, size=11, bold=True, color=DARK)
        r = p.add_run(f"     {qid}" if self.show_ids else ""); set_run_font(r, size=7.5, color="8A8A8A")
        # body: stem lines until options; options rendered tight
        stem, opts = [], []
        for ln in body:
            if re.match(r"^\s*[A-D]\)\s", ln): opts.append(ln.strip())
            else: stem.append(ln)
        self.render_blocks(stem, container=cell, size=10.5)
        for o in opts:
            p = cell.add_paragraph(); para_fmt(p, 0, 1.5, 1.04, left=0.9, first=-0.55)
            p.paragraph_format.tab_stops.add_tab_stop(Cm(0.9))
            m = re.match(r"([A-D])\)\s*(.*)", o)
            r = p.add_run(m.group(1) + ".\t"); set_run_font(r, size=10.5, bold=True, color=DARK)
            add_inline(p, m.group(2), 10.5)
        if "FRQ" in qid and self.show_ids:
            for _ in range(2):
                pp = cell.add_paragraph(); para_fmt(pp, 0, 0, 1.0)
        sp = self.d.add_paragraph(); para_fmt(sp, 0, 3, 0.5)

    show_ids = True

    def solution(self, head, body):
        parts = [x.strip() for x in head.split("|")]
        qid = parts[0]
        meta = dict(x.split("=", 1) for x in parts[1:] if "=" in x)
        p = self.d.add_paragraph(); para_fmt(p, 3, 1, 1.0, keep_next=True)
        lab = meta.get("label") or qid
        r = p.add_run(lab); set_run_font(r, size=10.5, bold=True, color=RED)
        if meta.get("year"):
            r = p.add_run(f" — {meta['year']}"); set_run_font(r, size=10.5, bold=True, color=DARK)
        if meta.get("label") and self.show_ids:
            r = p.add_run(f"   {qid}"); set_run_font(r, size=7.5, color="8A8A8A")
        self.render_blocks(body, size=10.5)

    def reset_numbering(self): self.qcount["n"] = 0

    # ---- markdown file ingestion
    def add_markdown(self, path):
        lines = open(path, encoding="utf-8").read().splitlines()
        self.base = os.path.dirname(path)
        self.render_blocks(lines)

    def save(self, path): self.d.save(path)
