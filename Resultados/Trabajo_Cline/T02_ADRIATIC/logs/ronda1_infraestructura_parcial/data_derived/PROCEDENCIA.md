# Procedencia T02

Todos los datos son derivados locales; los pseudo-IPD son aproximaciones, no datos individuales originales.

Fuentes solo lectura:
- PDF: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Data_insumo\Durvalumab-after-Chemoradiotherapy-in-Limited-Stage-Small-Cell-Lung-Cancer.pdf`. SHA-256 44b9eb70e00ad09bd8d80c014b585dd85f6a2a8f1ac1e6b8bdd3d68503234d0c. Fig.1A/1B p.6; Fig.2A/2B p.8; texto p.7 y leyendas pp.7/9.
- Tabla: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\04_plan\tabla_insumos_E2_ADRIATIC.csv`. Fuente de cifras por fila. Solo filas autorizadas de reconstrucción; se ignoran las filas de extrapolación del archivo.
- Ficha D04 §4.2–4.4/7/8 y contrato T02 v1.0, ubicados en las rutas del contrato.

Familias de archivos en `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\data_derived`:
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
