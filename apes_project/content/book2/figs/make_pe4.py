import sys, math
sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book2/figs/'
def S(fig,n): save(fig,D+n)

# F01 energy pyramid
fig,ax=canvas(6.0,3.3,(0,10),(0,5.2))
tiers=[("Producers (phytoplankton)\n60,000 kJ/m²/yr",8.0,0.2),("Primary consumers\n?",5.6,1.35),("Secondary consumers\n600 kJ/m²/yr",3.4,2.5),("Tertiary consumers\n?",1.8,3.65)]
for t,w,y in tiers:
    ax.add_patch(Rectangle((5-w/2,y),w,1.05,fc=LIGHT if "?" not in t else "white",ec=RED,lw=1.3))
    ax.text(5,y+0.52,t,ha="center",va="center",fontsize=8.5)
ax.set_title("Energy flow in a taiga lake food chain",fontsize=10)
S(fig,'PE4_01_pyramid.png')

# F02 island biogeography
fig,ax=plt.subplots(figsize=(5.6,3.4))
A=np.logspace(0,3,100)
ax.plot(A,45*(A/100)**0.30,color=BLUE,lw=2,label="Islands less than 20 km from mainland")
ax.plot(A,30*(A/100)**0.30,color=RED,lw=2,label="Islands more than 100 km from mainland")
ax.set_xscale('log'); ax.set_xlabel("Island area (km²)"); ax.set_ylabel("Number of bird species")
ax.set_xticks([1,10,100,1000]); ax.set_xticklabels(["1","10","100","1,000"]); ax.set_ylim(0,110)
ax.grid(alpha=.3); ax.legend(fontsize=8,frameon=False,loc="upper left")
S(fig,'PE4_02_island.png')

# F03 tolerance
fig,ax=plt.subplots(figsize=(5.6,3.2))
T=np.linspace(16,38,300)
def tri(T,lo,opt,hi):
    y=np.where(T<opt,(T-lo)/(opt-lo),(hi-T)/(hi-opt)); return np.clip(y,0,1)*100
ax.plot(T,tri(T,22,26,30),color=BLUE,lw=2.2,label="Coral species X")
ax.plot(T,tri(T,20,28,36),color=RED,lw=2.2,label="Coral species Y")
ax.set_xlabel("Mean water temperature (°C)"); ax.set_ylabel("Relative growth rate (%)")
ax.set_ylim(0,110); ax.grid(alpha=.3); ax.legend(frameon=False,fontsize=9,loc="upper left")
S(fig,'PE4_03_tolerance.png')

# F04 survivorship
fig,ax=plt.subplots(figsize=(5.4,3.3))
x=np.linspace(0,100,200)
ax.plot(x,1000*np.where(x<80,1-0.02*(x/80)**4*40/40*1, 1)*np.clip(1-(x/100)**5,0.001,1),color=BLUE,lw=2,label="Curve A")
ax.plot(x,1000*np.exp(-0.046*x),color=GREEN,lw=2,label="Curve B")
ax.plot(x,1000*np.exp(-0.14*x)*0+1000*np.where(x<10,np.exp(-0.65*x),np.exp(-0.65*10)*np.exp(-0.03*(x-10))),color=RED,lw=2,label="Curve C")
ax.plot(x,1000*np.where(x<40,1-0.0*x,np.exp(-0.17*(x-40))),color=ORANGE,lw=2,ls="--",label="Curve D")
ax.set_yscale('log'); ax.set_ylim(1,1500)
ax.set_xlabel("Percent of maximum life span"); ax.set_ylabel("Number of survivors (log scale)")
ax.legend(frameon=False,fontsize=8.5,loc="lower left"); ax.grid(alpha=.3)
S(fig,'PE4_04_survivorship.png')

