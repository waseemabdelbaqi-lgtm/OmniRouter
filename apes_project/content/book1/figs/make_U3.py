import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book1/figs/'

# 1 survivorship
fig,ax=plt.subplots(figsize=(6,3.6))
x=np.linspace(0,100,200)
t1=1000*(1-(x/100)**6.5)+0*x; t1=np.clip(t1,1,1000)
t2=1000*(1-x/100)*0.98+10
t3=1000*np.exp(-x/9)+3
ax.semilogy(x,t1,color=BLUE,lw=2.2,label="Type I")
ax.semilogy(x,t2,color=GREEN,lw=2.2,label="Type II")
ax.semilogy(x,t3,color=RED,lw=2.2,label="Type III")
ax.set_ylim(3,1500); ax.set_xlim(0,100)
ax.set_xlabel("Age (% of maximum life span)"); ax.set_ylabel("Survivors per 1,000 born (log scale)")
ax.text(70,1180,"Type I: most die old\n(humans, elephants)",color=BLUE,fontsize=8.5,ha="center")
ax.text(52,160,"Type II: steady loss\nat every age (many birds)",color=GREEN,fontsize=8.5,ha="center")
ax.text(70,22,"Type III: most die young\n(oysters, most insects, sea turtles)",color=RED,fontsize=8.5,ha="center")
ax.legend(loc="lower left",frameon=False,fontsize=8.5)
save(fig,D+'U3_survivorship.png')

# 2 growth curves
fig,(a,b)=plt.subplots(1,2,figsize=(6.2,3.2))
t=np.linspace(0,10,200)
a.plot(t,100*np.exp(0.45*t)/np.exp(0)**1,color=RED,lw=2.2); a.set_ylim(0,6000); a.set_xlim(0,10)
a.set_title("J-curve (exponential)"); a.set_xlabel("Time"); a.set_ylabel("Population size")
a.text(1,4800,"No limits:\ngrowth speeds up",fontsize=8.5)
K=1000; N=K/(1+(K/20-1)*np.exp(-1.0*t*1.0))
b.plot(t,N,color=BLUE,lw=2.2); b.axhline(K,color=GREY,ls="--"); b.set_ylim(0,1250); b.set_xlim(0,10)
b.text(0.2,K+30,"K = carrying capacity",fontsize=8.5,color=GREY)
b.set_title("S-curve (logistic)"); b.set_xlabel("Time"); b.set_yticks([0,500,1000]); 
b.annotate("fastest growth\nat K/2",xy=(3.9,500),xytext=(5.6,300),arrowprops=dict(arrowstyle="->",color=DARK),fontsize=8.5)
b.text(0.3,120,"slow start",fontsize=8.5)
fig.tight_layout(); save(fig,D+'U3_growth_curves.png')

# 3 age structure
fig,axs=plt.subplots(1,4,figsize=(6.4,3.0),sharey=True)
groups=["0–14","15–44","45–64","65+"]
data=[("Rapid growth",[34,38,20,8][::1],[33,38,21,9]),
      ("Slow growth",[22,34,27,17],[21,33,27,19]),
      ("Stable (zero)",[19,33,30,18],[18,33,30,19]),
      ("Declining",[12,30,32,26],[11,29,32,28])]
# use finer bars: 8 age bands
bands=["0-9","10-19","20-29","30-39","40-49","50-59","60-69","70+"]
shapes={"Rapid growth":[17,15,13,11,9,6,3,1.5],"Slow growth":[11,11,11,10,9,8,6,4],
        "Stable":[10,10,10,10,10,9,7,5],"Declining":[6,7,8,10,12,13,11,9]}
cols=[RED,ORANGE,GREEN,BLUE]
for ax,(k,v),c in zip(axs,shapes.items(),cols):
    v=np.array(v); y=np.arange(8)
    ax.barh(y,-v,color=c,alpha=.85,height=.85); ax.barh(y,v,color=c,alpha=.55,height=.85)
    ax.set_title(k,fontsize=9); ax.set_xlim(-20,20); ax.axvline(0,color="#444",lw=.8)
    ax.set_xticks([-15,0,15]); ax.set_xticklabels(["15","0","15"],fontsize=7.5)
    ax.set_yticks(y); ax.set_yticklabels(bands if ax is axs[0] else [],fontsize=7.5)
    ax.text(-19,7.5,"M",fontsize=7.5); ax.text(16,7.5,"F",fontsize=7.5)
    ax.spines["left"].set_visible(False)
