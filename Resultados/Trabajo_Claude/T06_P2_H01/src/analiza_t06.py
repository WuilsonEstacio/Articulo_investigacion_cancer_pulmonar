"""T06 · Fase 2: análisis preespecificado (PREESPECIFICACION_T06.md §2–§3) del efecto de H01 en los 44 índices de P2.

Entradas: log original de T01 (P1 y P2 con el fallo), log de T06 (P2 corregido), control de determinismo
(data_derived/control_bug_comp1.json), Tabla 2 publicada transcrita (verificada 88/88 en T03), registros Q de la corrida
corregida (data_derived/q_corr/*.json) y muestreo de recursos (logs/docker_stats.csv, logs/docker_inspect_final.txt).
Salidas (data_derived/): t06_p2_indices.csv, t06_88_corregido.csv, t06_resumen.json; figura figures/fig_h01.(png|svg).
Uso (desde T06_P2_H01): python -I src/analiza_t06.py <log_T01> <log_T06> <tabla2_publicada.csv>
"""
import sys, re, ast, csv, json, glob, os
import numpy as np

log01, log06, pub_csv = sys.argv[1:4]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DD, FIG, LOGS = (os.path.join(ROOT, d) for d in ('data_derived', 'figures', 'logs'))
os.makedirs(FIG, exist_ok=True)

# alfa por defecto (verificados en T03 frente al código y a los 22 vectores del log)
ALPHA = {'P1': [52.5 * 6.87e-3, 15 * 0.7 * 0.499, 2.0, 0.1, 0.2, 5e-4, 5e-4, 2.0, 1e-5, 1.0, 4.0],
         'P2': [0.55 * 6.87e-3, 1.1 * 0.499, 1.0, 20.0, 0.2, 5e-4, 5e-4, 2.0, 1e-5, 1.0, 4.0]}
METRICAS = [('g_phiT', 'g_t'), ('g_phiP', 'g_p'), ('g_phiN', 'g_n'), ('g_Vvis', 'g_vt')]
P2_PK = {'MED_mas': 143600, 'MED_dos': 0.2, 'MED_tim': 22.0}


def listas(path, suf):
    txt = open(path, encoding='utf-8', errors='replace').read()
    out = {}
    for _, k in METRICAS:
        m = re.findall(re.escape(f'{k}_list_{suf}') + r' = (\[.*?\])', txt, flags=re.S)
        if not m:
            raise SystemExit(f'{k}_list_{suf} no está en {path}')
        v = [float(x) for x in ast.literal_eval(re.sub(r'\n\d\d:\d\d:\d\d ', ' ', m[-1]))]
        if len(v) != 11 or not all(np.isfinite(v)):
            raise SystemExit(f'{k}_list_{suf}: valores inválidos')
        out[k] = v
    return out


def tres_cifras(x):
    return f'{x:.2e}'


orig = {'P1': listas(log01, 'p1'), 'P2': listas(log01, 'p2')}
corr = listas(log06, 'p2')
pub = list(csv.DictReader(open(pub_csv, encoding='utf-8')))

# --- control de determinismo (componente 1 de P2 con el fallo) ---
ctrl = json.load(open(os.path.join(DD, 'control_bug_comp1.json')))
det = {}
for col, k in METRICAS:
    key = {'g_t': 'tumor', 'g_p': 'proliferative', 'g_n': 'necrotic', 'g_vt': 'tumor_visible'}[k]
    a, b = ctrl['g'][key], orig['P2'][k][ctrl['componente']]
    det[col] = {'control': a, 'log_T01': b, 'dif_rel': abs(a - b) / abs(b) if b != 0 else abs(a - b)}
det_ok = all(v['dif_rel'] <= 1e-8 for v in det.values())
pk_ctrl = {n: r['pk'] for n, r in ctrl['registros'].items()}