# F05 overshoot
fig,ax=plt.subplots(figsize=(5.6,3.2))
yrs=[1950,1954,1958,1961,1964,1966,1968,1970]; pop=[25,260,1200,3100,5600,2200,60,40]
xs=np.linspace(1950,1970,200)
from scipy.interpolate import PchipInterpolator
ax.plot(xs,PchipInterpolator(yrs,pop)(xs),color=RED,lw=2); ax.plot(yrs,pop,'o',color=DARK,ms=4)
ax.set_xlabel("Year"); ax.set_ylabel("Reindeer on Marsh Island"); ax.set_ylim(0,6500); ax.grid(alpha=.3)
ax.set_xticks(range(1950,1971,4))
S(fig,'PE4_05_overshoot.png')

# F06 age structure
fig,axs=plt.subplots(1,3,figsize=(6.2,3.0),sharey=True)
ages=["0–14","15–29","30–44","45–59","60–74","75+"]
data={"Country X":[17,14,11,8,4,1],"Country Y":[8,9,9,9,8,5],"Country Z":[5,7,9,10,11,9]}
for ax,(k,v) in zip(axs,data.items()):
    y=np.arange(6)
    ax.barh(y,[-i for i in v],color=BLUE,height=.85); ax.barh(y,v,color=RED,height=.85)
    ax.set_title(k,fontsize=9); ax.set_xlim(-20,20); ax.set_xticks([-15,-10,-5,0,5,10,15]); ax.set_xticklabels(["15","10","5","0","5","10","15"],fontsize=7)
    ax.set_yticks(y); ax.set_yticklabels(ages,fontsize=8)
    ax.set_xlabel("Percent of population",fontsize=8)
axs[0].text(-19,5.6,"Male",fontsize=7,color=BLUE); axs[0].text(5,5.6,"Female",fontsize=7,color=RED)
fig.tight_layout(); S(fig,'PE4_06_age.png')

# F07 demographic transition
fig,ax=plt.subplots(figsize=(5.8,3.4))
yy=[1900,1930,1950,1970,1990,2010,2040]
cbr=[41,41,40,38,26,18,12]; cdr=[36,33,28,14,9,7,9]
xs=np.linspace(1900,2040,300)
ax.plot(xs,PchipInterpolator(yy,cbr)(xs),color=RED,lw=2,label="Crude birth rate")
ax.plot(xs,PchipInterpolator(yy,cdr)(xs),color=BLUE,lw=2,label="Crude death rate")
ax.plot(yy,cbr,'o',color=RED,ms=3.5); ax.plot(yy,cdr,'o',color=BLUE,ms=3.5)
ax.set_xlabel("Year"); ax.set_ylabel("Rate (per 1,000 people per year)"); ax.set_ylim(0,45)
ax.set_xticks(range(1900,2041,20)); ax.grid(alpha=.35); ax.legend(frameon=False,fontsize=9,loc="center left")
S(fig,'PE4_07_demographic.png')

# F08 atmosphere
fig,ax=plt.subplots(figsize=(4.6,4.2))
alt=[0,11,20,32,47,51,71,85,100]; tmp=[15,-56,-56,-44,-2,-2,-86,-90,-40]
a=np.linspace(0,100,300); t=PchipInterpolator(alt,tmp)(a)
ax.plot(t,a,color=RED,lw=2.2)
for y in (11,50,85): ax.axhline(y,color=GREY,ls=":",lw=1)
for lab,y in (("W",5.5),("X",30),("Y",67),("Z",93)): ax.text(-118,y,lab,fontsize=14,fontweight="bold",color=DARK,va="center")
ax.set_xlim(-125,40); ax.set_xlabel("Temperature (°C)"); ax.set_ylabel("Altitude (km)"); ax.grid(alpha=.25)
S(fig,'PE4_08_atmosphere.png')

