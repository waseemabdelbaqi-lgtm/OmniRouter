import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
OUT='/home/user/OmniRouter/apes_project/content/book2/figs/'
def S(fig,name): save(fig,OUT+name)

def smooth(x,xs,ys,w=2.0):
    xi=np.linspace(min(xs),max(xs),400); yi=np.interp(xi,xs,ys)
    k=np.exp(-0.5*((np.arange(-40,41))/ (w*400/ (max(xs)-min(xs)) /1.0))**2); k/=k.sum()
    pad=np.pad(yi,40,mode='edge'); ys2=np.convolve(pad,k,mode='same')[40:-40]
    return xi,ys2

# ---------- U1 climate panels
mon=['J','F','M','A','M','J','J','A','S','O','N','D']
sites={'Site P':([5,8,6,3,1,0,0,1,1,2,4,6],[14,17,21,26,31,35,36,35,32,27,20,15]),
       'Site Q':([150,140,130,90,30,5,2,5,20,60,120,150],[25,25,26,26,25,23,22,23,24,25,25,25]),
       'Site R':([25,25,35,55,85,95,85,70,55,40,30,25],[-6,-4,2,9,15,20,23,22,16,9,2,-4])}
fig,axs=plt.subplots(1,3,figsize=(6.4,2.6),sharey=True)
for ax,(n,(p,t)) in zip(axs,sites.items()):
    ax.bar(range(12),p,color=BLUE,width=0.7)
    ax.set_xticks(range(12)); ax.set_xticklabels(mon,fontsize=7); ax.set_ylim(0,200); ax.set_title(n,fontsize=10)
    ax2=ax.twinx(); ax2.plot(range(12),t,color=RED,marker='o',ms=2.5,lw=1.4); ax2.set_ylim(-10,40)
    ax2.spines['right'].set_visible(True)
    if n!='Site R': ax2.set_yticklabels([]); ax2.tick_params(right=False)
    else: ax2.set_ylabel('Mean temperature (°C)',color=RED,fontsize=8)
axs[0].set_ylabel('Monthly precipitation (mm)',fontsize=8)
fig.tight_layout(); S(fig,'PE3_u1_climate.png')

# ---------- U2 tolerance
x=np.linspace(0,1000,500)
a=np.exp(-0.5*((x-600)/80)**2); b=0.8*np.exp(-0.5*((x-500)/200)**2)
fig,ax=plt.subplots(figsize=(5.6,3.0))
ax.plot(x,a,color=RED,lw=2,label='Grass species 1'); ax.plot(x,b,color=BLUE,lw=2,label='Grass species 2')
ax.axvline(300,color=GREY,ls='--',lw=1); ax.text(305,1.0,'Rainfall in\ndrought year',fontsize=8,color=GREY,va='top')
ax.set_xlabel('Mean annual rainfall (mm)'); ax.set_ylabel('Relative abundance'); ax.set_ylim(0,1.1); ax.legend(frameon=False,fontsize=9,loc='upper right')
S(fig,'PE3_u2_tolerance.png')

# ---------- U3 survivorship
t=np.linspace(0,100,200)
fig,ax=plt.subplots(figsize=(5.4,3.1))
iii=1000*np.exp(-0.075*t)*np.where(t<20,1,1)  # steep early loss
c3=np.where(t<12,1000*np.exp(-0.45*t/1.0),0);
y3=1000*np.where(t<10,np.exp(-0.5*t),np.exp(-5)*np.exp(-0.01*(t-10)))
y1=1000*np.where(t<70,1-0.02*(t/70)**2,0.98*np.exp(-0.18*(t-70)))
y2=1000*np.exp(-0.035*t)
ax.semilogy(t,y3,color=RED,lw=2,label='Curve A'); ax.semilogy(t,y1,color=BLUE,lw=2,label='Curve B'); ax.semilogy(t,y2,color=GREEN,lw=2,label='Curve C')
ax.set_ylim(1,1500); ax.set_xlabel('Percent of maximum lifespan'); ax.set_ylabel('Survivors per 1,000 born (log scale)'); ax.legend(frameon=False,fontsize=9)
S(fig,'PE3_u3_survivorship.png')

