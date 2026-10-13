# INFORME T01: reproducción del modelo de campo de fase (Wagner et al., MBE 2023), F0–F1

**Estado: revisado (T03) y corregido.** Fecha: 12-oct-2026. Responsable: Claude Code. Contrato: T01 v1.0. Revisión independiente: T03 (Cline), `Resultados/Trabajo_Cline/T03_revision_T01/REVISION_T03.md`, con dictamen de objeciones mayores (H01 y H02, sobre la interpretación; ninguna sobre las clasificaciones). Las correcciones aplicadas tras T03 se indican en el §8. **Las clasificaciones no cambian.**

## Resumen

| Bloque | Criterio (contrato §4) | Resultado | Clasificación |
|---|---|---|---|
| F0: entorno | Ejecutar el código original sin modificar | dolfin 2019.1.0 en Docker (conda-forge); prueba de humo con ambos pacientes correcta | completado |
| PK (ec. 6) | Pico y valle ≤ 0,1 % | Criterio original: 3 de 6 extremos ≤ 0,1 %; los otros tres, 0,107–0,129 % (corregido tras T03-H04; antes decía «4 de 6»). Diagnóstico: en cada dosis, una sola muestra queda desfasada medio subpaso; la dosis total es exacta | **parcialmente reproducido** |
| Correspondencia artículo–código | Lista clasificada | 35 elementos: coinciden 21 (3 por redondeo y 1 por unidades); el código resuelve 5 puntos que el artículo no especifica; 8 discrepancias, entre ellas el factor 0,7 del término del fármaco; la definición de g, evaluada con la Tabla 2 (§4.5), es la 9.ª. Añadida tras T03: inconsistencia de los parámetros PK de P2 en el script de sensibilidad (§5, n.º 10) | completado (las discrepancias se conservan) |
| Tabla 2 (88 índices g) | ≤ 10 % reproducido; H1 si ≥ 80 % | Salida directa del script: 0/88 (H1 no se cumple). Diagnóstico: con g·α/100 (ec. 4.1), los 88 valores coinciden al redondear a 3 cifras (error máx. 0,449 %) y los 88 rangos | **discrepancia**. La discrepancia de escala se elimina con α/100 (diagnóstico; §4.5). Persisten limitaciones de método (§4.5, H01) |

## 1. Fuentes y versión