# F09 ENSO
fig,ax=plt.subplots(figsize=(6.0,3.2))
t=np.linspace(2008,2020,600)
def g(c,a,w): return a*np.exp(-((t-c)/w)**2)
an=g(2010.0,0.9,0.4)+g(2010.9,-1.6,0.55)+g(2015.7,2.3,0.55)+g(2013.2,-0.5,0.4)+g(2017.9,-0.9,0.4)+g(2019.0,0.6,0.3)+0.08*np.sin(9*t)
ax.plot(t,an,color=DARK,lw=1.6); ax.axhline(0,color="k",lw=.8)
ax.axhline(0.5,color=GREY,ls="--",lw=.8); ax.axhline(-0.5,color=GREY,ls="--",lw=.8)
ax.fill_between(t,0.5,an,where=an>0.5,color=RED,alpha=.35); ax.fill_between(t,-0.5,an,where=an<-0.5,color=BLUE,alpha=.35)
ax.annotate("P",(2015.7,2.3),xytext=(2015.7,2.62),ha="center",fontsize=12,fontweight="bold")
ax.annotate("Q",(2010.9,-1.6),xytext=(2010.9,-2.05),ha="center",fontsize=12,fontweight="bold")
ax.set_ylim(-2.4,3.0); ax.set_xlabel("Year"); ax.set_ylabel("Equatorial Pacific sea surface\ntemperature anomaly (°C)")
ax.set_xticks(range(2008,2021,2)); ax.grid(alpha=.25)
S(fig,'PE4_09_enso.png')

# F10 irrigation efficiency
fig,ax=plt.subplots(figsize=(5.2,3.2))
m=["Flood","Furrow","Sprinkler","Drip"]; e=[50,60,75,90]
b=ax.bar(m,e,color=[BROWN,SAND,BLUE,GREEN],width=.6)
for r,v in zip(b,e): ax.text(r.get_x()+r.get_width()/2,v+1.5,f"{v}%",ha="center",fontsize=9)
ax.set_ylabel("Irrigation efficiency (% of withdrawn\nwater reaching crop roots)"); ax.set_ylim(0,105)
S(fig,'PE4_10_irrigation.png')

# F11 emissions intensity
fig,ax=plt.subplots(figsize=(5.2,3.2))
m=["Coal","Natural gas","Solar PV","Wind"]; e=[1000,450,45,12]
b=ax.bar(m,e,color=[DARK,ORANGE,YELLOW,SKY],width=.6)
for r,v in zip(b,e): ax.text(r.get_x()+r.get_width()/2,v+20,f"{v:,}",ha="center",fontsize=9)
ax.set_ylabel("Life-cycle CO₂ emissions\n(g CO₂ per kWh of electricity)"); ax.set_ylim(0,1150)
S(fig,'PE4_11_emissions.png')

# F12 biofuel energy
fig,ax=plt.subplots(figsize=(5.4,3.4))
labels=["Corn ethanol","Switchgrass ethanol"]
farm=[7.0,3.0]; trans=[1.0,1.5]; proc=[10.0,5.5]
x=np.arange(2)
ax.bar(x,farm,.5,color=GREEN,label="Growing and harvesting")
ax.bar(x,trans,.5,bottom=farm,color=SAND,label="Transport")
ax.bar(x,proc,.5,bottom=np.array(farm)+np.array(trans),color=BROWN,label="Conversion to fuel")
ax.axhline(21,color=RED,ls="--",lw=1.5); ax.text(1.42,21.4,"Energy in 1 L of ethanol = 21 MJ",ha="right",fontsize=8.5,color=RED)
ax.set_xticks(x); ax.set_xticklabels(labels); ax.set_ylabel("Fossil energy input (MJ per liter)"); ax.set_ylim(0,25)
ax.legend(frameon=False,fontsize=8,loc="upper left",bbox_to_anchor=(0,0.88)); ax.set_xlim(-.5,1.5)
S(fig,'PE4_12_biofuel.png')

# F13 smog
fig,ax=plt.subplots(figsize=(5.8,3.3))
h=np.linspace(0,24,400)
def b(c,a,w): return a*np.exp(-((h-c)/w)**2)
no=4+b(7.5,38,1.5)+b(18,10,1.5)
no2=14+b(9,26,2.0)+b(19,10,2.0)
o3=18+b(14.5,70,3.2)
ax.plot(h,no,color=BLUE,lw=2,label="NO"); ax.plot(h,no2,color=ORANGE,lw=2,label="NO₂"); ax.plot(h,o3,color=RED,lw=2,label="O₃")
ax.set_xticks(range(0,25,3)); ax.set_xlabel("Hour of day (24-hour clock)"); ax.set_ylabel("Concentration (ppb)")
ax.legend(frameon=False,fontsize=9,loc="upper left"); ax.grid(alpha=.3)
S(fig,'PE4_13_smog.png')

