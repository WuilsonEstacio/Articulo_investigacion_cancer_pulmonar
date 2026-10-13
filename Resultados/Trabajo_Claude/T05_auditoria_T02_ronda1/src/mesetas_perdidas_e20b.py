"""T05: en las réplicas E2.0b con una meseta menos que la verdad, mide el hueco temporal más corto entre tiempos de
evento consecutivos de la curva verdadera, en meses y en pt del PDF (escala de la Fig. 1A: 63 meses = 260,21 pt).
Uso: python -I mesetas_perdidas_e20b.py <data_derived de T02> <salida.csv>"""
import sys, numpy as np, pandas as pd
dd, out = sys.argv[1], sys.argv[2]
PT_PER_MONTH = (345.45 - 85.24) / 63
pop = pd.read_csv(f"{dd}/simulation_b_populations.csv")
rows = []
for r in pop.itertuples():
    tr = pd.read_csv(f"{dd}/simulation_b/{r.replicate:03d}_{r.endpoint}/truth_{r.arm}.csv")
    tcol = [c for c in tr.columns if 'time' in c][0]; ecol = [c for c in tr.columns if 'event' in c][0]
    et = np.unique(tr.loc[tr[ecol] == 1, tcol].values)
    gaps = np.diff(et)
    g = float(gaps.min()) if gaps.size else np.nan
    rows.append(dict(replicate=r.replicate, endpoint=r.endpoint, arm=r.arm, plateaus=r.plateaus, true_plateaus=r.true_plateaus,
                     perdida=int(r.true_plateaus - r.plateaus), min_gap_months=g, min_gap_pt=g * PT_PER_MONTH))
d = pd.DataFrame(rows); d.to_csv(out, index=False)
pd.set_option('display.width', 200)
print(d[d.perdida != 0].to_string(index=False))
ok = d[d.perdida == 0]
print('curvas sin pérdida:', len(ok), ' min_gap_pt mínimo entre ellas:', ok.min_gap_pt.min())
print('curvas sin pérdida con min_gap_pt < 0,002:', int((ok.min_gap_pt < 0.002).sum()))
