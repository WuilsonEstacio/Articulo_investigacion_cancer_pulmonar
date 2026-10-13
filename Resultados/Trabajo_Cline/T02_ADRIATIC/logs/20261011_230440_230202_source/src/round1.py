"""Round-1 comparisons; clinical targets never enter this descriptive calculation."""
import json
import numpy as np
import pandas as pd
from scipy.optimize import brentq
from validate import fit_cox


def cox_ties(pair,method):
    if method not in ['efron','breslow']:
        raise ValueError(method)
    data=pd.concat([d.assign(x=int(arm=='durvalumab')) for arm,d in pair.items()])
    t=data.time_months.to_numpy()
    e=data.event.to_numpy()
    x=data.x.to_numpy()
    groups=[]
    for time in np.unique(t[e==1]):
        risk=t>=time
        event=(t==time)&(e==1)
        groups.append((int(sum(risk&(x==0))),int(sum(risk&(x==1))),int(sum(event&(x==0))),int(sum(event&(x==1)))))
    def score(beta):
        z=np.exp(beta)
        value=0.
        for n0,n1,d0,d1 in groups:
            d=d0+d1
            if method=='breslow':
                value+=d1-d*n1*z/(n0+n1*z)
            else:
                frac=np.arange(d)/d
                value+=d1-np.sum((n1*z-frac*d1*z)/(n0+n1*z-frac*(d0+d1*z)))
        return value
    return float(np.exp(brentq(score,-10,10,xtol=1e-12)))


def comparisons(root,cfg):
    out=root/'data_derived'
    original=root/'logs/ronda0_original'
    ties=[]
    hrs=[]
    for version,directory in [('original',original),('corregido',out)]:
        for ep in cfg['pages']:
            pair={}
            for arm in cfg['colors']:
                ipd=pd.read_csv(directory/f'pseudo_ipd_{ep}_{arm}.csv')
                points=pd.read_csv(directory/f'points_{ep}_{arm}.csv')
                groups=ipd[ipd.event==1].groupby('time_months').size()
                ties.append(dict(version=version,endpoint=ep,arm=arm,plateaus=int((points.kind=='plateau').sum()),events=int(ipd.event.sum()),max_tie=int(groups.max()),distinct_event_times=len(groups),distinct_all_times=ipd.time_months.nunique(),times_with_at_least_5=int((groups>=5).sum())))
                pair[arm]=ipd
            hrs.append(dict(version=version,endpoint=ep,efron_lifelines=fit_cox(pair)['hr'],efron_score=cox_ties(pair,'efron'),breslow_score=cox_ties(pair,'breslow')))
    pd.DataFrame(ties).to_csv(out/'round1_ties.csv',index=False)
    pd.DataFrame(hrs).to_csv(out/'round1_hr.csv',index=False)
    for scope,name in [('H1','h1'),('riesgo','risks')]:
        frames=[]
        for version,directory in [('original',original),('corregido',out)]:
            data=pd.read_csv(directory/'validation.csv')
            frames.append(data[data.scope==scope].assign(version=version))
        pd.concat(frames).to_csv(out/f'round1_{name}.csv',index=False)


