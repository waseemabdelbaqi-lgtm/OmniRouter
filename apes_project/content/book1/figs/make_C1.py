import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
from matplotlib.patches import Wedge
OUT='/home/user/OmniRouter/apes_project/content/book1/figs/'

# =============== 1.1 Geologic time ===============
fig,ax=plt.subplots(figsize=(6.4,4.3)); ax.set_xlim(-1,101); ax.set_ylim(-1.0,12.6); ax.axis('off')
def X1(t): return (4600-t)/4600*100
def X2(t): return (541-t)/541*100
eons=[("Hadean",4600,4000,"#C9856B"),("Archean",4000,2500,"#B08AA8"),("Proterozoic",2500,541,"#8FB3C9"),("Phanerozoic",541,0,"#7DB07D")]
ax.text(0,12.5,"All of Earth history (Ma = millions of years ago; 1,000 Ma = 1 Ga)",fontsize=8.5,fontweight='bold',va='top')
for n,a,b,c in eons:
    ax.add_patch(Rectangle((X1(a),8.0),X1(b)-X1(a),1.0,fc=c,ec='k',lw=.8))
    ax.text((X1(a)+X1(b))/2,8.5,n,ha='center',va='center',fontsize=8.5 if n!="Phanerozoic" else 6.4)
ev1=[(4600,"Earth forms\n4.6 Ga",'left'),(3500,"Earliest clear\nfossils ~3.5 Ga",'center'),(2400,"Oxygen builds up\nin air ~2.4 Ga",'center'),(541,"Animals diversify\n~541 Ma",'right')]
for t,sx,h in ev1:
    ax.plot([X1(t)]*2,[9.0,9.6],color=RED,lw=1)
    ax.text(X1(t)+(0.5 if h=='left' else (-0.5 if h=='right' else 0)),9.7,sx,ha=h,va='bottom',fontsize=7.8,color=DARK)
ax.plot([X1(541),0],[8.0,4.5],color=GREY,lw=.8,ls=':'); ax.plot([100,100],[8.0,4.5],color=GREY,lw=.8,ls=':')
eras=[("Paleozoic",541,252,"#8DB88D"),("Mesozoic",252,66,"#6FA2B8"),("Cenozoic",66,0,"#D9B26F")]
for n,a,b,c in eras:
    ax.add_patch(Rectangle((X2(a),3.4),X2(b)-X2(a),1.0,fc=c,ec='k',lw=.8))
    ax.text((X2(a)+X2(b))/2,3.9,n,ha='center',va='center',fontsize=8.5)
ax.text(30,6.0,"Zoom: the last 541 million years",fontsize=8.5,fontweight='bold',va='center',ha='center',bbox=dict(fc='white',ec='none',pad=1))
ev2=[(470,"Plants colonize\nland ~470 Ma",'center',2.9,2.9),(252,"Largest mass extinction\n252 Ma",'right',2.9,2.9),
     (66,"Asteroid impact; dinosaurs\n(except birds) gone 66 Ma",'right',2.9,2.9),(230,"Dinosaurs appear\n~230 Ma",'left',1.5,1.5),
     (0.3,"Modern humans ~0.3 Ma\n(a sliver at the right edge)",'right',0.1,0.1)]
for t,sx,h,y,_ in ev2:
    ax.plot([X2(t)]*2,[3.4,y+0.05],color=RED,lw=1)
    ax.text(X2(t)+(0.5 if h=='left' else (-0.5 if h=='right' else 0)),y,sx,ha=h,va='top',fontsize=7.8,color=DARK)
fig.savefig(OUT+'C1_geologic_time.png'); plt.close(fig)

