import fitz,sys
from collections import Counter
d=fitz.open(sys.argv[1]); pg=d[int(sys.argv[2])-1]; ymax=float(sys.argv[3])
cols=Counter()
for dr in pg.get_drawings():
    c=dr.get('color'); r=dr['rect']
    if r.y0>ymax: continue
    cols[(tuple(round(x,2) for x in c) if c else None, len(dr['items']), dr.get('dashes'))]+=1
for k,v in cols.items(): print(k,v)
for b in pg.get_text('dict')['blocks']:
  for l in b.get('lines',[]):
    s=''.join(sp['text'] for sp in l['spans']); bb=l['bbox']
    if bb[1]<ymax: print(repr(s),[round(v,1) for v in bb])
