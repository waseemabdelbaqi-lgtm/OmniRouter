import sys, math
sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
from matplotlib.patches import Wedge
OUT='/home/user/OmniRouter/apes_project/content/book2/figs/'

# 1 plates map
def plates_map():
    fig,ax=canvas(6.2,3.6,(0,10),(0,6.3))
    def rect(x,y,w,h,fc): ax.add_patch(Rectangle((x,y),w,h,fc=fc,ec=DARK,lw=2))
    rect(0.1,2.2,3.2,3.8,SKY); rect(3.3,2.2,3.3,3.8,SKY); rect(6.6,2.2,3.3,3.8,SAND); rect(6.6,0.1,3.3,2.1,SKY)
    for t,x,y in [("Plate P",1.7,5.45),("Plate Q",4.95,5.45),("Plate R",8.25,5.45),("Plate S",8.25,0.55)]:
        ax.text(x,y,t,ha="center",fontsize=11,fontweight="bold")
    def ar(p,q): ax.add_patch(FancyArrowPatch(p,q,arrowstyle="-|>",mutation_scale=18,color=RED,lw=2.6))
    ar((2.9,3.9),(1.5,3.9)); ar((3.7,3.9),(5.1,3.9)); ar((5.9,3.0),(6.4,3.0)) if False else None
    ar((4.6,4.6),(6.3,4.6)); ar((9.2,3.9),(7.3,3.9))
    ar((9.3,2.65),(7.5,2.65)); ar((7.2,1.65),(9.0,1.65))
    for lab,x,y in [("I",3.3,2.7),("II",6.6,2.7),("III",8.9,2.2)]:
        ax.add_patch(Circle((x,y),0.33,fc="white",ec=DARK,lw=1.6,zorder=5)); ax.text(x,y,lab,ha="center",va="center",fontsize=10,fontweight="bold",zorder=6)
    ax.text(0.1,0.4,"Red arrows show the direction each plate is moving.",fontsize=8.5,style="italic")
    ax.text(0.1,0.0,"Blue = oceanic crust; tan = continental crust.",fontsize=8.5,style="italic")
    save(fig,OUT+'QB_U4_plates_map.png')

def benioff():
    rng=np.random.default_rng(4)
    x=rng.uniform(0,450,45); d=10+0.45*x+rng.normal(0,14,45); d=np.clip(d,3,None)
    fig,ax=plt.subplots(figsize=(6,3.4))
    ax.scatter(x,d,s=22,color=RED,alpha=.85,edgecolor="white",lw=.4)
    ax.invert_yaxis(); ax.set_xlabel("Distance inland from the trench (km)"); ax.set_ylabel("Earthquake focal depth (km)")
    ax.set_title("Earthquake foci along a 100-km-wide strip"); ax.set_xlim(0,460); ax.grid(alpha=.25)
    save(fig,OUT+'QB_U4_benioff.png')

