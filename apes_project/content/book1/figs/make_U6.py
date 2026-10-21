import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book1/figs/'

# 1 energy mix
fig,ax=plt.subplots(figsize=(6.2,3.4))
src=['Oil','Coal','Natural gas','Nuclear','Hydro','Wind + solar','Biomass/other']
dev=[36,14,30,9,4,5,2]; dvg=[28,38,12,2,6,4,10]
x=np.arange(len(src)); w=0.38
ax.bar(x-w/2,dev,w,color=RED,label='Developed country (illustrative)')
ax.bar(x+w/2,dvg,w,color=SAND,label='Developing country (illustrative)')
ax.set_xticks(x); ax.set_xticklabels(src,rotation=20,ha='right')
ax.set_ylabel('Share of primary energy (%)'); ax.set_ylim(0,45)
ax.set_title('Energy mix of two example countries (illustrative values)')
ax.legend(frameon=False,fontsize=8)
for i,(a,b) in enumerate(zip(dev,dvg)):
    ax.text(i-w/2,a+0.8,str(a),ha='center',fontsize=7); ax.text(i+w/2,b+0.8,str(b),ha='center',fontsize=7)
save(fig,D+'U6_energy_mix.png')

# 2 steam plant
fig,ax=canvas(6.2,3.0)
box(ax,0.03,0.55,0.16,0.3,'Fuel\n(coal, gas,\nbiomass, or\nU-235 rods)',fc='#EADBC8',fs=8)
box(ax,0.25,0.5,0.17,0.4,'Boiler /\nreactor\n(heat makes\nsteam)',fc='#F6D5C0',fs=8)
box(ax,0.5,0.55,0.14,0.3,'Turbine',fc=LIGHT,fs=9,bold=True)
box(ax,0.72,0.55,0.14,0.3,'Generator',fc=LIGHT,fs=9,bold=True)
box(ax,0.5,0.08,0.18,0.25,'Condenser\n(steam → water)',fc='#D6E8F5',fs=8)
box(ax,0.78,0.08,0.19,0.25,'Cooling water\nor cooling tower\n(waste heat out)',fc='#D6E8F5',fs=8)
arrow(ax,(0.2,0.7),(0.25,0.7),'')
arrow(ax,(0.42,0.7),(0.5,0.7),'')
ax.text(0.46,0.76,'steam',ha='center',fontsize=7.5,color=DARK)
arrow(ax,(0.64,0.7),(0.72,0.7),'')
ax.text(0.68,0.76,'spins',ha='center',fontsize=7.5,color=DARK)
arrow(ax,(0.86,0.7),(0.96,0.7),'')
ax.text(0.9,0.77,'electricity',ha='center',fontsize=7.5,color=RED,fontweight='bold')
arrow(ax,(0.57,0.55),(0.57,0.33),'')
arrow(ax,(0.5,0.2),(0.34,0.2),'')
arrow(ax,(0.34,0.2),(0.34,0.5),'')
ax.text(0.34,0.03,'water returns to boiler',ha='center',fontsize=8)
arrow(ax,(0.68,0.2),(0.78,0.2),'')
ax.text(0.5,0.97,'Thermal power plant: the same steam cycle for coal, gas, biomass, and nuclear',ha='center',fontsize=9.5,fontweight='bold')
save(fig,D+'U6_steam_plant.png')

# 3 fission
fig,ax=canvas(6.2,3.0,(0,1),(0,1))
def nuc(x,y,r,c,t=''):
    ax.add_patch(Circle((x,y),r,fc=c,ec='black',lw=1)); 
    if t: ax.text(x,y,t,ha='center',va='center',fontsize=8,color='white',fontweight='bold')
