"""T05: compara por SHA-256 la re-ejecución aislada con la entrega de T02 (data_derived/, figures/, requirements_T02.txt).
Uso: python -I compara_rerun.py <T02_entrega> <T02_rerun> <salida.json>"""
import sys, json, hashlib
from pathlib import Path
a, b, out = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
def files(root):
    fs = {}
    for sub in ('data_derived', 'figures'):
        for p in (root / sub).rglob('*'):
            if p.is_file():
                fs[p.relative_to(root).as_posix()] = p
    fs['requirements_T02.txt'] = root / 'requirements_T02.txt'
    return fs
fa, fb = files(a), files(b)
comunes = sorted(set(fa) & set(fb))
dif = [k for k in comunes if sha(fa[k]) != sha(fb[k])]
res = dict(n_entrega=len(fa), n_rerun=len(fb), comparados=len(comunes), identicos=len(comunes) - len(dif), diferentes=dif,
           solo_entrega=sorted(set(fa) - set(fb)), solo_rerun=sorted(set(fb) - set(fa)))
json.dump(res, open(out, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(json.dumps({k: (v if not isinstance(v, list) or len(v) < 30 else f'{len(v)} elementos') for k, v in res.items()}, indent=1, ensure_ascii=False))
