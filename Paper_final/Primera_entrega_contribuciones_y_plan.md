# Primera entrega: posibles contribuciones y plan de simulaciones

**Proyecto:** Paper_Cancer, cáncer de pulmón. **Fecha:** 10-oct-2026. **Estado (13-oct-2026):** plan aprobado. Ejecutados F0–F1 de E1 (más la variante corregida T06) y E2.0–E2.2. El resto no se ha ejecutado. Detalle en la **sección E**.


**Base documental:**
- 10 artículos de `Data_insumo` (inventario en `01_inventario/`; fichas y matriz en `02_matriz_evidencia/`).
- Búsquedas externas registradas en `03_registro_busquedas/`.

**Etiquetas:**
- **[PUB]** evidencia publicada.
- **[OBS]** dato observado.
- **[COMP]** resultado computacional publicado por otros.
- **[HIP]** hipótesis nuestra pendiente de evaluar.
- **[SUP]** supuesto o limitación.
- **[LECTOR]** cálculo o juicio de la revisión.

> **Declaración de transparencia.** Durante la lectura, tres lectores hicieron comprobaciones numéricas breves que no estaban planificadas. No son resultados del plan y no se usan como evidencia; los scripts se conservan en `99_verificaciones_exploratorias_lectores/`. Fueron:
> (i) reproducción analítica de la farmacocinética de D02;
> (ii) integración de las ODE publicadas de D10;
> (iii) extracción de coordenadas vectoriales de figuras (D02, D04, D09) para verificar transcripciones.
> El resultado (ii) se menciona más abajo solo para explicar por qué el experimento E3 incluye un punto de decisión, y se tratará como hipótesis a contrastar.

---

## A. Resumen de lo que sabemos

### A.1 Conclusiones respaldadas por los insumos

1. **El cribado con TC reduce la mortalidad por cáncer de pulmón en poblaciones de alto riesgo.**
   - NLST: reducción relativa del 20,0 % (IC 95 % 6,8–26,7) frente a radiografía de tórax, con 53 454 participantes y mediana de seguimiento de 6,5 años [PUB; D08 p. 8].
   - NELSON: RR 0,76 (0,61–0,94) a 10 años en 13 195 varones frente a no cribar [PUB; D09 p. 7/508].
   - El NLST además redujo la mortalidad total un 6,7 % [D08]; NELSON no la cambió (RR 1,01) [D09].
2. **El cribado tiene costes documentados.**
   - NLST: positividad del 24,2 % de las pruebas, con un 96,4 % de falsos positivos entre los positivos [PUB; D08 p. 1, Tabla 3].
   - NELSON reportó un 2,1 % de positivos gracias al manejo volumétrico, y un sobrediagnóstico estimado de 8,9 % a 11 años y 19,7 % a 10 años [PUB; D09; ficha D09 §5].
3. **En CPCP de estadio limitado sin progresión tras QRT concurrente, la consolidación con durvalumab prolongó la SG y la SLP en un análisis intermedio.**
   - SG: HR 0,73 (IC 98,321 % 0,54–0,98).
   - SLP: HR 0,76 (IC 97,195 % 0,59–0,98).
   - n = 530 [PUB; D04 p. 1, 7].
4. **En CPCNP con alteraciones accionables, varias terapias dirigidas mejoran la SLP frente a sus comparadores.** Por ejemplo, FLAURA: 18,9 frente a 10,2 meses, HR 0,46. Hay excepciones en SG, como CodeBreaK200 con HR 1,01 [PUB secundaria; D05]. Esta evidencia procede de una revisión narrativa con errores de cita (ficha D05) y debe verificarse en los ensayos originales antes de usarla cuantitativamente.

### A.2 Dónde hay incertidumbre

- **ADRIATIC es provisional.**
  - Madurez de SG del 49,2 %.
  - La mediana de SG con durvalumab (55,9 meses) depende de la cola de la curva, con entre 11 y 5 pacientes en riesgo entre los meses 54 y 57 [LECTOR; ficha D04 §6].
  - La SLP alcanzó significación solo tras reciclar alfa [D04 p. 3].
  - No se encontró un análisis final publicado (registro W01, B05); hay que volver a verificarlo.
- **Los ensayos de cribado no son intercambiables.** Difieren en comparador, población (solo ≈50 % de NELSON cumpliría los criterios del NLST), sexo, protocolo y seguimiento (ficha D09 §8).
- **Modelos mecanicistas de tratamiento en pulmón: evidencia débil.**
  - D02: n = 2, calibración manual, sin validación fuera de muestra.
  - D01: n = 1 y datos ya no accesibles.
  - D10: teórico, con umbrales críticos no publicados y sin código.
  - Las revisiones D06 y D07 no aportan parámetros pulmonares con fuente primaria.
- **Organoides (D03) y resistencia a TKI (D05):** solo hay evidencia secundaria, insuficiente para modelos cuantitativos.

### A.3 Problemas abiertos (respaldados por los insumos)

- **Estimación de parámetros e identificabilidad en modelos individualizados.** Los propios autores de D02 lo señalan:
  - "the parameter estimation should be addressed in particular" [D02 p. 12].
  - "[λ_P^pro y λ_τ^eff] are hard to determine" [D02 p. 11].
- **Predicción, no solo ajuste.** "inferred over the whole simulation time, including the clinical outcomes" [D02 p. 12].
- **Reproducibilidad de modelos multiescala.** D10 no publica umbrales, código ni semillas [ficha D10 §11–12]. El código de D01 está cerrado [D01 p. 29].
- **Supervivencia a largo plazo tras la consolidación en CPCP limitado.** Es desconocida con los datos actuales [ficha D04 §6]. Además, dos análisis de costo-efectividad del mismo ensayo eligen distribuciones distintas (log-normal y Weibull) para extrapolar (registro B18).

