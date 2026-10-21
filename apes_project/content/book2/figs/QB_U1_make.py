import sys, math
sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book2/figs/'

# 1 climate diagram
def climate():
    m=list("JFMAMJJASOND")
    p=[215,190,205,130,40,10,5,8,20,60,140,200]
    t=[27,27,27,26,25,24,24,26,28,29,28,27]
    fig,ax=plt.subplots(figsize=(6,3.4))
    ax.bar(range(12),p,color=BLUE,width=0.7)
    ax.set_ylabel("Precipitation (mm per month)"); ax.set_ylim(0,250)
    ax.set_xticks(range(12)); ax.set_xticklabels(m)
    ax2=ax.twinx(); ax2.spines["right"].set_visible(True)
    ax2.plot(range(12),t,color=RED,marker="o",lw=2)
    ax2.set_ylim(0,40); ax2.set_ylabel("Mean temperature (°C)",color=RED)
    ax.set_title("Climate diagram, Station K")
    save(fig,D+"QB_U1_climate_station.png")

# 2 carbon fluxes
def carbon():
    fig,ax=canvas(6.2,3.9,xlim=(-0.04,1.04))
    box(ax,0.33,0.70,0.34,0.22,"Atmosphere\nstock: 860 Gt C",fc="#E3EEF7",ec=BLUE,fs=9.5,bold=True)
    box(ax,0.02,0.22,0.30,0.22,"Land plants,\nanimals and soils",fc="#E4F0E6",ec=GREEN,fs=9.5,bold=True)
    box(ax,0.68,0.22,0.30,0.22,"Surface ocean",fc="#D8E8F3",ec=BLUE,fs=9.5,bold=True)
    box(ax,0.36,0.02,0.28,0.14,"Fossil fuel deposits",fc="#EDE3D6",ec=BROWN,fs=9)
    arrow(ax,(0.38,0.69),(0.20,0.45),"A  120",color=GREEN,rad=0.0,off=(-0.10,0.0))
    arrow(ax,(0.26,0.45),(0.43,0.69),"B  118",color=DARK,off=(0.08,-0.03))
    arrow(ax,(0.62,0.69),(0.80,0.45),"C  92",color=BLUE,off=(0.10,0.0))
    arrow(ax,(0.74,0.45),(0.57,0.69),"D  90",color=DARK,off=(-0.10,0.0))
    arrow(ax,(0.50,0.17),(0.50,0.68),"E  10",color=RED,off=(0.05,0.0))
    ax.text(0.5,-0.06,"Annual fluxes in gigatonnes of carbon per year (Gt C/yr)",ha="center",fontsize=8.5,color=GREY)
    save(fig,D+"QB_U1_carbon_fluxes.png")

# 3 nitrogen cycle
def nitrogen():
    fig,ax=canvas(6.2,4.2,xlim=(-0.04,1.04))
    box(ax,0.32,0.82,0.36,0.14,"Atmosphere: N₂ gas",fc="#E3EEF7",ec=BLUE,bold=True)
    box(ax,0.02,0.40,0.26,0.14,"Soil ammonium\n(NH$_4^+$)",fc="#F3EBDD",ec=BROWN)
    box(ax,0.72,0.40,0.26,0.14,"Soil nitrate\n(NO$_3^-$)",fc="#F3EBDD",ec=BROWN)
    box(ax,0.37,0.14,0.26,0.14,"Plants and animals\n(organic N)",fc="#E4F0E6",ec=GREEN)
    box(ax,0.02,0.02,0.26,0.14,"Dead matter and\nwastes (organic N)",fc="#EDE3D6",ec=BROWN)
    def lab(x,y,s): ax.text(x,y,s,ha="center",va="center",fontsize=10,fontweight="bold",color="white",
                         bbox=dict(boxstyle="circle,pad=0.25",fc=RED,ec=RED))
    arrow(ax,(0.38,0.81),(0.16,0.55)); lab(0.24,0.70,"P")
    arrow(ax,(0.29,0.47),(0.71,0.47)); lab(0.50,0.47,"Q")
    arrow(ax,(0.80,0.39),(0.60,0.27)); lab(0.72,0.31,"R")
    arrow(ax,(0.15,0.17),(0.15,0.39)); lab(0.15,0.285,"S")
    arrow(ax,(0.85,0.55),(0.62,0.81)); lab(0.76,0.69,"T")
    arrow(ax,(0.37,0.20),(0.29,0.12),color=GREY)
    ax.text(0.30,0.03,"",fontsize=7)
    ax.text(0.50,0.35,"",fontsize=7)
    save(fig,D+"QB_U1_nitrogen_cycle.png")

# 4 grassland web
def web():
    fig,ax=canvas(6.2,4.3)
    pos={"Grass":(0.25,0.08),"Clover":(0.72,0.08),"Grasshopper":(0.14,0.38),"Vole":(0.62,0.38),
         "Frog":(0.14,0.62),"Snake":(0.42,0.76),"Hawk":(0.70,0.92)}
    cols={"Grass":GREEN,"Clover":GREEN,"Grasshopper":BROWN,"Vole":BROWN,"Frog":TEAL,"Snake":ORANGE,"Hawk":RED}
    for k,(x,y) in pos.items():
        ax.add_patch(FancyBboxPatch((x-0.09,y-0.04),0.18,0.08,boxstyle="round,pad=0.01,rounding_size=0.02",fc="white",ec=cols[k],lw=1.6))
        ax.text(x,y,k,ha="center",va="center",fontsize=9.5,fontweight="bold")
    E=[("Grass","Grasshopper"),("Grass","Vole"),("Clover","Vole"),("Grasshopper","Frog"),("Frog","Snake"),("Vole","Snake"),("Vole","Hawk"),("Snake","Hawk")]
    for a,b in E:
        (x1,y1),(x2,y2)=pos[a],pos[b]
        dx,dy=x2-x1,y2-y1
        k=0.10/ max(abs(dx)/0.1, abs(dy)/0.05)  # approximate box-edge trim
        f=0.0
        t=min(0.09/abs(dx) if abs(dx)>1e-9 else 9, 0.05/abs(dy) if abs(dy)>1e-9 else 9)
        p=(x1+dx*t*1.15,y1+dy*t*1.15); q=(x2-dx*t*1.15,y2-dy*t*1.15)
        arrow(ax,p,q,color=DARK)
    ax.text(0.0,0.94,"Arrows point from the food\nto the organism that eats it",ha="left",fontsize=8,color=GREY)
    save(fig,D+"QB_U1_grass_web.png")

