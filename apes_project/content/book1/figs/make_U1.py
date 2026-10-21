import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
OUT='/home/user/OmniRouter/apes_project/content/book1/figs/'

# ---------- Fig 1: biome climate chart ----------
def biomes():
    fig,ax=plt.subplots(figsize=(6.2,4.3))
    B=[("Tundra",(-9,22),(14,24),"#9FB8C8",0),
       ("Taiga",(-1,72),(12,46),"#4F7F6A",0),
       ("Temperate\ngrassland",(9,38),(16,26),"#C9C46A",0),
       ("Shrubland",(18,64),(12,24),"#B88A5A",0),
       ("Temperate\nseasonal forest",(11,130),(14,70),"#5E9B58",0),
       ("Temperate\nrainforest",(10,270),(10,150),"#2F6B4A",0),
       ("Savanna",(25,125),(8,70),"#D9A441",0),
       ("Tropical\nrainforest",(25,310),(7,170),"#1F7A3A",0),
       ("Desert",(18,11),(26,22),"#E3CFA0",0)]
    for n,(t,p),(w,h),c,_ in B:
        ax.add_patch(Ellipse((t,p),w,h,fc=c,ec="#333",lw=0.8,alpha=0.85))
    lab={"Tundra":(-9,22),"Taiga":(-1,72),"Temperate\ngrassland":(9,38),"Shrubland":(18,64),
         "Temperate\nseasonal forest":(11,130),"Temperate\nrainforest":(10,270),"Savanna":(25,125),
         "Tropical\nrainforest":(25,310),"Desert":(18,11)}
    for n,(x,y) in lab.items():
        ax.text(x,y,n,ha="center",va="center",fontsize=7.5,color="black",fontweight="bold")
    ax.set_xlim(-18,32); ax.set_ylim(-5,400)
    ax.set_xlabel("Mean annual temperature (°C)"); ax.set_ylabel("Mean annual precipitation (cm)")
    ax.set_title("Terrestrial biomes follow temperature and precipitation (approximate zones)")
    ax.grid(alpha=0.25)
    save(fig,OUT+'U1_biome_climate.png')

# ---------- Fig 2: carbon cycle ----------
def lab(ax,x,y,t,c,ha="center",fs=8):
    ax.text(x,y,t,ha=ha,va="center",fontsize=fs,color=c,bbox=dict(fc="white",ec="none",pad=1.2))
def carbon():
    fig,ax=canvas(6.3,4.6)
    box(ax,0.30,0.80,0.40,0.15,"ATMOSPHERE\nCO₂ (and CH₄)",fc="#E6EEF5",ec=BLUE,bold=True)
    box(ax,0.02,0.52,0.24,0.14,"Producers\n(plants, algae)",fc="#E3F0E5",ec=GREEN,bold=True)
    box(ax,0.76,0.52,0.22,0.14,"Consumers\n(animals)",fc="#E3F0E5",ec=GREEN,bold=True)
    box(ax,0.02,0.22,0.24,0.14,"Dead organisms,\nwastes, soil carbon",fc="#EFE5DA",ec=BROWN,bold=True,fs=8.5)
    box(ax,0.38,0.02,0.24,0.14,"Fossil fuels &\nsedimentary rock",fc="#E4E0DC",ec=GREY,bold=True)
    box(ax,0.76,0.22,0.22,0.14,"Ocean (dissolved\nCO₂, shells)",fc="#DCEBF5",ec=BLUE,bold=True,fs=8.5)
    arrow(ax,(0.34,0.80),(0.21,0.66),color=GREEN); lab(ax,0.31,0.72,"photosynthesis",GREEN,"left")
    arrow(ax,(0.08,0.66),(0.30,0.85),color=RED); lab(ax,0.08,0.755,"respiration",RED,"center")
    arrow(ax,(0.26,0.59),(0.76,0.59),color=DARK); lab(ax,0.5,0.61,"feeding",DARK)
    arrow(ax,(0.82,0.66),(0.66,0.80),color=RED); lab(ax,0.88,0.74,"respiration",RED)
    arrow(ax,(0.14,0.52),(0.14,0.36),color=BROWN); lab(ax,0.19,0.44,"death",BROWN,"left")
    arrow(ax,(0.26,0.33),(0.35,0.80),color=RED); lab(ax,0.33,0.44,"decomposition\n(respiration)",RED,"left",7.5)
    arrow(ax,(0.18,0.22),(0.38,0.09),color=GREY); lab(ax,0.10,0.115,"burial over\nmillions of years",GREY,"center",7.5)
    arrow(ax,(0.54,0.16),(0.54,0.80),color=RED); lab(ax,0.55,0.25,"combustion",RED,"left")
    ax.add_patch(FancyArrowPatch((0.60,0.80),(0.79,0.36),arrowstyle="<|-|>",mutation_scale=12,color=BLUE,lw=1.4))
    lab(ax,0.66,0.46,"CO₂\nexchange",BLUE,"center",7.5)
    ax.text(0.99,0.02,"Fast pathways: days to centuries\nSlow pathway: millions of years",ha="right",fontsize=7.5,style="italic",color=GREY)
    save(fig,OUT+'U1_carbon_cycle.png')

