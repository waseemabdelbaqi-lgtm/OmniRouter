import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book2/figs/'

# 1 island equilibrium model
fig,ax=plt.subplots(figsize=(6,3.8))
S=np.linspace(0,60,100)
ax.plot(S,24-0.4*S,color=BLUE,lw=2,label="Immigration, near island")
ax.plot(S,12-0.2*S,color=GREEN,lw=2,label="Immigration, far island")
ax.plot(S,0.2*S,color=RED,lw=2,ls="--",label="Extinction, large island")
ax.plot(S,0.6*S,color=ORANGE,lw=2,ls="--",label="Extinction, small island")
ax.set_xlim(0,60); ax.set_ylim(0,36)
ax.set_xticks(range(0,61,5)); ax.set_yticks(range(0,36,5))
ax.grid(True,color="#ddd",lw=0.6)
ax.set_xlabel("Number of species on the island (mainland pool = 60)")
ax.set_ylabel("Rate (species per year)")
ax.legend(fontsize=8,loc="upper left",frameon=True,ncol=2)
save(fig,D+"QB_U2_island_model.png")

# 2 tolerance curves
fig,ax=plt.subplots(figsize=(6,3.4))
T=np.linspace(0,40,400)
def curve(lo,opt,hi):
    y=np.zeros_like(T)
    for i,t in enumerate(T):
        if lo<t<opt: y[i]=np.sin((t-lo)/(opt-lo)*np.pi/2)**1.2
        elif opt<=t<hi: y[i]=np.cos((t-opt)/(hi-opt)*np.pi/2)**1.2
    return y
ax.plot(T,curve(16,21,26),color=RED,lw=2.2,label="Species P")
ax.plot(T,curve(6,20,34),color=BLUE,lw=2.2,label="Species Q")
ax.plot(T,curve(24,31,38),color=GREEN,lw=2.2,label="Species R")
ax.set_xlabel("Water temperature (°C)"); ax.set_ylabel("Relative growth rate")
ax.set_xlim(0,40); ax.set_ylim(0,1.1); ax.set_xticks(range(0,41,5))
ax.grid(True,color="#e5e5e5",lw=0.6); ax.legend(fontsize=9,frameon=False)
save(fig,D+"QB_U2_tolerance.png")

# 3 shell thickness distributions
fig,ax=plt.subplots(figsize=(6,3.2))
x=np.linspace(2,8,300)
g=lambda m,s: np.exp(-0.5*((x-m)/s)**2)/(s*np.sqrt(2*np.pi))
ax.fill_between(x,g(4.0,0.6),color=SKY,alpha=0.7,label="Before crabs arrived")
ax.fill_between(x,g(5.2,0.6),color=ORANGE,alpha=0.55,label="25 generations after crabs arrived")
ax.plot(x,g(4.0,0.6),color=BLUE); ax.plot(x,g(5.2,0.6),color=BROWN)
ax.set_xlabel("Shell thickness (mm)"); ax.set_ylabel("Proportion of snails")
ax.set_yticks([]); ax.set_ylim(0,0.95); ax.legend(fontsize=8.5,frameon=False,loc="upper left")
save(fig,D+"QB_U2_shell.png")

# 4 fragmentation schematic
fig,axs=plt.subplots(1,2,figsize=(6.2,3.0))
for a in axs: a.set_xlim(0,10); a.set_ylim(0,10); a.set_aspect("equal"); a.axis("off")
axs[0].add_patch(Rectangle((0,0),10,10,fc=GREEN,ec="#1f4d2b",lw=1.5,alpha=0.85))
axs[0].text(5,5,"Intact forest\n100 ha",ha="center",va="center",color="white",fontsize=10,fontweight="bold")
axs[0].set_title("Before",fontsize=10,pad=14)
axs[1].add_patch(Rectangle((0,0),10,10,fc=SAND,ec="#8a7340",lw=1.0,alpha=0.5))
for (x0,y0) in [(0.25,0.25),(5.15,0.25),(0.25,5.15),(5.15,5.15)]:
    axs[1].add_patch(Rectangle((x0,y0),4.6,4.6,fc=GREEN,ec="#1f4d2b",lw=1.5,alpha=0.85))
    axs[1].text(x0+2.3,y0+2.3,"25 ha",ha="center",va="center",color="white",fontsize=10,fontweight="bold")
axs[1].set_title("After (roads and fields\nbetween patches)",fontsize=10)
axs[0].text(5,-0.9,"Schematic, not to scale",ha="center",va="top",fontsize=8.5,color=GREY)
axs[1].text(5,-0.9,"Tan = roads and fields",ha="center",va="top",fontsize=8.5,color=GREY)
save(fig,D+"QB_U2_fragments.png")