### A.4 Hallazgo de la revisión que condiciona el plan

El PDF de D02 de la carpeta es el **preprint arXiv v1**. La **versión publicada** (Wagner et al., *Math Biosci Eng* 2023;20:18670–94) cambia parámetros calibrados (por ejemplo, λ_τ^eff del P1 pasa de 4,49 a 5,2; α_H y α_P quedan intercambiados), añade un análisis de sensibilidad local (Tabla 2) y **publica datos y código**: `github.com/wagnandr/immunotherapy-lung-cancer`.
- Los volúmenes del CSV coinciden exactamente con la digitalización independiente de la Fig. 1 del preprint (21/21 y 11/11) [LECTOR; inventario, nota 1].
- Esto convierte a D02 en el **único insumo con datos de pacientes, código y resultados publicados contra los que se puede reproducir**.

---

## B. Oportunidades de contribución

Con respaldo suficiente se identifican **cuatro** oportunidades. No se propone una quinta: las demás líneas posibles (organoides, resistencia a TKI, gemelo digital de D01, modelos de las revisiones D06 y D07) **no tienen datos ni parámetros primarios** en los insumos (matriz §1, M6–M9).

### C1. Reproducción independiente, identificabilidad y valor predictivo de un modelo de campo de fase de CPCNP bajo anti-PD-1 (D02 / Wagner et al. 2023)

| Aspecto | Contenido |
|---|---|
| **Problema científico** | Un modelo espacial con unos 20 parámetros se calibró a mano a 2 pacientes (21 y 11 volúmenes) sin función de pérdida, incertidumbre ni predicción fuera de muestra. No se sabe si los parámetros específicos de cada paciente están determinados por los datos, ni si el modelo predice mejor que alternativas más simples |
| **Evidencia** | Calibración manual [D02 p. 7, 9; MBE p. 10, 12]; compensación λ_P^pro–λ_τ^eff admitida [D02 p. 11]; los autores piden abordar la estimación de parámetros [D02 p. 12]; solo sensibilidad local [MBE ec. 4.1, Tabla 2, pp. 16–17]; datos y código públicos (registro Q05); ninguna cita indexada que lo reproduzca (registro B02) |
| **Aporte** | (1) Reproducción independiente: código original y reimplementación propia, con verificación entre ambos. (2) Calibración objetiva por verosimilitud. (3) Identificabilidad práctica con perfiles de verosimilitud. (4) Comparación con modelos ODE parsimoniosos con la misma farmacocinética. (5) Evaluación de la predicción temporal fuera de muestra |
| **Reproducción frente a extensión** | **Reproducción:** curvas de φ_τ (farmacocinética), trayectorias 1D del volumen visible para P1 y P2 con los parámetros de MBE Tabla 1, e índices de sensibilidad de MBE Tabla 2. **Extensión:** puntos (2) a (5) |
| **Datos y parámetros disponibles** | CSV de volúmenes (P1: 21 tiempos, 0–2346 d; P2: 11 valores, 114–1266 d); MBE Tabla 1 (`tabla_parametros_E1_phasefield.csv`); esquemas de dosis [MBE p. 8 (P1) y p. 10 (P2)]; código 1D y 3D |
| **Información faltante** | Valor de φ_σ,v en 1D, condición inicial, función de corte y desfase temporal (en el código, por confirmar). Error de medición de la volumetría por TC (no reportado: se estimará con los datos [SUP]). Licencia del código (no hay). Texto completo de Scibilia et al. 2024 (registro B01, B19) |
| **Viabilidad** | Alta para 1D: Docker Desktop y conda disponibles para FEniCS 2019.1.0; 14 CPU. Coste medido en F0: la referencia 1D de P1 tarda unos 21 min, y la Tabla 2 completa, 309 min con 8 CPU (en una imagen Docker propia de conda-forge). El 3D queda fuera del alcance |
| **Limitaciones y alcance** | **n = 2**: conclusiones solo metodológicas, sobre identificabilidad y predicción en estos casos. **Sin validez clínica** y sin generalización a otros pacientes, fármacos ni histologías. Los datos incluyen la anotación de metástasis por el CAD [MBE p. 7]; no son volúmenes de un único tumor [SUP] |
| **Cómo comprobar que no está resuelto** | (a) Leer el texto completo de Scibilia et al. 2024 (*Math Biosci*, de pago) para ver si usa estos pacientes y compara con el campo de fase. (b) Repetir `CITES:38052574` y revisar Google Scholar justo antes de redactar. (c) Escribir a los autores (Wagner, Schlicke) para confirmar el uso de los datos y si existe trabajo posterior |

### C2. Reconstrucción exacta de ADRIATIC e incertidumbre estructural de la supervivencia a largo plazo (D04)

