import sys, fitz
pdf, out, pages, prefix = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
doc = fitz.open(pdf)
for p in [int(x) for x in pages.split(',')]:
    pix = doc[p-1].get_pixmap(dpi=130)
    pix.save(f"{out}/{prefix}_p{p}.png")
print(prefix, doc.page_count)
