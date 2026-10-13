"""Extrae texto por página de los PDF de Data_insumo (solo lectura) con marcas [p. N].
Uso: python -I extraer_pdf.py <dir_insumo> <dir_salida>"""
import sys, os, hashlib, json, fitz
src, out = sys.argv[1], sys.argv[2]
report = []
for fn in sorted(os.listdir(src)):
    if not fn.lower().endswith('.pdf'): continue
    p = os.path.join(src, fn)
    sha = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    doc = fitz.open(p)
    pages, low = [], []
    for i, pg in enumerate(doc, 1):
        t = pg.get_text()
        pages.append(f"\n\n===== [p. {i}] =====\n{t}")
        if len(t.strip()) < 200: low.append(i)
    base = os.path.splitext(fn)[0].strip()
    open(os.path.join(out, base + '.txt'), 'w', encoding='utf-8').write(''.join(pages))
    report.append(dict(archivo=fn, sha256=sha, paginas=doc.page_count,
                       caracteres=sum(len(x) for x in pages), paginas_poco_texto=low,
                       metadata={k: v for k, v in doc.metadata.items() if v}))
json.dump(report, open(os.path.join(out, '_reporte_extraccion.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for r in report: print(r['paginas'], r['caracteres'], r['paginas_poco_texto'], r['archivo'], r['metadata'].get('title',''))