# F14 dose response
fig,ax=plt.subplots(figsize=(5.6,3.4))
d=np.logspace(-0.3,3,300)
ax.plot(d,100/(1+(8/d)**2),color=RED,lw=2.2,label="Chemical X")
ax.plot(d,100/(1+(120/d)**4),color=BLUE,lw=2.2,label="Chemical Y")
ax.axhline(50,color=GREY,ls=":",lw=1)
ax.set_xscale('log'); ax.set_xlim(0.5,1000); ax.set_ylim(0,100)
ax.set_xticks([1,10,100,1000]); ax.set_xticklabels(["1","10","100","1,000"])
ax.set_yticks(range(0,101,10))
ax.set_xlabel("Dose (mg per kg body mass, log scale)"); ax.set_ylabel("Test animals dead (%)")
ax.legend(frameon=False,fontsize=9,loc="upper left"); ax.grid(alpha=.3,which="both",axis="y")
ax.grid(alpha=.25,which="major",axis="x")
S(fig,'PE4_14_dose.png')

# F15 Keeling-like
fig,ax=plt.subplots(figsize=(5.8,3.2))
t=np.linspace(2016,2021.99,72)
co2=409+2.4*(t-2016)+3.0*np.cos(2*np.pi*(t-2016.37))
ax.plot(t,co2,color=DARK,lw=1.6)
ax.set_xlabel("Year"); ax.set_ylabel("Atmospheric CO₂ (ppm)"); ax.set_xticks(range(2016,2023)); ax.grid(alpha=.3)
S(fig,'PE4_15_co2.png')

# F16 ice core
fig,ax=plt.subplots(figsize=(6.0,4.0),sharex=True,nrows=2)
k=np.linspace(0,400,500)  # thousand years before present
base=np.cos(2*np.pi*(k-10)/100)  # warm near 0,100,... (interglacial peaks at ~10,110,...)
ph=0.25*np.cos(2*np.pi*(k-10)/41)
sig=base+ph
co2=230+50*sig*0.9+8*np.sin(k/3.1); tmp=-4+3.2*sig+0.4*np.sin(k/2.3)
co2=np.clip(co2,180,300)
ax[0].plot(k,co2,color=RED,lw=1.5); ax[0].set_ylabel("CO₂ (ppm)"); ax[0].plot([0],[425],'o',color=DARK,ms=6); ax[0].annotate("Present: 425 ppm",(0,425),xytext=(95,395),fontsize=8.5,arrowprops=dict(arrowstyle="-",color=GREY))
ax[0].set_ylim(160,450)
ax[1].plot(k,tmp,color=BLUE,lw=1.5); ax[1].set_ylabel("Temperature change\nfrom today (°C)"); ax[1].set_xlabel("Thousands of years before present")
ax[1].invert_xaxis(); 
for a_ in ax: a_.grid(alpha=.25)
fig.tight_layout(); S(fig,'PE4_16_icecore.png')

# F17 pH
fig,ax=plt.subplots(2,1,figsize=(5.6,4.2),sharex=True)
yrs=np.arange(1990,2021)
pco2=355+(410-355)*(yrs-1990)/30+2.5*np.sin(yrs*1.7)
ph=8.11-0.06*(yrs-1990)/30+0.004*np.sin(yrs*2.3)
ax[0].plot(yrs,pco2,color=BLUE,lw=1.6); ax[0].set_ylabel("Surface seawater\npCO₂ (µatm)")
ax[1].plot(yrs,ph,color=RED,lw=1.6); ax[1].set_ylabel("Surface seawater pH"); ax[1].set_xlabel("Year")
ax[1].set_ylim(8.03,8.13)
for a_ in ax: a_.grid(alpha=.3)
ax[1].annotate("1990: pH 8.11",(1990,8.11),xytext=(1993,8.12),fontsize=8.5); ax[1].annotate("2020: pH 8.05",(2020,8.05),xytext=(2010.5,8.04),fontsize=8.5)
fig.tight_layout(); S(fig,'PE4_17_ph.png')

