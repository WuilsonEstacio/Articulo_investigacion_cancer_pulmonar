import fitz,sys
import numpy as np
d=fitz.open(sys.argv[1]); pg=d[7]
D=pg.get_drawings()
def pts(dr):
    out=[]
    for it in dr['items']:
        if it[0]=='l': out+= [it[1],it[2]]
        elif it[0]=='c': out+=[it[1],it[4]]
    res=[]
    for p in out:
        if not res or (abs(res[-1][0]-p.x)>1e-3 or abs(res[-1][1]-p.y)>1e-3): res.append((p.x,p.y))
    return np.array(res)
def cal(a,c): return lambda p: c[1]+(p-c[0])*(c[3]-c[1])/(c[2]-c[0])
cfg={'P1':dict(real=22,sim=44,imm=75,m_solid=105,m_dash=106,m_dot=107,X=(64.02,0,109.51,500),Yv=(170.37,0,128.42,3),Yi=(230.54,0,196.68,1.0),Ym=(291.72,0,249.94,3)),
     'P2':dict(real=141,sim=153,imm=186,m_solid=215,m_dash=216,m_dot=217,X=(351.97,0,383.71,200),Yv=(169.96,0,132.53,0.4),Yi=(230.65,0,185.85,1.0),Ym=(291.71,0,245.53,0.00004))}
for k,c in cfg.items():
    fx=cal(None,c['X']); fv=cal(None,c['Yv']); fi=cal(None,c['Yi']); fm=cal(None,c['Ym'])
    R=pts(D[c['real']]); S=pts(D[c['sim']])
    rt=fx(R[:,0]); rv=fv(R[:,1]); st=fx(S[:,0]); sv=fv(S[:,1])
    o=np.argsort(st); st,sv=st[o],sv[o]
    print(k,'sim t range',round(st.min(),1),round(st.max(),1),'sim V0',round(sv[0],3),'sim Vmax',round(sv.max(),3),'at',round(st[sv.argmax()],1), 'V end', round(sv[-1],3))
    si=np.interp(rt,st,sv)
    for t,v,s in zip(rt,rv,si): print('   t=%6.0f real=%.3f sim=%.3f'%(t,v,s))
    I=pts(D[c['imm']]); print('  imm max (1e17)',round(fi(I[:,1]).max(),3),'t range',round(fx(I[:,0]).min()),round(fx(I[:,0]).max()))
    for nm in ['m_solid','m_dash','m_dot']:
        M=pts(D[c[nm]]); mt=fx(M[:,0]); mv=fm(M[:,1])
        print('  ',nm,'max',mv.max(),'at',round(mt[mv.argmax()]),'end',mv[np.argmax(mt)])
