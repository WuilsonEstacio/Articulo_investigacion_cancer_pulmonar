"""Full synthetic KM -> filled vector PDF -> extract_pdf -> Guyot experiment."""
import json
import numpy as np
import pandas as pd
from lifelines import KaplanMeierFitter
from simulate import generate
from vector_simulation import FigureGeometry
from extract import extract_pdf
from guyot import reconstruct,step_at
from validate import fit_cox


def run_digitized_simulations(cfg,out):
    simdir=out/'simulation_b'
    simdir.mkdir(exist_ok=True)
    geometry=FigureGeometry(cfg)
    rows=[]
    populations=[]
    risks=[]
    def add(rep,seed,ep,arm,quantity,truth,rec,tol):
        evaluable=np.isfinite(truth) and np.isfinite(rec)
        rows.append(dict(replicate=rep,seed=seed,endpoint=ep,arm=arm,quantity=quantity,truth=truth,reconstructed=rec,error=rec-truth if evaluable else np.nan,tolerance=tol,evaluable=evaluable,both_not_reached=bool(np.isinf(truth) and np.isinf(rec)),within_tolerance=bool(abs(rec-truth)<=tol+1e-12) if evaluable else False))
    for rep in range(cfg['replicates']):
        seed=cfg['seed']+rep
        rng=np.random.default_rng(seed)
        for ep in cfg['pages']:
            pair={arm:generate(rng,n,f'{ep}_{arm}',cfg['simulation']) for arm,n in [('durvalumab',264),('placebo',266)]}
            directory=simdir/f'{rep:03d}_{ep}'
            directory.mkdir(exist_ok=True)
            pdf=directory/'km.pdf'
            geometry.render(pdf,pair,cfg)
            curves,audits=extract_pdf(pdf,dict(cfg,pages={ep:1}),directory)
            (directory/'extraction_audit.json').write_text(json.dumps(audits,indent=2),encoding='utf-8')
            rec_pair={}
            for arm,truth in pair.items():
                km=KaplanMeierFitter().fit(truth.time_months,truth.event)
                point=curves[ep,arm]
                rt=np.arange(0,64,3)
                nr=np.array([(truth.time_months>=t).sum() for t in rt])
                pdf_risk=pd.read_csv(directory/f'risk_pdf_{ep}.csv')
                np.testing.assert_array_equal(pdf_risk[pdf_risk.arm==arm].at_risk,nr)
                rec,audit=reconstruct(point.time_months,point.survival,rt,nr,int(truth.event.sum()))
                rec_km=KaplanMeierFitter().fit(rec.time_months,rec.event)
                truth.to_csv(directory/f'truth_{arm}.csv',index=False)
                rec.to_csv(directory/f'reconstructed_{arm}.csv',index=False)
                audit.to_csv(directory/f'intervals_{arm}.csv',index=False)
                risk_error=[]
                for t,r in zip(rt,nr):
                    rr=int((rec.time_months>=t).sum())
                    risk_error.append(abs(rr-r))
                    risks.append(dict(replicate=rep,seed=seed,endpoint=ep,arm=arm,time_months=t,truth=int(r),reconstructed=rr,difference=int(rr-r)))
                grid=np.arange(0,min(point.time_months.iloc[-1],truth.time_months.max()),cfg['grid_months'])
                delta=step_at(point.time_months,point.survival,grid)-km.predict(grid).to_numpy()
                ties=rec.loc[rec.event==1].groupby('time_months').size()
                true_ties=truth.loc[truth.event==1].groupby('time_months').size()
                populations.append(dict(replicate=rep,seed=seed,endpoint=ep,arm=arm,n=len(truth),events=int(truth.event.sum()),censor_fraction=float(1-truth.event.mean()),support_end=float(truth.time_months.max()),max_risk_error=int(max(risk_error)),mean_risk_error=float(np.mean(risk_error)),max_tie=int(ties.max()) if len(ties) else 0,true_max_tie=int(true_ties.max()) if len(true_ties) else 0,event_times=len(ties),plateaus=int((point.kind=='plateau').sum()),true_plateaus=1+len(true_ties),extraction_max_absolute=float(abs(delta).max()),extraction_mean_absolute=float(abs(delta).mean())))
                add(rep,seed,ep,arm,'eventos_totales',int(truth.event.sum()),int(rec.event.sum()),.03*truth.event.sum())
                add(rep,seed,ep,arm,'mediana',km.median_survival_time_,rec_km.median_survival_time_,3 if (ep,arm)==('SG','durvalumab') else 1)
                for milestone in ([24,36] if ep=='SG' else [18,24]):
                    add(rep,seed,ep,arm,f'S_{milestone}',float(km.predict(milestone)),float(rec_km.predict(milestone)),.02)
                rec_pair[arm]=rec
            add(rep,seed,ep,'D vs P','HR',fit_cox(pair)['hr'],fit_cox(rec_pair)['hr'],.03)
        pd.DataFrame(rows).to_csv(out/'simulation_b_metrics.csv',index=False)
        pd.DataFrame(populations).to_csv(out/'simulation_b_populations.csv',index=False)
        pd.DataFrame(risks).to_csv(out/'simulation_b_risks.csv',index=False)
        if (rep+1)%10==0:
            print(f'E2.0b: {rep+1}/{cfg["replicates"]}',flush=True)
    frame=pd.DataFrame(rows)
    summary=[]
    for (ep,quantity),group in frame.groupby(['endpoint','quantity']):
        valid=group[group.evaluable]
        error=valid.error.abs()
        summary.append(dict(endpoint=ep,quantity=quantity,total=len(group),evaluable=len(valid),not_evaluable=len(group)-len(valid),both_not_reached=int(group.both_not_reached.sum()),bias=float(valid.error.mean()),mae=float(error.mean()),p95_absolute=float(error.quantile(.95)),max_absolute=float(error.max()),within_tolerance=int(valid.within_tolerance.sum())))
    pd.DataFrame(summary).to_csv(out/'simulation_b_summary.csv',index=False)
    return frame