def append_report(root,cfg):
    from reporting import table,save
    import matplotlib.pyplot as plt
    comparisons(root,cfg)
    out=root/'data_derived'
    original=root/'logs/ronda0_original'
    val=pd.read_csv(out/'validation.csv')
    h1=val[val.scope=='H1']
    risk=val[val.scope=='riesgo']
    ties=pd.read_csv(out/'round1_ties.csv')
    hrs=pd.read_csv(out/'round1_hr.csv')
    metrics_b=pd.read_csv(out/'simulation_b_metrics.csv')
    summary_b=pd.read_csv(out/'simulation_b_summary.csv')
    pop_b=pd.read_csv(out/'simulation_b_populations.csv')
    summary_a=pd.read_csv(out/'simulation_summary.csv')
    pop_a=pd.read_csv(out/'simulation_populations.csv')
    assert len(metrics_b)==cfg['replicates']*18 and len(pop_b)==cfg['replicates']*4
    cols=['quantity','endpoint','arm','published','reconstructed','difference','tolerance','classification']
    parts=['\n## Ronda 1 de corrección\n',
           'Fecha de corrección: 11-oct-2026 (hora local de inicio). Estado: entregada (ronda 1). Pendiente de revisión del coordinador.\n',
           'Se conserva arriba el informe original íntegro. La auditoría T04 detectó D1 (mesetas fusionadas) y D2 (E2.0 sin extracción). Los resultados vigentes son los corregidos que siguen. No se cambiaron Guyot, semillas, diseño, configuración ni tolerancias. No se optimizó contra estadísticas publicadas.\n',
           f'Copia original verificada: `{original}`; manifiesto `{root / "logs/ronda0_original_sha256.csv"}`. Código/documentos originales: `{root / "logs/ronda0_documentos"}`.\n',
           '### D1: método y resultados originales primero\n',
           'Se emparejan bordes horizontales opuestos separados aproximadamente 0,502 pt, sin filtro de grosor de franja ni mínimo de longitud de meseta. Se incluyen segmentos con desnivel de 0,001 pt por precisión del PDF. Las mesetas cortas pueden tener bordes no solapados. Se guardan los segmentos de cada pareja, y se exige unicidad y continuidad. La calibración textual, elección de contorno y marcas permanecen iguales. Justificación fechada en DECISIONES_METODO.md.\n']
    for version,directory in [('original',original),('corregido',out)]:
        data=pd.read_csv(directory/'validation.csv')
        parts.extend([f'#### Resultado {version}\n','**18 cantidades H1** (tasas en probabilidad, no porcentaje):\n',table(data[data.scope=='H1'][cols]),
                      '\n**Empates y tiempos distintos**: event_times son tiempos distintos de evento; all_times incluyen censuras.\n',table(ties[ties.version==version]),
                      '\n**HR no estratificada Efron/Breslow**, sin nueva tolerancia; score Efron se contrasta con lifelines:\n',table(hrs[hrs.version==version]),
                      '\n**88 números en riesgo**, con diferencia en cada tiempo (restricciones de entrada, no validación independiente):\n',table(data[data.scope=='riesgo'][cols])])
    audit=json.loads((out/'extraction_audit.json').read_text(encoding='utf-8'))
    parts.extend(['\n#### Comprobación de mesetas corregidas\n',table(pd.DataFrame(audit).T[['paired_horizontal_levels','points','support_end','unique_marks']].reset_index(names='curva')),
                  '\nEl número de puntos incluye un punto adicional de fin de soporte. La prueba cuenta de forma independiente los pares de niveles horizontales y compara las ordenadas una a una con las mesetas extraídas; además recalcula el empate máximo y los tiempos distintos de cada pseudo-IPD. Un empate residual no identifica eventos originales: persisten redondeo de curva e inversión KM.\n',
                  '\n#### Errores de curva corregida\n',table(pd.read_csv(out/'curve_errors.csv')),
                  '\n### D2: E2.0a: sin digitalización (original)\n',
                  '100 réplicas, 400 reconstrucciones, semillas 20261010–20261109. Se conserva la simulación original y se reejecuta sin cambiar su código; se comprueba identidad con la copia de ronda 0.\n',table(summary_a),
                  f'\nError máximo de riesgo E2.0a: {int(pop_a.max_risk_error.max())} sujetos.\n',
                  '\n### D2: E2.0b: con extracción vectorial (corregido)\n',
                  f'{pop_b.replicate.nunique()} réplicas completas, {len(pop_b)} reconstrucciones y {len(metrics_b)} comparaciones; **no se redujo a 20 réplicas**. Mismas semillas y poblaciones verdaderas que E2.0a. Cada par KM se dibuja en un PDF reabierto por extract_pdf: escala y posiciones textuales de Fig.1A, polígonos rellenos de 0,502 pt, colores de brazos, marcas de censura rectangulares 0,502 ×5 pt y riesgo. No se pasan coordenadas KM exactas a reconstruct.\n',
                  table(summary_b),
                  f'\nResultado E2.0b: {int(summary_b.within_tolerance.sum())}/{int(summary_b.evaluable.sum())} evaluables dentro de las tolerancias originales; {int(summary_b.not_evaluable.sum())} no evaluables. Las discrepancias se conservan sin reajustes.\n'])
    descriptive=pop_b.groupby(['endpoint','arm']).agg(reconstructions=('replicate','size'),max_risk_error=('max_risk_error','max'),mean_risk_error=('mean_risk_error','mean'),max_tie=('max_tie','max'),true_max_tie=('true_max_tie','max'),extraction_max_absolute=('extraction_max_absolute','max'),extraction_mean_absolute=('extraction_mean_absolute','mean')).reset_index()
    descriptive.to_csv(out/'simulation_b_diagnostics_summary.csv',index=False)
    parts.extend([table(descriptive),f'\nLos 8.800 controles de riesgo por tiempo se conservan en `{out / "simulation_b_risks.csv"}`; diferencias >1 sujetos: {int((pd.read_csv(out/"simulation_b_risks.csv").difference.abs()>1).sum())}. Riesgo sin tolerancia contractual fija. Empates sin umbral clínico nuevo. Errores de extracción en probabilidad sobre rejilla de 0,1 meses, dentro del soporte común.\n',
                  'Los PDF sintéticos prueban contornos vectoriales y marcas, no ruido ráster ni todos los salientes de unión del editor de ADRIATIC. Se conservan también tiempo/ordenada de cada meseta para distinguir error de coordenadas de error KM. La asignación uniforme de censuras sigue siendo aproximada. E2.0b no garantiza exactitud fuera de este diseño ni recupera los datos originales.\n',
                  '\n### Estado numérico y limitaciones tras la corrección\n',
                  f'- H1 corregido: {int(h1.classification.eq("reproducido").sum())}/18 cantidades reproducidas con criterios sin cambios.\n',
                  f'- Riesgo corregido: {risk.classification.value_counts().to_dict()}; desviación máxima {risk.difference.abs().max():g} sujetos.\n',
                  '- Eventos, como entrada, no son validación independiente; resultados por brazo:\n',table(h1[h1.quantity=='eventos_totales'][cols]),
                  '\n- Continúan las limitaciones originales: pseudo-IPD aproximados, censuras no identificables, cola SG-D frágil, ausencia de covariables y PH no directamente equivalente. SG y SLP son reconstrucciones marginales sin enlace entre sujetos. La ronda queda entregada, no aceptada.\n'])
    archived=(root/'logs/ronda0_documentos/INFORME_T02.md').read_text(encoding='utf-8')
    (root/'INFORME_T02.md').write_text(archived+'\n'+'\n'.join(parts),encoding='utf-8')
    deliver=f'''# Entrega T02 — Ronda 1 de corrección

Estado: entregada (ronda 1)

Pendiente de revisión del coordinador. No se declara aceptación.

- Informe original seguido de sección «Ronda 1 de corrección»: `{root / 'INFORME_T02.md'}`.
- D1: extractor corregido, pares de bordes y comprobación de mesetas; D2: E2.0a conservado y E2.0b con 100 réplicas, PDF y extracción compartida.
- H1: {int(h1.classification.eq('reproducido').sum())}/18 cantidades reproducidas; tolerancias/configuración/Guyot sin cambios.
- Riesgo corregido: {risk.classification.value_counts().to_dict()}.
- E2.0b: {int(summary_b.within_tolerance.sum())}/{int(summary_b.evaluable.sum())} evaluables en tolerancia; {int(summary_b.not_evaluable.sum())} no evaluables. Riesgo y empates en informe/CSV.
- Código y pruebas: `{root / 'src'}`, `{root / 'tests'}`. Configuración: `{root / 'config/config.yaml'}`.
- Derivados clínicos, tablas original/corregido y ambas simulaciones: `{out}`.
- Figuras PNG/SVG clínicas y E2.0a/b: `{root / 'figures'}`.
- Reproducción: `{root / 'REPRODUCIR.md'}`; entorno: `{root / 'requirements_T02.txt'}`.
- Métodos/criterios: `{root / 'DECISIONES_METODO.md'}`, `{root / 'CRITERIOS_PREESPECIFICADOS.md'}`.
- Copia original: `{original}`; documentación/código originales: `{root / 'logs/ronda0_documentos'}`; hashes: `{root / 'logs/ronda0_original_sha256.csv'}`.
- Registros de ejecución y exit_code: `{root / 'logs'}`. Incidencias: `{root / 'logs/INCIDENCIAS.md'}`.

## Problemas abiertos
Tiempos individuales no identificables, censura uniforme aproximada, fragilidad de cola SG-D, simulación vectorial idealizada y PH no equivalente al análisis publicado. Los eventos y el riesgo son restricciones de entrada. Ninguna discrepancia se corrigió mediante ajuste a cifras publicadas. Revisión del coordinador pendiente.
'''
    (root/'ENTREGA_LISTA.md').write_text(deliver,encoding='utf-8')
    prov=out/'PROCEDENCIA.md'
    with prov.open('a',encoding='utf-8') as handle:
        handle.write(f'\n## Ronda 1\nOriginal: `{original}`. `plateaus_*.csv`: pares de bordes del contorno. `round1_*.csv`: original primero, corregido después. `simulation_*` y `simulation/`: E2.0a sin digitalización. `simulation_b_*` y `simulation_b/`: E2.0b, PDF sintético por réplica/desenlace, fuente de extracción página 1, verdad y reconstrucción por brazo. No son páginas del ensayo.\n')
    fig,axes=plt.subplots(2,2,figsize=(11,7))
    for ax,q in zip(axes.flat,['eventos_totales','mediana','HR','S_24']):
        group=metrics_b[(metrics_b.quantity==q)&metrics_b.evaluable]
        for ep in cfg['pages']:
            ax.hist(group[group.endpoint==ep].error,bins=20,alpha=.55,label=ep)
        ax.set(title=q,xlabel='Reconstruido − verdadero',ylabel='Frecuencia')
        ax.legend()
    fig.suptitle('E2.0b: KM → PDF vectorial → extracción → reconstrucción (100 réplicas)')
    fig.tight_layout()
    save(fig,root/'figures/simulation_E20b')