import sys, fitz
pdf, out, page, x0,y0,x1,y1, name = sys.argv[1], sys.argv[2], int(sys.argv[3]), *map(float, sys.argv[4:8]), sys.argv[8]
doc = fitz.open(pdf)
pg = doc[page-1]
r = pg.rect
clip = fitz.Rect(r.width*x0, r.height*y0, r.width*x1, r.height*y1)
pg.get_pixmap(dpi=300, clip=clip).save(f"{out}/{name}.png")
# also dump raw chars with font info in clip
for b in pg.get_text("rawdict", clip=clip)["blocks"]:
    for l in b.get("lines", []):
        for s in l["spans"]:
            t = "".join(c["c"] for c in s["chars"])
            if t.strip(): print(ascii(t), s["font"])
