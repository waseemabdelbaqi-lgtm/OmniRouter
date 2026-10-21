import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
OUT='/home/user/OmniRouter/apes_project/content/book2/figs/'
def S(fig,n): save(fig,OUT+n)

# 1 food web
fig,ax=canvas(6.2,5.0)
W,H=0.26,0.085
pos={'Algae':(0.06,0.03),'Phytoplankton':(0.62,0.03),'Parrotfish':(0.06,0.25),'Zooplankton':(0.62,0.25),
     'Sardine':(0.62,0.47),'Grouper':(0.30,0.69),'Shark':(0.30,0.89)}
for k,(x,y) in pos.items(): box(ax,x,y,W,H,k,fs=10)
def c(k,top): x,y=pos[k]; return (x+W/2, y+H+0.02 if top else y-0.02)
def e(a,b):
    ax.add_patch(FancyArrowPatch((pos[a][0]+W/2,pos[a][1]+H+0.02),(pos[b][0]+W/2,pos[b][1]-0.02) if True else None,arrowstyle="-|>",mutation_scale=13,color=DARK,lw=1.4))
for a,b in [('Algae','Parrotfish'),('Phytoplankton','Zooplankton'),('Zooplankton','Sardine'),('Parrotfish','Grouper'),('Sardine','Grouper'),('Grouper','Shark')]: e(a,b)
ax.set_ylim(-0.1,1.0); ax.set_xlim(0,0.95)
ax.text(0.30,-0.06,"Arrows point in the direction of energy flow",fontsize=8,color=GREY,va="top")
S(fig,'PE2_foodweb.png')

# 2 species-area
rng=np.random.default_rng(4)
fig,ax=plt.subplots(figsize=(5.6,3.6))
A=np.array([1,2,3,5,8,12,20,35,60,90,150,250,400,700,1000,1200])
Sp=10+14*np.log10(A)+rng.normal(0,1.0,len(A))
ax.scatter(A,Sp,color=RED,zorder=3,s=26)
xx=np.logspace(0,3.15,50); ax.plot(xx,10+14*np.log10(xx),color=GREY,lw=1.5)
ax.set_xscale('log'); ax.set_xlabel('Fragment area (ha, log scale)'); ax.set_ylabel('Forest bird species (number)')
ax.set_ylim(0,70); ax.set_yticks(range(0,71,10)); ax.grid(True,which='both',alpha=.25)
S(fig,'PE2_speciesarea.png')

# 3 tolerance
T=np.linspace(20,36,400)
def g(c,w): return np.clip(1-((T-c)/w)**2,0,None)
fig,ax=plt.subplots(figsize=(5.6,3.4))
ax.plot(T,g(26.5,3.0),color=RED,lw=2,label='Species A'); ax.plot(T,g(27.5,6.0),color=BLUE,lw=2,label='Species B'); ax.plot(T,g(30,2.7),color=GREEN,lw=2,label='Species C')
ax.axvline(28,ymax=0.90,color=GREY,ls=':'); ax.axvline(30,ymax=0.90,color=GREY,ls='--')
ax.text(28,1.04,'28 °C',ha='center',fontsize=8,color=GREY); ax.text(30,1.04,'30 °C',ha='center',fontsize=8,color=GREY)
ax.set_xlabel('Mean reef water temperature (°C)'); ax.set_ylabel('Relative growth rate'); ax.set_ylim(0,1.12); ax.legend(frameon=False,loc='upper left',fontsize=8)
S(fig,'PE2_tolerance.png')

# 4 survivorship
x=np.linspace(0,100,300)
fig,ax=plt.subplots(figsize=(5.4,3.6))
ax.plot(x,np.clip(1000*(1-(x/100)**5),1,None),color=RED,lw=2,label='Curve X')
ax.plot(x,1000*np.exp(-0.046*x),color=BLUE,lw=2,label='Curve Y')
ax.plot(x,1000*10**(-3*(x/100)**0.35),color=GREEN,lw=2,label='Curve Z')
ax.set_yscale('log'); ax.set_ylim(1,1500); ax.set_xlim(0,100)
ax.set_xlabel('Percent of maximum life span'); ax.set_ylabel('Survivors per 1,000 born (log scale)'); ax.legend(frameon=False,fontsize=8,loc='lower left')
S(fig,'PE2_survivorship.png')

