import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
OUT='/home/user/OmniRouter/apes_project/content/book1/figs/'

# ---- Fig 2.1 fronts ----
fig,axs=plt.subplots(2,1,figsize=(6.2,5.4))
WARM="#F3C9A8"; COLD="#A9CBE8"
def cloud(a,x,y,s=1.0):
    for dx,dy,r in [(0,0,.7),(.8,.2,.9),(1.7,0,.7),(.9,-.2,.8)]:
        a.add_patch(Circle((x+dx*s,y+dy*s),r*s*0.55,fc="#EEF0F4",ec="#8A8A8A",lw=.7,zorder=4))
def rain(a,xs,y0,y1):
    for x in xs: a.plot([x,x-.15],[y0,y1],color=BLUE,lw=1,zorder=5)
# cold front: moves right; steep wedge
a=axs[0]; a.set_xlim(0,12); a.set_ylim(0,6); a.axis('off')
a.set_title("Cold front: cold air pushes under warm air (front moves →)",fontsize=10)
a.add_patch(Rectangle((0,0),12,.25,fc="#8B7355",ec='none'))
a.add_patch(Polygon([[0,.25],[6.0,.25],[6.9,2.2],[7.6,4.4],[8.2,5.6],[0,5.6]],fc=COLD,ec='none'))
a.add_patch(Polygon([[6.0,.25],[12,.25],[12,5.6],[8.2,5.6],[7.6,4.4],[6.9,2.2]],fc=WARM,ec='none'))
a.plot([6.0,6.9,7.6,8.2],[.25,2.2,4.4,5.6],color=BLUE,lw=2.2,zorder=3)
cloud(a,6.8,4.5,.9); rain(a,[5.2,5.7,6.2],2.3,0.5)
a.text(2.8,3.0,"cold, dense air\n(moving in)",ha='center',fontsize=9)
a.text(10.0,3.0,"warm, moist air\nforced up quickly",ha='center',fontsize=9)
a.text(5.2,2.5,"",fontsize=8)
a.text(10,0.7,"steep slope (≈1:50)\nshort, intense storms,\nthen cooler and clear",ha='center',fontsize=8,color=DARK)
arrow(a,(3.2,1.0),(5.0,1.0),color=BLUE); arrow(a,(11.6,4.8),(10.0,4.8),color=DARK)
# warm front
a=axs[1]; a.set_xlim(0,12); a.set_ylim(0,6); a.axis('off')
a.set_title("Warm front: warm air glides up over cold air (front moves →)",fontsize=10)
a.add_patch(Rectangle((0,0),12,.25,fc="#8B7355",ec='none'))
a.add_patch(Polygon([[4.2,.25],[12,.25],[12,2.0],[8.0,1.2]],fc=COLD,ec='none'))
a.add_patch(Polygon([[0,.25],[4.2,.25],[0,.25]],fc=COLD,ec='none'))
a.add_patch(Polygon([[0,.25],[4.2,.25],[8.0,1.2],[12,2.0],[12,5.6],[0,5.6]],fc=WARM,ec='none'))
a.add_patch(Polygon([[4.2,.25],[12,.25],[12,2.0],[8.0,1.2]],fc=COLD,ec='none'))
# cold air is ahead (right); warm wedge rides over it
a.plot([4.2,8.0,12],[.25,1.2,2.0],color=RED,lw=2.2,zorder=3)
cloud(a,6.5,2.9,.9); cloud(a,9.2,3.5,.9)
rain(a,[7.6,8.1,8.6,9.1],2.5,1.2)
a.text(2.2,3.2,"warm, moist air\nrises gently",ha='center',fontsize=9)
a.text(11.0,0.55,"cold air\nahead",ha='center',fontsize=8.5)
a.text(2.2,0.9,"gentle slope (≈1:200)\nwide belt of steady rain\nahead of the front",ha='left',fontsize=8,color=DARK) if False else None
a.text(6.0,5.0,"gentle slope (≈1:200): layered clouds, long steady rain, then warmer and humid",ha='center',fontsize=8,color=DARK)
arrow(a,(2.0,1.2),(3.6,1.2),color=RED)
fig.tight_layout(); save(fig,OUT+'C2_fronts.png')