# ---------- U3 overshoot
xs=[0,6,12,18,24,30,36,42,48,54,60]; ys=[40,300,1500,2800,2000,1100,1000,1250,1450,1400,1400]
xi,yi=smooth(None,xs,ys,0.9)
fig,ax=plt.subplots(figsize=(5.4,3.0))
ax.plot(xi,yi,color=RED,lw=2); pass
ax.set_xlabel('Years since introduction'); ax.set_ylabel('Sheep population'); ax.set_ylim(0,3200)
S(fig,'PE3_u3_overshoot.png')

# ---------- U3 age structure
def pyr(ax,males,title):
    ages=['0–4','5–9','10–14','15–19','20–24','25–29','30–34','35–39','40–44','45–49','50–54','55–59','60–64','65–69','70–74','75–79','80+']
    y=np.arange(len(ages)); m=np.array(males); f=m*1.0
    ax.barh(y,-m,color=BLUE,height=0.85); ax.barh(y,f,color=ORANGE,height=0.85)
    ax.set_yticks(y[::2]); ax.set_yticklabels(ages[::2],fontsize=7); ax.set_title(title,fontsize=10)
    ax.set_xlim(-9,9); ax.set_xticks([-8,-4,0,4,8]); ax.set_xticklabels(['8','4','0','4','8'],fontsize=7)
    ax.set_xlabel('Percent of population',fontsize=8); ax.spines['left'].set_visible(False)
A=[8.0,7.0,6.2,5.4,4.6,3.9,3.2,2.6,2.1,1.6,1.2,0.9,0.7,0.5,0.3,0.2,0.1]
B=[2.1,2.2,2.4,2.5,2.7,3.1,3.4,3.9,4.3,4.5,4.4,4.1,3.8,3.6,3.4,3.1,3.4]
C=[3.7,3.8,4.0,4.3,4.5,4.4,4.3,4.0,3.6,3.2,2.8,2.4,1.9,1.5,1.1,0.8,0.7]
A,B,C=[list(np.array(v)/ (sum(v)*2)*100) for v in (A,B,C)]
for n,v in zip('ABC',[A,B,C]):
    mm=np.array(v); print(n,'sum(m)*2=',mm.sum()*2,'0-14',mm[:3].sum()*2/ (mm.sum()*2)*100,'15-64',mm[3:13].sum()/mm.sum()*100,'65+',mm[13:].sum()/mm.sum()*100)
fig,axs=plt.subplots(1,3,figsize=(6.6,3.0),sharey=True)
pyr(axs[0],A,'Country A'); pyr(axs[1],B,'Country B'); pyr(axs[2],C,'Country C')
axs[0].text(-8.7,16.6,'Male',fontsize=7,color=BLUE); axs[0].text(5.5,16.6,'Female',fontsize=7,color=ORANGE)
fig.tight_layout(); S(fig,'PE3_u3_agestructure.png')

# ---------- U3 transition
yr=[1900,1920,1940,1960,1980,2000,2020]; cbr=[42,42,41,39,31,22,14]; cdr=[40,34,24,14,8,6,6]
fig,ax=plt.subplots(figsize=(5.4,3.0))
ax.plot(yr,cbr,color=RED,marker='o',lw=2,label='Crude birth rate'); ax.plot(yr,cdr,color=BLUE,marker='s',lw=2,label='Crude death rate')
ax.set_xlabel('Year'); ax.set_ylabel('Rate (per 1,000 people per year)'); ax.set_ylim(0,50); ax.legend(frameon=False,fontsize=9,loc='lower left')
S(fig,'PE3_u3_transition.png')

