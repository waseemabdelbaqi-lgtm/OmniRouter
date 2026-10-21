import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
from matplotlib.patches import Wedge
D='/home/user/OmniRouter/apes_project/content/book1/figs/'
ICE='#E3F1FA'; ICEEDGE='#5C93B8'; SEA='#BFDDF0'; ROCK='#C9C2BB'; CLAY='#A9805A'; SANDC='#EBD9A8'; WATER='#7FB6DE'

# ---------------------------------------------------------------- 1 global water distribution
fig,ax=plt.subplots(figsize=(6.2,3.1))
def seg(y,parts,h=0.5):
    left=0
    for w,c,t,tc,ha in parts:
        ax.barh(y,w,left=left,height=h,color=c,edgecolor='white',lw=1)
        if t: ax.text(left+w/2,y,t,ha='center',va='center',fontsize=8.5,color=tc,fontweight='bold')
        left+=w
seg(1.0,[(97.5,BLUE,'Salt water (oceans, salty lakes, salty groundwater)  97.5%','white','c'),(2.5,SKY,'',None,None)])
ax.text(98.8,1.42,'Fresh water\n2.5%',fontsize=8.5,ha='center',va='bottom',color=DARK,fontweight='bold')
seg(0,[(69,'#DCEBF5','Glaciers, ice caps and ice sheets  about 69%',DARK,'c'),(30,TEAL,'Groundwater  about 30%','white','c'),(1,ORANGE,'',None,None)])
for r in ax.patches[:0]: pass
ax.annotate('Lakes, rivers, wetlands, soil moisture,\npermafrost, air and living things:\nonly about 1% of fresh water',(99.5,0),(70,-1.15),fontsize=8,ha='center',va='center',
            arrowprops=dict(arrowstyle='-|>',color=GREY),color=DARK)
ax.plot([97.5,0],[0.74,0.27],color=GREY,lw=0.8,ls=':'); ax.plot([100,100],[0.74,0.27],color=GREY,lw=0.8,ls=':')
ax.set_xlim(0,100); ax.set_ylim(-1.6,2.0); ax.set_yticks([1.0,0],['All water\non Earth','The fresh\n2.5% alone']); ax.set_xlabel('Percent of total volume (rounded)')
ax.spines['left'].set_visible(False); ax.tick_params(axis='y',length=0)
ax.set_title('Where Earth\'s water is',loc='left')
save(fig,D+'C3_water_distribution.png')

# ---------------------------------------------------------------- 2 water properties
fig=plt.figure(figsize=(6.2,3.0))
ax=fig.add_axes([0.0,0.02,0.5,0.9]); ax.set_xlim(0,10); ax.set_ylim(0,6); ax.axis('off'); ax.set_aspect('equal')
ax.set_title('Polar molecules and hydrogen bonds',fontsize=9.5,loc='left')
def h2o(cx,cy,flip=False):
    s=-1 if flip else 1
    ax.add_patch(Circle((cx,cy),0.62,fc='#E8A0A0',ec=RED,lw=1.2,zorder=3)); ax.text(cx,cy,'O',ha='center',va='center',fontsize=10,fontweight='bold',zorder=4)
    for ang in (52,-52):
        a=np.deg2rad(ang if not flip else 180-ang)
        hx,hy=cx+1.3*np.cos(a),cy+1.3*np.sin(a)
        ax.plot([cx,hx],[cy,hy],color=GREY,lw=2,zorder=2)
        ax.add_patch(Circle((hx,hy),0.38,fc='white',ec=BLUE,lw=1.2,zorder=3)); ax.text(hx,hy,'H',ha='center',va='center',fontsize=8.5,zorder=4)
        ax.text(hx+0.1*s*0,hy+(0.65 if ang>0 else -0.7),'δ+',ha='center',va='center',fontsize=8.5,color=BLUE,fontweight='bold')
    ax.text(cx+(-1.05 if not flip else 1.05),cy,'δ−',ha='center',va='center',fontsize=8.5,color=RED,fontweight='bold')
