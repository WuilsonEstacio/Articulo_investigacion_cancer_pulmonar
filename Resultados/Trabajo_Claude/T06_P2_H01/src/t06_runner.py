"""T06 · H01: envoltorio del runner original de P2. Está en un módulo importable (no en __main__) para que joblib/loky
lo serialice por referencia, como al runner original. Con la función definida en __main__ y serializada por valor, los
workers fallaban con SIGSEGV al importar dolfin (prueba de humo del 12-oct-2026).

Antes de cada simulación restablece MED_mas / MED_dos / MED_tim a los valores de default_parameters_patient2(),
registra los campos antes y después de la corrección y guarda las integrales Q (regla del trapecio original).
"""
import os, json, time
import numpy as np
import local_sensitivity_analysis as lsa  # código original, sin cambios
from run_spherical_patient_2 import run_patient_2_parametrized  # código original, sin cambios

PK_FIELDS = ('MED_mas', 'MED_dos', 'MED_tim')
REF_PK = {f: getattr(lsa.default_parameters_patient2(), f) for f in PK_FIELDS}
CAMPOS_Q = ('tumor', 'proliferative', 'necrotic', 'tumor_visible')


def runner_p2_corr(dt, final_time, model_params, **kw):
    qdir = os.environ.get('T06_QDIR', '/out/data_derived/q_corr')
    antes = {f: getattr(model_params, f) for f in PK_FIELDS}
    for f in PK_FIELDS:
        setattr(model_params, f, REF_PK[f])
    res = run_patient_2_parametrized(dt=dt, final_time=final_time, model_params=model_params, **kw)
    t = np.asarray(res['time'])
    rec = {'pid': os.getpid(), 'pk_antes': antes, 'pk_usado': {f: getattr(model_params, f) for f in PK_FIELDS},
           'vec': [float(v) for v in lsa.parameters_to_vector(model_params)], 'n_t': int(len(t)), 't_fin': float(t[-1]),
           'Q': {k: float(lsa.integrate(t, np.asarray(res[k]))) for k in CAMPOS_Q}}
    os.makedirs(qdir, exist_ok=True)
    with open(os.path.join(qdir, f'q_{time.time_ns()}_{os.getpid()}.json'), 'w') as fh:
        json.dump(rec, fh, indent=1)
    print('runner_p2_corr', json.dumps({k: rec[k] for k in ('pk_antes', 'pk_usado')}), flush=True)
    return res
