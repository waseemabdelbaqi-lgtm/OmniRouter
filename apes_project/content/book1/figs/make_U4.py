import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
OUT='/home/user/OmniRouter/apes_project/content/book1/figs/'

# ---------- Fig 4.1 plate boundaries ----------
fig,axs=plt.subplots(1,3,figsize=(6.6,3.0))
for a in axs:
    a.set_xlim(0,10); a.set_ylim(0,10); a.axis('off')
MANT="#E9C9A0"; OCE="#7FA9C9"; CON="#B8A27C"
# convergent
a=axs[0]; a.set_title("Convergent",fontsize=10)
a.add_patch(Polygon([[0,6],[0,10],[10,10],[10,6]],fc="#CFE6F5",ec='none'))  # water bg
a.add_patch(Polygon([[5.5,6.2],[10,6.2],[10,8.6],[8.6,8.6],[7.6,9.4],[6.8,8.6],[5.5,8.6]],fc=CON,ec='k',lw=.8))
a.add_patch(Polygon([[0,6],[4.6,6],[7.6,3.0],[7.6,2.2],[4.6,5.0],[0,5.0]],fc=OCE,ec='k',lw=.8))
a.add_patch(Polygon([[0,5],[10,5],[10,0],[0,0]],fc=MANT,ec='none',zorder=0))
a.add_patch(Polygon([[5.5,6.2],[10,6.2],[10,5],[7.6,3.0],[4.6,6]],fc="#C9B591",ec='none',zorder=0))
a.add_patch(Polygon([[5.5,6.0],[10,6.0],[10,5.0],[6.5,5.0]],fc=CON,ec='k',lw=.8))
a.add_patch(Polygon([[7.0,8.6],[7.5,9.6],[8.0,8.6]],fc=RED,ec='k',lw=.8))
arrow(a,(1,6.6),(3.2,6.6),color=DARK); arrow(a,(9.5,5.6),(8.2,5.6),color=DARK)
a.text(2,7.4,"oceanic\nplate",fontsize=7.5,ha='center'); a.text(7.6,1.0,"subduction\nzone: deep\nquakes",fontsize=7.5,ha='center',color=DARK)
a.text(3.6,6.5,"trench",fontsize=7.5,ha='center',color=DARK)
a.text(8.4,7.2,"mountains,\nvolcanoes",fontsize=7.5,ha='center')
# divergent
a=axs[1]; a.set_title("Divergent",fontsize=10)
a.add_patch(Polygon([[0,5],[4.2,5],[4.6,6.2],[0,6.2]],fc=OCE,ec='k',lw=.8))
a.add_patch(Polygon([[10,5],[5.8,5],[5.4,6.2],[10,6.2]],fc=OCE,ec='k',lw=.8))
a.add_patch(Polygon([[0,5],[10,5],[10,1],[0,1]],fc=MANT,ec='none',zorder=0))
a.add_patch(Polygon([[4.2,5],[5.8,5],[5.6,1],[4.4,1]],fc="#E8863A",ec='none',zorder=1))
a.add_patch(Polygon([[4.2,5],[4.6,6.2],[5,6.6],[5.4,6.2],[5.8,5]],fc=RED,ec='k',lw=.8))
arrow(a,(4.2,7.8),(1.8,7.8),color=DARK); arrow(a,(5.8,7.8),(8.2,7.8),color=DARK)
a.text(5,3,"magma\nrises",fontsize=7.5,ha='center'); a.text(5,8.5,"ridge / rift: new crust",fontsize=7.5,ha='center')
a.text(5,0.2,"seafloor spreading, rift valleys,\nshallow quakes",fontsize=7.5,ha='center',color=DARK)
# transform
a=axs[2]; a.set_title("Transform (map view)",fontsize=10)
a.add_patch(Rectangle((0.5,5.2),9,3.6,fc=CON,ec='k',lw=.8)); a.add_patch(Rectangle((0.5,1.2),9,3.6,fc="#9DB58A",ec='k',lw=.8))
a.plot([0.5,9.5],[5,5],color=RED,lw=2.2,ls='--')
arrow(a,(2.5,7.0),(7.5,7.0),color=DARK,lw=2); arrow(a,(7.5,3.0),(2.5,3.0),color=DARK,lw=2)
a.text(5,8.2,"plate A",fontsize=8,ha='center'); a.text(5,1.8,"plate B",fontsize=8,ha='center')
a.text(5,5.15,"fault: locked, then slips",fontsize=7.5,ha='center',va='bottom',color=RED,backgroundcolor='white')
a.text(5,0.1,"earthquakes; crust not\ncreated or destroyed",fontsize=7.5,ha='center',color=DARK)
fig.tight_layout(); save(fig,OUT+'U4_plate_boundaries.png')

