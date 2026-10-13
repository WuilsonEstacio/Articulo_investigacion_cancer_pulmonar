import fitz,sys
d=fitz.open(sys.argv[1]); pg=d[5]
# calibrations: (x0pix,x0val,x1pix,x1val),(y0pix,y0val,y1pix,y1val)
X1=(78.91,0,258.16,2000); X2=(345.63,0,554.55,1400)
panels={
 'P1_LCAD_cm3':(X1,(120.34,0,68.64,3),(60,125)),
 'P1_RECIST_mm':(X1,(184.31,5,141.22,20),(125,190)),
 'P1_WHO_mm2':(X1,(234.01,100,205.16,300),(190,250)),
 'P2_Manual_cm3':(X2,(111.01,0.1,69.95,0.4),(60,125)),
 'P2_RECIST_cm':(X2,(184.6,8,147.92,12),(125,190)),
 'P2_WHO_cm2':(X2,(236.87,50,206.75,100),(190,250)),
}
def lin(p,c): return c[1]+(p-c[0])*(c[3]-c[1])/(c[2]-c[0])
mk=[];vl=[]
for dr in pg.get_drawings():
    c=dr.get('color'); r=dr['rect']
    if c and round(c[0],2)==0.12 and len(dr['items'])==2 and r.width<4:
        mk.append(((r.x0+r.x1)/2,(r.y0+r.y1)/2))
    if c and c==(0.0,0.0,0.0) and r.width<0.5 and r.height>20 and r.y0<260:
        vl.append((round(r.x0,2),round(r.y0,1),round(r.y1,1)))
for name,(X,Y,(ya,yb)) in panels.items():
    left = X is X1
    pts=sorted([(lin(x,X),lin(y,Y)) for x,y in mk if ya<y<yb and ((x<300)==left)])
    print(name,len(pts)); print('  ',[(round(a),round(b,3)) for a,b in pts])
print('vertical black lines', sorted(set((v[0]) for v in vl)))
for v in sorted(set(v[0] for v in vl)):
    print(v, round(lin(v,X1 if v<300 else X2),1))
