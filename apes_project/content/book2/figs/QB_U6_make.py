import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book2/figs/'

# 1 energy mix
fig,ax=plt.subplots(figsize=(6.4,3.4))
groups=['Low-income\ngroup','Middle-income\ngroup','High-income\ngroup']
src=['Biomass (wood, charcoal)','Coal','Oil','Natural gas','Nuclear','Hydroelectric','Wind and solar']
vals=[[60,5,18,3,0,12,2],[15,40,22,12,2,7,2],[3,12,33,30,10,5,7]]
cols=[BROWN,"#444444",ORANGE,SKY,YELLOW,BLUE,GREEN]
left=np.zeros(3)
for i,s in enumerate(src):
    v=np.array([vals[g][i] for g in range(3)])
    ax.barh(groups,v,left=left,height=0.62,color=cols[i],edgecolor='white',label=s)
    for g in range(3):
        if v[g]>=5: ax.text(left[g]+v[g]/2,g,str(v[g]),ha='center',va='center',fontsize=9.5,color='white' if cols[i] in (BROWN,"#444444",BLUE,GREEN) else 'black')
        elif v[g]>0: ax.text(left[g]+v[g]/2,g-0.36,str(v[g]),ha='center',va='bottom',fontsize=9.5,color='black')
    left+=v
ax.set_ylim(2.55,-0.7); ax.set_xlim(0,100); ax.set_xlabel('Share of primary energy supply (%)')
ax.legend(ncol=3,fontsize=9.5,loc='upper center',bbox_to_anchor=(0.45,-0.2),frameon=False)
ax.set_title('Primary energy supply by source, three country groups')
save(fig,D+'QB_U6_mix.png')

# 2 PWR schematic
fig,ax=canvas(6.4,4.0,(0,16),(0,10))
def bx(x,y,w,h,t,fc=LIGHT): box(ax,x,y,w,h,t,fc=fc,fs=9.5)
bx(0.3,3.8,3.0,3.8,'Reactor\nvessel\n(fuel rods)',fc="#F2D7A8")
bx(5.3,3.8,3.0,3.8,'Steam\ngenerator')
bx(10.0,6.0,2.8,1.8,'Turbine',fc="#DDE8F2")
bx(13.4,6.0,2.5,1.8,'Generator',fc="#DDE8F2")
bx(9.8,2.0,3.6,2.2,'Condenser',fc="#DDE8F2")
bx(3.2,0.1,9.6,0.9,'River',fc=SKY)
def num(x,y,n):
    ax.add_patch(Circle((x,y),0.42,fc='white',ec=RED,lw=1.4,zorder=5)); ax.text(x,y,str(n),ha='center',va='center',fontsize=10.5,fontweight='bold',color=RED,zorder=6)
# primary loop (1: hot water out of reactor; return line below)
arrow(ax,(3.3,6.8),(5.3,6.8)); arrow(ax,(5.3,4.6),(3.3,4.6))
num(4.3,7.5,1)
# steam to turbine (2)
arrow(ax,(8.3,6.9),(10.0,6.9)); num(9.15,7.6,2)
arrow(ax,(12.8,6.9),(13.4,6.9))
# turbine exhaust to condenser
arrow(ax,(11.4,6.0),(11.4,4.2))
# condensed water back to steam generator (3)
ax.plot([9.8,6.8],[3.0,3.0],color=DARK,lw=1.4); arrow(ax,(6.8,3.0),(6.8,3.8))
num(8.3,3.0,3)
# river water: intake (left) and discharge (right)
arrow(ax,(10.6,1.0),(10.6,2.0),color=BLUE,lw=1.8)
arrow(ax,(12.6,2.0),(12.6,1.0),color=BLUE,lw=1.8)
num(13.5,1.5,4)
ax.text(0.3,9.3,'Reactor water, turbine steam and river water are in separate, sealed pathways',fontsize=9.5,color=GREY)
save(fig,D+'QB_U6_pwr.png')

