import sys, os
sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D=os.path.dirname(os.path.abspath(__file__))

# 1 eutrophication cascade
fig,ax=canvas(6.2,3.9,xlim=(-0.02,1.02))
W=0.26
steps=[("Fertilizer, manure,\ndetergent, sewage\n(N and P runoff)",0.0,0.68,SAND),
       ("Nutrient\nenrichment\nof water",0.37,0.68,LIGHT),
       ("Algal bloom;\nsunlight blocked\nat surface",0.74,0.68,"#CFE8C9"),
       ("Plants and algae\ndie, sink",0.74,0.36,"#E6DCC3"),
       ("Bacteria decompose\nthem and use up\ndissolved O\u2082",0.37,0.36,"#E6DCC3"),
       ("Hypoxia: fish and\nother aerobic life\ndie or flee",0.0,0.36,"#F2C9C9")]
for t,x,y,c in steps: box(ax,x,y,W,0.22,t,fc=c,fs=8.5)
arrow(ax,(0.28,0.79),(0.36,0.79)); arrow(ax,(0.65,0.79),(0.73,0.79))
arrow(ax,(0.87,0.67),(0.87,0.59)); arrow(ax,(0.73,0.47),(0.65,0.47)); arrow(ax,(0.36,0.47),(0.28,0.47))
box(ax,0.0,0.03,1.0,0.19,"Result: a eutrophic, oxygen-poor system (a dead zone when severe).\nAn oligotrophic lake is the opposite: few nutrients, clear water, high O\u2082.",fc="white",fs=8.5)
arrow(ax,(0.13,0.35),(0.13,0.23))
ax.set_title("Eutrophication cascade",loc="left")
save(fig,D+"/U8_eutrophication.png")

# 2 oxygen sag
x=np.linspace(0,100,400)
sat=9.0
def do(x):
    # Streeter-Phelps-like sag
    k1,k2,L0,D0=0.12,0.25,9,0.2
    k1*=0.1;k2*=0.1
    d=(k1*L0/(k2-k1))*(np.exp(-k1*x)-np.exp(-k2*x))+D0*np.exp(-k2*x)
    return d
deficit=np.where(x<10,0,do(np.maximum(x-10,0))*1.0)
d0=do(np.maximum(x-10,0))
dd=np.where(x<10,0,d0)
dd=dd*(7.2/dd.max())
oxy=sat-dd
fig,ax=plt.subplots(figsize=(6.2,3.6))
ax.plot(x,oxy,color=RED,lw=2.4,label="Dissolved oxygen (DO)")
ax.axhline(sat,color=BLUE,ls="--",lw=1,label="Saturation DO (clean water)")
ax.axhline(5,color=GREY,ls=":",lw=1)
ax.text(99,5.15,"≈5 mg/L: stress threshold for many fish",ha="right",fontsize=8,color=GREY)
ax.axvline(10,color="k",lw=1); ax.text(10.8,0.5,"Pollution\ndischarge",fontsize=8)
imin=np.argmin(oxy)
ax.plot(x[imin],oxy[imin],"o",color=DARK); ax.annotate("Lowest DO\n(the sag)",(x[imin],oxy[imin]),(x[imin]+2,3.6),arrowprops=dict(arrowstyle="->"),fontsize=8.5)
ax.text(3,9.4,"Clean\nzone",fontsize=8,ha="left")
ax.text(22,7.9,"Decomposition\n(DO falls)",fontsize=8,ha="center")
ax.text(80,7.0,"Recovery\n(re-aeration,\ndilution)",fontsize=8,ha="center")
ax.set_ylim(0,10.8); ax.set_xlim(0,100)
ax.set_xlabel("Distance downstream (km)"); ax.set_ylabel("Dissolved oxygen (mg/L)")
ax.set_title("Oxygen sag curve below an organic-waste discharge",loc="left")
ax.legend(loc="upper center",bbox_to_anchor=(0.5,-0.2),ncol=2,fontsize=8,frameon=False)
save(fig,D+"/U8_oxygen_sag.png")

# 3 biomagnification
fig,ax=canvas(6.2,3.6,xlim=(0,1.0))
lv=[("Water","0.000002\nppm",BLUE),("Phyto-\nplankton","0.002\nppm","#9ACD9A"),("Zoo-\nplankton","0.02\nppm","#C7DE9A"),
    ("Small\nfish","0.2\nppm",SAND),("Large\nfish","2\nppm",ORANGE),("Osprey","20\nppm",RED)]
