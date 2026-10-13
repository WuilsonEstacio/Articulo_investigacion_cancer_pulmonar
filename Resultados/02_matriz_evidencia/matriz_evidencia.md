# Matriz de evidencia y revisión crítica

**Fecha:** 10-oct-2026. **Base:** fichas `fichas/D01…D10`, que contienen las citas textuales, la transcripción de ecuaciones y tablas y las ubicaciones completas.

**Etiquetas de evidencia** (sección 1 del encargo):
- **[PUB]** evidencia publicada.
- **[OBS]** datos observados.
- **[COMP]** resultado computacional publicado por los autores.
- **[HIP]** hipótesis.
- **[SUP]** supuesto o limitación del modelo.
- **[LECTOR]** cálculo o juicio nuestro.

Todavía no hay resultados computacionales propios del plan.

## 1. Matriz principal

Cadena: pregunta → fuente → método → datos → resultado → limitación → oportunidad.

| # | Pregunta | Fuente (ubicación) | Método | Datos | Resultado | Limitación | Oportunidad de investigación |
|---|---|---|---|---|---|---|---|
| M1 | ¿Reduce la TCBD la mortalidad por cáncer de pulmón frente a la radiografía de tórax? | D08 NLST [p. 8; Tablas 2–7, pp. 15–22] | ECA, 33 centros, 3 rondas anuales | 53 454 participantes de 55–74 años, ≥30 paquetes-año [OBS] | Reducción de mortalidad por cáncer de pulmón de 20,0 % (IC 95 % 6,8–26,7); 247 frente a 309 por 100 000 personas-año; mortalidad total −6,7 % [PUB] | Comparador radiografía; sobrediagnóstico no cuantificado; mediana de seguimiento 6,5 años (ficha D08 §7–8) | Datos tabulados por ronda, estadio y modo de detección, útiles para calibrar un modelo de historia natural (ficha D08 §9). Novedad baja: ya existen modelos CISNET con datos individuales (registro B06) |
| M2 | ¿Reduce la TC volumétrica la mortalidad frente a no cribar? | D09 NELSON [p. 7/508; Tablas 1–4, pp. 6–9] | ECA, 4 rondas con intervalos crecientes | 13 195 varones (+2594 mujeres) [OBS] | RR 0,76 (0,61–0,94) a 10 años en varones; mujeres 0,67 (0,38–1,14); positivos 2,1 % [PUB] | Umbrales volumétricos en suplemento no incluido; dos recuentos de muertes (ficha D09 §10) | Validación externa de un modelo calibrado con M1. Ya hecha con datos individuales por MISCAN-Lung (de Nijs 2025, registro B06) |
| M3 | ¿Mejora la consolidación con durvalumab tras QRT la SG y la SLP en CPCP limitado? | D04 ADRIATIC [p. 1, 6–8; Tabla 1 p. 5; Tabla 3 p. 12] | ECA fase 3 doble ciego; análisis intermedio | 530 pacientes (264/266); KM con números en riesgo en 22 tiempos [OBS] | SG HR 0,73 (IC 98,321 % 0,54–0,98); medianas 55,9 frente a 33,4 meses; SLP HR 0,76 (IC 97,195 % 0,59–0,98) [PUB] | Intermedio; madurez de SG 49,2 %; mediana del brazo durvalumab sostenida por 5–11 pacientes en riesgo (ficha D04 §6) | Reconstrucción de datos individuales, tiempo medio de supervivencia restringido (RMST) e incertidumbre estructural de la extrapolación. Novedad moderada-baja: hay ≥5 análisis de costo-efectividad con supervivencia reconstruida (registro B04) |
| M4 | ¿Describe un modelo de campo de fase la dinámica del CPCNP bajo anti-PD-1? | D02 (preprint) [pp. 3–12]; versión publicada MBE 2023 y su repositorio | Cahn–Hilliard + nutrientes + farmacocinética; calibración manual | 2 pacientes: P1 con 21 volúmenes, P2 con 11 [OBS, CSV público] | Ajuste "cualitativo"; contrafactual de dosis con umbral entre 18 y 23 % [COMP] | n = 2; sin función de pérdida, IC, identificabilidad ni predicción fuera de muestra; compensación λ_P^pro–λ_τ^eff admitida [p. 11] | **Reproducción + calibración objetiva + identificabilidad práctica + comparación con modelos parsimoniosos + predicción temporal fuera de muestra** (oportunidad C1) |
| M5 | ¿Explica la señalización EGFR–ERK la expansión del CPCNP en un modelo de agentes multiescala? | D10 [Tablas 1–3, pp. 3–5; Figs. 4–7, pp. 8–11] | ABM 2D + 20 ODE por célula | Ninguno (teórico; parámetros de otros tipos celulares [p. 12]) | Transición de fase en el umbral de EGF; desplazamiento con la sobreexpresión de EGFR [COMP] | Umbrales críticos no publicados; sin código; sin sensibilidad; una corrida por regla | **Auditoría de reproducibilidad del submodelo ODE** (oportunidad C3) |
| M6 | ¿Puede un gemelo digital multiescala predecir la respuesta del CPCNP a la RT? | D01 [pp. 13–23; Tabla 7 p. 18] | Hipermodelo discreto + LQ + TCP, entre otros | 1 paciente de pulmón (datos ya no accesibles [p. 29]) | Control tumoral predicho, coherente con TC sin tumor [COMP] | n = 1; código cerrado; incoherencias internas (ficha D01 §14) | Solo metodológica: estructura de cinética celular y TCP. **No reproducible** con lo publicado |
| M7 | ¿Qué modelos matemáticos de crecimiento y terapia existen para el cáncer de pulmón? | D06 [pp. 4–15]; D07 [pp. 7–12] | Revisiones narrativas sin método de búsqueda | Ninguno primario | Catálogo de ecuaciones (D06: 40 ecuaciones) [PUB] | Sin parámetros pulmonares (D06); valores ilustrativos o genéricos (D07); erratas en ecuaciones | Fuente de **formas funcionales** (Gompertz, log-kill, LQ, Emax) para los comparadores de C1. **No son fuente de parámetros** |
| M8 | ¿Qué terapias dirigidas existen y con qué eficacia? | D05 [Tabla 1 p. 2; secciones 3–13] | Revisión narrativa | Resultados de ensayos citados (unos 60) | Por ejemplo, FLAURA SLP 18,9 frente a 10,2 meses (HR 0,46); CodeBreaK200 HR de SG 1,01 [PUB, secundaria] | Tabla 1 sin fuentes; errores de cita; sin IC ni n por brazo | Sin respaldo suficiente para modelar resistencia a TKI: faltan dinámica clonal y frecuencias por tiempo (ficha D05) |
| M9 | ¿Predicen los organoides la respuesta clínica? | D03 [pp. 6–9] | Revisión narrativa | Cifras de estudios citados | Concordancia >80 % (ref. 56, sin métrica definida); establecimiento 41 % / 17 % "puros" (ref. 90) [PUB, secundaria] | Citas de colorrectal y vejiga usadas como apoyo; evidencia observacional | Sin respaldo para una simulación cuantitativa. Solo modelos ilustrativos de flujo de proceso |