# 3 decay
t=np.linspace(0,150,300); y=100*0.5**(t/30)
fig,ax=plt.subplots(figsize=(6,3.4))
ax.plot(t,y,color=RED,lw=2)
ax.set_xlim(0,150); ax.set_ylim(0,100); ax.set_xticks(range(0,151,15)); ax.set_yticks(range(0,101,12 if False else 10))
ax.grid(alpha=.35); ax.set_xlabel('Time since reactor shutdown (years)'); ax.set_ylabel('Activity remaining (% of original)')
ax.set_title('Radioactive decay of isotope Q in spent fuel')
save(fig,D+'QB_U6_decay.png')

# 4 solar day
h=np.linspace(0,24,481)
pv=np.where((h>6)&(h<18),4.0*np.clip(np.sin(np.pi*(h-6)/12),0,None)**1.5,0)
dem=0.5+1.3*np.exp(-((h-7.2)/1.3)**2)+0.5*np.exp(-((h-13)/2.5)**2)+2.7*np.exp(-((h-19.5)/1.9)**2)
fig,ax=plt.subplots(figsize=(6.2,3.4))
ax.plot(h,pv,color=ORANGE,lw=2.2,label='Rooftop PV output')
ax.plot(h,dem,color=BLUE,lw=2.2,label='Household electricity demand')
ax.set_xticks(range(0,25,3)); ax.set_xlim(0,24); ax.set_ylim(0,4.6); ax.grid(alpha=.3)
ax.set_xlabel('Hour of day (24-hour clock)'); ax.set_ylabel('Power (kW)'); ax.legend(frameon=False,loc='upper left',fontsize=9.5)
ax.set_title('One sunny day: PV output and household demand')
save(fig,D+'QB_U6_solar_day.png')

# 5 reserves
fig,ax=plt.subplots(figsize=(6.2,3.2))
reg=['A','B','C','D','E']; res=[48,13,8,20,11]; con=[9,24,31,15,21]
x=np.arange(5)
ax.bar(x-.19,res,.38,color=RED,label='Share of world proved crude oil reserves')
ax.bar(x+.19,con,.38,color=SKY,edgecolor=GREY,label='Share of world crude oil consumption')
for i in range(5):
    ax.text(x[i]-.19,res[i]+.8,res[i],ha='center',fontsize=9.5); ax.text(x[i]+.19,con[i]+.8,con[i],ha='center',fontsize=9.5)
ax.set_xticks(x); ax.set_xticklabels(['Region '+r for r in reg]); ax.set_ylabel('Percent of world total'); ax.set_ylim(0,58)
ax.legend(frameon=False,fontsize=9.5,loc='upper right'); ax.set_title('Oil reserves and oil consumption by region')
save(fig,D+'QB_U6_reserves.png')

# 6 coal flow
fig,ax=canvas(6.4,3.6,(0,16),(0,9))
box(ax,0.1,3,3.6,3,'Chemical energy\nin coal\n100 units',fc="#DDDDDD",fs=9.5,bold=True)
box(ax,5.8,3,3.8,3,'Steam power\nplant\n(boiler, turbine,\ngenerator)',fs=9.5)
box(ax,12.5,3.3,3.3,2.4,'Electricity\n35 units',fc="#DDE8F2",fs=9.5,bold=True)
arrow(ax,(3.7,4.5),(5.8,4.5)); arrow(ax,(9.6,4.5),(12.5,4.5))
box(ax,5.3,7.3,4.8,1.3,'Boiler and stack losses\n10 units',fs=9.5,fc="#FBEFD9",ec=ORANGE)
box(ax,9.8,0.2,5.9,1.5,'Heat discharged at condenser\n52 units',fs=9.5,fc="#FBEFD9",ec=ORANGE)
box(ax,1.4,0.2,4.2,1.5,'Generator and\nother losses\n3 units',fs=9.5,fc="#FBEFD9",ec=ORANGE)
arrow(ax,(7.7,6),(7.7,7.3),color=ORANGE); arrow(ax,(8.7,3),(11.5,1.7),color=ORANGE); arrow(ax,(6.7,3),(4.6,1.7),color=ORANGE)
ax.set_title('Energy flow in a coal-fired power plant (units per 100 units of fuel)')
save(fig,D+'QB_U6_coal_flow.png')

