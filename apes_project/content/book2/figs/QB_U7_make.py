import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
OUT='/home/user/OmniRouter/apes_project/content/book2/figs/'
g=lambda x,m,s:np.exp(-0.5*((x-m)/s)**2)

# 1 diurnal
t=np.linspace(0,24,300)
no=4+76*g(t,7.5,1.3)+20*g(t,18,1.5)
no2=10+35*g(t,9.5,1.8)+12*g(t,19,2)
o3=18+78*g(t,14.2,2.6)
fig,ax=plt.subplots(figsize=(6.2,3.4))
ax.plot(t,no,color=RED,lw=2,label='NO'); ax.plot(t,no2,color=ORANGE,lw=2,label='NO₂'); ax.plot(t,o3,color=BLUE,lw=2,label='O₃')
ax.set_xticks(range(0,25,3)); ax.set_xticklabels(['12 am','3 am','6 am','9 am','12 pm','3 pm','6 pm','9 pm','12 am'])
ax.set_xlim(0,24); ax.set_ylim(0,100); ax.set_xlabel('Time of day (sunny July day)'); ax.set_ylabel('Concentration (ppb)')
ax.legend(frameon=False,loc='upper left',bbox_to_anchor=(0.0,1.0)); ax.grid(alpha=.25)
save(fig,OUT+'QB_U7_diurnal.png')

# 2 inversion
z=np.linspace(0,600,200)
d1=14-0.0085*z
d2=np.where(z<300,6+6*z/300,12-0.01*(z-300))
fig,ax=plt.subplots(figsize=(5.2,3.6))
ax.plot(d1,z,color=BLUE,lw=2.2,label='Day 1'); ax.plot(d2,z,color=RED,lw=2.2,label='Day 2')
ax.set_xlabel('Air temperature (°C)'); ax.set_ylabel('Height above ground (m)'); ax.set_ylim(0,600); ax.set_xlim(4,16)
ax.legend(frameon=False,loc='upper right'); ax.grid(alpha=.25)
save(fig,OUT+'QB_U7_inversion.png')

# 3 power plant
fig,ax=canvas(6.2,2.9,(-0.03,1),(0,1))
box(ax,0.02,0.30,0.17,0.40,'Coal\nboiler',fs=9,bold=True)
box(ax,0.27,0.22,0.23,0.56,'',fc='white')
ax.text(0.385,0.84,'Device 1',ha='center',fontsize=9,fontweight='bold',color=RED)
for xx in (0.31,0.385,0.46):
    ax.plot([xx,xx],[0.28,0.72],color=GREY,lw=3)
for xx in (0.345,0.425):
    ax.plot([xx,xx],[0.28,0.72],color=RED,lw=1,ls='--')
ax.text(0.385,0.14,'charged wires and\ncollection plates',ha='center',fontsize=7.5,va='top')
box(ax,0.58,0.22,0.23,0.56,'',fc='white')
ax.text(0.695,0.84,'Device 2',ha='center',fontsize=9,fontweight='bold',color=RED)
for xx in (0.63,0.695,0.76):
    ax.plot([xx],[0.70],marker='v',color=BLUE,ms=7)
    for yy in (0.6,0.5,0.4): ax.plot([xx],[yy],marker='.',color=SKY,ms=8)
ax.text(0.695,0.14,'spray of limestone-\nwater slurry',ha='center',fontsize=7.5,va='top')
ax.add_patch(Rectangle((0.90,0.30),0.05,0.62,fc='#bbb',ec='#444'))
ax.text(0.925,0.97,'Stack',ha='center',fontsize=8.5,fontweight='bold')
arrow(ax,(0.18,0.5),(0.27,0.5)); arrow(ax,(0.50,0.5),(0.58,0.5)); arrow(ax,(0.81,0.5),(0.90,0.5))
ax.text(0.232,0.60,'flue\ngas',fontsize=7,ha='center')
save(fig,OUT+'QB_U7_plant.png')

# 4 noise
labels=['Quiet\nlibrary','Office\nconversation','Heavy city\ntraffic','Leaf\nblower','Chainsaw','Jackhammer']
vals=[40,60,80,95,105,110]
fig,ax=plt.subplots(figsize=(6.2,3.3))
bars=ax.bar(labels,vals,color=[GREY,GREY,GREY,RED,RED,RED][:0] or [BLUE]*6,width=0.6)
ax.axhline(85,color=RED,ls='--',lw=1.6); ax.text(-0.45,87,'85 dB',color=RED,ha='left',fontsize=9)
for b,v in zip(bars,vals): ax.text(b.get_x()+b.get_width()/2,v+1.5 if v!=80 else v-6,str(v),ha='center',fontsize=9,color='black' if v!=80 else 'white')
ax.set_ylim(0,125); ax.set_ylabel('Sound level (dB)'); ax.tick_params(axis='x',labelsize=8)
save(fig,OUT+'QB_U7_noise.png')