# ---------- U4 soils
fig,axs=plt.subplots(1,2,figsize=(5.8,2.7))
axs[0].bar(['P','Q','R'],[120,6,28],color=[SAND,BROWN,GREEN]); axs[0].set_ylabel('Infiltration rate (mm/h)'); axs[0].set_title('Water entry',fontsize=10)
axs[1].bar(['P','Q','R'],[9,42,28],color=[SAND,BROWN,GREEN]); axs[1].set_ylabel('Water held after drainage\n(% of soil volume)'); axs[1].set_title('Water retention',fontsize=10)
for ax in axs: ax.set_xlabel('Soil sample')
fig.tight_layout(); S(fig,'PE3_u4_soils.png')

# ---------- U4 rain shadow
fig,ax=canvas(6.2,3.0,(0,10),(0,5))
ax.add_patch(Rectangle((0,0),2.4,0.9,fc=SKY,ec='none')); ax.text(1.2,0.35,'Ocean',ha='center',fontsize=9)
ax.add_patch(Polygon([(2.4,0.9),(5.0,3.6),(7.4,0.9),(10,0.9),(10,0),(2.4,0)],fc=SAND,ec='#444',lw=1))
ax.add_patch(Polygon([(2.4,0.9),(5.0,3.6),(7.4,0.9)],fc=BROWN,ec='#444',lw=1))
for (px,py,lab) in [(2.9,1.15,'1'),(4.0,2.55,'2'),(8.6,1.2,'3')]:
    ax.add_patch(Circle((px,py),0.17,fc=RED,ec='white')); ax.text(px,py,lab,color='white',ha='center',va='center',fontsize=8,fontweight='bold')
    ax.text(px,py+0.4,'Site '+lab,ha='center',fontsize=8)
arrow(ax,(0.3,1.6),(2.1,1.6)); ax.text(1.2,1.8,'Prevailing wind',ha='center',fontsize=8,color=DARK)
ax.set_xlim(0,10); ax.set_ylim(0,5)
S(fig,'PE3_u4_rainshadow.png')

# ---------- U4 ENSO
yrs=np.arange(2000,2014); sst=[-0.4,-0.1,0.9,1.0,0.3,0.5,0.8,-0.7,-1.0,-0.2,1.1,0.2,-0.6,-0.2]
catch=[10.5,9.9,6.8,6.1,9.0,8.2,7.4,11.3,11.9,10.0,6.5,8.8,11.0,10.2]
fig,ax=plt.subplots(figsize=(5.8,3.0))
ax.bar(yrs,sst,color=[ORANGE if s>0 else SKY for s in sst],width=0.7); ax.axhline(0,color='#444',lw=0.8)
ax.set_ylabel('Sea-surface temperature anomaly (°C)'); ax.set_xlabel('Year'); ax.set_ylim(-1.6,1.6)
ax2=ax.twinx(); ax2.plot(yrs,catch,color=RED,marker='o',ms=3.5,lw=1.6); ax2.set_ylim(0,14); ax2.spines['right'].set_visible(True)
ax2.set_ylabel('Anchovy catch (million t)',color=RED)
S(fig,'PE3_u4_enso.png')

# ---------- U5 overfishing
y=[2000,2004,2008,2012,2016,2020]; eff=[20,25,32,40,50,60]; cat=[4.0,5.2,6.4,6.8,5.6,4.2]; cpue=[c*1000/e for c,e in zip(cat,eff)]
fig,axs=plt.subplots(1,2,figsize=(6.3,2.8))
axs[0].bar(y,cat,width=2.6,color=BLUE); axs[0].set_ylabel('Total catch (thousand t)',color=BLUE); axs[0].set_ylim(0,8)
a2=axs[0].twinx(); a2.plot(y,eff,color=RED,marker='o',lw=1.6); a2.set_ylim(0,70); a2.spines['right'].set_visible(True); a2.set_ylabel('Fishing effort (thousand boat-days)',color=RED,fontsize=8)
axs[0].set_xticks(y); axs[0].set_xticklabels(y,fontsize=7,rotation=45)
axs[1].plot(y,cpue,color=GREEN,marker='s',lw=2); axs[1].set_ylabel('Catch per boat-day (kg)'); axs[1].set_ylim(0,260)
axs[1].set_xticks(y); axs[1].set_xticklabels(y,fontsize=7,rotation=45)
fig.tight_layout(); print('cpue',cpue); S(fig,'PE3_u5_overfishing.png')

