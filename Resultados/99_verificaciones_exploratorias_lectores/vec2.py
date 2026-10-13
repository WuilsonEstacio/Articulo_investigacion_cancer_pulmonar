import sys, fitz
doc = fitz.open(sys.argv[1]); pg = doc[int(sys.argv[2])-1]
hs=[];vs=[]
for d in pg.get_drawings():
    for it in d["items"]:
        if it[0]=="l":
            a,b=it[1],it[2]
            if 60<a.x<300 and 270<a.y<560:
                L=abs(a.x-b.x)+abs(a.y-b.y)
                if L<6: 
                    if abs(a.y-b.y)<0.1: hs.append((round(min(a.x,b.x),2),round(a.y,2)))
                    else: vs.append((round(a.x,2),round(max(a.y,b.y),2)))
print("horizontal short ticks (y-axis):",sorted(set(hs),key=lambda t:t[1]))
print("vertical short ticks (x-axis):",sorted(set(vs)))
