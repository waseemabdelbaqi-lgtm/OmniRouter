import sys, os
sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D=os.path.dirname(os.path.abspath(__file__))
def P(n): return os.path.join(D,'QB_U9_'+n+'.png')

# 1 Antarctic ozone
fig,ax=plt.subplots(figsize=(6,3.3))
m=['Jul','Aug','Sep','Oct','Nov','Dec']
ax.plot(m,[300,295,280,260,280,320],'-o',color=BLUE,label='1980')
ax.plot(m,[290,250,160,120,150,230],'-s',color=RED,label='2000')
ax.set_ylabel('Total ozone column (Dobson units)'); ax.set_xlabel('Month'); ax.set_ylim(80,350); ax.legend(frameon=False)
ax.set_title('Ozone over an Antarctic station')
save(fig,P('o3_antarctic'))

# 2 Keeling
t=np.arange(2016,2023.99,1/12)+1/24
mo=((t-2016)*12).astype(int)%12+0.5
co2=396+2.4*(t-2013)+3.0*np.cos(2*np.pi*(mo-4.5)/12)
fig,ax=plt.subplots(figsize=(6,3.3))
ax.plot(t,co2,color=RED,lw=1.4); ax.set_xlabel('Year'); ax.set_ylabel('Atmospheric CO₂ (ppm)')
ax.set_title('Monthly CO₂ at a remote mountaintop observatory'); ax.set_ylim(395,430)
save(fig,P('keeling'))

# 3 albedo loop
fig,ax=canvas(6.2,3.6)
box(ax,0.03,0.62,0.30,0.26,'Arctic air and\nocean temperature\nincrease',fs=9)
box(ax,0.62,0.62,0.30,0.26,'Area of sea ice\nand snow cover\ndecreases',fs=9)
box(ax,0.62,0.10,0.30,0.26,'More dark ocean\nis exposed',fs=9)
box(ax,0.03,0.10,0.30,0.26,'Surface reflects\nless sunlight;\nmore is absorbed',fs=9)
arrow(ax,(0.36,0.75),(0.59,0.75)); arrow(ax,(0.77,0.59),(0.77,0.39)); arrow(ax,(0.59,0.23),(0.36,0.23)); arrow(ax,(0.18,0.39),(0.18,0.59))
ax.text(0.475,0.50,'Arctic feedback\nprocess',ha='center',va='center',fontsize=9,color=DARK,style='italic')
save(fig,P('albedo_loop'))

# 4 ice core
pts=[(400,270),(380,235),(350,200),(335,190),(325,280),(300,250),(270,210),(250,190),(240,278),(215,240),(180,200),(150,185),(140,180),(125,285),(100,250),(70,215),(40,200),(20,185),(12,230),(8,270),(0,280)]
tk=np.array([p[0] for p in pts])[::-1]; cv=np.array([p[1] for p in pts])[::-1]
x=np.linspace(0,400,800); c=np.interp(x,tk,cv); tmp=(c-280)*0.085
fig,(a1,a2)=plt.subplots(2,1,figsize=(6,4.4),sharex=True)
a1.plot(x,c,color=RED); a1.axhline(420,color=GREY,ls='--',lw=1); a1.text(396,412,'2023 value: 420 ppm',ha='left',va='top',fontsize=9,color=GREY)
a1.set_ylabel('CO₂ (ppm)'); a1.set_ylim(160,440)
a2.plot(x,tmp,color=BLUE); a2.axhline(0,color=GREY,lw=0.6,ls=':'); a2.set_ylabel('Temperature\ndifference (°C)'); a2.set_xlabel('Thousands of years before present'); a2.invert_xaxis()
a1.set_title('Ice-core record (simplified values)')
save(fig,P('icecore'))

# 5 bleaching
xs=[0,1,2,3,4,5,6,7,8,9,10,12]; ys=[3,5,9,14,25,31,48,55,66,72,80,91]
fig,ax=plt.subplots(figsize=(6,3.4))
ax.scatter(xs,ys,color=RED,zorder=3); ax.scatter([9],[22],color=BLUE,marker='D',zorder=3)
ax.annotate('Reef K',(9,22),xytext=(9.4,12),fontsize=8,color=BLUE)
ax.set_xlabel('Weeks with water temperature above the bleaching threshold'); ax.set_ylabel('Coral colonies bleached (%)')
ax.set_title('Thirteen reefs after one warm season'); ax.set_ylim(0,100)
save(fig,P('bleaching'))

# 6 coral pH
ph=[7.80,7.90,8.00,8.10,8.20]; cal=[41,60,78,91,100]
fig,ax=plt.subplots(figsize=(6,3.3))
ax.plot(ph,cal,'-o',color=RED)
for a,b in zip(ph,cal): ax.annotate(str(b),(a,b),xytext=(0,6),textcoords='offset points',ha='center',fontsize=8)
ax.set_xlabel('Seawater pH in experimental tank'); ax.set_ylabel('Calcification rate\n(% of rate at pH 8.20)'); ax.set_ylim(30,108); ax.set_yticks(range(30,101,10))
ax.set_title('Coral calcification at five pH levels')
save(fig,P('coral_ph'))

