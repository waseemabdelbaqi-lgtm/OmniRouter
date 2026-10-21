import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book1/figs/'

# 1 decay curve
fig,ax=plt.subplots(figsize=(6.0,3.0))
t=np.linspace(0,40,200); ax.plot(t,100*0.5**(t/10),color=RED,lw=2)
for n in range(0,5):
    y=100*0.5**n; ax.plot([10*n,10*n],[0,y],ls=':',color=GREY,lw=0.9); ax.plot([0,10*n],[y,y],ls=':',color=GREY,lw=0.9)
    ax.plot(10*n,y,'o',color=DARK,ms=5)
    ax.text(10*n+0.8,y+4,f'{y:g}%',fontsize=8,color=DARK)
ax.set_xticks([0,10,20,30,40]); ax.set_xticklabels(['0','1 half-life\n(10 y)','2 half-lives\n(20 y)','3 half-lives\n(30 y)','4 half-lives\n(40 y)'],fontsize=8)
ax.set_ylabel('Activity remaining (%)'); ax.set_ylim(0,112); ax.set_xlim(0,41)
ax.set_title('Radioactive decay: halve the amount for every half-life')
save(fig,D+'U6_gap_decay.png')

# 2 wind power curve
fig,ax=plt.subplots(figsize=(6.0,3.0))
v=np.linspace(0,28,400); P=np.zeros_like(v)
for i,x in enumerate(v):
    if x<3: P[i]=0
    elif x<12: P[i]=100*((x-3)/9)**3*1.0
    elif x<=25: P[i]=100
    else: P[i]=0
ax.plot(v,P,color=BLUE,lw=2)
ax.axvspan(3,12,color=SKY,alpha=0.25); ax.axvspan(12,25,color=SAND,alpha=0.25)
ax.axvline(3,color=GREY,ls=':',lw=0.9); ax.axvline(25,color=GREY,ls=':',lw=0.9)
ax.text(7.5,88,'power rises steeply\n(≈ cube of speed)',ha='center',fontsize=8)
ax.text(18.5,50,'rated power:\noutput levels off',ha='center',fontsize=8)
ax.text(3,-17,'cut-in\n3 m/s',ha='center',fontsize=8,va='top'); ax.text(25,-17,'cut-out\n25 m/s',ha='center',fontsize=8,va='top')
ax.set_xlabel('Wind speed at hub height (m/s)',labelpad=22); ax.set_ylabel('Output (% of rated power)')
ax.set_ylim(0,112); ax.set_xlim(0,28)
ax.set_title('Idealized wind-turbine power curve (illustrative)')
save(fig,D+'U6_gap_windcurve.png')
