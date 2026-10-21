import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
OUT='/home/user/OmniRouter/apes_project/content/book2/figs/'
d=[0,1,2,3,4,5,6]; w=[55,85,130,190,215,110,60]; p=[1006,998,982,955,946,985,1003]
fig,ax=plt.subplots(figsize=(6.2,3.4))
ax.plot(d,w,"o-",color=RED,lw=2,label="Maximum sustained wind (km/h)")
ax.set_xlabel("Day of storm"); ax.set_ylabel("Maximum sustained wind (km/h)",color=RED); ax.set_ylim(0,260)
ax2=ax.twinx(); ax2.spines["right"].set_visible(True)
ax2.plot(d,p,"s--",color=BLUE,lw=2); ax2.set_ylabel("Central pressure (hPa)",color=BLUE); ax2.set_ylim(1020,930)
ax.axvline(4.0,color=GREY,ls=":"); ax.text(4.05,15,"Center crosses\ncoastline",fontsize=8.5,color=GREY)
ax.set_title("Hurricane Mira: wind and pressure")
ax.set_xticks(d)
save(fig,OUT+'QBC2_hurricane.png')
