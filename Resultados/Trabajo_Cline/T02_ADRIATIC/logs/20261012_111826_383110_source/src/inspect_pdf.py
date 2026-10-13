"""Read-only inspection of authorized PDF; outputs stay inside T02."""
import os
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
os.environ['MPLCONFIGDIR'] = str(ROOT / '.mplconfig')
import json
import hashlib
from datetime import datetime
import pymupdf
import yaml

cfg = yaml.safe_load((ROOT / 'config/config.yaml').read_text(encoding='utf-8'))
pdf = Path(cfg['project_root']) / cfg['pdf_relative']
out = ROOT / 'logs'
out.mkdir(exist_ok=True)
doc = pymupdf.open(pdf)
report = {'timestamp': datetime.now().astimezone().isoformat(), 'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(), 'pages': {}}
for endpoint, pno in cfg['pages'].items():
    page = doc[pno-1]
    drawings = page.get_drawings()
    colored = []
    for idx, d in enumerate(drawings):
        col = d['fill'] or d['color']
        if col and any(sum((a-b)**2 for a,b in zip(col,target))**0.5 < cfg['color_tolerance'] for target in cfg['colors'].values()):
            colored.append({'id': idx, 'fill':d['fill'], 'color':d['color'], 'rect':list(d['rect']), 'items_count':len(d['items']), 'items_sample':str(d['items'][:12])})
    report['pages'][endpoint] = {'colored_drawings':colored, 'words':[list(w) for w in page.get_text('words') if w[1]<410]}
    page.get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).save(str(out / f'page_{pno}.png'))
(out / 'pdf_inspection.json').write_text(json.dumps(report, indent=2),encoding='utf-8')
print('PDF',report['pdf_sha256'])
for endpoint,p in report['pages'].items():
    print(endpoint, 'colored',len(p['colored_drawings']))
    print(json.dumps(p['colored_drawings'][:12],indent=2))