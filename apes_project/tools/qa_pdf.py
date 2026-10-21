"""Per-page QA of a rendered book PDF: frame present, watermark image present, blank pages, content near frame."""
import sys, subprocess, json, os, re, glob, shutil, tempfile
import numpy as np
from PIL import Image
from pypdf import PdfReader

DPI = 50
FRAME_PT = 20.0   # distance of the frame from the page edge (points)

def render(pdf, outdir):
    os.makedirs(outdir, exist_ok=True)
    subprocess.run(["pdftoppm", "-r", str(DPI), "-gray", "-png", pdf, f"{outdir}/p"], check=True, capture_output=True)
    return sorted(glob.glob(f"{outdir}/p-*.png"))

def wm_pages(pdf):
    out = subprocess.run(["pdfimages", "-list", pdf], capture_output=True, text=True).stdout.splitlines()[2:]
    pages = {}
    for ln in out:
        c = ln.split()
        if len(c) < 5: continue
        pg, w, h = int(c[0]), int(c[3]), int(c[4])
        # watermark image: tall (portrait, rotated) large raster of aspect ≈ 0.72
        if h > 600 and 0.6 < w / h < 0.85:
            pages[pg] = pages.get(pg, 0) + 1
    return pages

def analyse(pdf, tmp):
    rd = PdfReader(pdf); n = len(rd.pages)
    imgs = render(pdf, tmp)
    wm = wm_pages(pdf)
    d = int(round(FRAME_PT / 72 * DPI))     # frame offset in px
    rep = {"pdf": os.path.basename(pdf), "pages": n, "no_watermark": [], "no_frame": [], "blank": [], "near_frame": [], "page_size": None}
    box = rd.pages[0].mediabox; rep["page_size"] = [round(float(box.width), 1), round(float(box.height), 1)]
    for i, f in enumerate(imgs, 1):
        a = np.asarray(Image.open(f).convert("L")).astype(float)
        H, W = a.shape
        # frame: dark pixels along each side at offset d..d+3
        band = lambda arr: (arr < 170).mean()
        top = a[d:d + 4, 120:W - 120].min(axis=0); bot = a[H - d - 4:H - d, 120:W - 120].min(axis=0)
        lef = a[120:H - 120, d:d + 4].min(axis=1); rig = a[120:H - 120, W - d - 4:W - d].min(axis=1)
        ok = all((s < 190).mean() > 0.9 for s in (top, bot, lef, rig))
        if not ok: rep["no_frame"].append(i)
        if i not in wm: rep["no_watermark"].append(i)
        inner = a[d + 8:H - d - 8, d + 8:W - d - 8]
        ink = (inner < 200).mean()
        if ink < 0.004: rep["blank"].append(i)
        # content hugging the frame: dark pixels within 3px inside frame edge (ignoring corners)
        m = 5
        edge = np.concatenate([inner[:m, 40:-40].ravel(), inner[-m:, 40:-40].ravel(), inner[40:-40, :m].ravel(), inner[40:-40, -m:].ravel()])
        if (edge < 120).mean() > 0.01: rep["near_frame"].append(i)
    return rep

if __name__ == "__main__":
    pdf = sys.argv[1]; tmp = tempfile.mkdtemp(prefix="qa_")
    try:
        rep = analyse(pdf, tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print(json.dumps(rep))
