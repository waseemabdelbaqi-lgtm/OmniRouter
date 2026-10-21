import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book2/figs/'

# 1 survivorship (log scale)
x=np.linspace(0,1,201)
t1=1000*np.exp(-np.log(500)*x**0.3)          # Curve 1 : Type III
t2=np.maximum(1000*(1-x**3.5),2)             # Curve 2 : Type I
t3=1000*np.exp(-np.log(500)*x)               # Curve 3 : Type II
fig,ax=plt.subplots(figsize=(5.6,3.5))
ax.plot(x*100,t1,color=RED,lw=2,ls='-',label='Curve 1')
ax.plot(x*100,t2,color=BLUE,lw=2,ls='--',label='Curve 2')
ax.plot(x*100,t3,color=GREEN,lw=2,ls=':',label='Curve 3')
ax.set_yscale('log'); ax.set_ylim(1,1500); ax.set_xlim(0,100)
ax.set_xlabel('Age (% of maximum life span)'); ax.set_ylabel('Survivors per 1,000 born (log scale)')
ax.legend(frameon=False,loc='lower left'); ax.grid(alpha=.25)
save(fig,D+'QB_U3_surv.png')

# 2 logistic with labelled points
K=600; N0=20; r=0.9
t=np.linspace(0,10,300); N=K/(1+(K/N0-1)*np.exp(-r*t))
def tat(n): return np.log((K/N0-1)/(K/n-1))/r
pts={'Q':60,'S':300,'P':520,'R':596}
fig,ax=plt.subplots(figsize=(5.6,3.4))
ax.plot(t,N,color=RED,lw=2.2)
ax.axhline(K,color=GREY,ls='--',lw=1); ax.text(0.2,K+14,'Carrying capacity, K = 600',fontsize=9,color=GREY)
for k,n in pts.items():
    tt=tat(n); ax.plot(tt,n,'o',color=DARK,ms=7)
    ax.annotate(k,(tt,n),xytext=(-14,6) if k!='R' else (-4,-17),textcoords='offset points',fontsize=11,fontweight='bold',color=DARK)
ax.set_xlim(0,10); ax.set_ylim(0,680)
ax.set_xlabel('Years since introduction'); ax.set_ylabel('Number of sheep')
save(fig,D+'QB_U3_logistic.png')

# 3 deer + browse
yrs=np.arange(0,15)
deer=[40,55,80,120,180,260,360,440,480,410,300,210,160,140,130]
browse=[1000,960,900,800,650,480,330,210,140,120,150,190,260,340,380]
fig,(a1,a2)=plt.subplots(2,1,figsize=(5.6,4.4),sharex=True)
a1.plot(yrs,deer,'-o',color=RED,lw=2,ms=4); a1.set_ylabel('Deer on island'); a1.set_ylim(0,550); a1.grid(alpha=.25)
a2.plot(yrs,browse,'-s',color=GREEN,lw=2,ms=4); a2.set_ylabel('Browse biomass\n(kg per hectare)'); a2.set_ylim(0,1100); a2.grid(alpha=.25)
a2.set_xlabel('Year of study'); a2.set_xticks(yrs)
save(fig,D+'QB_U3_deer.png')

# 4 yeast cultures
tt=np.linspace(0,48,300); fig,ax=plt.subplots(figsize=(5.6,3.4))
for Kc,lab,c,ls in [(20,'Low glucose',BLUE,':'),(45,'Medium glucose',GREEN,'--'),(90,'High glucose',RED,'-')]:
    ax.plot(tt,Kc/(1+(Kc/0.5-1)*np.exp(-0.22*tt)),color=c,ls=ls,lw=2,label=lab)
ax.set_xlabel('Time (hours)'); ax.set_ylabel('Yeast cells (millions per mL)'); ax.set_xlim(0,48); ax.set_ylim(0,100)
ax.legend(frameon=False,loc='upper left'); ax.grid(alpha=.25)
save(fig,D+'QB_U3_yeast.png')

# 5 pyramids
bands=['0–4','5–9','10–14','15–19','20–24','25–29','30–34','35–39','40–44','45–49','50–54','55–59','60–64','65–69','70–74','75–79','80+']
C=[7.6,6.6,5.6,4.7,3.9,3.2,2.6,2.1,1.6,1.2,0.9,0.6,0.4,0.25,0.15,0.08,0.04]
A=[3.2,3.3,3.4,3.5,3.6,3.7,3.7,3.6,3.5,3.3,3.0,2.5,2.0,1.5,1.0,0.6,0.4]
B=[2.0,2.2,2.5,2.9,3.4,3.9,4.3,4.5,4.6,4.4,4.0,3.6,3.2,2.6,1.9,1.2,0.8]
Dd=[4.3,4.3,4.3,4.3,4.1,3.9,3.5,3.1,2.6,2.2,1.8,1.4,1.0,0.7,0.4,0.2,0.1]
fig,axs=plt.subplots(2,2,figsize=(6.2,6.2),sharey=True)
for ax,(nm,v) in zip(axs.flat,[('Country A',A),('Country B',B),('Country C',C),('Country D',Dd)]):
    v=np.array(v); v=v/v.sum()*50
    y=np.arange(17)
    ax.barh(y,-v,color=BLUE,height=0.85); ax.barh(y,v,color=ORANGE,height=0.85)
    ax.set_xlim(-10,10); ax.set_yticks(y[::2]); ax.set_yticklabels(bands[::2],fontsize=8)
    ax.set_xticks([-8,-4,0,4,8]); ax.set_xticklabels(['8','4','0','4','8'],fontsize=8)
    ax.set_title(nm,fontsize=10); ax.spines['left'].set_visible(True)
    ax.text(-9.7,16.2,'Male',fontsize=8,color=BLUE,fontweight='bold'); ax.text(9.7,16.2,'Female',fontsize=8,color=ORANGE,fontweight='bold',ha='right')
