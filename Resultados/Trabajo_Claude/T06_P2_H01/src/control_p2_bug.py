"""T06 · control de determinismo: recalcula CON EL FALLO ORIGINAL (vector_to_parameters sin corregir) un componente de P2
y aplica la misma fórmula del código, g = (Q+ - Q-) / (2 h alpha Q0), para compararlo con el log original de T01.
Uso (dentro del contenedor):  python -u /src/control_p2_bug.py 1
"""
import sys, os, json
sys.path.insert(0, '/repo/reduced_models')
import numpy as np
import joblib
from local_sensitivity_analysis import (default_parameters_patient2, parameters_to_vector, vector_to_parameters,
                                        integrate)  # código original, sin cambios
from run_spherical_patient_2 import run_patient_2_parametrized

COMP = int(sys.argv[1]) if len(sys.argv) > 1 else 1
H, DT = 1e-3, 1 / 24.
T = float(os.environ.get('T06_FINAL_TIME', 1102))  # solo la prueba de humo usa otro valor
OUT = os.environ.get('T06_OUT', '/out/data_derived')
CAMPOS = ('tumor', 'proliferative', 'necrotic', 'tumor_visible')  # orden del log: g_t, g_p, g_n, g_vt


def sim(etiqueta, params):
    res = run_patient_2_parametrized(dt=DT, final_time=T, model_params=params, verbose=False, output_enabled=False)
    t = np.asarray(res['time'])
    return etiqueta, {'pk': [params.MED_mas, params.MED_dos, params.MED_tim], 'n_t': int(len(t)),
                      'Q': {k: float(integrate(t, np.asarray(res[k]))) for k in CAMPOS}}


if __name__ == '__main__':
    ref = default_parameters_patient2()
    vec = parameters_to_vector(ref)
    e = np.eye(len(vec))[COMP] * H
    trabajos = [('ref', ref), ('mas', vector_to_parameters(vec + vec * e)), ('menos', vector_to_parameters(vec - vec * e))]
    out = dict(joblib.Parallel(n_jobs=3)(joblib.delayed(sim)(n, p) for n, p in trabajos))
    g = {k: (out['mas']['Q'][k] - out['menos']['Q'][k]) / (2 * H * vec[COMP] * out['ref']['Q'][k]) for k in CAMPOS}
    print('control_registros', json.dumps(out), flush=True)
    print(f'control_bug_comp{COMP} g_t = {g["tumor"]!r}, g_p = {g["proliferative"]!r}, g_n = {g["necrotic"]!r}, '
          f'g_vt = {g["tumor_visible"]!r}', flush=True)
    json.dump({'componente': COMP, 'g': g, 'registros': out}, open(f'{OUT}/control_bug_comp{COMP}.json', 'w'), indent=1)