# =============== 1.2 Earth layers ===============
fig,ax=plt.subplots(figsize=(6.4,4.3)); ax.set_xlim(-1.15,3.6); ax.set_ylim(-1.5,1.15); ax.set_aspect('equal'); ax.axis('off')
R=1.0
layers=[(1.00,"#6E4B2A","crust"),(0.955,"#A9714B","lith"),(0.86,"#D9822B","astheno"),(0.55,"#C9632B","mantle"),(0.35,"#F2C14E","outer"),(0.2,"#F7E08A","inner")]
# radii (not to scale in the thin outer layers)
ax.add_patch(Circle((0,0),1.0,fc="#6E4B2A",ec='k',lw=.8))      # crust (thickened)
ax.add_patch(Circle((0,0),0.96,fc="#B98A5E",ec='k',lw=.6))     # rigid upper mantle (with crust = lithosphere)
ax.add_patch(Circle((0,0),0.89,fc="#E5A25A",ec='k',lw=.6))     # asthenosphere
ax.add_patch(Circle((0,0),0.82,fc="#D56F3A",ec='k',lw=.8))     # rest of mantle
ax.add_patch(Circle((0,0),0.546,fc="#F2C14E",ec='k',lw=.8))    # outer core (true scale radius)
ax.add_patch(Circle((0,0),0.19,fc="#FBEFB0",ec='k',lw=.8))     # inner core (true scale radius)
ax.text(0,0.0,"inner\ncore",ha='center',va='center',fontsize=7)
ax.text(0,-0.68,"deeper mantle",ha='center',va='center',fontsize=7.5,color='white')
rows=[ (0.99,0.95,"Crust","5–10 km (ocean), 30–70 km (continent)","solid rock; 2.7–3.0 g/cm³"),
       (0.88,0.75,"Lithosphere","crust + rigid top of mantle, ~100 km","rigid, brittle; broken into plates"),
       (0.78,0.45,"Asthenosphere","~100 to ~350 km deep","solid but soft; flows slowly"),
       (0.6,0.1,"Mantle (whole)","to 2,900 km; ~84% of Earth's volume","hot solid rock; 3.3–5.7 g/cm³"),
       (0.3,-0.25,"Outer core","2,900–5,150 km","liquid iron–nickel; 10–12 g/cm³"),
       (0.1,-0.7,"Inner core","5,150–6,371 km","solid iron–nickel; ~13 g/cm³; ~5,400 °C")]
ys=[1.0,0.62,0.24,-0.14,-0.52,-0.9]
for (rr,_,n,d,p),y in zip(rows,ys):
    # leader from a point in that layer (angle varied) to text
    ang={"Crust":50,"Lithosphere":38,"Asthenosphere":25,"Mantle (whole)":12,"Outer core":-5,"Inner core":-20}[n]
    r={"Crust":0.98,"Lithosphere":0.93,"Asthenosphere":0.855,"Mantle (whole)":0.70,"Outer core":0.38,"Inner core":0.1}[n]
    px,py=r*np.cos(np.radians(ang)),r*np.sin(np.radians(ang))
    ax.plot([px,1.25],[py,y],color=GREY,lw=.7); ax.plot(px,py,'o',ms=2.5,color='k')
    ax.text(1.28,y+0.03,n,fontsize=8.5,fontweight='bold',va='center',color=DARK)
    ax.text(1.28,y-0.075,d+"\n"+p,fontsize=7,va='top')
ax.text(0,-1.38,"Crust, lithosphere and asthenosphere are drawn thicker than true scale; the core radii are to scale.",ha='center',va='top',fontsize=7,color=GREY)
fig.savefig(OUT+'C1_earth_layers.png'); plt.close(fig)

# =============== 1.3 Plate boundaries (redrawn) ===============
fig,axs=plt.subplots(1,3,figsize=(6.6,3.0))
for a in axs:
    a.set_xlim(0,10); a.set_ylim(0,10); a.axis('off')