| Aspecto | Contenido |
|---|---|
| **Problema científico** | La SG a largo plazo y una posible fracción curada tras durvalumab son desconocidas [ficha D04 §6]. Los análisis económicos publicados extrapolan con una sola distribución elegida de forma heterogénea (log-normal en Tsai 2025; Weibull en TLCR 2025), digitalizada a mano (registro B18). La mediana de SG del brazo durvalumab es frágil |
| **Evidencia** | Curvas KM vectoriales con números en riesgo en 22 tiempos, eventos, medianas, tasas hito y HR [D04 pp. 6–8; ficha §4.4, §7]; registro B04, B15, B18 |
| **Aporte** | (1) Extracción exacta de las coordenadas vectoriales en lugar de digitalización manual. (2) Reconstrucción de datos individuales (Guyot 2012) **validada** contra eventos, medianas, tasas y HR publicados. (3) RMST a 24, 36 y 48 meses como resumen robusto. (4) Conjunto de modelos paramétricos, splines y de curación con **validación temporal interna** (ajuste con datos hasta el mes 24 y contraste con el KM de los meses 24–42). (5) Rango de SG a 5 y 10 años y posición de las elecciones de los análisis económicos publicados dentro de ese rango |
| **Reproducción frente a extensión** | **Reproducción:** HR, medianas y tasas a 24/36 meses de SG y 18/24 meses de SLP. **Extensión:** puntos (3) a (5) |
| **Datos disponibles** | `tabla_insumos_E2_ADRIATIC.csv`; PDF de D04 (solo lectura) |
| **Información faltante** | Suplemento (número de eventos objetivo, fracción de información); análisis final de SG (no encontrado); métodos de los otros 3 análisis económicos |
| **Viabilidad** | Muy alta: cálculo ligero (Python y `lifelines`, por instalar en un entorno aislado) |
| **Limitaciones y alcance** | Los datos reconstruidos son aproximados; el análisis es intermedio; la cola tiene menos de 20 pacientes en riesgo tras el mes 51. **Solo CPCP limitado tras QRT concurrente.** No genera evidencia nueva de eficacia: cuantifica qué es compatible con los datos y cuánto depende la extrapolación del modelo elegido |
| **Cómo comprobar que no está resuelto** | Revisar los 3 análisis económicos restantes y buscar en actas 2025–2026 un análisis final. Si existe un corte de datos posterior, C2 se reorienta a **validación externa de las extrapolaciones** con ese corte (más fuerte) |

### C3. Auditoría de reproducibilidad del submodelo de señalización EGFR–ERK de un modelo de agentes multiescala de CPCNP (D10)

| Aspecto | Contenido |
|---|---|
| **Problema científico** | ¿Se puede reproducir con lo publicado la dinámica intracelular que gobierna las decisiones fenotípicas del modelo (tasas de cambio de PLCγ y ERK, Fig. 6)? |
| **Evidencia** | Tablas 1–2 completas (20 ODE, 19 reacciones) [D10 pp. 3–4]; umbrales y código ausentes [ficha D10 §11–12]; parámetros de otros tipos celulares [D10 p. 12]; posibles incoherencias de unidades y de conservación [ficha D10 §10]; 60 citas sin replicación detectada (registro B07, no exhaustivo) |
| **Aporte** | Informe de reproducibilidad del submodelo ODE: reproducción, diagnóstico de discrepancias contra las fuentes primarias de los parámetros y análisis de sensibilidad de las tasas de cambio usadas como disparadores fenotípicos |
| **Reproducción frente a extensión** | **Reproducción:** respuesta de PLCγ y ERK-PP al EGF y magnitud de las tasas de cambio (Fig. 6). **Extensión (condicionada):** sensibilidad global e inhibición del receptor (TKI) en el submodelo |
| **Información faltante** | Fuentes primarias de los parámetros (refs. 11, 12, 14 y 39 de D10); umbrales T_PLC y T_ERK; unidades de tiempo de la Fig. 6 |
| **Viabilidad** | Alta para las ODE. **No se propone reproducir el ABM completo**: le faltan parámetros esenciales |
| **Limitaciones y alcance** | Contribución metodológica (reproducibilidad), sin implicaciones biológicas ni clínicas directas. El modelo es de 2007 y no incluye TKI ni mutaciones |
| **Cómo comprobar que no está resuelto** | Revisar los 60 trabajos que lo citan y ReScience C (registro, pendiente 4) |

### C4. Modelo de historia natural y cribado calibrado con NLST y validado con NELSON (D08, D09). **No recomendado como contribución principal**

| Aspecto | Contenido |
|---|---|
| **Problema** | Validar externamente un modelo de cribado entre ensayos de distinto diseño |
| **Evidencia** | Tablas por ronda, estadio y modo de detección en ambos ensayos [fichas D08 §9, D09 §9] |
| **Por qué no se recomienda** | (1) Ya existe con datos individuales y modelos validados: MISCAN-Lung reproduce NELSON (de Nijs 2025) y hay análisis de heterogeneidad con datos individuales de ambos ensayos (Welz 2025) (registro B06, B08). (2) Hacen falta parámetros de historia natural (tiempo de estancia preclínica, sensibilidad por tamaño, crecimiento) que **no están en los insumos** y habría que tomar de fuentes externas (perfiles CISNET). Con datos agregados la identificabilidad sería pobre |
| **Qué sí sería posible** | Un ejercicio didáctico y reproducible, clasificado como **exploratorio**, si el proyecto necesitara capacidad interna de modelado del cribado (por ejemplo, para adaptarlo a Latinoamérica, como Salgado 2026 en Argentina, registro B06) |

---

## C. Plan de simulaciones en Python

Reglas comunes a todos los experimentos:
- Configuración separada del código (YAML).
- Semillas registradas.
- Entorno fijado (`environment.yml` o `requirements.txt` con versiones; contenedor para FEniCS).
- Registro de cada ejecución (hash de configuración, fecha, versión del código, tiempo).
- Resultados en CSV o Parquet y figuras en PNG + SVG.
- Métricas y criterios definidos **antes** de ver los resultados.
- Resultados negativos conservados.
- Salidas en `Resultados/05_experimentos/E*/`.

### E1. Campo de fase de CPCNP bajo anti-PD-1: reproducción, calibración, identificabilidad, comparadores y predicción (C1)

