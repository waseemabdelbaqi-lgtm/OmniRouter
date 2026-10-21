import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
OUT='/home/user/OmniRouter/apes_project/content/book1/figs/'

# ---------- 1. soil conservation ----------
def soil():
    fig,axs=plt.subplots(1,3,figsize=(6.4,2.7))
    # contour plowing: top view of a hill with contour lines
    ax=axs[0]; ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis('off')
    ax.add_patch(Rectangle((0,0),10,10,fc="#EFE3C4",ec=GREY,lw=0.8))
    for r,c in [(4.3,"#8B5E3C"),(3.3,"#8B5E3C"),(2.3,"#8B5E3C"),(1.3,"#8B5E3C")]:
        ax.add_patch(Ellipse((5,5),2*r*1.0,2*r*0.8,fc="none",ec=GREEN,lw=1.6))
    ax.text(5,5,"hilltop",ha="center",va="center",fontsize=7,color=DARK)
    ax.annotate("",xy=(9.3,1.0),xytext=(9.3,3.5),arrowprops=dict(arrowstyle="-|>",color=BLUE,lw=1.4))
    ax.text(8.6,0.4,"water",fontsize=7,color=BLUE,ha="center")
    ax.set_title("Contour plowing\n(rows follow the slope's level lines)",fontsize=8.5)
    # terracing: side view
    ax=axs[1]; ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis('off')
    xs=[0,0.5,2.5,2.5,4.5,4.5,6.5,6.5,8.5,8.5,10]; 
    # steps descending to the right? draw ascending left->right hillside as steps
    pts=[(0,0),(0,2),(2.5,2),(2.5,4),(5,4),(5,6),(7.5,6),(7.5,8),(10,8),(10,0)]
    ax.add_patch(Polygon(pts,fc="#C9A77A",ec=BROWN,lw=1.2))
    for (x0,x1,y) in [(0,2.5,2),(2.5,5,4),(5,7.5,6),(7.5,10,8)]:
        ax.add_patch(Rectangle((x0+0.15,y),x1-x0-0.3,0.35,fc=GREEN,ec="none"))
    ax.text(5,0.9,"flat steps\nhold soil and water",ha="center",fontsize=7,color=DARK)
    ax.set_title("Terracing\n(steep slope cut into steps)",fontsize=8.5)
    # strip cropping: top view
    ax=axs[2]; ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis('off')
    cols=["#E8C547","#3E7D4F"]*3
    for i in range(6):
        ax.add_patch(Rectangle((0,i*1.4+0.8),10,1.4,fc=cols[i],ec="white",lw=0.8))
    ax.text(5,1.5,"row crop (corn)",ha="center",va="center",fontsize=7)
    ax.text(5,2.9,"dense cover (hay)",ha="center",va="center",fontsize=7,color="white")
    ax.annotate("",xy=(9.6,0.2),xytext=(9.6,0.2),arrowprops=dict())
    ax.set_title("Strip cropping\n(dense strips trap soil)",fontsize=8.5)
    fig.tight_layout(w_pad=1.0)
    save(fig,OUT+'C7_soil_conservation.png')

