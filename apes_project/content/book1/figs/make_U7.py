import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book1/figs/'

# ---- Fig 1: inversion vs normal
fig,axs=plt.subplots(1,2,figsize=(6.4,3.6))
alt=np.linspace(0,1.5,50)
for ax,title,prof,trap in [(axs[0],"Normal conditions",lambda a:20-9*a,False),(axs[1],"Thermal inversion",lambda a:np.where(a<0.5,8+ 14*a*1.0,15-3*(a-0.5)),True)]:
    ax.plot(prof(alt),alt,color=RED,lw=2.4)
    ax.set_xlim(0,24); ax.set_ylim(0,1.5)
    ax.set_xlabel("Air temperature (°C)"); ax.set_title(title)
    ax.set_yticks([0,0.5,1.0,1.5]);
axs[0].set_ylabel("Altitude above ground (km)")
axs[0].annotate("",xy=(4,1.3),xytext=(4,0.2),arrowprops=dict(arrowstyle="-|>",color=GREEN,lw=2))
axs[0].text(5,0.75,"Warm surface air\nrises and carries\npollutants upward",fontsize=8,color=GREEN,va="center")
axs[0].text(12,1.38,"Cooler air aloft",fontsize=8,color=GREY)
# inversion
axs[1].axhspan(0.5,0.52,color=BLUE,alpha=0.6)
axs[1].text(23.5,0.56,"inversion layer\n(warm air lid)",fontsize=8,color=BLUE,ha="right",va="bottom")
axs[1].axhspan(0,0.5,color="#8d8576",alpha=0.35)
axs[1].text(0.4,0.1,"Smog and particulates\ntrapped near ground",fontsize=8,color=DARK,va="center")
axs[1].text(2,0.62,"Cool surface air is\nheavier than the\nwarmer air above it",fontsize=8,color=GREY,va="bottom")
for x in (3,6,9): axs[1].annotate("",xy=(x,0.46),xytext=(x,0.25),arrowprops=dict(arrowstyle="-|>",color=GREY,lw=1)); 
fig.tight_layout(); save(fig,D+'U7_inversion.png')

# ---- Fig 2: smog formation (flow + daily curve)
fig=plt.figure(figsize=(6.4,3.9))
ax=fig.add_axes([0,0,0.5,1]); ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis("off")
box(ax,0.04,0.80,0.92,0.14,"Fossil-fuel combustion\n(vehicles, power plants)",fs=8.5,bold=True)
box(ax,0.04,0.56,0.40,0.14,"NO and NO₂\n(NOₓ)",fc="#F6E3C7",ec=ORANGE,fs=8.5)
box(ax,0.56,0.56,0.40,0.14,"VOCs\n(fuel vapor, solvents)",fc="#DDEBD9",ec=GREEN,fs=8.5)
box(ax,0.15,0.33,0.70,0.12,"Sunlight + heat\n(+ O₂)",fc="#FFF3B8",ec=YELLOW,fs=8.5)
box(ax,0.04,0.04,0.92,0.2,"Photochemical smog (secondary\npollutants): ground-level ozone O₃,\nPAN, aldehydes, fine particulates",fc="#E6D9D9",ec=RED,fs=8.5,bold=True)
arrow(ax,(0.5,0.80),(0.24,0.71)); arrow(ax,(0.5,0.80),(0.76,0.71))
arrow(ax,(0.24,0.56),(0.38,0.46)); arrow(ax,(0.76,0.56),(0.62,0.46)); arrow(ax,(0.5,0.33),(0.5,0.25))
ax.text(0.02,0.99,"A  Formation pathway",fontsize=9,fontweight="bold",va="top",color=RED)
ax2=fig.add_axes([0.58,0.2,0.4,0.68])
h=np.linspace(0,24,200)
g=lambda m,s:np.exp(-0.5*((h-m)/s)**2)
nox=g(7.5,1.5)+0.7*g(18,1.8)+0.1
vocs=0.9*g(8,1.8)+0.6*g(18,2)+0.1
o3=1.2*g(15,2.6)
ax2.plot(h,nox/1.2,color=ORANGE,lw=2,label="NOₓ"); ax2.plot(h,vocs/1.2,color=GREEN,lw=2,label="VOCs"); ax2.plot(h,o3/1.2,color=RED,lw=2.4,label="Ozone")
ax2.set_xticks([0,6,12,18,24]); ax2.set_xlabel("Hour of day"); ax2.set_ylabel("Relative concentration")
ax2.set_yticks([]); ax2.legend(fontsize=8,frameon=False,loc="upper left")
ax2.set_title("B  Typical summer day (schematic)",fontsize=9,loc="left")
fig.savefig(D+'U7_smog.png'); plt.close(fig)

# ---- Fig 3: pH scale
fig,ax=plt.subplots(figsize=(6.4,3.3)); ax.set_xlim(-0.2,14.7); ax.set_ylim(-3.2,3.2); ax.axis("off")
import matplotlib.cm as cm
cols=["#c1272d","#d6452a","#e8692b","#f0932c","#f4b92f","#e6d83a","#a8cf45","#4fae5b","#2f9c88","#2f80a3","#2f63a8","#3d4fa3","#4d3d9a","#5a2e8a","#6b2780"]
for i in range(15):
    ax.add_patch(Rectangle((i-0.5,-0.4),1,0.8,fc=cols[i],ec="white",lw=1))
    ax.text(i,0,str(i),ha="center",va="center",color="white",fontsize=10,fontweight="bold")