for ax in axs[1]: ax.set_xlabel('% of total population',fontsize=9)
for ax in axs[:,0]: ax.set_ylabel('Age group (years)',fontsize=9)
fig.tight_layout()
save(fig,D+'QB_U3_pyramids.png')

# 6 DTM
x=np.linspace(0,4,400); sg=lambda z:1/(1+np.exp(-z))
cdr=9+27*(1-sg((x-1.5)/0.22)); cbr=11+29*(1-sg((x-2.6)/0.3))
cdr=cdr+0.0; 
fig,ax=plt.subplots(figsize=(5.8,3.5))
ax.plot(x,cbr,color=RED,lw=2.2,label='Birth rate'); ax.plot(x,cdr,color=BLUE,lw=2.2,ls='--',label='Death rate')
for b in (1,2,3): ax.axvline(b,color=GREY,lw=.8,ls=':')
for c,l in zip((0.5,1.5,2.5,3.5),'WXYZ'): ax.text(c,46,'Stage '+l,ha='center',fontsize=10,fontweight='bold',color=DARK)
ax.set_xlim(0,4); ax.set_ylim(0,50); ax.set_xticks([]); ax.set_xlabel('Time (increasing economic development)')
ax.set_ylabel('Births or deaths per 1,000 people per year'); ax.legend(frameon=False,loc='center left',bbox_to_anchor=(0.0,0.45))
save(fig,D+'QB_U3_dtm.png')

# 7 TFR vs enrollment
en=[12,20,30,41,52,60,71,82,90,96]; tf=[6.4,5.8,5.2,4.6,3.9,3.3,2.8,2.2,1.8,1.5]
fig,ax=plt.subplots(figsize=(5.6,3.4))
ax.scatter(en,tf,color=RED,s=40,zorder=3); ax.axhline(2.1,color=GREY,ls='--',lw=1.2)
ax.text(14,2.25,'Replacement level (2.1)',fontsize=9,color=GREY)
ax.set_xlabel('Girls enrolled in secondary school (%)'); ax.set_ylabel('Total fertility rate\n(children per woman)')
ax.set_xlim(0,100); ax.set_ylim(0,7); ax.grid(alpha=.25)
save(fig,D+'QB_U3_tfr.png')

# 8 FRQ1 goats
yr=np.arange(2005,2025)
goats=[110,135,165,205,250,300,345,385,410,425,430,420,395,370,345,330,320,315,312,310]
forage=[900,880,850,810,760,700,640,580,520,470,430,410,395,385,380,378,376,376,375,375]
fig,(a1,a2)=plt.subplots(2,1,figsize=(5.8,4.6),sharex=True)
a1.plot(yr,goats,'-o',color=RED,lw=2,ms=4); a1.set_ylabel('Mountain goats\ncounted'); a1.set_ylim(0,500); a1.grid(alpha=.25)
a2.plot(yr,forage,'-s',color=GREEN,lw=2,ms=4); a2.set_ylabel('Winter forage\n(kg per hectare)'); a2.set_ylim(0,1000); a2.grid(alpha=.25)
a2.set_xlabel('Year'); a2.set_xticks(yr[::3])
save(fig,D+'QB_U3_frq1.png')

# 9 FRQ2 CBR/CDR
yy=[1960,1980,2000,2020]; cb=[44,42,30,19]; cd=[24,13,8,7]
fig,ax=plt.subplots(figsize=(5.6,3.3))
ax.plot(yy,cb,'-o',color=RED,lw=2,label='Crude birth rate'); ax.plot(yy,cd,'--s',color=BLUE,lw=2,label='Crude death rate')
ax.set_xticks(yy); ax.set_ylim(0,50); ax.set_xlabel('Year'); ax.set_ylabel('Per 1,000 people per year'); ax.legend(frameon=False); ax.grid(alpha=.25)
save(fig,D+'QB_U3_frq2.png')

# 10 FRQ4 survivorship
ages=[0,1,2,4,6,8,10,12,14]; X=[1000,950,880,840,790,700,520,250,40]
ay=[0,1,2,4,6,8]; Y=[1000,60,45,25,12,5]
fig,ax=plt.subplots(figsize=(5.6,3.5))
ax.plot(ages,X,'-o',color=RED,lw=2,ms=4,label='Species X'); ax.plot(ay,Y,'--s',color=BLUE,lw=2,ms=4,label='Species Y')
ax.set_yscale('log'); ax.set_ylim(1,1500); ax.set_xlim(0,15)
ax.set_xlabel('Age (years)'); ax.set_ylabel('Survivors per 1,000 born (log scale)'); ax.legend(frameon=False,loc='lower left'); ax.grid(alpha=.25)
ax.text(8.6,4.2,'Species Y: none alive\nat age 10 or later',fontsize=9,color=BLUE,va='center')
save(fig,D+'QB_U3_frq4.png')
