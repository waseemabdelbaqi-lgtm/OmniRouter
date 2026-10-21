import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import matplotlib.pyplot as plt
OUT='/home/user/OmniRouter/apes_project/content/book1/figs/'
BL="#E4EDF5"; GR="#E1EFE3"; BR="#EFE3D8"; GY="#E6E3DF"; YL="#F7EFC9"

def line(ax,pts,color=DARK,lw=1.4):
    xs,ys=zip(*pts); ax.plot(xs,ys,color=color,lw=lw,solid_capstyle='round')

# ---------------- Carbon ----------------
def carbon():
    fig,ax=canvas(6.4,4.7,xlim=(-0.12,1.08),ylim=(-0.06,1.02))
    box(ax,-0.02,0.86,1.06,0.14,"ATMOSPHERE\nCO₂ and CH₄  (≈ 900 Gt C)",fc=BL,ec=BLUE,fs=9.5,bold=True)
    box(ax,0.04,0.52,0.26,0.17,"Producers\n(plants, algae)",fc=GR,ec=GREEN,bold=True)
    box(ax,0.45,0.52,0.20,0.17,"Consumers\n(animals)",fc=GR,ec=GREEN,bold=True)
    box(ax,0.84,0.52,0.20,0.17,"Surface\nocean\n(CO₂, shells)",fc=BL,ec=BLUE,bold=True,fs=8.5)
    box(ax,0.04,0.27,0.44,0.15,"Dead organisms, wastes,\nsoil organic carbon",fc=BR,ec=BROWN,bold=True,fs=8.5)
    box(ax,0.84,0.24,0.20,0.14,"Carbonate\nsediments\n(limestone)",fc=GY,ec=GREY,bold=True,fs=8)
    box(ax,0.04,0.03,0.58,0.12,"Fossil fuels (coal, oil, natural gas)",fc=GY,ec=GREY,bold=True,fs=9)
    arrow(ax,(0.07,0.86),(0.07,0.69),color=GREEN); ax.text(0.085,0.775,"photosynthesis",ha="left",va="center",fontsize=7.5,color=GREEN)
    arrow(ax,(0.26,0.69),(0.26,0.86),color=RED); ax.text(0.275,0.775,"respiration",ha="left",va="center",fontsize=7.5,color=RED)
    arrow(ax,(0.55,0.69),(0.55,0.86),color=RED); ax.text(0.565,0.775,"respiration",ha="left",va="center",fontsize=7.5,color=RED)
    arrow(ax,(0.32,0.605),(0.43,0.605),color=DARK); ax.text(0.375,0.64,"feeding",ha="center",fontsize=7,color=DARK)
    ax.add_patch(FancyArrowPatch((0.94,0.69),(0.94,0.86),arrowstyle="<|-|>",mutation_scale=12,color=BLUE,lw=1.4))
    ax.text(0.93,0.775,"CO₂ exchange",ha="center",va="center",fontsize=7.5,color=BLUE)
    line(ax,[(0.65,0.09),(0.76,0.09),(0.76,0.80)],color=RED,lw=2.2); arrow(ax,(0.76,0.80),(0.76,0.86),color=RED,lw=2.2)
    ax.text(0.775,0.14,"combustion\n(burning fuels\nand wood)",ha="left",va="center",fontsize=8,color=RED)
    arrow(ax,(0.12,0.52),(0.12,0.42),color=BROWN); ax.text(0.135,0.47,"death",fontsize=7.5,color=BROWN,va="center")
    arrow(ax,(0.45,0.52),(0.38,0.42),color=BROWN); ax.text(0.435,0.465,"wastes, death",fontsize=7.5,color=BROWN,ha="left",va="center")
    line(ax,[(0.04,0.345),(-0.07,0.345),(-0.07,0.80)],color=RED)
    arrow(ax,(-0.07,0.80),(-0.07,0.86),color=RED)
    ax.text(-0.095,0.60,"decomposition (CO₂, CH₄)",rotation=90,ha="center",va="center",fontsize=7.5,color=RED)
    arrow(ax,(0.26,0.27),(0.26,0.15),color=GREY); ax.text(0.275,0.21,"burial over millions of years",fontsize=7.5,color=GREY,va="center")
    arrow(ax,(0.94,0.52),(0.94,0.38),color=GREY); ax.text(0.925,0.45,"shells sink",ha="right",fontsize=7.5,color=GREY,va="center")
    ax.text(1.04,-0.045,"Fast pathways: days to centuries.  Slow pathways: millions of years.",ha="right",fontsize=7.5,style="italic",color=GREY)
    save(fig,OUT+"C5_carbon_cycle.png")