# ---------- U6 mix
labs=['Country X','Country Y','Country Z']
data={'Coal':[55,5,20],'Natural gas':[25,20,40],'Nuclear':[0,60,30],'Hydropower':[15,10,5],'Geothermal, wind, solar':[5,5,5]}
cols=[DARK,ORANGE,YELLOW,BLUE,GREEN]
fig,ax=plt.subplots(figsize=(5.6,3.0)); left=np.zeros(3)
for (k,v),c in zip(data.items(),cols):
    ax.barh(labs,v,left=left,color=c,label=k,height=0.55,edgecolor='white')
    for i,(vv,l) in enumerate(zip(v,left)):
        if vv>=5: ax.text(l+vv/2,i,str(vv),ha='center',va='center',fontsize=8,color='white' if c in (DARK,BLUE,GREEN) else 'black')
    left+=np.array(v)
ax.set_xlabel('Share of electricity generation (%)'); ax.set_xlim(0,100); ax.invert_yaxis()
ax.legend(frameon=False,fontsize=7.5,ncol=3,loc='upper center',bbox_to_anchor=(0.5,-0.2))
S(fig,'PE3_u6_mix.png')

# ---------- U7 PM
fig,ax=plt.subplots(figsize=(5.2,2.9))
ax.bar(['Open three-stone\nwood fire','Improved biomass\nstove','LPG stove'],[480,190,30],color=[BROWN,ORANGE,TEAL],width=0.55)
ax.axhline(15,color=RED,ls='--',lw=1.2); ax.text(2.45,32,'Health-based guideline\n(15 µg/m³)',fontsize=7.5,color=RED,ha='right',va='bottom')
ax.set_ylabel('Indoor PM2.5, 24-h mean (µg/m³)'); ax.tick_params(axis='x',labelsize=8)
S(fig,'PE3_u7_pm.png')

# ---------- U7 smog
h=np.linspace(0,24,300)
g=lambda m,s,a: a*np.exp(-0.5*((h-m)/s)**2)
no=5+g(7.5,1.2,55)+g(18,1.5,18); no2=12+g(8.8,1.6,33)+g(18.5,1.8,10); o3=8+g(14.3,2.6,90)
fig,ax=plt.subplots(figsize=(5.6,3.0))
ax.plot(h,no,color=BLUE,lw=2,label='NO'); ax.plot(h,no2,color=ORANGE,lw=2,label='NO₂'); ax.plot(h,o3,color=RED,lw=2,label='O₃')
ax.set_xlim(0,24); ax.set_xticks(range(0,25,4)); ax.set_xlabel('Hour of day (0 = midnight)'); ax.set_ylabel('Concentration (ppb)'); ax.legend(frameon=False,fontsize=9)
S(fig,'PE3_u7_smog.png')

# ---------- U8 DO sag
d=np.linspace(-10,60,300)
do=np.where(d<0,9.0,9.0-6.5*np.exp(-0.5*((d-14)/9)**2)*(1-np.exp(-(d.clip(0))/6))-0.0)
m=np.exp(-12.07/30)-np.exp(-12.07/6)
do=np.where(d<0,9.0,9.0-6.5*((np.exp(-d.clip(0)/30)-np.exp(-d.clip(0)/6))/m))
do=np.where(d<0,9.0,do)
bod=np.where(d<0,2,2+23*np.exp(-d.clip(0)/14))
fig,ax=plt.subplots(figsize=(5.6,3.0))
ax.plot(d,do,color=BLUE,lw=2.2,label=None); pass
ax.axvline(0,color=GREY,lw=1); ax.text(0.8,9.3,'Wastewater outfall',fontsize=8,color=GREY)
ax.set_xlabel('Distance downstream of outfall (km)'); ax.set_ylabel('Dissolved oxygen (mg/L)'); ax.set_ylim(0,10.2); print('do min',do.min(),d[do.argmin()])
S(fig,'PE3_u8_dosag.png')

