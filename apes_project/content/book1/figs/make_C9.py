import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book1/figs/'
SANDC="#EAD9B0"; WET="#BFD9EC"; CLAY="#A98467"; SOIL="#C9B48C"

# ---------- Fig: thermal inversion (redrawn, labels clear of the line)
fig,axs=plt.subplots(1,2,figsize=(6.4,3.5))
alt=np.linspace(0,1.5,60)
normal=20-9*alt
inv=np.where(alt<0.5,8+14*alt,15-3*(alt-0.5))
for ax,t,prof in [(axs[0],"Normal conditions",normal),(axs[1],"Thermal inversion",inv)]:
    ax.plot(prof,alt,color=RED,lw=2.4); ax.set_xlim(0,24); ax.set_ylim(0,1.5)
    ax.set_xlabel("Air temperature (°C)"); ax.set_title(t); ax.set_yticks([0,0.5,1.0,1.5])
axs[0].set_ylabel("Altitude above ground (km)")
axs[0].annotate("",xy=(3.5,1.3),xytext=(3.5,0.2),arrowprops=dict(arrowstyle="-|>",color=GREEN,lw=2))
axs[0].text(4.5,0.75,"Warm surface air\nrises and carries\npollutants upward",fontsize=8,color=GREEN,va="center")
axs[0].text(11,1.38,"cooler air aloft",fontsize=8,color=GREY)
axs[1].axhspan(0,0.5,color="#8d8576",alpha=0.3)
axs[1].axhline(0.5,color=BLUE,lw=3,alpha=0.7)
axs[1].text(23.5,0.56,"top of the cold layer:\nwarm air above acts as a lid",fontsize=7.5,color=BLUE,ha="right",va="bottom")
axs[1].text(23.5,0.25,"smog and particulates\ntrapped near the ground",fontsize=8,color=DARK,ha="right",va="center")
for x in (2,4,6): axs[1].annotate("",xy=(x,0.46),xytext=(x,0.2),arrowprops=dict(arrowstyle="-|>",color=GREY,lw=1))
axs[1].text(1,0.7,"cool surface air is denser\nthan the warm air over it,\nso it cannot rise",fontsize=7.5,color=GREY,va="bottom")
fig.tight_layout(); save(fig,D+'C9_inversion.png')


# ---------- Fig: groundwater pollution
fig,ax=plt.subplots(figsize=(6.4,4.0)); ax.set_xlim(0,100); ax.set_ylim(0,62); ax.axis("off")
x=np.linspace(0,100,200); wt=30-5*(x/100)
ax.fill_between(x,0,8,color=CLAY); ax.fill_between(x,8,wt,color=WET); ax.fill_between(x,wt,42,color=SANDC)
ax.plot(x,wt,color=BLUE,lw=1.5,ls="--"); ax.plot(x,[42]*200,color="#5a4a2a",lw=1.5)
ax.text(1,3.5,"Clay layer (aquitard): water barely moves through it",fontsize=7.5,color="white",va="center")
ax.text(1,19,"Saturated zone = aquifer (every pore filled with water)",fontsize=7.5,color=DARK)
ax.text(60,36.3,"Unsaturated zone\n(pores hold air and water)",fontsize=7.5,color=DARK,va="center")
ax.text(1,wt[0]+1.6,"water table",fontsize=7.5,color=BLUE,ha="left",style="italic")
ax.add_patch(Polygon([[3,42],[7,48],[19,48],[22,42]],fc="#7d7466",ec="#333")); ax.text(12.5,44.4,"Landfill",fontsize=7.5,ha="center",color="white",weight="bold")
ax.add_patch(Rectangle((33,44),9,4,fc="#c44",ec="#333")); ax.text(37.5,49.5,"Gas station",fontsize=7.5,ha="center")
ax.add_patch(Rectangle((34,36.5),7,3.2,fc="#555",ec="black")); ax.text(32.5,38,"leaking\ntank",fontsize=7,ha="right",va="center",color=DARK)
ax.add_patch(Rectangle((52,44),9,5,fc="#e8d6a6",ec="#333")); ax.add_patch(Polygon([[51,49],[56.5,54],[62,49]],fc=RED,ec="#333")); ax.text(56.5,56,"Home with septic tank",fontsize=7.5,ha="center")
ax.add_patch(Rectangle((54,38.5),5,3,fc="#777",ec="black"))
ax.add_patch(Rectangle((68,42),16,1.6,fc=GREEN,ec=GREEN)); ax.text(76,46.5,"Fertilized field",fontsize=7.5,ha="center")
for xx in (71,76,81): ax.annotate("",xy=(xx,39),xytext=(xx,45),arrowprops=dict(arrowstyle="-|>",color=ORANGE,lw=1.2))
def plume(p0,p1,H,c):
    t=np.linspace(0,1,60); cx=p0[0]+(p1[0]-p0[0])*t; cy=p0[1]+(p1[1]-p0[1])*t; hw=H*np.sin(np.pi*t**0.8)**0.8
    ax.add_patch(Polygon(np.c_[np.r_[cx,cx[::-1]],np.r_[cy+hw,(cy-hw)[::-1]]],fc=c,ec="none",alpha=0.6))