# --- registros Q de la corrida corregida ---
qs = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(DD, 'q_corr', '*.json')))]
q_check = {'n_simulaciones': len(qs),
           'pk_usado_siempre_P2': all(q['pk_usado'] == P2_PK for q in qs),
           'n_pk_antes_por_defecto': sum(q['pk_antes'] != P2_PK for q in qs),
           'n_pk_antes_P2': sum(q['pk_antes'] == P2_PK for q in qs),
           't_fin': sorted({q['t_fin'] for q in qs})}

# --- 44 índices de P2: original frente a corregido ---
filas = []
for r in pub:
    p, i = r['paciente'], int(r['indice_codigo'])
    for col, k in METRICAS:
        a = ALPHA[p][i]
        go = orig[p][k][i]
        gc = corr[k][i] if p == 'P2' else go
        gp = float(r[col])
        fila = {'paciente': p, 'parametro': r['parametro'], 'indice': col, 'alpha': a, 'g_publicado': gp,
                'rango_publicado': int(r['rango_' + col[2:]]), 'g_script_orig': go, 'g_script_corr': gc,
                'g_esc_orig': go * a / 100, 'g_esc_corr': gc * a / 100,
                'delta_rel': (gc - go) / abs(go) if p == 'P2' else 0.0,
                'err_pub_orig': abs(go * a / 100 - gp) / abs(gp), 'err_pub_corr': abs(gc * a / 100 - gp) / abs(gp),
                'igual3_orig': tres_cifras(go * a / 100) == tres_cifras(gp),
                'igual3_corr': tres_cifras(gc * a / 100) == tres_cifras(gp)}
        fila['cambio_signo'] = bool(np.sign(gc) != np.sign(go))
        filas.append(fila)
for p in ('P1', 'P2'):
    for col, _ in METRICAS:
        sub = [f for f in filas if f['paciente'] == p and f['indice'] == col]
        for etiqueta, clave in (('rango_orig', 'g_script_orig'), ('rango_corr', 'g_script_corr')):
            orden = np.argsort([-abs(f[clave] * f['alpha']) for f in sub], kind='stable')
            for rk, j in enumerate(orden, 1):
                sub[j][etiqueta] = rk
for f in filas:
    f['cambio_rango'] = f['rango_orig'] != f['rango_corr']

p2 = [f for f in filas if f['paciente'] == 'P2']
d = np.array([abs(f['delta_rel']) for f in p2])
n_signo, n_rango = sum(f['cambio_signo'] for f in p2), sum(f['cambio_rango'] for f in p2)
if d.max() <= 0.005 and n_signo == 0 and n_rango == 0:
    clase = 'despreciable'
elif d.max() <= 0.10 and n_signo == 0 and n_rango == 0:
    clase = 'menor'
else:
    clase = 'relevante'
peores = sorted(p2, key=lambda f: -abs(f['delta_rel']))[:8]


def acuerdo(fs, clave_err, clave_3):
    e = np.array([f[clave_err] for f in fs])
    return {'n': len(fs), 'le_10pct': int((e <= 0.10).sum()), 'igual_3_cifras': int(sum(f[clave_3] for f in fs)),
            'err_mediana': float(np.median(e)), 'err_max': float(e.max())}


# --- recursos del contenedor ---
rec = {}
sp = os.path.join(LOGS, 'docker_stats.csv')
if os.path.exists(sp):
    rows = list(csv.DictReader(open(sp, encoding='utf-8-sig')))
    mem = [float(re.match(r'([\d.]+)MiB', r['mem_usage']).group(1)) if 'MiB' in r['mem_usage'].split('/')[0]
           else float(re.match(r'([\d.]+)GiB', r['mem_usage']).group(1)) * 1024 for r in rows]
    cpu = [float(r['cpu_perc'].rstrip('%')) for r in rows]
    rec = {'muestras': len(rows), 'mem_pico_MiB': max(mem), 'mem_mediana_MiB': float(np.median(mem)),
           'mem_limite': rows[0]['mem_usage'].split('/')[1].strip(), 'cpu_media_pct': float(np.mean(cpu)),
           'cpu_max_pct': max(cpu), 'pids_max': max(int(r['pids']) for r in rows)}