# F18 ozone
fig,ax=plt.subplots(figsize=(6.0,3.4))
rng=np.random.RandomState(4)
yrs=np.arange(1979,2024)
sm=np.interp(yrs,[1979,1985,1990,1995,2000,2005,2010,2015,2023],[225,170,110,105,102,112,118,122,128])
noise=rng.normal(0,7,len(yrs)); val=sm+noise
ax.plot(yrs,val,'-o',color=DARK,ms=3,lw=1.2)
ax.axhline(220,color=GREY,ls="--",lw=1); ax.text(1980,226,"220 DU",fontsize=8,color=GREY)
ax.axvline(1987,color=RED,lw=1.5); ax.text(1987.6,235,"1987 Montreal Protocol signed",fontsize=8,color=RED)
ax.set_ylim(60,260); ax.set_xlabel("Year"); ax.set_ylabel("Minimum October ozone column\nover Antarctica (Dobson units)")
ax.grid(alpha=.25); S(fig,'PE4_18_ozone.png')

# FRQ1 schematic
fig,ax=canvas(6.4,3.5,(0,12),(0,6.6))
box(ax,0.2,3.6,3.1,2.2,"Irrigated cotton fields\n(herbicide applied\neach spring)",fc="#EAF2D8",ec=GREEN,fs=8.5)
box(ax,0.2,0.5,3.1,1.7,"Irrigation supply canal\n(Site 1)",fc="#DCEBF5",ec=BLUE,fs=8.5)
box(ax,4.7,3.6,2.8,2.2,"Return-flow drain\n(Site 2)",fc="#DCEBF5",ec=BLUE,fs=8.5)
box(ax,8.8,3.6,3.0,2.2,"Desert wetland pond\n(Site 3)\nfrog breeding habitat",fc="#DCEBF5",ec=BLUE,fs=8.5)
box(ax,8.8,0.5,3.0,1.7,"Reference pond\n(Site 4)\nno upstream farms",fc="#F1F1F1",ec=GREY,fs=8.5)
arrow(ax,(1.7,2.3),(1.7,3.5),"canal water",fs=7.5,off=(0.9,-0.2))
arrow(ax,(3.4,4.7),(4.6,4.7),"runoff",fs=7.5)
arrow(ax,(7.6,4.7),(8.7,4.7),"flow",fs=7.5)
ax.text(6,0.3,"Not to scale. Sites 3 and 4 are 25 km apart in the same desert valley.",ha="center",fontsize=8,color=GREY)
S(fig,'PE4_FRQ1_canal.png')

# FRQ2
yrs=[2000,2005,2010,2015,2020,2025]; co=[369,380,390,401,413,425]; al=[42,44,47,51,56,61]; ice=[6.3,5.6,4.9,4.6,3.9,3.6]
fig,axs=plt.subplots(1,2,figsize=(6.4,3.1))
axs[0].plot(yrs,co,'-o',color=RED,lw=2,ms=4); axs[0].set_ylabel("Atmospheric CO₂ (ppm)"); axs[0].set_xlabel("Year"); axs[0].grid(alpha=.3)
axs[0].set_xticks(yrs); axs[0].tick_params(axis='x',labelsize=7)
axs[1].bar([str(y) for y in yrs],al,color=BROWN,width=.6); axs[1].set_ylabel("Active-layer thickness (cm)",color=BROWN)
axs[1].set_ylim(0,70); axs[1].tick_params(axis='x',labelsize=7)
a2=axs[1].twinx(); a2.plot([str(y) for y in yrs],ice,'-s',color=BLUE,lw=2,ms=4); a2.set_ylim(0,8); a2.set_ylabel("Sea-ice minimum extent\n(million km²)",color=BLUE); a2.spines['right'].set_visible(True)
fig.tight_layout(); S(fig,'PE4_FRQ2_arctic.png')
print("ok")
