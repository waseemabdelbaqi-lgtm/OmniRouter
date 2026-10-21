import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book1/figs/'

# 1 irrigation efficiency
fig,ax=plt.subplots(figsize=(6.2,3.2))
names=['Furrow','Flood','Spray','Drip']; lost=[33,20,25,5]
lab=['about 1/3 lost','about 20% lost','1/4 or less lost','about 5% lost']
cols=[BROWN,SKY,BLUE,TEAL]
ax.barh(names,[100-l for l in lost],color=cols,label='Reaches crop roots')
ax.barh(names,lost,left=[100-l for l in lost],color='#DDDDDD',edgecolor='#999',hatch='//',label='Lost to evaporation and runoff')
for i,l in enumerate(lab): ax.text(101,i,l,va='center',fontsize=8.5)
ax.invert_yaxis(); ax.set_xlim(0,135); ax.set_xticks([0,25,50,75,100]); ax.set_xlabel('Percent of pumped water')
ax.set_title('Water delivered to crops by irrigation method',loc='left')
ax.legend(loc='lower center',bbox_to_anchor=(0.45,-0.45),ncol=2,frameon=False,fontsize=8.5)
save(fig,D+'U5_irrigation.png')

# 2 sustainable yield
fig,ax=plt.subplots(figsize=(6.2,3.3))
N=np.linspace(0,1000,200); K=1000; r=0.4
g=r*N*(1-N/K)
ax.plot(N,g,color=RED,lw=2.2,label='Natural growth (new fish added per year)')
ax.axhline(70,color=BLUE,ls='--',lw=1.5,label='Constant harvest of 70 (below the peak)')
ax.axhline(130,color=ORANGE,ls='--',lw=1.5,label='Constant harvest of 130 (above the peak)')
ax.plot([500],[100],'o',color=RED); ax.annotate('Maximum sustainable yield',(500,100),(560,108),fontsize=8.5,arrowprops=dict(arrowstyle='-',color=GREY))
ax.set_ylim(0,150); ax.set_xlim(0,1000)
ax.set_xlabel('Fish stock size (thousand tonnes)'); ax.set_ylabel('Fish per year (thousand tonnes)')
ax.set_title('Sustainable yield of a fish stock',loc='left')
ax.text(500,134,'Harvest exceeds growth at every stock size: collapse',fontsize=8.5,color=ORANGE,va='bottom',ha='center')
ax.legend(loc='lower center',bbox_to_anchor=(0.5,-0.5),frameon=False,fontsize=8.5)
save(fig,D+'U5_sustainable_yield.png')

# 3 hydrograph
fig,ax=plt.subplots(figsize=(6.2,3.2))
t=np.linspace(0,12,300)
def hyd(t,peak,tp,w): return peak*np.exp(-((t-tp)**2)/(2*w**2))
ax.axvspan(0,0.6,color=SKY,alpha=0.5); ax.text(0.7,56,'Storm\nbegins',fontsize=8,va='top')
ax.plot(t,hyd(t,18,4.2,1.6),color=GREEN,lw=2.2,label='Forested watershed')
ax.plot(t,hyd(t,55,2.2,0.8),color=RED,lw=2.2,label='Same watershed after paving')
ax.annotate('Higher, earlier peak',(2.2,55),(4.0,50),fontsize=8.5,arrowprops=dict(arrowstyle='->',color=GREY))
ax.annotate('Lag time\n(longer when\nwater soaks in)',(4.2,18),(7.2,28),fontsize=8.5,arrowprops=dict(arrowstyle='->',color=GREY))
ax.set_xlabel('Hours since storm began'); ax.set_ylabel('Stream discharge (m³/s)'); ax.set_ylim(0,60)
ax.set_title('Impervious surfaces and stormwater runoff',loc='left'); ax.legend(frameon=False,fontsize=8.5,loc='upper right')
save(fig,D+'U5_hydrograph.png')

# 4 footprint
fig,ax=plt.subplots(figsize=(6.2,3.3))
c=['Country A','Country B','Country C','Country D']; fp=[8.1,4.9,2.4,1.1]; bc=[3.2,5.6,1.9,1.6]
x=np.arange(4); w=0.36
ax.bar(x-w/2,fp,w,color=RED,label='Ecological footprint'); ax.bar(x+w/2,bc,w,color=GREEN,label='Biocapacity')
for i in range(4):
    d=bc[i]-fp[i]; ax.text(i,max(fp[i],bc[i])+0.35,('reserve +' if d>0 else 'deficit ')+f'{d:+.1f}'.lstrip('+-') if False else (f'reserve {d:.1f}' if d>0 else f'deficit {-d:.1f}'),ha='center',fontsize=8.5,color=DARK)
ax.set_xticks(x); ax.set_xticklabels(c); ax.set_ylim(0,9.8); ax.set_ylabel('Global hectares per person')
ax.set_title('Footprint versus biocapacity (invented data)',loc='left'); ax.legend(frameon=False,fontsize=8.5,loc='upper right')
save(fig,D+'U5_footprint.png')

# 5 trophic
fig,ax=plt.subplots(figsize=(6.2,3.2))
lv=['Producer\n(grain)','Primary consumer\n(cattle)','Secondary consumer\n(human eating beef)']
vals=[10000,1000,100]
b=ax.bar(lv,vals,color=[GREEN,ORANGE,RED],width=0.55); ax.set_yscale('log'); ax.set_ylim(30,30000)
for r_,v in zip(b,vals): ax.text(r_.get_x()+r_.get_width()/2,v*1.25,f'{v:,} kcal',ha='center',fontsize=9)
ax.annotate('',xy=(0.5,1000),xytext=(0.5,10000),arrowprops=dict(arrowstyle='->',color=GREY)); ax.text(0.5,2800,'×0.10',ha='center',fontsize=9,color=DARK,bbox=dict(fc='white',ec='none',pad=1))
ax.annotate('',xy=(1.5,100),xytext=(1.5,1000),arrowprops=dict(arrowstyle='->',color=GREY)); ax.text(1.5,280,'×0.10',ha='center',fontsize=9,color=DARK,bbox=dict(fc='white',ec='none',pad=1))
ax.set_ylabel('Usable energy (kcal, log scale)'); ax.set_title('The 10% rule: energy left at each step',loc='left')
save(fig,D+'U5_trophic_energy.png')
