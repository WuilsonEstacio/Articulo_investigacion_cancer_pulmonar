"""T01 · diagnóstico: ubicación temporal de los mayores errores relativos PK (código original frente a solución exacta).
Clasifica cada punto como 'en ventana de infusión' (s <= t <= s+1/24 + 1e-9) o 'fuera'. Uso: python pk_localiza_error.py"""
import math, numpy as np, json
exec(open('src/pk_check_trayectoria.py', encoding='utf-8').read().split("out = {}")[0].split('import sys, json, math, numpy as np')[1])
res = {}
for name, f, st, d, M, th, p0 in [('P1', 'data_derived/pk_check_P1_Q2W_serie.csv', P1, .24, 146000, 26.7, 0.),
                                  ('P2', 'data_derived/pk_check_P2_Q3W_serie.csv', P2, .20, 143600, 22., 6e16)]:
    t, y = np.loadtxt(f, delimiter=',', skiprows=1, unpack=True)
    e = exact(t, st, d, M, th, p0); m = e > 0.01*e.max()
    r = np.where(m, np.abs(y-e)/np.where(e > 0, e, 1), 0)
    inwin = np.zeros_like(t, bool)
    for s in st: inwin |= (t >= s - 1e-9) & (t <= s + 1/24 + 1e-9)
    res[name] = {'max_rel_en_ventana': float(r[inwin & m].max()), 'max_rel_fuera_ventana': float(r[~inwin & m].max()),
                 'n_puntos_ventana': int((inwin & m).sum()), 'top5_t': [round(float(x), 5) for x in t[np.argsort(r)[-5:]]]}
    print(name, json.dumps(res[name]))
json.dump(res, open('data_derived/pk_localizacion_error.json', 'w'), indent=1)
