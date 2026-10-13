# Contrato de tarea T02: reconstrucción y validación de las curvas de supervivencia de ADRIATIC

| Campo | Valor |
|---|---|
| **Identificador** | T02 |
| **Responsable** | **Cline** (CLI 3.0.70, proveedor `openai-codex`, modelo `gpt-6-astra`) |
| **Coordinación, auditoría e integración** | Claude Code |
| **Versión del contrato** | 1.0 (10-oct-2026) |
| **Estado** | ver `Coordinacion/ESTADO_TAREAS.md` |

## 1. Objetivo y alcance

Reconstruir **datos individuales aproximados** (pseudo-IPD) de las curvas de Kaplan–Meier publicadas en ADRIATIC y **validar** la reconstrucción contra todas las estadísticas publicadas.

Curvas incluidas:
- SG y SLP (revisión central independiente ciega, BICR).
- Durvalumab frente a placebo, población ITT.

**Fuera del alcance** (prohibido en esta fase):
- Extrapolar la supervivencia más allá de los datos observados.
- Ajustar modelos paramétricos, splines o modelos de curación.
- Calcular RMST.
- Analizar subgrupos.
- Reconstruir el brazo durvalumab + tremelimumab (cegado; no tiene curvas publicadas).
- Cualquier conclusión sobre eficacia clínica más allá de lo publicado.

> Los datos reconstruidos son una **aproximación**: **no** son los datos individuales originales del ensayo. No debe afirmarse que se recuperaron tiempos exactos de eventos o de censura.

## 2. Fuentes y ubicaciones (rutas absolutas; solo lectura)

Raíz del proyecto: `<PROJECT_ROOT>`

| Fuente | Ruta | Ubicaciones relevantes |
|---|---|---|
| Artículo ADRIATIC (Cheng et al., NEJM 2024;391:1313-27, doi:10.1056/NEJMoa2404873) | `Data_insumo\Durvalumab-after-Chemoradiotherapy-in-Limited-Stage-Small-Cell-Lung-Cancer.pdf` | **Fig. 1A, p. 6 del PDF** (SG; números en riesgo debajo); **Fig. 2A, p. 8 del PDF** (SLP); texto p. 7 (medianas, tasas, eventos, seguimiento); métodos p. 3–4 |
| Ficha de lectura (ya verificada visualmente) | `Resultados\02_matriz_evidencia\fichas\D04_ADRIATIC_2024.md` | §4.2–4.4 (cifras y números en riesgo transcritos), §7 (aptitud para reconstrucción, colores RGB de las curvas, advertencias), §8 (problemas de extracción) |
| Tabla de insumos y valores de validación | `Resultados\04_plan\tabla_insumos_E2_ADRIATIC.csv` | Todas las filas |
| Plan aprobado (experimento E2, solo E2.0–E2.2) | `Resultados\04_plan\Primera_entrega_contribuciones_y_plan.md` | Sección C, tabla "E2" |
| Método | Guyot P, Ades AE, Ouwens MJNM, Welton NJ. *Enhanced secondary analysis of survival data: reconstructing the data from published Kaplan-Meier survival curves.* BMC Med Res Methodol 2012;12:9 (doi:10.1186/1471-2288-12-9, acceso abierto) | Algoritmo con números en riesgo y número total de eventos |

**Advertencia ya documentada:** en el `.txt` extraído, los números en riesgo están desordenados. **Usa la ficha D04 §4.4 o extrae del PDF con coordenadas, nunca el `.txt`.**

## 3. Entradas autorizadas

- Los archivos de la sección 2, en **solo lectura**.
- Entorno Python aislado ya creado para ti: `<PAPERCANCER_ENV>\venv_cline_T02\Scripts\python.exe`. Contiene numpy 1.26.4, scipy 1.11.4, pandas 2.3.3, matplotlib 3.10.9, pymupdf 1.28.2, lifelines 0.30.0 y PyYAML 6.0.3; la lista completa está en `freeze_inicial.txt` de esa carpeta.
  - Puedes instalar paquetes adicionales **solo** en ese entorno y debes registrarlos.
  - No uses el Python global ni otros entornos.
