"""Figures and Spanish report generated from registered calculation tables."""
from pathlib import Path
import json
import hashlib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.hashsalt']='T02_ADRIATIC'
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter


def table(frame):
    def fmt(x):
        if isinstance(x,(float,np.floating)):
            return 'NR' if np.isinf(x) else ('—' if np.isnan(x) else f'{x:.6g}')
        return str(x).replace('|','/')
    return '| '+' | '.join(frame.columns)+' |\n| '+' | '.join(['---']*len(frame.columns))+' |\n'+'\n'.join('| '+' | '.join(fmt(x) for x in row)+' |' for row in frame.itertuples(index=False,name=None))


def save(fig,path):
    fig.savefig(str(path)+'.png',dpi=180,bbox_inches='tight')
    fig.savefig(str(path)+'.svg',bbox_inches='tight',metadata={'Date':None})
    plt.close(fig)


def figures(root,cfg):
    out=root/'data_derived'
    palette={'durvalumab':'#cb842a','placebo':'#3971ba'}
    for ep,page in cfg['pages'].items():
        fig,(ax,tax)=plt.subplots(2,1,figsize=(13,7),gridspec_kw={'height_ratios':[4,1.35]})
        risk=pd.read_csv(out/f'risk_pdf_{ep}.csv')
        times=np.arange(0,64,3)
        cell=[]
        names=[]
        for arm in cfg['colors']:
            points=pd.read_csv(out/f'points_{ep}_{arm}.csv')
            ipd=pd.read_csv(out/f'pseudo_ipd_{ep}_{arm}.csv')
            km=KaplanMeierFitter().fit(ipd.time_months,ipd.event)
            ax.step(points.time_months,points.survival,where='post',color=palette[arm],lw=2,label=f'{arm}: extraída')
            ax.step(km.survival_function_.index,km.survival_function_.iloc[:,0],where='post',color=palette[arm],linestyle='--',lw=1.2,label=f'{arm}: pseudo-IPD KM')
            cell.append(risk[risk.arm==arm].at_risk.astype(str).tolist())
            names.append(f'{arm} publ.')
            cell.append([str(int((ipd.time_months>=t).sum())) for t in times])
            names.append(f'{arm} recon.')
        ax.set(xlabel='Meses desde aleatorización',ylabel='Probabilidad de supervivencia',ylim=(0,1.02),xlim=(0,63),title=f'ADRIATIC — {ep} ITT'+(' (BICR)' if ep=='SLP' else ''))
        ax.legend(loc='lower left',ncol=2,fontsize=9)
        ax.grid(alpha=.2)
        tax.axis('off')
        tb=tax.table(cellText=cell,rowLabels=names,colLabels=[str(t) for t in times],loc='center',cellLoc='center')
        tb.auto_set_font_size(False)
        tb.set_fontsize(7)
        tb.scale(1,1.35)
        fig.text(.5,.01,f'Fuente: Cheng et al., NEJM 2024, Fig. {1 if ep=="SG" else 2}A, PDF p.{page}. Riesgo publicado/reconstruido. Pseudo-IPD aproximados; sin extrapolación.',ha='center',fontsize=8)
        fig.tight_layout(rect=[.08,.05,1,1])
        save(fig,root/'figures'/f'overlay_{ep}')
        fig,ax=plt.subplots(figsize=(10,4))
        for arm in cfg['colors']:
            diff=pd.read_csv(out/f'difference_{ep}_{arm}.csv')
            ax.plot(diff.time_months,100*diff.difference,label=arm,color=palette[arm])
        ax.axhline(0,color='black',lw=.7)
        ax.set(xlabel='Meses desde aleatorización',ylabel='S extraída − S reconstruida (pp)',title=f'{ep}: error en rejilla de 0,1 meses')
        ax.legend()
        fig.text(.5,.01,f'Fuente: cálculo T02 a partir de ADRIATIC Fig. {1 if ep=="SG" else 2}A, PDF p.{page}; soporte propio de cada curva.',ha='center',fontsize=8)
        fig.tight_layout(rect=[0,.05,1,1])
        save(fig,root/'figures'/f'differences_{ep}')
    sim=pd.read_csv(out/'simulation_metrics.csv')
    fig,axes=plt.subplots(2,2,figsize=(11,8))
    for ax,quantity,label in zip(axes.flat,['eventos_totales','mediana','milestone','HR'],['Error en eventos (recon. − verdad)','Error en mediana (meses)','Error en tasas hito (pp)','Error en HR']):
        subset=sim[sim.quantity.str.startswith('S_')] if quantity=='milestone' else sim[sim.quantity==quantity]
        for ep in cfg['pages']:
            values=subset[subset.endpoint==ep].error.dropna().to_numpy()
            if quantity=='milestone':
                values*=100
            ax.hist(values,bins=20,alpha=.5,label=ep)
        ax.set(xlabel=label,ylabel='Frecuencia')
        ax.legend()
    fig.suptitle('E2.0a: sin digitalización — 100 réplicas de dos desenlaces × dos brazos')
    fig.text(.5,.01,'Fuente: simulación no paramétrica T02, semillas 20261010–20261109 (decisiones de diseño). Medianas no evaluables excluidas solo del histograma.',ha='center',fontsize=8)
    fig.tight_layout(rect=[0,.04,1,.96])
    save(fig,root/'figures'/'simulation_E20')


