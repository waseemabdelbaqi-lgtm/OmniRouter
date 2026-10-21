import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
OUT='/home/user/OmniRouter/apes_project/content/book2/figs/'
# Fig 1: landfill plan view with wells
fig,ax=canvas(6.2,3.3,(0,10),(0,5.4))
ax.add_patch(Rectangle((3.2,1.9),2.0,1.6,fc="#D9CBB0",ec=DARK,lw=1.3)); ax.text(4.2,2.7,"Unlined\nlandfill",ha="center",va="center",fontsize=9,fontweight="bold")
wells=[(1.4,2.7,"Well A","12 mg/L"),(6.1,2.7,"Well B","180 mg/L"),(8.4,2.7,"Well C","95 mg/L"),(4.2,4.5,"Well D","14 mg/L")]
for x,y,n,c in wells:
    ax.add_patch(Circle((x,y),0.12,fc=RED,ec="black",zorder=3))
    dy=-0.5 if n!="Well D" else 0.3
    ax.text(x,y+(-0.3 if n!="Well D" else 0.25),"",fontsize=8)
    ax.text(x,y-0.28 if n!="Well D" else y+0.22,f"{n}\n{c}" if n!="Well D" else f"{n}: {c}",ha="center",va="top" if n!="Well D" else "bottom",fontsize=8.5)
arrow(ax,(0.4,0.8),(2.6,0.8),color=BLUE,lw=2); ax.text(1.5,0.95,"Groundwater flow",ha="center",fontsize=8.5,color=BLUE)
# scale bar
ax.plot([6.5,8.5],[0.8,0.8],color="black",lw=2); ax.text(7.5,0.55,"100 m",ha="center",fontsize=8)
ax.text(5,5.25,"Plan view, chloride in monitoring wells (regional background 10–15 mg/L)",ha="center",fontsize=9)
ax.annotate("",xy=(9.7,4.5),xytext=(9.7,3.7),arrowprops=dict(arrowstyle="-|>",color="black")); ax.text(9.7,3.55,"N",ha="center",va="top",fontsize=9,fontweight="bold")
save(fig,OUT+'QBC9_plume.png')
# Fig 2: stream map for FRQ
fig,ax=canvas(6.4,3.0,(0,10),(0,4.6))
import numpy as np
xs=np.linspace(0,10,200); ys=2.2+0.25*np.sin(xs*1.1)
ax.plot(xs,ys,color=BLUE,lw=7,solid_capstyle="round",alpha=.85); 
ax.add_patch(Rectangle((1.8,3.0),2.6,1.1,fc="#E7D98B",ec=BROWN,lw=1.2)); ax.text(3.1,3.55,"Cornfield\n(fertilized)",ha="center",va="center",fontsize=8.5)
ax.add_patch(Rectangle((4.6,0.7),1.6,1.0,fc="#D8D8D8",ec=GREY,lw=1.2)); ax.text(5.4,1.2,"Town",ha="center",va="center",fontsize=8.5)
ax.annotate("Wastewater plant\noutfall",xy=(7.6,2.2+0.25*np.sin(7.6*1.1)),xytext=(8.4,0.9),fontsize=8.5,ha="center",arrowprops=dict(arrowstyle="-|>",color=RED))
ax.annotate("Dead fish and\nalgal mats observed",xy=(9.3,2.2+0.25*np.sin(9.3*1.1)),xytext=(9.0,3.6),fontsize=8.5,ha="center",color=RED,arrowprops=dict(arrowstyle="-|>",color=RED))
ax.annotate("Forested\nheadwaters",xy=(0.5,2.2+0.25*np.sin(.55)),xytext=(0.7,3.6),fontsize=8.5,ha="center",arrowprops=dict(arrowstyle="-|>",color=GREEN))
arrow(ax,(0.3,0.45),(2.3,0.45),color=BLUE,lw=2); ax.text(1.3,0.6,"Stream flow",ha="center",fontsize=8.5,color=BLUE)
ax.plot([0,10],[0.1,0.1],color="black",lw=1); 
for km in range(0,5): ax.plot([km*2.5]*2,[0.05,0.15],color="black",lw=1); ax.text(km*2.5,-0.05,f"{km*1.5:.1f} km" if False else f"{km*2.0:.0f} km",ha="center",va="top",fontsize=7.5)
save(fig,OUT+'QBC9_stream.png')