MANT="#E9C9A0"; OCE="#7FA9C9"; CON="#B8A27C"
a=axs[0]; a.set_title("Convergent (subduction)",fontsize=9)
a.add_patch(Polygon([[0,0],[10,0],[10,5],[0,5]],fc=MANT,ec='none'))
a.add_patch(Polygon([[0,5],[5.4,5],[5.4,7.2],[0,7.2]],fc="#CFE6F5",ec='none'))
a.add_patch(Polygon([[0,5],[4.8,5],[8.2,1.2],[7.4,0.5],[4.2,4.0],[0,4.0]],fc=OCE,ec='k',lw=.8))
a.add_patch(Polygon([[4.8,5],[10,5],[10,7.6],[8.6,7.6],[7.8,8.8],[7.0,7.6],[5.6,7.0],[5.2,6.0]],fc=CON,ec='k',lw=.8))
a.add_patch(Polygon([[7.4,7.6],[7.8,8.8],[8.2,7.6]],fc=RED,ec='k',lw=.8))
arrow(a,(0.6,4.5),(2.8,4.5),color=DARK); arrow(a,(9.6,6.0),(8.4,6.0),color=DARK)
a.text(1.5,6.7,"ocean",fontsize=7.5,ha='center')
a.annotate("trench",xy=(4.7,5.1),xytext=(3.4,6.1),fontsize=7.5,color=DARK,ha='center',arrowprops=dict(arrowstyle='-|>',color=DARK,lw=.8))
a.text(5.4,9.2,"volcanic mountains",fontsize=7.5,ha='center')
a.text(1.6,1.6,"sinking slab:\nquakes get deeper\ninland",fontsize=7.3,ha='center',color=DARK)
a=axs[1]; a.set_title("Divergent",fontsize=9)
a.add_patch(Polygon([[0,5],[4.2,5],[4.6,6.2],[0,6.2]],fc=OCE,ec='k',lw=.8))
a.add_patch(Polygon([[10,5],[5.8,5],[5.4,6.2],[10,6.2]],fc=OCE,ec='k',lw=.8))
a.add_patch(Polygon([[0,5],[10,5],[10,1],[0,1]],fc=MANT,ec='none',zorder=0))
a.add_patch(Polygon([[4.2,5],[5.8,5],[5.6,1],[4.4,1]],fc="#E8863A",ec='none',zorder=1))
a.add_patch(Polygon([[4.2,5],[4.6,6.2],[5,6.6],[5.4,6.2],[5.8,5]],fc=RED,ec='k',lw=.8))
arrow(a,(4.2,7.8),(1.8,7.8),color=DARK); arrow(a,(5.8,7.8),(8.2,7.8),color=DARK)
a.text(5,3,"magma\nrises",fontsize=7.5,ha='center'); a.text(5,8.5,"new crust forms",fontsize=7.5,ha='center')
a.text(5,0.1,"ridge or rift valley;\nshallow quakes",fontsize=7.5,ha='center',color=DARK)
a=axs[2]; a.set_title("Transform (map view)",fontsize=9)
a.add_patch(Rectangle((0.5,5.2),9,3.6,fc=CON,ec='k',lw=.8)); a.add_patch(Rectangle((0.5,1.2),9,3.6,fc="#9DB58A",ec='k',lw=.8))
a.plot([0.5,9.5],[5,5],color=RED,lw=2.2,ls='--')
arrow(a,(2.5,7.0),(7.5,7.0),color=DARK,lw=2); arrow(a,(7.5,3.0),(2.5,3.0),color=DARK,lw=2)
a.text(5,8.2,"plate A",fontsize=8,ha='center'); a.text(5,1.8,"plate B",fontsize=8,ha='center')
a.text(5,5.1,"fault: locks, then slips",fontsize=7.2,ha='center',va='bottom',color=RED,backgroundcolor='white')
a.text(5,0.1,"earthquakes; crust not\ncreated or destroyed",fontsize=7.5,ha='center',color=DARK)
fig.tight_layout(); save(fig,OUT+'C1_plate_boundaries.png')

# =============== 1.4 Earthquake: focus, epicenter, waves, seismogram ===============
fig,(a1,a2)=plt.subplots(1,2,figsize=(6.6,3.0),gridspec_kw={'width_ratios':[1,1.15]})
a1.set_xlim(0,10); a1.set_ylim(0,10); a1.axis('off'); a1.set_title("Where it starts",fontsize=9)
a1.add_patch(Rectangle((0,0),10,7,fc="#D9C7A8",ec='none'))
a1.add_patch(Rectangle((0,7),10,0.25,fc=GREEN,ec='none'))
a1.plot([1.5,6.5],[9.4,1.0],color='k',lw=0)  # none
fx,fy=4.6,2.6
a1.plot([1.3,6.25],[7.0,0.4],color=DARK,lw=2.5)  # fault dipping through the focus
a1.plot([fx],[fy],'*',ms=15,color=RED,mec='k',zorder=5)
for r in (1.2,2.4,3.6):
    a1.add_patch(Wedge((fx,fy),r,40,140,width=0.04,fc=ORANGE,ec='none'))
