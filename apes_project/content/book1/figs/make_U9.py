import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
OUT='/home/user/OmniRouter/apes_project/content/book1/figs/'

# Fig 1 greenhouse effect
fig,ax=canvas(6.2,4.2,(0,10),(0,7))
ax.add_patch(Rectangle((0,0),10,0.9,fc=GREEN,ec='none',alpha=.8)); ax.text(5,0.38,"Earth's surface",ha='center',color='white',fontsize=10,fontweight='bold')
ax.add_patch(Rectangle((0,3.4),10,1.9,fc=SKY,ec='none',alpha=.35)); ax.text(9.9,5.05,"Troposphere:\ngreenhouse gases",ha='right',va='top',fontsize=8,color=BLUE)
ax.add_patch(Circle((1.2,6.1),0.6,fc=YELLOW,ec=ORANGE)); ax.text(1.95,6.15,"Sun",fontsize=9,va='center')
arrow(ax,(1.5,5.5),(2.4,1.0),color=ORANGE,lw=2); ax.text(0.1,2.5,"1  Sunlight\n    passes through",fontsize=8,color=ORANGE)
arrow(ax,(4.0,6.6),(3.7,5.3),color=GREY); ax.text(4.15,6.0,"Some reflected\n(clouds, ice)",fontsize=7.5,color=GREY,ha='left')
arrow(ax,(3.0,1.0),(3.0,3.3),color=RED,lw=2); ax.text(3.15,1.7,"2  Surface emits\n    infrared (heat)",fontsize=8,color=RED)
arrow(ax,(5.6,3.5),(5.6,6.8),color=GREY,lw=1.6); ax.text(5.75,6.3,"Escapes to space",fontsize=8,color=GREY)
arrow(ax,(6.7,4.3),(7.4,1.1),color=RED,lw=2,rad=-0.1); ax.text(7.55,2.3,"3  Gases re-radiate IR\n    back toward surface\n    → warmer surface",fontsize=8,color=RED)
ax.text(5,4.3,"CO₂  CH₄  N₂O  H₂O  CFCs",ha='center',fontsize=9,fontweight='bold',color=DARK)
ax.set_title("Greenhouse effect: energy in, infrared trapped")
save(fig,OUT+'U9_greenhouse_effect.png')

# Fig 2 ozone cycle
fig,ax=canvas(6.2,4.0,(0,10),(0,7))
box(ax,0.2,5.6,2.6,0.9,"CFC molecule at\nEarth's surface (inert)",fs=8.5)
box(ax,3.6,5.6,2.8,0.9,"Rises into the\nstratosphere (20–50 km)",fs=8.5)
box(ax,7.2,5.6,2.6,0.9,"UV-C breaks it:\nCl atom released",fs=8.5,fc="#FBE3E5")
arrow(ax,(2.85,6.05),(3.55,6.05)); arrow(ax,(6.45,6.05),(7.15,6.05))
box(ax,0.5,3.1,3.3,1.0,"Cl + O₃ → ClO + O₂\n(ozone destroyed)",fs=9,fc="#FBE3E5")
box(ax,5.5,3.1,3.8,1.0,"ClO + O → Cl + O₂\n(chlorine freed again)",fs=9,fc="#FBE3E5")
arrow(ax,(8.5,5.55),(3.2,4.15),rad=0.0,color=RED); arrow(ax,(3.85,3.6),(5.45,3.6),color=RED); 
arrow(ax,(7.4,3.05),(2.2,3.05+0.0),color=RED,rad=-0.3)
ax.text(5.0,0.95,"One Cl atom repeats this cycle thousands of times\nbefore it is removed from the stratosphere.",ha='center',fontsize=9,fontweight='bold',color=DARK)
ax.text(5.0,0.1,"Net: 2 O₃ → 3 O₂  (UV-absorbing ozone is lost; Cl acts as a catalyst)",ha='center',fontsize=8.5,color=GREY)
ax.set_title("CFC-driven ozone destruction")
save(fig,OUT+'U9_ozone_cfc_cycle.png')

# Fig 3 feedback loops
fig,(a1,a2)=plt.subplots(1,2,figsize=(6.4,3.8))
for a in (a1,a2): a.set_xlim(0,10); a.set_ylim(0,10); a.axis('off')
def cyc(a,labels,color,title,center):
    pts=[(5,8.6),(8.4,5),(5,1.4),(1.6,5)]
    for (x,y),t in zip(pts,labels):
        a.text(x,y,t,ha='center',va='center',fontsize=7.8,bbox=dict(boxstyle='round,pad=0.35',fc=LIGHT,ec=color,lw=1.2))
    pairs=[(0,1),(1,2),(2,3),(3,0)]
    for i,j in pairs:
        p=np.array(pts[i]);q=np.array(pts[j]);d=q-p
        a.add_patch(FancyArrowPatch(p+d*0.3,q-d*0.3,arrowstyle='-|>',mutation_scale=12,color=color,lw=1.6,connectionstyle="arc3,rad=-0.15"))
    a.text(5,5,center,ha='center',va='center',fontsize=8.5,fontweight='bold',color=color)
    a.set_title(title,fontsize=9.5)
