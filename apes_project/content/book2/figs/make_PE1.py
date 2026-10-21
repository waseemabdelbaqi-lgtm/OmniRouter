import sys, numpy as np
sys.path.insert(0, '/home/user/OmniRouter/apes_project/tools')
from figstyle import *
OUT = '/home/user/OmniRouter/apes_project/content/book2/figs/'
rng = np.random.default_rng(11)

# ---------- U1 estuary food web ----------
fig, ax = canvas(6.2, 3.8, (0, 10), (0, 6))
nodes = {'Phytoplankton': (1.1, 3.0), 'Zooplankton': (3.7, 4.6), 'Clam': (3.7, 1.2),
 'Anchovy': (6.3, 4.6), 'Heron': (8.8, 2.4), 'Harbor seal': (8.8, 5.4)}
for k, (x, y) in nodes.items():
    box(ax, x-0.9, y-0.35, 1.8, 0.7, k, fs=8.5)
arrow(ax,(1.8,3.35),(3.0,4.25),lw=1.3); arrow(ax,(1.8,2.65),(3.0,1.55),lw=1.3)
arrow(ax,(4.6,4.6),(5.4,4.6),lw=1.3); arrow(ax,(7.2,4.8),(7.95,5.2),lw=1.3)
arrow(ax,(7.0,4.25),(8.2,2.75),lw=1.3); arrow(ax,(4.6,1.3),(7.95,2.1),lw=1.3)
ax.text(5, 0.25, 'Arrows point from the organism eaten to the organism that eats it.', ha='center', fontsize=8, style='italic', color=GREY)
save(fig, OUT+'PE1_U1_estuary_web.png')

# ---------- U2 island biogeography ----------
fig, ax = plt.subplots(figsize=(6, 3.6))
A = np.logspace(0, 3, 100)
for c, lab, col, mk in [(14, 'Islands within 10 km of the mainland', BLUE, 'o'), (6, 'Islands more than 150 km from the mainland', ORANGE, 's')]:
    ax.plot(A, c*A**0.25, color=col, lw=1.2, alpha=.6)
    pts = np.array([1.5, 4, 12, 40, 120, 350, 900])
    ax.scatter(pts, c*pts**0.25*(1+rng.normal(0, 0.05, len(pts))), color=col, marker=mk, s=28, label=lab, zorder=3)
ax.set_xscale('log'); ax.set_xlabel('Island area (km², log scale)'); ax.set_ylabel('Number of bird species')
ax.set_ylim(0, 90); ax.legend(frameon=False, fontsize=8, loc='upper left'); ax.grid(alpha=.25)
save(fig, OUT+'PE1_U2_island_biogeog.png')

# ---------- U3 survivorship ----------
fig, ax = plt.subplots(figsize=(5.6, 3.6))
x = np.linspace(0, 100, 200)
c2 = 1000*(1-(x/100)**5.5)+0.001; c2 = np.clip(c2, 8, None)
c1 = 1000*np.exp(-x*0.065)
c3 = 1000*np.exp(-x*0.034)
ax.semilogy(x, c1, color=RED, lw=2); ax.semilogy(x, c2, color=BLUE, lw=2); ax.semilogy(x, c3, color=GREEN, lw=2)
ax.text(8, 12, 'Curve 1', color=RED, fontsize=10, fontweight='bold')
ax.text(72, 250, 'Curve 2', color=BLUE, fontsize=10, fontweight='bold')
ax.text(62, 160, 'Curve 3', color=GREEN, fontsize=10, fontweight='bold')
ax.set_xlabel('Age (% of maximum life span)'); ax.set_ylabel('Number of survivors (log scale)')
ax.set_ylim(1, 1500); ax.grid(alpha=.25, which='both')
save(fig, OUT+'PE1_U3_survivorship.png')

# ---------- U3 age structure ----------
groups = ['0–14', '15–29', '30–44', '45–59', '60–74', '75+']
data = {'Country 1': [18, 14, 9, 5, 3, 1], 'Country 2': [8, 9, 10, 10, 9, 4], 'Country 3': [5, 7, 9, 11, 12, 6]}
fig, axs = plt.subplots(1, 3, figsize=(6.4, 3.0), sharey=True)
for ax, (k, v) in zip(axs, data.items()):
    y = np.arange(len(groups))
    ax.barh(y, [-i for i in v], color=BLUE, height=.85); ax.barh(y, v, color=ORANGE, height=.85)
    ax.set_xlim(-20, 20); ax.set_title(k, fontsize=10); ax.set_yticks(y); ax.set_yticklabels(groups, fontsize=8)
    ax.set_xticks([-15, 0, 15]); ax.set_xticklabels(['15', '0', '15'], fontsize=8)
    ax.spines['left'].set_visible(False); ax.tick_params(axis='y', length=0)
