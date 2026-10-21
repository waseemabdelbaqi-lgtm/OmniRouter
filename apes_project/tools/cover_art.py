"""Original vector-style environmental illustrations for covers and unit openers (matplotlib)."""
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle, Ellipse, Wedge, FancyArrowPatch, PathPatch
from matplotlib.path import Path

OUT = "/home/user/OmniRouter/apes_project/build/art"
os.makedirs(OUT, exist_ok=True)
CREAM, ROSE, SUN = "#FBF3F1", "#EBC3C8", "#C9566A"
HILL = ["#E8C9CE", "#C9929F", "#9C4256", "#6E1A2D", "#46101C"]
GREEN, GREEN2, WATER, WATER2, SNOW, GREY = "#3F7F55", "#2D6143", "#7FA9C9", "#B5CFE3", "#FFFFFF", "#7A7A7A"
STRATA = ["#4B3326", "#7A5236", "#A9794A", "#C9A46C", "#8A8F96", "#5E6670"]

def canvas(w, h, sky_top="#FCF7F5", sky_bot=ROSE):
    fig = plt.figure(figsize=(w, h)); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 100); ax.set_ylim(0, 100 * h / w); ax.axis("off")
    g = np.linspace(0, 1, 256)[:, None]
    top = np.array(matplotlib.colors.to_rgb(sky_top)); bot = np.array(matplotlib.colors.to_rgb(sky_bot))
    img = (top * (1 - g) + bot * g)[:, None, :].repeat(2, axis=1)
    ax.imshow(img, extent=[0, 100, 0, 100 * h / w], origin="upper", aspect="auto", zorder=0)
    return fig, ax

def ridge(ax, base, amp, color, seed, n=14, z=2, x0=0, x1=100, rough=0.35, floor=0):
    rng = np.random.default_rng(seed)
    xs = np.linspace(x0, x1, 400)
    y = np.zeros_like(xs)
    for k in range(1, n):
        y += rng.normal(0, 1) / k * np.sin(2 * np.pi * k * xs / (x1 - x0) * 0.5 + rng.uniform(0, 6.28))
    y = base + amp * y / max(np.abs(y).max(), 1e-6) * (1 - rough) + amp * rough * 0.15 * rng.normal(0, 1, len(xs)).cumsum() / 30
    ax.fill_between(xs, floor, y, color=color, zorder=z, lw=0)
    return xs, y

def peaks(ax, specs, color, snow=None, z=3):
    for cx, w, h, base in specs:
        ax.add_patch(Polygon([(cx - w / 2, base), (cx, base + h), (cx + w / 2, base)], color=color, zorder=z, lw=0))
        if snow:
            sh = h * 0.28
            ax.add_patch(Polygon([(cx - w / 2 * 0.28, base + h - sh), (cx, base + h), (cx + w / 2 * 0.28, base + h - sh), (cx + w * 0.07, base + h - sh * 0.7), (cx, base + h - sh * 1.05), (cx - w * 0.07, base + h - sh * 0.7)], color=snow, zorder=z + 0.1, lw=0))

def sun(ax, x, y, r, color=SUN, halo=True, z=1):
    if halo:
        for k, a in ((2.3, 0.10), (1.7, 0.16), (1.3, 0.24)):
            ax.add_patch(Circle((x, y), r * k, color=color, alpha=a, zorder=z, lw=0))
    ax.add_patch(Circle((x, y), r, color=color, zorder=z + 0.1, lw=0))

def cloud(ax, x, y, s=1.0, color="white", alpha=0.85, z=1.5):
    for dx, dy, r in ((0, 0, 3.2), (3.2, 0.8, 3.8), (6.6, 0, 3.0), (3.2, -0.6, 3.0)):
        ax.add_patch(Ellipse((x + dx * s, y + dy * s), r * 2 * s, r * 1.1 * s, color=color, alpha=alpha, zorder=z, lw=0))