cyc(a1,["Air temperature\nrises","Sea ice and snow\nmelt","Darker ocean/land\nexposed (lower albedo)","More sunlight\nabsorbed"],RED,"Positive: ice–albedo","amplifies\nchange")
cyc(a2,["Air temperature\nrises","More evaporation,\nmore low cloud*","More sunlight\nreflected","Surface warming\nslows"],BLUE,"Negative (illustrative)","dampens\nchange")
fig.text(0.5,0.01,"*Cloud feedbacks are uncertain; shown only as an example of a stabilizing loop.",ha='center',fontsize=7,color=GREY)
fig.tight_layout(rect=(0,0.04,1,1))
save(fig,OUT+'U9_feedback_loops.png')

# Fig 4 ocean acidification
fig=plt.figure(figsize=(6.4,3.7))
ax=fig.add_axes([0.0,0.0,0.52,1]); ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,10)
ax.text(5,9.6,"Chemistry in seawater",ha='center',fontweight='bold',fontsize=10)
steps=["CO₂ (air)  →  CO₂ (dissolved)","CO₂ + H₂O  ↔  H₂CO₃","H₂CO₃  ↔  H$^{+}$ + HCO$_3^{-}$","H$^{+}$ + CO$_3^{2-}$  ↔  HCO$_3^{-}$","Less CO$_3^{2-}$ left for\nCaCO₃ shells and skeletons"]
ys=[8.2,6.6,5.0,3.4,1.5]
for t,y in zip(steps,ys):
    box(ax,0.4,y-0.55,9.2,1.1,t,fs=8.5,fc="#FBE3E5" if y==ys[-1] else LIGHT)
for y1,y2 in zip(ys[:-1],ys[1:]): arrow(ax,(5,y1-0.58),(5,y2+0.58))
a=fig.add_axes([0.6,0.2,0.37,0.65])
yrs=np.array([1850,1900,1950,2000,2050]); ph=np.array([8.18,8.16,8.12,8.05,7.95])
a.plot(yrs,ph,color=RED,marker='o',lw=2)
a.set_xlabel("Year"); a.set_ylabel("Surface ocean pH"); a.set_title("Illustrative trend",fontsize=9.5)
a.set_xticks([1850,1950,2050]); a.grid(alpha=.3); a.set_ylim(7.9,8.22)
a.text(1852,7.93,"pH falling =\nmore acidic",fontsize=8,color=DARK)
save(fig,OUT+'U9_ocean_acidification.png')

# Fig 5 HIPPCO
fig,ax=canvas(6.2,4.35,(0,10),(0,7))
ax.set_aspect('equal')
letters=[("H","Habitat loss and\nfragmentation","roads, farms,\nlogging, cities"),
("I","Invasive\nspecies","outcompete or\nprey on natives"),
("P","Population\ngrowth","more land, food\nand resources used"),
("P","Pollution","pesticides, plastics,\nnutrients, oil"),
("C","Climate\nchange","warming, rain shifts,\nsea-level rise"),
("O","Over-\nexploitation","overhunting,\noverfishing, trade")]
cols=[RED,ORANGE,BROWN,GREY,BLUE,GREEN]
for i,((l,t,e),c) in enumerate(zip(letters,cols)):
    r,cn=divmod(i,3); x=0.2+cn*3.3; y=3.7-r*3.4
    ax.add_patch(FancyBboxPatch((x,y),3.0,2.9,boxstyle="round,pad=0.02,rounding_size=0.15",fc='white',ec=c,lw=1.8))
    ax.add_patch(Circle((x+0.65,y+2.1),0.5,fc=c,ec='none')); ax.text(x+0.65,y+2.1,l,ha='center',va='center',color='white',fontsize=15,fontweight='bold')
    ax.text(x+1.3,y+2.1,t,va='center',fontsize=7.8,fontweight='bold')
    ax.text(x+1.5,y+0.8,e,ha='center',va='center',fontsize=7.8,color=GREY,wrap=True)
ax.set_title("HIPPCO: the six drivers of biodiversity loss")
save(fig,OUT+'U9_hippco.png')