def soil_profile():
    fig=plt.figure(figsize=(6.2,3.6))
    gs=fig.add_gridspec(1,3,width_ratios=[1.1,1.4,1.4],wspace=0.08)
    ax0=fig.add_subplot(gs[0]); tops=[0,6,28,75,130]; cols=["#3B2A1E","#6B4A2F","#B5763A","#D9C9A8"]; labs=["W","X","Y","Z"]
    for i in range(4):
        ax0.add_patch(Rectangle((0,tops[i]),1,tops[i+1]-tops[i],fc=cols[i],ec="black"))
        ax0.text(0.5,(tops[i]+tops[i+1])/2,labs[i],ha="center",va="center",color="white" if i<3 else "black",fontsize=13,fontweight="bold")
    rng=np.random.default_rng(2)
    ax0.scatter(rng.uniform(.1,.9,14),rng.uniform(78,128,14),marker="^",s=18,color="#7a7a7a")
    ax0.set_xlim(0,1); ax0.set_ylim(130,0); ax0.set_xticks([]); ax0.set_yticks(tops); ax0.set_ylabel("Depth (cm)")
    ax0.set_title("Profile",fontsize=10); ax0.spines["bottom"].set_visible(False)
    mid=[(tops[i]+tops[i+1])/2 for i in range(4)]; hgt=[tops[i+1]-tops[i] for i in range(4)]
    for k,(vals,t,c) in enumerate([([38,7,1.2,0.4],"Organic matter (%)",GREEN),([6,14,36,24],"Clay (%)",ORANGE)]):
        ax=fig.add_subplot(gs[k+1]); ax.barh(mid,vals,height=[h*0.9 for h in hgt],color=c,edgecolor="black")
        ax.set_ylim(130,0); ax.set_yticks([]); ax.set_title(t,fontsize=10); ax.set_xlim(0,max(vals)*1.25)
        for m,v in zip(mid,vals): ax.text(v+max(vals)*0.03,m,f"{v:g}",va="center",fontsize=9)
    save(fig,OUT+'QB_U4_soil_profile.png')

def triangle():
    fig,ax=plt.subplots(figsize=(5.4,4.9)); ax.axis("off"); ax.set_aspect("equal")
    T=np.array([.5,math.sqrt(3)/2]); BL=np.array([0,0]); BR=np.array([1,0])
    P=lambda cl,si,sa:(cl*T+si*BL+sa*BR)/(cl+si+sa)
    ax.add_patch(Polygon([T,BL,BR],fc="#FBF6EC",ec="black",lw=1.6))
    for v in range(10,100,10):
        f=v/100; ls=dict(color="#BBB",lw=.6)
        a=P(f,1-f,0); b=P(f,0,1-f); ax.plot(*zip(a,b),**ls)
        a=P(1-f,f,0); b=P(0,f,1-f); ax.plot(*zip(a,b),**ls)
        a=P(1-f,0,f); b=P(0,1-f,f); ax.plot(*zip(a,b),**ls)
    for v in range(20,100,20):
        f=v/100
        p=P(f,0,1-f); ax.text(p[0]+.03,p[1]+.005,str(v),color=BLUE,fontsize=8.5,va="center")
        p=P(1-f,f,0); ax.text(p[0]-.03,p[1],str(v),color=GREEN,fontsize=8.5,ha="right",va="center")
        p=P(0,1-f,f); ax.text(p[0],p[1]-.035,str(v),color=BROWN,fontsize=8.5,ha="center",va="top")
    ax.text(.86,.55,"% clay\n(horizontal lines)",color=BLUE,fontsize=9,ha="center",rotation=-60)
    ax.text(.12,.55,"% silt\n(lines slope down to the right)",color=GREEN,fontsize=8,ha="center",rotation=60)
    ax.text(.5,-.13,"% sand (lines slope down to the left)",color=BROWN,fontsize=9,ha="center")
    pts={"1":(10,10,80),"2":(20,40,40),"3":(60,25,15),"4":(15,65,20)}
    for k,(cl,si,sa) in pts.items():
        p=P(cl,si,sa); ax.scatter(*p,s=170,color=RED,zorder=5,edgecolor="white"); ax.text(p[0],p[1],k,color="white",ha="center",va="center",fontsize=9,fontweight="bold",zorder=6)
    ax.set_xlim(-.12,1.12); ax.set_ylim(-.2,.92)
    save(fig,OUT+'QB_U4_texture_triangle.png')