# ---------------- Phosphorus ----------------
def phosphorus():
    fig,ax=canvas(6.4,4.6,xlim=(-0.01,1.03),ylim=(0,1))
    ax.add_patch(Rectangle((-0.01,0.0),1.04,0.30,fc="#DCEBF5",ec="none",zorder=0))
    ax.text(0.99,0.275,"LAKE / OCEAN",ha="right",va="top",fontsize=8,color=BLUE,weight="bold")
    ax.text(0.01,0.985,"LAND",fontsize=8,color=BROWN,weight="bold",va="top")
    ax.text(0.99,0.985,"No gas phase:\nno atmospheric reservoir",ha="right",va="top",fontsize=8,color=RED,style="italic")
    box(ax,0.39,0.86,0.22,0.11,"Human sources:\nfertilizer, detergent,\nsewage",fc="#F6E2E4",ec=RED,bold=True,fs=7.5)
    box(ax,0.02,0.60,0.22,0.16,"Phosphate rock\n(apatite minerals)",fc=GY,ec=GREY,bold=True,fs=8.5)
    box(ax,0.39,0.60,0.22,0.16,"Dissolved\nphosphate\nPO$_4^{3-}$ in soil\nand water",fc=YL,ec=ORANGE,bold=True,fs=8.5)
    box(ax,0.76,0.60,0.22,0.16,"Producers\n(plants, algae)",fc=GR,ec=GREEN,bold=True,fs=8.5)
    box(ax,0.76,0.38,0.22,0.12,"Consumers",fc=GR,ec=GREEN,bold=True,fs=8.5)
    box(ax,0.39,0.38,0.22,0.12,"Wastes, dead\norganisms",fc=BR,ec=BROWN,bold=True,fs=8.5)
    box(ax,0.20,0.07,0.30,0.14,"Dissolved phosphate\nin lake / ocean water",fc=YL,ec=ORANGE,bold=True,fs=8.5)
    box(ax,0.74,0.07,0.24,0.14,"Sediments\n(phosphate-bearing)",fc=GY,ec=GREY,bold=True,fs=8)
    arrow(ax,(0.24,0.68),(0.39,0.68),color=GREY); ax.text(0.315,0.70,"weathering",ha="center",fontsize=7.5,color=GREY)
    arrow(ax,(0.61,0.68),(0.76,0.68),color=GREEN); ax.text(0.685,0.70,"uptake",ha="center",fontsize=7.5,color=GREEN)
    arrow(ax,(0.87,0.60),(0.87,0.50),color=DARK); ax.text(0.885,0.555,"eaten",fontsize=7.5,va="center")
    arrow(ax,(0.76,0.44),(0.61,0.44),color=BROWN); ax.text(0.685,0.46,"waste, death",ha="center",fontsize=7,color=BROWN)
    arrow(ax,(0.50,0.50),(0.50,0.60),color=RED); ax.text(0.515,0.555,"decomposition",fontsize=7.5,color=RED,va="center")
    arrow(ax,(0.50,0.86),(0.50,0.76),color=RED); ax.text(0.515,0.81,"added to soil\nand water",fontsize=7.5,color=RED,va="center")
    line(ax,[(0.40,0.60),(0.315,0.54),(0.315,0.27)],color=BLUE,lw=1.6); arrow(ax,(0.315,0.27),(0.315,0.21),color=BLUE,lw=1.6)
    ax.text(0.30,0.40,"runoff and\nleaching",fontsize=7.5,color=BLUE,ha="right",va="center")
    arrow(ax,(0.50,0.14),(0.74,0.14),color=GREY); ax.text(0.62,0.16,"sedimentation",ha="center",fontsize=7.5,color=GREY)
    line(ax,[(0.86,0.07),(0.86,0.02),(0.08,0.02),(0.08,0.55)],color=GREY,lw=1.6); arrow(ax,(0.08,0.55),(0.08,0.60),color=GREY,lw=1.6)
    ax.text(0.055,0.32,"uplift over millions of years",fontsize=7.5,color=GREY,va="center",ha="center",rotation=90)
    save(fig,OUT+"C5_phosphorus_cycle.png")