# ---------- Fig 4.2 soil horizons ----------
fig,ax=plt.subplots(figsize=(6.2,4.4)); ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis('off')
hz=[("O","#2B1D14",8.6,10,"Organic: leaf litter and humus; decomposing material"),
    ("A","#5A3B26",7.0,8.6,"Topsoil: dark; humus mixed with minerals; most roots and life"),
    ("E","#C9B79C",5.7,7.0,"Eluviation zone: water leaches clay and\nminerals downward; pale (not always present)"),
    ("B","#B07A3E",4.0,5.7,"Subsoil: accumulates leached clay, iron, minerals; little organic matter"),
    ("C","#A89F8F",2.0,4.0,"Weathered parent material: broken rock fragments"),
    ("R","#6B6B6B",0.3,2.0,"Bedrock: unweathered solid rock")]
for n,c,y0,y1,d in hz:
    ax.add_patch(Rectangle((0.3,y0),3.0,y1-y0,fc=c,ec='k',lw=.8))
    ax.text(1.8,(y0+y1)/2,n,color='white' if n in "OARB" else 'black',fontsize=14,fontweight='bold',ha='center',va='center')
    ax.text(3.6,(y0+y1)/2,d.replace("; ",";\n",1) if len(d)>55 and "\n" not in d else d,fontsize=8.2,va='center',ha='left')
rng=np.random.default_rng(3)
for _ in range(40):
    ax.plot(rng.uniform(.45,3.15),rng.uniform(2.1,3.9),'o',ms=rng.uniform(2,5),color="#7d7468",mec='k',mew=.3)
arrow(ax,(0.1,9.6),(0.1,0.6),color=GREY); ax.text(-0.15,5,"depth",rotation=90,va='center',fontsize=8,color=GREY)
ax.annotate("",xy=(9.9,5.0),xytext=(9.9,8.8),arrowprops=dict(arrowstyle='-|>',color=BLUE,lw=1.5))
ax.text(9.9,4.1,"infiltrating\nwater",fontsize=7.5,ha='center',va='top',color=BLUE)
ax.text(5.2,.1,"",fontsize=7)
fig.tight_layout(); save(fig,OUT+'U4_soil_horizons.png')

# ---------- Fig 4.3 atmosphere ----------
fig,(ax,ax2)=plt.subplots(1,2,figsize=(6.4,4.6),gridspec_kw={'width_ratios':[1.1,1.3]})
alt=[0,12,20,50,85,120]; T=[15,-57,-57,-3,-90,90]  # schematic
ax.plot(T,alt,color=RED,lw=2.2)
ax.set_xlabel("Temperature (°C), schematic"); ax.set_ylabel("Altitude (km)")
ax.set_ylim(0,125); ax.set_xlim(-110,120)
for y in (12,50,85):
    ax.axhline(y,color=GREY,ls=':',lw=.9)
ax.axhspan(15,35,xmin=0,xmax=1,color=SKY,alpha=.35); ax.text(60,25,"ozone\nlayer",fontsize=7.5,ha='center',color=BLUE)
ax.spines['top'].set_visible(False)
ax2.set_xlim(0,12.5); ax2.set_ylim(0,125); ax2.axis('off')
L=[("Exosphere",105,125,"#E6EAF2","above ~600 km; fades into space"),
   ("Thermosphere",85,105,"#D5DDEC","absorbs X-rays, UV; hot; auroras"),
   ("Mesosphere",50,85,"#C3D2E8","coldest layer; meteors burn up"),
   ("Stratosphere",12,50,"#A9C7E6","ozone absorbs UV; warms with height"),
   ("Troposphere",0,12,"#7FB0DD","weather; ~75% of mass")]