ip = os.path.join(LOGS, 'docker_inspect_final.txt')
if os.path.exists(ip):
    rec['docker_inspect'] = open(ip, encoding='utf-8-sig').read().strip()

res = {'preespecificacion': 'PREESPECIFICACION_T06.md',
       'determinismo': {'componente': ctrl['componente'], 'por_metrica': det, 'criterio_1e-8_cumplido': det_ok,
                        'pk_en_control': pk_ctrl},
       'registros_q': q_check,
       'efecto_H01_P2': {'max_abs_delta_rel': float(d.max()), 'mediana_abs_delta_rel': float(np.median(d)),
                         'n_cambio_signo': int(n_signo), 'n_cambio_rango': int(n_rango), 'clase': clase,
                         'mayores': [{k: f[k] for k in ('parametro', 'indice', 'g_script_orig', 'g_script_corr', 'delta_rel',
                                                        'rango_orig', 'rango_corr')} for f in peores]},
       'acuerdo_con_tabla2': {'P2_original_esc': acuerdo(p2, 'err_pub_orig', 'igual3_orig'),
                              'P2_corregido_esc': acuerdo(p2, 'err_pub_corr', 'igual3_corr'),
                              '88_P1orig_P2corr_esc': acuerdo(filas, 'err_pub_corr', 'igual3_corr'),
                              'rangos_corr_coinciden_con_publicados': int(sum(f['rango_corr'] == f['rango_publicado'] for f in filas))},
       'recursos': rec}

campos = list(filas[0].keys())
with open(os.path.join(DD, 't06_88_corregido.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=campos); w.writeheader(); w.writerows(filas)
with open(os.path.join(DD, 't06_p2_indices.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=campos); w.writeheader(); w.writerows(p2)
json.dump(res, open(os.path.join(DD, 't06_resumen.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(json.dumps(res, indent=1, ensure_ascii=False))

# --- figura: cambio relativo por parámetro y métrica (P2) ---
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
INK, MUTED, GRID = '#0b0b0b', '#52514e', '#e6e5e0'
COLS = {'g_phiT': '#2a78d6', 'g_phiP': '#eb6834', 'g_phiN': '#1baf7a', 'g_Vvis': '#6250d6'}
ETQ = {'g_phiT': 'Q̄(φT)', 'g_phiP': 'Q̄(φP)', 'g_phiN': 'Q̄(φN)', 'g_Vvis': 'Q̄(Vvis)'}
plt.rcParams.update({'font.size': 9, 'axes.edgecolor': MUTED, 'axes.labelcolor': INK, 'xtick.color': MUTED,
                     'ytick.color': MUTED, 'axes.spines.top': False, 'axes.spines.right': False})
params = [r['parametro'] for r in pub if r['paciente'] == 'P2']
fig, ax = plt.subplots(figsize=(9, 4.2), constrained_layout=True)
x = np.arange(len(params))
for j, (col, _) in enumerate(METRICAS):
    y = [100 * next(f['delta_rel'] for f in p2 if f['parametro'] == pm and f['indice'] == col) for pm in params]
    ax.scatter(x + (j - 1.5) * 0.18, y, s=28, color=COLS[col], edgecolor='white', lw=0.6, label=ETQ[col], zorder=3)
ax.axhline(0, color=MUTED, lw=0.8)
for lim in (0.5, -0.5):
    ax.axhline(lim, color=MUTED, lw=0.6, ls=(0, (3, 3)))
ax.set_xticks(x, params, rotation=35, ha='right')
ax.set_ylabel('Cambio relativo de g en P2 tras corregir H01 (%)')
ax.set_title(f'P2: efecto de H01 en los 44 índices (clase preespecificada: {clase}; líneas: ±0,5 %)', loc='left',
             color=INK, fontsize=10)
ax.grid(axis='y', color=GRID, lw=0.5)
ax.legend(frameon=False, ncol=4, loc='best')
for ext in ('png', 'svg'):
    fig.savefig(os.path.join(FIG, f'fig_h01.{ext}'), dpi=200)
