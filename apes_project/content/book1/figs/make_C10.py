import sys, os
sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D=os.path.dirname(os.path.abspath(__file__))

# ---------- 1 pathogen routes ----------
fig,ax=canvas(6.4,4.2)
box(ax,0.02,0.40,0.22,0.20,"Infected person\nor animal\n(reservoir)",fc=LIGHT,ec=RED,fs=9,bold=True)
box(ax,0.78,0.40,0.20,0.20,"New host\nexposed and\ninfected",fc=LIGHT,ec=RED,fs=9,bold=True)
routes=[(0.80,"Water: cholera, dysentery",SKY,"Fix: sewage treatment, safe water"),
        (0.57,"Air (droplets): TB, SARS",SAND,"Fix: isolate the sick, ventilation"),
        (0.34,"Vector bite: malaria, West Nile, Zika",SAND,"Fix: control mosquitoes, nets"),
        (0.11,"Animal contact: plague (fleas), MERS",SAND,"Fix: rodent control, safe handling")]
for y,t,c,fix in routes:
    box(ax,0.31,y-0.07,0.40,0.18,"",fc=c,ec=DARK)
    ax.text(0.51,y+0.065,t,ha="center",va="center",fontsize=8)
    ax.text(0.51,y-0.03,fix,ha="center",va="center",fontsize=7.5,color=GREEN,style="italic")
    arrow(ax,(0.24,0.50),(0.31,y+0.02),color=DARK)
    arrow(ax,(0.71,y+0.02),(0.78,0.50),color=DARK)
ax.set_ylim(0,1.0)
ax.text(0.5,1.0,"Break any route and the cycle stops",ha="center",va="top",fontsize=11,fontweight="bold")
save(fig,D+"/C10_pathogen_routes.png")

# ---------- 2 landfill liner cross-section ----------
fig,ax=canvas(6.4,4.4,(0,10),(0,7.6))
ax.add_patch(Rectangle((0,0),10,2.2,fc="#C9B68E",ec="none"))          # native soil
ax.add_patch(Rectangle((0,0),10,0.9,fc="#A8A8A8",ec="none"))          # bedrock-ish / aquifer zone
ax.add_patch(Rectangle((0,0),10,0.9,fc=SKY,ec="none",alpha=0.8))
ax.text(9.8,0.35,"Groundwater (aquifer)",ha="right",fontsize=8,color=DARK)
ax.add_patch(Rectangle((1.5,2.2),7,0.35,fc="#7A5A3A",ec="none"))      # compacted clay
ax.add_patch(Rectangle((1.5,2.55),7,0.08,fc="black",ec="none"))       # geomembrane
ax.add_patch(Rectangle((1.5,2.63),7,0.30,fc="#E0D6A8",ec="none"))     # drainage gravel
ax.add_patch(Rectangle((1.5,2.93),7,2.1,fc="#8F8F8F",ec="none"))      # waste
ax.add_patch(Polygon([(1.5,5.03),(8.5,5.03),(7.6,5.45),(2.4,5.45)],fc="#B5936B",ec="none")) # daily cover/cap
ax.add_patch(Polygon([(1.5,5.45),(8.5,5.45),(7.6,5.8),(2.4,5.8)],fc=GREEN,ec="none",alpha=0.0))
ax.add_patch(Rectangle((2.4,5.45),5.2,0.30,fc=GREEN,ec="none"))      # vegetated cap
# gas well
ax.plot([5,5],[3.2,6.2],color=DARK,lw=3)
ax.text(5.2,6.2,"Gas collection pipe (methane\nburned or used for energy)",fontsize=8,va="center",ha="left")
# leachate pipe and sump
ax.plot([1.7,8.3],[2.78,2.78],color=BLUE,lw=3,ls=(0,(1,0.7)))
ax.annotate("",xy=(9.4,2.0),xytext=(8.3,2.78),arrowprops=dict(arrowstyle="-|>",color=BLUE,lw=1.5))
ax.text(9.3,1.75,"Leachate to\ntreatment",ha="center",fontsize=8,color=BLUE,va="top")
# monitoring well
ax.plot([0.8,0.8],[0.6,3.3],color=ORANGE,lw=3)
ax.text(0.8,3.45,"Monitoring\nwell",ha="center",fontsize=8,color=ORANGE,va="bottom")
# labels
def lab(x,y,t,tx,ty):
    ax.annotate(t,xy=(x,y),xytext=(tx,ty),fontsize=8,arrowprops=dict(arrowstyle="-",color=GREY,lw=0.8),va="center")