## 2. Evaluación crítica por documento

| ID | Diseño y calidad | Muestra | Comparador / desenlaces / seguimiento | Incertidumbre, sesgos, confusión | Validación | Reproducibilidad | Coherencia con otros documentos |
|---|---|---|---|---|---|---|---|
| D08 | ECA de alta calidad; adherencia >90 % | 53 454; 41 % mujeres | Radiografía; mortalidad por cáncer de pulmón; mediana 6,5 años | El comparador activo subestima el efecto frente a no cribar; sobrediagnóstico no estimado | No aplica (ensayo) | Alta para cifras agregadas (tablas completas) | Distinto de D09 en comparador, población, protocolo y seguimiento (ficha D09 §8). **No son intercambiables** |
| D09 | ECA de alta calidad | 13 195 varones (análisis primario) | Sin cribado; mortalidad por cáncer de pulmón a 10 años | Solo ≈50 % cumpliría los criterios del NLST, y en ese subgrupo el RR es 0,82 (0,64–1,05) (ficha D09 §6); sobrediagnóstico de 8,9–19,7 % según horizonte | No aplica | Media: umbrales en el suplemento | Sin efecto sobre la mortalidad total (RR 1,01), a diferencia del NLST |
| D04 | ECA fase 3 de alta calidad, patrocinado; análisis intermedio | 530 (ITT D/P) | Placebo; SG y SLP; seguimiento mediano de SG 37,2 meses | Riesgo de sobrestimación por análisis intermedio; subgrupos sin p de interacción; más terapia posterior en el brazo placebo (47,7 % frente a 36,0 %) | No aplica | Alta para reconstrucción de datos individuales (curvas vectoriales y números en riesgo) | La SG del placebo (33,4 meses) supera las referencias históricas, como CONVERT (25,4–30,0 meses) [p. 11]. Es un efecto de selección declarado por los autores |
| D02 | Prueba de concepto; n = 2; preprint (hay versión publicada) | 2 pacientes; 21 y 11 volúmenes | Sin comparador; volumen visible | Calibración manual; un dato descartado (P2); parámetros fijos sin fuente; compensación entre parámetros | **Ninguna fuera de muestra** | Alta con la versión publicada (datos y código). Baja solo con el preprint | Las cifras del preprint difieren de la versión publicada (inventario, nota 1) |
| D10 | Simulación teórica | — | — | Una corrida por condición; 5 réplicas no mostradas [p. 8] | Solo cualitativa [pp. 10–12] | **Baja**: umbrales, paso de tiempo, semillas y código no publicados | Parámetros de otros sistemas celulares. D06 no cita este trabajo: la búsqueda de "Deisboeck" o "Wang Z" en su texto no da resultados |
| D01 | Desarrollo metodológico; validación anecdótica | 1 paciente de pulmón | — | Sin métricas de error; incoherencias (mediana fuera del rango intercuartílico; tiempo de duplicación de ≈338 frente a ≈370 días) | n = 1 | **Baja**: código y datos no accesibles | — |
| D06 / D07 | Revisiones narrativas sin método | — | — | Sesgo de selección no evaluable | — | No aplica | D06 cita a D07 [ref. 110]. Posible inversión ϕ/φ en D07 respecto a la fuente original (por verificar en Hahnfeldt 1999) |
| D05 / D03 | Revisiones narrativas sin método | — | — | Errores de cita (ficha D05; ficha D03, refs. 92–93) | — | No aplica | Coherentes con el v2 del reporte; no aportan datos primarios |

