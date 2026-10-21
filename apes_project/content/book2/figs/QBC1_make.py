import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
OUT='/home/user/OmniRouter/apes_project/content/book2/figs/'

# 1. Eons bar
fig,ax=plt.subplots(figsize=(6.2,2.2))
segs=[(4.6,4.0,"#C9B8A6","Eon 1"),(4.0,2.5,"#9CC5E3","Eon 2"),(2.5,0.54,"#8FB996","Eon 3"),(0.54,0.0,"#D9822B","Eon 4")]
for a,b,c,l in segs:
    ax.barh(0,a-b,left=b,height=0.5,color=c,edgecolor="#333",lw=1)
    if a-b>1: ax.text((a+b)/2,0,l,ha="center",va="center",fontsize=10,fontweight="bold")
ax.text(4.3,0,"Eon 1",ha="center",va="center",fontsize=8,fontweight="bold")
ax.annotate("Eon 4",xy=(0.27,0.27),xytext=(0.9,0.75),ha="center",fontsize=10,fontweight="bold",arrowprops=dict(arrowstyle="-|>",color=DARK))
ax.set_xlim(4.8,-0.1); ax.set_ylim(-0.5,1.0); ax.set_yticks([])
ax.set_xticks([4.6,4.0,3.0,2.5,2.0,1.0,0.54,0]); ax.set_xticklabels(["4.6","4.0","3.0","2.5","2.0","1.0","0.54","0"],fontsize=9)
ax.spines["left"].set_visible(False)
ax.set_xlabel("Time before present (billions of years)")
ax.set_title("Eons of Earth history (not named)")
save(fig,OUT+'QBC1_eons.png')

# 2. Layers
fig,ax=plt.subplots(figsize=(6.2,3.4))
ax.set_aspect('equal'); ax.axis('off')
R=[6371,6340,3480,1220]
cols=["#8B5E3C","#D9822B","#E8C547","#C0392B"]
rad=[6371,6000,3480,1220]  # crust drawn thicker for visibility
for r,c in zip(rad,cols):
    ax.add_patch(Circle((0,0),r,fc=c,ec="#333",lw=1))
for lab,r in zip("XYZ",[4740,2350,0]):
    ax.text(0,-r if lab!="Z" else 0,lab,ha="center",va="center",fontsize=16,fontweight="bold",color="white" if lab=="Z" else "black")
ax.annotate("W",xy=(-4500,-4500),xytext=(-6300,-6200),fontsize=16,fontweight="bold",ha="center",arrowprops=dict(arrowstyle="-|>",color=DARK))
ax.set_xlim(-7000,13500); ax.set_ylim(-6800,6800)
ax.text(7300,5200,"Layer data",fontsize=10,fontweight="bold")
rows=["W: 5–70 km thick; solid rock","X: about 2,900 km thick; solid rock","Y: about 2,300 km thick; Fe–Ni alloy","Z: radius about 1,200 km; Fe–Ni alloy","Temperature rises with depth in all layers","(W drawn thicker than scale)"]
for i,t in enumerate(rows): ax.text(7300,3900-i*1300,t,fontsize=8.5)
save(fig,OUT+'QBC1_layers.png')

# 3. Seismogram
rng=np.random.default_rng(4)
t=np.linspace(0,90,1800); y=rng.normal(0,0.04,t.size)
def burst(t0,amp,f,decay):
    m=t>=t0; return np.where(m,amp*np.exp(-(t-t0)/decay)*np.sin(2*np.pi*f*(t-t0)),0)
y+=burst(12,0.35,0.9,12)+burst(52,0.9,0.5,18)+0.05*np.exp(-(t-12)/40)*(t>12)*np.sin(2*np.pi*0.6*t)
fig,ax=plt.subplots(figsize=(6.2,2.6))
ax.plot(t,y,color="black",lw=0.7)
ax.set_xlim(0,90); ax.set_ylim(-1.3,1.5)
ax.set_xticks(range(0,91,10)); ax.set_yticks([])
ax.spines["left"].set_visible(False)
for x,l in[(12,"P wave arrives\nt = 12 s"),(52,"S wave arrives\nt = 52 s")]:
    ax.annotate(l,xy=(x,0),xytext=(x,1.15),ha="center",fontsize=9,arrowprops=dict(arrowstyle="-|>",color=RED))
ax.set_xlabel("Time after recording began (s)"); ax.set_title("Seismogram recorded at one station")
save(fig,OUT+'QBC1_seismogram.png')

# 4. Rock cycle
fig,ax=canvas(6.2,3.8)
B={'mag':(0.02,0.38,0.2,0.16,"Magma"),'ign':(0.22,0.78,0.22,0.16,"Igneous\nrock"),'sed':(0.62,0.78,0.22,0.16,"Sediment"),'sr':(0.76,0.40,0.22,0.16,"Sedimentary\nrock"),'met':(0.38,0.04,0.22,0.16,"Metamorphic\nrock")}
for k,(x,y,w,h,t) in B.items(): box(ax,x,y,w,h,t,fs=9.5,bold=True)
def c(k,dx=0,dy=0):
    x,y,w,h,_=B[k]; return (x+w/2+dx,y+h/2+dy)
arrows=[("mag","ign",(0.10,0.56),(0.26,0.77),"1"),("ign","sed",(0.44,0.86),(0.62,0.86),"2"),("sed","sr",(0.80,0.78),(0.86,0.57),"3"),("sr","met",(0.80,0.40),(0.60,0.14),"4"),("met","mag",(0.38,0.12),(0.14,0.37),"5"),("ign","met",(0.32,0.78),(0.46,0.21),"6")]
for _,_,p,q,n in arrows:
    arrow(ax,p,q,color=DARK,lw=1.6)
    mx,my=(p[0]+q[0])/2,(p[1]+q[1])/2
    ax.add_patch(Circle((mx,my),0.035,fc="white",ec=RED,lw=1.4,zorder=5))
    ax.text(mx,my,n,ha="center",va="center",fontsize=10,fontweight="bold",color=RED,zorder=6)
save(fig,OUT+'QBC1_rockcycle.png')

# 5. Subduction FRQ
dist=np.array([40,80,120,160,200,240,280]); dep=np.array([12,38,61,88,110,136,160])
rng=np.random.default_rng(11)
xs=rng.uniform(20,290,70); ys=0.6*xs-8+rng.normal(0,9,70); ys=np.clip(ys,1,None)
fig,ax=plt.subplots(figsize=(6.2,3.8))
ax.fill_between([-60,0],[0,0],[-3,-3],color=BLUE,alpha=0.0)
ax.axhline(0,color="#444",lw=1)
ax.scatter(xs,ys,s=14,color=GREY,alpha=0.7,label="Earthquake foci")
ax.scatter(dist,dep,s=34,color=RED,zorder=4,label="Selected foci (table)")
ax.scatter([190,200,212],[-6,-6,-6],marker="^",s=90,color=ORANGE,edgecolor="#333",zorder=5,label="Volcanoes")
ax.plot([0],[0],marker="v",color=BLUE,ms=9)
ax.text(14,-22,"Trench",fontsize=9,color=BLUE,ha="center")
ax.set_xlim(-10,310); ax.set_ylim(190,-30)
ax.set_xlabel("Distance inland from trench (km)"); ax.set_ylabel("Depth below surface (km)")
ax.set_title("Earthquake foci and volcanoes along a coastal transect")
ax.legend(loc="lower left",fontsize=8,frameon=False)
save(fig,OUT+'QBC1_subduction.png')
