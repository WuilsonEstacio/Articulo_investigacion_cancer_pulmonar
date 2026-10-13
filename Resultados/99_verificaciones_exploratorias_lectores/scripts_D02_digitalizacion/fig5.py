import fitz,sys
import numpy as np
d=fitz.open(sys.argv[1]); pg=d[9]; D=pg.get_drawings()
grid=[(round(dr['rect'].x0,2),round(dr['rect'].y0,2),round(dr['rect'].x1,2),round(dr['rect'].y1,2)) for dr in D if dr.get('color') and round(dr['color'][0],2)==0.69]
hor=sorted(set((g[1]) for g in grid if g[1]==g[3]))
ver=sorted(set((g[0]) for g in grid if g[0]==g[2]))
print('hor',hor); print('ver',ver)
for b in pg.get_text('dict')['blocks']:
  for l in b.get('lines',[]):
    s=''.join(sp['text'] for sp in l['spans']); bb=l['bbox']
    if bb[1]<270 and len(s)<12: print(repr(s),[round(v,1) for v in bb])
for i,dr in enumerate(D):
    r=dr['rect']
    if len(dr['items'])>30 and r.y1<270:
        ys=[]; xs=[]
        for it in dr['items']:
            if it[0]=='l': xs+=[it[1].x,it[2].x]; ys+=[it[1].y,it[2].y]
        print(i,[round(c,2) for c in dr['color']],dr.get('dashes'),len(dr['items']),[round(v,1) for v in r],'ymin',round(min(ys),2),'ymax',round(max(ys),2))