# 7 wind curve
v=np.linspace(0,30,601); P=np.minimum(3.5,v**3/500); P[v<3]=0; P[v>25]=0
fig,ax=plt.subplots(figsize=(6,3.5))
ax.plot(v,P,color=GREEN,lw=2.2)
ax.set_xlim(0,30); ax.set_ylim(0,4); ax.set_xticks(range(0,31,5)); ax.set_yticks([0,.5,1,1.5,2,2.5,3,3.5,4])
ax.grid(alpha=.35); ax.set_xlabel('Wind speed at hub height (m/s)'); ax.set_ylabel('Electrical power output (MW)')
ax.set_title('Power curve of one wind turbine')
save(fig,D+'QB_U6_wind_curve.png')

# 8 EROI
fig,ax=plt.subplots(figsize=(6.2,3.2))
names=['Coal','Conventional\noil','Natural\ngas','Corn\nethanol','Wind']; e=[30,18,20,1.8,20]
cl=["#444444",ORANGE,SKY,BROWN,GREEN]
b=ax.bar(names,e,color=cl)
for r,val in zip(b,e): ax.text(r.get_x()+r.get_width()/2,val+.6,str(val),ha='center',fontsize=9.5)
ax.set_ylabel('EROI (energy delivered ÷ energy invested)'); ax.set_ylim(0,35)
ax.set_title('Illustrative EROI values (hypothetical)')
save(fig,D+'QB_U6_eroi.png')

# 9 fracking cross-section
fig,ax=canvas(6.4,4.2,(0,16),(0,11))
ax.add_patch(Rectangle((0,8.5),16,2.5,fc="#D8C9A3",ec='none'))   # soil
ax.add_patch(Rectangle((0,6),16,2.5,fc=SKY,ec='none',alpha=.8))   # aquifer
ax.add_patch(Rectangle((0,3),16,3,fc="#B9B2A5",ec='none'))       # rock
ax.add_patch(Rectangle((0,1.2),16,1.8,fc="#4A4A4A",ec='none'))    # shale
ax.text(1.9,7.25,'Freshwater aquifer',ha='center',va='center',fontsize=9.5)
ax.text(8.25,4.5,'Sandstone and limestone',ha='center',va='center',fontsize=9.5)
ax.text(15.8,2.1,'Gas-bearing shale',ha='right',va='center',fontsize=9.5,color='white')
ax.text(0.2,10.4,'Land surface',fontsize=9.5)
# gas well
ax.plot([4,4],[11,2.1],color=RED,lw=3); ax.plot([4,12],[2.1,2.1],color=RED,lw=3)
ax.add_patch(Rectangle((3.5,11),1,0.6,fc=RED)); ax.text(3.3,11.9,'Gas well\npad',ha='right',fontsize=9.5)
for xm,n,d in [(6.5,'M1','0.3 km'),(10,'M2','1.2 km'),(13.5,'M3','4 km')]:
    ax.plot([xm,xm],[11,6.3],color=DARK,lw=2); ax.plot([xm],[11],'s',color=DARK)
    ax.text(xm,11.9,f'{n}\n{d}',ha='center',fontsize=9.5)
ax.text(8,0.9,'Not to scale (depths and horizontal spacing). M1–M3: monitoring wells screened in the aquifer;\ndistances are measured from the pad',ha='center',va='top',fontsize=9.5,color=GREY)
save(fig,D+'QB_U6_frack.png')
print('ok')
