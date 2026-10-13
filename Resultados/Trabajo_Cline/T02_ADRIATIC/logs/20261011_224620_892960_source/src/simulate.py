"""E2.0 fixed nonparametric synthetic experiments, not clinical fitting."""
import numpy as np
import pandas as pd
from lifelines import KaplanMeierFitter
from guyot import reconstruct
from validate import fit_cox


def generate(rng,n,key,design):
    edges=np.array(design['category_edges_months'])
    month=np.arange(.5,61,1)
    mass=np.array(design['event_mass'][key])
    weights=np.zeros(len(month))
    for a,b,p in zip(edges[:-1],edges[1:],mass):
        mask=(month>=a)&(month<b)
        weights[mask]=p/mask.sum()
    # Infinity is only a synthetic no-event category, never a fitted tail.
    event_time=rng.choice(np.r_[month,np.inf],size=n,p=np.r_[weights,1-weights.sum()])
    event_time+=rng.uniform(-design['event_jitter_months'],design['event_jitter_months'],n)
    censor=rng.uniform(*design['administrative_censor_months'],size=n)
    early=rng.random(n)<design['early_loss_probability']
    censor[early]=rng.uniform(*design['early_loss_months'],size=int(early.sum()))
    return pd.DataFrame(dict(time_months=np.minimum(event_time,censor),event=(event_time<=censor).astype(int)))


def run_simulations(cfg,out):
    rows=[]
    populations=[]
    simdir=out/'simulation'
    simdir.mkdir(exist_ok=True)
    def add(rep,seed,ep,arm,quantity,truth,rec,tol):
        evaluable=np.isfinite(truth) and np.isfinite(rec)
        rows.append(dict(replicate=rep,seed=seed,endpoint=ep,arm=arm,quantity=quantity,truth=truth,reconstructed=rec,error=rec-truth if evaluable else np.nan,tolerance=tol,evaluable=evaluable,both_not_reached=bool(np.isinf(truth) and np.isinf(rec)),within_tolerance=bool(abs(rec-truth)<=tol+1e-12) if evaluable else False))
    for rep in range(cfg['replicates']):
        seed=cfg['seed']+rep
        rng=np.random.default_rng(seed)
        for ep in cfg['pages']:
            true_pair={}
            rec_pair={}
            for arm,n in [('durvalumab',264),('placebo',266)]:
                truth=generate(rng,n,f'{ep}_{arm}',cfg['simulation'])
                km=KaplanMeierFitter().fit(truth.time_months,truth.event)
                rt=np.arange(0,64,3)
                nr=np.array([(truth.time_months>=t).sum() for t in rt])
                t=km.survival_function_.index.to_numpy()
                s=km.survival_function_.iloc[:,0].to_numpy()
                rec,audit=reconstruct(t,s,rt,nr,int(truth.event.sum()))
                rec_km=KaplanMeierFitter().fit(rec.time_months,rec.event)
                stem=f'{rep:03d}_{ep}_{arm}'
                truth.to_csv(simdir/f'truth_{stem}.csv',index=False)
                rec.to_csv(simdir/f'reconstructed_{stem}.csv',index=False)
                audit.to_csv(simdir/f'intervals_{stem}.csv',index=False)
                populations.append(dict(replicate=rep,seed=seed,endpoint=ep,arm=arm,n=n,events=int(truth.event.sum()),censor_fraction=float(1-truth.event.mean()),support_end=float(truth.time_months.max()),max_risk_error=int(max(abs((rec.time_months>=t).sum()-r) for t,r in zip(rt,nr)))))
                add(rep,seed,ep,arm,'eventos_totales',int(truth.event.sum()),int(rec.event.sum()),.03*truth.event.sum())
                add(rep,seed,ep,arm,'mediana',km.median_survival_time_,rec_km.median_survival_time_,3 if (ep,arm)==('SG','durvalumab') else 1)
                for milestone in ([24,36] if ep=='SG' else [18,24]):
                    add(rep,seed,ep,arm,f'S_{milestone}',float(km.predict(milestone)),float(rec_km.predict(milestone)),.02)
                true_pair[arm]=truth
                rec_pair[arm]=rec
            add(rep,seed,ep,'D vs P','HR',fit_cox(true_pair)['hr'],fit_cox(rec_pair)['hr'],.03)
        pd.DataFrame(rows).to_csv(out/'simulation_metrics.csv',index=False)
        pd.DataFrame(populations).to_csv(out/'simulation_populations.csv',index=False)
        if (rep+1)%10==0:
            print(f'E2.0: {rep+1}/{cfg["replicates"]}',flush=True)
    frame=pd.DataFrame(rows)
    summary=[]
    for (ep,quantity),group in frame.groupby(['endpoint','quantity']):
        valid=group[group.evaluable]
        error=valid.error.abs()
        summary.append(dict(endpoint=ep,quantity=quantity,total=len(group),evaluable=len(valid),not_evaluable=len(group)-len(valid),both_not_reached=int(group.both_not_reached.sum()),bias=float(valid.error.mean()),mae=float(error.mean()),p95_absolute=float(error.quantile(.95)),max_absolute=float(error.max()),within_tolerance=int(valid.within_tolerance.sum())))
    pd.DataFrame(summary).to_csv(out/'simulation_summary.csv',index=False)
    return frame