import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from figstyle import *
import numpy as np
OUT='/home/user/OmniRouter/apes_project/content/book1/figs/'
S3=np.sqrt(3)/2

def classify(c,si,sa):
    if si+1.5*c<15: return 'S'
    if si+2*c<30: return 'LS'
    if (c<20 and sa>52 and si+2*c>=30) or (c<7 and si<50 and 43<=sa<=52): return 'SL'
    if 7<=c<27 and 28<=si<50 and sa<=52: return 'L'
    if (si>=50 and 12<=c<27) or (50<=si<80 and c<12): return 'SiL'
    if si>=80 and c<12: return 'Si'
    if 20<=c<35 and si<28 and sa>45: return 'SCL'
    if 27<=c<40 and 20<sa<=45: return 'CL'
    if 27<=c<40 and sa<=20: return 'SiCL'
    if c>=35 and sa>45: return 'SC'
    if c>=40 and si>=40: return 'SiC'
    if c>=40 and sa<=45 and si<40: return 'C'
    return None
names={'S':'Sand','LS':'Loamy sand','SL':'Sandy loam','L':'Loam','SiL':'Silt loam','Si':'Silt','SCL':'Sandy clay loam','CL':'Clay loam','SiCL':'Silty clay loam','SC':'Sandy clay','SiC':'Silty clay','C':'Clay'}
cols={'S':'#F0DDA8','LS':'#EACB86','SL':'#E0B96B','L':'#B9D28B','SiL':'#A9CFA0','Si':'#8FC7B0','SCL':'#E3A98A','CL':'#C98E78','SiCL':'#A9A0C4','SC':'#D9857B','SiC':'#8EA8D0','C':'#B07A86'}

fig,ax=plt.subplots(figsize=(6.4,4.3)); ax.set_aspect('equal'); ax.axis('off')
n=320; cells={k:[] for k in names}
for i in range(n):
    for j in range(n-i):
        c=(i+0.5)/n*100; si=(j+0.5)/n*100; sa=100-c-si
        if sa<0: continue
        k=classify(c,si,sa)
        if k is None: continue
        cells[k].append((si/100+c/200, c/100*S3))
        # draw small tri-cell as a square marker
for k,pts in cells.items():
    p=np.array(pts); ax.scatter(p[:,0],p[:,1],s=1.6,marker='s',color=cols[k],linewidths=0,zorder=1)
# outline
ax.add_patch(Polygon([[0,0],[1,0],[.5,S3]],fill=False,ec='k',lw=1.2,zorder=3))
# gridlines every 10
for v in range(10,100,10):
    t=v/100
    ax.plot([t/2,1-t/2],[t*S3,t*S3],color='white',lw=.5,alpha=.7,zorder=2)  # clay const
    ax.plot([t,t+(1-t)/2],[0,(1-t)*S3],color='white',lw=.5,alpha=.7,zorder=2)  # silt const
    ax.plot([1-t,(1-t)/2],[0,(1-t)*S3],color='white',lw=.5,alpha=.7,zorder=2)  # sand const
# labels at class centroids
lab={k:tuple(np.mean(np.array(v),axis=0)) for k,v in cells.items()}
lab['S']=(0.045,0.03);lab['LS']=(0.13,0.075);lab['Si']=(0.88,0.06)
for k,(x,y) in lab.items():
    ax.text(x,y,k,fontsize=7.5,ha='center',va='center',fontweight='bold',color='#222',zorder=4)
# ticks
for v in range(0,101,20):
    t=v/100
    ax.text(t/2-0.025,t*S3,str(v),fontsize=7,ha='right',va='center',color=BLUE)           # clay on left edge
    ax.text(1-t/2+0.025,t*S3,str(100-v),fontsize=7,ha='left',va='center',color=GREEN)     # silt on right edge (0 at top)
    ax.text(1-t,-0.035,str(v),fontsize=7,ha='center',va='top',color=BROWN)                # sand on bottom (100 at left)
ax.text(0.11,0.50,"% clay",fontsize=8,color=BLUE,rotation=60,ha='center')
ax.text(0.89,0.50,"% silt",fontsize=8,color=GREEN,rotation=-60,ha='center')
ax.text(0.5,-0.11,"% sand",fontsize=8,color=BROWN,ha='center')
# worked point: clay 35, sand 40, silt 25 -> clay loam
c,si,sa=35,25,40
px,py=si/100+c/200,c/100*S3
ax.plot(px,py,'o',ms=6,mfc='white',mec=RED,mew=2,zorder=6)
ax.annotate("example: 35% clay,\n25% silt, 40% sand",xy=(px,py),xytext=(-0.12,0.80),fontsize=7.5,color=RED,
            arrowprops=dict(arrowstyle='-|>',color=RED,lw=1.2),zorder=6)
# legend key
y0=0.86
for idx,(k,nm) in enumerate(names.items()):
    yy=y0-idx*0.072
    ax.add_patch(Rectangle((1.12,yy-0.026),0.06,0.05,fc=cols[k],ec='k',lw=.4))
    ax.text(1.20,yy,f"{k} = {nm}",fontsize=7.5,va='center')
ax.set_xlim(-0.12,1.55); ax.set_ylim(-0.17,0.93)
save(fig,OUT+'U4_gap_texture_triangle.png')
