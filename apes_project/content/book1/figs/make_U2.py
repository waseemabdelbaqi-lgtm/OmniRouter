import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book1/figs/'

# 1 island biogeography
fig,(a,b)=plt.subplots(1,2,figsize=(6.2,3.0))
area=np.linspace(0,100,100)
a.plot(area,12*area**0.3,color=BLUE,lw=2,label="Near mainland")
a.plot(area,7*area**0.3,color=ORANGE,lw=2,label="Far from mainland")
a.set_xlabel("Island area (km²)"); a.set_ylabel("Species richness"); a.set_title("Bigger island, more species"); a.legend(frameon=False,fontsize=8)
a.set_ylim(0,None)
d=np.linspace(0,200,100)
b.plot(d,60*np.exp(-d/120),color=RED,lw=2,label="Large island")
b.plot(d,25*np.exp(-d/120),color=GREEN,lw=2,label="Small island")
b.set_xlabel("Distance from mainland (km)"); b.set_ylabel("Species richness"); b.set_title("Nearer island, more species"); b.legend(frameon=False,fontsize=8)
b.set_ylim(0,None)
fig.tight_layout(); save(fig,D+'U2_island.png')

# 2 tolerance
fig,ax=plt.subplots(figsize=(6.2,3.1))
t=np.linspace(0,40,400)
y=np.exp(-((t-22)/6.5)**2)
ax.plot(t,y,color=RED,lw=2.2)
ax.fill_between(t,0,y,where=(t>=14)&(t<=30),color=GREEN,alpha=.35)
ax.fill_between(t,0,y,where=((t>=8)&(t<14))|((t>30)&(t<=36)),color=YELLOW,alpha=.45)
ax.fill_between(t,0,y,where=(t<8)|(t>36),color=GREY,alpha=.3)
for x in (8,14,30,36): ax.axvline(x,color="#444",lw=.7,ls=":")
ax.text(22,0.45,"Optimum range",ha="center",fontsize=9,fontweight="bold")
ax.text(11,0.18,"Zone of\nstress",ha="center",fontsize=8)
ax.text(33,0.18,"Zone of\nstress",ha="center",fontsize=8)
ax.text(3.5,0.08,"Death",ha="center",fontsize=8); ax.text(38.3,0.08,"Death",ha="center",fontsize=8)
ax.annotate("",xy=(8,1.08),xytext=(36,1.08),arrowprops=dict(arrowstyle="<->",color=DARK))
ax.text(22,1.12,"Range of tolerance",ha="center",fontsize=9,color=DARK)
ax.set_ylim(0,1.25); ax.set_xlabel("Water temperature (°C)"); ax.set_ylabel("Relative performance\n(growth / survival)")
fig.tight_layout(); save(fig,D+'U2_tolerance.png')

# 3 succession
fig,axs=plt.subplots(1,2,figsize=(6.2,3.1),sharey=True)
stages=["Bare rock","Lichens\n& moss","Grasses\n& herbs","Shrubs","Pines","Hardwood\nforest"]
x=np.linspace(0,1,200)
def logi(x,c,k): return 1/(1+np.exp(-k*(x-c)))
for ax,title,t0 in ((axs[0],"Primary succession",0),(axs[1],"Secondary succession",0.25)):
    xs=np.linspace(0,1,200)
    bio=logi(xs,0.65,9)
    if t0: bio=0.25+0.75*logi(xs,0.5,8)
    rich=np.exp(-((xs-0.62)/0.28)**2); rich=rich/rich.max()
    if t0: rich=0.2+0.8*np.exp(-((xs-0.55)/0.3)**2)
    npp=np.exp(-((xs-0.5)/0.22)**2)
    if t0: npp=0.3+0.7*np.exp(-((xs-0.4)/0.25)**2)
    ax.plot(xs,bio,color=GREEN,lw=2,label="Biomass")
    ax.plot(xs,rich,color=BLUE,lw=2,label="Species richness")
    ax.plot(xs,npp,color=ORANGE,lw=2,ls="--",label="Net productivity")
    ax.set_title(title,fontsize=10); ax.set_xticks([]); ax.set_xlabel("Time →")
    ax.set_ylim(0,1.15)
axs[0].set_ylabel("Relative value"); axs[1].legend(frameon=False,fontsize=7.5,loc="lower right")
axs[0].text(0.02,1.05,"Starts with no soil",fontsize=8,color=DARK); axs[1].text(0.02,1.05,"Starts with soil",fontsize=8,color=DARK)
fig.tight_layout(); save(fig,D+'U2_succession.png')

# 4 recovery
fig,ax=plt.subplots(figsize=(6.2,3.0))
t=np.linspace(0,20,200)
def rec(t,drop,rate):
    y=np.where(t<2,1.0,drop+(1-drop)*(1-np.exp(-rate*(t-2))))
    return y
ax.plot(t,rec(t,0.45,0.45),color=GREEN,lw=2,label="High-diversity community")
ax.plot(t,rec(t,0.25,0.12),color=RED,lw=2,label="Low-diversity community")
ax.axvline(2,color=GREY,ls=":"); ax.text(2.2,1.05,"Disturbance (e.g., drought)",fontsize=8,color=GREY)
ax.axhline(1,color="#999",lw=.6)
ax.set_ylim(0,1.2); ax.set_xlabel("Years"); ax.set_ylabel("Productivity relative to pre-disturbance")
ax.legend(frameon=False,fontsize=8,loc="lower right")
fig.tight_layout(); save(fig,D+'U2_recovery.png')
