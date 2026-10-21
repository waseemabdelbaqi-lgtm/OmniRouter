import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book2/figs/'
# fire
dec=[1930,1940,1950,1960,1970,1980,1990,2000,2010]
area=[2.1,1.4,0.9,0.6,0.5,0.7,1.2,2.0,2.8]
fuel=[12,14,17,21,25,29,32,35,37]
fig,ax=plt.subplots(figsize=(6.2,3.6))
ax.bar(dec,area,width=7,color=SAND,ec=DARK,label="Area burned (left axis)")
ax.set_xlabel("Decade beginning"); ax.set_ylabel("Mean annual area burned (million ha)")
ax.set_xticks(dec); ax.set_ylim(0,3.5)
ax2=ax.twinx(); ax2.spines['right'].set_visible(True)
ax2.plot(dec,fuel,color=RED,marker='o',lw=2,label="Surface fuel load (right axis)")
ax2.set_ylabel("Mean surface fuel load (t/ha)",color=RED); ax2.set_ylim(0,45)
h1,l1=ax.get_legend_handles_labels();h2,l2=ax2.get_legend_handles_labels()
ax.legend(h1+h2,l1+l2,loc="upper center",fontsize=8,frameon=False,ncol=2,bbox_to_anchor=(0.5,1.12))
save(fig,D+'QBC7_fire.png')
# range
yr=list(range(0,11))
cont=[45,41,36,31,26,22,18,15,13,11,10]
rot=[45,46,47,47,48,48,49,48,49,49,49]
fig,ax=plt.subplots(figsize=(6.2,3.5))
ax.plot(yr,cont,marker='o',color=ORANGE,lw=2,label="Pasture 1")
ax.plot(yr,rot,marker='s',color=BLUE,lw=2,label="Pasture 2")
ax.set_xlabel("Year of study"); ax.set_ylabel("Perennial grass cover (%)"); ax.set_ylim(0,60)
ax.legend(frameon=False,loc="center right")
save(fig,D+'QBC7_range.png')
# ore grade
y=[1950,1965,1980,1995,2010,2020]; g=[1.6,1.3,1.0,0.75,0.5,0.4]
fig,ax=plt.subplots(figsize=(6.2,3.5))
ax.plot(y,g,marker='o',color=RED,lw=2)
ax.set_xlabel("Year"); ax.set_ylabel("Average grade of copper ore mined (% Cu by mass)")
ax.set_ylim(0,2.0); ax.set_xlim(1945,2025); ax.grid(alpha=.3)
ax.set_yticks([0,0.4,0.8,1.2,1.6,2.0])
save(fig,D+'QBC7_grade.png')