plume((13,41),(52,27),3.2,"#7a4a2a")      # landfill leachate
plume((38,36.5),(82,22),4.2,"#d9822b")  # fuel plume
for p,q in (((13,41.8),(13,36)),((38,36.5),(38,31))): ax.annotate("",xy=q,xytext=p,arrowprops=dict(arrowstyle="-|>",color=DARK,lw=1.2))
ax.text(60,16.5,"contaminant plumes drift with the groundwater",fontsize=7.5,color=DARK,ha="center",weight="bold")
ax.plot([92,92],[42,14],color="#222",lw=3); ax.add_patch(Rectangle((90,42),4,3,fc="#444")); ax.text(92,47,"Drinking-water\nwell",fontsize=7.5,ha="center")
ax.annotate("",xy=(72,12.5),xytext=(32,12.5),arrowprops=dict(arrowstyle="-|>",color=BLUE,lw=2))
ax.text(52,9.4,"groundwater flow (cm to a few m per day)",fontsize=7.5,color=BLUE,ha="center")
fig.savefig(D+'C9_groundwater.png'); plt.close(fig)

# ---------- Fig: septic system
fig,ax=plt.subplots(figsize=(6.4,3.7)); ax.set_xlim(0,100); ax.set_ylim(0,58); ax.axis("off")
ax.add_patch(Rectangle((0,0),100,34,fc=SOIL)); ax.add_patch(Rectangle((0,0),100,6,fc=WET)); ax.plot([0,100],[6,6],color=BLUE,ls="--",lw=1.2)
ax.text(99,2.6,"water table",fontsize=7.5,color=BLUE,ha="right",style="italic"); ax.plot([0,100],[34,34],color="#5a4a2a",lw=1.5)
ax.add_patch(Rectangle((3,34),14,9,fc="#e8d6a6",ec="#333")); ax.add_patch(Polygon([[2,43],[10,50],[18,43]],fc=RED,ec="#333")); ax.text(10,52,"1  House",fontsize=8.5,ha="center",weight="bold")
ax.plot([10,10,26],[34,28,28],color="#333",lw=2)
ax.add_patch(Rectangle((26,19),24,16,fc="#d8e2e8",ec="#333",lw=1.5))
ax.add_patch(Rectangle((26,19),24,6,fc="#8a6f4e",ec="none")); ax.add_patch(Rectangle((26,29.5),24,2.5,fc="#c8b98a",ec="none"))
ax.plot([33,33],[19,32],color="#333",lw=1.2); ax.plot([43,43],[19,32],color="#333",lw=1.2)
ax.text(38,22,"sludge",fontsize=7,ha="center",color="white"); ax.text(38,26.6,"clarified\nliquid",fontsize=7,ha="center",va="center"); ax.text(38,30.8,"scum",fontsize=6.5,ha="center",va="center")
ax.text(38,37.5,"2  Septic tank",fontsize=8.5,ha="center",weight="bold")
ax.plot([50,58],[27,27],color="#333",lw=2); ax.add_patch(Rectangle((58,24.5),5,5,fc="#999",ec="#333")); ax.text(60.5,21.3,"distribution\nbox",fontsize=7,ha="center",va="top")
ax.add_patch(Rectangle((66,23.5),30,6.5,fc="#b5b5b5",ec="#666",alpha=0.7)); ax.plot([63,96],[27.2,27.2],color="#222",lw=2.2,ls=(0,(3,1)))
ax.text(81,38,"3  Drain field\n(perforated pipe in gravel trench)",fontsize=8.5,ha="center",weight="bold",va="center")
for xx in (70,76,82,88,94): ax.annotate("",xy=(xx,16),xytext=(xx,23),arrowprops=dict(arrowstyle="-|>",color=BLUE,lw=1.1))
ax.text(80,11,"effluent seeps down: soil microbes\nbreak down waste and soil particles\nfilter out germs",fontsize=7,ha="center",va="center",color=DARK)
ax.text(36,11.5,"solids settle, anaerobic bacteria\ndigest some; sludge is pumped\nout every few years",fontsize=7,ha="center",va="center",color=DARK)
fig.savefig(D+'C9_septic.png'); plt.close(fig)