# ---------------- Sulfur ----------------
def sulfur():
    fig,ax=canvas(6.4,4.8,xlim=(-0.01,1.03),ylim=(0,1))
    ax.add_patch(Rectangle((0.645,0.0),0.375,0.70,fc="#DCEBF5",ec="none",zorder=0))
    ax.text(1.02,0.01,"OCEAN",ha="right",va="bottom",fontsize=8,color=BLUE,weight="bold")
    ax.text(0.01,0.685,"LAND",va="top",fontsize=8,color=BROWN,weight="bold")
    box(ax,0.01,0.74,0.97,0.24,"ATMOSPHERE\nSO₂, H₂S and DMS (dimethyl sulfide) are oxidized in air\nto sulfate aerosols (SO$_4^{2-}$) and sulfuric acid (H₂SO₄)",fc=BL,ec=BLUE,fs=8.5,bold=True)
    box(ax,0.01,0.40,0.16,0.14,"Volcanoes",fc=GY,ec=GREY,bold=True,fs=8)
    box(ax,0.22,0.40,0.18,0.14,"Fossil fuels\n(coal, oil)",fc=GY,ec=GREY,bold=True,fs=8)
    box(ax,0.45,0.40,0.16,0.14,"Soil and\nplants",fc=GR,ec=GREEN,bold=True,fs=8)
    box(ax,0.01,0.10,0.55,0.16,"Sulfur-bearing rocks (gypsum, pyrite)\nand buried organic matter",fc=BR,ec=BROWN,bold=True,fs=8)
    box(ax,0.69,0.40,0.32,0.14,"Seawater sulfate SO$_4^{2-}$,\nphytoplankton",fc=BL,ec=BLUE,bold=True,fs=8)
    box(ax,0.69,0.07,0.32,0.20,"Oxygen-poor sediments:\nsulfur bacteria make H₂S,\nwhich forms pyrite (FeS₂)",fc=GY,ec=GREY,bold=True,fs=7.5)
    def up(x,label,col=RED,lw=1.5,y0=0.56,y1=0.74):
        arrow(ax,(x,y0),(x,y1),color=col,lw=lw); ax.text(x+0.012,(y0+y1)/2,label,rotation=90,ha="left",va="center",fontsize=7.5,color=col)
    up(0.09,"SO₂",GREY)
    up(0.31,"burning fuels",RED,lw=3.2)
    up(0.50,"decay (H₂S)",BROWN)
    up(0.74,"DMS",TEAL)
    up(0.84,"sea spray",BLUE)
    arrow(ax,(0.57,0.74),(0.57,0.56),color=RED,lw=1.6); ax.text(0.585,0.65,"acid deposition",rotation=90,ha="left",va="center",fontsize=7.5,color=RED)
    arrow(ax,(0.94,0.74),(0.94,0.56),color=RED,lw=1.6); ax.text(0.955,0.65,"acid deposition",rotation=90,ha="left",va="center",fontsize=7.5,color=RED)
    arrow(ax,(0.53,0.26),(0.53,0.40),color=GREY); ax.text(0.545,0.33,"weathering",fontsize=7.5,color=GREY,va="center")
    arrow(ax,(0.84,0.40),(0.84,0.27),color=GREY); ax.text(0.855,0.335,"sinking, burial",fontsize=7.5,color=GREY,va="center")
    arrow(ax,(0.69,0.17),(0.56,0.17),color=GREY); ax.text(0.625,0.135,"uplift",fontsize=7,color=GREY,ha="center",va="top")
    arrow(ax,(0.12,0.26),(0.12,0.40),color=GREY,lw=1.0); ax.text(0.135,0.33,"slow\nburial",fontsize=6.5,color=GREY,va="center")
    save(fig,OUT+"C5_sulfur_cycle.png")

