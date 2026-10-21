import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
OUT='/home/user/OmniRouter/apes_project/content/book1/figs/'

# 1. Greenhouse effect (corrected: reflected sunlight arrow points away from Earth)
fig,ax=canvas(6.2,4.2,(0,10),(0,7))
ax.add_patch(Rectangle((0,0),10,0.9,fc=GREEN,ec='none',alpha=.8)); ax.text(5,0.38,"Earth's surface",ha='center',color='white',fontsize=10,fontweight='bold')
ax.add_patch(Rectangle((0,3.4),10,1.9,fc=SKY,ec='none',alpha=.35)); ax.text(9.9,5.05,"Troposphere:\ngreenhouse gases",ha='right',va='top',fontsize=8,color=BLUE)
ax.add_patch(Circle((1.2,6.1),0.6,fc=YELLOW,ec=ORANGE)); ax.text(1.95,6.15,"Sun",fontsize=9,va='center')
arrow(ax,(1.5,5.5),(2.4,1.0),color=ORANGE,lw=2); ax.text(0.1,2.5,"1  Sunlight\n    passes through",fontsize=8,color=ORANGE)
arrow(ax,(3.5,5.4),(4.1,6.7),color=GREY); ax.text(4.25,6.0,"About 30% of sunlight\nreflected (clouds, ice)",fontsize=7.5,color=GREY,ha='left')
arrow(ax,(3.0,1.0),(3.0,3.3),color=RED,lw=2); ax.text(3.15,1.7,"2  Surface emits\n    infrared (heat)",fontsize=8,color=RED)
arrow(ax,(6.9,3.5),(6.9,6.8),color=GREY,lw=1.6); ax.text(7.05,6.35,"Some infrared\nescapes to space",fontsize=8,color=GREY)
arrow(ax,(8.5,4.3),(8.9,1.1),color=RED,lw=2,rad=-0.1); ax.text(8.3,2.3,"3  Gases re-radiate IR\n    back toward surface\n    → warmer surface",fontsize=8,color=RED,ha='right')
ax.text(3.9,4.3,"CO₂  CH₄  N₂O  H₂O  CFCs",ha='center',fontsize=9,fontweight='bold',color=DARK)
ax.set_title("Greenhouse effect: energy in, infrared trapped")
save(fig,OUT+'C11_greenhouse_effect.png')

# 2. Ozone profile
fig,ax=plt.subplots(figsize=(6.2,3.9))
z=np.linspace(0,50,400)
strat=9.0*np.exp(-((z-25)/7.5)**2)
trop=0.9*np.exp(-z/8)
o3=strat+trop+0.15
ax.axhspan(15,35,color=SKY,alpha=.35); ax.plot(o3,z,color=RED,lw=2.4)
ax.axhline(12,color=GREY,ls='--',lw=1); ax.text(10.3,12.8,"tropopause (about 12 km)",fontsize=8,color=GREY,ha='right')
ax.text(10.3,34.0,"Ozone layer\n(about 15–35 km)",fontsize=9,fontweight='bold',color=BLUE,ha='right',va='top')
ax.annotate("Peak ozone near 20–30 km:\n'good' ozone absorbs UV-B and UV-C",xy=(9.2,25),xytext=(10.3,43),fontsize=8.5,color=DARK,ha='right',arrowprops=dict(arrowstyle='-|>',color=DARK))
ax.annotate("Ground-level ozone:\nsmall amount, a pollutant ('bad')",xy=(1.1,2),xytext=(3.3,4),fontsize=8.5,color=DARK,arrowprops=dict(arrowstyle='-|>',color=DARK))
ax.set_xlim(0,10.5); ax.set_ylim(0,50)
ax.set_xlabel("Ozone concentration (relative scale, illustrative)"); ax.set_ylabel("Altitude (km)")
ax.set_title("Where ozone is found in the atmosphere")
save(fig,OUT+'C11_ozone_profile.png')

