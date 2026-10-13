# Informe integrado F0–F1: reproducción del modelo de campo de fase (E1) y reconstrucción de ADRIATIC (E2)

| Campo | Valor |
|---|---|
| Proyecto | Paper_Cancer, cáncer de pulmón |
| Fecha | 12-oct-2026; actualizado el 13-oct-2026 (T06) |
| Coordinación e integración | Claude Code |
| Alcance | **E1, fases F0–F1** (T01): entorno, Tabla 2, farmacocinética y correspondencia artículo–código. **E2, pasos E2.0–E2.2** (T02): extracción, reconstrucción de Guyot y validación H1. **Variante corregida de E1** (T06): re-simulación de P2 con H01 corregido. Sin extensiones: ni calibración, perfiles, comparadores ODE, RMST ni extrapolación |
| Plan de referencia | `Paper_final/Primera_entrega_contribuciones_y_plan.md` (10-oct-2026) |
| Estado de las tareas | `Resultados/Coordinacion/ESTADO_TAREAS.md` |

**Regla de integración.** Solo se integran resultados respaldados por una ejecución registrada y por una verificación independiente (auditoría o revisión cruzada). La única excepción es T06, que se integra rotulado como pendiente de revisión independiente. Las clasificaciones son las preespecificadas en cada contrato y no se han cambiado. Los diagnósticos que explican una discrepancia se presentan aparte y se rotulan como tales.


## Resumen

| Bloque | Criterio preespecificado | Resultado | Clasificación | Verificación independiente |
|---|---|---|---|---|
| E1 · Tabla 2 (88 índices g) | ≤ 10 % y mismo signo; H1 si ≥ 80 % | Salida directa del script de los autores: **0/88** (signos 88/88; rangos 8/88) | **Discrepancia; H1 no se cumple** | T03 (Cline): clasificación confirmada; resúmenes de T01 coherentes con su recálculo |
| E1 · Tabla 2, diagnóstico (no criterio) | — | g_script·α/100 (definición verbal de la ec. 4.1): las 88 cifras coinciden al redondear a 3 cifras (error máx. 0,449 %); rangos 88/88 | Explicación numérica de la discrepancia de escala; **respalda, no demuestra**, el postprocesado de los autores | T03: concordancia **demostrada** con código propio y transcripción 88/88; de 7 transformaciones, solo ×α/100 recupera las 88 cifras; el postprocesado histórico es **plausible** |
| E1 · Defecto del script de sensibilidad en P2 (T03-H01) | — | En P2, las perturbaciones ± usan parámetros farmacocinéticos por defecto (146000; 0,24 g; 26,7 d) en vez de los de la referencia (143600; 0,20 g; 22 d) | Discrepancia de método del código de los autores. **Efecto cuantificado en T06: relevante** (mediana \|Δ\| 12,6 %, máx. 45,2 %; 7 cambios de rango en V_vis; sin cambios de signo) | T03 (análisis estático) + coordinador (lectura del código). T06: control de determinismo exacto; **sin revisión independiente** |
| E1 · Farmacocinética (ec. 6 del preprint; ec. 4 del paper) | Pico y valle ≤ 0,1 % | **3 de 6** extremos ≤ 0,1 %; los otros tres, 0,107–0,129 % (desfase de medio subpaso). Dosis total exacta | **Parcialmente reproducido** | T03 (detectó la errata «4 de 6» en el resumen de T01) |
| E1 · Correspondencia artículo–código | Lista clasificada | 35 elementos: 21 coinciden, 5 los resuelve el código, **9 discrepancias** (incluida la definición de g), más el defecto H01 | Completado | T03 (corrigió la magnitud de los desfases de calendario) |
| E2 · H1 (18 cantidades) | Eventos ±3 %, hitos ±2 pp, HR ±0,03, medianas ±1 mes (±3 en SG-D) | **18/18** en la versión original y en la corregida | **Reproducido** | T04 y T05: KM y Cox propios, re-ejecución byte a byte |
| E2 · Corrección D1 (escalones fusionados) | Mesetas = niveles del polígono | Empate máximo en SLP: 31/34 → 6/9; 0 saltos con niveles intermedios | Corregido | T05 (V5) |
| E2 · E2.0b (simulación con PDF y extracción) | Mismas tolerancias que H1 | 1800/1800 dentro de tolerancia; error de riesgo 0 | Superado | T05 (V7) |
| E2 · Pruebas de la entrega | Todas pasan | **22/23**. Falla `test_e20b_all_replicates_same_truth_and_diagnostics` (límite de resolución; §5.2) | Fallo declarado como limitación | T05 (O-T05-1) |

**Lectura conjunta.**
- **E1:** el script publicado no reproduce la Tabla 2 tal cual.
  - La discrepancia de escala desaparece, a la precisión publicada, aplicando α/100. Ese factor es coherente con la definición verbal de la ec. 4.1 y el script no lo aplica.
  - La coincidencia respalda, pero no demuestra, cómo generaron los autores la tabla.
  - La revisión T03 encontró además que, en P2, el script de sensibilidad perturba en torno a otra configuración farmacocinética (H01). T06 cuantificó su efecto: relevante (mediana 12,6 %, máx. 45,2 %), concentrado en V_vis y sin cambios de signo. La tabla publicada coincide con la configuración defectuosa (44/44) y no con la corregida (1/44).
  - Según el plan (§D.4, F1: «H1 falla → documentar las discrepancias como resultado antes de seguir»), todo esto se documenta como hallazgo de reproducibilidad.