axs[0].set_ylabel('Age group (years)'); fig.text(.5, -.02, 'Percent of total population (males left, females right)', ha='center', fontsize=9)
fig.tight_layout()
save(fig, OUT+'PE1_U3_agestructure.png')

# ---------- U4 ENSO ----------
t = np.linspace(2014, 2025, 133)
def g(c, a, w): return a*np.exp(-((t-c)/w)**2)
anom = g(2015.9, 2.5, .55)+g(2015.0, .6, .5)+g(2017.9, -0.8, .35)+g(2018.9, .7, .4)+g(2021.0, -1.1, .5)+g(2022.2, -1.4, .55)+g(2023.9, 1.9, .5)+g(2019.7, .4, .3)
anom += rng.normal(0, .05, len(t))
fig, ax = plt.subplots(figsize=(6.2, 3.2))
ax.plot(t, anom, color='#333', lw=1)
ax.fill_between(t, 0, anom, where=anom >= 0.5, color=RED, alpha=.55, interpolate=True)
ax.fill_between(t, 0, anom, where=anom <= -0.5, color=BLUE, alpha=.55, interpolate=True)
ax.axhline(0, color='#333', lw=.7); ax.axhline(.5, color=GREY, lw=.5, ls='--'); ax.axhline(-.5, color=GREY, lw=.5, ls='--')
ax.set_xlim(2014, 2025); ax.set_xticks(range(2014, 2026)); ax.set_xticklabels([str(i) for i in range(2014, 2026)], fontsize=8)
ax.set_ylabel('Sea-surface temperature anomaly,\ncentral equatorial Pacific (°C)'); ax.set_xlabel('Year')
save(fig, OUT+'PE1_U4_enso.png')
print('ENSO sample', {y: round(float(anom[np.argmin(abs(t-y))]), 2) for y in [2016, 2018, 2021, 2022, 2023.9]})

# ---------- U4 hydrograph ----------
h = np.linspace(0, 24, 300)
def hy(pk, tp, s, base):
    return base+(pk-base)*np.exp(-((h-tp)/s)**2*0.9)*np.where(h < tp, 1, np.exp(-(h-tp)/s*0.35))
pre = hy(18, 9.5, 3.6, 3); post = hy(52, 5, 1.9, 3)
fig, ax = plt.subplots(figsize=(5.8, 3.3))
ax.plot(h, pre, color=GREEN, lw=2, label='1995 (mostly forest and pasture)'); ax.plot(h, post, color=RED, lw=2, label='2025 (after urban development)')
ax.set_xlabel('Hours since rainfall began'); ax.set_ylabel('River discharge (m³/s)'); ax.set_xlim(0, 24); ax.set_ylim(0, 60)
ax.legend(frameon=False, fontsize=8); ax.grid(alpha=.25)
save(fig, OUT+'PE1_U4_hydrograph.png')

# ---------- U5 fishery ----------
yrs = [1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020]
catch = [12, 25, 38, 48, 44, 36, 29, 24, 20]; eff = [10, 16, 24, 32, 38, 46, 54, 62, 66]
fig, axs = plt.subplots(2, 1, figsize=(5.8, 4.2), sharex=True)
axs[0].plot(yrs, catch, 'o-', color=BLUE); axs[0].set_ylabel('Catch\n(thousand tons)'); axs[0].set_ylim(0, 60); axs[0].grid(alpha=.25)
axs[1].plot(yrs, eff, 's-', color=ORANGE); axs[1].set_ylabel('Fishing effort\n(thousand boat-days)'); axs[1].set_ylim(0, 80); axs[1].grid(alpha=.25)
axs[1].set_xlabel('Year'); axs[1].set_xticks(yrs)
fig.tight_layout()
save(fig, OUT+'PE1_U5_fishery.png')

# ---------- U6 grid mix ----------
yy = ['2010', '2015', '2020', '2024']
diesel = [780, 700, 520, 380]; hydro = [120, 120, 120, 120]; solar = [20, 80, 190, 300]; wind = [10, 40, 110, 200]
fig, ax = plt.subplots(figsize=(5.8, 3.5))
b = np.zeros(4)
for lab, v, c in [('Diesel and fuel oil', diesel, GREY), ('Hydropower', hydro, BLUE), ('Solar', solar, YELLOW), ('Wind', wind, TEAL)]:
    ax.bar(yy, v, bottom=b, label=lab, color=c, width=.6); b += np.array(v)
ax.set_ylabel('Electricity generated (GWh per year)'); ax.set_xlabel('Year'); ax.legend(frameon=False, fontsize=8, loc='upper left', ncol=2); ax.set_ylim(0, 1300)
save(fig, OUT+'PE1_U6_grid_mix.png')