# 3. Chlorine and polar ozone (illustrative)
yrs=np.arange(1960,2101)
def cl(y):
    up=np.interp(y,[1960,1980,1995,2000],[0.8,2.0,3.6,3.7])
    down=np.interp(y,[2000,2020,2050,2070,2100],[3.7,3.3,2.2,1.6,1.3])
    return np.where(y<=2000,up,down)
chl=cl(yrs)
o=np.interp(cl(yrs-7),[0.8,1.3,2.0,3.7],[290,285,190,95])
fig,ax=plt.subplots(figsize=(6.2,3.6))
ax.plot(yrs,chl,color=ORANGE,lw=2.4,label="Stratospheric chlorine (left axis)")
ax.set_ylabel("Chlorine (ppb)",color=ORANGE); ax.set_xlabel("Year"); ax.set_ylim(0,4.5)
ax2=ax.twinx(); ax2.spines['right'].set_visible(True)
ax2.plot(yrs,o,color=RED,lw=2.4,label="Lowest yearly Antarctic ozone column (right axis)")
ax2.set_ylabel("Ozone column (DU)",color=RED); ax2.set_ylim(0,330)
ax.axvline(1987,color=GREY,ls='--',lw=1); ax.text(1985.5,4.4,"1987 Montreal\nProtocol",fontsize=8,color=GREY,va='top',ha='right')
ax.axvline(2000,color=GREY,ls=':',lw=1); ax.text(2002,4.4,"chlorine peaks\n(about 2000)",fontsize=8,color=GREY,va='top')
ax2.axhline(220,color=GREY,lw=.8); ax2.text(2074,198,"220 DU =\n'ozone hole'\nthreshold",fontsize=7.5,color=GREY,va='top')
h1,l1=ax.get_legend_handles_labels(); h2,l2=ax2.get_legend_handles_labels()
ax.legend(h1+h2,l1+l2,loc='upper center',fontsize=7.5,frameon=False,bbox_to_anchor=(0.5,-0.17),ncol=1)
ax.set_title("Ozone mirrors chlorine, with a lag (schematic, not measured data)",fontsize=10)
save(fig,OUT+'C11_chlorine_ozone.png')

# 4. CO2 records
fig,(a1,a2)=plt.subplots(1,2,figsize=(6.6,3.4),gridspec_kw={'width_ratios':[1.25,1]})
peaks=[(785,255),(690,262),(615,275),(520,268),(410,288),(330,282),(240,280),(125,285),(10,278)]
ages=[800]; ppm=[200]
for i,(p,pk) in enumerate(peaks):
    ages+= [p+9]; ppm+=[190 if i else 200]
    ages+= [p]; ppm+=[pk]
    if i<len(peaks)-1:
        q=peaks[i+1][0]
        ages+= [p-0.4*(p-q)]; ppm+=[pk-45]
ages+=[0]; ppm+=[280]
a1.plot(ages,ppm,color=RED,lw=1.6)
a1.invert_xaxis(); a1.set_ylim(150,440); a1.set_xlabel("Thousand years ago"); a1.set_ylabel("Atmospheric CO₂ (ppm)")
a1.axhline(421,color=DARK,ls='--',lw=1.2); a1.text(790,428,"Recent year: about 420 ppm",fontsize=7.5,color=DARK,va='bottom')
a1.text(790,160,"Ice-core range: about 180–300 ppm",fontsize=7.5,color=RED)
a1.set_title("Ice cores (simplified)",fontsize=9.5)
t=np.arange(1958,2024,1/12)
trend=315+0.746*(t-1958)+0.01361*(t-1958)**2
seas=3.0*np.cos(2*np.pi*(t-1958-0.38))
a2.plot(t,trend+seas,color=RED,lw=0.9); a2.plot(t,trend,color=DARK,lw=1.6)
a2.set_xlabel("Year"); a2.set_ylabel("CO₂ (ppm)"); a2.set_ylim(300,435)
a2.text(1960,415,"Yearly zigzag: plants take\nup CO₂ in growing season",fontsize=7.5,color=RED,va='top')
a2.text(1996,325,"Annual average\n(the trend)",fontsize=7.5,color=DARK)
a2.set_title("Keeling curve (approximate)",fontsize=9.5)
fig.tight_layout()
save(fig,OUT+'C11_co2_records.png')

