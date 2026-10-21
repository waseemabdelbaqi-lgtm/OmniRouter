import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book1/figs/'

# 1 growth rates: dN/dt vs N, and doubling times
fig,(a,b)=plt.subplots(1,2,figsize=(6.4,3.2))
K=1000; r=0.4
N=np.linspace(0,1250,300); g=r*N*(K-N)/K
a.plot(N,g,color=BLUE,lw=2.2); a.axhline(0,color="#444",lw=0.8)
a.axvline(K,color=GREY,ls="--",lw=1.2); a.axvline(K/2,color=GREY,ls=":",lw=1)
a.plot([K/2],[r*K/4],"o",color=RED,ms=6)
a.annotate("fastest growth\nat N = K/2",xy=(K/2,100),xytext=(60,45),fontsize=8.5,arrowprops=dict(arrowstyle="->",color=DARK))
a.text(K+12,-118,"K",color=GREY,fontsize=9)
a.text(1010,40,"growth = 0\nat K",fontsize=8.5,color=DARK,ha="left")
a.text(1215,-55,"N > K:\nnegative",fontsize=8.5,color=RED,ha="right")
a.set_xlim(0,1250); a.set_ylim(-125,125)
a.set_xlabel("Population size N (fish)"); a.set_ylabel("Growth dN/dt (fish per year)")
a.set_title("Logistic growth rate (K = 1,000, r = 0.40)",fontsize=9.5)
t=np.linspace(0,140,300)
for rate,c in [(1,BLUE),(2,GREEN),(3.5,RED)]:
    b.plot(t,(1+rate/100)**t,color=c,lw=2,label=f"{rate}% per year")
    td=70/rate
    b.plot([td,td],[0,2],color=c,ls=":",lw=1); b.plot([td],[2],"o",color=c,ms=4)
    b.text(td,0.12,f"{td:.0f} y",color=c,fontsize=8,ha="center",bbox=dict(fc="white",ec="none",pad=0.5))
b.axhline(2,color=GREY,lw=0.8,ls="--")
b.set_xlim(0,140); b.set_ylim(0,8); b.set_xlabel("Time (years)"); b.set_ylabel("Population (multiple of start)")
b.set_title("Doubling time ≈ 70 ÷ growth rate (%)",fontsize=9.5)
b.legend(frameon=False,fontsize=8,loc="upper left")
fig.tight_layout(); save(fig,D+'C6_growth_rates.png')

# 2 age structure
bands=["0–9","10–19","20–29","30–39","40–49","50–59","60–69","70+"]
shapes=[("Rapid growth",[26,21,17,13,9,6,4,4],RED),
        ("Slow growth",[16,15,15,14,13,12,9,6],ORANGE),
        ("Stable",[12,12,13,14,14,13,12,10],GREEN),
        ("Declining",[8,9,11,13,15,16,15,13],BLUE)]
fig,axs=plt.subplots(1,4,figsize=(6.6,3.2),sharey=True)
y=np.arange(8)
fm=np.array([1.0,1.0,1.0,1.0,0.99,0.97,0.93,0.82])
for ax,(name,v,c) in zip(axs,shapes):
    v=np.array(v,float); tot=v.sum(); v=v/tot*100
    f=v*fm/(1+fm)*1.0; m=v-f
    ax.barh(y,-m,color=c,alpha=0.95,height=0.85); ax.barh(y,f,color=c,alpha=0.55,height=0.85)
    ax.axvline(0,color="#444",lw=0.8); ax.set_xlim(-16,16); ax.set_ylim(-0.6,7.9)
    ax.set_title(name,fontsize=9.5); ax.set_xticks([-10,0,10]); ax.set_xticklabels(["10","0","10"],fontsize=8)
    ax.text(-15,7.55,"M",fontsize=8); ax.text(15,7.55,"F",fontsize=8,ha="right")
    ax.spines["left"].set_visible(False); ax.tick_params(axis="y",length=0)
axs[0].set_yticks(y); axs[0].set_yticklabels(bands,fontsize=8); axs[0].set_ylabel("Age band (years)")
# mark reproductive range on first panel
fig.supxlabel("Percent of total population in each sex and age band",fontsize=9.5,y=0.0)
fig.tight_layout(); save(fig,D+'C6_age_structure.png')