# 5 age structure
labs=['0–14','15–29','30–44','45–59','60–74','75+']
P=[17,14,10,6,2.5,0.5]; Q=[5.5,8.5,11,12.5,8.5,4]
fig,axs=plt.subplots(1,2,figsize=(6.4,3.3),sharey=True)
for ax,d,t in zip(axs,[P,Q],['Country P','Country Q']):
    y=np.arange(6)
    ax.barh(y,[-v for v in d],color=BLUE,label='Male'); ax.barh(y,d,color=ORANGE,label='Female')
    ax.set_yticks(y); ax.set_yticklabels(labs); ax.set_xlim(-20,20); ax.set_xticks([-15,-10,-5,0,5,10,15]); ax.set_xticklabels(['15','10','5','0','5','10','15'])
    ax.set_title(t); ax.set_xlabel('Percent of total population')
axs[0].set_ylabel('Age group (years)'); axs[1].legend(frameon=False,fontsize=8,loc='lower right')
fig.tight_layout(); S(fig,'PE2_agestructure.png')

# 6 DTM
xs=np.array([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]); xi=np.linspace(0,5,400)
from numpy import interp
birth=np.array([40,40,39.5,37,31,24,17,13,12,12,12]); death=np.array([37,36,34,24,14,10,9,9,9,9,9])
from scipy.interpolate import PchipInterpolator as PI
bi=PI(xs,birth)(xi); di=PI(xs,death)(xi)
fig,ax=plt.subplots(figsize=(6.0,3.5))
ax.plot(xi,bi,color=RED,lw=2,label='Birth rate'); ax.plot(xi,di,color=BLUE,lw=2,label='Death rate')
ax.fill_between(xi,di,bi,where=bi>di,color=SAND,alpha=.35)
for xb in [1,2,3,4]: ax.axvline(xb,color='#bbb',lw=.8)
for i,lab in enumerate(['1','2','3','4']): ax.text(i+0.5,46,'Stage '+lab if False else lab,ha='center',fontsize=10,fontweight='bold')
ax.text(0.05,46,'Stage',fontsize=8,color=GREY); 
ax.axvline(2.6,color=DARK,ls='--',lw=1.4); ax.text(2.63,5,'M',fontsize=12,fontweight='bold',color=DARK)
ax.set_ylim(0,52); ax.set_xlim(0,4.7); ax.set_xticks([]); ax.set_ylabel('Rate (per 1,000 people per year)'); ax.set_xlabel('Time →'); ax.legend(frameon=False,loc='center left',fontsize=8)
S(fig,'PE2_dtm.png')

# 7 El Nino
yrs=np.arange(2000,2024)
an=np.array([-0.8,-0.2,0.9,0.4,0.5,0.3,0.8,-1.0,-1.4,1.1,-1.3,-1.0,0.2,-0.2,0.3,2.4,0.7,-0.6,0.8,0.5,-1.0,-1.1,-1.0,1.9])
rng=np.random.default_rng(11); land=np.clip(9.5-2.8*an+rng.normal(0,0.5,len(an)),1.5,None)
fig,(a1,a2)=plt.subplots(2,1,figsize=(6.2,4.4),sharex=True,gridspec_kw={'height_ratios':[1,1]})
a1.bar(yrs,an,color=[RED if v>0 else BLUE for v in an]); a1.axhline(0,color='#444',lw=.8); a1.set_ylabel('Sea-surface temperature\nanomaly (°C)')
a2.plot(yrs,land,color=DARK,marker='o',ms=3.5); a2.set_ylabel('Anchovy landings\n(million t)'); a2.set_xlabel('Year'); a2.set_ylim(0,15)
fig.tight_layout(); S(fig,'PE2_elnino.png')