def create_report(root,cfg):
    out=root/'data_derived'
    validation=pd.read_csv(out/'validation.csv')
    h1=validation[validation.scope=='H1']
    risk=validation[validation.scope=='riesgo']
    info=validation[validation.scope=='informativo']
    errors=pd.read_csv(out/'curve_errors.csv')
    simulation=pd.read_csv(out/'simulation_summary.csv')
    populations=pd.read_csv(out/'simulation_populations.csv')
    assert populations.replicate.nunique()==cfg['replicates']==100
    assert len(populations)==400 and len(pd.read_csv(out/'simulation_metrics.csv'))==1800
    audit=json.loads((out/'extraction_audit.json').read_text(encoding='utf-8'))
    figures(root,cfg)
    maincols=['quantity','endpoint','arm','published','reconstructed','difference','classification']
    n_pass=int((h1.classification=='reproducido').sum())
    risk_counts=risk.classification.value_counts().to_dict()
    maxpp=float(100*errors.max_absolute.max())
    censor_summary=populations.groupby(['endpoint','arm']).censor_fraction.agg(['mean','min','max']).reset_index()
    report=f'''# INFORME T02 — Reconstrucción ADRIATIC

Fecha: 10-oct-2026. Estado: entregada para revisión, no aceptada.

## Resultado ejecutivo

Se reconstruyeron las cuatro curvas ITT (SG y SLP BICR; durvalumab/placebo). **{n_pass}/{len(h1)} cantidades H1 reproducidas** conforme al contrato v1.0 §5.2; no se modificaron tolerancias. La validación numérica no significa recuperación de los datos originales ni aceptación por el coordinador.

Los pseudo-IPD tienen 264/266 sujetos por brazo y desenlace [D04 PDF pp.6/8; comprobación en inventario]. No existe enlace entre sujetos de SG y SLP: son reconstrucciones marginales separadas, no una cohorte conjunta utilizable para análisis multidesenlace.

## Fuentes y método

- Artículo autorizado: Cheng et al., NEJM 2024;391:1313–27, DOI 10.1056/NEJMoa2404873. Curvas/riesgo: Fig.1A p.6 y Fig.2A p.8; medianas/tasas/eventos/seguimiento: p.7; forest p.6/8; PH: leyendas pp.7/9. Se verificó el SHA-256 contra la ficha D04.
- Método: Guyot et al., BMC Med Res Methodol 2012;12:9, DOI 10.1186/1471-2288-12-9, Methods, ecuaciones 1–9 y pasos 1–8. Versión editorial 1-feb-2012 consultada 10-oct-2026. Implementación Python independiente **basada en Guyot**, no copia exacta del R original.
- Diferencias declaradas previamente: búsqueda entera exhaustiva de censuras uniformes por intervalo, sin reiniciar artificialmente el riesgo; desempate por error de curva. El total de eventos guía el último intervalo; no se modifica retrospectivamente ningún evento previo. Si no puede alcanzarse el total se informa. Residuo administrativo censurado al extremo observado. Esto deja 140 frente a 139 eventos en SLP-D, dentro del 3 %, pero no es cumplimiento exacto de la restricción.
- Extracción vectorial: colores, centros de polígonos estrechos, contorno de menor complejidad; marcas rectangulares separadas y deduplicadas. Puntos/segmentos conservan página, trazado y coordenadas PDF. Ejes calibrados con 22 ticks x y 11 ticks y, verificados por código. No se emplearon medianas ni hitos para calibrar o reconstruir.
- Censura uniforme intraintervalo y redondeo de eventos son supuestos. Los tiempos aproximados no son tiempos originales. Riesgo calculado como número de tiempos >= t; empates con eventos antes de censuras. Las simulaciones usan el mismo código.
- Exclusiones respetadas: sin extrapolación, ajustes paramétricos, curación, RMST ni subgrupos. Cox no estratificado se usa solo para validación contractual. Sin instalaciones nuevas; entorno congelado.

Detalle preevaluación: `{root / 'CRITERIOS_PREESPECIFICADOS.md'}` y `{root / 'DECISIONES_METODO.md'}`. Correcciones/incidencias: `{root / 'logs/INCIDENCIAS.md'}`.

## Validación principal (cálculo registrado)

Las tasas se muestran como probabilidades; diferencias en la misma escala. Fuente individual y tolerancia en cada fila del CSV de validación. Eventos y riesgo son entradas, por lo que su reproducción no es validación independiente.

{table(h1[maincols])}

## Números en riesgo

Clasificaciones: {risk_counts}. No hay diferencias mayores de un sujeto. Las diferencias no nulas corresponden a la imposibilidad de lograr exactamente el entero siguiente con la inversión KM y censura uniforme; no se fuerza un reinicio del riesgo.

{table(risk[risk.difference!=0][maincols])}

Tabla completa de los 88 controles:

{table(risk[maincols])}

## Error de curva y extracción

La diferencia entre la curva extraída y KM en rejilla de 0,1 meses cumple la métrica solicitada; no es un estimador puro de error de digitalización, pues también incorpora error de reconstrucción. No existe una curva original numérica independiente con la que separar ambos componentes. Máximo global: {maxpp:.6g} puntos porcentuales. Sin prolongación más allá del trazado.

{table(errors)}

Auditoría geométrica:

{table(pd.DataFrame(audit).T[['page','path_id','points','support_end','unique_marks','origin_shift_probability','s0','monotone']].reset_index(names='curva'))}

Todas las curvas son monótonas, S(0)=1; los hitos de los puntos extraídos se comparan en la etapa de validación, sin alimentar la reconstrucción en las filas `scope=extraccion`. Los números en riesgo obtenidos de coordenadas de texto coinciden exactamente con la tabla autorizada. Los intervalos SLP 30–33 meses no tienen eventos ni censuras reconstruidos; el control está en las pruebas de integración. Las marcas visibles no permiten contar todos los censurados: pueden solaparse, duplicarse o representar empates; la tabla de coherencia muestra por intervalo salidas del riesgo, marcas y censuras reconstruidas. No se afirma haber recuperado su multiplicidad original.

## Validación informativa: IC, PH y seguimiento

Los IC KM usan Greenwood log-log. Se comparan sus extremos, sin tolerancia contractual. PH usa Schoenfeld escalado con transformación rank y Cox no estratificado; no se considera réplica exacta de la prueba publicada, cuyo ajuste y definición pueden diferir. El seguimiento es la distribución de tiempos entre sujetos censurados, tal como dice la p.7, no KM inverso. Las cifras descriptivas de censura no se usan para ajustar la reconstrucción. `NR` representa no alcanzado, no un tiempo extrapolado.

{table(info[maincols])}

## E2.0: validación con verdad conocida

100 réplicas completas, cada una con ambos desenlaces y dos brazos: 400 reconstrucciones. Semillas 20261010–20261109. Tamaños 264/266 según D04 pp.6/8. Masa de evento por categorías mensuales, jitter y censura administrativa/temprana fijados como **supuestos de software**, no como datos del ensayo; valores completos en configuración. No se ajustó distribución paramétrica. Se conservaron verdad, pseudo-IPD y auditoría de intervalos para cada réplica. Las tasas de censoring pueden contrastarse en la tabla de poblaciones. El análisis compara estadísticas del KM/Cox verdadero de cada réplica con las del reconstruido, no con un HR generador.

{table(simulation)}

Evaluable excluye medianas no finitas; `both_not_reached` informa cuando ambas son no alcanzadas. Una mediana no alcanzada no se inventa. Las simulaciones prueban censura/redondeo, pero no reproducen todos los artefactos de digitalización del PDF. El desempeño es condicional al diseño sintético, no garantía universal. Errores fuera de las tolerancias se conservan y no provocaron cambios de método.

Resultado calculado: {int(simulation.within_tolerance.sum())}/{int(simulation.evaluable.sum())} comparaciones evaluables dentro de tolerancia; {int(simulation.not_evaluable.sum())} no evaluables. En esta corrida todas las medianas se alcanzaron. Esto no es una prueba de casos de mediana no alcanzada, que se cubren en pruebas unitarias mediante datos completamente censurados.

Fracción censurada simulada por brazo (cálculo de los 100 conjuntos):

{table(censor_summary)}

El diseño aproxima el tamaño y calendario de riesgo del ensayo, pero no iguala su fracción de censura por brazo, especialmente en SLP. Por ello E2.0 no es una calibración exacta a la censura de ADRIATIC. No se ajustaron las masas sintéticas después de observar este resultado. Máxima diferencia absoluta de riesgo simulado: {int(populations.max_risk_error.max())} sujetos.

## Problemas abiertos y limitaciones

1. SLP durvalumab: 140 eventos reconstruidos frente a 139 publicados; no se ha forzado coincidencia retroactiva. Requiere revisión de la adaptación del algoritmo y del límite de redondeo, aunque satisface el umbral contractual.
2. Tres controles de riesgo con -1 sujeto; no hay diferencia >1. Distribución intraintervalo de censuras no identificable, especialmente en tiempos cercanos a cero y en la cola.
3. Mediana SG-D depende de muy pocos sujetos en riesgo (D04 §6, tabla de riesgo PDF p.6). Los IC de pseudo-IPD no incluyen error de extracción/reconstrucción ni sustituyen incertidumbre clínica original.
4. No se cuenta con covariables de estratificación ni suplemento. HR/PH no estratificados y seguimiento son aproximaciones, no reproducción del modelo ajustado original.
5. Revisión independiente del coordinador pendiente; no se declara aceptación. Las pruebas unitarias y de integración se registran aparte.
6. E2.0 se ejecutó después de la primera validación clínica, a diferencia del orden enumerado en el contrato; no se presenta como validación cegada. La corrida parcial interrumpida de E2.0 no se archivó íntegramente antes del relanzamiento: se conservan código y stdout, no todos sus CSV originales. Las corridas clínicas originales sí están archivadas.

## Reproducibilidad y archivos

Comandos absolutos en `{root / 'REPRODUCIR.md'}`. Fuentes no modificadas, un solo hilo numérico y ejecuciones registradas con versión, fecha, duración, semillas y hashes. La corrida E2.0 síncrona inicial quedó interrumpida por el límite de herramienta y se relanzó sin cambios de diseño; véase registro de incidencias.

Resultados CSV en `{out}`; figuras PNG/SVG en `{root / 'figures'}`; código en `{root / 'src'}`; pruebas en `{root / 'tests'}`. Cada evaluación clínica conserva copia en logs. Solo el archivo de comunicaciones permitido se escribe fuera del directorio exclusivo.
'''
    (root/'INFORME_T02.md').write_text(report,encoding='utf-8')
    provenance=f'''# Procedencia T02

Todos los datos son derivados locales; los pseudo-IPD son aproximaciones, no datos individuales originales.

Fuentes solo lectura:
- PDF: `{Path(cfg['project_root'])/cfg['pdf_relative']}`. SHA-256 {hashlib.sha256((Path(cfg['project_root'])/cfg['pdf_relative']).read_bytes()).hexdigest()}. Fig.1A/1B p.6; Fig.2A/2B p.8; texto p.7 y leyendas pp.7/9.
- Tabla: `{Path(cfg['project_root'])/cfg['inputs_relative']}`. Fuente de cifras por fila. Solo filas autorizadas de reconstrucción; se ignoran las filas de extrapolación del archivo.
- Ficha D04 §4.2–4.4/7/8 y contrato T02 v1.0, ubicados en las rutas del contrato.

Familias de archivos en `{out}`:
- `segments_*.csv`: segmentos originales del trazado elegido, página, path_id y coordenadas PDF.
- `points_*.csv`: centros extraídos/calibrados de mesetas, saltos y fin del soporte.
- `censor_marks_*.csv`: rectángulos verticales deduplicados, sin inferencia de multiplicidad.
- `risk_pdf_*.csv`: riesgo transcrito por coordenadas de texto (no texto lineal desordenado).
- `pseudo_ipd_*.csv`: time_months, event, arm, endpoint; ningún identificador original; marginales independientes por desenlace.
- `intervals_*.csv`: decisiones de censura y redondeo de Guyot adaptado.
- `validation.csv`: cifras publicadas con fuente/página, reconstruidas, diferencias, tolerancia y clasificación.
- `curve_errors.csv`, `difference_*.csv`: errores calculados en soporte observado, paso 0,1 meses.
- `censor_coherence.csv`: marcas frente a salidas y censuras; no equivalencia uno a uno.
- `simulation_metrics.csv`, `simulation_summary.csv`, `simulation_populations.csv` y carpeta `simulation`: E2.0 sintético, diseño en config; semillas por fila, verdad conocida y reconstrucción. Son cifras de cálculo, no publicadas.

Los hashes de código/config se registran por ejecución. `manifest_sha256.csv` permite verificar entregables; excluye el propio manifiesto, cachés y logs de una ejecución todavía abierta. No publicar ni redistribuir fuentes.
'''
    (out/'PROCEDENCIA.md').write_text(provenance,encoding='utf-8')
    deliver=f'''# Entrega T02

Estado: entregada

Fecha: 10-oct-2026. Pendiente de revisión del coordinador; no aceptada.

## Entregables
- `{root / 'INFORME_T02.md'}`
- `{root / 'src'}` y `{root / 'tests'}`
- `{root / 'config/config.yaml'}`
- `{root / 'requirements_T02.txt'}`
- `{root / 'logs'}`
- `{out}` (coordenadas, pseudo-IPD, validación, simulación, procedencia)
- `{root / 'figures'}` (PNG + SVG)
- `{root / 'REPRODUCIR.md'}`
- `{root / 'CRITERIOS_PREESPECIFICADOS.md'}` y `{root / 'DECISIONES_METODO.md'}`

## Validación
{n_pass}/{len(h1)} cantidades H1 reproducidas; criterios contractuales sin cambios.

{table(h1[maincols])}

Riesgo: {risk_counts}. E2.0: 100 réplicas, 400 reconstrucciones; métricas completas en informe y CSV. Error de curva máximo global {maxpp:.6g} pp.

## Problemas abiertos
SLP-D 140 vs 139 eventos; tres riesgos con -1; revisión de adaptación de Guyot; tiempos individuales no identificables; fragilidad de cola; PH no directamente equivalente al análisis publicado. E2.0: {int(simulation.within_tolerance.sum())}/{int(simulation.evaluable.sum())} dentro de tolerancia, sin garantía fuera del diseño sintético. Ninguna corrección orientada a forzar concordancia.
'''
    (root/'ENTREGA_LISTA.md').write_text(deliver,encoding='utf-8')
    from round1 import append_report
    append_report(root,cfg)
    print('Report and delivery generated:',root/'INFORME_T02.md')