a1.add_patch(Wedge((fx,fy),4.4,40,140,width=0.04,fc=ORANGE,ec='none'))
a1.plot([fx,fx],[fy,7.0],color=GREY,lw=1,ls='--')
a1.plot([fx],[7.12],'o',ms=7,color='white',mec=RED,mew=2,zorder=6)
a1.text(0.2,1.9,"focus (hypocenter):\nwhere the rock slips",fontsize=7.5,color=DARK,va='top')
a1.text(fx+0.4,8.0,"epicenter",fontsize=7.8,color=RED,va='bottom',ha='left')
a1.text(fx+0.2,4.9,"depth",fontsize=7.5,color=GREY,rotation=90,va='center')
a1.text(0.8,5.4,"fault",fontsize=7.5,color=DARK,rotation=-53)
a1.text(8.5,3.6,"seismic\nwaves spread\nin all directions",fontsize=7.2,ha='center',color=ORANGE)
a1.plot([9.0],[7.6],'^',ms=9,color=BLUE,mec='k'); a1.text(9.0,8.3,"station",fontsize=7.2,ha='center',color=BLUE)
# seismogram
rng=np.random.default_rng(5)
t=np.linspace(0,10,2000); y=0.05*rng.normal(size=t.size)
def burst(t0,dur,amp,f):
    m=(t>=t0)&(t<t0+dur); s=np.zeros_like(t); tt=t[m]-t0
    s[m]=amp*np.sin(2*np.pi*f*tt)*np.exp(-tt/ (dur/2.2)); return s
y+=burst(2.0,2.5,0.45,4.0)+burst(4.2,3.0,0.95,2.2)+burst(6.4,3.6,1.8,0.9)
a2.plot(t,y,color='k',lw=.7); a2.set_ylim(-2.6,3.0); a2.set_xlim(0,10)
for tx,lab,col in ((2.0,"P",BLUE),(4.2,"S",GREEN),(6.4,"surface",RED)):
    a2.axvline(tx,color=col,ls=':',lw=1)
a2.text(2.05,2.6,"P waves\nfirst, fastest",fontsize=7.2,color=BLUE,va='top')
a2.text(4.25,2.6,"S waves\nsecond",fontsize=7.2,color=GREEN,va='top')
a2.text(6.45,2.6,"surface waves\nlast, largest",fontsize=7.2,color=RED,va='top')
a2.annotate("",xy=(4.2,-2.1),xytext=(2.0,-2.1),arrowprops=dict(arrowstyle='<->',color=DARK,lw=1))
a2.text(3.1,-2.5,"S–P interval",fontsize=7.5,ha='center',color=DARK)
a2.set_xlabel("time after the earthquake (schematic)",fontsize=8); a2.set_yticks([]); a2.set_title("What a seismograph records",fontsize=9)
a2.spines['left'].set_visible(False)
fig.tight_layout(); save(fig,OUT+'C1_earthquake.png')

# =============== 1.5 Tsunami ===============
fig,ax=plt.subplots(figsize=(6.4,3.3)); ax.set_xlim(0,100); ax.set_ylim(-5.4,3.9); ax.axis('off')
x=np.linspace(0,100,2000)
floor=-np.where(x<62,4.0,np.interp(x,[62,92,100],[4.0,0.5,-0.3]))
floor=floor+0.55*np.exp(-((x-9)/4.5)**2)
ax.fill_between(x,floor,-5.0,color="#C9A877",zorder=1)
d=np.clip(-floor,0.2,None); d=np.where(x<20,4.0,d)
lam=np.sqrt(d); k=2*np.pi/(15*lam/2.0); phase=np.cumsum(k)*(x[1]-x[0])
amp=0.22*(4.0/d)**0.25
sm=np.clip((x-14)/12,0,1); sm=sm*sm*(3-2*sm)
hump=0.45*np.exp(-((x-9)/5)**2)*(1-sm)
surf=hump+amp*np.sin(phase+1.0)*sm
keep=x<=95.5
ax.fill_between(x[keep],floor[keep],surf[keep],where=(surf[keep]>floor[keep]),color="#CFE6F5",zorder=2)
ax.plot(x[keep],surf[keep],color=BLUE,lw=1.6,zorder=3)
ax.annotate("",xy=(9,1.55),xytext=(9,0.75),arrowprops=dict(arrowstyle='-|>',color=RED,lw=1.5))
ax.text(9,1.8,"seafloor lifted\nby a quake",ha='center',va='bottom',fontsize=7.5,color=RED)
ax.annotate("",xy=(48,2.3),xytext=(30,2.3),arrowprops=dict(arrowstyle='-|>',color=DARK,lw=1.4))
ax.text(39,2.5,"deep ocean: ~200 m/s (700 km/h);\nlong wavelength, height < 1 m",ha='center',va='bottom',fontsize=7.5,color=DARK)
ax.annotate("",xy=(97,1.6),xytext=(84,1.6),arrowprops=dict(arrowstyle='-|>',color=DARK,lw=1.4))
ax.text(88,1.8,"near shore: slower,\nshorter, taller",ha='center',va='bottom',fontsize=7.5,color=DARK)
ax.text(40,-2.4,"deep water (about 4,000 m)",ha='center',fontsize=7.5,color=DARK)
ax.text(80,-3.4,"shallow shelf",ha='center',fontsize=7.5,color=DARK)
ax.text(50,-5.3,"Wave heights greatly exaggerated; open-ocean wavelengths are about 100–200 km.",ha='center',fontsize=7,color=GREY)
fig.savefig(OUT+'C1_tsunami.png'); plt.close(fig)