- **Artículo:** Wagner A. et al., *Math Biosci Eng* 2023;20:18670–94, doi:10.3934/mbe.2023828. Tabla 1 [p. 6], ec. 4.1 [p. 16], Tabla 2 [p. 17].
- **Código:** github.com/wagnandr/immunotherapy-lung-cancer, commit `fa8e6229d1540d33014a994f1ea309d6525597aa` (14-ago-2023, último commit, anterior a la aceptación del artículo). SHA-256 del zip: `e45a8cd3…1acce`.
  - El repositorio **no tiene licencia**: se usa solo para ejecución privada, fuera de OneDrive (`<PAPERCANCER_ENV>\repos\`), y no se redistribuye.
  - Script de la Tabla 2: `reduced_models/local_sensitivity_analysis.py`, SHA-256 `e44eb9a9…b3a8`, sin modificar.

## 2. F0: entorno

- **dolfin 2019.1.0** no tiene build para Windows. Además, la imagen oficial `quay.io/fenicsproject/stable:2019.1.0.r3` usa un manifiesto v1 que Docker 29 ya no admite.
- **Imagen propia** `papercancer/t01-fenics2019:1`, construida con `env/Dockerfile` (miniforge3 + conda-forge): python 3.10.22, fenics-dolfin 2019.1.0, numpy 1.26.4, scipy 1.15.2, petsc 3.25.6 y joblib 1.6.0. El bloqueo exacto está en `env/conda_explicit_lock.txt` y el ID de la imagen en `env/imagen_t01.txt`.
- **Prueba de humo** (`src/smoke_test.py` → `logs/smoke_test.json`): 10 días simulados con los parámetros por defecto. Tiempos: 2,24 s por día simulado en P1 y 1,01 s en P2.
- **Diferencias de versión respecto a los autores:** desconocidas, porque el repositorio no fija versiones. Son una fuente de tolerancia (contrato §4.1(c)).

## 3. Farmacocinética (ec. 6)

### 3.1 Comportamiento original: criterio preespecificado

`src/pk_check.py` ejecuta el `MedicineSolver` original con los esquemas de `run_spherical_patient_1/2.py`. Después compara el último pico y el último valle del estado periódico con la fórmula analítica de la ec. 6 (`data_derived/pk_check.json`).

| Caso | Error del pico | Error del valle | ≤ 0,1 % |
|---|---|---|---|
| P1 Q2W | 0,0017 % | **0,107 %** | no |
| P2 Q3W | 0,0020 % | **0,129 %** | no |
| P2 Q6W | **0,129 %** | 0,0021 % | no |

### 3.2 Diagnóstico (no cambia el criterio)

1. **Dosis entregada.** `src/pk_diagnostico_dosis.py` y `src/pk_diagnostico_esquema.py` anulan la eliminación. Las 136 administraciones (96 de P1 y 40 de P2) entregan exactamente la dosis nominal: razón 1 (`data_derived/pk_dosis_efectiva_por_administracion.csv`).
2. **Trayectoria completa.** `src/pk_check_trayectoria.py` compara cada muestra (dt = 1/24 d) con la solución exacta, obtenida por superposición de infusiones rectangulares (`data_derived/pk_check_trayectoria.json`):
   - p99 del error relativo: 1,7·10⁻⁵ en P1 y 2,1·10⁻⁵ en P2;
   - error máximo: 0,92 % en P1 y 2,70 % en P2.
3. **Localización del error** (`src/pk_localiza_error.py`, `data_derived/pk_localizacion_error.json`; verificación del 11-oct):
   - solo 135 muestras superan el 0,1 % (95 en P1 y 40 en P2), **una por dosis**, siempre en el instante de inicio (t = s) o de fin (t = s + 1/24) de la infusión;
   - en todas, la diferencia equivale a **±0,50 subpasos** de infusión (subpaso = 1/24/32 d). La ventana de infusión efectiva del código está desplazada medio subpaso (≈ 56 s) respecto de [s, s + 1/24].

   Los «picos» y «valles» del §3.1 caen justo en esas muestras, y por eso superan el 0,1 %.
4. **Figura:** `figures/fig_pk.png` / `.svg`, con la trayectoria completa, el zoom sobre la dosis de mayor error y el error puntual con la línea de tolerancia.

### 3.3 Clasificación

**Parcialmente reproducido.**
- La ODE de la ec. 6 y la dosis total se reproducen.
- La discrepancia se limita a medio subpaso en los bordes de cada infusión de 1 h, y procede de la discretización interna del `MedicineSolver` (ambigüedad del subpaso).
- El criterio de pico y valle ≤ 0,1 % no se cumple con la definición preespecificada y se conserva así.
- Efecto previsto sobre el modelo tumoral: despreciable, porque la cantidad integrada es exacta y el desfase es de ~56 s cada 14–42 días. Esto es una **interpretación no verificada**: no se cuantificó sobre la Tabla 2.

## 4. Tabla 2: índices de sensibilidad local

### 4.1 Procedimiento

- **Script:** el original sin modificar (`local_sensitivity_analysis.py`).
- **Parámetros:** h = 10⁻³; diferencias centrales; dt = 1/24 d.
- **Horizontes:** T = 1470 d en P1 y 1102 d en P2.
- **Paralelismo:** joblib con `multiprocessing.cpu_count()` workers.
- **Lanzador:** `src/run_tabla2_original.sh`, con Docker `--cpus 8`. El único ajuste de entorno es crear `output/`, porque `solvers.py` escribe allí aunque `output_enabled=False`.
- **Paralelismo efectivo:** dentro del contenedor `cpu_count()` devuelve 14 (los núcleos del host), así que las 11 tareas de cada paciente se reparten la cuota de 8 núcleos.

### 4.2 Ejecución del 11-oct-2026: interrumpida (no evaluable)

- **Log:** `logs/tabla2_original_20261011T003301Z.log`. Inicio a las 00:33:01 UTC; simulación de referencia de P1 terminada a las 00:54:25; última línea a las 02:07:29 UTC. No contiene las listas `g_*` ni `fin_utc`.
- **Causa probable:** el registro de Windows muestra la entrada en espera moderna a las 21:29 hora local (02:29 UTC) y otra suspensión a las 00:35. El contenedor, lanzado con `--rm`, desapareció.
- Se relanzó con autorización del usuario el 12-oct (§4.3). El comparador (`src/compare_tabla2.py`) ya está probado y la tabla publicada está transcrita y verificada (`data_derived/tabla2_publicada.csv`, 22 filas × 4 métricas).

### 4.3 Ejecución del 12-oct-2026: completa

- **Log:** `logs/tabla2_original_20261012T035307Z.log`. Contenedor `t01_tabla2` (`--cpus 8`). Inicio a las 03:53:07 UTC y fin a las 09:02:20 UTC (`fin_utc`); 309 min de tiempo real; exit code 0; sin OOM.
- El log contiene las 8 listas `g_{t,p,n,vt}_list_p{1,2}` con 11 valores cada una, todos finitos.
- Los vectores de parámetros por defecto que imprime el log coinciden con los α del comparador; por ejemplo, en P2: 3,7785·10⁻³, 0,5489, 1, 20…

### 4.4 Resultados: criterio primario (salida directa del script frente a la Tabla 2)

`src/compare_tabla2.py` → `data_derived/tabla2_comparacion.csv`, `data_derived/tabla2_resumen.json`.

| Métrica | Valor |
|---|---|
| Valores comparados | 88 (2 pacientes × 11 parámetros × 4 métricas) |
| Reproducido (≤ 10 %, mismo signo) | **0** |
| Parcialmente reproducido (10–50 %) | 0 |
| Discrepancia (> 50 % o signo opuesto) | **88** (44 en P1 y 44 en P2) |
| Error relativo: mediana / p90 / máx. | 228 / 2,0·10⁵ / 1,0·10⁷ (en tanto por uno; la mediana equivale a ~22 800 %) |
| Mismo signo | 88 / 88 |
| Rangos (orden por \|g\|) que coinciden | 8 / 88 |
| **H1 (≥ 80 % reproducido)** | **no se cumple** |

**Clasificación de la Tabla 2 según el criterio preespecificado: discrepancia.** Esta clasificación no se modifica.

### 4.5 Diagnóstico de la discrepancia (no es criterio)

El código (`reduced_models/local_sensitivity_analysis.py`, l. 101–104) calcula g_script = (Q̄⁺ − Q̄⁻) / (2·h·α·Q̄), es decir, ∂_α Q̄ / Q̄ (derivada por unidad de α) por diferencias centrales con Δα = h·α y h = 10⁻³ (l. 137). La ec. 4.1 del artículo (MBE p. 16) define g := (∂_α Q̄ / Q̄) · α / 100 %, «el cambio relativo a primer orden al variar α un 1 %». El script no aplica ese factor final α/100 (elemento 5 de la §5).

> *Corrección del 12-oct-2026, antes de T03:* la versión anterior de este párrafo decía que el código calcula «(ΔQ/Q)/(Δα/α)». Era incorrecto: con esa definición el factor sería 1/100, no α/100. Los cálculos y las clasificaciones no cambian.

 `src/diag_escala_tabla2.py` aplica a g_script·α/100 la misma clasificación (`data_derived/tabla2_diag_escala.csv` y `_resumen.json`):

| Métrica | g_script·α/100 |
|---|---|
| Reproducido (≤ 10 %) | **88 / 88** |
| Error relativo: mediana / p90 / máx. | 0,068 % / 0,22 % / 0,45 % (P1 λ_P,pro, g_φT) |
| Valores con error ≤ 1 % | 88 / 88 |
| Mismo signo | 88 / 88 |
| Rangos que coinciden | **88 / 88** |

Con la transformación ×α/100 (ec. 4.1), los 88 valores coinciden con la Tabla 2 a tres cifras significativas, que es la precisión con la que están publicados. En cambio, la transformación ×α no los reproduce (mediana del error de 9 900 %).

**Notación de la ec. 4.1 (T03-H03).** El texto publicado escribe el divisor como «100 %». Interpretado literalmente como el número 1, la fórmula daría la elasticidad (×α). La prosa contigua («relative change … when varying α by 1 percent») y un desarrollo de Taylor con Δα = 0,01·α dan ×α/100. Por tanto, el factor se apoya en la descripción verbal y en la Tabla 2, no solo en la notación.

**Interpretación** (redacción revisada tras T03-H02; la versión anterior afirmaba que la simulación «reproduce los índices», que la diferencia era «única» y que la tabla «se obtuvo» aplicando α/100):
- Las salidas del log, reescaladas por α/100, coinciden con los 88 valores publicados al redondear a tres cifras significativas y conservan los 88 rangos (error máximo 0,449 %). T03 lo confirma con código propio y con la transcripción completa (88 cifras y 88 rangos) frente al texto publicado.
- Los resultados son **compatibles** con que la Tabla 2 se calculara aplicando α/100 a la salida de este script. La coincidencia **respalda, pero no demuestra**, ese postprocesado: el repositorio y el artículo no documentan cómo se generó la tabla.
- El reescalado explica la diferencia numérica observada, pero **no valida por sí solo el procedimiento**. En particular, T03-H01 detecta en P2 una inconsistencia del propio script de los autores, que consta como n.º 10 en el §5:
  - la simulación de referencia usa los parámetros farmacocinéticos de P2 (MED_mas = 143600, MED_dos = 0,20 g, MED_tim = 22 d; `default_parameters_patient2`, l. 23–32);
  - las simulaciones perturbadas ± se reconstruyen con `vector_to_parameters` (l. 35–48), que solo traslada los 11 parámetros del vector, de modo que vuelven a los valores por defecto (146000; 0,24 g; 26,7 d; `parameters.py`, l. 34–37).

  En P2, por tanto, el numerador del cociente diferencia en torno a otra configuración farmacocinética distinta de la que normaliza el denominador. Verificado también por el coordinador leyendo el código, sin ejecutarlo. **Su efecto se cuantificó después, en T06** (`Trabajo_Claude/T06_P2_H01/INFORME_T06.md`): es relevante (mediana \|Δ\| 12,6 %, máx. 45,2 %). La Tabla 2 publicada coincide con la configuración defectuosa (44/44) y no con la corregida (1/44), lo que indica que los valores publicados de P2 contienen H01.
- Las diferencias residuales (≤ 0,45 %) son compatibles con el redondeo a 3 cifras. No es necesario ni está demostrado atribuirlas a versiones de bibliotecas.
- Los 88 índices proceden de **dos pacientes calibrados**, no de 88 observaciones independientes.

**Figura:** `figures/fig_tabla2.png` / `.svg`.
- Panel A: criterio primario. Los puntos quedan entre 10 y 10⁷ veces por encima de la identidad, con un factor distinto para cada parámetro porque α varía.
- Panel B: diagnóstico. Los puntos caen sobre la identidad, dentro de la banda de ±10 %.

### 4.6 Clasificación

- **Criterio primario (contrato §4.1): discrepancia. H1 no se cumple** (0/88).
- **Diagnóstico (redacción revisada tras T03):** la discrepancia de escala observada se elimina, a la precisión publicada, aplicando α/100, coherente con la definición verbal de la ec. 4.1. Subsisten limitaciones de método (H01).
- Nota sobre el comparador (T03-H05): `compare_tabla2.py` y `diag_escala_tabla2.py` etiquetan por error relativo y signo, y calculan los rangos aparte. El contrato §4.1 pide etiquetar «parcialmente reproducido» un valor que cumple la tolerancia pero no el rango. Aquí no cambia nada: con la salida directa ningún valor cumple la tolerancia, y con α/100 todos los rangos coinciden. Si se reutilizan los scripts, habría que incorporar el rango al etiquetado.
- **Formulación para el informe integrado** (propuesta de T03, adoptada): «Con la salida directa del script, la Tabla 2 mantiene la clasificación preespecificada de discrepancia (0/88; H1 no se cumple). Como diagnóstico, multiplicar por α/100 (coherente con interpretar g como el cambio relativo ante una variación del parámetro del 1 %) recupera las 88 cifras al redondear a tres cifras significativas y los 88 rangos (error máximo 0,449 %). La coincidencia respalda, pero no demuestra, ese postprocesado. Además, en P2 las perturbaciones no conservan tres parámetros farmacocinéticos de la referencia; corregirlo (T06) cambia los índices de P2 una mediana del 12,6 % y hasta un 45,2 %. No se infiere validación predictiva ni clínica.»

## 5. Correspondencia artículo–código

Archivo: `data_derived/correspondencia_articulo_codigo.csv` (35 elementos). Discrepancias que se conservan como incertidumbre:

1. **Término del fármaco:** factor 0,7 no declarado en el artículo (`MED_eff·0,7/80`), equivalente a ω efectivo = 114,3 en lugar de 80.
2. **Inicio de terapia de P1:** primera dosis en el día 322 de los datos según el código, frente al día 296 del texto: **26 d de diferencia**. El código coincide con la Fig. 2A del preprint. (Corregido tras T03-H06: antes decía «176 d», que es el cambio de origen entre el día de simulación y el de los datos, no la discrepancia.)
3. **Esquema de P2:** Q6W desde el día 671 de los datos frente al 514 del texto (**157 d**), y fin en el día 1218 frente al 1063 (**155 d**). (Corregido tras T03-H06: antes decía «114 d», que es el cambio de origen.)
4. **Malla de P2:** 1000 elementos en el código frente a los 500 que declara el artículo.
5. **Definición de g:** ec. 4.1 frente al código (diferencia de escala α/100). **Evaluado con la Tabla 2 (§4.5):** la tabla publicada corresponde a la ec. 4.1, no a la salida directa del script.
6. **Función H:** sigmoide suave (pendiente 30) en lugar del escalón de Heaviside.
7. **Consumo de nutriente:** las células necróticas no consumen en el código.
8. **λ_τ,eff de P2:** 0,5489 en el código, que redondea a 0,55, frente a 0,54 en el artículo.
9. **T de la Tabla 2:** 9 y 2 días antes del fin de la terapia.
10. **Parámetros farmacocinéticos de P2 en el análisis de sensibilidad** (añadido tras T03-H01): la referencia usa MED_mas = 143600, MED_dos = 0,20 g y MED_tim = 22 d; las perturbaciones ±, los valores por defecto (146000; 0,24 g; 26,7 d). Ver §4.5. Efecto cuantificado en T06: relevante.

## 6. Limitaciones

- Solo hay **n = 2 pacientes**, ambos ajustados por los autores. No se evalúa la capacidad predictiva.
- No se conocen las versiones de bibliotecas que usaron los autores.
- La lectura del artículo procede del texto extraído. T03 contrastó las 88 cifras y los 88 rangos de la Tabla 2 con ese texto, no con una imagen de la página publicada.
- El efecto de la discrepancia n.º 10 (H01) sobre los índices de P2 queda fuera de T01. Se cuantificó en T06 (efecto relevante; sin revisión independiente).
- La conexión entre la Tabla 2 y α/100 es una compatibilidad numérica, no un procedimiento documentado.

## 7. Reproducción

Ver `REPRODUCIR.md`.

## 8. Revisión T03 y correcciones aplicadas (12-oct-2026)

Revisión de Cline: `Resultados/Trabajo_Cline/T03_revision_T01/REVISION_T03.md`. Dictamen: **objeciones mayores** (H01 y H02); R1 «plausible, con concordancia numérica demostrada». La clasificación de T01 se mantiene.

| Hallazgo | Severidad | Decisión del coordinador | Dónde |
|---|---|---|---|
| H01: parámetros PK de P2 no conservados en las perturbaciones | mayor | **Aceptado**, tras verificarlo en el código (l. 23–48, 87, 94; `parameters.py`, l. 34–37). Se documenta; sin simulación nueva | §4.5, §5 n.º 10, §6 |
| H02: interpretación sobredimensionada | mayor | **Aceptado.** Se rehace la redacción y se adopta la formulación propuesta | Resumen, §4.5, §4.6 |
| H03: notación «100 %» de la ec. 4.1 | menor | Aceptado | §4.5 |
| H04: PK 3/6, no 4/6 | menor | Aceptado (errata) | Resumen |
| H05: el comparador no etiqueta por rango | menor | Aceptado como nota. Sin efecto en los resultados | §4.6 |
| H06: desfases de calendario confundidos con el cambio de origen | menor | Aceptado (26, 157 y 155 d) | §5 |
| H07: precisión de `REPRODUCIR.md` | menor | Aceptado | `REPRODUCIR.md` |
| H08: la transcripción y los α son correctos | nota | — | — |

Además, la fila «definición de g» de `data_derived/correspondencia_articulo_codigo.csv` pasa de «por evaluar» a evaluada.
