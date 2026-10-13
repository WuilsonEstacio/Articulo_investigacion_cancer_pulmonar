# T04: auditoría de T02 (ADRIATIC, Cline)

| Campo | Valor |
|---|---|
| Auditor | Claude Code (coordinador) |
| Fecha | 11-oct-2026 (hora local) |
| Objeto | `Trabajo_Cline/T02_ADRIATIC/`, entrega de la ronda 1 (10-oct-2026), contrato T02 v1.0 |
| **Dictamen** | **Requiere corrección (ronda 1 de 2)** |

## 1. Qué se verificó y cómo

| # | Verificación | Método | Resultado |
|---|---|---|---|
| V1 | Reproducibilidad | Re-ejecución completa desde cero (`pipeline.py --stage all`) en una copia aislada del scratchpad, con el intérprete autorizado `venv_cline_T02`. Comparación byte a byte con la entrega | Termina con exit 0 en 146 s. Se compararon por SHA-256 1.248 archivos (`data_derived/`, incluidas las 1.200 réplicas de E2.0; `figures/`; `requirements_T02.txt`; `INFORME_T02.md`; `ENTREGA_LISTA.md`). Solo difieren 3 (`PROCEDENCIA.md`, `INFORME_T02.md` y `ENTREGA_LISTA.md`), y únicamente por las rutas absolutas impresas. Registro en `logs/rerun_pipeline_all.json` |
| V2 | Pruebas | `unittest discover` sobre la copia re-ejecutada | 14/14 OK |
| V3 | Tolerancias fijadas antes | `diff` entre la primera instantánea archivada (`logs/20261010_192418_*_source`) y los archivos actuales | `CRITERIOS_PREESPECIFICADOS.md` y `DECISIONES_METODO.md` idénticos. Las tolerancias de `config.yaml` coinciden con el contrato §5.2. El bloque de diseño de E2.0 se añadió entre la 2.ª y la 3.ª instantánea y ya estaba presente en la primera evaluación clínica (19:26:32) |
| V4 | Sin ajuste del método a posteriori | SHA-256 de `guyot.py` y `extract.py` en las 13 instantáneas registradas | Idénticos en todas (`77e64e25…` y `999d20ca…`) |
| V5 | Fugas (cifras publicadas como objetivo) | Lectura de `guyot.py`, `extract.py`, `pipeline.py`, `validate.py` y `simulate.py` | `reconstruct()` recibe solo la curva extraída, los números en riesgo y el total de eventos (este último es una entrada declarada en el contrato y en Guyot 2012). Medianas, tasas y HR se leen únicamente en `validate.py`, después de reconstruir. La calibración de ejes usa las etiquetas de los ticks y S(0)=1. **No hay fuga.** |
| V6 | Alcance | `grep` de RMST, modelos paramétricos, curación y extrapolación en `src/` | Nada fuera de alcance. `km.predict` solo se evalúa dentro del soporte observado |
| V7 | Coordenadas frente al PDF (pp. 6 y 8) | Extracción **ráster independiente** (`src/raster_check.py`): render a 16 px/pt, píxeles del color de cada brazo y ejes calibrados con las **marcas de tick vectoriales** (`src/ticks.py`), no con etiquetas de texto | Mediana \|ΔS\| 0,09–0,13 pp; p95 0,29–0,44 pp; entre el 96 y el 98,5 % de las columnas con \|ΔS\| < 0,5 pp (fuera de ±0,15 meses de cada salto). Los máximos (hasta 7,6 pp) se concentran donde la curva naranja tapa a la azul, a los 2–4 meses de la SLP, y donde se acumulan marcas de censura o leyendas; son artefactos del método ráster, no de Cline |
| V8 | Números en riesgo | Inspección visual del render de la p. 6 y coordenadas de palabras de las pp. 6 y 8 | Coinciden con `tabla_insumos_E2_ADRIATIC.csv` |
| V9 | Métricas de validación | KM y Cox **propios**, sin lifelines (`src/km_cox_indep.py`), sobre los pseudo-IPD entregados | Reproducen exactamente las 18 cantidades H1 (p. ej., HR Efron SG 0,73026 y SLP 0,77019; mediana SG-D 55,937) |

### 1.1 Por qué el ajuste es casi exacto (riesgo de calibración descartado)

El ajuste casi perfecto (115/115 eventos; mediana 55,94 frente a 55,9) se explica sin calibración:
1. las curvas son **vectoriales**, por lo que no hay error de digitalización manual;
2. el total de eventos y los números en riesgo son **entradas** del algoritmo, así que su reproducción no es una validación independiente (Cline lo declara);
3. las tasas hito y las medianas se heredan directamente de la curva extraída, que el propio artículo dibujó a partir de los datos reales.

La extracción ráster independiente confirma que la curva extraída coincide con el PDF.

## 2. Defectos encontrados

### D1 (corrección obligatoria): fusión de escalones en tramos empinados de la curva