for i,(n,c,col) in enumerate(lv):
    x=0.01+0.165*i; h=0.10+0.09*i
    ax.add_patch(Rectangle((x,0.30),0.125,h,fc=col if i else SKY,ec=DARK,lw=1))
    ax.text(x+0.0625,0.30+h+0.02,n,ha="center",va="bottom",fontsize=8.5,fontweight="bold")
    ax.text(x+0.0625,0.26,c,ha="center",va="top",fontsize=8.5,color=RED)
    if i<5: arrow(ax,(x+0.13,0.36),(x+0.16,0.36))
ax.text(0.5,0.05,"From phytoplankton upward, each feeding step multiplies the tissue concentration by about 10 because prey\nare eaten in large numbers and the fat-soluble toxin is stored, not excreted. (Illustrative values.)",ha="center",va="center",fontsize=8)
ax.set_title("Biomagnification of a persistent, fat-soluble pollutant",loc="left",fontsize=10)
save(fig,D+"/U8_biomagnification.png")

# 4 dose response
fig,(a,b)=plt.subplots(1,2,figsize=(6.4,3.3))
d=np.logspace(-1,2.3,200)
r=100/(1+(25/d)**2.2)
th=1.0
r=np.where(d<2,r*(d/2)**3,r); 
a.semilogx(d,r,color=RED,lw=2.4)
a.axhline(50,color=GREY,ls=":"); 
ld=np.interp(50,r,d)
a.plot([ld,ld],[0,50],color=BLUE,ls="--"); a.plot(ld,50,"o",color=DARK)
a.text(ld*1.1,6,"LD50 ≈ 25 mg/kg",color=BLUE,fontsize=8.5)
a.axvline(2,color=GREEN,ls="--"); a.text(2.2,80,"Threshold\n≈ 2 mg/kg",color=GREEN,fontsize=8)
a.set_xlabel("Dose (mg per kg body mass, log scale)"); a.set_ylabel("Population dead (%)")
a.set_ylim(0,102); a.set_title("Typical S-shaped curve",fontsize=9.5,loc="left")
# comparison
d2=np.logspace(-1,2.7,200)
for ldv,col,lab in [(25,RED,"Chemical A"),(200,BLUE,"Chemical B")]:
    a2=100/(1+(ldv/d2)**2.2)
    b.semilogx(d2,a2,color=col,lw=2,label=lab)
b.axhline(50,color=GREY,ls=":"); b.legend(fontsize=8,frameon=False,loc="upper left")
b.set_xlabel("Dose (mg/kg, log scale)"); b.set_ylim(0,102)
b.set_title("Lower LD50 = more toxic",fontsize=9.5,loc="left")
fig.tight_layout(); save(fig,D+"/U8_dose_response.png")

# 5 sewage flow
fig,ax=canvas(6.3,3.7,xlim=(-0.02,1.02))
ax.text(0.0,0.93,"Sewage treatment plant",fontsize=11,fontweight="bold")
bx=[("Raw sewage\nin",0.0,"white"),("PRIMARY\nScreens, grit,\nsettling tank",0.205,"#E6DCC3"),
    ("SECONDARY\nAerated tank:\nbacteria digest\norganic matter",0.41,"#CFE8C9"),
    ("TERTIARY\nRemove N, P,\nother pollutants",0.615,"#CDE3F0"),("DISINFECT\nChlorine,\nozone or UV",0.82,"#F6E8B0")]
for t,x,c in bx: box(ax,x,0.50,0.16,0.30,t,fc=c,fs=7.8)
for x in [0.17,0.375,0.58,0.785]: arrow(ax,(x,0.65),(x+0.03,0.65))
box(ax,0.205,0.12,0.16,0.17,"Primary sludge\n(settled solids)",fc="#D2B48C",fs=8)
box(ax,0.41,0.12,0.16,0.17,"CO\u2082 released;\nsludge settles",fc="#D2B48C",fs=8)
arrow(ax,(0.285,0.49),(0.285,0.30)); arrow(ax,(0.49,0.49),(0.49,0.30))
box(ax,0.73,0.12,0.27,0.17,"Treated water to river,\nlake or sea, or reuse",fc="#CDE3F0",fs=8)
arrow(ax,(0.90,0.49),(0.90,0.30))
ax.text(0.5,0.02,"Physical  \u2192  biological  \u2192  chemical / ecological  \u2192  disinfection",ha="center",fontsize=8.5,color=RED)
save(fig,D+"/U8_sewage.png")
