"""Inspección local del PDF; solo escribe en T03, no importa código de autores."""
from pathlib import Path
import hashlib
import json
import fitz

OUT = Path(__file__).resolve().parents[1]
BASE = OUT.parents[2]
PDF = BASE / 'Data_insumo' / 'A phase-field model for non-small cell lung cancer under the.pdf'


def main():
    dest = OUT / 'data_derived'
    dest.mkdir(exist_ok=True)
    doc = fitz.open(PDF)
    pages = [0, 5, 15, 16]
    metadata = {'path': str(PDF), 'sha256': hashlib.sha256(PDF.read_bytes()).hexdigest(),
                'page_count': len(doc), 'metadata': doc.metadata, 'extracted_pages_1based': [p + 1 for p in pages]}
    (dest / 'pdf_metadata.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding='utf-8')
    for p in pages:
        text = doc[p].get_text(sort=True)
        (dest / f'pdf_p{p+1:02d}.txt').write_text(text, encoding='utf-8')
        if p in (5, 15, 16):
            doc[p].get_pixmap(matrix=fitz.Matrix(1.7, 1.7)).save(str(dest / f'pdf_p{p+1:02d}.png'))
        print(f'\n=== PDF página {p+1} ===\n{text}')
    print('Extracción completada; páginas:', len(doc))


if __name__ == '__main__':
    main()