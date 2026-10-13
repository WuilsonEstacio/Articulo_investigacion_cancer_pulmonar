"""T01 · diagnóstico (no criterio): dosis efectiva por administración en el MedicineSolver ORIGINAL.
Se anula la eliminación (t½ = 1e30) y se simula 1 dosis aislada; se compara el incremento con N_A·d/(24·M).
Uso: python pk_diagnostico_dosis.py <ruta_reduced_models>"""
import sys, numpy as np
sys.path.insert(0, sys.argv[1])
from medicine_solver import MedicineSolver
from time_therapy_evaluator import TimeTherapyEvaluator
from parameters import TumorModelParameters
DT, SUB = 1/24., 1/24./32.
mp = TumorModelParameters(MED_tim=1e30)
tt = TimeTherapyEvaluator(start=[5.0], length=[1/24.])
ms = MedicineSolver(mp, tt, DT, SUB); t = 0.0
traj = []
for i in range(int(7/DT)):
    ms.reassign(); ms.solve(t); t += DT; traj.append((t, ms.MED))
nominal = 6.022140857e23 * mp.MED_dos / (24 * mp.MED_mas)
inc = traj[-1][1]
print(f'nominal={nominal:.6e} entregado={inc:.6e} razon={inc/nominal:.6f} (33/32={33/32:.6f})')
for tt_, m in traj:
    if 4.9 < tt_ < 5.15: print(f'  t={tt_:.5f}  phi={m:.6e}  frac={m/nominal:.5f}')
