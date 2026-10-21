import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
D='/home/user/OmniRouter/apes_project/content/book2/figs/'

# 1 bloom
fig,ax=plt.subplots(figsize=(6.2,3.5))
m=['Apr','May','Jun','Jul','Aug','Sep','Oct']; x=np.arange(7)
chl=[4,6,30,85,40,12,6]; do=[10.5,10.2,8.5,6.0,2.5,1.2,4.0]
ax.bar(x,chl,color=GREEN,width=0.55,label='Chlorophyll-a (µg/L)')
ax.set_ylabel('Chlorophyll-a (µg/L)',color=GREEN); ax.set_xticks(x); ax.set_xticklabels(m); ax.set_ylim(0,100)
ax2=ax.twinx(); ax2.spines['right'].set_visible(True)
ax2.plot(x,do,color=RED,marker='o',lw=2,label='Bottom-water DO (mg/L)'); ax2.set_ylim(0,12); ax2.set_ylabel('Bottom-water DO (mg/L)',color=RED)
ax.annotate('Heavy rain and lawn\nrunoff (late May)',xy=(1.3,8),xytext=(0.0,60),fontsize=8,arrowprops=dict(arrowstyle='-|>',color=DARK))
ax.set_title('Lake Tamarack, April–October')
h1,l1=ax.get_legend_handles_labels(); h2,l2=ax2.get_legend_handles_labels(); ax.legend(h1+h2,l1+l2,loc='upper right',fontsize=8,frameon=False)
save(fig,D+'QB_U8_bloom.png')

# 2 thermal
fig,ax=plt.subplots(figsize=(5.6,3.4))
T=np.array([5,10,15,20,25,30]); S=np.array([12.8,11.3,10.1,9.1,8.3,7.5])
ax.plot(T,S,color=BLUE,marker='o',lw=2)
for t,s in zip(T,S): ax.annotate(f'{s}',(t,s),textcoords='offset points',xytext=(0,7),ha='center',fontsize=8)
ax.set_xlabel('Water temperature (°C)'); ax.set_ylabel('DO at saturation (mg/L)'); ax.set_ylim(6,14); ax.set_xlim(2,33); ax.grid(alpha=.3)
ax.set_title('Saturation DO in freshwater at sea level')
save(fig,D+'QB_U8_thermal.png')

# 3 sag
fig,ax=plt.subplots(figsize=(6.0,3.4))
d=np.linspace(-10,90,400)
def f(d):
    y=np.full_like(d,8.5)
    k=d>=0
    t=d[k]
    y[k]=8.5-5.5*(np.exp(-t/22)-np.exp(-t/9))/(np.exp(-20/22)-np.exp(-20/9))*0.0+0
    return y
t=np.clip(d,0,None)
deficit=np.where(d>=0,6.0*(np.exp(-t/28)-np.exp(-t/7))/0.5217,0)
# normalise so min deficit 5.5
deficit=deficit/deficit.max()*5.5
ax.plot(d,8.5-deficit,color=BLUE,lw=2.2)
ax.axvline(0,color=GREY,ls='--',lw=1); ax.text(1,9.3,'Wastewater outfall',fontsize=8,color=DARK)
ax.set_xlabel('Distance downstream of outfall (km)'); ax.set_ylabel('Dissolved oxygen (mg/L)'); ax.set_ylim(0,10); ax.set_xlim(-10,90); ax.grid(alpha=.3)
ax.set_title('River DO downstream of an outfall')
save(fig,D+'QB_U8_sag.png')
i=np.argmin(8.5-deficit); print('sag min at',d[i],8.5-deficit[i])

# 4 biomag
fig,ax=plt.subplots(figsize=(6.0,3.5))
lv=['Phyto-\nplankton','Zoo-\nplankton','Small\nfish','Large\nfish','Fish-eating\nbird']
X=[2,2,2,2,2];Y=[1,9,80,700,6000];Z=[30,10,3,1,0.3]
for v,n,c,mk in [(X,'Compound X',GREY,'s'),(Y,'Compound Y',RED,'o'),(Z,'Compound Z',BLUE,'^')]:
    ax.plot(range(5),v,marker=mk,color=c,lw=2,label=n)
