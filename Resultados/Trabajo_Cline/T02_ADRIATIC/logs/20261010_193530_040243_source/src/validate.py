"""Published targets read from authorized CSV, never used to tune reconstruction."""
import re
import numpy as np
import pandas as pd
from lifelines import KaplanMeierFitter,CoxPHFitter
from lifelines.statistics import proportional_hazard_test
from lifelines.utils import median_survival_times
from guyot import step_at


def numbers(value):
    return [float(v) for v in re.findall(r'\d+(?:\.\d+)?',str(value))]


def fit_cox(ipds, ph=False):
    data=pd.concat([v.assign(treatment=int(arm=='durvalumab'))[['time_months','event','treatment']] for arm,v in ipds.items()],ignore_index=True)
    fit=CoxPHFitter().fit(data,duration_col='time_months',event_col='event')
    ci=np.exp(fit.confidence_intervals_.loc['treatment'].to_numpy())
    result=dict(hr=float(fit.hazard_ratios_['treatment']),ci_lower=float(ci[0]),ci_upper=float(ci[1]))
    if ph:
        result['ph_p_rank']=float(proportional_hazard_test(fit,data,time_transform='rank').summary.loc['treatment','p'])
    return result


def validate(curves,ipds,inputs,cfg,out):
    rows=[]
    errors=[]
    censor_rows=[]
    def add(quantity,endpoint,arm,pub,rec,unit,tol,source,page,note='',scope='H1'):
        finite=np.isfinite(rec) and np.isfinite(pub)
        delta=rec-pub if finite else np.nan
        if tol is None or not finite:
            status='no evaluable'
        else:
            status='reproducido' if abs(delta)<=tol+1e-12 else 'discrepancia'
        rows.append(dict(quantity=quantity,endpoint=endpoint,arm=arm,published=pub,reconstructed=rec,difference=delta,unit=unit,tolerance=tol,classification=status,source=source,page=page,note=note,scope=scope))
    for (ep,arm),ipd in ipds.items():
        sub=inputs[(inputs.brazo==arm)&(inputs.desenlace==ep)]
        point=curves[ep,arm]
        km=KaplanMeierFitter().fit(ipd.time_months,ipd.event)
        for kind,rec,tol,unit in [('eventos_totales',float(ipd.event.sum()),None,'eventos'),('mediana',float(km.median_survival_time_),cfg['tolerances']['median_sg_durvalumab_months'] if (ep,arm)==('SG','durvalumab') else cfg['tolerances']['median_months'],'meses')]:
            ref=sub[sub.insumo==kind].iloc[0]
            pub=numbers(ref.valor)[0]
            if kind=='eventos_totales':
                tol=cfg['tolerances']['events_relative']*pub
            add(kind,ep,arm,pub,rec,unit,tol,ref.fuente,ref.ubicacion,'Restricción de entrada' if kind=='eventos_totales' else '')
            if kind=='mediana':
                vals=numbers(ref.valor)
                ci=median_survival_times(km.confidence_interval_).iloc[0].to_numpy()
                for label,published,recon in [('IC95_inferior',vals[1],ci[0]),('IC95_superior',vals[2] if len(vals)>2 else np.inf,ci[1])]:
                    add('mediana_'+label,ep,arm,published,float(recon),'meses',None,ref.fuente,ref.ubicacion,'IC log-log Greenwood, informativo; NR=inf','informativo')
        milestones=inputs[(inputs.insumo=='tasa_hito')&(inputs.brazo==arm)&inputs.desenlace.str.startswith(ep+' ')]
        for _,ref in milestones.iterrows():
            time=numbers(ref.desenlace)[0]
            vals=np.array(numbers(ref.valor))/100
            rec=float(km.predict(time))
            add(f'S_{time:g}',ep,arm,vals[0],rec,'probabilidad',cfg['tolerances']['milestone_probability'],ref.fuente,ref.ubicacion)
            extracted=float(step_at(point.time_months,point.survival,time))
            add(f'extraida_S_{time:g}',ep,arm,vals[0],extracted,'probabilidad',cfg['tolerances']['milestone_probability'],ref.fuente,ref.ubicacion,'Comprobación de extracción; no independiente de figura','extraccion')
            ci=km.confidence_interval_.loc[km.confidence_interval_.index<=time].iloc[-1].to_numpy()
            for label,published,recon in [('IC95_inferior',vals[1],ci[0]),('IC95_superior',vals[2],ci[1])]:
                add(f'S_{time:g}_{label}',ep,arm,published,float(recon),'probabilidad',None,ref.fuente,ref.ubicacion,'IC log-log Greenwood; sin tolerancia contractual','informativo')
        ref=sub[sub.insumo=='numeros_en_riesgo'].iloc[0]
        risk=np.array([int(v) for v in ref.valor.split(',')])
        times=np.arange(0,64,3)
        pdf_risk=pd.read_csv(out/f'risk_pdf_{ep}.csv')
        np.testing.assert_array_equal(pdf_risk[pdf_risk.arm==arm].at_risk,risk)
        for time,pub in zip(times,risk):
            rec=int((ipd.time_months>=time).sum())
            add(f'riesgo_{time:g}',ep,arm,int(pub),rec,'pacientes',None,ref.fuente,ref.ubicacion,'Restricción de entrada; riesgo inmediatamente antes del tiempo','riesgo')
            rows[-1]['classification']='reproducido' if rec==pub else ('parcialmente reproducido' if abs(rec-pub)==1 else 'discrepancia')
            if abs(rec-pub)>1:
                rows[-1]['note']+='; incompatibilidad entre redondeo KM/censura uniforme y riesgo: ver auditoría por intervalo; no corregida artificialmente'
        grid=np.arange(0,float(point.time_months.iloc[-1])+1e-9,cfg['grid_months'])
        diff=step_at(point.time_months,point.survival,grid)-km.predict(grid).to_numpy()
        pd.DataFrame(dict(time_months=grid,difference=diff)).to_csv(out/f'difference_{ep}_{arm}.csv',index=False)
        errors.append(dict(endpoint=ep,arm=arm,max_absolute=float(abs(diff).max()),mean_absolute=float(abs(diff).mean()),grid_months=cfg['grid_months'],grid_n=len(grid),support_end=float(point.time_months.iloc[-1])))
        marks=pd.read_csv(out/f'censor_marks_{ep}_{arm}.csv')
        followup={('SG','durvalumab'):(37.2,.1,60.2),('SG','placebo'):(37.2,.7,60.9),('SLP','durvalumab'):(27.4,0.,55.4),('SLP','placebo'):(27.7,0.,55.8)}
        censored=ipd.loc[ipd.event==0,'time_months']
        for label,pub,rec in zip(['mediana','minimo','maximo'],followup[ep,arm],[censored.median(),censored.min(),censored.max()]):
            add('seguimiento_censurados_'+label,ep,arm,pub,float(rec),'meses',None,'D04 ADRIATIC','PDF p.7 {1319}, Efficacy','Descriptivo entre censurados, no KM reverso; no identifica censuras originales','informativo')
        for a,b,na,nb in zip(times[:-1],times[1:],risk[:-1],risk[1:]):
            selected=marks[(marks.time_months>=a)&(marks.time_months<b)]
            gap=selected.survival.to_numpy()-step_at(point.time_months,point.survival,selected.time_months)
            censor_rows.append(dict(endpoint=ep,arm=arm,start=a,end=b,risk_exits=int(na-nb),unique_marks=len(selected),reconstructed_censors=int(((ipd.event==0)&(ipd.time_months>=a)&(ipd.time_months<b)).sum()),max_mark_survival_offset=float(abs(gap).max()) if len(gap) else 0,note='Marcas gráficas no equivalen uno a uno a sujetos; solapamiento/dobles contornos. No restricción de conteo.'))
    for ep in cfg['pages']:
        cox=fit_cox({arm:ipds[ep,arm] for arm in cfg['colors']},ph=True)
        ref=inputs[(inputs.insumo=='HR')&(inputs.desenlace==ep)].iloc[0]
        add('HR',ep,'D vs P',numbers(ref.valor)[0],cox['hr'],'razón',cfg['tolerances']['hr_absolute'],ref.fuente,ref.ubicacion,'Cox no estratificado; forest no aclara inequívocamente ajuste')
        # Forest 95% CI, not the multiplicity-adjusted CI in the CSV headline.
        ci_pub=(.57,.93) if ep=='SG' else (.61,.95)
        for label,pub,key in [('inferior',ci_pub[0],'ci_lower'),('superior',ci_pub[1],'ci_upper')]:
            add('HR_IC95_'+label,ep,'D vs P',pub,cox[key],'razón',None,'D04',f'Fig. {1 if ep=="SG" else 2}B, PDF p.{cfg["pages"][ep]}','Informativo, sin tolerancia','informativo')
        ref=inputs[(inputs.insumo=='prueba_PH')&(inputs.desenlace==ep)].iloc[0]
        add('PH_p_rank',ep,'D vs P',numbers(ref.valor)[0],cox['ph_p_rank'],'p',None,ref.fuente,ref.ubicacion,'Schoenfeld rank no estratificado; no necesariamente mismo contraste publicado','informativo')
    frame=pd.DataFrame(rows)
    frame.to_csv(out/'validation.csv',index=False)
    pd.DataFrame(errors).to_csv(out/'curve_errors.csv',index=False)
    pd.DataFrame(censor_rows).to_csv(out/'censor_coherence.csv',index=False)
    return frame