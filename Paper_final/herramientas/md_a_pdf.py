"""Convierte un manuscrito Markdown del proyecto en un PDF A4 maquetado.

Uso:  python md_a_pdf.py <entrada.md> <salida.pdf> <en|es>

Pasos: Markdown -> HTML (tablas, código, fórmulas KaTeX y figuras incrustadas) -> PDF con Chrome
en modo headless -> numeración de páginas con PyMuPDF. Requiere Python con `markdown` y `fitz`
(PyMuPDF), Google Chrome y conexión a internet para cargar KaTeX desde jsDelivr.
"""
import html, os, re, shutil, subprocess, sys, tempfile, pathlib
import markdown
import fitz

CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
KATEX = 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist'

FIGURAS = {
    'en': {
        'fig_tabla2.png': ('Figure 1', 'Published Table 2 indices against the released-script output. '
                           'A: raw script output (pre-specified criterion; 0/88 reproduced). '
                           'B: script output ×α/100 (diagnostic; 88/88 within 10 %, maximum error 0.45 %). '
                           'Axis labels are in Spanish.'),
        'fig_h01.png': ('Figure 3', 'Patient 2: relative change of the 44 sensitivity indices after correcting H01, '
                        'by parameter and quantity of interest (dashed lines: ±0.5 %). Axis labels are in Spanish.'),
    },
    'es': {
        'fig_tabla2.png': ('Figura 1', 'Índices de la Tabla 2 publicada frente a la salida del script liberado. '
                           'A: salida bruta (criterio preespecificado; 0/88 reproducidos). '
                           'B: salida ×α/100 (diagnóstico; 88/88 dentro del 10 %, error máximo 0,45 %).'),
        'fig_h01.png': ('Figura 3', 'Paciente 2: cambio relativo de los 44 índices de sensibilidad tras corregir H01, '
                        'por parámetro y cantidad de interés (líneas discontinuas: ±0,5 %).'),
    },
}

CSS = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: Cambria, Georgia, 'Times New Roman', serif; font-size: 10.3pt; line-height: 1.42;
       color: #1a1a1a; margin: 0; }