# 7 invasive
yr=np.arange(0,31)
inv=1500/(1+((1500-20)/20)*np.exp(-0.4*yr)); inv=np.where(yr>=22,np.minimum(inv,1500*0.99+0.0),inv)
nat=300+700*np.exp(-0.17*yr)
fig,ax=plt.subplots(figsize=(6,3.3))
ax.plot(yr,inv,color=RED,label='Invasive shrub'); ax.plot(yr,nat,color=GREEN,label='Native shrub')
ax.set_xlabel('Years since invasive shrub arrived'); ax.set_ylabel('Plants per hectare'); ax.legend(frameon=False,loc='center right')
ax.set_title('Shrub densities in a forest preserve')
save(fig,P('invasive'))

# 8 fragments
fig,ax=plt.subplots(figsize=(5.2,4.0))
ax.add_patch(Rectangle((0,0),6,4,fc='#CFE3CF',ec=GREEN,lw=2))
for i in range(1,6): ax.plot([i,i],[0,4],color='#9FBF9F',lw=0.6)
for j in range(1,4): ax.plot([0,6],[j,j],color='#9FBF9F',lw=0.6)
ax.plot([4,4],[-0.35,4.35],color=BROWN,lw=5,solid_capstyle='butt'); ax.text(4.12,4.45,'Road',color=BROWN,fontsize=9,fontweight='bold')
ax.text(2,2,'Forest\npatch 1',ha='center',va='center',fontsize=10); ax.text(5,2,'Forest\npatch 2',ha='center',va='center',fontsize=10)
ax.set_xlim(-0.5,6.5); ax.set_ylim(-0.7,4.9); ax.set_aspect('equal')
ax.set_xlabel('Distance east–west (km)'); ax.set_ylabel('Distance north–south (km)')
ax.set_title('Forest crossed by a road (grid squares = 1 km × 1 km)',fontsize=10)
save(fig,P('fragments'))

# 9 hatchery
mm=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
phv=[8.05,8.05,8.02,7.98,7.92,7.88,7.85,7.86,7.90,7.97,8.02,8.05]; sv=[82,81,79,74,64,52,46,47,56,70,78,82]
fig,(a1,a2)=plt.subplots(2,1,figsize=(6,4.3),sharex=True)
a1.plot(mm,phv,'-o',color=BLUE); a1.set_ylabel('pH of intake\nseawater'); a1.set_title('Hatchery records over one year')
a2.bar(mm,sv,color=RED); a2.set_ylabel('Larvae surviving\nto day 14 (%)'); a2.set_xlabel('Month'); a2.tick_params(axis='x',labelsize=8); a2.set_ylim(0,100)
save(fig,P('hatchery'))

# 10 transect
fig,ax=canvas(6.2,3.0,xlim=(0,10),ylim=(0,5))
ax.add_patch(Rectangle((0,0),1,5,fc='#BDBDBD',ec=GREY)); ax.text(0.5,2.5,'Hiking\ntrail',rotation=90,ha='center',va='center',fontsize=9)
ax.add_patch(Rectangle((1,0),9,5,fc='#E3EFE0',ec=GREEN,lw=1.5))
rng=np.random.default_rng(3)
for px,n in [(2.2,14),(5.5,6),(9.0,2)]:
    ax.add_patch(Rectangle((px-0.5,1.5),1,2,fc='none',ec=DARK,lw=1.4,ls='--'))
    ax.scatter(px+rng.uniform(-0.4,0.4,n),2.5+rng.uniform(-0.9,0.9,n),s=14,color=RED,zorder=3)
for px,l in [(2.2,'Plot 1'),(5.5,'Plot 2'),(9.0,'Plot 3')]: ax.text(px,3.75,l,ha='center',fontsize=9)
arrow(ax,(1,0.6),(10,0.6),'distance from trail',fs=9,off=(0,0.1))
ax.scatter([1.3],[4.6],s=14,color=RED); ax.text(1.5,4.5,'= one invasive shrub',fontsize=8,va='center')
save(fig,P('transect'))

# 11 sea ice
ice=[6.3,5.6,4.9,4.5,3.9]; sv=[66,61,52,44,35]; yrs=[2000,2005,2010,2015,2020]
fig,ax=plt.subplots(figsize=(6,3.3))
ax.plot(ice,sv,'o',color=RED)
for a,b,y in zip(ice,sv,yrs): ax.annotate(str(y),(a,b),xytext=(5,4),textcoords='offset points',fontsize=8)
ax.set_xlabel('September sea ice extent (million km²)'); ax.set_ylabel('Polar bear cubs surviving\ntheir first year (%)')
ax.set_title('Cub survival and sea ice extent, five study years'); ax.set_xlim(3.4,6.9); ax.set_ylim(25,75)
save(fig,P('seaice_cubs'))