| Campo | Contenido |
|---|---|
| **Pregunta** | (Q1) ¿Se reproducen los resultados publicados con los datos y el código públicos? (Q2) ¿Están identificados en la práctica los parámetros específicos de cada paciente? (Q3) ¿Aporta el modelo espacial mejor ajuste penalizado o mejor predicción que modelos ODE más simples con la misma farmacocinética? |
| **Hipótesis** | **H1 (reproducción):** el código original con los parámetros de MBE Tabla 1 reproduce los índices g de MBE Tabla 2 con error relativo ≤10 %, y nuestra reimplementación reproduce las trayectorias del código original (error relativo L2 ≤5 %). **H2 [HIP]:** con calibración por verosimilitud, el par (λ_P^pro, λ_τ^eff) **no** es identificable en la práctica en P2 (perfil sin cierre por ambos lados al nivel del 95 %). Deriva de D02 p. 11. **H3 [HIP]:** un modelo de Gompertz con muerte Emax impulsada por la misma farmacocinética obtiene un AICc igual o menor que el modelo de campo de fase 1D en P1 y P2. Deriva de Ghaffari Laleh 2022 (registro B16) y del carácter "cualitativo" del ajuste [D02 p. 1]. **H4 [HIP]:** en predicción temporal fuera de muestra, el campo de fase no reduce el error frente a los comparadores ODE. Las hipótesis H2–H4 se evaluarán sin preferencia por un resultado concreto |
| **Fundamento** | D02 pp. 3–13 (ecuaciones y supuestos); MBE 2023 Tabla 1 p. 6, texto pp. 8–12 y Tabla 2 pp. 16–17; repositorio (registro Q05); ficha D02 §5, §7, §9, §13–14; D06 ecs. 4–6 (formas de crecimiento; corregir la errata de la ec. 6 según la ficha D06) |
| **Modelo** | (a) **Modelo 1D radial de los autores**: ecs. 3, 6–10 [D02 p. 5], parámetros de MBE, FEM P1 y FEniCS 2019.1.0. (b) **Reimplementación independiente** en Python con elementos finitos 1D en coordenadas esféricas (numpy/scipy o scikit-fem), mismo esquema semi-implícito con descomposición convexo-cóncava [D02 p. 13]. (c) **Comparadores ODE** para el volumen V(t), todos con el término de muerte de la ec. 2 de D02 (λ_τ^eff/ω · φ_τ/(φ_τ+φ_τ^50)) y la farmacocinética de la ec. 6: M-exp dV/dt = rV − k·E(t)·V; M-Gompertz dV/dt = rV ln(K/V) − k·E(t)·V; M-logístico dV/dt = rV(1−V/K) − k·E(t)·V, donde E(t) = φ_τ/(φ_τ+φ_τ^50). (d) **Verosimilitud**: error multiplicativo log-normal, log V_obs = log V_mod + ε con ε ~ N(0, σ²) y σ estimado [SUP: no hay error de medición reportado]. (e) Perfiles de verosimilitud (Raue et al., *Bioinformatics* 2009) |
| **Datos** | CSV del repositorio. P1: 21 volúmenes; se usarán los que caen en la ventana de simulación de los autores (19 según la ficha D02 §6) y, como sensibilidad, los 21. P2: 11 valores; análisis principal sin el primero, como los autores [MBE p. 12], y sensibilidad con él. Calidad: volumetría CAD en TC rutinaria que incluye nódulos sospechosos bajo el umbral habitual [MBE p. 7]; embolia pulmonar que afecta la calidad en P1 [D02 p. 7] |
| **Parámetros** | `tabla_parametros_E1_phasefield.csv`: valores, unidades, rol (fijo, estimado o discreto) y fuente. Estimados: λ_P^pro, λ_τ^eff y λ_PN (y el volumen inicial si el código lo requiere). λ ∈ {1, 2} se analiza por separado. Rangos de búsqueda: λ_P^pro [10⁻⁴, 5] d⁻¹; λ_τ^eff [10⁻², 50] d⁻¹; λ_PN [10⁻³, 50] d⁻¹. Son amplios y en escala logarítmica, centrados en los valores publicados [SUP] |
| **Comparador** | Parámetros manuales de los autores (MBE Tabla 1); comparadores ODE (M-exp, M-Gompertz, M-logístico); modelo nulo de volumen constante |
| **Experimento** | **E1.0** Entorno y tiempos: una corrida 1D de P1 con el código original; medir el tiempo de cómputo. **E1.1** Farmacocinética: reproducir φ_τ(t) (picos y valles periódicos). **E1.2** Reproducir MBE Tabla 2 (diferencia central con h = α·10⁻³ [MBE p. 16]) y las trayectorias 1D de P1 y P2. **E1.3** Reimplementación y verificación entre códigos, más convergencia en malla (250/500/1000 elementos) y en paso de tiempo (1/12, 1/24, 1/48 d). **E1.4** Calibración por máxima verosimilitud con arranques múltiples (≥20, semillas registradas) para cada λ ∈ {1, 2}. **E1.5** Perfiles de verosimilitud de cada parámetro estimado. **E1.6** Ajuste de los comparadores ODE con la misma verosimilitud; AICc y BIC. **E1.7** Predicción con origen móvil: calibrar con los datos hasta t_k y predecir los 1–3 puntos siguientes, para k desde el 6.º punto. Se mantienen fijos los parámetros "fijos" de la Tabla 1, la farmacocinética y el umbral de visibilidad 0,3; en un análisis de sensibilidad aparte se varía el umbral (0,2 y 0,4) y la condición inicial |
| **Evaluación** | **H1:** se acepta si el error relativo de los índices g es ≤10 % en al menos 80 % de las entradas de la Tabla 2 y la verificación entre códigos da ≤5 % de error relativo L2 en V_vis(t). **H2:** identificable en la práctica si el perfil cruza el umbral χ²₁(0,95)/2 = 1,92 de log-verosimilitud a ambos lados dentro del rango de búsqueda. **H3:** diferencia de AICc mayor de 2 a favor de un modelo; si |ΔAICc| ≤ 2, equivalencia. **H4:** error medio absoluto en log-volumen de las predicciones a 1 paso, con comparación pareada por punto. **No se aplican pruebas de significación con n = 2 pacientes**: los resultados se presentan por paciente |
| **Validación** | Verificación: farmacocinética analítica, convergencia y comparación entre códigos. Validación interna: predicción temporal fuera de muestra. **No hay validación externa posible** (no hay otros pacientes con datos públicos). Para ello se necesitarían los datos de Vivli usados en Ghaffari Laleh 2022 o colaborar con el grupo de Múnich |
| **Gráficas** | (1) Datos frente a trayectorias reproducidas (autores frente a nuestra) por paciente, con eje de días y volumen en cm³, eventos de terapia marcados y fuente "CSV del repositorio". (2) Barras de los índices g reproducidos frente a los publicados (Tabla 2). (3) Curvas de convergencia. (4) Perfiles de verosimilitud con el umbral del 95 %. (5) Superficie o contorno de log-verosimilitud λ_P^pro × λ_τ^eff para mostrar la compensación. (6) Ajustes de los comparadores ODE y tabla de AICc. (7) Predicción con origen móvil: predicho frente a observado y error por horizonte |
| **Incertidumbre** | Intervalos por perfil de verosimilitud (condicionados al modelo y al supuesto de error log-normal). Bandas de predicción por bootstrap paramétrico (≥200 réplicas, semillas registradas). **Estas bandas representan incertidumbre de parámetros bajo el modelo, no un intervalo de confianza clínico** |
| **Reproducibilidad** | Código original en contenedor (`fenics 2019.1.0`), con fecha y hash del commit del repositorio registrados. Nuestro código en `05_experimentos/E1/` con `config/*.yaml`, `environment.yml`, `run_*.py`, registro JSON por ejecución y semillas. **No se redistribuirá el código de los autores** (sin licencia): se documentará cómo obtenerlo |
| **Alcance** | Permite concluir sobre reproducibilidad, identificabilidad y desempeño predictivo **en estos dos pacientes y bajo los supuestos declarados**. **No** permite concluir sobre eficacia ni dosis de inmunoterapia, ni generalizar a otros pacientes con CPCNP. Las simulaciones contrafactuales de dosis de los autores **no** se evaluarán como predicciones clínicas |