def pine(ax, x, y, h, color=GREEN, z=4):
    for k in range(3):
        w = h * (0.34 - 0.07 * k); yy = y + h * (0.22 + 0.27 * k)
        ax.add_patch(Polygon([(x - w, yy), (x, yy + h * 0.42), (x + w, yy)], color=color, zorder=z, lw=0))
    ax.add_patch(Rectangle((x - h * 0.03, y), h * 0.06, h * 0.25, color="#4B2E2A", zorder=z - 0.1, lw=0))

def broadleaf(ax, x, y, h, color=GREEN2, z=4):
    ax.add_patch(Rectangle((x - h * 0.04, y), h * 0.08, h * 0.45, color="#4B2E2A", zorder=z - 0.1, lw=0))
    for dx, dy, r in ((0, 0.62, 0.3), (-0.2, 0.5, 0.22), (0.2, 0.5, 0.22), (0, 0.8, 0.2)):
        ax.add_patch(Circle((x + dx * h, y + dy * h), r * h, color=color, zorder=z, lw=0))

def turbine(ax, x, y, h, color="#FFFFFF", z=5, ang=20, lw=None):
    lw = lw or max(0.6, h * 0.05)
    ax.plot([x, x], [y, y + h], color=color, lw=lw, zorder=z, solid_capstyle="round")
    cx, cy = x, y + h
    for a in (ang, ang + 120, ang + 240):
        r = np.deg2rad(a)
        ax.plot([cx, cx + h * 0.5 * np.cos(r)], [cy, cy + h * 0.5 * np.sin(r)], color=color, lw=lw * 0.8, zorder=z, solid_capstyle="round")
    ax.add_patch(Circle((cx, cy), h * 0.035, color=color, zorder=z + 0.1))

def river(ax, pts, w0, w1, color=WATER, z=3.5):
    pts = np.array(pts); n = len(pts)
    left = []; right = []
    for i in range(n):
        d = pts[min(i + 1, n - 1)] - pts[max(i - 1, 0)]; nrm = np.array([-d[1], d[0]]) / (np.linalg.norm(d) + 1e-9)
        w = w0 + (w1 - w0) * i / (n - 1)
        left.append(pts[i] + nrm * w / 2); right.append(pts[i] - nrm * w / 2)
    ax.add_patch(Polygon(left + right[::-1], color=color, zorder=z, lw=0))

def waves(ax, y0, y1, color, alpha=0.5, n=9, z=3, seed=0):
    rng = np.random.default_rng(seed)
    for k in range(n):
        y = y0 + (y1 - y0) * k / (n - 1); xs = np.linspace(0, 100, 300)
        ax.plot(xs, y + 0.35 * np.sin(xs * (0.35 + 0.05 * k) + rng.uniform(0, 6)), color=color, alpha=alpha, lw=0.8, zorder=z)

def strata_block(ax, y_top, y_bot, seed=1):
    """Cutaway Earth strata under the landscape."""
    rng = np.random.default_rng(seed); bands = len(STRATA); hh = (y_top - y_bot) / bands
    xs = np.linspace(0, 100, 200)
    for i, c in enumerate(STRATA):
        top = y_top - hh * i + 0.6 * np.sin(xs / 9 + i) ; bot = y_top - hh * (i + 1) + 0.6 * np.sin(xs / 9 + i + 1)
        ax.fill_between(xs, bot, top, color=c, zorder=6, lw=0)
    ax.add_patch(Polygon([(62, y_bot), (68, y_bot + 2.2 * hh), (74, y_bot)], color="#C8452D", zorder=6.5, lw=0))

def save(fig, name, dpi=240):
    fig.savefig(f"{OUT}/{name}.png", dpi=dpi, facecolor="white"); plt.close(fig)