# 5 CO2 trend
def co2():
    t=np.arange(0,4,1/12)
    y=414+2.4*t+3.2*np.cos(2*np.pi*(t-0.37))
    fig,ax=plt.subplots(figsize=(6,3.3))
    ax.plot(2022+t,y,color=RED,lw=1.8)
    ax.set_xlabel("Year"); ax.set_ylabel("Atmospheric CO₂ (ppm)")
    ax.set_title("Monthly CO₂ at a remote Northern Hemisphere station")
    ax.set_xticks([2022,2023,2024,2025,2026]); ax.set_ylim(408,430); ax.grid(alpha=0.25)
    save(fig,D+"QB_U1_co2_station.png")

# 6 energy pyramid
def pyramid():
    fig,ax=canvas(6.0,3.4,xlim=(0,10),ylim=(0,5))
    lv=[("Producers","20,000",8.4),("Primary consumers","1,800",6.4),("Secondary consumers","160",4.4),("Tertiary consumers","12",2.4)]
    cols=[GREEN,BROWN,ORANGE,RED]
    for i,(n,v,w) in enumerate(lv):
        y=0.2+i*1.15
        ax.add_patch(Rectangle((5-w/2,y),w,1.0,fc=cols[i],ec="white",alpha=0.9))
        ax.text(5,y+0.5,f"{n}\n{v} kcal/m²/yr",ha="center",va="center",color="white",fontsize=9,fontweight="bold")
    ax.text(5,4.95,"Energy stored at each trophic level (bar widths not to scale)",ha="center",fontsize=8.5,color=GREY)
    save(fig,D+"QB_U1_energy_levels.png")

# 7 FRQ1 lake schematic
def lake():
    fig,ax=canvas(6.2,3.4)
    ax.add_patch(Rectangle((0.0,0.45),0.30,0.45,fc="#E8E3C8",ec=BROWN,lw=1.2))
    ax.text(0.15,0.67,"Dairy farms and\ncropland\n(manure and\nfertilizer applied)",ha="center",va="center",fontsize=8.5)
    ax.add_patch(Ellipse((0.74,0.55),0.44,0.52,fc="#BFDDF0",ec=BLUE,lw=1.6))
    ax.text(0.74,0.63,"Lake Verrin",ha="center",fontsize=10,fontweight="bold")
    ax.text(0.74,0.46,"summer surface scum\nof algae",ha="center",fontsize=8.5,color=GREEN)
    arrow(ax,(0.31,0.60),(0.51,0.56),"Inlet stream",color=BLUE,off=(0,0.03))
    arrow(ax,(0.96,0.50),(1.04,0.42),color=BLUE)
    ax.text(0.62,0.12,"July surface water: nitrate-N 0.90 mg/L,  total phosphorus 0.008 mg/L",ha="center",fontsize=8.5,
            bbox=dict(boxstyle="round",fc=LIGHT,ec=RED))
    ax.set_xlim(0,1.08)
    save(fig,D+"QB_U1_frq1_lake.png")

# 8 FRQ2 forest
FG=[40,80,260,600,1100,1500,1550,1400,900,400,120,40]
FR=[90,90,150,280,450,620,700,650,480,260,130,90]
def forest():
    m=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    fig,ax=plt.subplots(figsize=(6,3.4))
    ax.plot(m,FG,color=GREEN,marker="o",lw=2,label="Gross primary productivity (GPP)")
    ax.plot(m,FR,color=RED,marker="s",lw=2,label="Plant respiration")
    ax.set_ylabel("kcal/m² per month"); ax.legend(frameon=False,fontsize=8.5,loc="upper left")
    ax.set_title("Temperate seasonal forest, monthly energy flows"); ax.grid(alpha=0.25)
    save(fig,D+"QB_U1_frq2_forest.png")
    print("sums",sum(FG),sum(FR),sum(FG)-sum(FR),sum(FR)/sum(FG)*100)

# 9 FRQ4 reef
def reef():
    fig,axs=plt.subplots(1,3,figsize=(6.2,2.8))
    data=[("Large predatory fish\n(per 100 m²)",14,2),("Sea urchins\n(per m²)",3,22),("Kelp canopy\ncover (%)",82,9)]
    for ax,(t,a,b) in zip(axs,data):
        ax.bar(["Reserve","Fished"],[a,b],color=[TEAL,ORANGE],width=0.6)
        ax.set_title(t,fontsize=9)
        for i,v in enumerate([a,b]): ax.text(i,v,str(v),ha="center",va="bottom",fontsize=9)
        ax.set_ylim(0,max(a,b)*1.2)
    fig.tight_layout()
    save(fig,D+"QB_U1_frq4_reef.png")

for f in (climate,carbon,nitrogen,web,co2,pyramid,lake,forest,reef): f()
