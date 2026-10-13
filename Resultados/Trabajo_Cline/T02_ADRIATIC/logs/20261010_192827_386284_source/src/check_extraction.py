import json
from pathlib import Path
import yaml
from extract import extract_pdf
ROOT=Path(__file__).resolve().parents[1]
cfg=yaml.safe_load((ROOT/'config/config.yaml').read_text(encoding='utf-8'))
out=ROOT/'data_derived'
out.mkdir(exist_ok=True)
curves,audit=extract_pdf(Path(cfg['project_root'])/cfg['pdf_relative'],cfg,out)
(out/'extraction_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
print(json.dumps(audit,indent=2))