# ---------- 2. fire triangle + fire types ----------
def fire():
    fig=plt.figure(figsize=(6.4,3.4))
    ax=fig.add_axes([0,0.1,0.34,0.9]); ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis('off')
    ax.add_patch(Polygon([(1,1.5),(9,1.5),(5,8.4)],fc=LIGHT,ec=RED,lw=2))
    ax.text(5,3.3,"FIRE",ha="center",fontsize=12,fontweight="bold",color=RED)
    ax.text(5,8.9,"Heat\n(spark, lightning)",ha="center",va="bottom",fontsize=7.5)
    ax.text(1.0,0.5,"Fuel\n(wood, litter)",ha="center",va="top",fontsize=7.5)
    ax.text(9.0,0.5,"Oxygen\n(air)",ha="center",va="top",fontsize=7.5)
    ax.text(5,10.5,"Fire triangle",ha="center",fontsize=9,fontweight="bold")
    ax.set_ylim(-1,11.5)
    ax2=fig.add_axes([0.37,0.0,0.63,1]); ax2.set_xlim(0,20); ax2.set_ylim(-3,11); ax2.axis('off')
    ax2.add_patch(Rectangle((0,0),20,-0.0,fc="none"))
    ax2.add_patch(Rectangle((0,-2.2),20,2.2,fc="#8B5E3C",ec="none"))      # soil/duff
    ax2.add_patch(Rectangle((0,-0.7),20,0.7,fc="#5C3B22",ec="none"))      # organic layer
    ax2.text(19.8,-1.4,"soil",ha="right",va="center",fontsize=7,color="white")
    ax2.text(19.8,-0.35,"organic layer (duff, roots)",ha="right",va="center",fontsize=6.5,color="white")
    for x in [3,7,11,15,18.5]:
        ax2.add_patch(Rectangle((x-0.2,0),0.4,6.0,fc=BROWN,ec="none"))
        ax2.add_patch(Ellipse((x,7.4),2.8,3.4,fc=GREEN,ec="none",alpha=0.9))
    # shrubs / litter
    for x in [1,5,9,13,17]:
        ax2.add_patch(Ellipse((x,0.45),1.8,0.9,fc="#6E8B3D",ec="none"))
    # flames
    def flame(x,y,h,w=0.9):
        ax2.add_patch(Polygon([(x-w,y),(x,y+h),(x+w,y)],fc=ORANGE,ec="none"))
        ax2.add_patch(Polygon([(x-w/2,y),(x,y+h*0.6),(x+w/2,y)],fc=YELLOW,ec="none"))
    for x in [1,5,9,13]: flame(x,0.2,1.2)
    for x in [7,11,15]: flame(x,6.6,3.0,1.2)
    for x in [4,10]: flame(x,-0.6,0.5,0.4)
    for (x,y,l) in [(13,3.3,"A"),(11,10.6,"B"),(4,-1.0,"C")]:
        pass
    ax2.text(5,2.3,"A",fontsize=9,fontweight="bold",color=DARK,ha="center",bbox=dict(boxstyle="circle,pad=0.2",fc="white",ec=DARK))
    ax2.text(11,10.0,"B",fontsize=9,fontweight="bold",color=DARK,ha="center",bbox=dict(boxstyle="circle,pad=0.2",fc="white",ec=DARK))
    ax2.text(4,-2.9,"C",fontsize=9,fontweight="bold",color=DARK,ha="center",bbox=dict(boxstyle="circle,pad=0.2",fc="white",ec=DARK))
    ax2.text(0.2,-5.0,"A  Surface fire: burns litter, grass and shrubs\nB  Crown fire: spreads through the tree canopy\nC  Ground fire: smolders in duff and roots",fontsize=7.2,va="top")
    ax2.text(10,11.6,"Three kinds of forest fire",ha="center",fontsize=9,fontweight="bold")
    ax2.set_ylim(-3.6,12.2)
    save(fig,OUT+'C7_fire_types.png')

# ---------- 3. fuel build-up ----------
def fuel():
    fig,ax=plt.subplots(figsize=(6.2,3.1))
    t=np.arange(0,101)
    # suppression: fuel rises toward a high level, then one severe fire at t=85
    f=np.zeros_like(t,dtype=float); v=10
    for i in t:
        v=v+(100-v)*0.03
        if i==85: v=8
        f[i]=v
    ax.plot(t,f,color=RED,lw=2.2,label="Every fire suppressed")
    g=np.zeros_like(t,dtype=float); v=10
    for i in t:
        v=v+(100-v)*0.03
        if i in (10,20,30,40,50,60,70,80,90,100): v=10
        g[i]=v
    ax.plot(t,g,color=GREEN,lw=2.0,label="Frequent low-intensity fires or prescribed burns")
    ax.axhline(70,color=GREY,ls="--",lw=1)
    ax.text(1,73,"fuel load above which crown\nfires become likely (approximate)",fontsize=7,color=GREY)
    ax.annotate("Severe, hard-to-control fire",xy=(84.5,f[84]-1),xytext=(52,100),fontsize=8,color=RED,
                arrowprops=dict(arrowstyle="-|>",color=RED))
    ax.set_xlabel("Years since the last fire (conceptual)"); ax.set_ylabel("Fuel load (relative units)")
    ax.set_ylim(0,112); ax.set_xlim(0,101); ax.legend(loc="upper center",bbox_to_anchor=(0.5,-0.2),ncol=1,fontsize=7.5,frameon=False)
    ax.set_title("Why total suppression builds up fuel (conceptual model)")
    save(fig,OUT+'C7_fuel_buildup.png')