h2o(2.2,3.0,flip=False)
h2o(7.9,3.0,flip=True)
# hydrogen bond between H of left molecule (to the right) and O of right molecule
a=np.deg2rad(52); hx,hy=2.2+1.3*np.cos(a),3.0+1.3*np.sin(a)
ax.plot([hx+0.4,7.9-0.65],[hy,3.0],color=ORANGE,lw=1.8,ls=(0,(3,2)),zorder=1)
ax.text(5.15,4.55,'hydrogen bond\n(weak attraction)',ha='center',fontsize=8,color=ORANGE)
ax.text(5.0,0.25,'Bent shape: O end slightly negative (δ−),\nH ends slightly positive (δ+)',ha='center',fontsize=8,color=DARK)

ax2=fig.add_axes([0.6,0.2,0.38,0.62])
T=np.array([0,1,2,3,4,5,6,7,8,10]); rho=np.array([0.99984,0.99990,0.99994,0.99996,0.99997,0.99996,0.99994,0.99990,0.99985,0.99970])
ax2.plot(T,rho,'-o',color=RED,lw=2,ms=4)
ax2.annotate('Maximum density\nat 4 °C',(4,0.99997),(5.6,1.00002),fontsize=8,arrowprops=dict(arrowstyle='->',color=GREY))
ax2.text(0.1,0.99968,'Ice at 0 °C:\n0.917 g/cm³\n(far below this\naxis, so ice floats)',fontsize=7.5,color=BLUE)
ax2.set_ylim(0.99965,1.00007); ax2.set_xlim(-0.3,10.3)
ax2.set_xlabel('Liquid water temperature (°C)',fontsize=8.5); ax2.set_ylabel('Density (g/cm³)',fontsize=8.5)
ax2.tick_params(labelsize=7.5); ax2.yaxis.get_offset_text().set_fontsize(7)
ax2.ticklabel_format(axis='y',useOffset=False,style='plain')
ax2.set_title('Density of liquid water',fontsize=9.5,loc='left')
save(fig,D+'C3_water_properties.png')

# ---------------------------------------------------------------- 3 aquifer cross-section
fig,ax=plt.subplots(figsize=(6.4,4.4)); ax.set_xlim(0,10); ax.set_ylim(0,7.0); ax.axis('off')
SEAY=4.3
ax.add_patch(Rectangle((0,0),8.2,1.2,fc=ROCK,ec='none')); ax.text(0.15,0.6,'Impermeable bedrock',fontsize=8,va='center')
ax.add_patch(Polygon([(8.2,0),(10,0),(10,SEAY),(8.2,SEAY)],fc=SEA,ec='none')); ax.text(9.1,3.0,'Ocean',ha='center',fontsize=8.5,color=BLUE)
ax.add_patch(Rectangle((0,1.2),8.2,1.1,fc=WATER,ec='none',alpha=0.9)); ax.text(0.2,1.75,'Confined aquifer (saturated)',fontsize=8,va='center')
ax.add_patch(Rectangle((2.2,2.3),6.0,0.5,fc=CLAY,ec='none')); ax.text(5.2,2.55,'Aquitard (clay): confining layer',fontsize=8,color='white',ha='center',va='center')
wt=lambda x: 4.5-0.02*x
xs=np.linspace(0,8.2,200)
def wtc(x): return wt(x)-0.95*np.exp(-((x-3.9)/0.85)**2)
sat=[wtc(x) for x in xs]
ax.add_patch(Polygon([(0,2.3),(0,sat[0])]+list(zip(xs,sat))+[(8.2,2.8),(2.2,2.8),(2.2,2.3)],fc=WATER,ec='none',alpha=0.55))
gs=lambda x: 6.0-0.1*x
ax.add_patch(Polygon([(0,sat[0])]+list(zip(xs,sat))+[(x,gs(x)) for x in xs[::-1]],fc=SANDC,ec='none'))
ax.text(1.5,5.0,'Unsaturated\nzone (air\nin pores)',fontsize=7.5,va='center')
ax.plot(xs,sat,color=DARK,lw=1.8,ls='--'); ax.text(0.15,3.95,'Water table',fontsize=8.5,color=DARK,fontweight='bold')
ax.text(0.9,3.15,'Unconfined aquifer\n(saturated zone)',fontsize=8,va='center')
ax.plot(xs,[gs(x) for x in xs],color='#5a4a2a',lw=1.6)
for x0 in (0.35,0.75,1.15):
    ax.annotate('',(x0,wt(x0)+0.05),(x0,gs(x0)+0.6),arrowprops=dict(arrowstyle='-|>',color=BLUE,lw=1.4))
