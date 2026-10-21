import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book1/figs/'

# Catch, effort and catch per unit effort (invented data)
yr=np.arange(1980,2025,5)
eff=np.array([20,35,50,65,80,90,95,100,105])      # thousand boat-days
catch=np.array([40,70,95,110,100,85,70,60,55])    # thousand tonnes
cpue=catch/eff
fig,(a,b)=plt.subplots(2,1,figsize=(6.2,4.6),sharex=True,gridspec_kw={'height_ratios':[1.15,1]})
a.bar(yr,catch,width=3.4,color=SKY,edgecolor=BLUE,label='Total catch (thousand tonnes)')
a.set_ylabel('Total catch\n(thousand tonnes)'); a.set_ylim(0,135)
a2=a.twinx(); a2.spines['right'].set_visible(True)
a2.plot(yr,eff,color=RED,lw=2.2,marker='o',ms=4,label='Fishing effort (thousand boat-days)')
a2.set_ylabel('Effort\n(thousand boat-days)',color=RED); a2.set_ylim(0,135); a2.tick_params(axis='y',colors=RED)
a.set_title('Catch, effort and catch per unit effort (invented data)',loc='left')
h1,l1=a.get_legend_handles_labels(); h2,l2=a2.get_legend_handles_labels()
a.legend(h1+h2,l1+l2,loc='upper left',frameon=False,fontsize=8)
b.plot(yr,cpue,color=GREEN,lw=2.4,marker='o',ms=4)
b.set_ylim(0,2.4); b.set_ylabel('Catch per unit effort\n(tonnes per boat-day)'); b.set_xlabel('Year')
b.annotate('Effort still rising, catch per boat-day falling:\nthe stock is being depleted',(2005,0.94),(1982,0.35),fontsize=8.5,arrowprops=dict(arrowstyle='->',color=GREY))
b.set_xticks(yr)
save(fig,D+'U5_gap_cpue.png')