- **E2:** la reconstrucción cumple H1. Los pseudo-IPD corregidos son aptos como insumo para E2.3–E2.5, con las limitaciones del §6.

---

## 1. Reparto real del trabajo

| Tarea | Contenido | Ejecutó | Verificó | Estado | Coste de Cline (USD) |
|---|---|---|---|---|---|
| T00 | Prueba de delegación a Cline CLI | Claude Code | — | aceptada | — |
| T01 | E1 F0–F1: entorno, Tabla 2, PK y correspondencia | **Claude Code** | **Cline (T03)** | revisada y corregida. Dictamen de T03: **objeciones mayores** (H01 y H02, sobre la interpretación), aceptadas y aplicadas; clasificaciones sin cambios | — |
| T02 | E2.0–E2.2: extracción, Guyot y validación | **Cline** | **Claude Code (T04, T05)** | aceptada (ronda 1, con observaciones) | 9,07 (ronda 0, cortada por límite de uso) + 9,11 (ronda 1, sesión interrumpida) + 1,66 (cierre) = **19,84** |
| T03 | Revisión crítica acotada de T01 | **Cline** | Claude Code (verificó H01 en el código y aplicó H01–H07) | aceptada | 0,57 (sesión cortada por un error de fuente del coordinador) + 2,73 (revisión) = **3,31**; con la prueba de créditos, **3,36** (límite autorizado: 10) |
| T04 | Auditoría de T02 (ronda 0) | Claude Code | — | aceptada (dictamen: requiere corrección D1 y D2) | — |
| T05 | Auditoría de la ronda 1 de T02 | Claude Code | — | aceptada (dictamen: T02 aceptada) | — |
| T06 | E1: re-simulación de P2 con H01 corregido (variante declarada) | **Claude Code** | **pendiente** (no encargada) | entregada | — |
| Pruebas de créditos | `PRUEBA_OK` antes de cada encargo | Cline | Claude Code | completadas | 0,046 + 0,048 + 0,046 |

- Modelo de Cline: `openai-codex` / `gpt-6-astra`, con `--thinking high`.
- Los costes salen del campo `totalCost` de los registros `<PAPERCANCER_ENV>\logs_cline\*.jsonl`. No se registra el coste de Claude Code.
- **Incidencia del coordinador:** el primer envío de T03 indicaba como fuente de la ec. 4.1 y la Tabla 2 el PDF de `Data_insumo`, que es el **preprint** y no contiene esas partes. Se cortó la sesión (0,57 USD), se corrigió el encargo (v2) y se reenvió.
- **Corrección del coordinador antes de T03:** en `INFORME_T01.md` §4.5 se corrigió una frase incorrecta sobre la definición de g en el código. Decía «(ΔQ/Q)/(Δα/α)»; el código calcula ∂_α Q̄ / Q̄. T03 confirmó que la redacción corregida es exacta.
- **Correcciones tras T03:** aplicadas en `INFORME_T01.md` (§8, con una tabla de decisiones por hallazgo), en `REPRODUCIR.md` y en la fila «definición de g» de `correspondencia_articulo_codigo.csv`. Ningún cálculo cambia.

## 2. Métodos

### 2.1 E1 / T01: campo de fase (Wagner et al., *Math Biosci Eng* 2023;20:18670–94)

- **Fuentes:**
  - artículo publicado (texto extraído, `Resultados/03_registro_busquedas/MBE_2023_Wagner_texto_extraido.txt`; CC BY 4.0);
  - repositorio `wagnandr/immunotherapy-lung-cancer`, commit `fa8e6229`, sin licencia (ejecución privada fuera de OneDrive).
- **Entorno:** imagen Docker propia `papercancer/t01-fenics2019:1` (miniforge, conda-forge; python 3.10, fenics-dolfin 2019.1.0, petsc 3.25.6), con el bloqueo exacto en `env/conda_explicit_lock.txt`. Prueba de humo con P1 y P2.
- **Tabla 2:** script original `reduced_models/local_sensitivity_analysis.py` **sin modificar**: h = 10⁻³, diferencias centrales, dt = 1/24 d, T = 1470 d (P1) y 1102 d (P2). Docker con `--cpus 8`; 309 min. Comparación con `src/compare_tabla2.py` usando el criterio del contrato §4.1, fijado antes de ejecutar. Diagnóstico de escala aparte (`src/diag_escala_tabla2.py`).
- **PK:** `MedicineSolver` original frente a la solución exacta de la ec. 6 (superposición de infusiones).
- **Correspondencia:** 35 elementos de la Tabla 1 y del texto frente al código.

### 2.2 E2 / T02: ADRIATIC (Cheng et al., *NEJM* 2024;391:1313–27)

- **Extracción vectorial** de la Fig. 1A (SG, p. 6) y la Fig. 2A (SLP, p. 8): colores por brazo, ejes calibrados con 22 + 11 ticks y marcas de censura separadas.
  - **Corrección D1:** mesetas derivadas de **pares de bordes horizontales** del polígono del trazo (≈ 0,502 pt), sin depender del grosor vertical.
