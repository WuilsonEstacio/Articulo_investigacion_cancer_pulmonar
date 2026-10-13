import sys, fitz
doc = fitz.open(sys.argv[1]); pg = doc[int(sys.argv[2])-1]
for d in pg.get_drawings():
    c = d.get("color")
    if c is None: continue
    if c and (abs(c[0]-c[1])>0.2 or abs(c[1]-c[2])>0.2):  # colored strokes
        pts=[]
        for it in d["items"]:
            if it[0]=="l": pts += [(round(it[1].x,2),round(it[1].y,2)),(round(it[2].x,2),round(it[2].y,2))]
            elif it[0]=="c": pts += [(round(it[1].x,2),round(it[1].y,2)),(round(it[4].x,2),round(it[4].y,2))]
        # dedupe consecutive
        out=[]
        for p in pts:
            if not out or out[-1]!=p: out.append(p)
        print("COLOR",[round(x,2) for x in c],"w",d.get("width"),"n",len(out)); print(out)
# axis tick labels positions
for b in pg.get_text("words"):
    x0,y0,x1,y1,w = b[:5]
    if x0<330 and 250<y0<720 and (w.replace('.','').isdigit()):
        print("TXT",w,round((x0+x1)/2,2),round((y0+y1)/2,2))
