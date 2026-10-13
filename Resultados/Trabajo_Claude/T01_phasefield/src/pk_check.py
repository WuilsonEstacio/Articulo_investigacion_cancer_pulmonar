"""T01 · F1 · Farmacocinética: el MedicineSolver ORIGINAL (sin modificar) frente a la solución analítica de la ec. 6.

Ec. 6 (MBE 2023; D02 p. 4): dφ/dt = -ln2/t½ · φ + (N_A/M)·d · 1{t ∈ I_τ}.
Con infusiones rectangulares de duración τ = 1/24 d cada P días, el estado periódico exacto es:
    pico  = (R/k)(1 - e^{-kτ}) / (1 - e^{-kP}),   R = N_A·d/M [moléculas/d],  k = ln2/t½
    valle = pico · e^{-k(P-τ)}
Criterio (contrato T01 §4.2, fijado antes de ejecutar): error relativo ≤ 0.1 % en pico y valle.

Esquemas tomados del código original (run_spherical_patient_1/2.py, funciones *_parametrized usadas en la Tabla 2):
  P1: inicio 146 d (tiempo de simulación), cada 14 d, fin 1479 d; d=0.24 g; M=146000; t½=26.7 d; φ(0)=0.
  P2: Q3W desde 14 d hasta 557 d, Q6W desde 557 d hasta 1104 d; d=0.20 g; M=143600; t½=22 d; φ(0)=1.2e17/2.
Uso: python pk_check.py <ruta_reduced_models> <salida_json>
"""
import sys, json, math
import numpy as np

sys.path.insert(0, sys.argv[1])
from medicine_solver import MedicineSolver               # original, sin cambios
from time_therapy_evaluator import TimeTherapyEvaluator  # original, sin cambios
from parameters import TherapyParameters, TumorModelParameters
from create_therapy_schedule import create_therapy_schedule

NA = 6.022140857e23
DT, SUB = 1 / 24., 1 / 24. / 32.  # create_system_PN_i: MedicineSolver(params, time_therapy, dt, 1/24/32)


def simulate(therapies, mparams, final_time, med_init):
    start, length = create_therapy_schedule(therapies)
    tt = TimeTherapyEvaluator(start=start, length=length)
    ms = MedicineSolver(mparams, tt, DT, SUB)  # igual que create_system_PN_i (solvers.py)
    ms.MED = med_init                          # igual que SimulationRunner.run (medicine_solver.MED = med_init)
    n = int(final_time / DT)
    t, med, cur = np.zeros(n + 1), np.zeros(n + 1), 0.0
    med[0] = med_init
    for i in range(n):
        ms.reassign(); ms.solve(cur); cur += DT
        t[i + 1], med[i + 1] = cur, ms.MED
    return t, med


def analytic(d, M, thalf, P, tau=1 / 24.):
    k, R = math.log(2) / thalf, NA * d / M
    peak = (R / k) * (1 - math.exp(-k * tau)) / (1 - math.exp(-k * P))
    return peak, peak * math.exp(-k * (P - tau))


def periodic_extrema(t, med, t0, t1, P):
    """Picos (máximos locales) y valles (justo antes de cada dosis) en la ventana [t0, t1]."""
    m = (t >= t0) & (t <= t1)
    tt, mm = t[m], med[m]
    i = np.where((mm[1:-1] > mm[:-2]) & (mm[1:-1] >= mm[2:]))[0] + 1
    j = np.where((mm[1:-1] < mm[:-2]) & (mm[1:-1] <= mm[2:]))[0] + 1
    return mm[i], mm[j]


out = {}
cases = {
    'P1_Q2W': dict(th=[TherapyParameters(146, 1655 - 176, 14)], mp=TumorModelParameters(), T=1479, init=0.0,
                   win=(1000, 1470), P=14),
    'P2_Q3W': dict(th=[TherapyParameters(14, 557, 21), TherapyParameters(557, 1104, 42)],
                   mp=TumorModelParameters(MED_mas=143600, MED_dos=0.2, MED_tim=22.), T=1104, init=1.2e17 / 2,
                   win=(300, 550), P=21),
    'P2_Q6W': dict(th=[TherapyParameters(14, 557, 21), TherapyParameters(557, 1104, 42)],
                   mp=TumorModelParameters(MED_mas=143600, MED_dos=0.2, MED_tim=22.), T=1104, init=1.2e17 / 2,
                   win=(800, 1100), P=42),
}
for name, c in cases.items():
    t, med = simulate(c['th'], c['mp'], c['T'], c['init'])
    pk, vl = periodic_extrema(t, med, *c['win'], c['P'])
    apk, avl = analytic(c['mp'].MED_dos, c['mp'].MED_mas, c['mp'].MED_tim, c['P'])
    rec = {'pico_analitico': apk, 'valle_analitico': avl,
           'pico_codigo_ultimo': float(pk[-1]), 'valle_codigo_ultimo': float(vl[-1]),
           'n_picos_ventana': int(len(pk)),
           'err_rel_pico': float(abs(pk[-1] - apk) / apk), 'err_rel_valle': float(abs(vl[-1] - avl) / avl)}
    rec['cumple_0.1%'] = bool(rec['err_rel_pico'] <= 1e-3 and rec['err_rel_valle'] <= 1e-3)
    out[name] = rec
    print(name, json.dumps(rec))
    np.savetxt(sys.argv[2].replace('.json', f'_{name}_serie.csv'), np.c_[t, med], delimiter=',',
               header='t_sim_dias,phi_tau_moleculas', comments='', fmt='%.10g')
json.dump(out, open(sys.argv[2], 'w'), indent=1)