# 8 overfishing
y5=np.arange(1980,2021,5); catch=np.array([120,190,270,340,300,230,170,120,90]); boats=np.array([200,260,340,430,520,610,690,760,820]); cpue=catch/boats
fig,(a1,a2)=plt.subplots(1,2,figsize=(6.4,3.2))
a1.bar(y5,catch,width=3.5,color=SKY,edgecolor=BLUE,label='Total catch (thousand t)'); a1.set_ylabel('Total catch (thousand t)'); a1.set_xlabel('Year')
b=a1.twinx(); b.plot(y5,boats,color=RED,marker='o',ms=4); b.set_ylabel('Fishing boats (number)',color=RED); b.set_ylim(0,900); b.spines['right'].set_visible(True)
a1.set_ylim(0,400)
a2.plot(y5,cpue,color=DARK,marker='s',ms=4); a2.set_ylabel('Catch per boat (t per boat per year)'); a2.set_xlabel('Year'); a2.set_ylim(0,1.0)
fig.tight_layout(w_pad=2.5); S(fig,'PE2_overfish.png')

# 9 hydrograph
t=np.linspace(0,24,300)
def hyd(tp,qp,k): 
    return qp*((t/tp)*np.exp(1-t/tp))**k
fig,ax=plt.subplots(figsize=(5.6,3.3))
ax.plot(t,hyd(4,120,2.2)+3,color=RED,lw=2,label='Watershed X'); ax.plot(t,hyd(9,45,1.6)+3,color=GREEN,lw=2,label='Watershed Y')
ax.set_xlabel('Hours after start of storm'); ax.set_ylabel('Stream discharge (m³/s)'); ax.legend(frameon=False); ax.set_xlim(0,24); ax.set_ylim(0)
S(fig,'PE2_hydrograph.png')

# 10 energy mix
cn=['Country W','Country X','Country Y','Country Z']
mix={'Coal':[70,0,10,15],'Oil':[5,0,0,15],'Natural gas':[10,10,20,60],'Nuclear':[3,0,55,0],'Hydroelectric':[8,80,10,0],'Wind and solar':[4,10,5,10]}
cols={'Coal':'#444444','Oil':BROWN,'Natural gas':ORANGE,'Nuclear':'#7B5EA7','Hydroelectric':BLUE,'Wind and solar':GREEN}
fig,ax=plt.subplots(figsize=(6.4,3.3)); left=np.zeros(4)
for k,v in mix.items():
    ax.barh(cn,v,left=left,color=cols[k],label=k,edgecolor='white'); left+=np.array(v)
ax.invert_yaxis(); ax.set_xlim(0,100); ax.set_xlabel('Share of electricity generation (%)'); ax.legend(ncol=3,frameon=False,fontsize=8,loc='upper center',bbox_to_anchor=(0.5,-0.2))
S(fig,'PE2_energymix.png')

# 11 smog
h=np.linspace(0,24,300)
G=lambda m,s,a: a*np.exp(-0.5*((h-m)/s)**2)
NO=5+G(7.5,1.2,55)+G(18,1.5,20); NO2=10+G(9.5,1.8,35)+G(19,2,12); O3=8+G(14.5,2.6,82)
fig,ax=plt.subplots(figsize=(6.0,3.4))
ax.plot(h,NO,color=BLUE,lw=2,label='NO'); ax.plot(h,NO2,color=ORANGE,lw=2,label='NO₂'); ax.plot(h,O3,color=RED,lw=2,label='O₃')
ax.set_xticks(range(0,25,3)); ax.set_xticklabels(['0:00','3:00','6:00','9:00','12:00','15:00','18:00','21:00','24:00'])
ax.set_xlabel('Time of day (clear, sunny day)'); ax.set_ylabel('Concentration (ppb)'); ax.legend(frameon=False,loc='upper right'); ax.set_xlim(0,24); ax.set_ylim(0)
S(fig,'PE2_smog.png')

