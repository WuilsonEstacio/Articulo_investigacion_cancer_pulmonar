"""T01 · F0: prueba de humo del código ORIGINAL (sin modificaciones).

Importa las funciones de los autores desde el repositorio montado en solo lectura (/repo, commit
fa8e6229) y simula pocos días de cada paciente con los parámetros por defecto de
local_sensitivity_analysis.py, para medir el coste por paso y comprobar que dolfin funciona.

Uso (dentro del contenedor):  python /src/smoke_test.py --days 10
"""
import argparse, json, sys, time, platform
sys.path.insert(0, '/repo/reduced_models')

import dolfin  # noqa: E402
import numpy as np  # noqa: E402
from local_sensitivity_analysis import (  # noqa: E402  (código original, sin cambios)
    default_parameters_patient1, default_parameters_patient2)
from run_spherical_patient_1 import run_patient_1_parametrized  # noqa: E402
from run_spherical_patient_2 import run_patient_2_parametrized  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument('--days', type=float, default=10.)
ap.add_argument('--dt', type=float, default=1 / 24.)
ap.add_argument('--out', default='/out/logs/smoke_test.json')
a = ap.parse_args()

rec = {'dolfin_version': dolfin.__version__, 'numpy': np.__version__, 'python': platform.python_version(),
       'days': a.days, 'dt': a.dt, 'pacientes': {}}
for name, runner, params in [('P1', run_patient_1_parametrized, default_parameters_patient1()),
                             ('P2', run_patient_2_parametrized, default_parameters_patient2())]:
    t0 = time.time()
    res = runner(dt=a.dt, final_time=a.days, model_params=params, verbose=False, output_enabled=False)
    el = time.time() - t0
    rec['pacientes'][name] = {'segundos': el, 'seg_por_dia_simulado': el / a.days,
                              'claves_resultado': sorted(res.keys()),
                              'n_tiempos': len(res['time']),
                              'tumor_visible_final': float(np.asarray(res['tumor_visible'])[-1])}
    print(name, json.dumps(rec['pacientes'][name]))
json.dump(rec, open(a.out, 'w'), indent=1)