- **Reconstrucción:** algoritmo de Guyot et al. (2012), implementación propia en Python. Entradas: curva extraída, números en riesgo (22 tiempos) y total de eventos.
- **Validación:** KM y Cox no estratificado (Efron; Breslow como sensibilidad) frente a las 18 cantidades H1 del contrato §5.2.
- **E2.0a:** 100 réplicas simuladas de verdad conocida, sin digitalización.
- **E2.0b:** mismas semillas, cada KM dibujado en un PDF vectorial con la geometría de la Fig. 1A y extraído con el mismo `extract.py`.
- **Entorno:** `venv_cline_T02` (python 3.10.0, lifelines, pymupdf); hilos = 1.

### 2.3 Verificación independiente

- **T04 y T05 (Claude sobre T02):**
  - re-ejecución completa en una copia aislada, con comparación SHA-256;
  - extracción ráster independiente calibrada con ticks vectoriales (T04);
  - KM y Cox propios sin lifelines;
  - detector propio de escalones fusionados;
  - comprobación de tolerancias y de ausencia de ajuste a posteriori (instantáneas de `extract.py` frente a los resultados clínicos).
- **T03 (Cline sobre T01):** revisión acotada con código propio. Prioridades: R1, justificación del reescalado α/100 (ec. 4.1, código, valores α, alternativas de escala y transcripción de la Tabla 2); R2, alcance de la interpretación. Cline usó su propio código, sin importar el de los autores ni los comparadores de T01, y un análisis estático del árbol sintáctico del script. No ejecutó simulaciones. El coordinador verificó H01 leyendo el código antes de aceptarlo.

## 3. Resultados verificados

### 3.1 E1: Tabla 2

| Métrica | Salida directa del script (criterio) | g_script·α/100 (diagnóstico) |
|---|---|---|
| Reproducido (≤ 10 %, mismo signo) | **0 / 88** | 88 / 88 |
| Error relativo: mediana / p90 / máx. | 228 / 2,0·10⁵ / 1,0·10⁷ (en tanto por uno) | 0,068 % / 0,22 % / 0,45 % |
| Signo coincidente | 88 / 88 | 88 / 88 |
| Orden de rangos coincidente | 8 / 88 | 88 / 88 |
| Igualdad al redondear a 3 cifras (T03) | 0 / 88 | **88 / 88** |

- Ejecución: exit 0, del 12-oct a las 03:53 UTC al 12-oct a las 09:02 UTC (`T01_phasefield/logs/tabla2_original_20261012T035307Z.log`). Figura: `figuras/fig_tabla2.png`.
- **Definición de g.** El código calcula g = (Q̄⁺ − Q̄⁻)/(2·h·α·Q̄), es decir ∂_α Q̄/Q̄ (`local_sensitivity_analysis.py`, l. 101–104). La ec. 4.1 define g := (∂_α Q̄/Q̄)·α/100 %, el cambio relativo al variar α un 1 % (MBE p. 16).
  - La notación «100 %» leída literalmente como 1 daría la elasticidad (×α).
  - El factor α/100 se apoya en la descripción verbal (Taylor con Δα = 0,01·α) y en la Tabla 2 (T03-H03).
- **Verificación T03** (`T03_revision_T01/data_derived/alternativas_616.csv`):

| Transformación de g_script | Error relativo máx. | ≤ 10 % y signo | Rangos | Igualdad a 3 cifras |
|---|---|---|---|---|
| Directa | 1,0·10⁹ % | 0 | 8 | 0 |
| **×α/100** | **0,449 %** | **88** | **88** | **88** |
| ×α | 9 931 % | 0 | 88 | 0 |
| /100 | 1,0·10⁷ % | 12 | 8 | 12 |
| ×α del otro paciente/100 | 19 939 % | 56 | 25 | 56 |
| ×α redondeados (Tabla 1)/100 | 1,81 % | 88 | 88 | 74 |
| ×α/101 (control sin base teórica) | 1,44 % | 88 | 88 | 0 |

  - Por sí solo, el umbral del 10 % no identifica una explicación única: ×α con los valores redondeados de la Tabla 1 y el control /101 también lo cumplen.
  - Solo ×α/100 recupera las 88 cifras impresas. No se ha probado que sea la única transformación posible.
  - T03 verificó además la transcripción completa de la Tabla 2 (88 cifras y 88 rangos, sin discrepancias) frente al texto publicado extraído, y los 22 vectores de α frente al código y al log.

### 3.2 E1: farmacocinética

| Caso | Error del pico | Error del valle |
|---|---|---|
| P1 Q2W | 0,0017 % | 0,107 % |
| P2 Q3W | 0,0020 % | 0,129 % |
| P2 Q6W | 0,129 % | 0,0021 % |

Cumplen 3 de 6 extremos. El resumen de T01 decía «4 de 6»; la errata la detectó T03-H04 y está corregida. Las 136 administraciones entregan exactamente la dosis nominal. Los excesos sobre el 0,1 % aparecen en una sola muestra por dosis, en el borde de la infusión: la ventana efectiva está desplazada ±0,5 subpasos (≈ 56 s). Figura: `figuras/fig_pk.png`.

### 3.3 E2: validación H1 (pseudo-IPD corregidos, ronda 1)

