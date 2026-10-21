import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
D='/home/user/OmniRouter/apes_project/content/book2/figs/'
names=['Fossil fuel\ncombustion','Ocean\n(dimethyl sulfide)','Metal ore\nsmelting','Volcanoes','Soils and\nvegetation']
vals=[60,20,10,8,2]; col=[RED,GREEN,RED,GREEN,GREEN]
fig,ax=plt.subplots(figsize=(6,3.5))
b=ax.bar(names,vals,color=col,edgecolor='#333',lw=0.6)
for r,v in zip(b,vals): ax.text(r.get_x()+r.get_width()/2,v+1.2,str(v),ha='center',fontsize=9)
ax.set_ylabel('Sulfur emitted to the atmosphere\n(Tg S per year)'); ax.set_ylim(0,70)
ax.tick_params(axis='x',labelsize=8)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(fc=GREEN,ec='#333',label='Natural source'),Patch(fc=RED,ec='#333',label='Human activity')],frameon=False,loc='upper right')
save(fig,D+'QBC5_sulfur_sources.png')