# 12 DO sag
d=np.linspace(0,60,300); tt=d/20.0
k1,k2,L0,D0,DOs=0.7,1.3,20.0,0.5,9.0
BOD=L0*np.exp(-k1*tt); D=(k1*L0/(k2-k1))*(np.exp(-k1*tt)-np.exp(-k2*tt))+D0*np.exp(-k2*tt); DO=DOs-D
print('DO min',DO.min(),d[DO.argmin()])
fig,ax=plt.subplots(figsize=(6.2,3.5))
ax.plot(d,DO,color=BLUE,lw=2,label='Dissolved oxygen (DO), left axis')
ax.axhline(5,color=GREY,ls='--',lw=1); ax.text(59,5.15,'5 mg/L',ha='right',fontsize=8,color=GREY)
ax.axvline(0,color=DARK,lw=1.4); ax.text(0.8,0.4,'Sewage\noutfall',fontsize=8,color=DARK)
ax.set_xlabel('Distance downstream of outfall (km)'); ax.set_ylabel('Dissolved oxygen (mg/L)',color=BLUE); ax.set_ylim(0,10); ax.set_xlim(-2,60)
b2=ax.twinx(); b2.plot(d,BOD,color=BROWN,lw=2,label='Biochemical oxygen demand (BOD), right axis'); b2.set_ylim(0,25); b2.set_ylabel('BOD (mg/L)',color=BROWN); b2.spines['right'].set_visible(True)
h1,l1=ax.get_legend_handles_labels(); h2,l2=b2.get_legend_handles_labels()
ax.legend(h1+h2,l1+l2,frameon=False,loc='upper right',fontsize=8,bbox_to_anchor=(1,1.0))
S(fig,'PE2_do.png')

# 13 dose-response
dose=np.logspace(-1,3,300)
def resp(l,s): return 100/(1+(l/dose)**s)
fig,ax=plt.subplots(figsize=(5.8,3.5))
ax.plot(dose,resp(40,1.8),color=GREEN,lw=2,label='Chemical P'); ax.plot(dose,resp(8,1.8),color=RED,lw=2,label='Chemical Q')
ax.axhline(50,color=GREY,ls=':'); ax.set_xscale('log'); ax.set_xlabel('Dose (mg per kg of body mass, log scale)'); ax.set_ylabel('Test animals killed (%)')
ax.set_ylim(0,105); ax.legend(frameon=False,loc='upper left'); ax.grid(True,which='both',axis='x',alpha=.25)
S(fig,'PE2_doseresponse.png')

# 14 CO2
mo=np.arange(108); yr=2016+mo/12
seas=np.array([0.7,1.5,2.4,3.8,4.5,3.4,1.0,-1.7,-4.0,-4.3,-2.4,-0.9]); seas-=seas.mean()
co2=404+2.4*(mo/12)+np.tile(seas,9)
fig,ax=plt.subplots(figsize=(6.0,3.2)); ax.plot(yr,co2,color=DARK,lw=1.6)
ax.set_xlabel('Year'); ax.set_ylabel('Atmospheric CO₂ (ppm)'); ax.set_xlim(2016,2025); ax.grid(alpha=.25)
S(fig,'PE2_co2.png')

# 15 coral
yr=np.arange(2012,2025)
sst=np.array([29.8,29.9,30.1,31.2,31.6,30.2,30.0,30.9,31.5,30.1,30.4,31.8,31.1]); bl=np.array([3,4,8,55,68,9,6,38,61,7,14,74,52])
fig,ax=plt.subplots(figsize=(6.2,3.4)); ax.bar(yr,bl,color=SAND,edgecolor=BROWN); ax.set_ylabel('Coral colonies bleached (%)'); ax.set_xlabel('Year'); ax.set_ylim(0,100)
b=ax.twinx(); b.plot(yr,sst,color=RED,marker='o',ms=4); b.axhline(30.5,color=RED,ls='--',lw=1); b.set_ylim(28.5,32.5); b.set_ylabel('Maximum summer SST (°C)',color=RED); b.spines['right'].set_visible(True)
b.text(2012.1,30.58,'30.5 °C',color=RED,fontsize=8)
fig.tight_layout(); S(fig,'PE2_coral.png')