# =============== 1.6 Volcano types ===============
fig,axs=plt.subplots(1,3,figsize=(6.6,3.9))
tit=["Shield volcano","Composite volcano","Cinder cone"]
desc=[["Magma: runny basalt","Slopes: gentle, about 2–10°","Eruptions: mostly quiet lava flows","Examples: Mauna Loa, Kilauea"],
      ["Magma: thick, gas-rich","(andesite to rhyolite)","Slopes: steep, up to about 30°","Eruptions: explosive; ash, pyroclastic","flows, lahars. Mt. St. Helens, Fuji"],
      ["Magma: gas-rich; blown into","cinders and ash","Size: small, usually under 300 m","Eruptions: short-lived","Example: Parícutin, Mexico"]]
for a,t,dl in zip(axs,tit,desc):
    a.set_xlim(0,10); a.set_ylim(-5.0,7.5); a.axis('off'); a.set_title(t,fontsize=9)
    a.add_patch(Rectangle((0,-1.0),10,1.0,fc="#C9B591",ec='none'))
    for n,l in enumerate(dl): a.text(0.2,-1.7-n*0.72,l,fontsize=6.9,ha='left',va='top',color=DARK if n else 'black')
a=axs[0]; a.add_patch(Polygon([[0,0],[2.5,1.0],[4.4,1.8],[5,1.9],[5.6,1.8],[7.5,1.0],[10,0]],fc="#5A4A42",ec='k',lw=.8))
a.add_patch(Polygon([[4.9,-0.7],[5.1,-0.7],[5.15,1.9],[4.85,1.9]],fc="#E8863A",ec='none'))
a.add_patch(Ellipse((5,-0.7),2.2,0.5,fc="#E8863A",ec='k',lw=.5))
a.plot([5.0,6.8,8.2],[1.9,1.6,1.2],color="#E8863A",lw=2)
a.text(5,3.2,"broad and low",ha='center',fontsize=7.5)
a=axs[1]; a.add_patch(Polygon([[0.3,0],[3.6,3.2],[4.5,4.4],[5,4.7],[5.5,4.4],[6.4,3.2],[9.7,0]],fc="#6B6B6B",ec='k',lw=.8))
for yy,xx0,xx1,c in ((0.9,0.6,9.4,"#B7A48A"),(1.7,1.4,8.6,"#8E5A3C"),(2.5,2.2,7.8,"#B7A48A"),(3.3,3.4,6.6,"#8E5A3C")):
    a.plot([xx0,xx1],[yy,yy],color=c,lw=2.4)
a.add_patch(Polygon([[4.9,-0.7],[5.1,-0.7],[5.2,4.5],[4.8,4.5]],fc="#E8863A",ec='none'))
a.add_patch(Ellipse((5,-0.7),2.0,0.5,fc="#E8863A",ec='k',lw=.5))
for cx,cy,rr in ((4.4,5.6,0.55),(5.2,6.2,0.7),(6.0,5.5,0.5),(4.9,5.0,0.4)):
    a.add_patch(Circle((cx,cy),rr,fc="#B0B0B0",ec='none',alpha=.7))