# ---------- U8 dose response
x=np.logspace(0,3.3,200); f=lambda ld,sl: 100/(1+(ld/x)**sl)
fig,ax=plt.subplots(figsize=(5.4,3.0))
ax.semilogx(x,f(20,2.2),color=RED,lw=2,label='Toxicant 1'); ax.semilogx(x,f(200,2.2),color=BLUE,lw=2,label='Toxicant 2')
ax.axhline(50,color=GREY,ls=':',lw=1); ax.set_xlabel('Dose (mg per kg body mass, log scale)'); ax.set_ylabel('Test animals that died (%)'); ax.set_ylim(0,100)
ax.legend(frameon=False,fontsize=9,loc='lower right')
S(fig,'PE3_u8_doseresponse.png')

# ---------- U9 CO2
mo=np.arange(0,132)/12; tr=389+2.4*mo; sea=3.0*np.cos(2*np.pi*(mo-0.38+0.0)) # peak ~May
co2=tr+3.0*np.cos(2*np.pi*(mo-(4.5/12)))
fig,ax=plt.subplots(figsize=(5.8,2.9))
ax.plot(2010+mo,co2,color=RED,lw=1.6); ax.set_xlabel('Year'); ax.set_ylabel('Atmospheric CO₂ (ppm)'); ax.set_xlim(2010,2021)
S(fig,'PE3_u9_co2.png')

# ---------- U9 invasive
yy=[2005,2008,2011,2014,2017,2020]; area=[120,190,300,480,760,1200]
fig,ax=plt.subplots(figsize=(5.4,2.9))
ax.plot(yy,area,color=RED,marker='o',lw=2); ax.set_xlabel('Survey year'); ax.set_ylabel('Area infested by shrub (ha)'); ax.set_ylim(0,1400)
S(fig,'PE3_u9_invasive.png')

# ---------- FRQ1 survey
fig,axs=plt.subplots(1,2,figsize=(5.8,2.7))
cats=['Not\ninvaded','Light','Heavy']
axs[0].bar(cats,[62,41,12],color=[GREEN,SAND,BROWN],width=0.6); axs[0].set_ylabel('Perennial grass cover (%)'); axs[0].set_title('Grass cover',fontsize=10)
axs[1].bar(cats,[9.1,7.4,4.8],color=[GREEN,SAND,BROWN],width=0.6); axs[1].set_ylabel('Soil moisture, 0–20 cm\n(% by volume)'); axs[1].set_title('Soil moisture (end of dry season)',fontsize=9)
for ax in axs: ax.set_xlabel('Shrub invasion level of survey plots')
fig.tight_layout(); S(fig,'PE3_frq1_survey.png')

# ---------- FRQ2 TFR
yrs=[1960,1970,1980,1990,2000,2010,2020]
fig,ax=plt.subplots(figsize=(5.6,3.0))
ax.plot(yrs,[6.8,6.9,6.8,6.5,6.2,5.7,5.1],color=RED,marker='o',lw=2,label='Country A')
ax.plot(yrs,[2.6,2.4,1.9,1.5,1.4,1.4,1.3],color=BLUE,marker='s',lw=2,label='Country B')
ax.plot(yrs,[6.0,5.4,4.2,3.3,2.9,2.3,1.9],color=GREEN,marker='^',lw=2,label='Country C')
ax.axhline(2.1,color=GREY,ls='--',lw=1); ax.text(1983,2.2,'Replacement level (2.1)',fontsize=8,color=GREY)
ax.set_xlabel('Year'); ax.set_ylabel('Total fertility rate\n(children per woman)'); ax.set_ylim(0,8); ax.legend(frameon=False,fontsize=9,ncol=3,loc='upper center',bbox_to_anchor=(0.5,1.12))
S(fig,'PE3_frq2_tfr.png')