| Cantidad | SG durvalumab | SG placebo | SLP durvalumab | SLP placebo | Tolerancia |
|---|---|---|---|---|---|
| Eventos (publicado → reconstruido) | 115 → 115 | 146 → 146 | 139 → **140** | 169 → **170** | ±3 % |
| Mediana, meses | 55,9 → 55,94 | 33,4 → 33,39 | 16,6 → 16,54 | 9,2 → 9,18 | ±1 (±3 en SG-D) |
| Hito 1 (SG 24 m; SLP 18 m) | 0,680 → 0,680 | 0,585 → 0,585 | 0,488 → 0,490 | 0,361 → 0,361 | ±2 pp |
| Hito 2 (SG 36 m; SLP 24 m) | 0,565 → 0,565 | 0,476 → 0,477 | 0,462 → 0,464 | 0,342 → 0,343 | ±2 pp |

| HR no estratificado | Publicado | Efron | Breslow | Tolerancia |
|---|---|---|---|---|
| SG | 0,73 | 0,7303 | 0,7304 | ±0,03 |
| SLP | 0,76 | 0,7715 | 0,7723 | ±0,03 |

- Clasificación: **18/18 reproducidas**, también en la versión original (ronda 0).
- Valores confirmados por un KM y un Cox independientes (`T05_auditoria_T02_ronda1/data_derived/km_cox_indep.json`).
- Números en riesgo: 88/88 coinciden en la versión corregida; en la original, 85 coincidían y 3 diferían en un sujeto. Figuras: `figuras/overlay_SG.png` y `figuras/overlay_SLP.png`.

### 3.4 E2: efecto de la corrección D1 (original → corregido)

| Curva | Mesetas | Empate máximo | Tiempos de evento distintos |
|---|---|---|---|
| SG durvalumab | 73 → 109 | 5 → 3 | 72 → 108 |
| SG placebo | 81 → 133 | 6 → 2 | 80 → 132 |
| SLP durvalumab | 45 → 90 | 31 → 6 | 40 → 88 |
| SLP placebo | 50 → 101 | 34 → 9 | 49 → 100 |

La diferencia Efron–Breslow en la HR de SLP baja de 0,0049 a 0,0008. La mediana de SLP placebo pasa de 9,09 a 9,18 meses (publicada: 9,2).

### 3.5 E2: validación con verdad conocida

| Cantidad (100 réplicas × 2 brazos) | E2.0a (sin digitalización): máx. \|error\| | E2.0b (PDF + extracción): máx. \|error\| |
|---|---|---|
| HR SG / SLP | 0,0061 / 0,0044 | 0,0089 / 0,0044 |
| Hitos | ≤ 0,0020 | ≤ 0,0020 |
| Medianas | ≤ 2,10 meses (todas dentro de su tolerancia) | ≤ 2,10 meses (ídem) |
| Eventos | ≤ 2 | ≤ 2 |
| Dentro de tolerancia | 1800/1800 | 1800/1800 |

## 4. Comparaciones con lo publicado

- **E1, Tabla 2.**
  - El script publicado, ejecutado sin cambios, devuelve índices entre 10 y 10⁷ veces mayores que los de la tabla, con el mismo signo.
  - Aplicando ×α/100, los 88 valores coinciden al redondear a 3 cifras significativas (la precisión publicada) y también los 88 rangos.
  - **Formulación adoptada** (propuesta de T03, actualizada con T06): «Con la salida directa del script, la Tabla 2 mantiene la clasificación preespecificada de discrepancia (0/88; H1 no se cumple). Como diagnóstico, multiplicar por α/100 (coherente con interpretar g como el cambio relativo ante una variación del parámetro del 1 %) recupera las 88 cifras al redondear a tres cifras significativas y los 88 rangos (error máximo 0,449 %). La coincidencia respalda, pero no demuestra, ese postprocesado. Además, en P2 las perturbaciones no conservan tres parámetros farmacocinéticos de la referencia; corregirlo (T06) cambia los índices de P2 una mediana del 12,6 % y hasta un 45,2 %. No se infiere validación predictiva ni clínica.»
- **E1, PK:** la ODE de la ec. 6 y la dosis total se reproducen. El criterio de pico y valle ≤ 0,1 % no se cumple con la definición preespecificada, por un desfase de discretización interno del código.
- **E2:**
  - Las 18 cantidades H1 caen dentro de tolerancia.
  - Como información, sin tolerancia: los extremos de los IC 95 % de hitos y HR difieren ≤ 0,014 del publicado. Los de las medianas difieren ≤ 0,15 meses, salvo el límite inferior del IC de la mediana de SG-D (35,6 frente a 37,3). La prueba de PH da p = 0,94/0,85 frente a 0,91/0,79 publicados, con métodos no idénticos. Estas cifras proceden de la ronda 0 (`INFORME_T02.md`, «Validación informativa»).
  - El total de eventos y los números en riesgo son **entradas** de Guyot, de modo que su coincidencia no es una validación independiente. Medianas, hitos y HR se heredan de la curva extraída.

## 5. Discrepancias

### 5.1 E1 (se conservan como incertidumbre; no se han corregido)