def atm():
    pts=[(15,0),(-56,12),(-56,20),(-2,50),(-2,52),(-90,86),(-80,95),(-10,110),(90,120)]
    t=[p[0] for p in pts]; h=[p[1] for p in pts]
    fig,ax=plt.subplots(figsize=(5.4,4.0))
    for lo,hi,c,l in [(0,12,"#E3EEF7","W"),(12,50,"#EFE4F2","X"),(50,86,"#E8F1E4","Y"),(86,120,"#F7ECDD","Z")]:
        ax.axhspan(lo,hi,color=c,zorder=0); ax.text(112,(lo+hi)/2,l,fontsize=16,fontweight="bold",color=RED,va="center",ha="center")
    ax.plot(t,h,color=RED,lw=2.4)
    for y in (12,50,86): ax.axhline(y,color=GREY,ls="--",lw=.8)
    ax.set_xlim(-100,125); ax.set_ylim(0,120); ax.set_xlabel("Temperature (°C)"); ax.set_ylabel("Altitude (km)")
    ax.set_title("Average temperature profile of the atmosphere")
    ax.set_yticks([0,12,20,40,50,60,80,86,100,120])
    save(fig,OUT+'QB_U4_atm_profile.png')

def circ():
    fig,ax=plt.subplots(figsize=(6.2,3.4)); ax.set_xlim(-6,96); ax.set_ylim(-14,60); ax.axis("off")
    ax.add_patch(Rectangle((0,0),90,-3.5,fc="#C9D8C0",ec="black",lw=1)); ax.add_patch(Rectangle((0,0),90,50,fc="#F4F8FB",ec="none",zorder=0))
    def A(p,q): ax.add_patch(FancyArrowPatch(p,q,arrowstyle="-|>",mutation_scale=14,color=BLUE,lw=2))
    # Hadley
    A((28,3),(4,3)); A((0,5),(0,38)); A((3,40),(27,40)); A((30,38),(30,5))
    # Ferrel
    A((32,3),(56,3)); A((60,5),(60,38)); A((57,40),(33,40)); A((30,38),(30,5)) if False else None
    # Polar
    A((88,3),(64,3)); A((60,5),(60,38)) if False else None; A((63,40),(87,40)); A((90,38),(90,5))
    ax.plot([0,90],[0,0],color="black",lw=1.2)
    for lat,lab in [(0,"W"),(30,"X"),(60,"Y")]:
        ax.add_patch(Circle((lat,-9),3.4,fc="white",ec=RED,lw=1.6)); ax.text(lat,-9,lab,ha="center",va="center",fontsize=11,fontweight="bold",color=RED)
    for lat in (0,30,60,90): ax.text(lat,-3.2-8.6+8,"",fontsize=1); ax.text(lat,45,f"{lat}°",ha="center",fontsize=9,color=GREY)
    ax.text(45,55,"Meridional cross-section, Northern Hemisphere (equator at left, pole at right)",ha="center",fontsize=9)
    ax.text(75,-9,"Blue arrows = direction of air movement",fontsize=8,style="italic",ha="center")
    save(fig,OUT+'QB_U4_circulation.png')