# ---------- Fig: drinking-water treatment
fig,ax=canvas(6.4,3.9,(-0.01,1.01),(0,1))
steps=[("1 Intake and screens","Screens remove\nleaves, fish, debris"),
("2 Coagulation","Alum added and mixed\nfast: tiny particles\nlose their charge"),
("3 Flocculation","Slow stirring: particles\nclump into heavy flocs"),
("4 Sedimentation","Flocs settle out as\nsludge in a basin"),
("5 Filtration","Sand and carbon filters\ntrap fine particles,\ncysts and some organics"),
("6 Disinfection","Chlorine, chloramine,\nozone or UV kills\nremaining microbes"),
("7 Storage","Clear well: contact\ntime and a chlorine\nresidual"),
("8 Distribution","Pipes carry safe water\nto homes; residual\nstops regrowth")]
cols=["#DCE9F2","#E6D9D9","#E6D9D9","#E6D9D9","#D5E8D0","#F7E8B0","#DCE9F2","#DCE9F2"]
w,h=0.215,0.32; xs=[0.01,0.26,0.51,0.76]
for i,(t,d) in enumerate(steps):
    r=i//4; c=i%4 if r==0 else 3-i%4
    x0=xs[c]; y0=0.52 if r==0 else 0.10
    ax.add_patch(FancyBboxPatch((x0,y0),w,h,boxstyle="round,pad=0.005,rounding_size=0.02",fc=cols[i],ec=RED,lw=1.2))
    ax.text(x0+w/2,y0+h-0.04,t,ha="center",va="top",fontsize=7.6,weight="bold",color=DARK)
    ax.text(x0+w/2,y0+h-0.115,d,ha="center",va="top",fontsize=7)
for c in range(3): arrow(ax,(xs[c]+w+0.006,0.68),(xs[c+1]-0.006,0.68))
arrow(ax,(xs[3]+w/2,0.515),(xs[3]+w/2,0.425))
for c in range(3,0,-1): arrow(ax,(xs[c]-0.006,0.26),(xs[c-1]+w+0.006,0.26))
ax.text(0.5,0.99,"Conventional surface-water treatment plant",ha="center",va="top",fontsize=10,weight="bold")
ax.text(0.5,0.02,"Particles are removed first (steps 1 to 5); dirty water would use up the disinfectant.",ha="center",fontsize=7.8,color=RED,style="italic")
save(fig,D+'C9_water_treatment.png')

