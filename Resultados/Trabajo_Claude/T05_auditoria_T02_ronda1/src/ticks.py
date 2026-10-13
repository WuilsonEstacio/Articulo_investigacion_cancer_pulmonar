import sys, pymupdf, numpy as np
doc = pymupdf.open(sys.argv[1])
for p in (6, 8):
    page = doc[p-1]
    segs=[]
    for d in page.get_drawings():
        col = d.get('color') or d.get('fill')
        if col is None or max(col) > 0.25: continue
        for it in d['items']:
            if it[0]=='l':
                a,b=it[1],it[2]
                if 60<a.y<200 and 70<a.x<360: segs.append((round(a.x,2),round(a.y,2),round(b.x,2),round(b.y,2), d.get('width')))
            elif it[0]=='re':
                r=it[1]
                if 60<r.y0<200 and 70<r.x0<360 and (r.width<1.5 or r.height<1.5): segs.append(('re',round(r.x0,2),round(r.y0,2),round(r.x1,2),round(r.y1,2)))
    print(p, len(segs)); print(segs[:80])