fig.supxlabel("Percent of population (males left, females right)",fontsize=8.5)
axs[0].set_ylabel("Age band (years)",fontsize=8.5)
fig.tight_layout(); save(fig,D+'U3_age_structure.png')

# 4 DTM
fig,ax=plt.subplots(figsize=(6.2,3.6))
x=np.linspace(0,10,400)
def sig(x,c,w): return 1/(1+np.exp(-(x-c)/w))
dr=40-30*sig(x,3.0,0.45)+0*x
br=40-27*sig(x,5.6,0.6)
ax.plot(x,br,color=GREEN,lw=2.3,label="Birth rate")
ax.plot(x,dr,color=RED,lw=2.3,label="Death rate")
for v in (2.5,5,7.5): ax.axvline(v,color="#999",ls=":",lw=1)
ax.set_xlim(0,10); ax.set_ylim(0,55); ax.set_xticks([])
ax.set_ylabel("Births or deaths per 1,000 people per year")
for xc,s in zip((1.25,3.75,6.25,8.75),("Stage 1\nPre-industrial","Stage 2\nTransitional","Stage 3\nIndustrializing","Stage 4\nIndustrial")):
    ax.text(xc,51,s,ha="center",va="top",fontsize=8.5,fontweight="bold",color=DARK)
ax.text(3.75,27,"Natural increase\nlargest (gap)",ha="center",fontsize=8,color=DARK)
ax.fill_between(x,dr,br,where=(br>dr+1),color=SAND,alpha=.45)
ax2=ax.twinx(); ax2.spines["right"].set_visible(True)
pop=np.cumsum(br-dr); pop=pop/pop.max()
ax2.plot(x,pop,color=BLUE,lw=2,ls="--",label="Total population"); ax2.set_ylim(0,1.45); ax2.set_yticks([]); ax2.set_ylabel("Total population (relative)")
ax.legend(loc="lower left",frameon=False,fontsize=8.5)
ax2.legend(loc="lower center",frameon=False,fontsize=8.5,bbox_to_anchor=(0.62,0.0))
fig.tight_layout(); save(fig,D+'U3_dtm.png')

# 5 r vs K
fig,(a,b)=plt.subplots(1,2,figsize=(6.4,3.2))
t=np.linspace(0,20,400); K=100
rng=np.random.default_rng(3)
r=[]; n=10
# boom-bust for r-species via sinusoid-like
rs=60+55*np.sin(0.9*t)*np.exp(-0*t); rs=np.clip(rs,5,None)*np.where(t<20,1,1)
rs=np.abs(70*np.sin(0.75*t)**2*(1+0.3*np.sin(2*t)))+4
ks=K/(1+9*np.exp(-0.5*t))+2*np.sin(1.6*t)*(t>8)
a.plot(t,rs,color=ORANGE,lw=2,label="r-selected: boom and bust")
a.plot(t,ks,color=BLUE,lw=2,label="K-selected: near K")
a.axhline(K,color=GREY,ls="--"); a.text(0.3,K+4,"K",color=GREY)
a.set_ylim(0,125); a.set_xlabel("Time"); a.set_ylabel("Population size"); a.set_title("Population pattern",fontsize=10)
a.legend(frameon=False,fontsize=7.5,loc="upper center",bbox_to_anchor=(.5,-.2),ncol=1)
cats=["Offspring\nper event","Parental\ncare","Age at\nmaturity","Life span"]
rv=[9,1,1.5,1.5]; kv=[1.5,9,8,9]
xx=np.arange(4); w=.38
b.bar(xx-w/2,rv,w,color=ORANGE,label="r-selected"); b.bar(xx+w/2,kv,w,color=BLUE,label="K-selected")
b.set_xticks(xx); b.set_xticklabels(cats,fontsize=7.5); b.set_yticks([0,5,10]); b.set_yticklabels(["low","","high"])
b.set_title("Typical traits (relative)",fontsize=10); b.legend(frameon=False,fontsize=7.5,loc="upper center",ncol=2,bbox_to_anchor=(.5,1.0))
b.set_ylim(0,12)
fig.tight_layout(); save(fig,D+'U3_r_K.png')