ax.text(0.2,6.85,'Rain and snowmelt: recharge',fontsize=8.5,color=BLUE,fontweight='bold',va='top')
def well(x,bottom,label,lx,ly,col='k',wl=None):
    ax.plot([x-0.1,x-0.1],[gs(x)+0.25,bottom],color='k',lw=1.2); ax.plot([x+0.1,x+0.1],[gs(x)+0.25,bottom],color='k',lw=1.2)
    ax.add_patch(Rectangle((x-0.2,gs(x)+0.1),0.4,0.2,fc=GREY,ec='k',zorder=5))
    ax.annotate(label,(x,gs(x)+0.3),(lx,ly),fontsize=8,ha='center',va='center',arrowprops=dict(arrowstyle='-',color=GREY))
well(3.9,3.0,'Pumping well',3.0,6.45)
well(5.6,1.6,'Confined well: water rises\nto dotted pressure level',5.15,6.4)
ax.add_patch(Rectangle((5.5,1.6),0.2,4.83-1.6,fc=WATER,ec='none',zorder=0))
pot=lambda x: 4.95-0.022*x
ax.plot([4.5,8.2],[pot(4.5),pot(8.2)],color=RED,lw=1.2,ls=':')
ax.annotate('Cone of\ndepression',(4.1,wtc(4.1)),(4.2,3.1),fontsize=8,ha='left',va='center',color=RED,arrowprops=dict(arrowstyle='->',color=RED))
ax.add_patch(Polygon([(8.2,2.8),(6.3,2.8),(8.2,3.95)],fc='#6F94BD',ec='none',alpha=0.9))
ax.text(7.55,3.15,'Salt wedge',fontsize=7.5,ha='center',va='center',color='white',fontweight='bold')
ax.text(8.9,5.35,'Heavy coastal pumping\ndraws the salt wedge\ninland: saltwater\nintrusion',fontsize=7.5,ha='center',va='bottom',color=DARK)
ax.annotate('',(6.95,gs(6.95)+0.05),(6.95,gs(6.95)+0.55),arrowprops=dict(arrowstyle='-|>',color=ORANGE,lw=1.8))
ax.text(6.95,gs(6.95)+0.95,'Land\nsubsidence',fontsize=7.5,color=ORANGE,va='center',ha='center',fontweight='bold')
ax.set_title('Aquifers in cross-section',loc='left',fontsize=11)
save(fig,D+'C3_aquifer.png')