for n,y0,y1,c,d in L:
    ax2.add_patch(Rectangle((0,y0),10,y1-y0,fc=c,ec='k',lw=.6))
    ym=(y0+y1)/2
    if y1-y0>15:
        ax2.text(5,ym+3,n,ha='center',va='center',fontsize=8.6,fontweight='bold'); ax2.text(5,ym-3,d,ha='center',va='center',fontsize=7)
    elif y1-y0>=12:
        ax2.text(5,ym,n+": "+d,ha='center',va='center',fontsize=6.5)
    else:
        ax2.text(5,ym,n+": "+d,ha='center',va='center',fontsize=6.5,fontweight='bold')
ax2.text(10.2,12,"tropopause",fontsize=7,va='center'); ax2.text(10.2,50,"stratopause",fontsize=7,va='center'); ax2.text(10.2,85,"mesopause",fontsize=7,va='center')
ax.text(-105,118,"Upper layers compressed;\nthermosphere reaches ~600 km",fontsize=6.5,va='top')
fig.tight_layout(); save(fig,OUT+'U4_atmosphere_layers.png')

# ---------- Fig 4.4 circulation cells ----------
fig,ax=plt.subplots(figsize=(6.4,4.2)); ax.set_xlim(0,10.2); ax.set_ylim(0,6.2); ax.axis('off')
ax.add_patch(Rectangle((0.3,1.2),9.4,3.6,fc="#EEF4FA",ec='k',lw=.8))
for x,l in [(0.3,"0° Equator"),(3.43,"30° N"),(6.57,"60° N"),(9.7,"90° N")]:
    ax.plot([x,x],[1.2,4.8],color=GREY,ls=':',lw=.9); ax.text(x,.95,l,ha='center',va='top',fontsize=8.5,fontweight='bold')
def cell(x0,x1,c,cw=True):
    xm=(x0+x1)/2
    # surface arrow, aloft arrow, vertical arrows
    s,e=((x1,x0) if cw else (x0,x1))
    arrow(ax,(s-(s-e)*0.05,1.55),(e+(s-e)*0.05,1.55),color=c,lw=2)
    arrow(ax,(e+(s-e)*0.05,4.45),(s-(s-e)*0.05,4.45),color=c,lw=2)
cell(0.3,3.43,RED,True)   # surface flow toward equator (from 30 to 0)
for x,dirn in [(0.3,"up"),(3.43,"down")]:
    if dirn=="up": arrow(ax,(x+.03,1.7),(x+.03,4.3),color=RED,lw=2)
    else: arrow(ax,(x,4.3),(x,1.7),color=RED,lw=2)
# Ferrel: surface poleward 30->60, aloft equatorward
arrow(ax,(3.6,1.55),(6.4,1.55),color=GREEN,lw=2); arrow(ax,(6.4,4.45),(3.6,4.45),color=GREEN,lw=2)
arrow(ax,(3.43,4.3),(3.43,1.7),color=RED,lw=0.1)
arrow(ax,(6.57,1.7),(6.57,4.3),color=GREEN,lw=2)
# polar: surface equatorward 90->60, aloft poleward 60->90
arrow(ax,(9.6,1.55),(6.75,1.55),color=BLUE,lw=2); arrow(ax,(6.75,4.45),(9.6,4.45),color=BLUE,lw=2)
arrow(ax,(9.7,4.3),(9.7,1.7),color=BLUE,lw=2)
ax.text(1.9,3.0,"HADLEY\nCELL",ha='center',fontsize=10,color=RED,fontweight='bold')
ax.text(5.0,3.0,"FERREL\nCELL",ha='center',fontsize=10,color=GREEN,fontweight='bold')
ax.text(8.2,3.0,"POLAR\nCELL",ha='center',fontsize=10,color=BLUE,fontweight='bold')
ax.text(0.6,5.0,"rising air: ITCZ\nrain, low pressure",fontsize=7.5,va='bottom')
ax.text(3.43,5.0,"sinking air\ndeserts, high pressure",fontsize=7.5,va='bottom',ha='center')
ax.text(6.57,5.0,"rising air\nlow pressure, rain",fontsize=7.5,va='bottom',ha='center')
ax.text(9.7,5.0,"sinking air\nhigh pressure",fontsize=7.5,va='bottom',ha='right')
ax.text(1.9,1.35,"NE trade winds",fontsize=7.5,ha='center',va='bottom',style='italic')
ax.text(5.0,1.35,"prevailing westerlies (from SW)",fontsize=7.5,ha='center',va='bottom',style='italic')
ax.text(8.2,1.35,"polar easterlies (from NE)",fontsize=7.5,ha='center',va='bottom',style='italic')
ax.text(5,6.05,"Northern Hemisphere cross-section (Southern Hemisphere mirrors it); upper arrows = high-altitude flow",ha='center',fontsize=7.5,color=GREY)
ax.text(0.3,0.1,"Winds are named for the direction they come FROM. The Coriolis effect deflects moving air\nto the right in the Northern Hemisphere and to the left in the Southern.",fontsize=7.8,color=DARK)
fig.tight_layout(); save(fig,OUT+'U4_circulation_cells.png')