# ---------- Fig 3: nitrogen cycle ----------
def nitrogen():
    fig,ax=canvas(6.3,4.8,ylim=(-0.30,1))
    box(ax,0.15,0.86,0.70,0.12,"ATMOSPHERE: N₂ gas (about 78% of air), the largest reservoir",fc="#E6EEF5",ec=BLUE,bold=True,fs=8.5)
    box(ax,0.02,0.50,0.25,0.14,"Ammonia / ammonium\nNH₃ / NH$_4^+$",fc="#F3E9D2",ec=BROWN,bold=True,fs=8.5)
    box(ax,0.39,0.50,0.25,0.14,"Nitrite → nitrate\nNO$_2^-$ → NO$_3^-$",fc="#F3E9D2",ec=BROWN,bold=True,fs=8.5)
    box(ax,0.76,0.50,0.22,0.14,"Plants & algae\n(organic N)",fc="#E3F0E5",ec=GREEN,bold=True,fs=8.5)
    box(ax,0.76,0.22,0.22,0.14,"Consumers\n(organic N)",fc="#E3F0E5",ec=GREEN,bold=True,fs=8.5)
    box(ax,0.02,0.22,0.25,0.14,"Wastes & dead\norganisms (organic N)",fc="#EFE5DA",ec=BROWN,bold=True,fs=8.5)
    box(ax,0.33,0.02,0.37,0.12,"Synthetic fertilizer (made from N₂\nby the Haber–Bosch process)",fc="#EEEEEE",ec=GREY,fs=7.5)
    arrow(ax,(0.20,0.86),(0.14,0.64),color=GREEN); lab(ax,0.15,0.75,"1",GREEN,fs=9)
    arrow(ax,(0.27,0.57),(0.39,0.57),color=ORANGE); lab(ax,0.33,0.57,"2",ORANGE,fs=9)
    arrow(ax,(0.64,0.57),(0.76,0.57),color=GREEN); lab(ax,0.70,0.57,"3",GREEN,fs=9)
    arrow(ax,(0.87,0.50),(0.87,0.36),color=DARK)
    arrow(ax,(0.76,0.29),(0.27,0.29),color=BROWN)
    arrow(ax,(0.12,0.36),(0.12,0.50),color=RED); lab(ax,0.17,0.43,"4",RED,fs=9)
    arrow(ax,(0.45,0.64),(0.45,0.86),color=BLUE); lab(ax,0.45,0.75,"5",BLUE,fs=9)
    arrow(ax,(0.55,0.14),(0.55,0.50),color=GREY)
    ax.text(0.89,0.43,"eaten",fontsize=7.5,color=DARK,va="center")
    ax.text(0.40,0.31,"death, wastes",fontsize=7.5,color=BROWN,ha="center")
    L=["1 Nitrogen fixation: N₂ → NH₃ (soil bacteria; also lightning)","2 Nitrification: NH$_4^+$ → NO$_2^-$ → NO$_3^-$ (soil bacteria, needs O₂)",
       "3 Assimilation: roots take up NH$_4^+$ / NO$_3^-$ and build organic N","4 Ammonification: decomposers turn organic N back into NH$_4^+$",
       "5 Denitrification: NO$_3^-$ → N₂ (bacteria in oxygen-poor soil)"]
    for i,t in enumerate(L): ax.text(0.02,-0.06-i*0.050,t,fontsize=7.5,va="center")
    save(fig,OUT+'U1_nitrogen_cycle.png')

# ---------- Fig 4: energy pyramid ----------
def pyramid():
    fig,ax=canvas(6.2,4.0,xlim=(0,10),ylim=(0,6.4))
    lv=[("Producers","10,000",GREEN,10.5),("Primary consumers","1,000",ORANGE,8.2),
        ("Secondary consumers","100",BLUE,6.0),("Tertiary consumers","10",RED,4.4)]
    for i,(n,e,c,w) in enumerate(lv):
        y=0.3+i*1.45
        ax.add_patch(Rectangle((5-w/2*0.62*1.0,y),w*0.62,1.25,fc=c,ec="white",lw=1.5,alpha=0.9))
        ax.text(5,y+0.62,f"{n}\n{e} kcal/m²/yr",ha="center",va="center",fontsize=8.5,color="white",fontweight="bold")
        if i<3:
            ax.annotate("",xy=(8.7,y+1.45+0.62),xytext=(8.7,y+0.62),arrowprops=dict(arrowstyle="-|>",color=DARK,lw=1.3))
            ax.text(8.85,y+1.15,"10% passed on",fontsize=7.5,color=DARK,va="center")
    ax.text(0.1,3.9,"90% lost as heat,\nrespiration, waste,\nuneaten parts",fontsize=7.5,color=GREY,va="center")
    ax.text(0.2,6.1,"Sunlight",fontsize=9,color=ORANGE,fontweight="bold",va="center")
    ax.annotate("",xy=(1.8,5.2),xytext=(1.0,6.0),arrowprops=dict(arrowstyle="-|>",color=ORANGE,lw=2))
    ax.set_title("Energy pyramid with the 10% rule (illustrative numbers)",loc="left",fontsize=10)
    save(fig,OUT+'U1_energy_pyramid.png')

# ---------- Fig 5: GPP / NPP ----------
biomes(); carbon(); nitrogen(); pyramid()