# ---------------------------------------------------------------- 4 ice types
fig=plt.figure(figsize=(6.4,3.5))
ax=fig.add_axes([0.0,0.0,0.68,0.93]); ax.set_xlim(0,10); ax.set_ylim(0,5.2); ax.axis('off')
SL=1.9
ax.add_patch(Rectangle((4.7,0),5.3,SL,fc=SEA,ec='none'))
ax.add_patch(Polygon([(0,0),(4.7,0),(4.7,1.5),(0,1.7)],fc='#8B7B66',ec='none')); ax.text(1.2,0.7,'Bedrock',fontsize=8,color='white')
# ice sheet dome
th=np.linspace(0,1,50)
dx=np.linspace(0.2,4.7,80); base=1.7-0.2*(dx-0.2)/4.5
top=base+0.6*(dx-0.2)/4.5+1.9*np.clip(4*((dx-0.2)/4.5)*(1-(dx-0.2)/4.5),0,1)**0.6
ax.add_patch(Polygon([(0.2,1.7)]+list(zip(dx,top))+[(4.7,1.5)],fc=ICE,ec=ICEEDGE,lw=1.2))
ax.text(2.4,2.75,'Ice sheet / glacier\n(land ice)',fontsize=8.5,ha='center',color=DARK,fontweight='bold')
# ice shelf floating
ax.add_patch(Polygon([(4.7,SL+0.2),(6.5,SL+0.2),(6.5,SL-1.2),(4.7,SL-1.2)],fc=ICE,ec=ICEEDGE,lw=1.2)); ax.text(5.6,SL-0.45,'Ice\nshelf',fontsize=8,ha='center',va='center',color=DARK)
# iceberg
ax.add_patch(Polygon([(7.1,SL+0.22),(7.9,SL+0.22),(8.0,SL),(8.0,SL-0.5),(7.7,SL-1.45),(7.3,SL-1.45),(7.05,SL-0.7),(7.0,SL)],fc=ICE,ec=ICEEDGE,lw=1.2))
ax.text(7.5,SL-0.7,'Iceberg',fontsize=8,ha='center',va='center',color=DARK)
# sea ice
ax.add_patch(Rectangle((8.4,SL-0.18),1.6,0.28,fc='white',ec=ICEEDGE,lw=1.2)); ax.text(9.2,SL+0.5,'Sea ice\n(frozen seawater)',fontsize=8,ha='center',va='bottom',color=DARK,fontweight='bold')
ax.plot([4.7,10],[SL,SL],color=BLUE,lw=1.2); ax.text(9.7,0.3,'Ocean',fontsize=8.5,color=BLUE,ha='right')
ax.text(8.1,SL-0.75,'about 90% of an\niceberg is below\nthe surface',fontsize=7.5,ha='left',va='center',color=GREY)
ax.annotate('calving',(6.55,SL+0.1),(6.0,3.2),fontsize=8,ha='center',arrowprops=dict(arrowstyle='->',color=GREY))
ax.text(0.1,4.95,'Melting LAND ice adds water to the ocean: sea level rises.',fontsize=8,color=RED,va='center')
ax.text(10,4.55,'Melting FLOATING ice barely changes sea level.',fontsize=8,color=BLUE,va='center',ha='right')
ax.set_title('Polar ice',loc='left',fontsize=10.5)
ax=fig.add_axes([0.72,0.02,0.27,0.9]); ax.set_xlim(0,4); ax.set_ylim(0,6.9); ax.axis('off')
ax.add_patch(Rectangle((0,4.9),4,0.5,fc='#8FB16A',ec='none')); ax.text(2,5.15,'Tundra surface',fontsize=7.5,ha='center',va='center')
ax.add_patch(Rectangle((0,4.0),4,0.9,fc='#B79B72',ec='none')); ax.text(2,4.45,'Active layer\n(thaws each summer)',fontsize=7.5,ha='center',va='center')
ax.add_patch(Rectangle((0,1.3),4,2.7,fc='#9BB0BF',ec='none')); ax.text(2,2.65,'Permafrost\n(frozen 2+ years,\ncontains ice)',fontsize=7.5,ha='center',va='center')
ax.add_patch(Rectangle((0,0.2),4,1.1,fc='#B79B72',ec='none')); ax.text(2,0.75,'Unfrozen ground',fontsize=7.5,ha='center',va='center')
ax.annotate('Thaw releases\nCO₂ and CH₄',(2,5.45),(2,5.95),fontsize=7.5,ha='center',va='bottom',color=ORANGE,arrowprops=dict(arrowstyle='<-',color=ORANGE)) if False else ax.text(2,5.55,'Thaw releases\nCO₂ and CH₄',fontsize=7.5,ha='center',va='bottom',color=ORANGE,fontweight='bold')
ax.set_title('Permafrost',loc='center',fontsize=10.5,pad=2)
save(fig,D+'C3_ice_types.png')

