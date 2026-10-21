import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book2/figs/'

# 1 well hydrograph
fig,ax=plt.subplots(figsize=(6,3.4))
yr=[2000,2005,2010,2015,2020,2025]; d=[20,24,29,35,40,44]
ax.plot(yr,d,'o-',color=RED,lw=2,ms=6)
ax.set_ylim(50,10); ax.set_xlim(1998,2027)
ax.set_xlabel('Year'); ax.set_ylabel('Depth to water table (m below surface)')
ax.set_xticks(yr); ax.set_yticks(range(10,51,10)); ax.grid(True,color='#ddd',lw=0.7)
ax.set_title('Monitoring well in an irrigated valley')
save(fig,D+'QBC3_wells.png')

# 2 thermocline profile
dep=[0,50,100,150,200,300,400,500,600,800,1000]
T=[28,28,26,22,18,13,9.5,7,6,4.5,4]
fig,ax=plt.subplots(figsize=(4.2,4.4))
ax.plot(T,dep,'o-',color=BLUE,lw=2,ms=5)
ax.set_ylim(1000,0); ax.set_xlim(0,30)
ax.xaxis.tick_top(); ax.xaxis.set_label_position('top')
ax.spines['top'].set_visible(True); ax.spines['bottom'].set_visible(False)
ax.set_xlabel('Temperature (°C)'); ax.set_ylabel('Depth (m)')
ax.set_yticks(range(0,1001,100)); ax.grid(True,color='#ddd',lw=0.7)
ax.set_title('Open-ocean station, 10° N',pad=34)
save(fig,D+'QBC3_thermocline.png')

# 3 aquifer cross-section
fig,ax=canvas(6.3,3.5,(0,10),(0,6))
ax.add_patch(Rectangle((0,4.6),10,0.9,fc='#8DB36B',ec='none'))          # farmland strip
ax.add_patch(Rectangle((0,0.8),10,3.8,fc=SAND,ec='none',alpha=0.55))    # unconfined aquifer
ax.add_patch(Rectangle((0,0),10,0.8,fc='#8a8a8a',ec='none'))            # bedrock
ax.plot([0,3.5,5.0,6.5,10],[3.9,3.9,3.0,3.9,3.9],color=BLUE,lw=0)       # unused
xs=np.linspace(0,10,200); wt=3.9-0.9*np.exp(-((xs-5)/1.3)**2)
ax.fill_between(xs,2.6*0+0.8,wt,color=SKY,alpha=0.8,zorder=1)
ax.plot(xs,wt,color=DARK,lw=1.6,ls='--',zorder=3)
ax.add_patch(Rectangle((4.88,0.8),0.24,4.6,fc='white',ec=DARK,lw=1.2,zorder=4))
ax.text(5.0,5.75,'Irrigation well',ha='center',fontsize=9,color=DARK)
ax.text(1.4,4.05,'Water table',fontsize=9,color=DARK,ha='center')
ax.text(8.6,2.2,'Sand and gravel\n(unconfined aquifer)',fontsize=9,ha='center',va='center',zorder=5)
ax.text(1.4,2.2,'Saturated\nthickness\n≈ 60 m',fontsize=9,ha='center',va='center')
ax.text(5,0.38,'Impermeable bedrock',fontsize=9,ha='center',color='white')
ax.text(8.5,5.05,'Irrigated farmland',fontsize=9,ha='center',color='#1f3d12',va='center')
ax.annotate('',xy=(3.1,3.9),xytext=(3.1,4.6),arrowprops=dict(arrowstyle='<-',color=BLUE))
ax.text(3.2,4.25,'recharge',fontsize=8,color=BLUE)
save(fig,D+'QBC3_aquifer.png')
