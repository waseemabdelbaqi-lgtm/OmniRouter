import sys, numpy as np
sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
from matplotlib.patches import Rectangle, Polygon
D='/home/user/OmniRouter/apes_project/content/book2/figs/'

# 1 salinization cross-section
fig,ax=canvas(6.2,3.6,(0,10),(0,6))
ax.add_patch(Rectangle((0,3.6),10,2.4,fc="#F1F6FA",ec="none",zorder=0))
ax.add_patch(Rectangle((0,0),10,3.6,fc="#E3D2B4",ec="none"))          # soil
ax.add_patch(Rectangle((0,0),10,2.7,fc=SKY,ec="none",alpha=0.85))      # saturated zone
ax.plot([0,10],[2.7,2.7],color=BLUE,lw=2)
ax.text(9.9,2.45,"saturated zone",ha="right",va="top",fontsize=9,color=DARK)
ax.plot([0,10],[3.6,3.6],color=BROWN,lw=2)
ax.add_patch(Rectangle((0,3.6),10,0.14,fc="white",ec="#555",lw=1.0,zorder=4))
for x in np.arange(0.3,10,0.35): ax.add_patch(Rectangle((x,3.74),0.18,0.07,fc="white",ec="#555",lw=0.6,zorder=4))
# crop plants
for x in np.arange(1.2,9.5,1.5):
    ax.plot([x,x],[3.7,4.5],color=GREEN,lw=2); ax.plot([x,x+0.25],[4.2,4.6],color=GREEN,lw=1.5); ax.plot([x,x-0.25],[4.0,4.4],color=GREEN,lw=1.5)
    ax.plot([x,x],[3.6,2.4],color=BROWN,lw=1.2); ax.plot([x,x-0.2],[3.0,2.5],color=BROWN,lw=1); ax.plot([x,x+0.2],[3.0,2.5],color=BROWN,lw=1)
# ditch with water
ax.add_patch(Polygon([[4.2,3.6],[4.6,3.0],[5.4,3.0],[5.8,3.6]],fc=BLUE,ec=DARK,lw=0.8))
ax.text(5,5.2,"Irrigation water applied by flooding",ha="center",fontsize=9,color=DARK)
ax.annotate("",xy=(5,3.75),xytext=(5,5.0),arrowprops=dict(arrowstyle="-|>",color=BLUE,lw=1.4))
# labels
ax.annotate("W  white crust of salts\nat the soil surface",xy=(0.6,3.66),xytext=(0.1,5.2),fontsize=9,arrowprops=dict(arrowstyle="-",color=GREY),va="center")
ax.annotate("X  water table about\n40 cm below the surface",xy=(8.0,2.7),xytext=(6.2,1.2),fontsize=9,arrowprops=dict(arrowstyle="-",color=GREY),va="center",bbox=dict(fc="white",ec="none",pad=1.5))
ax.text(0.15,0.35,"Z  deep groundwater supply",fontsize=9,color=DARK)
save(fig,D+'QB_U5_salinization.png')

# 2 resistance
fig,ax=plt.subplots(figsize=(6,3.4))
s=np.arange(1,9)
A=[2,10,35,70,92,98,99,99]; B=[2,4,8,14,24,38,55,70]
ax.plot(s,A,'-o',color=RED,label="Field A: 6 applications per season")
ax.plot(s,B,'-s',color=BLUE,label="Field B: 2 applications per season")
ax.set_xlabel("Growing season"); ax.set_ylabel("Aphids resistant to the insecticide (%)")
ax.set_ylim(0,105); ax.legend(frameon=False,fontsize=9,loc="upper left")
ax.grid(axis='y',alpha=.25)
save(fig,D+'QB_U5_resistance.png')

# 3 fishery
yrs=np.array([1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010])
catch=np.array([100,170,240,300,350,380,260,150,90,65,50])
ssb=np.array([900,820,700,610,520,330,200,110,60,50,45])
fig,ax=plt.subplots(figsize=(6,3.5))
ax.plot(yrs,ssb,'-o',color=GREEN,label="Spawning stock biomass")
ax.plot(yrs,catch,'-s',color=RED,label="Annual landings")
ax.set_xlabel("Year"); ax.set_ylabel("Thousand metric tons")
ax.set_ylim(0,950); ax.legend(frameon=False,fontsize=9); ax.grid(axis='y',alpha=.25)
save(fig,D+'QB_U5_fishery.png')

# 4 hydrograph
t=np.linspace(0,36,400)
def g(t,k,th,peak):
    y=t**(k-1)*np.exp(-t/th); return peak*y/y.max()
fig,ax=plt.subplots(figsize=(6,3.4))
ax.plot(t,g(t,6,2.4,12)+1.5,color=BLUE,lw=2,label="Watershed X")
ax.plot(t,g(t,3,1.4,46)+1.5,color=RED,lw=2,label="Watershed Y")
ax.axvline(0,color=GREY,lw=.8)
ax.set_xlabel("Hours after the start of the storm"); ax.set_ylabel("Stream discharge (m³/s)")
ax.set_xlim(0,36); ax.set_ylim(0); ax.legend(frameon=False,fontsize=9); ax.grid(axis='y',alpha=.25)
save(fig,D+'QB_U5_hydrograph.png')

