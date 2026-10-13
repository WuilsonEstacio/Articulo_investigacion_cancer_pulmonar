"""T01 · F1: compara la salida del script ORIGINAL local_sensitivity_analysis.py con la Tabla 2 publicada (MBE 2023, p. 17).

Criterio PRIMARIO (contrato T01 §4.1, fijado antes de ejecutar): salida directa del script (g_*_list_p1/p2) frente a la Tabla 2.
  reproducido: error relativo <= 10 % y mismo signo; parcial: 10-50 % y mismo signo; discrepancia: > 50 % o signo opuesto.
  Global: H1 si >= 80 % de los 88 valores están 'reproducido'. Se compara además el orden de rangos (por |g| en cada columna).
DIAGNÓSTICO (no criterio): si hubiera diferencias sistemáticas de escala, se evalúan las transformaciones implicadas por la
  ec. 4.1 (g_art = g_script * alpha / 100 y g_art = g_script * alpha), solo para explicar la discrepancia.
Uso: python compare_tabla2.py <log_del_script> <tabla2_publicada.csv> <salida_prefijo>
"""
import sys, re, csv, json, ast
import numpy as np

log, pub_csv, outp = sys.argv[1], sys.argv[2], sys.argv[3]
txt = open(log, encoding='utf-8', errors='replace').read()
lists = {}
for key in ['g_t_list_p1', 'g_p_list_p1', 'g_n_list_p1', 'g_vt_list_p1', 'g_t_list_p2', 'g_p_list_p2', 'g_n_list_p2', 'g_vt_list_p2']:
    m = re.findall(re.escape(key) + r' = (\[.*?\])', txt)
    if not m:
        raise SystemExit(f'No se encontró {key} en el log')
    # se conservan posiciones; nan/inf -> None ('no evaluable')
    raw = re.sub(r'\b(nan|inf|-inf)\b', 'None', m[-1])
    raw = re.sub(r'np\.float64\(([^)]*)\)', r'\1', raw)
    lists[key] = [None if v is None else float(v) for v in ast.literal_eval(raw)]
    if len(lists[key]) != 11:
        raise SystemExit(f'{key}: se esperaban 11 valores, hay {len(lists[key])}')

# valores por defecto (alpha) usados por el script original (local_sensitivity_analysis.py + parameters.py)
ALPHA = {'P1': [52.5 * 6.87e-3, 15 * 0.7 * 0.499, 2.0, 0.1, 0.2, 5e-4, 5e-4, 2.0, 1e-5, 1.0, 4.0],
         'P2': [0.55 * 6.87e-3, 1.1 * 0.499, 1.0, 20.0, 0.2, 5e-4, 5e-4, 2.0, 1e-5, 1.0, 4.0]}
cols = [('g_phiT', 'g_t'), ('g_phiP', 'g_p'), ('g_phiN', 'g_n'), ('g_Vvis', 'g_vt')]
pub = list(csv.DictReader(open(pub_csv, encoding='utf-8')))


def clasif(rep, ref):
    if rep is None or not np.isfinite(rep):
        return 'no evaluable', None
    e = abs(rep - ref) / abs(ref)
    same = np.sign(rep) == np.sign(ref)
    if same and e <= 0.10:
        return 'reproducido', e
    if same and e <= 0.50:
        return 'parcialmente reproducido', e
    return 'discrepancia', e


rows, ranks = [], {}
for r in pub:
    p = r['paciente']; i = int(r['indice_codigo']); suf = p.lower()
    for ccsv, cl in cols:
        rep = lists[f'{cl}_list_{suf}'][i]
        ref = float(r[ccsv])
        c, e = clasif(rep, ref)
        a = ALPHA[p][i]
        rows.append({'paciente': p, 'parametro': r['parametro'], 'indice': ccsv, 'g_publicado': ref, 'rango_publicado': int(r['rango_' + ccsv[2:]]),
                     'g_script': rep, 'err_rel': e, 'clasificacion': c, 'alpha_defecto': a,
                     'diag_err_rel_si_g_x_alpha_div_100': None if rep is None else abs(rep * a / 100 - ref) / abs(ref),
                     'diag_err_rel_si_g_x_alpha': None if rep is None else abs(rep * a - ref) / abs(ref)})
# orden de rangos reproducido por columna (|g| descendente, 1 = mayor), igual que la tabla
for p in ['P1', 'P2']:
    for ccsv, _ in cols:
        sub = [x for x in rows if x['paciente'] == p and x['indice'] == ccsv]
        order = np.argsort([-(abs(x['g_script']) if x['g_script'] is not None else -1) for x in sub])
        for rk, j in enumerate(order, 1):
            sub[j]['rango_reproducido'] = rk
for x in rows:
    x['rango_coincide'] = x['rango_publicado'] == x.get('rango_reproducido')

with open(outp + '_comparacion.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
from collections import Counter
cnt = Counter(x['clasificacion'] for x in rows)
summ = {'n': len(rows), 'conteo': dict(cnt), 'fraccion_reproducido': cnt['reproducido'] / len(rows),
        'H1_cumple(>=80%)': cnt['reproducido'] / len(rows) >= 0.8,
        'rangos_coinciden': sum(x['rango_coincide'] for x in rows),
        'err_rel_mediana': float(np.median([x['err_rel'] for x in rows if x['err_rel'] is not None])),
        'err_rel_p90': float(np.percentile([x['err_rel'] for x in rows if x['err_rel'] is not None], 90)),
        'err_rel_max': float(max(x['err_rel'] for x in rows if x['err_rel'] is not None)),
        'diag_mediana_err_si_x_alpha_div_100': float(np.median([x['diag_err_rel_si_g_x_alpha_div_100'] for x in rows if x['g_script'] is not None])),
        'diag_mediana_err_si_x_alpha': float(np.median([x['diag_err_rel_si_g_x_alpha'] for x in rows if x['g_script'] is not None]))}
for p in ['P1', 'P2']:
    c2 = Counter(x['clasificacion'] for x in rows if x['paciente'] == p)
    summ[f'conteo_{p}'] = dict(c2)
json.dump(summ, open(outp + '_resumen.json', 'w'), indent=1)
print(json.dumps(summ, indent=1))