lab(7.2,5.6,"Vegetated cap\n(seals out rain)",8.2,6.7)
lab(8.0,4.0,"Compacted waste\nin cells, daily\nsoil cover",8.7,4.0)
lab(6.5,2.78,"Drainage layer and\nleachate pipe",5.0,1.75)
lab(3.0,2.59,"Plastic geomembrane",1.3,1.75)
lab(3.5,2.38,"Compacted clay liner",2.4,1.15)
ax.text(5,0.12,"",fontsize=8)
ax.text(0.1,7.55,"Cross-section of a modern sanitary landfill",fontsize=11,fontweight="bold",va="top")
save(fig,D+"/C10_landfill_liner.png")

# ---------- 3 cleanup methods ----------
fig,ax=canvas(6.4,4.3,(0,10),(0,7))
ax.add_patch(Rectangle((0,0),10,3.2,fc="#C9B68E",ec="none"))
ax.add_patch(Rectangle((0,0),10,1.5,fc=SKY,ec="none",alpha=0.7))
ax.plot([0,10],[1.5,1.5],color=BLUE,lw=1.2,ls="--")
ax.text(9.9,1.58,"water table",ha="right",fontsize=7.5,color=BLUE)
ax.add_patch(Ellipse((2.4,0.85),3.0,0.8,fc=ORANGE,ec=DARK,alpha=0.75))
ax.text(2.4,0.85,"contaminant plume",ha="center",va="center",fontsize=7.5)
ax.annotate("",xy=(4.0,0.2),xytext=(0.3,0.2),arrowprops=dict(arrowstyle="-|>",color=DARK,lw=1.2))
ax.text(5.3,0.12,"groundwater flow",fontsize=7.5)
ax.annotate("",xy=(5.2,0.2),xytext=(4.1,0.2),arrowprops=dict(arrowstyle="-|>",color=DARK,lw=1.2))
ax.plot([4.2,4.2],[0.4,3.9],color=DARK,lw=3)
ax.add_patch(Rectangle((3.9,3.9),0.6,0.4,fc=GREY,ec=DARK))
ax.text(3.8,4.1,"Extraction well\nwith pump",ha="right",fontsize=8,va="center")
box(ax,4.8,3.95,2.0,0.95,"Treatment unit\n(carbon filter,\nair stripper)",fc=LIGHT,ec=RED,fs=7.5)
arrow(ax,(4.5,4.1),(4.8,4.25),color=BLUE)
ax.text(5.8,3.55,"clean water returned\nor discharged",fontsize=7.5,color=BLUE,va="center",ha="center")
ax.text(4.5,2.35,"contaminated water\npumped up",fontsize=7.5,color=DARK)
for x in (7.7,8.6,9.5):
    ax.plot([x,x],[3.2,4.3],color=BROWN,lw=3)
    ax.add_patch(Circle((x,4.75),0.45,fc=GREEN,ec="none"))
    ax.plot([x,x-0.25,x-0.4],[3.2,2.6,2.2],color=BROWN,lw=1); ax.plot([x,x+0.25,x+0.4],[3.2,2.6,2.2],color=BROWN,lw=1)
ax.add_patch(Ellipse((8.6,2.75),2.9,0.8,fc=ORANGE,ec="none",alpha=0.35))
ax.text(8.2,5.6,"Phytoremediation: roots take up\nor break down shallow contaminants",ha="center",fontsize=7.5,va="bottom")
ax.text(0.2,2.5,"Bioremediation: microbes\n(given oxygen and nutrients)\nbreak down the plume",ha="left",fontsize=7.5,color=DARK,va="center")
ax.annotate("",xy=(1.6,1.3),xytext=(1.4,2.0),arrowprops=dict(arrowstyle="-|>",color=DARK,lw=1))
ax.text(0.1,6.9,"Three ways to clean a contaminated site",fontsize=11,fontweight="bold",va="top")
save(fig,D+"/C10_cleanup_methods.png")

# ---------- 4 half-life ----------
fig,(a,b)=plt.subplots(1,2,figsize=(6.4,3.2),gridspec_kw={"width_ratios":[1.1,1]})
n=np.linspace(0,10,300); a.plot(n,100*0.5**n,color=RED,lw=2.4)
for k in range(0,8):
    a.plot(k,100*0.5**k,"o",color=DARK,ms=4)
for k,dy in ((1,6),(2,6),(3,6)):
    a.text(k+0.15,100*0.5**k+dy,f"{100*0.5**k:g}%",fontsize=7.5)
a.set_xlabel("Number of half-lives elapsed"); a.set_ylabel("Radioactive material left (%)")
a.set_title("Each half-life halves it",loc="left",fontsize=10); a.set_xlim(0,10); a.set_ylim(0,105)
a.text(6.2,22,"after 10 half-lives\nabout 0.1% remains",fontsize=8,color=DARK)
iso=["Cs-137","Sr-90","Pu-239","Tc-99"]; hl=[30.1,28.8,24100,211000]
t10=[10*h for h in hl]
yy=np.arange(len(iso))
b.barh(yy,t10,color=[BLUE,BLUE,ORANGE,ORANGE]); b.set_xscale("log")
b.set_yticks(yy); b.set_yticklabels(iso); b.invert_yaxis()
for y,h,t in zip(yy,hl,t10):
    b.text(t*1.25,y,f"{h:,.0f} yr half-life" if h>=100 else f"{h:.1f} yr half-life",va="center",fontsize=7.5)
