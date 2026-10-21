import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book1/figs/'
P=50
S=np.linspace(0,P,100)
fig,(a,b)=plt.subplots(1,2,figsize=(6.2,3.1),sharey=True)
def eq(i0,e1): # i0*(1-S/P) = e1*S
    return i0/(i0/P+e1)
def draw(ax,curves,title):
    for (kind,i0,e1,col,lab) in curves:
        y=i0*(1-S/P) if kind=='I' else e1*S
        ax.plot(S,y,color=col,lw=2,ls='-' if kind=='I' else '--',label=lab)
    ax.set_title(title,fontsize=10); ax.set_xlabel("Number of species on island")
    ax.set_xlim(0,P); ax.set_ylim(0,22)
# left: distance
draw(a,[('I',20,0,BLUE,"Immigration, near"),('I',8,0,ORANGE,"Immigration, far"),('E',0,0.4,RED,"Extinction")],"Distance changes arrivals")
for i0,c in ((20,BLUE),(8,ORANGE)):
    s=eq(i0,0.4); a.plot([s,s],[0,0.4*s],color=c,ls=':',lw=1.2); a.plot(s,0.4*s,'o',color=c,ms=5)
a.set_ylabel("Rate (species per year)")
# right: size
draw(b,[('I',14,0,BLUE,"Immigration"),('E',0,0.15,GREEN,"Extinction, large"),('E',0,0.6,RED,"Extinction, small")],"Size changes losses")
for e,c in ((0.15,GREEN),(0.6,RED)):
    s=eq(14,e); b.plot([s,s],[0,e*s],color=c,ls=':',lw=1.2); b.plot(s,e*s,'o',color=c,ms=5)
a.legend(frameon=False,fontsize=7.5,loc='upper center'); b.legend(frameon=False,fontsize=7.5,loc='center right',bbox_to_anchor=(1.0,0.62))
a.set_ylim(0,26); b.set_ylim(0,26)
fig.tight_layout(); save(fig,D+'U2_gap_equilibrium.png')