h1 { font-size: 17pt; line-height: 1.25; margin: 0 0 10pt; color: #0b2545; }
h2 { font-size: 13.5pt; margin: 18pt 0 6pt; padding-bottom: 2pt; border-bottom: 1.2pt solid #0b2545;
     color: #0b2545; break-after: avoid; }
h3 { font-size: 11.5pt; margin: 13pt 0 5pt; color: #13315c; break-after: avoid; }
h4 { font-size: 10.5pt; margin: 10pt 0 4pt; break-after: avoid; }
p { margin: 4pt 0 6pt; text-align: justify; hyphens: auto; }
ul, ol { margin: 3pt 0 6pt; padding-left: 16pt; }
li { margin: 1.5pt 0; overflow-wrap: anywhere; }
blockquote { margin: 6pt 0 10pt; padding: 6pt 10pt; background: #f2f5fa; border-left: 3pt solid #8da9c4;
             font-size: 9.3pt; }
blockquote p { margin: 3pt 0; text-align: left; }
a { color: #1d4e89; text-decoration: none; }
hr { border: 0; border-top: 0.6pt solid #b0b8c4; margin: 12pt 0; }
code { font-family: Consolas, 'Courier New', monospace; font-size: 8.6pt; background: #f3f4f6;
       padding: 0 2pt; border-radius: 2pt; overflow-wrap: anywhere; word-break: break-word; }
pre { background: #f6f8fa; border: 0.6pt solid #d0d7de; border-radius: 3pt; padding: 6pt 8pt;
      white-space: pre-wrap; word-break: break-all; font-size: 8.2pt; line-height: 1.35; break-inside: avoid; }
pre code { background: none; padding: 0; font-size: inherit; }
table { width: 100%; border-collapse: collapse; margin: 6pt 0 10pt; font-size: 8.4pt; line-height: 1.3;
        table-layout: auto; }
thead { display: table-header-group; }
p:has(+ table) { break-after: avoid; }
table tr:first-child, table tbody tr:nth-child(-n+2) { break-before: avoid; }
tr { break-inside: avoid; }
th { background: #dde5ef; color: #0b2545; font-weight: bold; text-align: left; }
th, td { border: 0.5pt solid #9aa7b6; padding: 2.5pt 4pt; vertical-align: top;
         overflow-wrap: anywhere; word-break: normal; hyphens: auto; }
tbody tr:nth-child(even) td { background: #f7f9fc; }
table.ancha { font-size: 6.9pt; }
table.ancha th, table.ancha td { padding: 1.5pt 2.5pt; }
table.muy-ancha { font-size: 6.4pt; }
figure { margin: 10pt 0 12pt; break-inside: avoid; text-align: center; }
figure img { max-width: 100%; max-height: 120mm; }
figcaption { font-size: 8.8pt; text-align: justify; margin-top: 4pt; color: #333; }
.katex { font-size: 1.02em; }
.katex-display { margin: 6pt 0; overflow-x: hidden; overflow-y: hidden; }
"""


def proteger(texto, patron, almacen, prefijo, flags=0):
    def sub(m):
        almacen.append(m.group(0))
        return f'{prefijo}{len(almacen) - 1}Z'
    return re.sub(patron, sub, texto, flags=flags)


def convertir(md_path, pdf_path, idioma):
    src = open(md_path, encoding='utf-8').read().replace('\r\n', '\n')

    # 1. Apartar el código para que sus «$» no se tomen como fórmulas.
    codigo = []
    src = proteger(src, r'```.*?```', codigo, 'QQCODEBLK', re.S)
    src = proteger(src, r'`[^`\n]+`', codigo, 'QQCODEINL')

    # 2. Apartar las fórmulas (display e inline).
    formulas = []
    src = proteger(src, r'\$\$.+?\$\$', formulas, 'QQMATHD', re.S)
    src = proteger(src, r'(?<![\\$])\$(?!\s)[^$\n]+?(?<![\s\\])\$', formulas, 'QQMATHI')

    # 3. Devolver el código y duplicar la sangría de las listas anidadas (python-markdown usa 4 espacios).
    def dev_codigo(m):
        return codigo[int(m.group(2))]
    for _ in range(2):
        src = re.sub(r'QQCODE(BLK|INL)(\d+)Z', dev_codigo, src)
    es_item = re.compile(r'^\s*(?:[-*+]|\d+\.)\s')
    lineas, en_bloque = [], False
    for ln in src.split('\n'):
        if ln.lstrip().startswith('```'):
            en_bloque = not en_bloque
        if not en_bloque:
            if ln[:1] == ' ':
                n = len(ln) - len(ln.lstrip(' '))
                ln = ' ' * (2 * n) + ln.lstrip(' ')
            # Una lista pegada a un párrafo necesita una línea en blanco delante en python-markdown.
            previa = lineas[-1] if lineas else ''
            if es_item.match(ln) and previa.strip() and not es_item.match(previa) \
                    and not previa.startswith(('|', '>', '#')) and not previa.startswith(' '):
                lineas.append('')
        lineas.append(ln)
    src = '\n'.join(lineas)

    # 4. Markdown -> HTML (con identificadores en los títulos para la tabla de contenido).
    cuerpo = markdown.markdown(src, extensions=['tables', 'fenced_code', 'sane_lists', 'toc'], output_format='html5')

    ids = set(re.findall(r'\sid="([^"]+)"', cuerpo))
    rotos = sorted({h for h in re.findall(r'href="#([^"]+)"', cuerpo) if h not in ids})
    if rotos:
        print('AVISO: enlaces internos sin destino:', rotos)

    # 5. Reinsertar las fórmulas para KaTeX.
    def dev_formula(m):
        tipo, k = m.group(1), int(m.group(2))
        f = formulas[k]
        if tipo == 'D':
            return '<div class="math-display">\\[' + html.escape(f[2:-2].strip()) + '\\]</div>'
        return '<span class="math">\\(' + html.escape(f[1:-1]) + '\\)</span>'
    cuerpo = re.sub(r'QQMATH([DI])(\d+)Z', dev_formula, cuerpo)
    cuerpo = cuerpo.replace('<p><div class="math-display">', '<div class="math-display">')
    cuerpo = re.sub(r'(</div>)\s*</p>', r'\1', cuerpo)

    # 6. Tablas anchas: letra más pequeña según el número de columnas.
    def clase_tabla(m):
        cabecera = re.search(r'<tr>(.*?)</tr>', m.group(0), re.S)
        ncol = cabecera.group(1).count('<th') if cabecera else 0
        clase = ' class="muy-ancha"' if ncol >= 10 else (' class="ancha"' if ncol >= 7 else '')
        return m.group(0).replace('<table>', f'<table{clase}>', 1)
    cuerpo = re.sub(r'<table>.*?</table>', clase_tabla, cuerpo, flags=re.S)

    # 7. Incrustar las figuras tras el párrafo que las cita.
    base = pathlib.Path(md_path).resolve().parent
    for archivo, (etiqueta, pie) in FIGURAS[idioma].items():
        img = (base / 'figuras' / archivo).as_uri()
        figura = (f'<figure><img src="{img}" alt="{etiqueta}"><figcaption><b>{etiqueta}.</b> '
                  f'{html.escape(pie)}</figcaption></figure>')
        i = cuerpo.find('figuras/' + archivo)
        assert i >= 0, f'no se encontró la cita de {archivo}'
        j = cuerpo.index('</p>', i) + len('</p>')
        cuerpo = cuerpo[:j] + figura + cuerpo[j:]

    titulo = html.escape(re.search(r'^# (.+)$', open(md_path, encoding='utf-8').read(), re.M).group(1).strip())
    pagina = f"""<!doctype html><html lang="{idioma}"><head><meta charset="utf-8"><title>{titulo}</title>
<link rel="stylesheet" href="{KATEX}/katex.min.css">
<script defer src="{KATEX}/katex.min.js"></script>
<script defer src="{KATEX}/contrib/auto-render.min.js"
 onload="renderMathInElement(document.body,{{delimiters:[{{left:'\\\\[',right:'\\\\]',display:true}},{{left:'\\\\(',right:'\\\\)',display:false}}],throwOnError:false}});document.body.setAttribute('data-katex','ok');"></script>
<style>{CSS}</style></head><body>{cuerpo}</body></html>"""

    tmp = pathlib.Path(tempfile.mkdtemp(prefix='md_a_pdf_'))
    try:
        html_path = tmp / 'manuscrito.html'
        html_path.write_text(pagina, encoding='utf-8')
        pdf_tmp = tmp / 'salida.pdf'
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
                        f'--user-data-dir={tmp / "perfil"}', '--no-pdf-header-footer', '--run-all-compositor-stages-before-draw',
                        '--virtual-time-budget=30000', f'--print-to-pdf={pdf_tmp}', html_path.as_uri()],
                       check=True, timeout=240, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # 8. Numeración de páginas.
        doc = fitz.open(pdf_tmp)
        n = doc.page_count
        for i, page in enumerate(doc):
            r = page.rect
            caja = fitz.Rect(0, r.height - 13 * 72 / 25.4, r.width, r.height - 7 * 72 / 25.4)
            page.insert_textbox(caja, f'{i + 1} / {n}', fontsize=8, fontname='helv', color=(0.35, 0.35, 0.35),
                                align=fitz.TEXT_ALIGN_CENTER)
        doc.set_metadata({'title': html.unescape(titulo), 'creator': 'md_a_pdf.py (Markdown + Chrome headless + PyMuPDF)'})
        doc.save(pdf_path, garbage=3, deflate=True)
        doc.close()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return n


if __name__ == '__main__':
    entrada, salida, idioma = sys.argv[1], sys.argv[2], sys.argv[3]
    paginas = convertir(entrada, salida, idioma)
    print(f'{salida}: {paginas} páginas')