def watershed():
    fig,ax=canvas(6.0,4.8,(0,10),(-0.8,10))
    div=[(1,9),(5,9.6),(9,8.2),(9.3,4.5),(7.2,1.4),(3.6,0.8),(1.2,3.5),(0.7,6.6),(1,9)]
    ax.add_patch(Polygon(div,fc="#EEF4E6",ec=DARK,lw=2.2,ls="--"))
    t1=[(2.0,8.3),(2.6,7.2),(3.4,6.3),(4.3,5.4)]; t2=[(8.4,7.9),(7.5,7.2),(6.5,6.4),(5.5,5.8),(4.5,5.3)]
    main=[(4.5,5.3),(4.7,3.8),(4.5,2.5),(4.7,1.4),(4.6,0.4)]
    for s in (t1,t2,main): ax.plot(*zip(*s),color=BLUE,lw=2.8,solid_capstyle="round")
    ax.add_patch(Ellipse((4.6,-0.35),2.4,0.9,fc=SKY,ec=BLUE)); ax.text(4.6,-0.35,"Lake",ha="center",va="center",fontsize=9)
    def flow(p,q): ax.add_patch(FancyArrowPatch(p,q,arrowstyle="-|>",mutation_scale=11,color="#0b3d63",lw=1.4,zorder=6))
    flow((2.8,6.95),(3.15,6.6)); flow((7.1,6.9),(6.8,6.65)); flow((5.1,5.55),(4.8,5.4)); flow((4.65,3.3),(4.6,2.9))
    ax.add_patch(Rectangle((5.9,7.2),1.2,0.9,fc="#D9B26F",ec=DARK,hatch="//",lw=1)); ax.text(6.5,8.25,"Fertilized field",ha="center",fontsize=8.5)
    ax.add_patch(FancyArrowPatch((6.5,7.2),(6.5,6.65),arrowstyle="-|>",mutation_scale=11,color=BROWN,lw=1.8,zorder=6))
    for n,(x,y) in {"1":(3.0,6.75),"2":(7.8,7.5),"3":(5.5,5.8),"4":(4.7,1.7)}.items():
        ax.add_patch(Circle((x,y),0.28,fc=RED,ec="white",zorder=7)); ax.text(x,y,n,color="white",ha="center",va="center",fontsize=9,fontweight="bold",zorder=8)
    ax.text(0.2,9.6,"- - -  watershed divide\n→  stream flow direction",fontsize=8.5,va="top",style="italic")
    ax.text(8.3,1.2,"Sites 1–4:\nwater-quality\nsampling points",fontsize=8.5,color=RED,ha="center")
    save(fig,OUT+'QB_U4_watershed.png')

def orbit():
    fig,ax=canvas(6.2,3.9,(-4.6,4.6),(-2.7,2.7)); a,b=3.0,1.6
    th=np.linspace(0,2*np.pi,200); ax.plot(a*np.cos(th),b*np.sin(th),color=GREY,lw=1.2)
    ax.add_patch(Circle((0,0),.55,fc=YELLOW,ec=ORANGE,lw=2)); ax.text(0,-.85,"Sun",ha="center",fontsize=9)
    pos={"W":(0,b),"X":(a,0),"Y":(0,-b),"Z":(-a,0)}
    tilt=math.radians(23.5); d=np.array([math.sin(tilt),math.cos(tilt)])
    for lab,(x,y) in pos.items():
        al=math.degrees(math.atan2(-y,-x))
        ax.add_patch(Circle((x,y),.42,fc="#CFE3F3",ec="black",lw=1.2,zorder=3))
        ax.add_patch(Wedge((x,y),.42,al+90,al+270,fc="#34495E",ec="black",lw=1.0,zorder=4,alpha=.85))
        e1=np.array([x,y])+d*.85; e2=np.array([x,y])-d*.85
        ax.plot([e1[0],e2[0]],[e1[1],e2[1]],color=RED,lw=2,zorder=5); ax.text(e1[0]+.12,e1[1]+.1,"N",color=RED,fontsize=9,fontweight="bold",zorder=6)
        off={"W":(0,1.15),"X":(.9,-.1),"Y":(0,-1.15),"Z":(-.9,-.1)}[lab]
        ax.text(x+off[0],y+off[1]-0.05 if lab in("X","Z") else y+off[1],lab,fontsize=14,fontweight="bold",ha="center",va="center")
    ax.add_patch(FancyArrowPatch((-2.4,-1.1),(-1.3,-1.52),arrowstyle="-|>",mutation_scale=13,color=GREY,lw=1.4,connectionstyle="arc3,rad=.3"))
    ax.text(-4.5,-2.55,"Orbit not to scale. Red line = Earth's axis, N = North Pole;\nshaded half of each Earth is in darkness. Arrow = direction of orbit.",fontsize=8,style="italic")
    save(fig,OUT+'QB_U4_orbit.png')

