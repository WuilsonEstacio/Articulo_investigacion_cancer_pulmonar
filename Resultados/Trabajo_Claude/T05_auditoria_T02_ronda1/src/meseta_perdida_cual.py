"""T05: identifica qué nivel del KM verdadero falta en la extracción E2.0b de cada curva discordante y mide la anchura
de su meseta (tiempo hasta el siguiente evento) en meses y en pt (63 meses = 260,21 pt).
Uso: python -I meseta_perdida_cual.py <data_derived de T02> <salida.csv>"""
import sys, numpy as np, pandas as pd
dd, out = sys.argv[1], sys.argv[2]
PT = (345.45 - 85.24) / 63
pop = pd.read_csv(f"{dd}/simulation_b_populations.csv")
pop = pop[pop.plateaus != pop.true_plateaus]
rows = []
for r in pop.itertuples():
    base = f"{dd}/simulation_b/{r.replicate:03d}_{r.endpoint}"
    tr = pd.read_csv(f"{base}/truth_{r.arm}.csv").sort_values('time_months')
    t, e = tr.time_months.values, tr.event.values
    ut = np.unique(t[e == 1]); S = 1.0; lv = [1.0]
    for u in ut:
        S *= 1 - ((t == u) & (e == 1)).sum() / (t >= u).sum(); lv.append(S)
    lv = np.array(lv)                                   # nivel k vale desde ut[k-1] hasta ut[k]
    starts = np.r_[0.0, ut]; ends = np.r_[ut, t.max()]
    ext = pd.read_csv(f"{base}/points_{r.endpoint}_{r.arm}.csv")
    ext = ext[ext.kind == 'plateau'].survival.values
    # nivel verdadero sin ningún nivel extraído a menos de 1e-6
    falta = [k for k in range(len(lv)) if np.min(np.abs(ext - lv[k])) > 1e-6]
    for k in falta:
        w = ends[k] - starts[k]
        rows.append(dict(replicate=r.replicate, endpoint=r.endpoint, arm=r.arm, nivel=k, S=lv[k], t_inicio=starts[k],
                         anchura_meses=w, anchura_pt=w * PT, bajo_margen_0p002pt=bool(w * PT < 0.002)))
d = pd.DataFrame(rows); d.to_csv(out, index=False)
pd.set_option('display.width', 200); print(d.to_string(index=False))
