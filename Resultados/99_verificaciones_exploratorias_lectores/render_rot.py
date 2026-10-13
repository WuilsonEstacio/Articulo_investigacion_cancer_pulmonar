import sys, fitz
pdf, prefix, pages, zoom, rot = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), int(sys.argv[5])
doc = fitz.open(pdf)
for p in [int(x) for x in pages.split(",")]:
    pg = doc[p-1]; r = pg.rect
    m = fitz.Matrix(zoom, zoom).prerotate(rot)
    for tag,(x0,x1) in {"a":(0, r.width/2+25), "b":(r.width/2-25, r.width)}.items():
        clip = fitz.Rect(x0, 0, x1, r.height)
        pix = pg.get_pixmap(matrix=m, clip=clip)
        pix.save(f"{prefix}_p{p:02d}_{tag}.png"); print(p, tag, pix.width, pix.height)