def daylen():
    def dl(lat,N):
        d=math.radians(23.44*math.sin(2*math.pi*(284+N)/365)); p=math.radians(lat)
        return 24/math.pi*math.acos(-math.tan(p)*math.tan(d))
    days=[15,46,74,105,135,166,196,227,258,288,319,349]; m="JFMAMJJASOND"
    fig,ax=plt.subplots(figsize=(6,3.5))
    for lat,lab,c,mk in [(3,"City P",BLUE,"o"),(40,"City Q",RED,"s"),(-45,"City R",GREEN,"^")]:
        ax.plot(range(12),[dl(lat,n) for n in days],marker=mk,color=c,label=lab,lw=2,ms=5)
    ax.set_xticks(range(12)); ax.set_xticklabels(list(m)); ax.set_ylabel("Hours of daylight on the 15th"); ax.set_xlabel("Month"); ax.set_ylim(8,16.5)
    ax.grid(alpha=.25); ax.legend(loc="upper center",ncol=3,frameon=False); ax.set_title("Day length through one year, three cities")
    save(fig,OUT+'QB_U4_daylength.png')
    print({lat:[round(dl(lat,n),1) for n in days] for lat in (3,40,-45)})

def rainshadow():
    fig,ax=plt.subplots(figsize=(6.2,3.5))
    xs=[0,15,55,78,100]; ys=[0,20,2500,600,550]
    ax.fill_between([0,15],[-300,-300],[0,0],color="#BFE0F2"); ax.fill_between([0,15],[0,0],[0,0])
    ax.fill_between(xs,[-300]*5,ys,color=BROWN,alpha=.85); ax.fill_between([0,15],[-300,-300],[0,0],color="#BFE0F2"); ax.plot(xs,ys,color="black")
    def el(x): return float(np.interp(x,xs,ys))
    for lab,x in [("W",10),("X",40),("Y",55),("Z",85)]:
        y=el(x); ax.scatter(x,y+60,s=200,color=RED,zorder=5,edgecolor="white"); ax.text(x,y+60,lab,color="white",ha="center",va="center",fontsize=10,fontweight="bold",zorder=6)
    ax.add_patch(FancyArrowPatch((2,3000),(30,3000),arrowstyle="-|>",mutation_scale=16,color=BLUE,lw=2.4)); ax.text(2,3200,"Prevailing wind (moist air from the ocean)",fontsize=9,color=BLUE)
    ax.set_ylim(-300,3600); ax.set_xlim(0,100); ax.set_xlabel("Distance inland (km)"); ax.set_ylabel("Elevation (m)"); ax.text(6,-180,"Ocean",fontsize=8.5)
    ax.set_title("West–east cross-section of a mountain range")
    save(fig,OUT+'QB_U4_rainshadow.png')

def hillside():
    fig,ax=canvas(6.0,4.4,(0,10),(0,8))
    ax.add_patch(Rectangle((0.3,1.6),9.4,6.0,fc="#F1EAD5",ec="black",lw=1.2))
    for i,y in enumerate([6.9,5.2,3.5,2.3]): ax.plot([0.3,9.7],[y+0.25*(i%2),y+0.25*(i%2)],color="#C9B98F",lw=.8,ls=":")
    ax.text(9.55,7.3,"Higher ground",ha="right",fontsize=8,style="italic"); 
    blocks={"Block 1":(0.6,3.8,"slope 6%\nloam"),"Block 2":(3.6,3.8,"slope 6%\nloam"),"Block 3":(6.6,3.8,"slope 14%\nclay loam"),"Block 4":(0.6,1.9,"slope 14%\nloam")}
    # place blocks: two on upper row, one more on right; use layout 2x2-ish
    layout=[("Block 1",0.6,4.4,"slope 6%\nloam"),("Block 2",3.4,4.4,"slope 6%\nloam"),("Block 3",6.2,4.4,"slope 14%\nclay loam"),("Block 4",6.2,2.2,"slope 14%\nloam")]
    for n,x,y,t in layout:
        ax.add_patch(Rectangle((x,y),2.6,1.9,fc="#DDE8C9",ec=GREEN,lw=1.6))
        ax.text(x+1.3,y+1.45,n,ha="center",fontweight="bold",fontsize=10); ax.text(x+1.3,y+.65,t,ha="center",fontsize=9)
        for k in range(4): ax.scatter(x+.4+k*.55,y+.2,s=22,color=GREEN,marker="^")
    ax.add_patch(Polygon([(0.3,1.6),(9.7,1.6),(9.7,1.0),(6,1.35),(0.3,0.9)],fc=BLUE,alpha=.8,ec=BLUE)); ax.text(2.5,1.07,"Stream",color="white",fontsize=10,fontweight="bold")
    ax.add_patch(FancyArrowPatch((2.0,4.3),(2.0,2.1),arrowstyle="-|>",mutation_scale=15,color=BROWN,lw=2)); ax.text(2.15,3.1,"Runoff\ndownhill",fontsize=8.5,color=BROWN)
    ax.text(0.3,7.8,"Orchard (planted the same year); rows of apple trees, bare soil between rows",fontsize=8.5,style="italic")
    save(fig,OUT+'QB_U4_frq1_hillside.png')

