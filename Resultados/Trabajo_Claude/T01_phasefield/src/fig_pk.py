"""T01 · F1 · Figura PK: φ_τ del MedicineSolver ORIGINAL (serie guardada por pk_check.py) frente a la solución
exacta de la ec. 6 (pk_check_trayectoria.exact), por paciente. Fila 1: trayectoria completa; fila 2: zoom en una
infusión del estado periódico; fila 3: error relativo puntual (φ > 1 % del máximo) con la tolerancia del contrato (0,1 %).
Uso (desde T01_phasefield): python src/fig_pk.py figures/fig_pk"""
import sys, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
src = open('src/pk_check_trayectoria.py', encoding='utf-8').read()
exec(src.split('out = {}')[0].split('import sys, json, math, numpy as np')[1].replace('NA =', 'import math\nNA ='))
C_CODE, C_EXACT, INK, MUTED = '#2a78d6', '#eb6834', '#0b0b0b', '#52514e'
cases = [('Paciente 1 (Q2W, 0,24 g)', 'data_derived/pk_check_P1_Q2W_serie.csv', P1, .24, 146000, 26.7, 0., None),
         ('Paciente 2 (Q3W → Q6W, 0,20 g)', 'data_derived/pk_check_P2_Q3W_serie.csv', P2, .20, 143600, 22., 6e16, None)]
plt.rcParams.update({'font.size': 9, 'axes.edgecolor': MUTED, 'axes.labelcolor': INK, 'xtick.color': MUTED,
                     'ytick.color': MUTED, 'axes.spines.top': False, 'axes.spines.right': False})
fig, ax = plt.subplots(3, 2, figsize=(10, 8.2), constrained_layout=True)
for j, (title, f, st, d, M, th, p0, zoom) in enumerate(cases):
    t, y = np.loadtxt(f, delimiter=',', skiprows=1, unpack=True)
    e = exact(t, st, d, M, th, p0)
    kk = e > 0.01 * e.max()
    tmax = t[kk][np.argmax(np.abs(y[kk] - e[kk]) / e[kk])]
    zoom = max(s for s in st if s <= tmax + 1e-9)  # dosis con el mayor error puntual
    a = ax[0, j]
    a.plot(t, y / 1e16, color=C_CODE, lw=1.2, label='Código original (MedicineSolver)')
    a.plot(t, e / 1e16, color=C_EXACT, lw=1.0, ls=(0, (4, 3)), label='Solución exacta ec. 6')
    a.set_title(title, loc='left', color=INK, fontsize=10)
    a.set_ylabel('φ_τ (×10¹⁶ moléculas)')
    a.set_xlabel('Tiempo de simulación (días)')
    a.grid(axis='y', color='#e6e5e0', lw=0.6)
    if j == 0:
        a.legend(frameon=False, loc='lower right')
    b = ax[1, j]
    m = (t >= zoom - 0.25) & (t <= zoom + 0.6)
    b.plot(t[m], y[m] / 1e16, color=C_CODE, lw=1.6, marker='o', ms=3.5, label='Código original')
    tf = np.linspace(zoom - 0.25, zoom + 0.6, 2000)
    b.plot(tf, exact(tf, st, d, M, th, p0) / 1e16, color=C_EXACT, lw=1.2, ls=(0, (4, 3)), label='Exacta (continua)')
    b.axvspan(zoom, zoom + 1 / 24, color='#f0efec', zorder=0)
    b.annotate('infusión 1/24 d', xy=(zoom + 1 / 48, b.get_ylim()[0]), xytext=(4, 6), textcoords='offset points',
               color=MUTED, fontsize=8)
    b.set_title(f'Zoom: dosis del día {zoom:g}, la de mayor error (muestreo dt = 1/24 d)', loc='left', color=INK, fontsize=9)
    b.set_ylabel('φ_τ (×10¹⁶)')
    b.set_xlabel('Tiempo de simulación (días)')
    c = ax[2, j]
    k = e > 0.01 * e.max()
    r = np.abs(y[k] - e[k]) / e[k] * 100
    c.semilogy(t[k], np.maximum(r, 1e-6), color=C_CODE, lw=0.6)
    c.axhline(0.1, color=INK, lw=0.8, ls=':')
    c.text(t[k][0], 0.13, 'tolerancia 0,1 %', color=INK, fontsize=8)
    c.set_ylabel('|error relativo| (%)')
    c.set_xlabel('Tiempo de simulación (días)')
    c.set_title(f'Error puntual: p99 = {np.percentile(r, 99):.1e} %, máx = {r.max():.2f} %', loc='left', color=INK, fontsize=9)
fig.text(0.01, -0.01, 'Fuente: código de Wagner et al. (MBE 2023), commit fa8e6229, sin modificar; ec. 6 resuelta '
         'analíticamente por superposición de infusiones rectangulares. Los errores > 0,1 % se concentran en los bordes '
         'de infusión (ver INFORME_T01 §3).', fontsize=7.5, color=MUTED)
for ext in ('png', 'svg'):
    fig.savefig(f'{sys.argv[1]}.{ext}', dpi=200, bbox_inches='tight', metadata={'Date': None} if ext == 'svg' else None)
print('ok')