# ---------- Fig 4.5 ENSO ----------
fig,axs=plt.subplots(2,1,figsize=(6.4,5.8))
def cloud(a,x,y,txt):
    a.add_patch(Ellipse((x,y),1.7,.55,fc="white",ec=GREY)); a.add_patch(Ellipse((x-.5,y-.15),1.0,.4,fc="white",ec=GREY))
    a.add_patch(Ellipse((x,y-.05),1.6,.45,fc="white",ec='none'))
    a.text(x,y+.45,txt,fontsize=7.3,ha='center',va='bottom')
def pac(a,title,el):
    a.set_xlim(0,10); a.set_ylim(0,6.6); a.axis('off'); a.set_title(title,fontsize=10,loc='left')
    a.add_patch(Rectangle((0.4,0.4),9.2,3.2,fc="#9CC5E3",ec='k',lw=.8))
    xs=np.linspace(0.4,9.6,50); fr=(xs-0.4)/9.2
    th=(2.0+1.0*fr) if not el else (2.45+0.2*fr)
    a.fill_between(xs,th,3.6,color="#F0A35E",alpha=.8,lw=0)
    a.plot(xs,th,color=RED,lw=2,ls='--'); a.text(5,th[25]-0.4,"thermocline (boundary of warm and cold water)",fontsize=7.3,color=RED,ha='center')
    a.add_patch(Polygon([[0,3.6],[0.4,3.6],[0.4,0.4],[0,0.4]],fc=SAND,ec='k',lw=.6))
    a.add_patch(Polygon([[9.6,3.6],[10,3.6],[10,0.4],[9.6,0.4]],fc=SAND,ec='k',lw=.6))
    a.text(0.4,0.05,"WEST (Asia, Australia)",fontsize=7,color=GREY); a.text(9.6,0.05,"EAST (South America)",fontsize=7,color=GREY,ha='right')
    if not el:
        arrow(a,(8.8,4.0),(1.6,4.0),color=DARK,lw=2.2); a.text(5.2,4.1,"strong easterly trade winds",fontsize=8,ha='center')
        a.text(2.2,2.95,"deep warm pool",fontsize=7.5,ha='center')
        a.text(8.3,3.1,"cool surface",fontsize=7.2,ha='center')
        arrow(a,(8.6,0.9),(8.6,2.7),color=BLUE,lw=2); a.text(8.3,1.0,"upwelling of cold,\nnutrient-rich water",fontsize=7,ha='right',color=DARK)
        cloud(a,2.0,5.2,"warm, moist air rises: heavy rain")
        a.text(8.3,5.45,"air sinks: dry",fontsize=7.3,ha='center')
    else:
        arrow(a,(7.6,4.0),(5.4,4.0),color=DARK,lw=1.2); a.text(6.6,4.1,"weak trade winds",fontsize=8,ha='center')
        arrow(a,(2.4,3.25),(8.0,3.25),color=ORANGE,lw=2.2); a.text(4.6,2.85,"warm water spreads east",fontsize=7.3,ha='center')
        a.text(8.3,1.2,"upwelling weak\nor stopped",fontsize=7,ha='center',color=DARK)
        cloud(a,6.8,5.2,"rain shifts to central and eastern Pacific")
        a.text(1.8,5.45,"drier: drought risk",fontsize=7.3,ha='center')
pac(axs[0],"Neutral (normal) conditions",False)
pac(axs[1],"El Niño: warm phase",True)
fig.tight_layout(); save(fig,OUT+'U4_enso.png')
