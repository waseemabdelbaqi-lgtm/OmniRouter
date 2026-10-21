import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
OUT='/home/user/OmniRouter/apes_project/content/book2/figs/'
t=np.arange(0,16.1,0.5)
c=40+460*np.exp(-t/1.6)
fig,ax=plt.subplots(figsize=(5.8,3.3))
ax.plot(t,c,color=RED,lw=2); ax.axhline(5,color=BLUE,ls="--",lw=1.3)
ax.text(15.8,12,"Drinking-water standard (5 µg/L)",ha="right",fontsize=8.5,color=BLUE)
ax.set_xlabel("Years since pump-and-treat began"); ax.set_ylabel("Solvent concentration in\nmonitoring well (µg/L)")
ax.set_xlim(0,16); ax.set_ylim(0,520)
save(fig,OUT+'QBC10_tailing.png')