# ---------- U6 insolation ----------
mo = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
X = [4.2, 4.6, 5.0, 5.3, 5.6, 5.8, 5.8, 5.6, 5.2, 4.8, 4.3, 4.0]
Y = [2.6, 3.2, 4.4, 5.6, 6.6, 7.4, 7.8, 7.2, 5.8, 4.3, 3.0, 2.4]
print('means', np.mean(X), np.mean(Y))
fig, ax = plt.subplots(figsize=(5.8, 3.3))
ax.plot(mo, X, 'o-', color=BLUE, label='Site 1 (coastal plain)'); ax.plot(mo, Y, 's-', color=ORANGE, label='Site 2 (inland basin)')
ax.set_ylabel('Solar energy received on a\nsouth-facing panel (kWh/m²/day)'); ax.set_xlabel('Month'); ax.tick_params(axis='x', labelsize=8); ax.set_ylim(0, 9); ax.legend(frameon=False, fontsize=8, loc='lower center', ncol=2); ax.grid(alpha=.25)
save(fig, OUT+'PE1_U6_insolation.png')

# ---------- U7 diurnal ----------
hr = np.linspace(0, 24, 240)
no2 = 8+30*np.exp(-((hr-7.5)/1.6)**2)+16*np.exp(-((hr-18)/1.8)**2)
o3 = 12+70*np.exp(-((hr-14.5)/3.2)**2)
fig, ax = plt.subplots(figsize=(5.8, 3.3))
ax.plot(hr, no2, color=RED, lw=2, label='Nitrogen dioxide (NO₂)'); ax.plot(hr, o3, color=GREEN, lw=2, label='Ozone (O₃)')
ax.set_xlim(0, 24); ax.set_xticks(range(0, 25, 3)); ax.set_xticklabels(['12 am', '3 am', '6 am', '9 am', '12 pm', '3 pm', '6 pm', '9 pm', '12 am'], fontsize=8)
ax.set_ylabel('Concentration (ppb)'); ax.set_xlabel('Time of day (sunny summer weekday)'); ax.legend(frameon=False, fontsize=8, loc='upper left'); ax.grid(alpha=.25)
save(fig, OUT+'PE1_U7_diurnal.png')

# ---------- U7 inversion ----------
alt = [0, 200, 500, 1200]; tmp = [11.0, 8.6, 15.8, 11.6]
fig, ax = plt.subplots(figsize=(4.6, 3.6))
ax.plot(tmp, alt, 'o-', color=RED, lw=2)
ax.set_xlabel('Air temperature (°C)'); ax.set_ylabel('Altitude above ground (m)'); ax.set_ylim(0, 1300); ax.set_xlim(6, 18); ax.grid(alpha=.25)
ax.set_yticks([0, 200, 500, 800, 1200])
save(fig, OUT+'PE1_U7_inversion.png')

# ---------- U8 DO sag ----------
d = np.linspace(0, 100, 300)
u = d/25.0
do = 8.5-5.5*u*np.exp(1-u)
fig, ax = plt.subplots(figsize=(5.8, 3.3))
ax.plot(d, do, color=BLUE, lw=2); ax.axhline(5, color=RED, ls='--', lw=1); ax.text(70, 5.15, 'Minimum for most fish (5 mg/L)', color=RED, fontsize=8)
ax.axvline(0, color=GREY, lw=1, ls=':'); ax.text(1.5, 1.2, 'Wastewater\noutfall', fontsize=8, color=GREY)
ax.set_xlabel('Distance downstream of outfall (km)'); ax.set_ylabel('Dissolved oxygen (mg/L)'); ax.set_ylim(0, 10); ax.set_xlim(-5, 100); ax.grid(alpha=.25)
save(fig, OUT+'PE1_U8_do_sag.png')

# ---------- U8 dose response ----------
dose = np.logspace(-1, 3, 300)
def lg(ld50, s=2.5): return 100/(1+(ld50/dose)**s)
fig, ax = plt.subplots(figsize=(5.8, 3.4))
ax.semilogx(dose, lg(10), color=RED, lw=2, label='Chemical A'); ax.semilogx(dose, lg(100), color=BLUE, lw=2, label='Chemical B')
ax.axhline(50, color=GREY, lw=.8, ls='--'); ax.set_xlabel('Dose (mg per kg body mass, log scale)'); ax.set_ylabel('Test animals that died (%)')
ax.set_ylim(0, 100); ax.set_xlim(.1, 1000); ax.legend(frameon=False, fontsize=9, loc='upper left'); ax.grid(alpha=.25, which='both')
save(fig, OUT+'PE1_U8_dose_response.png')