# ---- Fig 2.2 rain shadow ----
fig,ax=plt.subplots(figsize=(6.2,3.3)); ax.set_xlim(0,12); ax.set_ylim(0,6.5); ax.axis('off')
ax.add_patch(Rectangle((0,0),1.4,.9,fc=BLUE,ec='none'))
ax.text(.7,.35,"ocean",ha='center',fontsize=8,color='white')
ax.add_patch(Polygon([[1.4,.9],[4.0,.9],[6.0,4.0],[8.0,.9],[12,.9],[12,0],[1.4,0]],fc="#9C8A6A",ec='k',lw=.8))
ax.add_patch(Polygon([[4.0,.9],[6.0,4.0],[8.0,.9]],fc="#8B7355",ec='k',lw=.8))
ax.add_patch(Polygon([[4.9,2.5],[6.0,4.0],[6.45,3.3],[5.6,2.2]],fc="white",ec='none',alpha=.0))
# climate patches
ax.add_patch(Rectangle((1.4,.9),2.6,.15,fc=GREEN,ec='none')); ax.add_patch(Rectangle((8.0,.9),4,.15,fc=SAND,ec='none'))
ax.add_patch(Polygon([[3.9,1.1],[4.9,2.6],[5.4,2.6],[4.4,1.1]],fc=GREEN,ec='none',alpha=.0))
for x in [2.0,2.6,3.2,3.7]: ax.add_patch(Polygon([[x,1.05],[x+.15,1.5],[x+.3,1.05]],fc=GREEN,ec='none'))
for x in [9.0,10.2,11.3]: ax.plot([x,x+.25],[1.05,1.05],color=BROWN,lw=2)
# air path
xs=np.array([1.6,3.0,4.5,6.0,7.5,9.0,10.8]); ys=np.array([1.5,2.4,3.6,4.6,3.6,2.5,1.6])
from scipy.interpolate import make_interp_spline
xx=np.linspace(1.6,10.8,60); yy=make_interp_spline(xs,ys,k=3)(xx)
ax.plot(xx[:34],yy[:34],color=DARK,lw=1.8); ax.plot(xx[33:],yy[33:],color=RED,lw=1.8)
ax.annotate("",xy=(xx[-1],yy[-1]),xytext=(xx[-4],yy[-4]),arrowprops=dict(arrowstyle="-|>",color=RED,lw=1.8))
for dx,dy,r in [(3.6,4.4,.5),(4.2,4.7,.6),(4.8,4.3,.5)]: ax.add_patch(Circle((dx-1.6,dy-.5),r*.7,fc="#EEF0F4",ec="#8A8A8A",lw=.7,zorder=4))
for x in [2.4,2.8,3.2,3.6]: ax.plot([x,x-.12],[2.7,1.5],color=BLUE,lw=1.2)
ax.text(1.0,5.9,"WINDWARD side",fontsize=9.5,fontweight='bold',color=DARK)
ax.text(7.2,5.9,"LEEWARD side (rain shadow)",fontsize=9.5,fontweight='bold',color=RED)
ax.text(1.0,5.35,"moist air rises, cools,\nvapor condenses: heavy rain",fontsize=8,va='top')
ax.text(7.2,5.35,"dry air sinks, compresses,\nwarms: clouds clear, dry land",fontsize=8,va='top')
ax.text(6.0,.35,"prevailing wind →",ha='center',fontsize=8.5,color='white')
ax.text(3.0,.0,"",fontsize=1)
ax.text(2.7,-.35,"forest / green",ha='center',fontsize=8,color=GREEN); ax.text(10.0,-.35,"semi-arid / desert",ha='center',fontsize=8,color=BROWN)
save(fig,OUT+'C2_rain_shadow.png')

