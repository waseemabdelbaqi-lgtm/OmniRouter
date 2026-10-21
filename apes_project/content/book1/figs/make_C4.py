import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
OUT='/home/user/OmniRouter/apes_project/content/book1/figs/'

def g(t,c,w): return np.exp(-((t-c)/w)**2)

def succession():
    fig,axs=plt.subplots(1,2,figsize=(6.4,3.3),sharey=True)
    t=np.linspace(0,1,300)
    lg=lambda c,k: 1/(1+np.exp(-k*(t-c)))
    P=dict(bio=lg(0.6,9),
           npp=(0.30+0.70*g(t,0.42,0.22))*(1-np.exp(-10*t)),
           rich=(0.70+0.30*g(t,0.55,0.25))*(1-np.exp(-6*t)))
    S=dict(bio=0.25+0.75*lg(0.45,8),
           npp=0.30+0.70*g(t,0.32,0.22),
           rich=(0.72+0.28*g(t,0.5,0.25))*(0.30+0.70*(1-np.exp(-6*t))))
    for ax,title,D in ((axs[0],"Primary succession (no soil at start)",P),(axs[1],"Secondary succession (soil present)",S)):
        ax.plot(t,D['bio'],color=GREEN,lw=2.2,label="Biomass")
        ax.plot(t,D['rich'],color=BLUE,lw=2.2,label="Species richness")
        ax.plot(t,D['npp'],color=ORANGE,lw=2.2,ls="--",label="Net productivity")
        ax.set_title(title,fontsize=9); ax.set_xlabel("Time →"); ax.set_xticks([]); ax.set_ylim(0,1.12)
    axs[0].set_ylabel("Relative value"); axs[1].legend(fontsize=7.5,loc="lower right",frameon=False)
    fig.tight_layout(); save(fig,OUT+'C4_succession.png')

def foodweb():
    fig,ax=canvas(6.3,4.4,ylim=(-0.06,1.04))
    rows={"prod":0.13,"pri":0.33,"sec":0.53,"ter":0.73,"quat":0.91}
    labs=[("Producers","prod"),("Primary consumers","pri"),("Secondary consumers","sec"),("Tertiary consumers","ter"),("Quaternary consumers","quat")]
    for n,k in labs: ax.text(0.0,rows[k]+0.04,n.replace(" consumers","\nconsumers"),fontsize=8,color=GREY,va="center",fontweight="bold")
    N={}; h=0.08
    def nd(k,x,r,t,fc,ec,w=0.2):
        y=rows[r]; box(ax,x,y,w,h,t,fc=fc,ec=ec,fs=8.5,bold=True); N[k]=(x+w/2,y,y+h)
    nd("algae",0.28,"prod","Algae","#E3F0E5",GREEN,0.18)
    nd("plant",0.68,"prod","Aquatic plants","#E3F0E5",GREEN,0.24)
    nd("zoo",0.28,"pri","Zooplankton","#FBEBD5",ORANGE,0.2)
    nd("larva",0.68,"pri","Insect larvae","#FBEBD5",ORANGE,0.2)
    nd("minnow",0.28,"sec","Minnows","#FBEBD5",ORANGE,0.2)
    nd("bass",0.50,"ter","Bass","#E3EEF7",BLUE,0.18)
    nd("heron",0.50,"quat","Heron","#F3E1E4",RED,0.18)
    for a_,b_ in [("algae","zoo"),("plant","larva"),("zoo","minnow"),("minnow","bass"),("larva","bass"),("bass","heron")]:
        arrow(ax,(N[a_][0],N[a_][2]+0.01),(N[b_][0],N[b_][1]-0.01),color=DARK,lw=1.3)
    box(ax,0.30,-0.02,0.40,0.07,"Detritivores and decomposers recycle\nthe dead matter from every level",fc="#EFE5DA",ec=BROWN,fs=7.5)
    save(fig,OUT+'C4_food_web.png')

succession(); foodweb()