| # | Discrepancia | Efecto |
|---|---|---|
| 1 | **Definición de g:** el script calcula ∂_α Q̄/Q̄; la ec. 4.1 (definición verbal) y la Tabla 2 corresponden a ×α/100 | Elimina la discrepancia de escala a la precisión publicada (diagnóstico). No valida por sí sola el método |
| 2 | **Parámetros farmacocinéticos de P2 en el análisis de sensibilidad (T03-H01):** la referencia usa MED_mas = 143600, MED_dos = 0,20 g y MED_tim = 22 d (`default_parameters_patient2`, l. 23–32); las perturbaciones ± se reconstruyen con `vector_to_parameters` (l. 35–48), que vuelve a los valores por defecto 146000; 0,24 g; 26,7 d (`parameters.py`, l. 34–37) | Defecto del script de los autores. En P2, el numerador diferencia en torno a una configuración y el denominador normaliza con otra. **Efecto cuantificado en T06: relevante** (mediana \|Δ\| 12,6 %, máx. 45,2 %). La Tabla 2 publicada coincide con la configuración defectuosa (44/44) y no con la corregida (1/44) |
| 3 | Término del fármaco con un factor 0,7 no declarado (`MED_eff·0,7/80`; ω efectivo de 114,3) | No cuantificado por separado: la Tabla 2 coincide con el código tal cual |
| 4 | Calendario de terapia: inicio de P1, día 322 de los datos en el código frente al 296 del texto (**26 d**); Q6W de P2, 671 frente a 514 (**157 d**); fin de P2, 1218 frente a 1063 (**155 d**). El código coincide con las figuras del preprint | Ídem. (El borrador de T01 daba 176 y 114 d, que son el cambio de origen; corregido tras T03-H06) |
| 5 | Malla de P2: 1000 elementos en el código frente a 500 en el artículo | Ídem |
| 6 | Función H: sigmoide suave (pendiente 30) frente a un escalón de Heaviside | Ídem |
| 7 | Las células necróticas no consumen nutriente en el código | Ídem |
| 8 | λ_τ,eff de P2: 0,5489 en el código frente a 0,54 en el artículo | Ídem |
| 9 | T de la Tabla 2: 9 y 2 días antes del fin de la terapia | Ídem |
| 10 | PK: ventana de infusión desplazada medio subpaso (≈ 56 s) | Pico o valle hasta 0,129 % frente al 0,1 % preespecificado. Efecto sobre el tumor no cuantificado (despreciable según la interpretación de T01, sin verificar) |
| 11 | Comparador de T01: no etiqueta «parcialmente reproducido» por diferencia de rango, como pide el contrato §4.1 (T03-H05) | Sin efecto en los resultados actuales. Corregir si se reutiliza |

### 5.2 E2

| # | Discrepancia | Valoración |
|---|---|---|
| 1 | Eventos SLP-D 140 frente a 139 y SLP-P 170 frente a 169 | Dentro del ±3 %. Guyot no fuerza la coincidencia retroactiva. Visible como desviación de la cola de SLP-D tras el mes 44 (error de curva máximo de 0,9 pp) |
| 2 | HR de SLP: 0,7715 frente a 0,76 | Dentro de ±0,03. Cox no estratificado frente a estratificado publicado |
| 3 | Mínimo del seguimiento de los censurados en SG-D: 1,0 frente a 0,1 meses (informativo) | Esperable por la censura uniforme intraintervalo |
| 4 | **Prueba fallida** `test_e20b_all_replicates_same_truth_and_diagnostics` (`tests/test_round1.py`, l. 185) | Ver más abajo |

**Prueba fallida de T02 y su limitación.**
- **Qué falla.** La batería de 23 pruebas de la entrega tiene 22 correctas y 1 fallo, tanto en la ejecución de Cline del 12-oct como en la re-ejecución aislada de T05. La prueba exige que, en cada una de las 400 curvas de E2.0b, el número de mesetas extraídas sea igual al del KM verdadero. En **7 de 400 curvas** se extrae **una meseta menos**: réplicas 13/SG-P, 28/SG-D, 42/SG-P, 42/SLP-P, 82/SLP-D, 93/SLP-D y 95/SG-P.
- **Causa verificada** (T05, `meseta_perdida_cual.py`):
  - en 5 casos, la meseta ausente mide entre 2·10⁻⁶ y 1,3·10⁻⁵ pt: dos eventos separados por menos de 3·10⁻⁶ meses, por debajo de la precisión de coordenadas del PDF;
  - en los 2 restantes, la meseta ausente es el nivel terminal S = 0, de ancho nulo.

  Ninguna se puede representar gráficamente.
- **Efecto:** ninguno medible. Error de riesgo 0, error de extracción ≈ 3·10⁻⁷ y las 1800 comparaciones dentro de tolerancia. Las 4 curvas clínicas de ADRIATIC no pierden ningún nivel (su prueba de mesetas frente a niveles del polígono pasa).
- **Limitación:**
  - la extracción no puede separar eventos que el PDF no separa, y la frase de `DECISIONES_METODO.md` «sin eliminar el nivel» no se cumple para mesetas de ancho inferior a la precisión del PDF o nulo;
  - **la prueba no se ha modificado:** cambiarla después de ver el fallo sería ajustar el criterio a posteriori;
  - la entrega de T02 se acepta con esta prueba fallida declarada.

## 6. Limitaciones