# ---------------------------------------------------------------- 5 ocean zones
fig,ax=plt.subplots(figsize=(6.2,3.9))
zones=[(0,200,'Sunlight (euphotic) zone\nphotosynthesis possible','#8EC9EA'),(200,1000,'Twilight (dysphotic) zone\ndim light, no net photosynthesis','#4E8FBF'),
       (1000,4000,'Midnight (aphotic) zone\nno sunlight; near 2–4 °C','#27557F'),(4000,5000,'Abyssal zone (4,000–6,000 m)','#162B49')]
for a,b,t,c in zones: ax.axhspan(a,b,xmin=0,xmax=1,color=c,alpha=0.95)
ax.set_xlim(0,26); ax.set_ylim(5000,0); ax.set_yscale('function',functions=(lambda y: np.sqrt(np.clip(y,0,None)),lambda y: np.square(y))); ax.set_yticks([0,200,1000,2000,3000,4000,5000]); ax.set_yticklabels(['0','200','1,000','2,000','3,000','4,000','5,000'])
ax.text(0.4,100,'Sunlight zone: 0–200 m (warm mixed layer)',ha='left',va='center',fontsize=8.5,color='black',fontweight='bold')
ax.text(25.5,850,'Twilight zone: 200–1,000 m',ha='right',va='center',fontsize=8.5,color='white',fontweight='bold')
ax.text(25.5,2500,'Midnight zone: 1,000–4,000 m (no light)',ha='right',va='center',fontsize=8.5,color='white',fontweight='bold')
ax.text(25.5,4250,'Abyssal zone: 4,000–6,000 m',ha='right',va='center',fontsize=8.5,color='white',fontweight='bold')
ax.text(25.5,4900,'Hadal zone (trenches): 6,000 to about 11,000 m, below the axis',ha='right',va='bottom',fontsize=7.5,color='white')
d=np.array([0,50,100,200,400,600,800,1000,1500,2000,3000,4000,5000]); t=np.array([24,23.5,20,15,10,7,5.5,4.5,3.5,2.8,2.2,1.8,1.6])
ax.plot(t,d,color=ORANGE,lw=2.6); ax.plot(t,d,color='white',lw=0.6)
ax.annotate('Thermocline: temperature\nfalls steeply with depth',(10.5,420),(13,480),fontsize=8,color='white',va='center',arrowprops=dict(arrowstyle='->',color='white'))
ax.set_xlabel('Temperature of a tropical ocean (°C)'); ax.set_ylabel('Depth (m)')
ax.spines['left'].set_visible(True)
ax.set_title('Ocean zones and temperature with depth',loc='left')
save(fig,D+'C3_ocean_zones.png')

# ---------------------------------------------------------------- 6 currents and upwelling
fig=plt.figure(figsize=(6.4,3.3))
ax=fig.add_axes([0.0,0.02,0.52,0.88]); ax.set_xlim(-0.12,1.12); ax.set_ylim(0,1); ax.axis('off')
ax.add_patch(Rectangle((0,0),1,1,fc='#DCEBF5',ec=GREY,lw=1)); ax.add_patch(Rectangle((-0.12,0),0.12,1,fc=SAND,ec='none')); ax.add_patch(Rectangle((1,0),0.12,1,fc=SAND,ec='none'))
ax.text(-0.06,0.5,'continent',rotation=90,ha='center',va='center',fontsize=7.5); ax.text(1.06,0.5,'continent',rotation=90,ha='center',va='center',fontsize=7.5)
ax.axhline(0.5,color=GREY,lw=0.8,ls=':'); ax.text(0.97,0.505,'equator',ha='right',va='bottom',fontsize=7,color=GREY)
def ar(p,q,c): ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=13,color=c,lw=2.2))
for s,(cy) in ((1,0.75),(-1,0.25)):
    # equatorial side flows west, poleward side flows east
    ye=cy-0.2*s; yp=cy+0.2*s
    ar((0.85,ye),(0.15,ye),'#555')
    ar((0.15,yp),(0.85,yp),'#555')
    # west boundary: warm, flows poleward ; east boundary: cold, flows equatorward
    ar((0.1,ye),(0.1,yp),RED)
    ar((0.9,yp),(0.9,ye),BLUE)