# ---------------- Water ----------------
def water():
    fig,ax=canvas(6.4,4.4,xlim=(0,1),ylim=(0,1))
    ax.add_patch(Rectangle((0,0.0),0.56,0.20,fc="#BFD9EC",ec="none"))
    ax.text(0.02,0.04,"OCEAN (≈ 97% of Earth's water)",fontsize=8.5,color=BLUE,weight="bold")
    ax.add_patch(Polygon([(0.56,0.0),(0.56,0.20),(0.66,0.30),(0.76,0.44),(0.86,0.46),(0.92,0.58),(1.0,0.62),(1.0,0.0)],fc="#D9C9A8",ec="none"))
    ax.add_patch(Polygon([(0.88,0.50),(0.92,0.58),(1.0,0.62),(1.0,0.50)],fc="white",ec=GREY,lw=1))
    ax.text(0.955,0.535,"ice",ha="center",va="center",fontsize=7.5,weight="bold",color=DARK)
    ax.add_patch(Rectangle((0.70,0.02),0.26,0.10,fc="#9CC5E3",ec=BLUE,lw=0.8))
    ax.text(0.83,0.07,"Groundwater",ha="center",va="center",fontsize=8,weight="bold",color=DARK)
    for cx,cy,r in [(0.38,0.86,0.05),(0.46,0.89,0.06),(0.54,0.86,0.05),(0.46,0.84,0.05)]:
        ax.add_patch(Circle((cx,cy),r,fc="#F0F0F0",ec=GREY,lw=0.8))
    ax.text(0.46,0.85,"Clouds",ha="center",va="center",fontsize=8,weight="bold"); ax.text(0.46,0.775,"condensation of vapor",ha="center",va="center",fontsize=7.5,color=BLUE)
    ax.add_patch(Circle((0.07,0.92),0.04,fc=YELLOW,ec=ORANGE)); ax.text(0.07,0.86,"Sun powers\nthe cycle",ha="center",va="top",fontsize=7.5,color=ORANGE)
    ax.add_patch(Rectangle((0.775,0.45),0.012,0.06,fc=BROWN,ec="none")); ax.add_patch(Circle((0.781,0.54),0.04,fc=GREEN,ec="none"))
    arrow(ax,(0.22,0.22),(0.30,0.76),color=BLUE,lw=1.6); ax.text(0.20,0.50,"evaporation\n≈ 505,000",fontsize=7.5,color=BLUE,ha="right",va="center")
    arrow(ax,(0.42,0.74),(0.38,0.24),color=BLUE,lw=1.6); ax.text(0.425,0.46,"precipitation\non ocean\n≈ 458,000",fontsize=7.5,color=BLUE,ha="left",va="center")
    arrow(ax,(0.57,0.90),(0.76,0.90),color=BLUE,lw=1.4); ax.text(0.665,0.915,"vapor carried over land ≈ 47,000",fontsize=7.2,color=BLUE,ha="center",va="bottom")
    arrow(ax,(0.66,0.80),(0.66,0.34),color=BLUE,lw=1.6); ax.text(0.645,0.62,"rain, snow\non land\n≈ 119,000",fontsize=7.5,color=BLUE,ha="right",va="center")
    arrow(ax,(0.80,0.60),(0.80,0.80),color=GREEN,lw=1.5); ax.text(0.815,0.70,"evapotranspiration\n(evaporation + transpiration)\n≈ 72,000",fontsize=7.5,color=GREEN,ha="left",va="center")
    arrow(ax,(0.70,0.36),(0.58,0.23),color=BLUE,lw=1.4); ax.text(0.55,0.30,"runoff\n≈ 47,000",fontsize=7.5,color=BLUE,ha="right",va="center")
    arrow(ax,(0.84,0.40),(0.84,0.13),color=BROWN,lw=1.2); ax.text(0.855,0.27,"infiltration",fontsize=7.5,color=BROWN,va="center")
    ax.text(0.99,0.985,"Fluxes in km³ per year (approximate)",fontsize=7,style="italic",color=GREY,ha="right",va="top")
    save(fig,OUT+"C5_water_cycle.png")

# ---------------- Human body ----------------
def body():
    fig,(a1,a2)=plt.subplots(1,2,figsize=(6.4,3.3),gridspec_kw={"width_ratios":[1.15,1]})
    el=[("Oxygen (O)",65,BLUE),("Carbon (C)",18,BROWN),("Hydrogen (H)",10,SKY),("Nitrogen (N)",3,GREEN),("Calcium (Ca)",1.5,GREY),("Phosphorus (P)",1.0,ORANGE),("Sulfur (S)",0.25,YELLOW)]
    y=range(len(el))[::-1]
    a1.barh(list(y),[e[1] for e in el],color=[e[2] for e in el],edgecolor="#444",lw=0.6)
    a1.set_yticks(list(y)); a1.set_yticklabels([e[0] for e in el],fontsize=8.5)
    for yy,e in zip(y,el): a1.text(e[1]+1,yy,f"{e[1]:g}%",va="center",fontsize=8.5)
    a1.set_xlim(0,80); a1.set_xlabel("Percent of body mass"); a1.set_title("By element (typical adult)",fontsize=10)
    comp=[("Water",60,BLUE),("Protein",16,GREEN),("Fat",15,YELLOW),("Minerals\n(bone)",6,GREY),("Carbohydrate\nand other",3,BROWN)]
    y2=range(len(comp))[::-1]
    a2.barh(list(y2),[c[1] for c in comp],color=[c[2] for c in comp],edgecolor="#444",lw=0.6)
    a2.set_yticks(list(y2)); a2.set_yticklabels([c[0] for c in comp],fontsize=8.5)
    for yy,c in zip(y2,comp): a2.text(c[1]+1,yy,f"{c[1]:g}%",va="center",fontsize=8.5)
    a2.set_xlim(0,75); a2.set_xlabel("Percent of body mass"); a2.set_title("By substance (typical adult)",fontsize=10)
    fig.tight_layout()
    save(fig,OUT+"C5_body_composition.png")

if __name__=="__main__":
    for f in [carbon,phosphorus,sulfur,water,body]: f()
