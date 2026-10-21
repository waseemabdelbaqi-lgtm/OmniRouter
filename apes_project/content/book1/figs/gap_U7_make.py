import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book1/figs/'
fig,(a,b)=plt.subplots(1,2,figsize=(6.6,3.2),gridspec_kw={'width_ratios':[1.1,1]})
h=np.linspace(0,24,300)
g=lambda m,s:np.exp(-0.5*((h-m)/s)**2)
no=g(7.5,1.4)+0.15*g(18,1.5)+0.03
no2=0.8*g(9,1.8)+0.4*g(18.5,1.8)+0.15
o3=1.0*g(15,2.7)+0.08
a.plot(h,no,color=ORANGE,lw=2,label="NO"); a.plot(h,no2,color=BROWN,lw=2,label="NO₂"); a.plot(h,o3,color=RED,lw=2.4,label="O₃")
a.set_xticks([0,6,12,18,24]); a.set_yticks([]); a.set_xlabel("Hour of day"); a.set_ylabel("Relative concentration")
a.set_title("A  Order of the peaks",fontsize=9,loc="left")
a.annotate("1st",xy=(7.5,1.03),xytext=(5,1.12),fontsize=8,color=ORANGE,arrowprops=dict(arrowstyle="-",color=ORANGE,lw=.8))
a.annotate("2nd",xy=(9,0.95),xytext=(10.3,1.12),fontsize=8,color=BROWN,arrowprops=dict(arrowstyle="-",color=BROWN,lw=.8))
a.annotate("3rd",xy=(15,1.08),xytext=(16.5,1.2),fontsize=8,color=RED,arrowprops=dict(arrowstyle="-",color=RED,lw=.8))
a.set_ylim(0,1.35); a.legend(fontsize=8,frameon=False,loc="upper right",bbox_to_anchor=(1.0,0.82))
sites=["Busy\nhighway","City\ncenter","Suburb\ndownwind","Rural\ndownwind"]
NO=[10,6,2,0.5]; O3=[1.5,3,7,9]
x=np.arange(4); w=0.38
b.bar(x-w/2,NO,w,color=ORANGE,label="NO"); b.bar(x+w/2,O3,w,color=RED,label="O₃")
b.set_xticks(x); b.set_xticklabels(sites,fontsize=7.5); b.set_yticks([]); b.set_ylabel("Relative concentration, 3 p.m.")
b.set_title("B  Same afternoon, different places",fontsize=9,loc="left")
b.legend(fontsize=8,frameon=False,loc="upper left",bbox_to_anchor=(0.30,0.80),ncol=2)
b.annotate("",xy=(3.3,10.4),xytext=(0.2,10.4),arrowprops=dict(arrowstyle="-|>",color=GREY,lw=1.2))
b.text(1.75,10.9,"wind carries the air mass →",ha="center",fontsize=7.5,color=GREY)
b.set_ylim(0,13.5)
b.set_ylabel("Relative concentration, 3 p.m.",fontsize=9)
fig.tight_layout(); save(fig,D+'U7_gap_NO_O3.png')
