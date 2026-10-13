import fitz,sys
import numpy as np
d=fitz.open(sys.argv[1]); pg=d[7]; D=pg.get_drawings()
def pts(dr):
    out=[]
    for it in dr['items']:
        if it[0]=='l': out+= [it[1],it[2]]
    return np.array([(p.x,p.y) for p in out])
for idx,X,Y in [(75,(64.02,0,109.51,500),(230.54,0,196.68,1.0)),(186,(351.97,0,383.71,200),(230.65,0,185.85,1.0))]:
    P=pts(D[idx]); t=X[1]+(P[:,0]-X[0])*(X[3]-X[1])/(X[2]-X[0]); v=Y[1]+(P[:,1]-Y[0])*(Y[3]-Y[1])/(Y[2]-Y[0])
    nz=t[v>0.01]; print('first nonzero t',round(nz.min(),1),'last >0.01',round(nz.max(),1))
    # peaks: local maxima
    o=np.argsort(t,kind='stable'); 
    pk=[(round(t[i],1),round(v[i],3)) for i in range(1,len(t)-1) if v[i]>v[i-1] and v[i]>=v[i+1]]
    print(" n peaks",len(pk)); print([p for p in pk if p[1]>0.5*max(q[1] for q in pk)])
    if len(pk)>3:
        tt=np.array([p[0] for p in pk]); print(' median spacing', np.median(np.diff(tt)))
