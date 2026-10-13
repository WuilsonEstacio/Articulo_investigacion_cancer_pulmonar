"""Run any project Python script/tests with immutable execution metadata."""
import os
import sys
import json
import time
import subprocess
import hashlib
from pathlib import Path
from datetime import datetime

ROOT=Path(__file__).resolve().parents[1]
EXPECTED=Path(r'C:\Users\Administrador\PaperCancer_env\venv_cline_T02\Scripts\python.exe')
if Path(sys.executable).resolve()!=EXPECTED.resolve():
    raise RuntimeError('Only the authorized interpreter is allowed')
logs=ROOT/'logs'
logs.mkdir(exist_ok=True)
env=os.environ.copy()
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:
    env[key]='1'
env['MPLCONFIGDIR']=str(ROOT/'.mplconfig')
env['PYTHONIOENCODING']='utf-8'
env['PYTHONDONTWRITEBYTECODE']='1'
start=datetime.now().astimezone()
ident=start.strftime('%Y%m%d_%H%M%S_%f')
command=[str(EXPECTED)]+sys.argv[1:]
snapshot=logs/f'{ident}_source'
snapshot.mkdir()
hashes={}
for folder in ['src','tests','config']:
    for file in (ROOT/folder).glob('*'):
        if file.is_file():
            target=snapshot/folder/file.name
            target.parent.mkdir(exist_ok=True)
            target.write_bytes(file.read_bytes())
            hashes[str(file)]=hashlib.sha256(file.read_bytes()).hexdigest()
for name in ['CRITERIOS_PREESPECIFICADOS.md','DECISIONES_METODO.md']:
    file=ROOT/name
    (snapshot/name).write_bytes(file.read_bytes())
    hashes[str(file)]=hashlib.sha256(file.read_bytes()).hexdigest()
tic=time.perf_counter()
with (logs/f'{ident}.txt').open('w',encoding='utf-8') as handle:
    result=subprocess.run(command,cwd=ROOT,env=env,stdout=handle,stderr=subprocess.STDOUT)
meta=dict(start=start.isoformat(),end=datetime.now().astimezone().isoformat(),duration_seconds=time.perf_counter()-tic,command=command,python=sys.version,seed=20261010,threads=1,exit_code=result.returncode,source_sha256=hashes)
(logs/f'{ident}.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
print((logs/f'{ident}.txt').read_text(encoding='utf-8'))
print('LOG',logs/f'{ident}.json')
sys.exit(result.returncode)