**E1:**
1. **n = 2 pacientes**, ambos calibrados a mano por los autores. Nada de esta fase informa sobre la capacidad predictiva, la eficacia de la inmunoterapia ni la generalización a otros pacientes.
2. **Inferencia sobre la Tabla 2.** La relación entre la tabla y α/100 es una **compatibilidad numérica** (88/88 a 3 cifras), no un procedimiento documentado. T03 la califica de «plausible». El reescalado explica la escala, pero **no valida el método** de sensibilidad.
3. **Defecto H01:** los índices de P2 publicados (y los de T01) contienen la inconsistencia farmacocinética del §5.1, n.º 2. La variante corregida (T06) muestra un efecto relevante, concentrado en V_vis. **T06 no tiene revisión independiente.**
4. No se conocen las versiones de bibliotecas de los autores. Las diferencias residuales son compatibles con el redondeo; no es necesario ni está demostrado atribuirlas a versiones.
5. **H1 de E1 está incompleta en su segunda parte:** la verificación entre códigos (reimplementación propia ≤ 5 % L2, E1.3) no formaba parte de T01 y no se ha hecho.
6. Las discrepancias artículo–código no se cuantificaron por separado.
7. La transcripción de la Tabla 2 se verificó frente al texto extraído de la versión publicada, no frente a una imagen de la página.
8. La novedad no se ha verificado: falta leer completo Scibilia et al., *Math Biosci* 2024 (plan §B, C1).

**E2:**
1. Los pseudo-IPD son una **aproximación**: los tiempos individuales no son identificables, la censura intraintervalo se supone uniforme y SG y SLP son reconstrucciones marginales sin enlace entre sujetos.
2. Es un análisis **intermedio** (madurez de SG ≈ 49 %); la cola de SG-D tiene entre 5 y 11 pacientes en riesgo. Los IC calculados con pseudo-IPD no incluyen el error de reconstrucción.
3. HR y PH no estratificados: aproximan el análisis publicado (estratificado), no lo replican.
4. E2.0b usa PDF sintéticos **ideales**, sin ruido ráster ni todos los salientes de unión del editor. Valida la cadena extracción–reconstrucción con la geometría de la figura, no su robustez frente a figuras ráster.
5. **Prueba fallida declarada** (§5.2): límite de resolución en mesetas de ancho inferior a la precisión del PDF.
6. Quedan empates de 5–9 eventos en la SLP (t ≈ 1,6–1,9 y 3,67 meses). Corresponden a escalones verticales únicos de la figura publicada y no se pueden resolver a partir del PDF.
7. E2.0 se ejecutó después de la primera validación clínica: no es una validación cegada.

## 7. Licencias y términos de uso

Detalle en `Resultados/Coordinacion/licencias_y_terminos_de_uso.md`.

| Elemento | Términos | Medida aplicada |
|---|---|---|
| Wagner et al., MBE 2023 | CC BY 4.0 | Citar con atribución. La Tabla 2 se puede reutilizar |
| Repositorio `wagnandr/immunotherapy-lung-cancer` | **Sin licencia** (copyright por defecto) | Solo ejecución privada, fuera de OneDrive. **No se redistribuye.** Las citas se limitan a archivo y línea. No se publican versiones modificadas |
| Datos de pacientes (CSV del repositorio) | Anonimizados, aprobación BLAEK 19021, sin licencia de datos | Solo se usan para reproducir lo publicado. **Publicar análisis nuevos derivados requiere confirmarlo con los autores** |
| Cheng et al., NEJM 2024 | Copyright de la MMS | Extracción de datos numéricos para un análisis secundario. Las figuras de este informe muestran curvas reconstruidas, no el original. Para reproducir las figuras originales haría falta permiso |
| Pseudo-IPD de ADRIATIC | Derivados aproximados | Uso interno. Si se publican, se etiquetan como reconstrucción (Guyot 2012) |

El borrador de consulta a los autores de MBE **no se ha enviado**; requiere tu decisión.

## 8. Reproducción

| Bloque | Instrucciones | Entorno | Duración de referencia |
|---|---|---|---|
| E1 (T01) | `Resultados/Trabajo_Claude/T01_phasefield/REPRODUCIR.md` | Docker `papercancer/t01-fenics2019:1` (`env/Dockerfile`, `env/conda_explicit_lock.txt`) + `venv_claude_T01` para el análisis | Tabla 2: 309 min con 8 CPU |
| E2 (T02) | `Resultados/Trabajo_Cline/T02_ADRIATIC/REPRODUCIR.md` (`run_logged.py pipeline.py --stage all`) | `venv_cline_T02` (`requirements_T02.txt`); hilos = 1 | 225 s (re-ejecución T05) |
| Auditorías | `T04_auditoria_T02/AUDITORIA_T04.md` §4 y `T05_auditoria_T02_ronda1/AUDITORIA_T05.md` §5 | `venv_claude_T01`, `python -I` | Minutos |
| Revisión T03 | `Trabajo_Cline/T03_revision_T01/REVISION_T03.md` («Entregables y validación»): `src/revisar_t03.py` y `src/validar_entrega.py` | `venv_cline_T02` | Segundos |

- El código de los autores debe obtenerse de GitHub (commit `fa8e6229`; SHA-256 del zip `e45a8cd3…1acce`), porque no se incluye.
- La re-ejecución aislada de T02 reproduce **4660 de 4661** archivos byte a byte; solo difiere `PROCEDENCIA.md`, por las rutas absolutas.