b.set_xlim(100,2e8); b.set_xlabel("Time for 10 half-lives (years, log scale)")
b.set_title("Time to decay to ~0.1%",loc="left",fontsize=10)
fig.tight_layout()
save(fig,D+"/C10_half_life.png")

# ---------- 5 externality ----------
fig,ax=plt.subplots(figsize=(6.2,3.7))
Q=np.linspace(0,60,100)
ax.plot(Q,100-Q,color=GREEN,lw=2.3,label="Demand (marginal benefit)")
ax.plot(Q,20+Q,color=BLUE,lw=2.3,label="Private supply (producer's cost)")
ax.plot(Q,40+Q,color=RED,lw=2.3,label="Social cost (private + external)")
ax.plot([40],[60],"o",color=BLUE); ax.plot([30],[70],"o",color=RED)
ax.vlines(40,0,60,color=BLUE,ls=":"); ax.vlines(30,0,70,color=RED,ls=":")
ax.text(40.8,5,"Market output\nQ = 40",fontsize=8,color=BLUE)
ax.text(24.5,5,"Best output\nfor society\nQ = 30",fontsize=8,color=RED,ha="right")
ax.annotate("",xy=(14,34),xytext=(14,54),arrowprops=dict(arrowstyle="<->",color=GREY))
ax.text(13,38,"external cost\n$20 per unit",fontsize=8,color=GREY,va="center",ha="right")
ax.set_xlim(0,60); ax.set_ylim(0,140)
ax.set_xlabel("Quantity (thousand units per year)"); ax.set_ylabel("Price or cost ($ per unit)")
ax.legend(loc="upper left",fontsize=8,frameon=False)
ax.set_title("An unpriced pollution cost makes the market produce too much",loc="left",fontsize=10)
save(fig,D+"/C10_externality.png")

# ---------- 6 resilience ----------
fig,axs=plt.subplots(1,2,figsize=(6.4,3.2),sharey=True)
x=np.linspace(-2.0,2.0,600)
def pot(x,w): return (x**2-1)**2*w + 0.25*x
for k,(ax_,w,ttl) in enumerate(((axs[0],1.0,"Resilient: deep basin"),(axs[1],0.35,"Less resilient: shallow basin"))):
    y=pot(x,w); ax_.plot(x,y,color=DARK,lw=2.2)
    xl=x[x<0][np.argmin(y[x<0])]; xr=x[x>0.5][np.argmin(y[x>0.5])]; xt=x[(x>-0.5)&(x<0.6)][np.argmax(y[(x>-0.5)&(x<0.6)])]
    yl=pot(xl,w); yt=pot(xt,w); yr=pot(xr,w)
    ax_.plot(xl,yl+0.09,"o",color=RED,ms=11)
    ax_.set_title(ttl,loc="left",fontsize=10); ax_.set_xticks([]); ax_.set_yticks([])
    ax_.spines["left"].set_visible(False); ax_.spines["bottom"].set_visible(False)
    ax_.text(xl,-0.75,"healthy\nstate",ha="center",fontsize=8,color=GREEN,va="center")
    ax_.text(xr,-0.75,"degraded\nstate",ha="center",fontsize=8,color=GREY,va="center")
    ax_.text(xt,yt+0.12,"tipping point",fontsize=7.5,ha="center",color=DARK)
    ax_.annotate("",xy=(xl+0.55,yl+0.65),xytext=(xl-0.1,yl+0.25),arrowprops=dict(arrowstyle="-|>",color=ORANGE,lw=2))
    axs[0].set_ylim(-1.1,2.5)
axs[0].annotate("",xy=(-0.9,0.45),xytext=(-0.2,0.95),arrowprops=dict(arrowstyle="-|>",color=GREEN,lw=1.4,ls="--",connectionstyle="arc3,rad=0.3"))
axs[0].text(0,2.3,"Same push: system recovers",ha="center",fontsize=8,color=GREEN)
axs[1].annotate("",xy=(xr-0.05,pot(xr,0.35)+0.2),xytext=(xl+0.45,pot(xl,0.35)+1.2),arrowprops=dict(arrowstyle="-|>",color=RED,lw=1.4,ls="--",connectionstyle="arc3,rad=-0.4"))
axs[1].text(0,2.3,"Same push: system tips over",ha="center",fontsize=8,color=RED)
fig.text(0.5,0.0,"Orange arrow = a disturbance (drought, fire, pollution pulse); dashed arrow = what happens next",ha="center",fontsize=8,color=DARK)
fig.tight_layout(rect=(0,0.05,1,1))
save(fig,D+"/C10_resilience.png")
print("ok")