# 16 forest loss
fig,ax=plt.subplots(figsize=(5.6,3.3)); reg=['Region P','Region Q','Region R']; a0=[6.0,14.0,3.0]; a1=[4.2,11.2,2.7]; xx=np.arange(3)
ax.bar(xx-0.2,a0,0.38,color=GREEN,label='2000'); ax.bar(xx+0.2,a1,0.38,color=BROWN,label='2020')
ax.set_xticks(xx); ax.set_xticklabels(reg); ax.set_ylabel('Forest area (million ha)'); ax.legend(frameon=False)
for i in range(3):
    ax.text(i-0.2,a0[i]+0.2,f'{a0[i]:.1f}',ha='center',fontsize=8); ax.text(i+0.2,a1[i]+0.2,f'{a1[i]:.1f}',ha='center',fontsize=8)
S(fig,'PE2_forestloss.png')

# 17 FRQ1 schematic
fig,ax=canvas(6.4,3.6,(0,10),(0,6))
ax.add_patch(Rectangle((0,0),3.2,6,fc='#E3CF9E',ec='#8B7A4A')); ax.text(1.6,5.0,'Oil-palm\nplantation',ha='center',fontsize=10,fontweight='bold')
ax.add_patch(Rectangle((3.2,0),6.8,6,fc='#9CC79F',ec='#3E7D4F')); ax.text(7.6,5.4,'Lowland rainforest fragment (400 ha)',ha='center',fontsize=10,fontweight='bold')
ax.plot([3.2,3.2],[0,6],color=RED,lw=2.4); ax.text(3.05,0.2,'Forest edge',color=RED,fontsize=8,rotation=90,va='bottom',ha='right')
for xx_,lab in [(3.2,'0 m'),(4.4,'100 m'),(5.6,'200 m'),(6.8,'300 m'),(8.0,'400 m')]:
    ax.plot([xx_,xx_],[2.0,2.2],color=DARK,lw=1); ax.text(xx_+(0.3 if lab=='0 m' else 0),1.7,lab,ha='center',fontsize=8)
ax.annotate('',xy=(8.0,2.4),xytext=(3.2,2.4),arrowprops=dict(arrowstyle='<->',color=DARK)); ax.text(5.6,2.6,'Distance from edge',ha='center',fontsize=9)
ax.plot([3.2,10],[4.3,3.8],color=BLUE,lw=5,alpha=.7,solid_capstyle='round'); ax.text(9.8,4.25,'Stream',color=BLUE,fontsize=8,ha='right')
S(fig,'PE2_frq1_fragment.png')

# 18 FRQ2 monthly
mon=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']; pm=[150,130,100,78,68,52,38,36,50,90,140,170]; inv=[14,11,6,3,2,0,0,0,1,5,12,16]
fig,ax=plt.subplots(figsize=(6.2,3.3)); ax.bar(mon,pm,color=SKY,edgecolor=BLUE); ax.set_ylabel('Monthly mean PM2.5 (µg/m³)'); ax.set_xlabel('Month, 2024'); ax.set_ylim(0,200); ax.tick_params(axis='x',labelsize=8)
b=ax.twinx(); b.plot(mon,inv,color=RED,marker='o',ms=4); b.set_ylabel('Thermal-inversion days (per month)',color=RED); b.set_ylim(0,20); b.spines['right'].set_visible(True)
fig.tight_layout(); S(fig,'PE2_frq2_monthly.png')
