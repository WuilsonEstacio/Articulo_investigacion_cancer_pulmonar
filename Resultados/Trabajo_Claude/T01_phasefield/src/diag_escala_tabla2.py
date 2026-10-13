"""T01 · F1, DIAGNÓSTICO (no criterio): aplica la misma clasificación del contrato a g_script * alpha / 100 (ec. 4.1 del artículo)
para explicar la discrepancia del criterio primario. No sustituye a la clasificación primaria de compare_tabla2.py.
Uso: python diag_escala_tabla2.py <prefijo>_comparacion.csv <salida_prefijo>
"""
import sys, csv, json
from collections import Counter
import numpy as np

inp, outp = sys.argv[1], sys.argv[2]
rows = list(csv.DictReader(open(inp, encoding='utf-8')))
for x in rows:
    ref = float(x['g_publicado']); g = float(x['g_script']) * float(x['alpha_defecto']) / 100
    x['g_escalado'] = g
    e = abs(g - ref) / abs(ref); same = np.sign(g) == np.sign(ref)
    x['err_rel_escalado'] = e
    x['clasif_escalado'] = 'reproducido' if same and e <= 0.10 else ('parcialmente reproducido' if same and e <= 0.50 else 'discrepancia')
# rangos con el valor escalado (|g| descendente por paciente y métrica)
for p in ['P1', 'P2']:
    for m in ['g_phiT', 'g_phiP', 'g_phiN', 'g_Vvis']:
        sub = [x for x in rows if x['paciente'] == p and x['indice'] == m]
        for rk, j in enumerate(np.argsort([-abs(x['g_escalado']) for x in sub]), 1):
            sub[j]['rango_escalado'] = rk
for x in rows:
    x['rango_escalado_coincide'] = int(x['rango_publicado']) == x['rango_escalado']
with open(outp + '_diag_escala.csv', 'w', newline='', encoding='utf-8') as f:
    keys = ['paciente', 'parametro', 'indice', 'g_publicado', 'g_script', 'alpha_defecto', 'g_escalado', 'err_rel_escalado', 'clasif_escalado',
            'rango_publicado', 'rango_escalado', 'rango_escalado_coincide']
    w = csv.DictWriter(f, fieldnames=keys, extrasaction='ignore'); w.writeheader(); w.writerows(rows)
e = np.array([x['err_rel_escalado'] for x in rows])
cnt = Counter(x['clasif_escalado'] for x in rows)
peor = sorted(rows, key=lambda x: -x['err_rel_escalado'])[:5]
summ = {'nota': 'DIAGNÓSTICO, no criterio: g_script*alpha/100 frente a la Tabla 2',
        'n': len(rows), 'conteo': dict(cnt), 'signo_coincide': int(sum(np.sign(x['g_escalado']) == np.sign(float(x['g_publicado'])) for x in rows)),
        'rangos_coinciden': int(sum(x['rango_escalado_coincide'] for x in rows)),
        'err_rel_mediana': float(np.median(e)), 'err_rel_p90': float(np.percentile(e, 90)), 'err_rel_max': float(e.max()),
        'n_err_le_1pct': int((e <= 0.01).sum()), 'n_err_le_5pct': int((e <= 0.05).sum()),
        'peores_5': [{k: x[k] for k in ['paciente', 'parametro', 'indice', 'g_publicado', 'g_escalado', 'err_rel_escalado']} for x in peor]}
json.dump(summ, open(outp + '_diag_escala_resumen.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(json.dumps(summ, indent=1, ensure_ascii=False))