# ---------- Fig: sanitary landfill
fig,ax=plt.subplots(figsize=(6.4,4.2)); ax.set_xlim(0,100); ax.set_ylim(0,68); ax.axis("off")
ax.add_patch(Rectangle((0,0),100,40,fc=SOIL)); ax.add_patch(Rectangle((0,0),100,8,fc=WET)); ax.plot([0,100],[8,8],color=BLUE,ls="--",lw=1.2)
ax.text(99,3.5,"groundwater (water table)",fontsize=7.5,color=BLUE,style="italic",ha="right")
pit=np.array([[18,40],[24,14],[76,14],[82,40]])
ax.add_patch(Polygon(pit,fc="#f1efe8",ec="none"))
ax.add_patch(Polygon([[24.5,14.5],[25.5,18],[74.5,18],[75.5,14.5]],fc="#bbb",ec="none"))
for y0,c in [(18,"#7d6b52"),(23,"#9a8a6a"),(28,"#7d6b52"),(33,"#9a8a6a")]:
    xl=24+(y0-14)*6/26; xr=76-(y0-14)*6/26
    ax.add_patch(Polygon([[xl,y0],[xr,y0],[76-(y0+5-14)*6/26,y0+5],[24+(y0+5-14)*6/26,y0+5]],fc=c,ec="#444",lw=0.5))
ax.add_patch(Polygon([[18.5,38.5],[30,46],[70,46],[81.5,38.5]],fc="#c9b48c",ec="#444"))
ax.add_patch(Polygon([[18.5,38.5],[30,46],[70,46],[81.5,38.5],[81,37.5],[70,44.8],[30,44.8],[19,37.5]],fc="#6b8f5a",ec="none"))
ax.plot(pit[:,0],pit[:,1],color="black",lw=3.2); ax.plot([24,76],[14.8,14.8],color="#2a6f3a",lw=1.5)
ax.plot([26,76],[15.9,15.9],color="#222",lw=2,ls=(0,(1,1)))
ax.add_patch(Rectangle((83,14),3,3,fc="#444")); ax.plot([76,83],[15.9,15.9],color="#222",lw=2); ax.plot([84.5,84.5],[17,34],color="#222",lw=2)
for xx in (42,58): ax.plot([xx,xx],[22,52],color="#d9822b",lw=3)
ax.plot([42,58],[52,52],color="#d9822b",lw=3); ax.plot([50,50],[52,55],color="#d9822b",lw=3)
ax.text(50,56,"flare or generator",fontsize=7.5,ha="center",color=DARK)
ax.add_patch(Polygon([[4,40],[7,37.5],[11,37.5],[14,40]],fc=SKY,ec="#444"))
ax.plot([97,97],[40,5],color="#222",lw=2.2); ax.text(97,42,"monitoring\nwell",fontsize=7,ha="center")
def lab(txt,xy,xt,ha="left"): ax.annotate(txt,xy=xy,xytext=xt,fontsize=7.5,ha=ha,va="center",arrowprops=dict(arrowstyle="-",color="#333",lw=0.8))
lab("Cap: clay or plastic, soil\nand vegetation",(30,45.5),(1,60))
lab("Storm-water ditch\ndiverts runoff",(9,38.3),(1,50))
lab("Composite liner\n(clay + plastic)",(21,27),(1,27))
lab("Gas wells collect methane",(58,40),(66,64))
lab("Compacted waste,\ncovered daily",(66,28),(76,56))
lab("Leachate collection: gravel\nand perforated pipe",(40,15.9),(50,11),ha="center")
lab("pump to\ntreatment",(84.5,27),(87,27))
fig.savefig(D+'C9_landfill.png'); plt.close(fig)