ax.set_yscale('log'); ax.set_xticks(range(5)); ax.set_xticklabels(lv,fontsize=8); ax.set_ylabel('Tissue concentration (µg/kg, log scale)')
ax.legend(frameon=False,fontsize=8,loc='upper left'); ax.grid(alpha=.3,which='major')
ax.set_title('Three compounds measured in one food chain')
save(fig,D+'QB_U8_biomag.png')

# 5 dose response
fig,ax=plt.subplots(figsize=(5.8,3.5))
dd=np.logspace(0.5,2.4,200)
for ld,n,c in [(20,'Chemical A',RED),(80,'Chemical B',BLUE)]:
    ax.plot(dd,100/(1+(ld/dd)**3),color=c,lw=2.2,label=n)
ax.set_xscale('log'); ax.set_xticks([5,10,20,40,80,160]); ax.set_xticklabels(['5','10','20','40','80','160'])
ax.set_xlim(3,250); ax.set_ylim(0,102); ax.set_yticks(range(0,101,10))
ax.set_xlabel('Dose (mg per kg body mass, log scale)'); ax.set_ylabel('Tadpoles killed (%)'); ax.grid(alpha=.3,which='major'); ax.legend(frameon=False,loc='lower right')
ax.set_title('Mortality of tadpoles 48 h after dosing')
save(fig,D+'QB_U8_doseresp.png')

# 6 sewage
fig,ax=canvas(6.4,3.0)
ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.text(0.005,0.59,'Raw\nsewage',fontsize=9,ha='left',va='center')
for (x0,lab,t) in [(0.14,'P','Screens, then\nsettling tank'),(0.37,'Q','Aerated tank with\nmicrobes, then\nsettling tank'),(0.60,'R','Filter bed /\nconstructed\nwetland'),(0.82,'S','Disinfection\nchamber')]:
    box(ax,x0,0.38,0.15,0.42,t,fs=8)
    ax.text(x0+0.075,0.87,lab,ha='center',fontsize=13,fontweight='bold',color=RED)
for xa,xb in [(0.095,0.14),(0.29,0.37),(0.52,0.60),(0.75,0.82)]:
    arrow(ax,(xa+ (0.0 if xa>0.1 else 0.0),0.59),(xb,0.59),lw=1.6)
arrow(ax,(0.97,0.59),(0.995,0.59))
for bx in [0.41,0.435,0.46]:
    ax.add_patch(Circle((bx,0.43),0.009,fc='white',ec=BLUE,lw=1))
for x0 in [0.215,0.445]:
    arrow(ax,(x0,0.38),(x0,0.25),color=BROWN,lw=1.2)
ax.text(0.215,0.15,'Solids\n(sludge)',ha='center',fontsize=8,color=BROWN); ax.text(0.445,0.17,'Sludge',ha='center',fontsize=8,color=BROWN)
ax.text(0.99,0.14,'Treated water\nto river',ha='right',fontsize=8)
ax.set_title('A municipal sewage treatment plant',y=1.0)
save(fig,D+'QB_U8_sewage.png')

# 7 landfill
fig,ax=canvas(6.2,3.6)
ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.add_patch(Polygon([[0.05,0.12],[0.95,0.12],[0.95,0.22],[0.05,0.22]],fc=BROWN,ec=DARK))        # base soil
ax.add_patch(Rectangle((0.05,0.22),0.9,0.025,fc='#444',ec='#444'))                                # liner
ax.add_patch(Rectangle((0.05,0.245),0.9,0.07,fc='#BBB',ec=GREY))                                  # gravel
ax.add_patch(Polygon([[0.05,0.315],[0.95,0.315],[0.95,0.62],[0.80,0.74],[0.20,0.74],[0.05,0.62]],fc='#E6D8B8',ec=GREY))  # waste
ax.add_patch(Polygon([[0.20,0.74],[0.80,0.74],[0.95,0.62],[0.95,0.655],[0.80,0.775],[0.20,0.775],[0.05,0.655],[0.05,0.62]],fc=GREEN,ec=DARK))   # cap
for xx in [0.35,0.65]:
    ax.add_patch(Rectangle((xx-0.008,0.4),0.016,0.46,fc='white',ec=DARK))
ax.plot([0.15,0.85],[0.28,0.28],color=GREY,lw=3,ls=(0,(1,1)))
ax.text(0.5,0.55,'buried household waste',ha='center',fontsize=9)
ax.text(0.5,0.17,'compacted soil',ha='center',fontsize=8,color='white')
def tag(n,xy,xt):
    ax.annotate(str(n),xy=xy,xytext=xt,ha='center',va='center',fontsize=11,fontweight='bold',color=RED,
      bbox=dict(boxstyle='circle,pad=0.25',fc='white',ec=RED),arrowprops=dict(arrowstyle='-',color=RED))