SST=[-0.4,0.2,1.9,0.3,-0.7,-1.5,-0.2,0.5,2.4,0.6,-0.9,-0.3]; LAND=[8.1,7.6,3.2,6.8,8.7,9.4,8.0,6.5,1.9,5.8,9.0,8.3]
def enso():
    fig,(a1,a2)=plt.subplots(2,1,figsize=(6,4.4),sharex=True,gridspec_kw={"hspace":.12})
    yrs=np.arange(1,13); a1.bar(yrs,SST,color=[RED if v>0 else BLUE for v in SST]); a1.axhline(0,color="black",lw=.8)
    a1.set_ylabel("SST anomaly (°C)"); a1.set_title("Sea surface temperature anomaly, eastern equatorial Pacific"); a1.grid(axis="y",alpha=.25)
    a2.plot(yrs,LAND,marker="o",color=DARK,lw=2); a2.set_ylabel("Anchovy landings\n(million metric tons)"); a2.set_ylim(0,11); a2.grid(alpha=.25)
    a2.set_xticks(yrs); a2.set_xlabel("Year"); a2.set_title("Peruvian anchovy landings",fontsize=10)
    save(fig,OUT+'QB_U4_enso_series.png')

def climato():
    m="JFMAMJJASOND"
    H=([260,215,200,130,85,45,20,25,70,150,240,290],[7,8,9,11,14,16,18,18,16,12,9,7])
    P=([30,25,30,28,35,30,15,12,18,22,32,33],[-2,0,5,10,15,20,24,23,17,10,3,-1])
    fig,axs=plt.subplots(1,2,figsize=(6.4,3.3),sharey=True)
    for ax,(pr,tp),n in zip(axs,(H,P),("Harbor (coast)","Plain (inland)")):
        ax.bar(range(12),pr,color=SKY,edgecolor=BLUE); ax.set_ylim(0,320); ax.set_xticks(range(12)); ax.set_xticklabels(list(m),fontsize=8); ax.set_title(n,fontsize=10)
        a2=ax.twinx(); a2.plot(range(12),tp,color=RED,marker="o",ms=3.5,lw=2); a2.set_ylim(-10,32); a2.spines["right"].set_visible(True)
        if ax is axs[0]: ax.set_ylabel("Precipitation (mm)"); a2.set_yticklabels([])
        else: a2.set_ylabel("Mean temperature (°C)",color=RED)
    fig.subplots_adjust(wspace=.12)
    save(fig,OUT+'QB_U4_climatograms.png')
    print(sum(H[0]),sum(P[0]),sum(H[1])/12,sum(P[1])/12)

for f in (plates_map,benioff,soil_profile,triangle,atm,circ,watershed,orbit,daylen,rainshadow,hillside,enso,climato): f()
