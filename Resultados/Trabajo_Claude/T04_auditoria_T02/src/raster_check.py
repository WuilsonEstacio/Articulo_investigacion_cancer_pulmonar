"""T04 (Claude): extracción ráster independiente de Fig 1A (p6) y 2A (p8) y comparación con los puntos de Cline."""
import sys, json, pymupdf, numpy as np, pandas as pd
pdf, cline_dd, out = sys.argv[1], sys.argv[2], sys.argv[3]
COL = {'durvalumab': (0.89, 0.62, 0.25), 'placebo': (0.36, 0.53, 0.77)}
# calibración por marcas de tick vectoriales (centros), obtenidas con ticks.py
CAL = {6: dict(x0=85.24, x63=345.45, y100=77.08, y0=191.10), 8: dict(x0=85.24, x63=345.45, y100=76.33, y0=190.35)}
Z = 16  # px por pt
doc = pymupdf.open(pdf)
res = {}
for ep, p in (('SG', 6), ('SLP', 8)):
    c = CAL[p]
    clip = pymupdf.Rect(c['x0'] + 0.6, c['y100'] - 4, c['x63'] + 1, c['y0'] - 0.6)
    pix = doc[p-1].get_pixmap(matrix=pymupdf.Matrix(Z, Z), clip=clip, alpha=False)
    img = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width, 3) / 255.
    for arm, rgb in COL.items():
        m = np.linalg.norm(img - np.array(rgb), axis=2) < 0.12
        prev = (c['y100'] - clip.y0) * Z
        ys = np.full(pix.width, np.nan)
        for j in range(pix.width):
            idx = np.flatnonzero(m[:, j])
            if idx.size == 0:
                continue
            runs = np.split(idx, np.flatnonzero(np.diff(idx) > 1) + 1)
            centers = np.array([(r[0] + r[-1]) / 2 for r in runs])
            k = np.argmin(abs(centers - prev))
            if abs(centers[k] - prev) > 8 * Z:   # salto implausible (texto) -> ignorar
                continue
            ys[j] = prev = centers[k]
        x_pt = clip.x0 + (np.arange(pix.width) + 0.5) / Z
        y_pt = clip.y0 + ys / Z
        t = (x_pt - c['x0']) / (c['x63'] - c['x0']) * 63
        S = (c['y0'] - y_pt) / (c['y0'] - c['y100'])
        ok = ~np.isnan(S)
        t, S = t[ok], S[ok]
        cl = pd.read_csv(f"{cline_dd}/points_{ep}_{arm}.csv")
        end = cl.time_months.iloc[-1]
        sel = t <= end
        t, S = t[sel], S[sel]
        ix = np.searchsorted(cl.time_months.values, t, side='right') - 1
        Scl = cl.survival.values[np.maximum(ix, 0)]
        d = S - Scl
        # excluir ±0,15 meses alrededor de cada salto de Cline (columna vertical del escalón)
        jumps = cl.time_months.values[1:]
        far = np.min(abs(t[:, None] - jumps[None, :]), axis=1) > 0.15
        mil = {}
        for tm in ((24, 36) if ep == 'SG' else (18, 24)):
            w = abs(t - tm) < 0.05
            mil[f"S_{tm}"] = dict(raster=float(np.median(S[w])), cline=float(cl.survival.values[np.searchsorted(cl.time_months.values, tm, side='right') - 1]))
        res[f"{ep}_{arm}"] = dict(n_cols=int(sel.sum()), n_cols_far=int(far.sum()), coverage=float(sel.sum() / max(1, (t.max()-0) * Z * 4.13)),
            abs_diff_pp_median=float(np.median(abs(d[far])) * 100), abs_diff_pp_p95=float(np.quantile(abs(d[far]), .95) * 100),
            abs_diff_pp_max=float(abs(d[far]).max() * 100), frac_within_0p5pp=float(np.mean(abs(d[far]) < 0.005)), milestones=mil, S0_raster=float(np.median(S[t < 0.5])))
        pd.DataFrame(dict(time_months=t, S_raster=S, S_cline=Scl, far_from_jump=far)).to_csv(f"{out}/raster_vs_cline_{ep}_{arm}.csv", index=False)
print(json.dumps(res, indent=1))
json.dump(res, open(f"{out}/raster_vs_cline_resumen.json", 'w'), indent=1)
