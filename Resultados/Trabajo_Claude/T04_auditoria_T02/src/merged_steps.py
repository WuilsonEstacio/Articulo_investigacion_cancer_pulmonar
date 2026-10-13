"""Detecta saltos de Cline que agrupan varios escalones del polígono vectorial.
Para cada salto (entre mesetas consecutivas), cuenta niveles horizontales distintos del polígono
dentro de la franja x del salto y y estrictamente entre ambas mesetas."""
import sys, numpy as np, pandas as pd
dd = sys.argv[1]
W = 0.502
rows = []
for ep in ('SG', 'SLP'):
    for arm in ('durvalumab', 'placebo'):
        seg = pd.read_csv(f"{dd}/segments_{ep}_{arm}.csv")
        h = seg[(seg.y1 - seg.y2).abs() < 1e-6]
        pts = pd.read_csv(f"{dd}/points_{ep}_{arm}.csv")
        pts = pts[pts.kind == 'plateau'].reset_index(drop=True)
        ipd = pd.read_csv(f"{dd}/pseudo_ipd_{ep}_{arm}.csv")
        ev = ipd[ipd.event == 1].groupby('time_months').size()
        for k in range(1, len(pts)):
            y_hi, y_lo = pts.y_pdf[k-1], pts.y_pdf[k]   # PDF y crece hacia abajo
            x_jump = pts.x_pdf[k]
            lo_x, hi_x = x_jump - 2, x_jump + 2
            cand = h[(np.minimum(h.x1, h.x2) < hi_x) & (np.maximum(h.x1, h.x2) > lo_x) &
                     (h.y1 > y_hi + W * 0.75) & (h.y1 < y_lo - W * 0.75)]
            # niveles intermedios: bordes horizontales agrupados a 0.1 pt
            lv = np.unique(np.round(cand.y1.values / 0.1) * 0.1)
            if len(lv):
                n_ev = int(ev.get(pts.time_months[k], 0))
                rows.append(dict(endpoint=ep, arm=arm, jump_time=pts.time_months[k], S_before=pts.survival[k-1], S_after=pts.survival[k],
                                 drop_pp=100*(pts.survival[k-1]-pts.survival[k]), intermediate_edge_levels=len(lv), tied_events_at_jump=n_ev))
r = pd.DataFrame(rows)
pd.set_option('display.width', 200)
print(r.to_string(index=False))
r.to_csv(f"{sys.argv[2]}/saltos_fusionados.csv", index=False)
for ep in ('SG','SLP'):
    for arm in ('durvalumab','placebo'):
        ipd = pd.read_csv(f"{dd}/pseudo_ipd_{ep}_{arm}.csv"); ev = ipd[ipd.event==1].groupby('time_months').size()
        print(ep, arm, 'eventos', int(ev.sum()), 'tiempos distintos', len(ev), 'max empate', int(ev.max()), 'empates>=5:', ev[ev>=5].round(2).to_dict())
