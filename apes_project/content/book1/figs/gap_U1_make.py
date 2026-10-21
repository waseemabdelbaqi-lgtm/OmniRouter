import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
OUT='/home/user/OmniRouter/apes_project/content/book1/figs/'
M=list("JFMAMJJASOND")

def clim():
    D=[("A  Hot, wet, no dry season",[270,260,300,280,250,200,190,170,200,240,280,290],[26,26,27,27,26,26,25,26,26,27,27,26],"#1F7A3A"),
       ("B  Warm, long dry season",[5,5,20,60,130,180,190,170,110,40,10,5],[24,25,27,28,27,25,24,24,25,26,25,24],"#D9A441"),
       ("C  Mild, wet winter, dry summer",[100,95,80,40,15,3,1,2,10,40,70,95],[11,12,13,15,18,21,24,24,22,18,14,11],"#B88A5A"),
       ("D  Cold winter, rain peaks in summer",[15,15,30,50,80,90,70,60,45,30,20,15],[-8,-6,0,8,14,19,22,20,15,8,0,-6],"#C9C46A")]
    fig,axs=plt.subplots(2,2,figsize=(6.3,4.4),sharex=True)
    for ax,(t,p,T,c) in zip(axs.flat,D):
        ax.bar(range(12),p,color=SKY,ec="#5A8FB5",lw=0.5)
        ax.set_ylim(0,320); ax.set_xticks(range(12)); ax.set_xticklabels(M,fontsize=7.5)
        ax.tick_params(axis="y",labelsize=7.5); ax.set_title(t,fontsize=8.5,loc="left",color="black")
        ax.spines["right"].set_visible(True)
        a2=ax.twinx(); a2.plot(range(12),T,color=RED,lw=1.8,marker="o",ms=2.5)
        a2.set_ylim(-10,40); a2.tick_params(axis="y",labelsize=7.5,colors=RED); a2.spines["right"].set_color(RED); a2.spines["top"].set_visible(False)
    for ax in axs[:,0]: ax.set_ylabel("Precipitation (mm/month)",fontsize=8)
    for a in fig.axes[1::2][1::2]: pass
    fig.text(0.995,0.5,"Mean temperature (°C)",rotation=270,va="center",color=RED,fontsize=8.5)
    fig.text(0.5,-0.01,"Blue bars = precipitation (left axis); red line = temperature (right axis). Same scales in every panel.",ha="center",fontsize=8,color=GREY)
    fig.tight_layout(rect=(0,0.02,0.98,1))
    save(fig,OUT+'U1_gap_climatographs.png')

def keeling():
    m=np.arange(0,48)
    trend=410+0.20*m
    seas=3.0*np.cos(2*np.pi*(m-4)/12)   # peak ~May (m=4), min ~Sep-Oct
    y=trend+seas
    fig,ax=plt.subplots(figsize=(6.2,2.9))
    ax.plot(m,y,color=RED,lw=1.8,label="Monthly CO₂ (zigzag)")
    ax.plot(m,trend,color=GREY,ls="--",lw=1.3,label="Long-term trend")
    ax.set_xticks([0,12,24,36,47]); ax.set_xticklabels(["Jan, Yr 1","Jan, Yr 2","Jan, Yr 3","Jan, Yr 4","Dec, Yr 4"],fontsize=8)
    ax.set_ylabel("Atmospheric CO₂ (ppm)"); ax.set_ylim(401,426)
    ax.annotate("Late spring peak:\nrespiration and decay\nhave built up CO₂",xy=(16,y[16]),xytext=(5,421),fontsize=8,arrowprops=dict(arrowstyle="-|>",color=DARK))
    ax.annotate("Autumn low: summer\nphotosynthesis removed\nmore than respiration added",xy=(22,y[22]-0.2),xytext=(26,403.0),fontsize=8,arrowprops=dict(arrowstyle="-|>",color=DARK))
    ax.text(41,422.5,"Rising baseline:\nfossil fuel burning",fontsize=8,color=GREY,ha="center",rotation=0)
    ax.legend(fontsize=8,frameon=False,loc="lower left")
    ax.grid(alpha=0.25)
    save(fig,OUT+'U1_gap_co2_seasonal.png')
clim(); keeling()