# 5 stream indicator
fig,ax=plt.subplots(figsize=(6,3.4))
sites=[1,2,3,4,5]; may=[85,80,6,25,62]; do=[9.0,8.8,4.1,5.6,7.8]
ax.bar(sites,may,color=SKY,ec=BLUE,width=0.6,label="Mayfly nymphs (left axis)")
ax.set_xticks(sites); ax.set_xticklabels(["1\nupstream","2\nupstream","3\noutfall","4\n0.5 km below","5\n2 km below"],fontsize=8.5)
ax.set_ylabel("Mayfly nymphs per m²",color=BLUE); ax.set_ylim(0,100); ax.set_xlabel("Sampling site")
ax2=ax.twinx(); ax2.spines["right"].set_visible(True)
ax2.plot(sites,do,color=RED,marker="o",lw=2,label="Dissolved oxygen (right axis)")
ax2.set_ylabel("Dissolved oxygen (mg/L)",color=RED); ax2.set_ylim(0,10); ax2.tick_params(axis="y",colors=RED)
h1,l1=ax.get_legend_handles_labels(); h2,l2=ax2.get_legend_handles_labels()
ax.legend(h1+h2,l1+l2,fontsize=8,frameon=False,loc="upper center",bbox_to_anchor=(0.5,1.16),ncol=2)
save(fig,D+"QB_U2_stream.png")

# 6 FRQ1 vernal pools
fig,ax=plt.subplots(figsize=(6,3.5))
d=["10","50","150","400"]; cl=[620,310,95,40]; eg=[4,11,27,31]
ax.bar(d,cl,color=SKY,ec=BLUE,width=0.55,label="Chloride (left axis)")
ax.set_xlabel("Distance of vernal pool from highway (m)"); ax.set_ylabel("Chloride (mg/L)",color=BLUE); ax.set_ylim(0,700)
ax2=ax.twinx(); ax2.spines["right"].set_visible(True)
ax2.plot(d,eg,color=RED,marker="o",ms=8,ls="none",label="Wood frog egg masses (right axis)")
ax2.set_ylabel("Egg masses per pool",color=RED); ax2.set_ylim(0,40); ax2.tick_params(axis="y",colors=RED)
h1,l1=ax.get_legend_handles_labels(); h2,l2=ax2.get_legend_handles_labels()
ax.legend(h1+h2,l1+l2,fontsize=8,frameon=False,loc="upper center",bbox_to_anchor=(0.5,1.14),ncol=2)
save(fig,D+"QB_U2_pools.png")

# 7 FRQ2 succession
fig,axs=plt.subplots(1,2,figsize=(6.4,3.2))
age=[5,15,30,60,120,250]; rich=[3,9,18,26,24,22]; bio=[0.05,0.4,2.1,9.5,18.0,21.0]; npp=[0.03,0.25,0.80,1.30,1.10,1.00]
axs[0].plot(age,rich,color=GREEN,marker="o",lw=2); axs[0].set_xlabel("Age of lava flow (years)"); axs[0].set_ylabel("Species richness (per plot)"); axs[0].set_ylim(0,30); axs[0].set_xlim(0,260)
axs[0].set_title("Species richness",fontsize=10)
axs[1].plot(age,bio,color=BROWN,marker="s",lw=2,label="Total biomass")
axs[1].plot(age,[v*10 for v in npp],color=RED,marker="^",lw=2,ls="--",label="NPP × 10")
axs[1].set_xlabel("Age of lava flow (years)"); axs[1].set_ylabel("Biomass (kg/m²) or\nNPP × 10 (kg/m²/yr)"); axs[1].set_ylim(0,25); axs[1].set_xlim(0,260)
axs[1].legend(fontsize=8,frameon=False,loc="upper left"); axs[1].set_title("Biomass and NPP",fontsize=10)
fig.tight_layout()
save(fig,D+"QB_U2_succession.png")

# 8 FRQ4 islands
fig,ax=plt.subplots(figsize=(6,3.6))
near=[("A",2,12),("B",10,20),("C",50,30),("D",200,41)]
far=[("E",2,5),("F",10,9),("G",50,15),("H",200,22)]
ax.scatter([n[1] for n in near],[n[2] for n in near],color=RED,s=55,label="Near mainland (10–18 km)",zorder=3)
ax.scatter([n[1] for n in far],[n[2] for n in far],color=BLUE,marker="s",s=55,label="Far from mainland (110–140 km)",zorder=3)
for n in near: ax.annotate(n[0],(n[1],n[2]),xytext=(5,5),textcoords="offset points",fontsize=9)
for n in far: ax.annotate(n[0],(n[1],n[2]),xytext=(5,-12),textcoords="offset points",fontsize=9)
ax.set_xscale("log"); ax.set_xticks([2,10,50,200]); ax.set_xticklabels(["2","10","50","200"])
ax.set_xlabel("Island area (km², log scale)"); ax.set_ylabel("Land bird species"); ax.set_ylim(0,48)
ax.grid(True,color="#e5e5e5",lw=0.6); ax.legend(fontsize=8.5,frameon=False,loc="upper left")
save(fig,D+"QB_U2_islands.png")