### E2. ADRIATIC: reconstrucción validada, RMST e incertidumbre estructural de la extrapolación (C2)

| Campo | Contenido |
|---|---|
| **Pregunta** | (Q1) ¿Se pueden reconstruir datos individuales aproximados que reproduzcan los estadísticos publicados? (Q2) ¿Qué diferencia de RMST es compatible con los datos? (Q3) ¿Cuánto varía la SG a 5 y 10 años según el modelo de extrapolación, y qué modelos predicen mejor el tramo observado no usado para ajustar? |
| **Hipótesis** | **H1 (reproducción):** la reconstrucción reproduce los eventos (±3 %), las tasas hito (±2 puntos porcentuales), el HR no estratificado (±0,03 respecto a la fila del forest: 0,73 y 0,76) y las medianas (±1 mes; ±3 meses para la mediana de SG con durvalumab, por su fragilidad). **H2 [HIP]:** la SG a 5 años extrapolada varía más de 10 puntos porcentuales entre los modelos con AIC dentro de 4 unidades del mejor. **H3 [HIP]:** los modelos ajustados con datos hasta el mes 24 difieren en su error de predicción del KM de los meses 24–42 |
| **Fundamento** | D04 pp. 1–9, 11 (resultados, métodos, limitaciones); ficha D04 §4.4, §6, §7; registro B04, B15, B18 |
| **Modelo** | Reconstrucción: algoritmo de Guyot et al., *BMC Med Res Methodol* 2012;12:9, implementado en Python y probado con datos simulados de verdad conocida. Supervivencia: Kaplan–Meier; Cox no estratificado; RMST; paramétricos (exponencial, Weibull, Gompertz, log-normal, log-logístico, gamma generalizada); splines de Royston–Parmar (1–3 nodos); curación mixta (Weibull y log-normal). Ajuste **por brazo**, para no imponer riesgos proporcionales |
| **Datos** | Coordenadas vectoriales de las curvas (D04 pp. 6 y 8, solo lectura), números en riesgo y totales de eventos (`tabla_insumos_E2_ADRIATIC.csv`). Calidad: alta en la extracción y limitada en la cola (menos de 20 en riesgo después del mes 51) |
| **Parámetros** | Los de cada distribución, estimados por máxima verosimilitud. No hay parámetros biológicos externos |
| **Comparador** | Estadísticos publicados (para H1); distribuciones elegidas por Tsai 2025 (log-normal) y TLCR 2025 (Weibull) (para H2) |
| **Experimento** | **E2.0** Validar el algoritmo de Guyot con 100 conjuntos simulados de verdad conocida (semillas registradas). **E2.1** Extraer coordenadas y separar las marcas de censura; prueba de coherencia con los números en riesgo. **E2.2** Reconstruir los 4 brazos y desenlaces y validar contra la tabla de insumos. **E2.3** RMST a 24, 36 y 48 meses y su diferencia; diagnóstico de riesgos proporcionales (Grambsch–Therneau) frente al p publicado. **E2.4** Ajustar el conjunto de modelos con todos los datos; AIC y BIC; SG y SLP a 5 y 10 años; media restringida a 10 años. **E2.5** Validación temporal: censura administrativa artificial en el mes 24, reajuste y comparación con el KM reconstruido en los meses 24–42 (error absoluto integrado y error a 36 meses). Se mantienen fijos los datos reconstruidos de E2.2; se varían el modelo y el horizonte |
| **Evaluación** | H1 con los criterios indicados. Si falla, se documenta y no se continúa con E2.3–E2.5 hasta corregirlo. H2: rango de SG a 5 años entre modelos plausibles (ΔAIC ≤ 4). H3: ranking de error de predicción de los meses 24–42 |
| **Validación** | Interna: E2.0 (algoritmo) y E2.5 (temporal). Externa: **solo si aparece un corte posterior de ADRIATIC**. En ese caso, comparar con él las predicciones fijadas de antemano (se recomienda registrarlas con fecha antes de conocer el corte) |
| **Gráficas** | (1) KM reconstruido superpuesto a las coordenadas originales, con números en riesgo debajo (meses desde la aleatorización; ITT; fuente: D04 Fig. 1A/2A). (2) Tabla gráfica de validación (publicado frente a reconstruido). (3) RMST(τ) con IC 95 % por bootstrap. (4) Abanico de extrapolaciones hasta 10 años por modelo, con KM superpuesto y las elecciones de Tsai y TLCR resaltadas. (5) Error de predicción de los meses 24–42 por modelo |
| **Incertidumbre** | IC 95 % por bootstrap (≥1000 réplicas sobre los datos reconstruidos, semillas registradas). Incertidumbre estructural como rango entre modelos. **Se declara que los IC no recogen el error de reconstrucción ni el carácter intermedio del análisis** |
| **Reproducibilidad** | `05_experimentos/E2/` con configuración YAML, extractor de coordenadas, implementación de Guyot con pruebas unitarias, `lifelines` con versión fijada y semillas |
| **Alcance** | Cuantifica qué es compatible con los datos publicados y cuánto depende la extrapolación del modelo. **No** establece la supervivencia real a largo plazo, ni curación, ni costo-efectividad. Solo aplica a CPCP limitado tras QRT concurrente, PS 0–1 |