# 5. Sea-level rise: two causes
fig,(a1,a2,a3)=plt.subplots(1,3,figsize=(6.6,3.2))
for a in (a1,a2,a3): a.set_xlim(0,10); a.set_ylim(0,10); a.axis('off')
# panel1 thermal expansion
a1.add_patch(Rectangle((0.8,2),3.4,3.4,fc=SKY,ec=BLUE,lw=1.3)); a1.add_patch(Rectangle((5.2,2),3.4,4.4,fc=SKY,ec=BLUE,lw=1.3))
a1.plot([0.8,9.0],[5.4,5.4],color=GREY,ls='--',lw=.9)
a1.text(2.5,3.5,"cooler",ha='center',fontsize=8); a1.text(6.9,3.9,"warmer\n(expands)",ha='center',fontsize=8)
a1.annotate("",xy=(9.4,6.4),xytext=(9.4,5.4),arrowprops=dict(arrowstyle='<->',color=RED,lw=1.5))
a1.text(5,8.6,"1  Thermal\nexpansion",ha='center',fontsize=9,fontweight='bold',color=RED)
a1.text(5,0.3,"same mass of water,\nmore volume",ha='center',fontsize=7.5,color=GREY)
# panel2 land ice
a2.add_patch(Polygon([(0.5,3.2),(0.5,7.5),(4,8),(6,3.2)],fc='#EEF4F8',ec=BLUE,lw=1.3)); a2.text(2.8,5.4,"land ice\n(glacier,\nice sheet)",ha='center',fontsize=8)
a2.add_patch(Rectangle((6,1.2),3.8,2.0,fc=SKY,ec=BLUE)); a2.add_patch(Rectangle((0.5,1.2),5.5,2.0,fc=BROWN,alpha=.5,ec='none'))
arrow(a2,(5.2,4.6),(7.5,3.4),color=BLUE,lw=1.8); a2.text(8.0,4.3,"meltwater",fontsize=8,color=BLUE,ha='center')
a2.text(5,8.6,"2  Melting\nland ice",ha='center',fontsize=9,fontweight='bold',color=RED); a2.text(5,0.3,"adds NEW water\nto the ocean",ha='center',fontsize=7.5,color=GREY)
# panel3 sea ice
a3.add_patch(Rectangle((1,2),8,3.8,fc=SKY,ec=BLUE,lw=1.3)); a3.add_patch(Rectangle((3,4.4),4,1.8,fc='#EEF4F8',ec=BLUE,lw=1.3))
a3.text(5,5.3,"floating ice",ha='center',fontsize=8)
a3.text(5,8.6,"Not a cause:\nmelting sea ice",ha='center',fontsize=9,fontweight='bold',color=GREY); a3.text(5,0.3,"already displaces its own\nweight: level unchanged",ha='center',fontsize=7.5,color=GREY)
fig.suptitle("What raises sea level",fontweight='bold',fontsize=10.5)
fig.tight_layout(rect=(0,0,1,0.95))
save(fig,OUT+'C11_sea_level.png')

# 6. Carbon sinks budget
fig,ax=plt.subplots(figsize=(6.2,3.5))
labels=["Emitted by humans\n(fossil fuels + land use)","Stays in the\natmosphere","Absorbed by\nthe ocean","Absorbed by\nland (plants, soil)"]
vals=[41,19,10,12]; cols=[RED,ORANGE,BLUE,GREEN]
b=ax.bar(labels,vals,color=cols,width=.6)
for r,v in zip(b,vals): ax.text(r.get_x()+r.get_width()/2,v+0.8,f"{v}",ha='center',fontweight='bold',fontsize=10)
ax.set_ylabel("Billion tonnes CO₂ per year"); ax.set_ylim(0,50)
ax.text(3.4,46,"Approximate recent-decade values:\n19 + 10 + 12 = 41",fontsize=8,color=GREY,ha='right',va='top')
ax.tick_params(axis='x',labelsize=8)
ax.set_title("Where human CO₂ emissions go (rounded)")
save(fig,OUT+'C11_carbon_sinks.png')