tag(1,(0.50,0.76),(0.50,0.92)); tag(2,(0.35,0.80),(0.20,0.92)); tag(3,(0.80,0.28),(0.92,0.40)); tag(4,(0.88,0.233),(0.93,0.04))
ax.set_title('Cross-section of a sanitary municipal landfill',y=1.0)
save(fig,D+'QB_U8_landfill.png')

# FRQ1 map
fig,ax=canvas(6.2,3.8)
ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.add_patch(Ellipse((0.55,0.45),0.36,0.34,fc=SKY,ec=BLUE,lw=1.5)); ax.text(0.55,0.45,'Cedar Pond',ha='center',fontsize=10,fontweight='bold')
ax.add_patch(Rectangle((0.02,0.60),0.24,0.34,fc='#CFE5C8',ec=GREEN)); ax.text(0.14,0.77,'Housing development\n(fertilized lawns,\nstorm drains)',ha='center',va='center',fontsize=8)
ax.add_patch(Rectangle((0.02,0.04),0.24,0.30,fc='#9FC59A',ec=GREEN)); ax.text(0.14,0.19,'Forested\nhillside',ha='center',va='center',fontsize=8)
arrow(ax,(0.26,0.68),(0.43,0.52),color=BLUE,lw=2); arrow(ax,(0.26,0.22),(0.41,0.36),color=BLUE,lw=2)
arrow(ax,(0.73,0.42),(0.95,0.30),color=BLUE,lw=2); ax.text(0.90,0.20,'Outlet\nstream',fontsize=8,ha='center')
def site(lbl,x,y): ax.text(x,y,lbl,ha='center',va='center',fontsize=9,fontweight='bold',color='white',bbox=dict(boxstyle='circle,pad=0.3',fc=RED,ec=DARK))
site('S1',0.33,0.69); site('S2',0.33,0.22); site('S3',0.55,0.30); site('S4',0.80,0.38)
ax.text(0.40,0.84,'Inlet 1',fontsize=8,style='italic'); ax.text(0.40,0.08,'Inlet 2',fontsize=8,style='italic')
ax.set_title('Cedar Pond watershed (not to scale)',y=1.0)
save(fig,D+'QB_U8_frq1_map.png')

# FRQ2 Hg
fig,ax=plt.subplots(figsize=(6.2,3.4))
org=['Plankton','Mayfly\nlarvae','Yellow\nperch','Northern\npike','Common\nloon']
A=[0.01,0.02,0.06,0.20,0.80]; B=[0.02,0.05,0.20,0.90,3.6]
x=np.arange(5); w=0.38
ax.bar(x-w/2,A,w,color=GREEN,label='Lake Alder'); ax.bar(x+w/2,B,w,color=RED,label='Lake Birch')
ax.set_yscale('log'); ax.set_xticks(x); ax.set_xticklabels(org,fontsize=8); ax.set_ylabel('Total mercury (mg/kg wet mass, log scale)')
ax.legend(frameon=False,fontsize=8,loc='upper left'); ax.grid(alpha=.3,axis='y')
ax.set_title('Mercury in tissue of organisms from two lakes')
save(fig,D+'QB_U8_frq2_hg.png')

# FRQ4 dose
fig,ax=plt.subplots(figsize=(5.8,3.4))
dose=[0.01,0.03,0.1,0.3,1,3]; N=[2,8,30,72,95,100]; M=[0,3,12,38,74,96]
ax.plot(dose,N,'-o',color=RED,lw=2,label='Insecticide N'); ax.plot(dose,M,'-s',color=BLUE,lw=2,label='Insecticide M')
ax.set_xscale('log'); ax.set_xticks(dose); ax.set_xticklabels(['0.01','0.03','0.1','0.3','1','3'])
ax.set_xlabel('Dose (µg per bee, log scale)'); ax.set_ylabel('Bees killed (%)'); ax.set_ylim(-3,105); ax.grid(alpha=.3); ax.legend(frameon=False,loc='lower right')
ax.set_title('Honeybee mortality 24 h after dosing')
save(fig,D+'QB_U8_frq4_dose.png')