# ------------------------------------------------------------------ four book heroes (16.4 x 9.6 cm ≈ 1.71:1)
W, H = 8.2, 4.8
def hero1():   # Earth systems — mountains, forest, river, wind, cutaway strata
    fig, ax = canvas(W, H); top = 100 * H / W
    sun(ax, 72, 40, 7.5); cloud(ax, 14, 50, 1.0); cloud(ax, 44, 55, 0.8); cloud(ax, 80, 52, 0.7)
    ridge(ax, 33, 7, HILL[0], 3, z=2); peaks(ax, [(30, 38, 22, 24), (58, 44, 28, 24), (84, 36, 20, 24)], HILL[1], snow="white", z=2.5)
    ridge(ax, 27, 4.5, HILL[2], 7, z=3); ridge(ax, 22, 3.5, HILL[3], 11, z=3.3)
    for x in np.arange(4, 98, 3.4): pine(ax, x + (x * 7) % 1.5, 20 + (x * 3) % 2, 6 + (x * 5) % 3, color=GREEN if x % 7 < 3.5 else GREEN2, z=4)
    river(ax, [(35, 18.5), (42, 21), (48, 22.5), (60, 21), (70, 23.5), (82, 23)], 1.2, 3.4, z=3.6)
    for x, h in ((10, 24), (20, 19), (91, 22)): turbine(ax, x, 21, h * 0.55, "white", z=5, ang=18 + x)
    strata_block(ax, 18.2, 2.0)
    ax.add_patch(Rectangle((0, 18.2), 100, 0.5, color="#2B1A14", zorder=6.8, lw=0))
    ax.set_ylim(0, top); save(fig, "hero1")

def hero2():   # Practice — coast, offshore turbines and a data trend
    fig, ax = canvas(W, H, "#FDF8F6", "#EFC9CD"); top = 100 * H / W
    sun(ax, 50, 32, 8, SUN)
    ax.add_patch(Rectangle((0, 0), 100, 30, color="#8CB0CE", zorder=2, lw=0))
    ax.add_patch(Rectangle((0, 18), 100, 12, color="#6C97BA", zorder=2.1, lw=0))
    ax.add_patch(Rectangle((0, 0), 100, 18, color="#4C7DA3", zorder=2.2, lw=0))
    for k in range(7):
        ax.add_patch(Rectangle((44 + k * 0.5, 21.5 - k * 3.0), 12 - k, 0.7 + 0.1 * k, color=SUN, alpha=0.45 - 0.05 * k, zorder=2.5, lw=0))
    waves(ax, 3, 28, "white", 0.35, 12)
    for x, h, y in ((10, 22, 30), (24, 17, 30), (38, 13, 30), (66, 13, 30), (79, 17, 30), (92, 22, 30)): turbine(ax, x, y, h * 0.62, "#FFFFFF", z=5, ang=10 + x * 1.7)
    ridge(ax, 31.2, 0.8, HILL[1], 5, z=2.3, floor=29.5)
    xs = np.linspace(6, 94, 9); ys = np.array([42, 44, 43, 47, 49.5, 49, 53, 55.5, 57.5])
    ax.plot(xs, ys, color="white", lw=2.0, zorder=6, solid_capstyle="round"); ax.scatter(xs, ys, s=22, color=SUN, edgecolor="white", zorder=7, lw=1)
    for x in xs: ax.plot([x, x], [38.2, 39.6], color="white", lw=0.8, zorder=6, alpha=0.7)
    ax.plot([6, 94], [38.2, 38.2], color="white", lw=1, zorder=6, alpha=0.7)
    # sailboat
    ax.add_patch(Polygon([(18, 11), (30, 11), (27, 8.5), (21, 8.5)], color="#2F2A33", zorder=6))
    ax.add_patch(Polygon([(24, 12), (24, 24), (31, 12)], color="white", zorder=6)); ax.add_patch(Polygon([(23, 12), (23, 21), (18, 12)], color="#F4D7DA", zorder=6))
    ax.set_ylim(0, top); save(fig, "hero2")

