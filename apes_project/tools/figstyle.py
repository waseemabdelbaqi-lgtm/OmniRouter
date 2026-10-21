"""Shared figure style for all Success4Sure APES figures. Import with:
   import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools'); from figstyle import *
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle, Polygon, Ellipse

RED="#7A1424"; DARK="#4A0D14"; GREY="#6B6B6B"; LIGHT="#F4E9EA"
# scientific accent colours (kept muted so the brand red stays dominant)
GREEN="#3E7D4F"; BLUE="#2F6690"; SKY="#9CC5E3"; SAND="#D9B26F"; ORANGE="#D9822B"; BROWN="#8B5E3C"; TEAL="#2A8C82"; YELLOW="#E8C547"
CYCLE=[RED,BLUE,GREEN,ORANGE,TEAL,BROWN,GREY,YELLOW]

plt.rcParams.update({
    "font.family":"serif","font.serif":["Liberation Serif","Times New Roman","DejaVu Serif"],
    "font.size":10,"axes.titlesize":11,"axes.titleweight":"bold","axes.labelsize":10,
    "axes.edgecolor":"#444","axes.linewidth":0.8,"axes.spines.top":False,"axes.spines.right":False,
    "axes.prop_cycle":matplotlib.cycler(color=CYCLE),"figure.dpi":100,"savefig.dpi":220,
    "savefig.bbox":"tight","savefig.pad_inches":0.08,"figure.facecolor":"white","axes.facecolor":"white",
})

def box(ax,x,y,w,h,text,fc=LIGHT,ec=RED,fs=9,bold=False,tc="black"):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.02,rounding_size=0.03",fc=fc,ec=ec,lw=1.2))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",fontsize=fs,fontweight="bold" if bold else "normal",color=tc,wrap=True)

def arrow(ax,p,q,label=None,color=DARK,lw=1.4,fs=8,rad=0.0,off=(0,0.02)):
    ax.add_patch(FancyArrowPatch(p,q,arrowstyle="-|>",mutation_scale=12,color=color,lw=lw,connectionstyle=f"arc3,rad={rad}"))
    if label: ax.text((p[0]+q[0])/2+off[0],(p[1]+q[1])/2+off[1],label,ha="center",va="bottom",fontsize=fs,color=color)

def canvas(w=6.2,h=3.6,xlim=(0,1),ylim=(0,1)):
    fig,ax=plt.subplots(figsize=(w,h)); ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.axis("off"); return fig,ax

def save(fig,path):
    """path relative to content/bookN/figs/, e.g. save(fig,'/home/user/.../figs/U1_carbon_cycle.png')"""
    fig.savefig(path); plt.close(fig)