### E3. Submodelo EGFR–ERK de Wang et al. 2007: auditoría de reproducibilidad (C3)

| Campo | Contenido |
|---|---|
| **Pregunta** | ¿Reproducen las ODE publicadas (Tablas 1–2) la magnitud y la forma de las tasas de cambio de PLCγ y ERK que el artículo usa como disparadores fenotípicos (Fig. 6)? |
| **Hipótesis** | **H1:** las tablas publicadas reproducen el orden de magnitud de d[ERK-PP]/dt y d[PLCγ]/dt de la Fig. 6 (dentro de un factor 2). Antecedente declarado: la comprobación exploratoria de un lector sugiere que no (ERK-PP ≈ 0), así que **H1 se contrastará con un protocolo fijado de antemano y no se presupone el resultado**. **H2 (si H1 falla):** la discrepancia se explica por errores de transcripción identificables al cotejar con las fuentes primarias (por ejemplo, K16 y K18 = 1,46×10⁵ nM) |
| **Fundamento** | D10 Tablas 1–2 (pp. 3–4), Fig. 6 (p. 10), texto pp. 5–7, 12; ficha D10 §4(a), §6.3, §10, §12 |
| **Modelo** | 20 ODE de acción de masas y Michaelis–Menten según las Tablas 1–2, integradas con `scipy.integrate.solve_ivp` (BDF o LSODA, tolerancias 10⁻⁸/10⁻¹⁰). Variante con leyes de conservación explícitas de las enzimas, señalada como **modificación** |
| **Datos** | Ninguno observado. Referencia: Fig. 6 digitalizada (vectorial si es posible) [D10 p. 10] |
| **Parámetros** | Constantes cinéticas y concentraciones iniciales de las Tablas 1–2, con su fuente primaria citada por D10 (refs. 11, 12, 14 y 39; **pendiente obtenerlas**) |
| **Comparador** | Fig. 6 publicada; variante con conservación; versión con parámetros de las fuentes primarias |
| **Experimento** | Barrido de EGF (2,65 × {1, 2, 5, 10, 20, 31, 32, 40} nM); EGFR 80 frente a 800 nM [D10 p. 11]. Se registran picos y trayectorias de las tasas de cambio. Comprobación de conservación de masa por especie total |
| **Evaluación** | H1: cociente entre tasa simulada y tasa publicada dentro de [0,5; 2]. Conservación: error relativo de la masa total <10⁻⁶ en la variante corregida |
| **Validación** | Solo verificación numérica (tolerancias y solucionadores alternativos). No hay validación biológica |
| **Gráficas** | Trayectorias de PLCγ y ERK-PP frente al tiempo; tasa de cambio frente a EGF, simulada frente a publicada; balance de masas |
| **Incertidumbre** | Determinista. Sensibilidad local (logarítmica) de las tasas de cambio a cada constante; Sobol solo si H1 se cumple |
| **Reproducibilidad** | `05_experimentos/E3/`, con parámetros en YAML que llevan columna de fuente y página |
| **Alcance** | Concluye sobre la reproducibilidad de lo publicado. **Punto de decisión:** si H1 y H2 fallan, se detiene la línea y se documenta. No se reconstruirá el ABM, porque faltan umbrales, paso de tiempo y semillas |

