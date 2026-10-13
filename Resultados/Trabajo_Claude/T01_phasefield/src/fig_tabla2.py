"""T01 · F1 · Figura Tabla 2: g reproducido frente a g publicado (88 valores, 2 pacientes × 11 parámetros × 4 métricas).
Panel A (criterio primario): salida directa del script original. Panel B (solo diagnóstico): g_script·α/100 (ec. 4.1).
Ejes log de |g|; marcador relleno = mismo signo que la Tabla 2, hueco = signo opuesto.
Uso (desde T01_phasefield): python src/fig_tabla2.py data_derived/tabla2_diag_escala.csv figures/fig_tabla2"""
import sys, csv, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

rows = list(csv.DictReader(open(sys.argv[1], encoding='utf-8')))
out = sys.argv[2]
INK, MUTED, GRID = '#0b0b0b', '#52514e', '#e6e5e0'
COL = {'P1': '#2a78d6', 'P2': '#eb6834'}
MK = {'P1': 'o', 'P2': 's'}
plt.rcParams.update({'font.size': 9, 'axes.edgecolor': MUTED, 'axes.labelcolor': INK, 'xtick.color': MUTED,
                     'ytick.color': MUTED, 'axes.spines.top': False, 'axes.spines.right': False})
fig, ax = plt.subplots(1, 2, figsize=(10, 4.6), constrained_layout=True)
panels = [('g_script', 'A · Criterio primario: salida directa del script', '|g| del script original (sin escalar)'),
          ('g_escalado', 'B · Diagnóstico (no criterio): g del script × α / 100', '|g del script × α / 100|')]
for a, (key, title, ylab) in zip(ax, panels):
    allv = []
    for p in ['P1', 'P2']:
        sub = [x for x in rows if x['paciente'] == p]
        ref = np.array([float(x['g_publicado']) for x in sub]); g = np.array([float(x[key]) for x in sub])
        same = np.sign(ref) == np.sign(g)
        allv += list(np.abs(ref)) + list(np.abs(g))
        a.scatter(np.abs(ref[same]), np.abs(g[same]), s=26, marker=MK[p], color=COL[p], edgecolor='white', lw=0.6, zorder=3)
        a.scatter(np.abs(ref[~same]), np.abs(g[~same]), s=26, marker=MK[p], facecolor='none', edgecolor=COL[p], lw=1.2, zorder=3)
    lo, hi = min(allv) / 2, max(allv) * 2
    xr = np.array([1e-4 / 2, 0.4])
    a.plot(xr, xr, color=MUTED, lw=1, zorder=2)
    a.fill_between(xr, xr * 0.9, xr * 1.1, color=GRID, zorder=1, lw=0)
    a.set_xscale('log'); a.set_yscale('log')
    a.set_xlim(*xr); a.set_ylim(lo if key == 'g_script' else xr[0], hi if key == 'g_script' else xr[1])
    a.set_xlabel('|g| publicado (Tabla 2, MBE 2023)'); a.set_ylabel(ylab)
    a.set_title(title, loc='left', color=INK, fontsize=10)
    a.grid(color=GRID, lw=0.5)
ax[0].text(0.03, 0.97, '0 de 88 reproducidos (≤ 10 %)\nH1 no se cumple', transform=ax[0].transAxes, va='top', color=INK, fontsize=9)
ax[1].text(0.03, 0.97, '88 de 88 ≤ 10 %; error máx. 0,45 %\nsignos y rangos 88/88', transform=ax[1].transAxes, va='top', color=INK, fontsize=9)
leg = [Line2D([], [], ls='', marker='o', color=COL['P1'], label='Paciente 1'),
       Line2D([], [], ls='', marker='s', color=COL['P2'], label='Paciente 2'),
       Line2D([], [], ls='', marker='o', mfc='none', mec=MUTED, label='signo opuesto'),
       Line2D([], [], color=MUTED, lw=1, label='identidad (banda ±10 %)')]
ax[1].legend(handles=leg, frameon=False, loc='lower right')
for ext in ('png', 'svg'):
    fig.savefig(f'{out}.{ext}', dpi=200)
print('ok', out)