## 9. Recomendación

1. **E1: documentar el resultado de F1 como hallazgo de reproducibilidad**, como prevé el plan (§D.4), con la formulación adoptada en el §4:
   - H1 no se cumple con el script publicado;
   - la discrepancia de escala es compatible con α/100;
   - en P2, el script de sensibilidad tiene un defecto de configuración (H01), cuantificado en T06 (efecto relevante).
2. **Cuantificar H01: hecho** (T06, 13-oct-2026; ver la sección «T06» tras el §10). Pendiente: su revisión independiente (unos 3 USD de Cline), que requiere autorización.
3. **Antes de pasar a F2 (calibración e identificabilidad de E1)**, conviene:
   - (a) completar la segunda parte de H1, la reimplementación propia y la verificación entre códigos (E1.3);
   - (b) decidir si se consulta a los autores, porque el uso de los datos para análisis nuevos publicables lo exige y además permitiría confirmar α/100, el factor 0,7 y H01; el borrador de consulta habría que ampliarlo con H01;
   - (c) leer Scibilia et al. 2024 para verificar la novedad.
4. **E2:** H1 se cumple, así que según el plan se puede avanzar a **E2.3–E2.5** (RMST, conjunto de modelos de extrapolación y validación temporal) con los pseudo-IPD corregidos, manteniendo las limitaciones del §6. Antes: revisar los 3 análisis económicos restantes y confirmar que no hay un análisis final de SG publicado (plan §B, C2).
5. Ningún paso anterior se inicia sin tu autorización.

## 10. Tabla de trazabilidad

| Afirmación | Fuente (archivo) | Ejecución o registro | Verificación | Estado |
|---|---|---|---|---|
| Tabla 2: 0/88 con la salida directa | `T01_phasefield/data_derived/tabla2_resumen.json`, `tabla2_comparacion.csv` | `logs/tabla2_original_20261012T035307Z.log` (exit 0) | T03 R1/R3 (`T03_revision_T01/data_derived/alternativas_616.csv`, `revision_resumen.json`) | Discrepancia (criterio) |
| Tabla 2: 88/88 con ×α/100 (a 3 cifras) | `T01_phasefield/data_derived/tabla2_diag_escala_resumen.json` | `src/diag_escala_tabla2.py` | T03 R1.4 (recálculo propio; 7 transformaciones) | Diagnóstico: concordancia demostrada; postprocesado plausible |
| Definición de g en el código y en la ec. 4.1 | `local_sensitivity_analysis.py`, l. 101–104 y 137 (repositorio, no redistribuido); `MBE_2023_Wagner_texto_extraido.txt`, l. 1056–1076 | — | Coordinador (corrección del 12-oct) + T03 R1.1–R1.2 | Verificado; salvedad de la notación «100 %» (H03) |
| Defecto farmacocinético de P2 (H01) | `local_sensitivity_analysis.py`, l. 23–48, 87 y 94; `parameters.py`, l. 34–37 | Análisis estático | T03 R1.2 + coordinador (lectura) | Confirmado; efecto cuantificado en T06 (relevante) |
| Transcripción de la Tabla 2 publicada | `T01_phasefield/data_derived/tabla2_publicada.csv` | Verificación visual de T01 | T03 R1.5 (`T03_revision_T01/data_derived/transcripcion_88.csv`: 88 cifras y 88 rangos) | Verificada sin discrepancias |
| PK parcialmente reproducida | `T01_phasefield/data_derived/pk_check.json`, `pk_localizacion_error.json` | `src/pk_check.py`, `pk_localiza_error.py` | T03 R3 | Parcialmente reproducido |
| 9 discrepancias artículo–código (más H01) | `T01_phasefield/data_derived/correspondencia_articulo_codigo.csv` | — | T03 R3 | Completado |
| H1 de E2: 18/18 | `T02_ADRIATIC/data_derived/round1_h1.csv` | `logs/20261011_230459_401462.json` (exit 0) | T05 V6 (`km_cox_indep.json`), V1 (byte a byte) | Reproducido |
| D1 corregido | `T02_ADRIATIC/data_derived/round1_ties.csv` | ídem | T05 V5 (`saltos_fusionados.csv` vacío) | Corregido |
| E2.0b 1800/1800 | `T02_ADRIATIC/data_derived/simulation_b_summary.csv` | ídem | T05 V7 | Superado |
| Prueba fallida de E2.0b (7/400 curvas) | `T02_ADRIATIC/logs/20261012_111552_310913.json` (exit 1) | `tests/test_round1.py` l. 185 | T05 O-T05-1 (`e20b_meseta_perdida_cual.csv`), re-ejecución (`logs/rerun_unittest.txt`) | Limitación declarada |
| Tolerancias sin cambios | `T02_ADRIATIC/config/config.yaml`, `CRITERIOS_PREESPECIFICADOS.md` | — | T05 V3 (SHA-256 idéntico a la ronda 0) | Verificado |
| Sin ajuste a posteriori de `extract.py` | `T02_ADRIATIC/logs/*_source/` | 20 instantáneas | T05 V4 (39 derivados clínicos idénticos) | Verificado |
| Re-ejecución byte a byte | `T05_auditoria_T02_ronda1/data_derived/rerun_vs_entrega.json` | `logs/rerun_pipeline_all.json` (exit 0) | — | 4660/4661 |
| Costes de Cline | `PaperCancer_env/logs_cline/*.jsonl` | campo `totalCost` | Coordinador | Registrado |

