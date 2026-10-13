"""T01 · F1 · Farmacocinética, comparación CORREGIDA (tras el diagnóstico registrado en INFORME_T01 §PK):
solución exacta de la ec. 6 (superposición de infusiones rectangulares [s, s+1/24] con eliminación de primer orden)
evaluada en los MISMOS instantes que la serie del código original (data_derived/pk_check_*_serie.csv).
Criterio (sin cambios, contrato T01 §4.2): error relativo ≤ 0.1 %; se reporta max|código-exacto|/max(exacto)
y el error relativo puntual donde φ > 1 % del máximo.
Uso: python pk_check_trayectoria.py <salida_json>"""
import sys, json, math, numpy as np
NA = 6.022140857e23
def exact(t, starts, d, M, th, phi0, tau=1/24.):
    k, R = math.log(2)/th, NA*d/M
    y = phi0*np.exp(-k*t)
    for s in starts:
        u = np.clip(t - s, 0, None)
        y += (R/k)*(1 - np.exp(-k*np.minimum(u, tau)))*np.exp(-k*np.clip(u - tau, 0, None))
    return y
P1 = [146 + 14*i for i in range(200) if 146 + 14*i < 1655 - 176]
P2 = [14 + 21*i for i in range(200) if 14 + 21*i < 557] + [557 + 42*i for i in range(200) if 557 + 42*i < 1104]
out = {}
for name, f, st, d, M, th, p0 in [('P1_Q2W', 'data_derived/pk_check_P1_Q2W_serie.csv', P1, .24, 146000, 26.7, 0.),
                                  ('P2_Q3W_Q6W', 'data_derived/pk_check_P2_Q3W_serie.csv', P2, .20, 143600, 22., 6e16)]:
    t, y = np.loadtxt(f, delimiter=',', skiprows=1, unpack=True)
    e = exact(t, st, d, M, th, p0)
    m = e > 0.01*e.max()
    rec = {'n_puntos': int(len(t)), 'err_max_rel_al_maximo': float(np.max(np.abs(y-e))/e.max()),
           'err_rel_puntual_max(phi>1%max)': float(np.max(np.abs(y[m]-e[m])/e[m])),
           'err_rel_puntual_p99': float(np.percentile(np.abs(y[m]-e[m])/e[m], 99))}
    rec['cumple_0.1%'] = rec['err_rel_puntual_max(phi>1%max)'] <= 1e-3
    out[name] = rec; print(name, json.dumps(rec))
json.dump(out, open(sys.argv[1], 'w'), indent=1)