# ---------- 4. harvest methods ----------
def harvest():
    fig,axs=plt.subplots(1,3,figsize=(6.4,2.5))
    rng=np.random.default_rng(3)
    def forest(ax,keep):
        ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis('off')
        ax.add_patch(Rectangle((0,0),10,10,fc="#DCE8C8",ec=GREY,lw=0.8))
        for x in np.arange(0.8,10,1.4):
            for y in np.arange(0.8,10,1.4):
                if keep(x,y): ax.add_patch(Circle((x,y),0.5,fc=GREEN,ec="#2B5A38",lw=0.5))
                else: ax.add_patch(Circle((x,y),0.12,fc=BROWN,ec="none"))
    forest(axs[0],lambda x,y:False); axs[0].set_title("Clearcutting\n(all trees removed)",fontsize=8.5)
    sel=set()
    forest(axs[1],lambda x,y: ((int(x/1.4)*3+int(y/1.4)*5)%4!=0)); axs[1].set_title("Selective cutting\n(scattered mature trees)",fontsize=8.5)
    forest(axs[2],lambda x,y: not (int(y/1.4) in (1,2,5,6))); axs[2].set_title("Strip cutting\n(narrow bands, rest reseeds)",fontsize=8.5)
    axs[2].text(5,10.5,"",fontsize=6)
    fig.text(0.5,0.0,"green = standing trees     brown dots = stumps",ha="center",fontsize=7.5,color=GREY)
    fig.tight_layout(w_pad=1.0,rect=(0,0.04,1,1))
    save(fig,OUT+'C7_harvest_methods.png')

# ---------- 5. mining methods ----------
def mining():
    fig,ax=plt.subplots(figsize=(6.4,3.5)); ax.set_xlim(0,30); ax.set_ylim(-14,6); ax.axis('off')
    ax.add_patch(Rectangle((0,-14),30,14,fc="#C9B79C",ec="none"))      # rock
    ax.add_patch(Rectangle((0,0),30,0.6,fc=GREEN,ec="none"))           # ground cover
    ax.add_patch(Rectangle((0,-1.6),30,1.0,fc="#8B5E3C",ec="none"))    # overburden thin lines
    # coal seam shallow
    ax.add_patch(Rectangle((0,-3.2),30,0.9,fc="#222",ec="none"))
    ax.text(29.7,-2.75,"shallow coal seam",color="white",fontsize=7,ha="right",va="center")
    # deep seam
    ax.add_patch(Rectangle((0,-11),30,1.1,fc="#222",ec="none"))
    ax.text(29.7,-10.45,"deep seam",color="white",fontsize=7,ha="right",va="center")
    ax.text(0.3,-12.7,"rock layers",fontsize=7,color=DARK)
    # open pit (left): trapezoid pit
    ax.add_patch(Polygon([(1,0.6),(10,0.6),(8,-3.2),(3,-3.2)],fc="white",ec=DARK,lw=1))
    ax.text(5.5,-1.2,"Open pit /\nstrip mine",ha="center",va="center",fontsize=7.5,fontweight="bold")
    ax.add_patch(Polygon([(10,0.6),(12.2,0.6),(11.2,1.6),(10.6,1.6)],fc="#8B5E3C",ec="none"))
    ax.text(11.2,2.4,"overburden\npile",ha="center",fontsize=7)
    # mountaintop removal (middle): mountain with removed top
    ax.add_patch(Polygon([(13,0.6),(16,5.2),(18.5,5.2),(22,0.6)],fc="#B49A7A",ec=DARK,lw=1,alpha=0.55,ls="--"))
    ax.add_patch(Polygon([(13,0.6),(16,3.2),(18.5,3.2),(22,0.6)],fc="#B49A7A",ec=DARK,lw=1))
    ax.add_patch(Polygon([(16,3.2),(18.5,3.2),(18.5,5.2),(16,5.2)],fc="none",ec=DARK,lw=0.8,ls=":"))
    ax.text(17.25,4.3,"removed\nsummit",ha="center",va="center",fontsize=6.5,color=DARK)
    ax.text(17.5,-0.9,"Mountaintop removal",ha="center",fontsize=7.5,fontweight="bold")
    # underground mine
    ax.add_patch(Rectangle((24.6,-10.9),0.7,10.9,fc="white",ec=DARK,lw=0.8))   # shaft
    ax.add_patch(Rectangle((19,-10.9),6.3,0.9,fc="white",ec=DARK,lw=0.8))      # tunnel
    ax.add_patch(Rectangle((24.2,0.6),1.5,1.4,fc=GREY,ec="none"))
    ax.text(21.7,-7.0,"Underground\n(shaft and tunnels)",ha="center",fontsize=7.5,fontweight="bold")
    ax.text(15,-12.4,"underground mines disturb less surface but cost more and are hazardous for miners",ha="center",fontsize=6.8,color=DARK)
    ax.set_title("Surface mining versus underground mining (cross-section)",fontsize=10,fontweight="bold")
    save(fig,OUT+'C7_mining_methods.png')