ax.text(2.4,-0.75,"ACIDIC",ha="center",fontsize=10,fontweight="bold",color=RED)
ax.text(12,-0.75,"BASIC",ha="center",fontsize=10,fontweight="bold",color=BLUE)
up=[(0.5,"Battery acid",0.6*0+1.7),(2.0,"Lemon juice",2.6),(2.9,"Vinegar",1.4),(4.2,"Acid rain\n(typical 4.2–4.4)",2.4),(5.6,"Normal rain\n(≈ 5.6)",1.3),]
for x,t,y in [(0.5,"Battery acid",1.5),(2.0,"Lemon juice",2.6),(3.0,"Vinegar",1.5),(4.3,"Acid rain\n(≈ 4.2–4.4)",2.6),(5.6,"Normal rain\n(≈ 5.6)",1.5)]:
    ax.plot([x,x],[0.4,y-0.15],color=GREY,lw=0.8); ax.text(x,y,t,ha="center",va="bottom",fontsize=7.5)
for x,t,y in [(7,"Pure water",-1.4),(8.1,"Seawater\n(≈ 8.1)",-2.5),(9,"Baking soda\nsolution",-1.4),(11,"Household\nammonia",-2.5),(13,"Drain\ncleaner",-1.4)]:
    ax.plot([x,x],[-0.4,y+0.1],color=GREY,lw=0.8); ax.text(x,y,t,ha="center",va="top",fontsize=7.5)
ax.annotate("",xy=(0,-3.0),xytext=(3.2,-3.0),arrowprops=dict(arrowstyle="-|>",color=RED,lw=1.5))
ax.text(0,-3.2,"each step to the left = 10× more H+",fontsize=8,color=RED,va="top")
fig.savefig(D+'U7_pH.png'); plt.close(fig)

# ---- Fig 4: acid deposition pathway
fig,ax=canvas(6.4,3.5)
ax.add_patch(Rectangle((0,0),1,0.2,fc="#C9B79A",ec="none")); 
ax.add_patch(Polygon([[0.58,0.2],[0.72,0.2],[0.8,0.0],[0.52,0.0]],fc="#8fbad3",ec="none"))
ax.add_patch(Rectangle((0.52,0.2),0.28,0.02,fc="#8fbad3",ec="none"))
ax.text(0.66,0.09,"Lake",ha="center",fontsize=9,color=DARK)
ax.add_patch(Rectangle((0.06,0.38),0.07,0.18,fc="#7d7d7d",ec="none")); ax.add_patch(Rectangle((0.15,0.38),0.07,0.26,fc="#7d7d7d",ec="none"))
ax.text(0.14,0.28,"Power plant,\nvehicles",ha="center",fontsize=8,color=DARK)
ax.annotate("",xy=(0.26,0.72),xytext=(0.19,0.66),arrowprops=dict(arrowstyle="-|>",color=GREY,lw=2))
box(ax,0.02,0.86,0.28,0.1,"Step 1: SO₂ and NOₓ emitted",fs=8)
box(ax,0.36,0.86,0.30,0.1,"Step 2: Oxidized in air + water\n→ H₂SO₄, HNO₃",fs=8,fc="#F6E3C7",ec=ORANGE)
ax.add_patch(Ellipse((0.4,0.7),0.26,0.13,fc="#d8dde2",ec=GREY)); 
ax.text(0.4,0.7,"carried by wind",ha="center",va="center",fontsize=8)
box(ax,0.70,0.86,0.28,0.1,"Step 3: Wet or dry\ndeposition downwind",fs=8,fc="#DDEBD9",ec=GREEN)
arrow(ax,(0.3,0.91),(0.36,0.91)); arrow(ax,(0.66,0.91),(0.70,0.91))
for x in (0.62,0.68,0.74,0.80,0.86):
    ax.annotate("",xy=(x-0.03,0.40),xytext=(x,0.6),arrowprops=dict(arrowstyle="-|>",color=BLUE,lw=1.2))
ax.add_patch(Ellipse((0.74,0.65),0.3,0.1,fc="#d8dde2",ec=GREY))
ax.text(0.74,0.65,"acid rain, snow, fog",ha="center",va="center",fontsize=7.5)
for x in (0.88,0.93): ax.add_patch(Polygon([[x-0.02,0.2],[x+0.02,0.2],[x,0.36]],fc="#6b4a2f",ec="none"))
ax.text(0.9,0.4,"damaged\nforest",ha="center",fontsize=7.5,color=BROWN)
ax.text(0.02,0.1,"Step 4: Soil and lake acidification;\ncorrosion of stone and metal",fontsize=8,va="center",color=RED,fontweight="bold")
ax.text(0.66,0.28,"pH ↓",fontsize=8,color=BLUE,ha="center")
save(fig,D+'U7_acid.png')