### T06: efecto cuantitativo de H01 (13-oct-2026)

Ejecutado con autorización del usuario (recomendación n.º 2 del §9). Detalle en `Resultados/Trabajo_Claude/T06_P2_H01/INFORME_T06.md`.

- **Diseño:** P2 se re-simuló llamando a la rutina original sin modificarla. Solo cambia la función de simulación, que restaura en cada simulación los parámetros farmacocinéticos de P2. El análisis y las clases de efecto se fijaron antes de lanzar.
- **Determinismo:** el control con el fallo original es idéntico al log de T01 (diferencia 0,0).
- **Efecto:** **relevante.** Mediana \|Δ\| 12,6 %, máximo 45,2 %, sin cambios de signo y 7 de 11 rangos de V_vis reordenados.
- **Comparación con la Tabla 2:** el P2 corregido coincide con la publicada en 1/44 valores a 3 cifras, frente a 44/44 con la configuración defectuosa. Esto indica que la tabla publicada contiene H01.
- **Ejecución:** el intento 1 falló al arrancar los workers (MPI.init, sin OOM) y está archivado. El intento 2 terminó con exit 0 en 183,6 min y un pico de 1,36 GiB.
- **Revisión independiente de T06:** pendiente, no encargada.

### Figuras incluidas (`Resultados/Integrado/figuras/`)

| Archivo | Origen | Contenido |
|---|---|---|
| `fig_tabla2.png` / `.svg` | T01 (Claude) | A: salida directa frente a la Tabla 2 (criterio). B: ×α/100 (diagnóstico) |
| `fig_pk.png` / `.svg` | T01 (Claude) | φ_τ del código frente a la solución exacta; error puntual |
| `overlay_SG.png` / `.svg`, `overlay_SLP.png` / `.svg` | T02 (Cline) | Curva extraída frente al KM de los pseudo-IPD y números en riesgo |
| `simulation_E20.png`, `simulation_E20b.png` | T02 (Cline) | Errores de E2.0a y E2.0b |

## 11. Correspondencia con el paper

Paper: `Paper_final/Paper_Doctoral_Cancer_Pulmon_PhaseField.md` (borrador v0.3). Documento metodológico: `Paper_final/METODOLOGIA_SIMULACIONES_Y_COLABORACION_IA.md`.

### 11.1 Qué partes respaldan el paper

| Parte de este informe | ¿Respalda el paper? | Secciones del paper | Observaciones |
|---|---|---|---|
| Resumen, filas E1 | Sí | Resumen, §4, §6 | Las clasificaciones se mantienen tal como se preespecificaron |
| §2.1 Métodos E1 y §8 Reproducción E1 | Sí | §3.1, §3.2 | Detalle ampliado en el documento metodológico |
| §3.1 Tabla 2 (criterio y diagnóstico ×α/100) | Sí | §4.2, Tabla 3, Tabla 4, Fig. 1 | Diagnóstico «respalda, no demuestra» |
| §3.2 PK | Sí | §4.1 | 3/6 extremos; parcialmente reproducido |
| §5.1 Discrepancias E1 | Sí | §3.4, Tabla 2 del paper | 9 discrepancias + H01 |
| §6 Limitaciones E1 | Sí | §4.4 (Limitaciones) | — |
| T06 (sección tras el §10) | Sí, como **variante corregida** | §2.4, §4.3, Tabla 5, Fig. 3 | **Sin revisión independiente** |
| §7 Licencias | Sí | §7.3 | Bloqueante para publicar |
| §10 Trazabilidad | Sí | Suplemento S4 | — |
| §2.2, §3.3–3.5, §5.2 y §6 (E2: ADRIATIC) | **Solo como contraste del protocolo** | §3.3 y Suplemento S2 | **No validan ni calibran el modelo de E1** (otra enfermedad, otro método) |
| §9 Recomendación | Parcialmente | §5, §6 | El n.º 2 (cuantificar H01) está hecho (T06); los n.º 3–4 siguen pendientes de autorización |

### 11.2 Tareas, simulaciones y resultados

| Tarea | Simulaciones | Resultado | Verificación | Sección del paper |
|---|---|---|---|---|
| T01 (Claude Code) | 46 simulaciones FEM con el código original, sin modificar (309 min), más la prueba de humo y la PK | Tabla 2: 0/88 (criterio) y 88/88 ×α/100 (diagnóstico); PK 3/6 | T03 (Cline) | §3.1–3.4, §4.1–4.2 |
| T03 (Cline) | Ninguna | Objeciones mayores H01 y H02; transcripción 88/88 | El coordinador verificó H01 en el código | §2.4, §3.3 |
| T06 (Claude Code) | 23 simulaciones (variante corregida, 184 min) + 3 (control) | Efecto de H01 relevante; determinismo exacto | **Pendiente** | §4.3 |
| T02 (Cline) | Sin simulación tumoral; 100 + 100 réplicas de verdad conocida | H1 18/18; E2.0b 1800/1800; 22/23 pruebas | T04, T05 (Claude Code) | §3.3 y S2 |
