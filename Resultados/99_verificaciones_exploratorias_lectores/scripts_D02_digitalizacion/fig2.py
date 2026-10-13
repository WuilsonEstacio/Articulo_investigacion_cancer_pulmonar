import fitz,sys
d=fitz.open(sys.argv[1]); pg=d[int(sys.argv[2])-1]; ymax=float(sys.argv[3])
def pts(dr):
    out=[]
    for it in dr['items']:
        if it[0]=='l': out+= [it[1],it[2]]
        elif it[0]=='c': out+=[it[1],it[4]]
    # dedupe consecutive
    res=[]
    for p in out:
        if not res or (abs(res[-1][0]-p.x)>1e-3 or abs(res[-1][1]-p.y)>1e-3): res.append((p.x,p.y))
    return res
grid=[]
for i,dr in enumerate(pg.get_drawings()):
    c=dr.get('color'); r=dr['rect']
    if r.y0>ymax: continue
    if c and round(c[0],2)==0.69: grid.append((round(r.x0,2),round(r.y0,2),round(r.x1,2),round(r.y1,2)))
    elif len(dr['items'])>=8 or (c==(0,0,0) and r.height>20 and r.width<0.5):
        p=pts(dr)
        print('#',i,c,dr.get('dashes'),len(dr['items']),[round(v,1) for v in r])
        if len(p)<=30: print('   ',[(round(a,2),round(b,2)) for a,b in p])
print('GRID',grid)
