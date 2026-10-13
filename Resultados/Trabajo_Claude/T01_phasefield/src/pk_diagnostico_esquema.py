"""T01 · diagnóstico (no criterio): dosis efectiva de CADA administración del esquema P1 y P2 en el código ORIGINAL,
sin eliminación (t½=1e30), con el mismo avance temporal que SolverPN (t += dt, acumulado en coma flotante).
Uso: python pk_diagnostico_esquema.py <ruta_reduced_models> <salida_csv>"""
import sys, numpy as np
from collections import Counter
sys.path.insert(0, sys.argv[1])
from medicine_solver import MedicineSolver
from time_therapy_evaluator import TimeTherapyEvaluator
from parameters import TumorModelParameters, TherapyParameters
from create_therapy_schedule import create_therapy_schedule
DT, SUB = 1/24., 1/24./32.
rows = []
for pac, th, mp, T in [('P1', [TherapyParameters(146, 1655-176, 14)], TumorModelParameters(MED_tim=1e30), 1479),
                       ('P2', [TherapyParameters(14, 557, 21), TherapyParameters(557, 1104, 42)],
                        TumorModelParameters(MED_tim=1e30, MED_mas=143600, MED_dos=0.2), 1104)]:
    start, length = create_therapy_schedule(th)
    ms = MedicineSolver(mp, TimeTherapyEvaluator(start, length), DT, SUB); t = 0.0
    nominal = 6.022140857e23 * mp.MED_dos / (24 * mp.MED_mas)
    prev, prev_dose_level = 0.0, 0.0
    lvl = []
    for i in range(int(T / DT) + 48):
        ms.reassign(); ms.solve(t); t += DT; lvl.append((t, ms.MED))
    lvl = np.array(lvl)
    for s in start:
        a = lvl[(lvl[:, 0] > s - 0.5) & (lvl[:, 0] < s - 0.4)][-1, 1]
        b = lvl[(lvl[:, 0] > s + 0.4) & (lvl[:, 0] < s + 0.5)][-1, 1]
        rows.append((pac, s, (b - a) / nominal))
    c = Counter(round(r[2], 5) for r in rows if r[0] == pac)
    print(pac, 'n dosis', sum(c.values()), 'razon entregado/nominal ->', dict(c))
np.savetxt(sys.argv[2], np.array([(1 if p == 'P1' else 2, s, r) for p, s, r in rows]), delimiter=',',
           header='paciente,dia_inicio_dosis_sim,razon_dosis_entregada_nominal', comments='', fmt='%.8g')