def hero3():   # Solutions — forest, lake and cycle arrows
    fig, ax = canvas(W, H, "#FCF7F4", "#F1D2D2"); top = 100 * H / W
    sun(ax, 50, 38, 5.5, SUN, z=1)
    for r, a in ((11.5, 0.75),):
        for k in range(3):
            a0 = 20 + k * 120
            ax.add_patch(FancyArrowPatch((50 + r * np.cos(np.deg2rad(a0)), 38 + r * np.sin(np.deg2rad(a0))), (50 + r * np.cos(np.deg2rad(a0 + 85)), 38 + r * np.sin(np.deg2rad(a0 + 85))), connectionstyle="arc3,rad=0.45", arrowstyle="-|>", mutation_scale=16, color="#7A1424", lw=2.2, zorder=3, alpha=a))
    peaks(ax, [(18, 40, 26, 22), (82, 44, 30, 22), (50, 56, 18, 22)], HILL[1], snow="white", z=2)
    ridge(ax, 24, 4, HILL[2], 21, z=3); ridge(ax, 18, 3, HILL[3], 4, z=3.3)
    ax.add_patch(Ellipse((50, 13), 46, 8, color=WATER, zorder=4, lw=0)); ax.add_patch(Ellipse((50, 13), 34, 5, color=WATER2, zorder=4.1, lw=0, alpha=0.7))
    for x in np.arange(2, 30, 3.2): pine(ax, x, 12 + (x * 3) % 2, 8 + (x * 7) % 3, color=GREEN2 if int(x) % 2 else GREEN, z=5)
    for x in np.arange(72, 99, 3.4): broadleaf(ax, x, 12 + (x * 3) % 2, 8 + (x * 5) % 3, color=GREEN if int(x) % 2 else GREEN2, z=5)
    for x in (34, 44, 56, 66): ax.plot([x - 2, x + 2], [13 + (x % 3) * 0.3] * 2, color="white", lw=0.8, alpha=0.8, zorder=4.5)
    ax.add_patch(Rectangle((0, 0), 100, 8, color=HILL[4], zorder=5.5, lw=0)); ax.add_patch(Rectangle((0, 8), 100, 0.4, color="#2B1A14", zorder=6))
    ax.set_ylim(0, top); save(fig, "hero3")

def hero4():   # College Board — glacier peaks, ice, atmosphere bands
    fig, ax = canvas(W, H, "#F4F7FB", "#F2D5D8"); top = 100 * H / W
    for k, (c, a) in enumerate((("#9FBBD6", 0.35), ("#C9D8E9", 0.35), ("#EBCBD0", 0.3))):
        ax.add_patch(Rectangle((0, 38 + k * 4.2), 100, 4.2, color=c, alpha=a, zorder=0.5, lw=0))
    sun(ax, 22, 42, 6, SUN)
    peaks(ax, [(30, 50, 34, 20), (60, 58, 40, 20), (88, 44, 30, 20), (6, 36, 24, 20)], "#5E7691", snow="white", z=2)
    peaks(ax, [(46, 38, 24, 20), (74, 34, 22, 20)], "#8097B2", snow="white", z=2.2)
    ax.add_patch(Rectangle((0, 0), 100, 20, color="#8FB4D4", zorder=3, lw=0)); ax.add_patch(Rectangle((0, 0), 100, 8, color="#6F9CC0", zorder=3.1, lw=0))
    rng = np.random.default_rng(4)
    for k in range(9):
        x = rng.uniform(6, 92); y = rng.uniform(4, 17); w = rng.uniform(7, 15)
        ax.add_patch(Polygon([(x, y), (x + w, y), (x + w - 2, y + 2.4), (x + 2, y + 2.8)], color="white", zorder=4, lw=0))
    waves(ax, 1, 18, "white", 0.35, 8, z=3.5)
    ax.add_patch(Polygon([(0, 20), (18, 20), (12, 30), (6, 24), (0, 31)], color="white", zorder=3.3, lw=0))
    ax.set_ylim(0, top); save(fig, "hero4")

