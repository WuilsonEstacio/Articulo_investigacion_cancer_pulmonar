import fitz,sys
d=fitz.open(sys.argv[1]); pg=d[int(sys.argv[2])-1]
from collections import Counter
cols=Counter()
for dr in pg.get_drawings():
    c=dr.get('color')
    cols[(tuple(round(x,2) for x in c) if c else None, len(dr['items']))]+=1
print(cols)
for dr in pg.get_drawings():
    c=dr.get('color')
    if c and round(c[0],2)==0.69 and len(dr['items'])==1:
        r=dr['rect']; print('grid', round(r.x0,2),round(r.y0,2),round(r.x1,2),round(r.y1,2))