### E4. Historia natural y cribado (C4): **no se planifica su ejecución**

Solo se ejecutaría como ejercicio exploratorio si el equipo lo pide, con parámetros de historia natural tomados de fuentes primarias externas que habría que identificar primero (perfiles CISNET) y declarando que no aporta novedad frente a MISCAN-Lung (registro B06).

---

## D. Recomendación priorizada

### D.1 Contribución más defendible: **C1 / E1**

Por qué:
1. Es el **único insumo con datos de pacientes reales, código y resultados cuantitativos publicados** (MBE Tabla 2) contra los que medir la reproducción.
2. Los propios autores declaran el hueco: estimación de parámetros, identificabilidad y dependencia de parámetros inferidos con el desenlace [D02 p. 11–12].
3. La búsqueda no encontró reproducciones ni extensiones: 0 citas indexadas (registro B02).
4. Es computacionalmente viable en 1D con los recursos disponibles.
5. Si se confirma la no identificabilidad o la falta de ventaja predictiva frente a modelos simples, eso es en sí un resultado publicable y útil sobre los límites de los gemelos digitales con datos clínicos escasos. Si no se confirma, el resultado también es informativo.

**C2 / E2** se recomienda como **línea paralela de bajo coste**: alta viabilidad y novedad moderada, condicionada a revisar los otros 3 análisis económicos y a la ausencia de un corte posterior.

**C3 / E3** queda como línea secundaria, con punto de decisión temprano.

### D.2 Experimento mínimo reproducible (E1-mín)

1. **E1.0** Contenedor con FEniCS 2019.1.0 y el repositorio en un commit fijado; una corrida 1D de P1 con los parámetros de MBE; tiempo de cómputo medido.
2. **E1.1** Farmacocinética de P1 y P2: picos y valles periódicos frente a la fórmula analítica.
3. **E1.2** Reproducción de los índices g de MBE Tabla 2 para P1 y P2.
4. **E1.5 reducido** Perfil de verosimilitud de λ_τ^eff (con λ_P^pro reoptimizado) en P2, con λ = 1 fijo.

Entregables del mínimo: informe de reproducción, figuras 1, 2 y 4 de E1 y un registro completo de ejecución.

### D.3 Recursos necesarios

- Docker Desktop, en uso, con la imagen propia `papercancer/t01-fenics2019:1` (FEniCS 2019.1.0 de conda-forge). La imagen oficial no es compatible con Docker 29.
- Un entorno de Python aislado para nuestro código (numpy, scipy, matplotlib, pyyaml, pandas; scikit-fem opcional; lifelines para E2).
- CPU: 14 núcleos disponibles; cómputo por estimar en E1.0.
- Una persona revisora con conocimiento de elementos finitos y bioestadística para la verificación cruzada.
- Recomendado: **contacto con los autores** (Wagner, TUM), por tres motivos: (a) el repositorio no tiene licencia; (b) los datos son de pacientes, con aprobación ética BLAEK 19021 [D02 p. 6]: conviene confirmar los términos de uso para publicar un trabajo derivado; (c) evitar duplicar trabajo en curso.

### D.4 Fases y criterios para continuar o descartar

| Fase | Contenido | Continuar si | Descartar o reorientar si |
|---|---|---|---|
| F0 | Entorno, tiempo de cómputo, lectura del código (valores no reportados: φ_σ,v, condición inicial, desfase) | El código corre y una corrida 1D tarda ≤30 min | No corre tras un esfuerzo acotado (2 días) → solo reimplementación independiente y contacto con los autores |
| F1 | Reproducción (E1.1–E1.3) | H1 se cumple | H1 falla → documentar las discrepancias como resultado (informe de reproducibilidad) antes de seguir |
| F2 | Calibración y perfiles (E1.4–E1.5) | El presupuesto de corridas es viable (perfil ≤ ~500 corridas por parámetro) | No es viable → identificabilidad local (rango de la matriz de información de Fisher) y declararlo |
| F3 | Comparadores y predicción (E1.6–E1.7) | — | — |
| Verificación de novedad (antes de redactar) | Scibilia 2024 completo; citas de MBE 2023 | No hay solapamiento sustancial | Hay solapamiento → reorientar a lo no cubierto o a replicación explícita |

### D.5 Qué está listo y qué depende de información adicional

**Listo:**
- Datos de E1 (CSV) y parámetros con fuente (`tabla_parametros_E1_phasefield.csv`).
- Insumos de E2 (`tabla_insumos_E2_ADRIATIC.csv`) y PDF de D04.
- Ecuaciones de E3 (ficha D10).
- Métricas y criterios definidos de antemano.

**Depende de información adicional:**
- E1: valores no reportados que deben leerse en el código; texto completo de Scibilia 2024; respuesta de los autores sobre licencia y datos (recomendable, no bloqueante para la reproducción privada).
- E2: los otros 3 análisis económicos; confirmar que no hay un análisis final de SG.
- E3: fuentes primarias de los parámetros (refs. 11, 12, 14 y 39 de D10).

**Autorizado y ejecutado (10–12-oct-2026):** F0–F1 de E1 y E2.0–E2.2. Ver la sección E.

---

## E. Estado de ejecución y relación con el paper (13-oct-2026)

Las secciones A–D son el plan del 10-oct: sus hipótesis, tolerancias y criterios siguen vigentes. Esta sección registra el estado comprobado. Fuentes:
- `Resultados/Coordinacion/ESTADO_TAREAS.md`;
- `Resultados/Integrado/INFORME_INTEGRADO_F0_F1.md`;
- `Paper_final/METODOLOGIA_SIMULACIONES_Y_COLABORACION_IA.md`.