# ---------- U9 sea ice ----------
yr = np.arange(1980, 2021)
ice = 7.8-(3.9/40)*(yr-1980)+rng.normal(0, .22, len(yr)); ice[0] = 7.8; ice[-1] = 3.9
fig, ax = plt.subplots(figsize=(5.8, 3.3))
ax.plot(yr, ice, 'o-', color=BLUE, ms=3, lw=1)
ax.annotate('1980: 7.8', (1980, 7.8), xytext=(1983, 8.3), fontsize=8, arrowprops=dict(arrowstyle='-', color=GREY))
ax.annotate('2020: 3.9', (2020, 3.9), xytext=(2014.5, 3.0), fontsize=8, arrowprops=dict(arrowstyle='-', color=GREY))
ax.set_ylim(2, 9); ax.set_xlabel('Year'); ax.set_ylabel('September minimum Arctic sea-ice\nextent (million km²)'); ax.grid(alpha=.25)
save(fig, OUT+'PE1_U9_sea_ice.png')

# ---------- U9 pH ----------
y2 = np.arange(1985, 2025)
co2 = 346+(422-346)*((y2-1985)/39)**1.1+rng.normal(0, .8, len(y2)); co2[0] = 346; co2[-1] = 422
ph = 8.12-0.08*((y2-1985)/39)+rng.normal(0, .004, len(y2)); ph[0] = 8.12; ph[-1] = 8.04
fig, axs = plt.subplots(1, 2, figsize=(6.4, 3.0))
axs[0].plot(y2, co2, color=ORANGE, lw=1.5); axs[0].set_ylabel('Surface-seawater pCO₂ (µatm)'); axs[0].set_xlabel('Year')
axs[1].plot(y2, ph, color=TEAL, lw=1.5); axs[1].set_ylabel('Surface-seawater pH'); axs[1].set_xlabel('Year')
for a in axs: a.grid(alpha=.25)
fig.tight_layout()
save(fig, OUT+'PE1_U9_ph.png')

# ---------- FRQ1 estuary schematic ----------
fig, ax = canvas(6.4, 4.0, (0, 12), (0, 7.5))
ax.add_patch(Rectangle((0, 0), 12, 7.5, fc='white', ec='#444', lw=.8))
ax.add_patch(Rectangle((0, 0), 3.4, 7.5, fc='#E3EBC9', ec='none')); ax.text(1.7, 6.9, 'Farmland\n(corn, vegetables)', ha='center', va='center', fontsize=8.5)
ax.add_patch(Rectangle((8.2, 0), 3.8, 7.5, fc=SKY, ec='none', alpha=.7)); ax.text(10.1, 6.9, 'Harbor Bay', ha='center', fontsize=9, fontweight='bold')
ax.add_patch(Ellipse((6.3, 4.9), 3.4, 1.9, fc='#9DBB7A', ec=GREEN, lw=1.2)); ax.text(6.3, 4.35, 'Restored salt marsh\n(40 ha)', ha='center', va='center', fontsize=8)
ax.plot([3.4, 4.6, 8.2], [5.4, 4.9, 4.9], color=BLUE, lw=3); ax.text(3.4, 6.25, 'Harbor Creek', fontsize=8, color=BLUE)
ax.plot([3.4, 5.0, 6.4, 8.2], [1.6, 1.9, 1.4, 1.4], color=BLUE, lw=3); ax.text(3.6, 0.7, 'Mill Creek (no marsh)', fontsize=8, color=BLUE)
for (x, y, lab) in [(4.0, 5.2, 'H1'), (7.9, 4.9, 'H2'), (4.3, 1.8, 'M1'), (7.9, 1.4, 'M2')]:
    ax.add_patch(Circle((x, y), .22, fc=RED, ec='white', zorder=4)); ax.text(x, y+.45, lab, ha='center', fontsize=8.5, color=RED, fontweight='bold')
ax.text(6, 3.0, 'Drainage ditches carry irrigation and rain runoff\nfrom fields into both creeks', ha='center', fontsize=8, style='italic', color=GREY)
ax.text(.2, .25, 'Not to scale. Dots mark existing water-quality access points.', fontsize=7.5, color=GREY)
save(fig, OUT+'PE1_FRQ1_estuary.png')

# ---------- FRQ2 Arctic ----------
y3 = [2000, 2005, 2010, 2015, 2020, 2025]; ald = [42, 45, 52, 60, 68, 77]; shr = [12, 14, 19, 25, 31, 38]; tm = [3.1, 3.4, 4.0, 4.6, 5.1, 5.7]
fig, axs = plt.subplots(1, 2, figsize=(6.4, 3.0))
axs[0].plot(y3, ald, 'o-', color=BROWN); axs[0].set_ylabel('Active-layer depth (cm)'); axs[0].set_xlabel('Year'); axs[0].grid(alpha=.25)
axs[1].plot(y3, shr, 's-', color=GREEN); axs[1].set_ylabel('Shrub cover (% of ground)'); axs[1].set_xlabel('Year'); axs[1].grid(alpha=.25)
fig.tight_layout()
save(fig, OUT+'PE1_FRQ2_arctic.png')