# ---- Fig 2.3 climatograms ----
months=list("JFMAMJJASOND")
A_p=[210,170,150,90,60,25,10,12,40,110,180,220]; A_t=[8,9,10,12,14,16,18,18,16,13,10,8]
B_p=[25,25,35,40,55,70,75,65,50,40,30,28]; B_t=[-14,-11,-3,6,13,18,21,19,13,6,-3,-10]
fig,axs=plt.subplots(1,2,figsize=(6.4,3.0))
for a,p,t,ttl in [(axs[0],A_p,A_t,"City A"),(axs[1],B_p,B_t,"City B")]:
    a.bar(range(12),p,color=SKY,ec=BLUE,lw=.6); a.set_ylim(0,250); a.set_xticks(range(12)); a.set_xticklabels(months,fontsize=8)
    a.set_title(ttl,fontsize=10); a.spines['right'].set_visible(True)
    a2=a.twinx(); a2.plot(range(12),t,color=RED,lw=2,marker='o',ms=3); a2.set_ylim(-20,30); a2.spines['top'].set_visible(False)
    a.set_ylabel("Precipitation (mm/month)",fontsize=8,color=BLUE) if a is axs[0] else None
    a2.set_ylabel("Mean temperature (°C)",fontsize=8,color=RED) if a is axs[1] else None
    a.tick_params(labelsize=8); a2.tick_params(labelsize=8)
fig.tight_layout(); save(fig,OUT+'C2_climatograms.png')

# ---- Fig 2.4 hurricane cross-section ----
fig,ax=plt.subplots(figsize=(6.2,3.6)); ax.set_xlim(-10,10); ax.set_ylim(-1.3,8); ax.axis('off')
ax.add_patch(Rectangle((-10,-1.3),20,1.3,fc="#7FA9C9",ec='none'))
ax.plot([-10,10],[0,0],color='k',lw=.8)
# eye wall (tilted)
for s in (-1,1):
    ax.add_patch(Polygon([[s*1.0,0],[s*1.9,0],[s*3.2,7.0],[s*2.3,7.0]],fc="#C8CCD6",ec="#555",lw=.9,zorder=3))
# outer rain bands
for s in (-1,1):
    for x0 in (4.2,7.0):
        ax.add_patch(Polygon([[s*x0,0],[s*(x0+.8),0],[s*(x0+1.2),3.2],[s*(x0+.5),3.2]],fc="#DCDFE6",ec="#777",lw=.7,zorder=2))
# anvil
ax.add_patch(Polygon([[-9.5,7.0],[9.5,7.0],[8.0,7.7],[-8.0,7.7]],fc="#E6E8EE",ec="#777",lw=.7))
# inflow / outflow
arrow(ax,(-9.8,0.45),(-3.6,0.45),color=DARK,lw=1.6); arrow(ax,(9.8,0.45),(3.6,0.45),color=DARK,lw=1.6)
ax.annotate("",xy=(-9.5,7.9),xytext=(-3.0,7.9),arrowprops=dict(arrowstyle="-|>",color=RED,lw=1.6))
ax.annotate("",xy=(9.5,7.9),xytext=(3.0,7.9),arrowprops=dict(arrowstyle="-|>",color=RED,lw=1.6))
ax.annotate("",xy=(0,0.2),xytext=(0,6.4),arrowprops=dict(arrowstyle="-|>",color=BLUE,lw=1.6))
ax.text(0,3.3,"EYE\ncalm, clear,\nsinking air",ha='center',fontsize=8.5,color=BLUE,fontweight='bold',bbox=dict(fc="white",ec="none",pad=1.5),zorder=9)
ax.text(-2.55,4.2,"eyewall:\nstrongest winds,\nheaviest rain",ha='center',fontsize=7.5,rotation=0) if False else None
ax.text(5.6,5.4,"eyewall: strongest\nwinds, heaviest rain",ha='center',fontsize=8,color=DARK)
ax.text(-6.7,4.4,"spiral rain\nbands",ha='center',fontsize=8)
ax.text(9.9,-0.2,"not to scale",ha="right",fontsize=7,color=GREY,va="top")
ax.text(-6.5,1.3,"surface winds spiral in\n(counterclockwise in N. Hemisphere)",ha='center',fontsize=7.5,color=DARK,bbox=dict(fc="white",ec="none",pad=1.5),zorder=9)
ax.text(0,8.25,"outflow aloft: air spreads out and cools",ha='center',fontsize=8,color=RED)
ax.text(0,-0.75,"warm ocean (≥ 26.5°C) supplies heat and water vapor",ha='center',fontsize=8.5,color='white')
ax.set_ylim(-1.3,8.7)
save(fig,OUT+'C2_hurricane.png')
print("ok")