### E.1 Qué se ejecutó del plan

| Paso del plan | Estado | Tarea | Resultado frente al criterio del plan | Sección del paper |
|---|---|---|---|---|
| E1.0 Entorno y tiempos | **Ejecutado** | T01 | El código corre en Docker (imagen propia con conda-forge). La referencia 1D de P1 tardó ~21 min (≤ 30 min, criterio de F0) y la de P2 ~36 min con un proceso concurrente (leído en las marcas de tiempo de los logs) | §3.1 |
| E1.1 PK | **Ejecutado** | T01 | 3/6 extremos ≤ 0,1 %; dosis total exacta → parcialmente reproducido | §4.1 |
| E1.2 Tabla 2 | **Ejecutado** | T01 | 0/88 con la salida directa → **H1 no se cumple** (primera parte). Diagnóstico aparte: ×α/100, 88/88 | §4.2 |
| E1.2 Trayectorias 1D de P1 y P2 frente a los datos | **No ejecutado** | — | — | Pendiente (§5, etapa 0) |
| E1.3 Reimplementación y convergencia | **No ejecutado** | — | La segunda parte de H1 queda pendiente | §4.4, §5 |
| E1.4–E1.7 (F2–F3) | **No ejecutado** | — | H2–H4 sin evaluar | §5 (propuesta) |
| *Fuera del plan:* variante corregida de P2 (H01) | **Ejecutado** con autorización del 12-oct | T06 | Efecto relevante (preespecificado). **Sin revisión independiente** | §2.4, §4.3 |
| E2.0 Validación con verdad conocida | **Ejecutado** (E2.0a; E2.0b se añadió tras la auditoría T04, defecto D2) | T02, T04, T05 | 1800/1800 dentro de tolerancia; 1 prueba fallida declarada | Solo S2 |
| E2.1–E2.2 Extracción, reconstrucción y validación | **Ejecutado** | T02, T04, T05 | **H1 de E2: 18/18** | Solo §3.3 y S2 |
| E2.3–E2.5 | **No ejecutado** | — | — | No se usa |
| E3, E4 | **No ejecutado** | — | — | No se usa |
| D.2 E1-mín, punto 4 (E1.5 reducido) | **No ejecutado** | — | — | — |

**Decisiones según el §D.4.**
- **F0:** se cumple el criterio de continuar.
- **F1:** H1 falla, así que, según el plan, «documentar las discrepancias como resultado antes de seguir». Hecho en el informe integrado y en el paper.
- **F2:** no iniciada.
- **Verificación de novedad:** no hecha (falta Scibilia 2024).

### E.2 Desviaciones respecto al plan

| Plan | Lo realizado | Efecto |
|---|---|---|
| Salidas en `Resultados/05_experimentos/E*/` (§C) | `Resultados/Trabajo_Claude/` (T01, T04–T06) y `Resultados/Trabajo_Cline/` (T02, T03), con una carpeta exclusiva por tarea | Solo organizativo |
| Configuración en YAML (§C) | E2 sí (`T02_ADRIATIC/config/config.yaml`). En E1 no hay YAML: se ejecutó el código de los autores con sus parámetros por defecto, sin recalibrar | Ninguno sobre los resultados. Los parámetros están en el código (commit `fa8e6229`) |
| FEniCS en contenedor (§C, E1) | No sirvió la imagen oficial (manifiesto v1, incompatible con Docker 29). Se usó una imagen propia de conda-forge con bloqueo explícito | Versiones distintas de las de los autores (desconocidas); dentro de la tolerancia (§4.2 del paper) |
| Persona revisora con conocimiento de elementos finitos y bioestadística (§D.3) | La verificación cruzada la hicieron agentes de IA bajo supervisión: Cline revisó T01 (T03) y Claude Code auditó T02 (T04, T05) | **Sigue sin haber revisión humana experta.** Conviene antes del envío |
| Criterio de rango de T01 («parcial» si cumple la tolerancia pero difiere el rango) | El comparador propio no lo etiqueta (T03-H05) | Sin efecto en los resultados actuales |
| E2.0 solo sin digitalización | Se añadió E2.0b, que valida también la extracción (corrección D2) | Refuerza la validación |

Las hipótesis (H1–H4 de E1; H1–H3 de E2), las tolerancias y los criterios de las secciones C–D **no se han cambiado**.

### E.3 Qué partes de este plan respaldan el paper

| Parte del plan | Uso en el paper |
|---|---|
| A.1, punto 1 (NLST, NELSON) | §1.1 (contexto poblacional) |
| A.2–A.3 (modelos mecanicistas débiles; identificabilidad) y A.4 (preprint frente a versión publicada) | §1.3, §2–§3 |
| C1 / E1 (hipótesis, tolerancias, fases) | Núcleo del paper: §3.2 (criterios), §4, §5 (hoja de ruta con E1.3–E1.7) |
| C2 / E2 | **Solo** como contraste del protocolo (§3.3, S2). **No valida el modelo de E1** |
| C3 / E3 y C4 / E4 | No se usan |
| A.1, puntos 2–4 | No se usan |

**Título del paper.** El paper se titula como auditoría de reproducibilidad del modelo de Wagner et al. (2023). La calibración y la optimización (E1.4–E1.7; etapa 6 del §5 del paper) **no se han ejecutado** y figuran como trabajo futuro. Ver `Paper_final/Estado_Paper_Doctoral_brechas.md` §2.