# ---------- 6. resources vs reserves ----------
def reserves():
    fig,ax=plt.subplots(figsize=(6.2,3.5)); ax.axis('off'); ax.set_xlim(-0.8,10); ax.set_ylim(0,7.4)
    cols=[(0.9,3.3,"Identified\n(well measured)"),(3.4,5.8,"Identified\n(less certain)"),(5.9,9.9,"Undiscovered\n(hypothetical or speculative)")]
    # economic rows: economic (bottom), marginal, sub-economic (top)
    rows=[(0.6,2.2,"Economic\nnow"),(2.3,3.7,"Marginal"),(3.8,5.5,"Sub-economic")]
    for (y0,y1,t) in rows:
        ax.text(0.8,(y0+y1)/2,t,ha="right",va="center",fontsize=7.5)
    for (x0,x1,t) in cols:
        ax.text((x0+x1)/2,5.65,t,ha="center",va="bottom",fontsize=7.5)
    ax.add_patch(Rectangle((0.9,0.6),2.4,1.6,fc=RED,ec="white",lw=1.5))
    ax.text(2.1,1.4,"RESERVES",ha="center",va="center",color="white",fontsize=8.5,fontweight="bold")
    for (x0,x1) in [(3.4,5.8),(5.9,9.9)]:
        ax.add_patch(Rectangle((x0,0.6),x1-x0,1.6,fc="#D9A9AE",ec="white",lw=1.5))
    for (y0,y1) in [(2.3,3.7),(3.8,5.5)]:
        for (x0,x1) in [(0.9,3.3),(3.4,5.8),(5.9,9.9)]:
            ax.add_patch(Rectangle((x0,y0),x1-x0,y1-y0,fc="#F0DADC",ec="white",lw=1.5))
    ax.text(5.35,0.15,"Resources = all cells.  A higher price or cheaper technology moves material from the upper rows down into the economic row.",ha="center",fontsize=7,color=GREY,va="center")
    ax.text(5.35,7.2,"Reserves are a small part of total resources",ha="center",fontsize=10,fontweight="bold")
    ax.text(5.35,6.6,"horizontal axis: how certain the geology is   |   vertical axis: how profitable to mine",ha="center",fontsize=7,color=GREY)
    ax.set_ylim(0,7.5)
    save(fig,OUT+'C7_reserves_resources.png')

# ---------- 7. habitat fragmentation ----------
def frag():
    fig,axs=plt.subplots(1,2,figsize=(6.2,3.0))
    for ax in axs:
        ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis('off')
        ax.add_patch(Rectangle((0,0),10,10,fc="#E9E2CF",ec=GREY,lw=0.8))   # surrounding land
    EDGE="#B9D6A0"; CORE="#4F9A5E"
    ax=axs[0]; ax.set_title("Before: one large forest",fontsize=9)
    ax.add_patch(Rectangle((0.6,0.6),8.8,8.8,fc=EDGE,ec="none"))
    ax.add_patch(Rectangle((1.6,1.6),6.8,6.8,fc=CORE,ec="none"))
    ax.text(5,5,"large interior\n(core habitat)",ha="center",va="center",fontsize=8.5,color="white",fontweight="bold")
    ax=axs[1]; ax.set_title("After: roads cut it into fragments",fontsize=9)
    for (x0,y0) in [(0.6,5.4),(5.4,5.4),(0.6,0.6),(5.4,0.6)]:
        ax.add_patch(Rectangle((x0,y0),4.0,4.0,fc=EDGE,ec="none"))
        ax.add_patch(Rectangle((x0+1,y0+1),2.0,2.0,fc=CORE,ec="none"))
    ax.add_patch(Rectangle((0,4.4),10,1.0,fc="#555",ec="none"))
    ax.add_patch(Rectangle((4.4,0),1.0,10,fc="#555",ec="none"))
    ax.text(5,4.9,"road",ha="center",va="center",fontsize=6.5,color="white")
    ax.text(2.6,7.4,"small\ninterior",ha="center",va="center",fontsize=7,color="white")
    fig.text(0.5,0.0,"dark green = interior habitat     light green = edge (noise, light, predators, weeds, road salt)",ha="center",fontsize=7,color=GREY)
    fig.tight_layout(rect=(0,0.04,1,1))
    save(fig,OUT+'C7_fragmentation.png')

for f in (soil,fire,fuel,harvest,mining,reserves,frag): f()