- Puedes consultar el artículo de Guyot 2012 en la web (acceso abierto) para implementar el algoritmo correctamente. Cita la versión que uses.

## 4. Carpeta exclusiva y archivos modificables

- **Carpeta exclusiva:** `Resultados\Trabajo_Cline\T02_ADRIATIC\`. Puedes crear y modificar cualquier archivo **solo** dentro de ella.
- **Además, puedes añadir mensajes** (sin borrar los existentes) en `Resultados\Coordinacion\comunicaciones\cline_a_claude.md`.
- **Prohibido:** modificar o crear archivos en `Data_insumo\`, en `Resultados\` fuera de tu carpeta (salvo el archivo de comunicaciones), en `Paper_final\`, en `Trabajo_Claude\` o en `Integrado\`; modificar el entorno de Claude; usar git; publicar o subir nada a internet.

## 5. Métodos y criterios de aceptación (fijados ANTES de ver resultados)

### 5.1 Pasos

1. **Inventario de curvas.**
   - Identificar curvas, brazos, desenlaces, tiempos de los números en riesgo (0–63 meses cada 3), eventos totales y estadísticas publicadas.
   - Tabularlo con la página de origen.
2. **Extracción de coordenadas** (selección y justificación del método).
   - Método preferido: **extracción vectorial** de los trazados del PDF con PyMuPDF (`page.get_drawings()`), porque la ficha D04 §7 indica que las curvas son vectoriales (durvalumab naranja ≈ RGB (0.89, 0.62, 0.25); placebo azul ≈ (0.36, 0.53, 0.77)).
   - Calibrar los ejes con las etiquetas de la capa de texto (eje x 0–63 meses, eje y 0–100 %).
   - **Separar las marcas de censura** (segmentos verticales cortos del mismo color) de los escalones de la curva.
   - Guardar los puntos extraídos con la página, el identificador del trazado y las coordenadas en el PDF y en unidades del gráfico.
   - Si la extracción vectorial fallara, justificar el método alternativo y su error esperado.
3. **Comprobaciones de la extracción.**
   - Monotonía no creciente.
   - S(0) = 1.
   - Rango de tiempo.
   - Coherencia de las marcas de censura con los números en riesgo.
   - Comparar los valores de S(t) leídos en 24 y 36 meses (SG) y en 18 y 24 meses (SLP) con las tasas publicadas.
4. **Implementación del algoritmo de Guyot 2012** en Python, con pruebas unitarias.
5. **Validación del algoritmo con verdad conocida (E2.0).**
   - 100 conjuntos simulados con semillas registradas, con tamaño, censura y tabla de números en riesgo cada 3 meses similares a ADRIATIC.
   - Aplicar KM, extraer puntos y reconstruir.
   - Comparar con los datos verdaderos: error en eventos, en S(t) en los hitos, en mediana y en HR.
6. **Reconstrucción** de los 4 conjuntos (SG-D, SG-P, SLP-D, SLP-P) usando los números en riesgo y el número total de eventos por brazo (SG 115/146; SLP 139/169).
7. **Validación frente a lo publicado.**
   - KM reconstruido superpuesto a la curva extraída.
   - Números en riesgo reconstruidos frente a publicados en cada tiempo.
   - Eventos.
   - Medianas.
   - Tasas a 24 y 36 meses (SG) y a 18 y 24 meses (SLP).
   - HR de Cox **no estratificado** (lifelines) frente a la fila "All patients" del forest: SG 0,73 (IC 95 % 0,57–0,93); SLP 0,76 (0,61–0,95).
   - Comparación informativa con la prueba de riesgos proporcionales publicada (SG p = 0,91; SLP p = 0,79).
8. **Cuantificación del error.**
   - Error de digitalización: entre la curva extraída y su reconstrucción KM, como diferencia absoluta máxima y media de S(t) en una rejilla de 0,1 meses.
   - Error de reconstrucción: entre la estadística reconstruida y la publicada, y el obtenido en las simulaciones de E2.0.

### 5.2 Criterios de aceptación (preespecificados en el plan, sección C, E2, H1)

| Cantidad | Tolerancia | Justificación |
|---|---|---|
| Eventos totales por brazo | ±3 % | Guyot fuerza el total; la desviación solo procede del redondeo por intervalo |
| Tasas hito (SG 24/36; SLP 18/24) | ±2 puntos porcentuales | Error típico de digitalización y redondeo a 0,1 % |
| HR no estratificado | ±0,03 respecto a 0,73 / 0,76 | Diferencia esperada entre Cox estratificado y no estratificado + reconstrucción |
| Medianas | ±1 mes; **±3 meses** para la mediana de SG de durvalumab (55,9) | Esa mediana se sostiene con 5–11 pacientes en riesgo (ficha D04 §6) |
| Números en riesgo | Reportar la diferencia en cada tiempo | Coherencia interna; sin tolerancia fija, pero cualquier diferencia mayor de 1 debe explicarse |

Clasificación de cada cantidad: **reproducido** / **parcialmente reproducido** / **discrepancia** / **no evaluable**. **No ajustes el método después de ver los errores para que pasen las tolerancias.** Si cambias algo, documenta primero el resultado original y luego el cambio, con su justificación.

## 6. Entregables (en `Trabajo_Cline\T02_ADRIATIC\`)

1. `INFORME_T02.md`: métodos, decisiones justificadas, resultados, tabla de validación con clasificación, errores cuantificados, limitaciones y discrepancias.
2. `src/`: código ejecutable (extracción, Guyot, validación, simulación E2.0) y `tests/`.
3. `config/config.yaml`: rutas, páginas, colores, semillas y tolerancias.
4. `requirements_T02.txt`: salida de `pip freeze` del entorno al terminar.
5. `logs/`: registro de cada ejecución (fecha, comando, versión, semillas, duración).
6. `data_derived/`:
   - Puntos extraídos (CSV con procedencia: página, trazado, coordenadas).
   - Pseudo-IPD por curva (CSV con columnas `time_months`, `event`, `arm`, `endpoint`).
   - Tabla de validación (CSV).
   - `PROCEDENCIA.md`.
7. `figures/`: (a) curva extraída frente a KM reconstruido, por desenlace, con números en riesgo (PNG + SVG; unidades y fuente en el pie); (b) diferencias S_extraída − S_reconstruida frente al tiempo; (c) resultados de E2.0.
8. `REPRODUCIR.md`: comando(s) exactos para regenerar todo desde cero.

## 7. Restricciones

- No extrapolación, modelos de curación, paramétricos ni RMST (sección 1).
- No modificar las entradas. No redistribuir ni publicar nada.
- Las cifras deben proceder de fuentes con página o de cálculos registrados. Sin valores inventados.
- Semillas fijas y registradas para todo lo aleatorio.
- No paralelizar de forma masiva: el equipo tiene 14 CPU, compartidas con un cálculo del coordinador. Usa como máximo 4 procesos.
- Límite: dos rondas de corrección tras la revisión del coordinador.

## 8. Errores, dudas y estado

- Si encuentras una ambigüedad o un bloqueo, escribe un mensaje fechado en `Resultados\Coordinacion\comunicaciones\cline_a_claude.md` y continúa con lo que no dependa de ella. Usa una suposición conservadora y declárala.
- Al terminar, escribe `ENTREGA_LISTA.md` en tu carpeta con: lista de entregables, resumen de la validación, problemas abiertos y el texto "Estado: entregada".
- No marques nada como "aceptado": solo el coordinador acepta.
