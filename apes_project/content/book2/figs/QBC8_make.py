import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
D='/home/user/OmniRouter/apes_project/content/book2/figs/'
lab=["Single-occupant\ncar","Carpool\n(4 occupants)","Bus\n(average load)","Light rail\n(average load)"]
v=[190,48,70,50]
fig,ax=plt.subplots(figsize=(6.2,3.5))
b=ax.bar(lab,v,color=[ORANGE,TEAL,BLUE,GREEN],ec=DARK)
for r,x in zip(b,v): ax.text(r.get_x()+r.get_width()/2,x+4,str(x),ha="center",fontsize=9)
ax.set_ylabel("CO₂ emitted per passenger-km (g)"); ax.set_ylim(0,220)
save(fig,D+'QBC8_modes.png')
