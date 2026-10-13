"""Regenerate all scientific outputs from authorized inputs."""
import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.environ['MPLCONFIGDIR']=str(ROOT/'.mplconfig')
import sys
import json
import hashlib
import argparse
import io
from contextlib import redirect_stdout
import yaml
import pandas as pd
import numpy as np
from extract import extract_pdf
from guyot import reconstruct
from validate import validate
from simulate import run_simulations
from simulate_digitized import run_digitized_simulations


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--stage',choices=['all','clinical','simulation','report'],default='all')
    args=parser.parse_args()
    cfg=yaml.safe_load((ROOT/'config/config.yaml').read_text(encoding='utf-8'))
    if Path(sys.executable).resolve()!=Path(cfg['python']).resolve():
        raise RuntimeError('Unauthorized interpreter')
    out=ROOT/'data_derived'
    out.mkdir(exist_ok=True)
    (ROOT/'figures').mkdir(exist_ok=True)
    project=Path(cfg['project_root'])
    source=project/cfg['inputs_relative']
    inputs=pd.read_csv(source)
    if args.stage in ['all','clinical']:
        curves,audit=extract_pdf(project/cfg['pdf_relative'],cfg,out)
        (out/'extraction_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
        ipds={}
        inventory=[]
        for (ep,arm),points in curves.items():
            sub=inputs[(inputs.brazo==arm)&(inputs.desenlace==ep)]
            risk=sub[sub.insumo=='numeros_en_riesgo'].iloc[0]
            events=sub[sub.insumo=='eventos_totales'].iloc[0]
            nr=np.array([int(v) for v in risk.valor.split(',')])
            ipd,intervals=reconstruct(points.time_months,points.survival,np.arange(0,64,3),nr,int(events.valor))
            ipd['arm']=arm
            ipd['endpoint']=ep
            ipd.to_csv(out/f'pseudo_ipd_{ep}_{arm}.csv',index=False)
            intervals.to_csv(out/f'intervals_{ep}_{arm}.csv',index=False)
            ipds[ep,arm]=ipd
            inventory.append(dict(endpoint=ep,arm=arm,n=int(nr[0]),events_published=int(events.valor),curve_page=cfg['pages'][ep],risk_source=risk.ubicacion,events_source=events.ubicacion,support_end=float(points.time_months.iloc[-1]),pdf_sha256=hashlib.sha256((project/cfg['pdf_relative']).read_bytes()).hexdigest()))
        pd.DataFrame(inventory).to_csv(out/'inventory.csv',index=False)
        results=validate(curves,ipds,inputs,cfg,out)
        print(results[results.scope=='H1'].to_string(index=False),flush=True)
        # Preserve every evaluated clinical result, not just the final state.
        from datetime import datetime
        archive=ROOT/'logs'/('clinical_'+datetime.now().strftime('%Y%m%d_%H%M%S_%f'))
        archive.mkdir(parents=True)
        for f in out.glob('*'):
            if f.is_file():
                (archive/f.name).write_bytes(f.read_bytes())
    if args.stage in ['all','simulation']:
        run_simulations(cfg,out)
        run_digitized_simulations(cfg,out)
    # Execute pip's read-only freeze command in process: the Windows venv
    # launcher plus logging wrapper already occupy four OS process entries.
    from pip._internal.cli.main import main as pip_main
    buffer=io.StringIO()
    with redirect_stdout(buffer):
        status=pip_main(['freeze','--disable-pip-version-check'])
    if status:
        raise RuntimeError(f'pip freeze failed: {status}')
    freeze=buffer.getvalue()
    (ROOT/'requirements_T02.txt').write_text(freeze,encoding='utf-8')
    if args.stage in ['all','report']:
        from reporting import create_report
        create_report(ROOT,cfg)


if __name__=='__main__':
    main()