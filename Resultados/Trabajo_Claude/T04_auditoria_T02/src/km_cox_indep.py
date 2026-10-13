"""KM y Cox (Efron y Breslow) propios, sin lifelines, sobre los pseudo-IPD de T02."""
import sys, json, numpy as np, pandas as pd
from scipy.optimize import minimize_scalar
dd = sys.argv[1]
def km(t, e):
    ut = np.unique(t[e == 1]); S = 1.0; out = []
    for u in ut:
        n = (t >= u).sum(); d = ((t == u) & (e == 1)).sum(); S *= 1 - d / n; out.append((u, S))
    return np.array(out)
def S_at(k, x): i = np.searchsorted(k[:, 0], x, side='right') - 1; return 1.0 if i < 0 else k[i, 1]
def median(k): i = np.flatnonzero(k[:, 1] <= 0.5); return float(k[i[0], 0]) if i.size else float('inf')
def cox(t, e, z, ties):
    ut = np.unique(t[e == 1])
    def nll(b):
        ll = 0.0
        for u in ut:
            D = (t == u) & (e == 1); R = t >= u; d = D.sum()
            sR = np.exp(b * z[R]).sum(); sD = np.exp(b * z[D]).sum()
            ll += b * z[D].sum()
            if ties == 'breslow': ll -= d * np.log(sR)
            else: ll -= sum(np.log(sR - l / d * sD) for l in range(d))
        return -ll
    return float(np.exp(minimize_scalar(nll, bounds=(-3, 3), method='bounded', options={'xatol': 1e-10}).x))
res = {}
for ep, ms in (('SG', (24, 36)), ('SLP', (18, 24))):
    data = {}
    for arm in ('durvalumab', 'placebo'):
        d = pd.read_csv(f"{dd}/pseudo_ipd_{ep}_{arm}.csv"); t, e = d.time_months.values, d.event.values; data[arm] = (t, e)
        k = km(t, e)
        res[f"{ep}_{arm}"] = dict(n=len(t), events=int(e.sum()), median=median(k), **{f"S_{m}": S_at(k, m) for m in ms},
                                  at_risk=[int((t >= x).sum()) for x in range(0, 64, 3)])
    t = np.r_[data['durvalumab'][0], data['placebo'][0]]; e = np.r_[data['durvalumab'][1], data['placebo'][1]]
    z = np.r_[np.ones(len(data['durvalumab'][0])), np.zeros(len(data['placebo'][0]))]
    res[f"{ep}_HR"] = dict(efron=cox(t, e, z, 'efron'), breslow=cox(t, e, z, 'breslow'))
print(json.dumps(res, indent=1)); json.dump(res, open(sys.argv[2], 'w'), indent=1)