# ------------------------------------------------------------------ seven unit banners (16.4 x 5.4 cm ≈ 3.04:1)
UW, UH = 8.2, 2.7
def unit1():
    fig, ax = canvas(UW, UH); top = 100 * UH / UW
    sun(ax, 82, 22, 5, SUN); cloud(ax, 20, 25, 0.8); cloud(ax, 55, 27, 0.6)
    peaks(ax, [(28, 36, 16, 8), (50, 40, 20, 8), (74, 34, 14, 8)], HILL[1], snow="white", z=2)
    ridge(ax, 9, 2.5, HILL[3], 5, z=3, floor=6)
    ax.add_patch(Polygon([(60, 6), (66, 15), (72, 6)], color="#5A2A22", zorder=3.5)); ax.add_patch(Polygon([(64.5, 14.5), (66, 18), (67.5, 14.5)], color="#E26A2C", zorder=3.6))
    strata_block(ax, 6.2, 0.3, 3); ax.set_ylim(0, top); save(fig, "unit1")
def unit2():
    fig, ax = canvas(UW, UH, "#FCF7F5", "#E9D6C7"); top = 100 * UH / UW
    ridge(ax, 6, 1.2, HILL[2], 3, z=2)
    for x in np.arange(3, 99, 5.5): broadleaf(ax, x, 3 + (x * 7) % 3, 12 + (x * 3) % 5, color=GREEN if int(x) % 2 else GREEN2, z=3)
    for x, y in ((24, 20), (44, 25), (70, 21)):    # birds
        ax.plot([x - 2, x, x + 2], [y + 1, y, y + 1], color="#46101C", lw=1.2, zorder=6)
    ax.add_patch(Ellipse((88, 6.5), 9, 3.2, color=WATER, zorder=4)); ax.add_patch(Polygon([(93, 6.5), (97, 8.5), (97, 4.5)], color=WATER, zorder=4))
    ax.set_ylim(0, top); save(fig, "unit2")
def unit3():
    fig, ax = canvas(UW, UH, "#FCF7F5", "#F2DADD"); top = 100 * UH / UW
    xs = np.linspace(2, 98, 200); ax.fill_between(xs, 0, 5 + 14 / (1 + np.exp(-(xs - 55) / 9)), color=HILL[1], alpha=0.55, zorder=2)
    for i, x in enumerate(np.arange(5, 96, 7)):
        h = 4 + 0.07 * x * (1 + 0.2 * np.sin(i));
        ax.add_patch(Circle((x, 6.5 + h * 0.9), 1.3, color=HILL[3], zorder=4)); ax.add_patch(Polygon([(x - 1.5, 5.2), (x + 1.5, 5.2), (x + 1.0, 6.5 + h * 0.8), (x - 1.0, 6.5 + h * 0.8)], color=HILL[3], zorder=4))
    ax.set_ylim(0, top); save(fig, "unit3")
def unit4():
    fig, ax = canvas(UW, UH, "#F7F1E6", "#E8DCC0"); top = 100 * UH / UW
    rng = np.random.default_rng(8); cols = ["#9DB67A", "#C5BE72", "#7FA06A", "#D6B46B", "#A98A5B"]
    for i in range(10):
        for j in range(3):
            x0 = i * 10; y0 = j * 9; ax.add_patch(Rectangle((x0 + 0.5, y0 + 0.5), 9, 8, color=cols[(i * 2 + j * 3 + rng.integers(0, 3)) % 5], zorder=2, lw=0))
            for k in range(1, 4): ax.plot([x0 + 0.5, x0 + 9.5], [y0 + 0.5 + k * 2, y0 + 0.5 + k * 2], color="white", alpha=0.18, lw=0.6, zorder=2.1)
    for cx, cy in ((25, 14), (65, 14), (85, 22)): ax.add_patch(Circle((cx, cy), 4.2, color="#5E8C54", zorder=3, lw=0)); ax.add_patch(Circle((cx, cy), 4.2, fill=False, edgecolor="white", lw=1, zorder=3.1))
    river(ax, [(0, 4), (20, 7), (40, 5), (60, 9), (80, 6), (100, 9)], 2.0, 2.4, WATER, z=3.5)
    ax.set_ylim(0, top); save(fig, "unit4")
