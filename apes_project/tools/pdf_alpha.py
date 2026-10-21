"""Make pale box/table fills translucent in a LibreOffice-made PDF so the diagonal watermark shows through them.

Layer order in the result: page -> watermark (header image) -> translucent tinted panels -> text/formulas/figures -> frame.
Strong fills (maroon header cells, title bands) stay opaque; pale tints are re-drawn at alpha A with a deeper base colour so that
on plain white paper they look the same as the original tint (apparent = A*c' + (1-A)*white = c)."""
import re, sys
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, DictionaryObject, FloatObject, DecodedStreamObject

A = 0.40
TINTS = ["F4E9EA", "FFF6DD", "E8F1F8", "EAF5EC", "FCE9E9", "F2F2F2", "F8F1F2", "FAF3F3", "FFFFFF"]
def rgb(h): return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
TINT_RGB = [rgb(h) for h in TINTS]
RG = re.compile(r"^([\d.]+) ([\d.]+) ([\d.]+) rg$")
def match_tint(c):
    for t in TINT_RGB:
        if all(abs(c[i] - t[i]) < 0.006 for i in range(3)): return t
    return None
def deeper(t):
    if t == (1.0, 1.0, 1.0): return None            # white panels: drop entirely (fully transparent)
    return tuple(min(1.0, max(0.0, (t[i] - (1 - A)) / A)) for i in range(3))

def process_stream(data):
    out = []; in_tint = False
    lines = data.split("\n")
    i = 0
    skip_white_fill = False
    for ln in lines:
        s = ln.strip()
        m = RG.match(s)
        if m:
            c = tuple(float(m.group(k)) for k in (1, 2, 3)); t = match_tint(c)
            if t is not None:
                d = deeper(t)
                if d is None:
                    out.append("/GS0 gs"); out.append(s); skip_white_fill = True; in_tint = True; continue
                out.append("/GSt gs"); out.append("%.5f %.5f %.5f rg" % d); in_tint = True; skip_white_fill = False; continue
            out.append("/GS1 gs"); out.append(s); in_tint = False; skip_white_fill = False; continue
        if re.match(r"^[\d.]+ [\d.]+ [\d.]+ RG$", s) or re.match(r"^[\d.]+ g$", s) or s.endswith(" Do") or s == "BT" or " BT" in s[-4:]:
            if not in_tint or s.endswith(" Do") or s == "BT":
                out.append("/GS1 gs"); in_tint = False
        out.append(ln)
    return "\n".join(out)

def make_translucent(src, dst):
    r = PdfReader(src); w = PdfWriter(clone_from=r)
    for pg in w.pages:
        data = pg.get_contents().get_data().decode("latin1")
        new = process_stream(data)
        st = DecodedStreamObject(); st.set_data(new.encode("latin1"))
        pg[NameObject("/Contents")] = w._add_object(st)
        res = pg["/Resources"]
        gs = res.get("/ExtGState")
        if gs is None:
            gs = DictionaryObject(); res[NameObject("/ExtGState")] = gs
        else: gs = gs.get_object()
        def egs(a):
            d = DictionaryObject(); d[NameObject("/ca")] = FloatObject(a); d[NameObject("/CA")] = FloatObject(a); d[NameObject("/Type")] = NameObject("/ExtGState"); return d
        gs[NameObject("/GSt")] = egs(A); gs[NameObject("/GS1")] = egs(1.0); gs[NameObject("/GS0")] = egs(0.0)
    with open(dst, "wb") as f: w.write(f)

if __name__ == "__main__":
    make_translucent(sys.argv[1], sys.argv[2])