## 3. Extracción de modelos computacionales

El detalle completo (ecuaciones en LaTeX, variables, unidades y condiciones iniciales) está en las fichas indicadas.

| Elemento | D02 (campo de fase) | D10 (ABM EGFR) | D01 (hipermodelo CHIC) | D06 / D07 (revisiones) |
|---|---|---|---|---|
| Ecuaciones | Ecs. 1–13 transcritas (ficha D02 §4) | 20 ODE + 19 reacciones + difusión, ecs. 1–5 (ficha D10 §4) | LQ, TCP, ecs. 1–10, A1–A8 (ficha D01 §4) | 40 ecuaciones (D06); BioFVM, Hahnfeldt y Gatenby (D07) |
| Variables y unidades | φ_P, φ_N, φ_σ, φ_τ; unidades parcialmente ambiguas (φ_τ^50 en "mol") | Concentraciones en nM; tiempo y espacio sin unidades explícitas | Vóxeles de 1 u 8 mm³; horas | Parciales |
| Condiciones iniciales | No reportadas en el preprint; `initial_conditions.py` en el repositorio | Rejilla 7×7 de células semilla; gradientes gaussianos (anchuras no publicadas) | Desde TC | — |
| Parámetros y fuentes | 23 en Tabla 1; 4 calibrados; ~15 sin fuente (ficha D02 §5) | Cinéticas con fuente en modelos de otros tipos celulares; umbrales ausentes | Tabla 7 (pulmón) con rangos | **Sin valores pulmonares (D06)**; ilustrativos (D07) |
| Supuestos biológicos | Fármaco como escalar pulmonar; efecto Emax directo; nutrientes estacionarios; umbral de visibilidad 0,3 | Fenotipo según la tasa de cambio de PLCγ y ERK | Jerarquía stem/LIMP/DIFF; LQ a 15 Gy por fracción | — |
| Calibración | Manual (preprint); el repositorio incluye mínimos cuadrados | Ninguna | Restricciones con Ki-67 y tiempo de duplicación | — |
| Validación | Ninguna fuera de muestra | Cualitativa | Anecdótica (n = 1) | — |
| Sensibilidad e incertidumbre | **Local** en la versión publicada (Tabla 2); sin global, sin incertidumbre, sin identificabilidad | Ninguna | Escenarios (rango intercuartílico) | — |
| Resultados reproducibles | PK exacta; ajustes 1D con datos y código públicos; Tabla 2 de sensibilidad | Submodelo ODE (Tablas 1–2), probablemente cualitativo | No reproducible | Formas funcionales |

## 4. Síntesis de coherencias y contradicciones

1. **Cribado.** NLST y NELSON coinciden en una reducción relativa de la mortalidad por cáncer de pulmón de ~20–24 % [D08 p. 8; D09 p. 7]. Difieren en mortalidad total, comparador, protocolo y población. Cualquier modelo calibrado con uno y validado con el otro debe representar explícitamente esas diferencias de diseño.
2. **CPCP frente a CPCNP.**
   - El único dato clínico de tratamiento del CPCP es D04 (consolidación tras QRT, estadio limitado). D07 aporta cifras históricas de supervivencia de otra época y con otras definiciones [D07 p. 3]. **No se combinarán.**
   - D02 es CPCNP avanzado bajo anti-PD-1. **No se usará para inferir nada sobre CPCP.**
3. **Parámetros.** Ningún insumo aporta parámetros cinéticos de pulmón con fuente primaria y validación, salvo la farmacocinética de los anticuerpos (vida media y masa molar en D02, con referencia [16]) y las tablas de D01 (n = 1). Esto limita qué simulaciones mecanicistas se pueden justificar (sección C del plan).
4. **Versiones.** D02 (preprint) frente a MBE 2023: los parámetros calibrados y los coeficientes de consumo de nutrientes cambian. Toda reproducción debe referirse a la versión publicada.