a.text(1.9,5.3,"tall and steep",ha='center',fontsize=7.5)
a.text(8.4,3.0,"layers of\nash and\nlava",ha='center',fontsize=6.6)
a=axs[2]; a.add_patch(Polygon([[2.6,0],[4.6,2.2],[5,2.35],[5.4,2.2],[7.4,0]],fc="#7A3B2A",ec='k',lw=.8))
a.add_patch(Polygon([[4.92,-0.7],[5.08,-0.7],[5.12,2.3],[4.88,2.3]],fc="#E8863A",ec='none'))
a.add_patch(Ellipse((5,-0.7),1.6,0.5,fc="#E8863A",ec='k',lw=.5))
for cx,cy,rr in ((4.9,3.2,0.4),(5.3,3.8,0.5),(4.7,4.4,0.45)):
    a.add_patch(Circle((cx,cy),rr,fc="#B0B0B0",ec='none',alpha=.7))
a.text(5,5.3,"small and steep",ha='center',fontsize=7.5)
for a in axs: a.text(9.8,-0.62,"magma",ha='right',fontsize=6.4,color=DARK)
fig.tight_layout(); save(fig,OUT+'C1_volcano_types.png')

# =============== 1.7a Insolation spreading ===============
fig,ax=plt.subplots(figsize=(6.4,3.0)); ax.set_xlim(-2.6,2.2); ax.set_ylim(-1.8,1.45); ax.set_aspect('equal'); ax.axis('off')
ax.add_patch(Circle((0,0),1.12,fc="#E6F0F8",ec='none')); ax.add_patch(Circle((0,0),1.0,fc="#8DB88D",ec='k',lw=.9))
th=np.linspace(0,2*np.pi,300)
def beam(y0,y1,col):
    # rays from left to the surface between y0,y1 (horizontal sunlight)
    for yy in np.linspace(y0,y1,5):
        xs=-np.sqrt(1-yy**2)
        ax.annotate("",xy=(xs,yy),xytext=(-2.4,yy),arrowprops=dict(arrowstyle='-|>',color=ORANGE,lw=1.2))
    a0,a1=np.degrees(np.arcsin(y0)),np.degrees(np.arcsin(y1))
    tt=np.radians(np.linspace(180-a1,180-a0,40))
    ax.plot(np.cos(tt),np.sin(tt),color=RED,lw=4,solid_capstyle='butt')
beam(-0.1,0.1,RED); beam(0.75,0.95,RED)
ax.text(-2.45,0.0-0.18,"equator: rays hit head-on;\nenergy on a small area",fontsize=7.3,va='top',color=DARK)
ax.text(-2.45,1.2,"high latitude (~60°, sun angle 30°):\nsame beam\nspread over twice the area,\nthrough more atmosphere",fontsize=7.3,va='bottom',color=DARK)
ax.text(1.18,0,"equator",fontsize=7.5,va='center'); ax.text(0.45,1.08,"~60° N",fontsize=7.5,va='bottom')
ax.text(0,0,"Earth",ha='center',va='center',fontsize=8)
ax.text(-2.45,-1.3,"Parallel rays from the Sun. Red arcs: ground area the beam covers (shown at an equinox).\nThe atmosphere is the thin light ring.",fontsize=7,color=GREY,va='top')
fig.savefig(OUT+'C1_insolation.png'); plt.close(fig)

# =============== 1.7b Seasons orbit ===============
fig,ax=plt.subplots(figsize=(6.4,4.0)); ax.set_xlim(-5.6,5.6); ax.set_ylim(-3.7,3.6); ax.set_aspect('equal'); ax.axis('off')
ax.add_patch(Circle((0,0),0.5,fc=YELLOW,ec=ORANGE,lw=1.5)); ax.text(0,0,"Sun",ha='center',va='center',fontsize=7.5)
ex,ey=3.8,1.95
tt=np.linspace(0,2*np.pi,300); ax.plot(ex*np.cos(tt),ey*np.sin(tt),color=GREY,lw=1,ls='--')
tilt=np.radians(23.5); r=0.62
pos=[("June solstice",180,"N. Hemisphere tilted toward Sun;\ndirect sun at 23.5° N"),
     ("September equinox",270,"direct sun at the equator"),
     ("December solstice",0,"N. Hemisphere tilted away from Sun;\ndirect sun at 23.5° S"),
     ("March equinox",90,"direct sun at the equator")]
