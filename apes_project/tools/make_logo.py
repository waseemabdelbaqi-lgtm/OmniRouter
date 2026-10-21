"""Build the clean, official-proportion Success4Sure logo (logo_clean.png) and the diagonal watermark."""
from PIL import Image
import numpy as np, math, sys
B='/home/user/OmniRouter/apes_project/01_brand'
def analyse(src):
    a=np.asarray(src).astype(float);r,g,b=a[...,0],a[...,1],a[...,2]
    ispink=(r-g)>18
    alpha=np.where(ispink,np.clip((255-g)/(255-186),0,1),np.clip((255-a.mean(axis=2))/(255-212),0,1))
    alpha=np.where(alpha<0.04,0,alpha)
    mar=ispink&(alpha>0.5);ys,xs=np.where(mar)
    return a,ispink,alpha,(xs.min(),ys.min(),xs.max(),ys.max())
def build():
    src=Image.open('/tmp/claude-0/-home-user-OmniRouter/1a21046e-f8ca-5b17-af75-88e695d5d711/images/1.webp').convert('RGB')
    src=src.resize((src.width*2,src.height*2),Image.LANCZOS).rotate(25,expand=True,resample=Image.BICUBIC,fillcolor=(255,255,255))
    E=np.asarray(Image.open(f'{B}/logo_extracted_hi.png')).astype(float)
    Em=(E[...,3]>128)&(E[...,0]>100)&(E[...,1]<60);ys,xs=np.where(Em);Eb=(xs.min(),ys.min(),xs.max(),ys.max())
    a,ispink,alpha,Lb=analyse(src)
    f=((Eb[2]-Eb[0])/(Eb[3]-Eb[1]))/((Lb[2]-Lb[0])/(Lb[3]-Lb[1]))   # official aspect / art aspect
    src=src.resize((int(src.width*f),src.height),Image.LANCZOS)
    a,ispink,alpha,Lb=analyse(src)
    top=max(Lb[1]-80,0);left=max(Lb[0]-40,0);right=min(Lb[2]+120,a.shape[1])
    a=a[top:,left:right];ispink=ispink[top:,left:right];alpha=alpha[top:,left:right]
    Lb=(Lb[0]-left,Lb[1]-top,Lb[2]-left,Lb[3]-top)
    s=(Lb[2]-Lb[0])/(Eb[2]-Eb[0]);ph,pw=alpha.shape
    Hc=int(max(ph,Lb[3]+(E.shape[0]-Eb[3])*s+60))
    col=np.zeros((Hc,pw,3));alp=np.zeros((Hc,pw))
    colL=np.zeros(a.shape);colL[...]=(150,150,150);colL[ispink]=(122,20,36)
    yy=np.arange(ph)[:,None]*np.ones((1,pw))
    colL[(yy>=Lb[3]-30)&(yy<Lb[3]+8)&(alpha>0)]=(122,20,36)
    alL=np.where(yy<Lb[3]+8,alpha,0);col[:ph]=colL;alp[:ph]=alL
    yyE=np.arange(E.shape[0])[:,None]*np.ones((1,E.shape[1]))
    Eg=E.copy();Eg[...,3]=np.where((yyE>Eb[3]+0.03*(Eb[3]-Eb[1]))&(E[...,3]>0),E[...,3],0)
    Ei=Image.fromarray(Eg.astype('uint8'),'RGBA').resize((int(E.shape[1]*s),int(E.shape[0]*s)),Image.LANCZOS)
    Ea=np.asarray(Ei).astype(float);ox=int(Lb[0]-Eb[0]*s);oy=int(Lb[1]-Eb[1]*s)
    H,W=Ea.shape[:2];y0=max(oy,0);x0=max(ox,0);y1=min(oy+H,Hc);x1=min(ox+W,pw)
    sub=Ea[y0-oy:y1-oy,x0-ox:x1-ox];a2=sub[...,3]/255;reg=alp[y0:y1,x0:x1]
    col[y0:y1,x0:x1]=np.where((a2>reg)[...,None],sub[...,:3],col[y0:y1,x0:x1]);alp[y0:y1,x0:x1]=np.maximum(reg,a2)
    Lg=Image.fromarray(np.dstack([col,alp*255]).astype('uint8'),'RGBA')
    Lg=Lg.crop(Lg.getchannel('A').point(lambda v:255 if v>30 else 0).getbbox());Lg.save(f'{B}/logo_clean.png')
    bg=Image.new('RGB',Lg.size,'white');bg.paste(Lg,mask=Lg.getchannel('A'));bg.save(f'{B}/logo_on_white.png');bg.resize((Lg.width//3,Lg.height//3)).save(f'{B}/logo_preview.png')
    return Lg
def watermark(Lg,length_cm=24.6,opacity=0.13,angle=None,dpi=110):
    W,H=21.0,29.7
    ang=math.degrees(math.atan2(H,W)) if angle is None else angle   # page diagonal, top-left -> bottom-right
    w_px=int(length_cm/2.54*dpi*2)           # 2x oversampling
    h_px=int(w_px*Lg.height/Lg.width)
    L=Lg.resize((w_px,h_px),Image.LANCZOS)
    al=L.getchannel('A').point(lambda v:int(v*opacity));L.putalpha(al)
    Rt=L.rotate(-ang,expand=True,resample=Image.BICUBIC)       # clockwise: reads top-left -> bottom-right
    Rt=Rt.crop(Rt.getchannel('A').point(lambda v:255 if v>0 else 0).getbbox())
    Rt.save(f'{B}/watermark.png');print('watermark',Rt.size,ang,'cm size',Rt.width/(dpi*2)*2.54,Rt.height/(dpi*2)*2.54)
if __name__=="__main__":
    watermark(build())