# 5 footprint
c=["P","Q","R","S"]; fp=[8.1,4.2,1.4,2.9]; bc=[3.2,4.9,0.9,12.5]
x=np.arange(4); w=.36
fig,ax=plt.subplots(figsize=(6,3.4))
ax.bar(x-w/2,fp,w,color=RED,label="Ecological footprint")
ax.bar(x+w/2,bc,w,color=GREEN,label="Biocapacity")
for i in range(4):
    ax.text(x[i]-w/2,fp[i]+.2,f"{fp[i]}",ha="center",fontsize=9); ax.text(x[i]+w/2,bc[i]+.2,f"{bc[i]}",ha="center",fontsize=9)
ax.set_xticks(x); ax.set_xticklabels([f"Country {k}" for k in c])
ax.set_ylabel("Global hectares per person"); ax.set_ylim(0,14.5); ax.legend(frameon=False,fontsize=9,loc="upper left")
save(fig,D+'QB_U5_footprint.png')

# 6 surplus production
N=np.linspace(0,1000,300); G=0.5*N*(1-N/1000)
fig,ax=plt.subplots(figsize=(6,3.5))
ax.plot(N,G,color=BLUE,lw=2.2,label="Net population growth")
for h,col,lab in [(100,GREY,"Harvest of 100"),(150,RED,"Harvest of 150")]:
    ax.axhline(h,color=col,ls='--',lw=1.4); ax.text(985,h+3,lab,ha="right",fontsize=9,color=col)
ax.axvline(600,color=ORANGE,lw=1.2,ls=':'); ax.text(608,8,"current stock\n(600)",fontsize=8.5,color=ORANGE)
ax.set_xlabel("Stock size (metric tons)"); ax.set_ylabel("Tons per year"); ax.set_xlim(0,1000); ax.set_ylim(0,170)
ax.legend(frameon=False,fontsize=9,loc="upper left"); ax.grid(alpha=.2)
save(fig,D+'QB_U5_surplus.png')

# 7 erosion plots
lab=["Conventional\ntillage","Contour\nplowing","Strip\ncropping","No-till"]; v=[18.0,11.7,9.0,4.5]; e=[1.4,1.1,0.9,0.5]
fig,ax=plt.subplots(figsize=(6,3.4))
ax.bar(lab,v,yerr=e,capsize=4,color=[GREY,SAND,TEAL,GREEN],edgecolor="#333")
for i,val in enumerate(v): ax.text(i,val+e[i]+.5,f"{val}",ha="center",fontsize=9)
ax.set_ylabel("Soil loss (t/ha/yr)"); ax.set_ylim(0,22)
ax.text(3.45,21,"Error bars: range among replicates",ha="right",fontsize=8.5,style="italic",color=GREY)
save(fig,D+'QB_U5_erosion_plots.png')

# 8 paddocks (FRQ1) -- creek runs between the two rows so every paddock borders it
fig,ax=canvas(6.2,4.0,(0,12),(0,9))
for (y0,y1) in [(5.4,7.8),(1.4,3.8)]:
    ax.add_patch(Rectangle((0.2,y0),11.6,y1-y0,fc="#EEF2DF",ec=DARK,lw=1))
    for i in range(1,3): ax.plot([0.2+3.87*i]*2,[y0,y1],color=DARK,lw=1.2)
xs=np.linspace(0.2,11.8,100); ax.plot(xs,4.6+0.22*np.sin(xs*1.1),color=BLUE,lw=6,solid_capstyle='round')
ax.text(6.0,5.05,"Creek",ha="center",va="center",color=BLUE,fontsize=10,fontweight="bold")
names=[["C1","C2","C3"],["R1","R2","R3"]]
for r,(row,y) in enumerate(zip(names,[6.6,2.6])):
    for i,n in enumerate(row):
        ax.text(0.2+3.87*i+1.93,y+0.25,n,ha="center",fontsize=11,fontweight="bold",color=RED if r==0 else GREEN)
        ax.text(0.2+3.87*i+1.93,y-0.45,"20 ha",ha="center",fontsize=9)
ax.text(6,8.4,"Continuous grazing (C1–C3): 40 cattle stay in each paddock all season",ha="center",fontsize=9,color=RED)
ax.text(6,0.6,"R1–R3: rotational grazing, one herd of 120 cattle moves to the next paddock every 10 days",ha="center",va="center",fontsize=8.5,color=GREEN)
save(fig,D+'QB_U5_paddocks.png')

# 9 aquifer (FRQ2)
yr=[1960,1970,1980,1990,2000,2010,2020]; irr=[40,90,160,210,230,225,215]; pump=[300,700,1350,1700,1850,1600,1300]; thick=[62,58,50,42,35,30,27]
fig,ax=plt.subplots(figsize=(6,3.5))
ax.plot(yr,thick,'-o',color=BLUE,lw=2,label="Saturated thickness (m)")
ax.set_xlabel("Year"); ax.set_ylabel("Saturated thickness (m)",color=BLUE); ax.set_ylim(0,70)
ax2=ax.twinx(); ax2.spines['right'].set_visible(True)
ax2.plot(yr,pump,'-s',color=RED,lw=2,label="Groundwater pumped (million m³/yr)")
ax2.set_ylabel("Groundwater pumped (million m³/yr)",color=RED); ax2.set_ylim(0,2100)
h1,l1=ax.get_legend_handles_labels(); h2,l2=ax2.get_legend_handles_labels()
ax.legend(h1+h2,l1+l2,frameon=False,fontsize=8.5,loc="lower center")
save(fig,D+'QB_U5_aquifer.png')
print("ok")