for lab,ang,sub in pos:
    cx,cy=ex*np.cos(np.radians(ang)),ey*np.sin(np.radians(ang))
    ax.add_patch(Circle((cx,cy),r,fc="#BFD9EE",ec='k',lw=.9,zorder=3))
    dirang=np.degrees(np.arctan2(cy,cx))
    ax.add_patch(Wedge((cx,cy),r,dirang-90,dirang+90,fc="#2B3A55",ec='none',alpha=.75,zorder=4))
    dx,dy=np.sin(tilt),np.cos(tilt)
    ax.plot([cx-1.0*r*dx*1.0,cx+1.6*r*dx],[cy-1.0*r*dy,cy+1.6*r*dy],color=RED,lw=1.6,zorder=5)
    ax.text(cx+1.7*r*dx+0.04,cy+1.7*r*dy,"N",fontsize=7.5,color=RED,fontweight='bold',zorder=6,ha='left',va='center')
    if ang in (180,0): ax.text(cx,cy-0.95,lab+"\n"+sub,ha='center',va='top',fontsize=7.3,color=DARK,bbox=dict(fc='white',ec='none',pad=0.5))
    elif ang==270: ax.text(cx,cy-0.95,lab+"; "+sub,ha='center',va='top',fontsize=7.3,color=DARK)
    else: ax.text(cx,cy+1.3,lab+"; "+sub,ha='center',va='bottom',fontsize=7.3,color=DARK)
ax.text(0,-3.55,"The 23.5° tilt always points the same way in space. Dark half of each Earth = night. Not to scale.",ha='center',fontsize=7,color=GREY,va='center')
fig.savefig(OUT+'C1_seasons.png'); plt.close(fig)

# =============== 1.7c Latitude / longitude globe ===============
fig,ax=plt.subplots(figsize=(6.2,3.5)); ax.set_xlim(-1.95,2.9); ax.set_ylim(-1.15,1.2); ax.set_aspect('equal'); ax.axis('off')
lat0,lon0=np.radians(22),np.radians(-45)
def proj(lat,lon):
    lat=np.radians(lat); lon=np.radians(lon)
    x=np.cos(lat)*np.sin(lon-lon0)
    y=np.cos(lat0)*np.sin(lat)-np.sin(lat0)*np.cos(lat)*np.cos(lon-lon0)
    c=np.sin(lat0)*np.sin(lat)+np.cos(lat0)*np.cos(lat)*np.cos(lon-lon0)
    return x,y,c
ax.add_patch(Circle((0,0),1,fc="#DCEBF7",ec='k',lw=1))
def line(lats,lons,col,lw,ls='-',z=2):
    x,y,c=proj(lats,lons); x=np.where(c>0,x,np.nan); y=np.where(c>0,y,np.nan)
    ax.plot(x,y,color=col,lw=lw,ls=ls,zorder=z)
lo=np.linspace(-180,180,721); la=np.linspace(-90,90,361)
for l in range(-60,90,30): line(np.full_like(lo,l),lo,GREY,.6)
for m in range(-180,180,30): line(la,np.full_like(la,m),GREY,.6)
line(np.zeros_like(lo),lo,RED,2.0)          # equator
line(la,np.zeros_like(la),BLUE,2.0)         # prime meridian
line(np.full_like(lo,23.5),lo,ORANGE,1.2,'--'); line(np.full_like(lo,66.5),lo,TEAL,1.2,'--')
# labels
for l,t in ((0,"0° (equator)"),(30,"30° N"),(60,"60° N"),(-30,"30° S")):
    x,y,c=proj(l,-120);
for l,t in ((30,"30° N"),(60,"60° N"),(-30,"30° S"),(-60,"60° S")):
    x,y,c=proj(l,-45); ax.text(x+0.02,y+0.01,t,fontsize=6.6,ha='left',va='bottom',color=DARK)
x,y,c=proj(0,-132); ax.text(x-0.05,y,"equator 0°",fontsize=7,ha='right',va='center',color=RED,fontweight='bold')
for m in (-90,-60,-30):
    x,y,c=proj(-8,m); ax.text(x,y,f"{abs(m)}°{'W' if m<0 else 'E'}",fontsize=6.6,ha='center',va='top',color=DARK)
