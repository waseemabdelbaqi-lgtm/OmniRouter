import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
OUT='/home/user/OmniRouter/apes_project/content/book2/figs/'
names=["LED lighting","Building insulation","Onshore wind","Reforestation","Utility-scale solar","Coal plant with\ncarbon capture","Direct air capture"]
cost=[-80,-40,10,20,30,90,400]
fig,ax=plt.subplots(figsize=(6.0,3.5))
cols=[GREEN if v<0 else RED for v in cost]
ax.barh(names[::-1],cost[::-1],color=cols[::-1])
ax.axvline(0,color="black",lw=1)
for i,v in enumerate(cost[::-1]): ax.text(v+(8 if v>=0 else -8),i,f"{v:+d}",va="center",ha="left" if v>=0 else "right",fontsize=8.5)
ax.set_xlim(-130,470)
ax.set_xlabel("Net cost per tonne of CO₂ avoided (US$/t; negative = net savings)")
save(fig,OUT+'QBC11_abatement.png')