- **Dónde:** `src/extract.py`, líneas 28–39. Una franja entre abscisas consecutivas solo cuenta como meseta si el grosor vertical del polígono es ≤ 0,55 pt. En los tramos en los que varios escalones caen en menos de ~0,5 pt horizontales (el grosor del trazo), las franjas superan ese umbral y se descartan. Todos los escalones intermedios se fusionan entonces en **un único salto**, situado en el centro del hueco.
- **Evidencia:** los segmentos vectoriales del trazado 334 (SLP placebo) entre x = 98,6 y 101,2 pt (t ≈ 3,24–3,87 meses) contienen unos 8 escalones distintos. Cline los convierte en un salto de 10,1 pp con **25 eventos empatados en t = 3,838**. `src/merged_steps.py` cuenta los niveles horizontales intermedios del polígono dentro de cada salto (`data_derived/saltos_fusionados.csv`).
- **Alcance:**

| Curva | Empate máximo | Saltos con ≥ 5 eventos empatados |
|---|---|---|
| SLP durvalumab | 31 (t = 1,84) | 6 (31, 23, 13, 10, 8, 5) |
| SLP placebo | 34 (t = 1,82) | 5 (34, 25, 21, 12, 9) |
| SG placebo | 6 | 4 (≤ 6) |
| SG durvalumab | 5 | 1 |

- **Efecto:**
  - las cantidades H1 siguen dentro de tolerancia;
  - la estructura temporal de los pseudo-IPD está distorsionada: los eventos de ventanas de ~0,5–1 mes quedan concentrados en un solo instante;
  - la HR de SLP se vuelve sensible al tratamiento de empates (Efron 0,770 frente a Breslow 0,775);
  - la mediana publicada de SLP-P (9,2) cae dentro de un salto fusionado (t = 9,09; 9 eventos).

  Como estos pseudo-IPD se usarán en fases posteriores, el defecto debe corregirse.
- **Corrección pedida:**
  - recuperar los escalones intermedios, por ejemplo derivando los niveles de meseta de los pares de bordes horizontales del polígono del trazo, separados ≈ 0,502 pt, en lugar de usar el criterio de grosor vertical;
  - añadir una prueba que compare el número de mesetas extraídas con el número de niveles del polígono;
  - documentar **primero** el resultado original y **después** el corregido;
  - re-ejecutar la validación **sin cambiar las tolerancias**;
  - informar del cambio en H1, en los empates y en la HR (Efron y Breslow).

### D2 (corrección obligatoria): E2.0 no incluye el paso de extracción

- El contrato (§5.1, paso 5) pide «aplicar KM, **extraer puntos** y reconstruir». `simulate.py`, en las líneas 45–47, pasa a `reconstruct()` las coordenadas **exactas** del KM simulado y se salta la extracción.
- Por eso E2.0 solo valida el algoritmo con una extracción perfecta: no podía detectar D1, y sus errores casi nulos (error de riesgo 0 en las 400 reconstrucciones) sobrestiman la exactitud del flujo completo.
- **Corrección pedida:**
  - conservar el E2.0 actual, etiquetado como «sin digitalización»;
  - añadir **E2.0b**: dibujar las curvas simuladas en un PDF vectorial con la geometría de la Fig. 1A (escala de ejes, trazo de 0,5 pt y marcas de censura), pasarlas por `extract.py` y reconstruir. Mismas semillas; 100 réplicas o, si el tiempo lo exige, las 20 primeras, declarándolo.

### Observaciones menores (documentar, sin corrección obligatoria)

- O1. SLP-D tiene 140 eventos reconstruidos frente a 139 publicados. Está dentro del ±3 % y Cline lo declara. Conviene revisarlo después de D1.
- O2. E2.0 se ejecutó después de la validación clínica. Está declarado y es aceptable.
- O3. El seguimiento entre censurados es informativo; el mínimo de SG-D da 1,0 frente a 0,1 meses. Se espera por la censura uniforme y no requiere acción.

## 3. Clasificación provisional de T02 (antes de la corrección)

- **18/18 cantidades H1:** «reproducido» según el contrato, verificado de forma independiente (V9).
- **Las curvas como insumo para fases posteriores:** el estado de la entrega es «requiere corrección» por D1 y D2.

Hasta cerrar la ronda de corrección, el resultado se integra con la etiqueta «reproducido con defecto de extracción documentado».

## 4. Archivos de esta auditoría

- `src/ticks.py`, `src/raster_check.py`, `src/merged_steps.py`, `src/km_cox_indep.py`: scripts propios (entorno `venv_claude_T01`, ejecutados con `python -I`).
- `data_derived/raster_vs_cline_*.csv` y `raster_vs_cline_resumen.json`: comparación columna a columna.
- `data_derived/saltos_fusionados.csv`: saltos con niveles intermedios.
- `data_derived/km_cox_indep.json`: KM y Cox propios.
- `logs/rerun_pipeline_all.json` y `logs/rerun_all_stdout.txt`: re-ejecución completa.