ax.set_aspect('auto')
nuc(0.08,0.62,0.035,GREY,'n')
arrow(ax,(0.12,0.62),(0.22,0.62))
nuc(0.3,0.62,0.07,RED,'U-235')
ax.text(0.3,0.5,'unstable\nnucleus',ha='center',va='top',fontsize=8)
arrow(ax,(0.38,0.62),(0.46,0.62))
nuc(0.58,0.8,0.045,BLUE,'');nuc(0.58,0.44,0.05,GREEN,'')
ax.text(0.66,0.8,'smaller nucleus\n(fission product)',fontsize=8,va='center')
ax.text(0.66,0.44,'smaller nucleus\n(fission product)',fontsize=8,va='center')
for i,(dx,dy) in enumerate([(0.12,0.12),(0.13,-0.02),(0.12,-0.14)]):
    pass
nuc(0.55,0.62,0.02,GREY);nuc(0.64,0.62,0.02,GREY);nuc(0.73,0.62,0.02,GREY)
arrow(ax,(0.76,0.62),(0.84,0.62))
ax.text(0.92,0.62,'extra\nneutrons\n→ chain\nreaction',fontsize=8,va='center',ha='center')
ax.text(0.5,0.27,'+ large amount of heat  →  boils water  →  steam turns turbine',ha='center',fontsize=9,color=RED,fontweight='bold')
box(ax,0.05,0.04,0.42,0.14,'Control rods absorb neutrons (slow reaction)',fc='#E5E5E5',fs=8)
box(ax,0.53,0.04,0.42,0.14,'Fuel rods hold U-235 pellets; water = coolant',fc='#E5E5E5',fs=8)
ax.text(0.5,0.97,'Nuclear fission of uranium-235 (schematic)',ha='center',fontsize=10,fontweight='bold')
save(fig,D+'U6_fission.png')

# 4 capacity
fig,ax=plt.subplots(figsize=(6.2,3.2))
names=['Nuclear','Geothermal','Coal','Natural gas','Hydro','Wind','Solar PV']
cf=[92,75,50,55,40,35,25]
cols=[RED,BROWN,GREY,ORANGE,BLUE,TEAL,YELLOW]
ax.barh(names[::-1],cf[::-1],color=cols[::-1])
for i,v in enumerate(cf[::-1]): ax.text(v+1,i,f'{v}%',va='center',fontsize=8)
ax.set_xlim(0,105); ax.set_xlabel('Capacity factor (%)')
ax.set_title('Typical capacity factors (illustrative values)')
save(fig,D+'U6_capacity.png')

# 5 sankey-like
fig,ax=canvas(6.2,3.2,(0,1),(0,1))
ax.add_patch(Rectangle((0.03,0.2),0.14,0.6,fc=BROWN,ec='black'))
ax.text(0.1,0.5,'Coal\nenergy in\n100 units',ha='center',va='center',color='white',fontsize=8,fontweight='bold')
ax.add_patch(Rectangle((0.17,0.2),0.23,0.6,fc='#EFD9C5',ec='none'))
ax.text(0.285,0.5,'100 units\nflow in',ha='center',va='center',fontsize=8)
# boiler block
ax.add_patch(Rectangle((0.4,0.2),0.2,0.6,fc=ORANGE,ec='black'))
ax.text(0.5,0.5,'Plant\n(boiler,\nturbine,\ngenerator)',ha='center',va='center',fontsize=8,color='white',fontweight='bold')
ax.add_patch(Rectangle((0.6,0.2),0.3,0.2,fc=GREEN,ec='black'))   # 33% useful bottom? scale: 0.6 height = 100 -> 33 = 0.2
ax.text(0.75,0.3,'33 units electricity',ha='center',va='center',fontsize=8,color='white',fontweight='bold')
ax.add_patch(Rectangle((0.6,0.4),0.3,0.4,fc=RED,ec='black'))
ax.text(0.75,0.6,'67 units waste heat\n(to air and cooling water)',ha='center',va='center',fontsize=8,color='white',fontweight='bold')
ax.text(0.5,0.92,'Energy flow in a coal plant: efficiency = 33 ÷ 100 = 33% (illustrative values)',ha='center',fontsize=9.5,fontweight='bold')
ax.text(0.5,0.08,'Energy is conserved: 33 + 67 = 100. Waste heat is not destroyed; it is just not useful.',ha='center',fontsize=8.5)
save(fig,D+'U6_sankey.png')