ax.text(0.5,0.925,'westerly winds →',fontsize=7.5,ha='center',color=DARK,va='top'); ax.text(0.5,0.565,'← trade winds',fontsize=7.5,ha='center',color=DARK)
ax.text(0.5,0.435,'← trade winds',fontsize=7.5,ha='center',color=DARK,va='top'); ax.text(0.5,0.075,'westerly winds →',fontsize=7.5,ha='center',color=DARK,va='bottom')
ax.text(0.17,0.75,'warm\nwestern\ncurrent',fontsize=7.5,color=RED,va='center',ha='left'); ax.text(0.83,0.75,'cold\neastern\ncurrent',fontsize=7.5,color=BLUE,va='center',ha='right')
ax.text(0.5,0.75,'N. hemisphere\ngyre: clockwise',fontsize=8,ha='center',va='center',fontweight='bold'); ax.text(0.5,0.25,'S. hemisphere\ngyre: counter-\nclockwise',fontsize=8,ha='center',va='center',fontweight='bold')
ax.set_title('Surface currents of an ocean basin',loc='left',fontsize=9.5)
ax=fig.add_axes([0.56,0.02,0.43,0.88]); ax.set_xlim(0,10); ax.set_ylim(0,7); ax.axis('off')
ax.add_patch(Polygon([(0,1.2),(5.0,1.6),(7.4,3.2),(8.2,5.6),(0,5.6)],fc='#A9D3EE',ec='none'))
ax.add_patch(Polygon([(0,1.2),(5.0,1.6),(6.1,2.3),(6.3,2.9),(0,2.9)],fc='#2C5E86',ec='none'))
ax.add_patch(Polygon([(10,0),(10,6.4),(8.2,6.4),(8.2,5.6),(7.4,3.2),(5.0,1.6),(0,1.2),(0,0)],fc='#C9B98F',ec='none'))
ax.plot([0,8.2],[5.6,5.6],color=BLUE,lw=1.2)
ax.annotate('',(0.8,5.1),(5.6,5.1),arrowprops=dict(arrowstyle='-|>',color=DARK,lw=2.2)); ax.text(3.2,5.2,'surface water moves offshore',fontsize=7.5,ha='center',va='bottom',color=DARK)
ax.annotate('',(7.0,5.0),(4.6,2.0),arrowprops=dict(arrowstyle='-|>',color=ORANGE,lw=2.4,connectionstyle='arc3,rad=-0.2'))
ax.text(2.7,2.25,'cold, nutrient-rich\ndeep water',fontsize=7.8,color='white',ha='center',va='center',fontweight='bold')
ax.text(3.0,3.9,'upwelling: deep water\nrises to replace it',fontsize=7.8,color=DARK,ha='center',va='center',fontweight='bold')
ax.text(5.0,6.3,'Wind blows along the coast\ntoward the equator',fontsize=7.5,ha='center',va='center',color=DARK)
ax.text(8.9,2.6,'land',fontsize=8,ha='center')
ax.set_title('Coastal upwelling (section)',loc='left',fontsize=9.5)
save(fig,D+'C3_currents.png')
print('ok')