# 5 ozone sites
t=np.linspace(8,22,200)
fig,ax=plt.subplots(figsize=(6.2,3.4))
ax.plot(t,25+53*g(t,13,2.4),color=RED,lw=2,label='Urban center')
ax.plot(t,25+71*g(t,15,2.6),color=ORANGE,lw=2,label='Suburb, 30 km downwind')
ax.plot(t,25+63*g(t,17,2.8),color=BLUE,lw=2,label='Rural site, 80 km downwind')
ax.set_xticks(range(8,23,2)); ax.set_xticklabels(['8 am','10 am','12 pm','2 pm','4 pm','6 pm','8 pm','10 pm'])
ax.set_xlabel('Time of day'); ax.set_ylabel('Ozone (ppb)'); ax.set_ylim(0,110); ax.legend(frameon=False,loc='upper left'); ax.grid(alpha=.25)
save(fig,OUT+'QB_U7_ozone_sites.png')

# 6 trends
yrs=np.arange(1990,2021,5)
so2=[100,68,45,30,19,12,12][:7]; so2=[100,66,44,29,20,14,12]
nox=[100,92,76,60,48,41,38]
pb=[100,50,26,14,8,5,3]
co2=[100,103,106,109,112,114,116]
fig,ax=plt.subplots(figsize=(6.2,3.5))
for y,c,l in ((so2,RED,'SO₂ emissions'),(nox,ORANGE,'NOₓ emissions'),(pb,GREEN,'Airborne lead'),(co2,BLUE,'Atmospheric CO₂')):
    ax.plot(yrs,y,color=c,lw=2,marker='o',ms=4,label=l)
ax.set_ylim(0,125); ax.set_xlabel('Year'); ax.set_ylabel('Index (1990 = 100)'); ax.legend(frameon=False,ncol=2,loc='upper center',bbox_to_anchor=(0.5,-0.18)); ax.set_ylim(0,130); ax.grid(alpha=.25)
save(fig,OUT+'QB_U7_trends.png')

# 7 school plan
fig,ax=canvas(6.2,3.3,(0,1),(0,1))
ax.add_patch(Rectangle((0.03,0.14),0.44,0.74,fc='white',ec=DARK,lw=1.6))
ax.add_patch(Rectangle((0.53,0.14),0.44,0.74,fc=LIGHT,ec=DARK,lw=1.6))
ax.text(0.25,0.93,'Wing A (not renovated)',ha='center',fontweight='bold',fontsize=9)
ax.text(0.75,0.93,'Wing B (renovated last summer)',ha='center',fontweight='bold',fontsize=9)
for (x0,lab) in ((0.03,'A'),(0.53,'B')):
    for i,(rx,ry) in enumerate([(0.06,0.52),(0.26,0.52),(0.06,0.16),(0.26,0.16)]):
        ax.add_patch(Rectangle((x0+rx,ry),0.17,0.32,fc='none',ec=GREY,lw=0.9))
        ax.text(x0+rx+0.085,ry+0.16,f'{lab}{i+1}',ha='center',va='center',fontsize=9)
ax.text(0.75,0.085,'New carpet, particleboard cabinets, fresh paint',ha='center',fontsize=7.5,style='italic')
ax.text(0.25,0.085,'Older floors and furniture',ha='center',fontsize=7.5,style='italic')
ax.text(0.50,0.02,'One shared ventilation unit serves both wings',ha='center',va='center',fontsize=7.5,color=RED)
save(fig,OUT+'QB_U7_school_plan.png')

# 8 lakes
yrs=np.array([1990,1995,2000,2005,2010,2015,2020])
so2=[480,430,340,260,190,150,132]; ph_a=[4.6,4.7,4.9,5.1,5.4,5.6,5.7]; ph_b=[6.9,6.9,6.8,6.9,7.0,6.9,7.0]
fig,(a1,a2)=plt.subplots(1,2,figsize=(6.4,3.1))
a1.plot(yrs,so2,color=RED,marker='o',lw=2); a1.set_ylim(0,550); a1.set_title('Plant SO₂ emissions',fontsize=10)
a1.set_ylabel('SO₂ (thousand metric tons/yr)'); a1.set_xlabel('Year'); a1.set_xticks([1990,2005,2020]); a1.grid(alpha=.25)
a2.plot(yrs,ph_a,color=BLUE,marker='o',lw=2,label='Lake Alder'); a2.plot(yrs,ph_b,color=GREEN,marker='s',lw=2,label='Lake Birch')
a2.set_ylim(4,8); a2.set_title('Lake pH',fontsize=10); a2.set_ylabel('pH'); a2.set_xlabel('Year'); a2.set_xticks([1990,2005,2020]); a2.legend(frameon=False,loc='lower right',bbox_to_anchor=(1.0,0.12),fontsize=8.5); a2.set_ylim(4,8); a2.grid(alpha=.25)
fig.tight_layout(); save(fig,OUT+'QB_U7_lakes.png')

# 9 PM days
days=['Dec 2','Dec 3','Dec 4','Dec 5','Dec 6','Dec 7','Dec 8','Dec 9']
pm=[14,18,61,78,92,23,12,85]; inv=[0,0,1,1,1,0,0,1]
fig,ax=plt.subplots(figsize=(6.2,3.2))
ax.bar(days,pm,color=[RED if i else SKY for i in inv],width=0.65)
for i,v in enumerate(pm): ax.text(i,v+1.5,str(v),ha='center',fontsize=8.5)
ax.set_ylabel('Daily mean PM2.5 (µg/m³)'); ax.set_ylim(0,105)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=RED,label='Thermal inversion present'),Patch(color=SKY,label='No inversion')],frameon=False,loc='upper left',fontsize=8.5)
save(fig,OUT+'QB_U7_pm_days.png')