def unit5():
    fig, ax = canvas(UW, UH, "#FCF7F5", "#EBC3C8"); top = 100 * UH / UW
    sun(ax, 14, 17, 5, SUN); ridge(ax, 6, 1.5, HILL[2], 9, z=2)
    for x, h in ((36, 15), (52, 12), (66, 15), (80, 11)): turbine(ax, x, 6, h, "white", z=5, ang=5 + x)
    for x in (88, 93, 98):
        ax.add_patch(Polygon([(x - 2, 7.5), (x + 2, 7.5), (x + 3, 10.5), (x - 1, 10.5)], color="#2F4E78", zorder=4)); ax.plot([x, x], [5, 7.5], color="#555", lw=0.8, zorder=3.9)
    ax.set_ylim(0, top); save(fig, "unit5")
def unit6():
    fig, ax = canvas(UW, UH, "#F6F0EF", "#D9C7C9"); top = 100 * UH / UW
    ax.add_patch(Rectangle((0, 0), 100, 6, color=HILL[4], zorder=3, lw=0))
    for x, h in ((20, 14), (28, 18), (36, 12)):
        ax.add_patch(Rectangle((x, 6), 4, h, color="#3A2A30", zorder=3.5)); ax.add_patch(Rectangle((x - 0.4, 6 + h - 1.4), 4.8, 1.4, color="#7A1424", zorder=3.6))
        for k in range(4): ax.add_patch(Ellipse((x + 2 + 3 * k, 6 + h + 2 + 2.6 * k), 5 + 1.4 * k, 3 + 0.9 * k, color="#9A9097", alpha=0.55 - 0.1 * k, zorder=3.4, lw=0))
    ax.add_patch(Rectangle((46, 6), 22, 7, color="#4B3F45", zorder=3.5))
    for x in (49, 54, 59, 64): ax.add_patch(Rectangle((x, 8.5), 2, 2.4, color="#F3D9A6", zorder=3.6))
    ax.add_patch(Polygon([(86, 22), (90, 14), (82, 14)], color=WATER, zorder=4)); ax.add_patch(Circle((86, 14.2), 4, color=WATER, zorder=4))
    ax.set_ylim(0, top); save(fig, "unit6")
def unit7():
    fig, ax = canvas(UW, UH, "#FCF7F5", "#F0C6C6"); top = 100 * UH / UW
    sun(ax, 78, 24, 7, SUN)
    ax.add_patch(Rectangle((0, 0), 100, 8, color="#6C97BA", zorder=2, lw=0)); waves(ax, 1, 7, "white", 0.4, 5)
    ax.add_patch(Polygon([(2, 8), (14, 22), (24, 8)], color="white", zorder=3)); ax.add_patch(Polygon([(16, 8), (30, 18), (40, 8)], color="#DDE8F2", zorder=3))
    ax.add_patch(Rectangle((52, 6), 2.2, 18, color="white", ec="#7A1424", lw=1.2, zorder=4)); ax.add_patch(Circle((53.1, 5.2), 2.2, color="#7A1424", zorder=4.1))
    ax.add_patch(Rectangle((52.55, 6), 1.1, 12, color="#7A1424", zorder=4.2))
    xs = np.linspace(58, 98, 40); ax.plot(xs, 8 + 0.0012 * (xs - 58) ** 2 * 3.2, color="#7A1424", lw=2, zorder=5)
    ax.set_ylim(0, top); save(fig, "unit7")

def build_all():
    for f in (hero1, hero2, hero3, hero4, unit1, unit2, unit3, unit4, unit5, unit6, unit7): f()

if __name__ == "__main__":
    build_all(); print("art built in", OUT)
