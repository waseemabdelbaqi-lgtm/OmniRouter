import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book1/figs/'

# 1 per-capita birth and death rates versus density
fig,ax=plt.subplots(figsize=(6,3.4))
d=np.linspace(0,12,100)
b=0.60-0.04*d; m=0.12+0.02*d; m2=m+0.06
ax.plot(d,b,color=GREEN,lw=2.3,label="Births per individual")
ax.plot(d,m,color=RED,lw=2.3,label="Deaths per individual (normal year)")
ax.plot(d,m2,color=RED,lw=2.0,ls="--",label="Deaths per individual (after drought)")
ax.plot([8],[0.28],'o',color=DARK,ms=7); ax.plot([7],[0.26],'o',color=DARK,ms=7,mfc='white')
ax.vlines(8,0,0.28,color=GREY,ls=":"); ax.vlines(7,0,0.32,color=GREY,ls=":")
ax.text(8.25,0.03,"K = 8",fontsize=8.5,color=DARK)
ax.text(5.3,0.03,"new K = 7",fontsize=8.5,color=DARK,ha="right")
ax.text(1.0,0.55,"births > deaths:\npopulation grows",fontsize=8.5,color=GREEN)
ax.text(9.4,0.50,"deaths > births:\npopulation shrinks",fontsize=8.5,color=RED)
ax.set_xlim(0,12); ax.set_ylim(0,0.7)
ax.set_xlabel("Population density (individuals per km²)"); ax.set_ylabel("Rate per individual per year")
ax.legend(loc="upper center",bbox_to_anchor=(0.5,-0.2),ncol=1,frameon=False,fontsize=8.5)
save(fig,D+'U3_gap_birth_death.png')

# 2 predator-prey cycles (simulated Lotka-Volterra, rescaled)
def lv(T=60,dt=0.01):
    x,y=1.0,0.5; a,bb,c,dd=0.6,0.9,0.8,0.5
    ts=[];xs=[];ys=[]
    for i in range(int(T/dt)):
        dx=(a*x-bb*x*y)*dt; dy=(-c*y+dd*x*y*1.6)*dt
        x+=dx; y+=dy; ts.append(i*dt); xs.append(x); ys.append(y)
    return np.array(ts),np.array(xs),np.array(ys)
t,x,y=lv()
m=(t>=0)&(t<=24)
fig,ax=plt.subplots(figsize=(6,3.0))
ax.plot(t[m],x[m]/x[m].max()*100,color=GREEN,lw=2.2,label="Prey")
ax.plot(t[m],y[m]/y[m].max()*100,color=RED,lw=2.2,label="Predator")
# mark first peaks
ip=np.argmax(x[m][:800]); iq=np.argmax(y[m][:1600])
ax.annotate("prey peak",xy=(t[ip],x[ip]/x[m].max()*100),xytext=(t[ip]-3.5,108),arrowprops=dict(arrowstyle="->",color=DARK),fontsize=8.5)
ax.annotate("predator peak\ncomes later",xy=(t[iq],y[iq]/y[m].max()*100),xytext=(t[iq]+1.2,108),arrowprops=dict(arrowstyle="->",color=DARK),fontsize=8.5)
ax.set_ylim(0,130); ax.set_xlim(0,24)
ax.set_xlabel("Time (years)"); ax.set_ylabel("Population (% of its own maximum)")
ax.legend(loc="lower right",frameon=False,fontsize=8.5)
save(fig,D+'U3_gap_predator_prey.png')