x,y,c=proj(-25,0); ax.annotate("prime meridian\n(0° longitude)",xy=(x,y),xytext=(1.2,-0.85),fontsize=7,color=BLUE,fontweight='bold',arrowprops=dict(arrowstyle='-',color=BLUE,lw=.8))
px,py,pc=proj(40,-75); ax.plot(px,py,'o',ms=7,color=RED,mec='k',zorder=6)
ax.annotate("Point: 40° N, 75° W",xy=(px,py),xytext=(-1.9,0.98),fontsize=8,color=RED,arrowprops=dict(arrowstyle='-',color=RED,lw=.9))
ax.text(1.2,0.9,"Latitude: angle north or south of the\nequator (0° to 90°). Parallels run east–west.\n\nLongitude: angle east or west of the\nprime meridian (0° to 180°). Meridians\nrun pole to pole.",fontsize=7.4,va='top',color=DARK)
ax.text(1.2,-0.1,"Dashed lines: Tropic of Cancer 23.5° N\n(orange) and Arctic Circle 66.5° N (teal).",fontsize=7,va='top',color=GREY)
fig.savefig(OUT+'C1_latlong.png'); plt.close(fig)

# =============== 1.9 Rock cycle ===============
fig,ax=plt.subplots(figsize=(6.4,4.2)); ax.set_xlim(0,10); ax.set_ylim(-0.5,7); ax.axis('off')
nodes={"magma":(5,6.0,"Magma / lava\n(molten rock)","#F2B58A"),
       "ign":(8.6,4.2,"Igneous rock\ngranite, basalt","#D9B6A8"),
       "sed":(7.8,1.0,"Sediment\nsand, silt, clay, ions","#E6D6A8"),
       "sdr":(2.2,1.0,"Sedimentary rock\nsandstone, limestone","#C9D9B8"),
       "met":(1.4,4.2,"Metamorphic rock\nmarble, slate, gneiss","#B9C9DC")}
w,h=2.5,0.95
for k,(x,y,t,c) in nodes.items():
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle="round,pad=0.02,rounding_size=0.12",fc=c,ec=RED,lw=1.3,zorder=3))
    ax.text(x,y,t,ha='center',va='center',fontsize=7.8,zorder=4)
def ar(p,q,lab,lp,rad=0.0,ls='-',ha='center'):
    ax.add_patch(FancyArrowPatch(p,q,arrowstyle="-|>",mutation_scale=13,color=DARK,lw=1.4,ls=ls,connectionstyle=f"arc3,rad={rad}",zorder=2))
    ax.text(lp[0],lp[1],lab,fontsize=7.2,color=DARK,ha=ha,va='center',bbox=dict(fc='white',ec='none',pad=0.8,alpha=.9),zorder=5)
ar((6.25,5.9),(8.2,4.7),"cooling and\ncrystallization",(7.9,5.75),rad=-0.1)
ar((8.7,3.7),(7.9,1.5),"weathering,\nerosion, transport,\ndeposition",(9.25,2.6),rad=0.0,ha='center')
ar((6.5,1.0),(3.5,1.0),"compaction and cementation\n(lithification)",(5.0,0.45))
ar((2.0,1.5),(1.5,3.7),"heat and pressure",(0.9,2.6),rad=0.0)
ar((1.9,4.65),(3.75,5.85),"melting",(2.5,5.7),rad=-0.1)
# shortcuts
ar((7.6,4.0),(2.65,4.0),"",(5,4),ls='--')
ax.text(5,4.25,"igneous rock can also be metamorphosed",ha='center',fontsize=6.8,color=GREY)
ar((2.0,3.7),(6.6,1.45),"",(0,0),ls='--',rad=0.0)
ax.text(5.35,2.55,"any rock can weather into sediment",fontsize=6.8,color=GREY,rotation=-25,ha='center')
ax.text(5,-0.3,"Uplift by plate tectonics exposes buried rock to weathering; subduction carries rock down to melt.",ha='center',fontsize=7,color=GREY)
fig.savefig(OUT+'C1_rock_cycle.png'); plt.close(fig)
print("done")
