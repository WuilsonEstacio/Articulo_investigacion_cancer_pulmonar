# Metodología de las simulaciones y de la colaboración con agentes de IA

| Campo | Valor |
|---|---|
| Documento | Complementario de [Paper_Doctoral_Cancer_Pulmon_PhaseField.md](Paper_Doctoral_Cancer_Pulmon_PhaseField.md) (borrador v0.3) |
| Fecha | 13-oct-2026 |
| Redacción | Claude Code (agente coordinador), a partir de los archivos citados. Lo revisa y se responsabiliza de él la persona investigadora |
| Fuentes | Contratos de tarea (`Resultados/Coordinacion/tareas/`), código propio (`src/`), registros de ejecución (`logs/`), registros de Cline (`PaperCancer_env/logs_cline/*.jsonl`), informes T01–T06 e informe integrado |
| Regla | Todo dato de este documento remite a un archivo. Lo que no se pudo comprobar se indica en el §8 |

**Cómo leerlo.** Distingue tres tipos de contenido, marcados así:
- **[ORIGINAL]:** ejecución del código de los autores, sin modificar.
- **[VARIANTE]:** ejecución con una corrección declarada. No sustituye al original; se presenta aparte.
- **[PENDIENTE]:** experimento planificado que no se ha ejecutado.

**Dos líneas de trabajo que no deben mezclarse:**
- **E1, campo de fase de CPCNP** (Wagner et al., MBE 2023): es el objeto del paper.
- **E2, ADRIATIC** (CPCP, reconstrucción de curvas de supervivencia): es otro problema, otra enfermedad y otro método, estadístico y no de simulación tumoral. **No valida el modelo de E1.** En el paper solo aparece como contraste del protocolo de auditoría (§3.3 y Suplemento S2).

---

## 1. Mapa de tareas, simulaciones y secciones del paper

| Tarea | Línea | Tipo | Ejecutó | Verificó | Estado (`ESTADO_TAREAS.md`) | Sección del paper |
|---|---|---|---|---|---|---|
| T00 | — | Prueba de delegación a Cline | Claude Code | — | aceptada | §7.4 |
| T01 | E1 | **[ORIGINAL]** Entorno, PK, Tabla 2 (46 simulaciones FEM), correspondencia artículo–código | Claude Code | Cline (T03) | aceptada, con correcciones tras T03 | §2.3, §3.1–3.4, §4.1–4.2, Tablas 2–4 |
| T03 | E1 | Revisión crítica de T01, **sin simulaciones** | Cline | Claude Code (verificó H01 leyendo el código) | aceptada | §2.4, §3.3, Tabla 3 |
| T06 | E1 | **[VARIANTE]** Re-simulación de P2 con H01 corregido (23 simulaciones) y control de determinismo (3 simulaciones) | Claude Code | **Sin revisión independiente** | entregada | §2.4, §3.1, §4.3, Tablas 4–5, Fig. 3 |
| T02 | E2 | Extracción vectorial y reconstrucción de Guyot de ADRIATIC; validación con verdad conocida (E2.0a/b) | Cline | Claude Code (T04, T05) | aceptada (ronda 1, con observaciones) | Solo §3.3 y Suplemento S2 |
| T04 | E2 | Auditoría de la entrega inicial de T02 | Claude Code | — | aceptada (dictamen: requiere corrección D1, D2) | Suplemento S2 |
| T05 | E2 | Auditoría de la corrección de T02 | Claude Code | — | aceptada (dictamen: T02 aceptada) | Suplemento S2 |
| INT | E1 + E2 | Informe integrado F0–F1 | Claude Code | — | entregado (incluye T06) | Suplemento S4 |

Fuente: [`Resultados/Coordinacion/ESTADO_TAREAS.md`](../Resultados/Coordinacion/ESTADO_TAREAS.md).

---

## 2. E1: qué se simuló y con qué objetivo

### 2.1 Objetivo

Comprobar si los resultados publicados de Wagner et al. (MBE 2023) se regeneran con su código y sus datos (fases F0–F1 del plan; hipótesis H1). Además, tras la revisión T03, cuantificar el efecto del defecto H01 sobre los índices de P2 (T06).

Las simulaciones **no** buscaban calibrar, predecir ni optimizar dosis. Esos objetivos están en el §2.8 como [PENDIENTE].

### 2.2 Modelo

Es el modelo 1D radial de los autores: campo de fase de Cahn–Hilliard con tumor proliferativo y necrótico, nutriente cuasiestacionario y PK monocompartimental del anticuerpo. Se resolvió con elementos finitos en FEniCS/dolfin 2019.1.0. Ecuaciones: paper, §2.1–2.2.

**Numeración de ecuaciones.** El plan y los informes internos usan la del preprint (D02): la PK es la «ec. 6». El paper usa su propia numeración: PK = ec. (4); índice de sensibilidad = ec. (5), que corresponde a la ec. 4.1 del artículo publicado.

### 2.3 Fuentes, datos y parámetros

| Elemento | Detalle | Fuente |
|---|---|---|
| Artículo | Wagner et al., *Math Biosci Eng* 2023;20:18670–94 (CC BY 4.0). Texto extraído de la versión publicada. El PDF de `Data_insumo` es el preprint arXiv v1 y **no** contiene la ec. 4.1 ni la Tabla 2 | `Resultados/03_registro_busquedas/MBE_2023_Wagner_texto_extraido.txt` |
| Código | `github.com/wagnandr/immunotherapy-lung-cancer`, commit `fa8e6229d1540d33014a994f1ea309d6525597aa` (14-ago-2023). SHA-256 del zip: `e45a8cd3…1acce`. **Sin licencia:** se ejecuta en privado fuera de OneDrive (`PaperCancer_env/repos/`), montado en solo lectura, y no se copia ni redistribuye | `INFORME_T01.md` §1 |
| Script de la Tabla 2 | `reduced_models/local_sensitivity_analysis.py`, SHA-256 `e44eb9a9…b3a8`, sin modificar (el hash se imprime en la cabecera del log) | log de T01 |
| Parámetros | Los valores por defecto del código: `default_parameters_patient1/2` y `parameters.py`. **No se recalibró nada.** No hay configuración YAML propia (la carpeta `config/` de T01 está vacía): los parámetros son los del código de los autores | `INFORME_T01.md` §4–5 |
| Datos de pacientes | CSV de volúmenes del repositorio (P1: 21 tiempos; P2: 11 valores; plan §B, C1). **Ninguna salida de T01 ni de T06 se compara con estos volúmenes:** los índices de sensibilidad se calculan sobre integrales del modelo. La comparación de trayectorias con los datos (E1.2) está [PENDIENTE] | plan; salidas de T01/T06 |

### 2.4 Entorno de ejecución

| Componente | Versión o detalle | Fuente |
|---|---|---|
| Imagen Docker | `papercancer/t01-fenics2019:1`, construida con `env/Dockerfile` (miniforge3 + conda-forge). Motivo: dolfin 2019.1.0 no existe para Windows, y la imagen oficial `quay.io/fenicsproject/stable:2019.1.0.r3` usa un manifiesto v1 que Docker 29 no admite | `T01_phasefield/env/`, `INFORME_T01.md` §2 |
| Paquetes clave | python 3.10.22, fenics-dolfin 2019.1.0, numpy 1.26.4, scipy 1.15.2, petsc 3.25.6, joblib 1.6.0, MPICH 5.0.1. Bloqueo exacto en `env/conda_explicit_lock.txt` e ID de la imagen en `env/imagen_t01.txt` | ídem; log de T01 (línea de versiones); preespecificación T06 §7 |
| Análisis sin dolfin | `PaperCancer_env/venv_claude_T01` (Python 3.10, numpy 1.26.4, matplotlib 3.10.9, pymupdf) | `REPRODUCIR.md` de T01 |
| Equipo | Windows 11 con Docker Desktop y Git Bash; 14 núcleos; la máquina virtual de Docker tenía 7,48 GiB | `INFORME_T01.md` §4.1; `t06_resumen.json` → `recursos` |
| Límites del contenedor | `--cpus 8`. En T06 (intento 2), además, `--shm-size=1g` | lanzadores |
| Paralelismo | El script de los autores lanza `multiprocessing.cpu_count()` workers de joblib/loky. Según T01 §4.1, dentro del contenedor ese valor es 14, de modo que las 11 tareas de cada paciente se reparten la cuota de 8 CPU. La línea `nproc_visible=1` de la cabecera del log de T01 **no lo contradice**: GNU `nproc` respeta `OMP_NUM_THREADS=1`, que el lanzador fija. El log no imprime directamente el valor de `cpu_count()` (§8) | log de T01; `INFORME_T01.md` §4.1 |
| Mantener el equipo activo | `PaperCancer_env/mantener_despierto.ps1` y `restaurar_suspension.ps1` (T01); `vigilar_t06.ps1` (T06, que además muestrea memoria y CPU cada 60 s) | `PaperCancer_env/` |

### 2.5 Simulaciones originales [ORIGINAL] (T01)

| Id. | Qué | Simulaciones | Duración | Resultado | Registro |
|---|---|---|---|---|---|
| S0 | Prueba de humo: 10 días con parámetros por defecto, P1 y P2 | 2 | ~40 s; 2,24 s por día simulado (P1) y 1,01 s (P2) | Correcta | `T01_phasefield/logs/smoke_test.json` |
| S1 | PK: `MedicineSolver` original frente a la solución exacta, sin FEM y fuera de Docker | — (EDO) | Segundos | 3 de 6 extremos ≤ 0,1 %; dosis total exacta en 136 administraciones | `data_derived/pk_check.json`, `pk_check_trayectoria.json`, `pk_localizacion_error.json` |
| S2 | Tabla 2, ejecución del 11-oct | 46 previstas | Interrumpida tras ~1,5 h | **No evaluable.** Causa probable: suspensión del equipo (registro de Windows: espera moderna a las 02:29 UTC); el contenedor tenía `--rm` y desapareció | `logs/tabla2_original_20261011T003301Z.log`; `INFORME_T01.md` §4.2 |
| S3 | Tabla 2, ejecución del 12-oct: `local_sensitivity_analysis.py` sin modificar; 2 pacientes × (1 referencia + 11 parámetros × 2 perturbaciones ±0,1 %); h = 10⁻³; dt = 1/24 d; T = 1470 d (P1) y 1102 d (P2) | 46 | **309 min** (03:53–09:02 UTC). La parte de P2 duró 2 h 04 min | Exit 0, sin OOM. 8 listas `g_*` con 11 valores finitos | `logs/tabla2_original_20261012T035307Z.log` |

**Comandos.** Están en [`T01_phasefield/REPRODUCIR.md`](../Resultados/Trabajo_Claude/T01_phasefield/REPRODUCIR.md), que cubre la imagen, la prueba de humo, la PK, la Tabla 2, la comparación y el diagnóstico. El lanzador es [`src/run_tabla2_original.sh`](../Resultados/Trabajo_Claude/T01_phasefield/src/run_tabla2_original.sh). Escribe en la cabecera del log el commit, el SHA-256 del script y las versiones, y pone hora a cada línea.

- **Único ajuste de entorno:** se crea `output/`, porque `solvers.py` escribe allí aunque `output_enabled=False`.
- **Contenedor sin `--rm`:** la ejecución de referencia del 12-oct se lanzó sin `--rm` (`Coordinacion/PROMPT_REANUDAR_20261011.md`), para que el contenedor sobreviviera a una interrupción. `REPRODUCIR.md` usa el mismo comando.

**Análisis de las salidas** (scripts propios de Claude Code):
- `compare_tabla2.py`: aplica el criterio preespecificado.
- `diag_escala_tabla2.py`: diagnóstico de la escala ×α/100; **no es criterio**.
- `fig_tabla2.py`.
- Scripts de PK: `pk_check.py`, `pk_check_trayectoria.py`, `pk_localiza_error.py`, `pk_diagnostico_dosis.py`, `pk_diagnostico_esquema.py` y `fig_pk.py`.

**Criterio de F0 del plan** («una corrida 1D tarda ≤ 30 min»):
- la referencia de P1 terminó unos 21 min después del arranque (00:33:01 → 00:54:25 UTC, ejecución del 11-oct);
- la referencia de P2 tardó unos 36 min en el intento 1 de T06 (23:10:50 → 23:47:12 UTC), con un proceso de control en paralelo.

Ambas cifras se leen en las marcas de tiempo de los logs y no son mediciones aisladas.

### 2.6 Variante corregida [VARIANTE] (T06)

**Por qué.** T03 detectó H01. En P2, las simulaciones perturbadas se reconstruyen con `vector_to_parameters` (l. 35–48), que no conserva MED_mas, MED_dos ni MED_tim. Por eso vuelven a los valores por defecto (146 000 g/mol; 0,24 g; 26,7 d) en lugar de los de P2 (143 600; 0,20 g; 22 d). El coordinador lo verificó leyendo el código. P1 no se ve afectado.

**Preespecificación.** [`PREESPECIFICACION_T06.md`](../Resultados/Trabajo_Claude/T06_P2_H01/PREESPECIFICACION_T06.md) se escribió **antes** de lanzar y fija:
- el control de determinismo (diferencia relativa ≤ 10⁻⁸);
- las métricas: Δ_rel, signos y rangos;
- las clases de efecto: despreciable (≤ 0,5 %), menor (≤ 10 %) o relevante (> 10 %, o cualquier cambio de signo o de rango).

Sus §6–7 se añadieron después y solo documentan incidencias de ejecución. Ningún criterio cambió.

**Qué cambia y qué no.**
- Se llama a `run_local_sensitivity_analysis` **original y sin modificar**, con los mismos dt, T, h y paralelismo.
- El único cambio es el argumento `runner`: [`src/t06_runner.py`](../Resultados/Trabajo_Claude/T06_P2_H01/src/t06_runner.py) restaura el triplete PK de P2 antes de cada simulación, llama al `run_patient_2_parametrized` original y escribe las integrales Q en `data_derived/q_corr/`.
- El script de lanzamiento es `src/run_p2_h01.py`.

| Id. | Qué | Simulaciones | Duración | Resultado | Registro |
|---|---|---|---|---|---|
| V0a | Prueba de humo de 5 d, primer intento | 23 | — | **Falló:** SIGSEGV en los workers. El envoltorio estaba definido en `__main__` y se serializaba por valor | preespecificación §6 |
| V0b | Prueba de humo de 5 d con el envoltorio en un módulo importable | 23 | — | Exit 0. 22 perturbadas corregidas; la referencia ya traía P2 | ídem; `PaperCancer_env/runs_t06_smoke/` |
| V1 | Intento 1, corrida principal (contenedor `t06_p2_h01`) | 1 terminada de 23 | 23:10–23:47 UTC | **Falló** al arrancar los 11 workers: SIGSEGV/SIGBUS en `cpp.MPI.init()`. Exit 1, sin OOM, pico de 1,28 GiB | `logs/intento1_fallido_SIGBUS/` |
| C1 | Control de determinismo **con el defecto original**: componente 1 de P2 (λ_τ^eff), referencia y ± (`src/control_p2_bug.py`, concurrente con V1) | 3 | — | Exit 0. Los 4 índices son idénticos al log de T01 (diferencia relativa 0,0) | `logs/t06_control_bug_20261012T231050Z.log`; `data_derived/control_bug_comp1.json` |
| V2 | Intento 2, corrida principal (contenedor `t06_p2_h01b`, `src/run_t06_main.sh`): `--shm-size=1g`, sin procesos concurrentes y con reintento automático (máximo 3) solo ante `TerminatedWorkerError` | 23 | **183,6 min** (23:52–02:55 UTC) | Exit 0, sin OOM, sin necesidad de reintento. Pico de 1,36 GiB; CPU media de 7,2 núcleos (máx. 9,6); 177 muestras | `logs/t06_p2_h01_20261012T235219Z.log`; `logs/docker_stats.csv`; `logs/docker_inspect_final.txt` |

**Causa del fallo de V1.** Es probable, pero **no está demostrada**: contención en la inicialización de MPI con unos 16 procesos y `/dev/shm` de 64 MB. La preespecificación §7 recoge también los datos que debilitan esta hipótesis.

**Análisis.**
- `src/analiza_t06.py` genera `t06_resumen.json`, `t06_p2_indices.csv`, `t06_88_corregido.csv` y `figures/fig_h01.*`.
- `src/tablas_paper.py` genera las Tablas 4 y 5 del paper directamente desde los CSV, sin transcribir cifras a mano.

Comandos: [`INFORME_T06.md`](../Resultados/Trabajo_Claude/T06_P2_H01/INFORME_T06.md) §4.

### 2.7 Resultados de E1, por tipo

| Resultado | Tipo | Valor | Clasificación | Verificación |
|---|---|---|---|---|
| PK | [ORIGINAL] | 3/6 extremos ≤ 0,1 %; dosis total exacta; desfase de ±0,5 subpasos (≈ 56 s) | Parcialmente reproducido | T03 (corrigió la errata «4/6») |
| Tabla 2, salida directa del script | [ORIGINAL] | 0/88; signos 88/88; rangos 8/88 | **Discrepancia; H1 no se cumple** (sin cambios) | T03 |
| Tabla 2 ×α/100 | Diagnóstico sobre [ORIGINAL] | 88/88 a 3 cifras; rangos 88/88; error máx. 0,449 % | Explicación numérica: **respalda, no demuestra** el postprocesado | T03: concordancia demostrada con código propio; postprocesado «plausible» |
| Correspondencia artículo–código | [ORIGINAL] | 35 elementos: 21 coinciden, 5 los resuelve el código, 9 discrepancias (incluida la definición de g), más H01 | Completado | T03 (corrigió los desfases de calendario: 26/157/155 d) |
| Efecto de H01 en P2 | [VARIANTE] | Mediana \|Δ\| 12,6 %, máx. 45,2 %; 0 cambios de signo; 7 cambios de rango (todos en V_vis) | **Relevante** (preespecificado) | **Sin revisión independiente**; determinismo exacto (C1) |
| P2 corregido frente a la Tabla 2 publicada | [VARIANTE] | 1/44 a 3 cifras (19/44 ≤ 10 %), frente a 44/44 con la configuración original | Inferencia: la tabla publicada contiene H01 (por coincidencia numérica, no documentada) | Sin revisión independiente |
| 88 combinados (P1 original + P2 corregido) | [VARIANTE] | 45/88 a 3 cifras; 63/88 ≤ 10 %; rangos 81/88 | Informativo | `t06_resumen.json` → `acuerdo_con_tabla2` |

### 2.8 Experimentos de E1 pendientes [PENDIENTE]

Ninguno se ha ejecutado. Todos requieren la autorización de la persona investigadora:
- **E1.2b:** trayectorias V_vis(t) de P1 y P2 frente a los datos (Fig. 3 del artículo).
- **E1.3:** reimplementación independiente (segunda parte de H1: L2 ≤ 5 %) y convergencia en malla (250/500/1000) y en paso (1/12, 1/24, 1/48).
- **E1.4–E1.5 (F2):** calibración por máxima verosimilitud y perfiles. Requiere además el permiso de los autores para publicar análisis nuevos con sus datos.
- **E1.6–E1.7 (F3):** comparadores EDO y predicción con origen móvil.
- Optimización de dosis y modelo 3D: fuera del alcance actual.
- **Revisión independiente de T06.**

---

## 3. E2: ADRIATIC (no valida E1)

**Objetivo (T02, plan E2.0–E2.2).** Reconstruir datos individuales aproximados (pseudo-IPD) de las curvas de Kaplan–Meier de SG y SLP de ADRIATIC (Cheng et al., NEJM 2024) y validarlos frente a 18 cantidades publicadas, con tolerancias fijadas antes de ejecutar.

**Qué es y qué no es.**
- **Es** extracción de datos y estadística de supervivencia: Guyot 2012, KM y Cox.
- **No es** una simulación de la dinámica tumoral.
- Las únicas «simulaciones» son de validación con verdad conocida:
  - E2.0a: 100 réplicas sin digitalización;
  - E2.0b: las mismas 100 réplicas dibujadas en PDF vectoriales sintéticos y extraídas con el mismo `extract.py`.
- Las semillas son 20261010 + r.

| Elemento | Detalle | Fuente |
|---|---|---|
| Datos | Curvas vectoriales de la Fig. 1A (p. 6) y la Fig. 2A (p. 8) del PDF de NEJM (solo lectura), números en riesgo y eventos totales (`Resultados/04_plan/tabla_insumos_E2_ADRIATIC.csv`) | contrato T02 §2 |
| Entorno | `PaperCancer_env/venv_cline_T02` (python 3.10.0; numpy 1.26.4, scipy 1.11.4, pandas 2.3.3, lifelines 0.30.0, pymupdf 1.28.2, PyYAML 6.0.3); hilos = 1; máximo 4 procesos | contrato T02 §3; `requirements_T02.txt` |
| Configuración | `T02_ADRIATIC/config/config.yaml` (rutas, colores, semillas, tolerancias) y `CRITERIOS_PREESPECIFICADOS.md` | T05 V3: hashes idénticos a los de la ronda 0 |
| Comando | `run_logged.py pipeline.py --stage all`, seguido de `unittest discover` y `verify_outputs.py` | [`T02_ADRIATIC/REPRODUCIR.md`](../Resultados/Trabajo_Cline/T02_ADRIATIC/REPRODUCIR.md) |
| Duración | Ejecución final de Cline: 1093 s (`logs/20261011_230459_401462.json`). Re-ejecuciones aisladas del coordinador: 146 s (T04) y 225 s (T05) | registros citados |
| Resultados | H1 18/18 en las versiones original y corregida; números en riesgo 88/88 (corregida); E2.0b 1800/1800 dentro de tolerancia | `INFORME_INTEGRADO_F0_F1.md` §3.3–3.5 |
| Prueba fallida | `test_e20b_all_replicates_same_truth_and_diagnostics`: 22/23 pruebas. Hay 7 de 400 curvas sintéticas que pierden una meseta más estrecha que la precisión del PDF (o de ancho nulo). Sin efecto medible. **No se modificó la prueba** | T05 O-T05-1; informe integrado §5.2 |
| Pendiente | E2.3–E2.5 (RMST, extrapolación y validación temporal): **[PENDIENTE]**, no autorizados | plan §C, E2 |

**Nomenclatura de las rondas de T02.** Los documentos no la usan de forma uniforme:

| Momento | Informe integrado y T05 | T04 | Registro de Cline |
|---|---|---|---|
| Entrega inicial, 10-oct | «ronda 0» | «ronda 1» | `logs_cline/T02_ronda1.jsonl` |
| Corrección de D1 y D2, 11-oct | «ronda 1» | — | `logs_cline/T02_ronda2_correccion1.jsonl` |
| Cierre documental, 12-oct | «cierre» | — | `logs_cline/T02_ronda2_cierre.jsonl` |

---

## 4. Reparto del trabajo entre la persona investigadora y los agentes de IA

**Principio.** Los agentes de IA son herramientas de ejecución y revisión bajo supervisión humana. **No son autores científicos.**
- Las decisiones las tomó la persona investigadora: autorizaciones, presupuestos, qué se integra y qué se publica.
- Esa persona es responsable del contenido (paper, §7.4).

### 4.1 Persona investigadora y manejo de las herramientas

- **Manejo de las herramientas:** Wuilson Estacio manejó los agentes de IA (Claude Code y Cline), el IDE (Visual Studio Code, desde el que se ejecuta Claude Code) y el entorno de cómputo (Docker).
- Autorizó cada fase y cada ejecución pesada: F0–F1, el relanzamiento de la Tabla 2, T03 con un tope de 10 USD y T06.
- Fijó las restricciones de trabajo:
  - no tocar `Data_insumo`;
  - no recalibrar ni cambiar tolerancias;
  - no redistribuir el código de los autores;
  - no contactar a nadie ni publicar nada;
  - no sustituir a Cline sin aviso;
  - no lanzar ejecuciones pesadas en paralelo;
  - recibir un aviso antes de integrar o de relanzar tras un fallo.
- Tiene pendientes las decisiones del documento de brechas: consulta a los autores, F2 y revisión de T06.

### 4.2 Claude Code (Anthropic): coordinación, ejecución de E1 y auditorías

**Implementó:**
- **T01:**
  - la imagen Docker y el bloqueo de conda (`env/`);
  - los envoltorios y análisis de `T01_phasefield/src/` (lanzador, comparador, diagnóstico de escala, PK y figuras);
  - la transcripción de la Tabla 2 (`data_derived/tabla2_publicada.csv`);
  - la tabla de correspondencia (`correspondencia_articulo_codigo.csv`).
- **T06:**
  - la preespecificación;
  - `t06_runner.py`, `run_p2_h01.py`, `control_p2_bug.py`, los lanzadores, `analiza_t06.py` y `tablas_paper.py`.
- **T04 y T05:** re-ejecución aislada, extracción ráster independiente (`raster_check.py`, `ticks.py`), KM y Cox propios sin lifelines (`km_cox_indep.py`), detector de escalones fusionados (`merged_steps.py`) y análisis de la prueba fallida (`meseta_perdida_cual.py`, entre otros).
- **Coordinación:** los contratos de tarea, el tablero de estado, el informe integrado, el borrador del paper y este documento.

**Verificó:**
- las entregas de Cline (T04, T05);
- el hallazgo H01 de T03, leyendo el código antes de aceptarlo.

**No verificado de forma independiente:**
- su propio trabajo en T06;
- la redacción del paper.

### 4.3 Cline (CLI 3.0.70; proveedor `openai-codex`, modelo `gpt-6-astra`, `--thinking high`): ejecución de E2 y revisión de E1

**Implementó:**
- **T02:** la extracción vectorial con PyMuPDF, el algoritmo de Guyot propio, la validación con lifelines, las simulaciones E2.0a/b, la comparación entre rondas (`round1.py`) y 23 pruebas.
- **T03:** revisión con código propio (`revisar_t03.py`, `validar_entrega.py`). Analizó el script de los autores de forma estática, sin importarlo, y **no ejecutó simulaciones**.

**Revisó:**
- T01: dictamen de «objeciones mayores»:
  - H01: defecto de configuración de P2;
  - H02: interpretación que iba más allá de la evidencia;
  - H03–H07: menores.

  La clasificación de T01 no cambió.

### 4.4 Cómo se delegaron las tareas

1. **Contrato escrito antes de ejecutar** (`Resultados/Coordinacion/tareas/`). Fija:
   - objetivo y lo que queda fuera del alcance;
   - fuentes en solo lectura;
   - carpeta exclusiva de escritura;
   - entorno autorizado;
   - criterios y tolerancias preespecificados;
   - entregables;
   - límites: procesos, presupuesto y número de rondas;
   - la regla de que el ejecutor **no declara la aceptación**.

   Contratos: [T01](../Resultados/Coordinacion/tareas/T01_phasefield_reproduccion_Claude.md), [T02](../Resultados/Coordinacion/tareas/T02_ADRIATIC_reconstruccion_Cline.md), [corrección de T02](../Resultados/Coordinacion/tareas/T02_correccion_ronda1_Cline.md), [cierre de T02](../Resultados/Coordinacion/tareas/T02_correccion_ronda1_cierre_Cline.md) y [T03, v2](../Resultados/Coordinacion/tareas/T03_revision_T01_Cline.md).
2. **Invocación de Cline**, en modo no interactivo y con registro JSON:
   `cline.cmd -P openai-codex -m gpt-6-astra --thinking high --json -t <segundos> -c <directorio> "<encargo>"`.
   - La salida se guarda en `PaperCancer_env/logs_cline/<tarea>.jsonl`.
   - El límite de tiempo fue de 120 s en las pruebas de créditos y de 2400 o 5400 s en las tareas.
3. **Prueba de créditos** (`PRUEBA_OK`) antes de cada encargo, a partir del 11-oct.
4. **Vigilante de coste** en T03: un proceso en PowerShell que lee `totalCost` y corta la sesión al llegar al umbral. Su marca de fin está en `logs_cline/T03_revision_T01.jsonl.vigia.txt`.
5. **Canal de mensajes:** `Coordinacion/comunicaciones/claude_a_cline.md` y `cline_a_claude.md`, solo para añadir mensajes.
6. **Tablero de estado:** solo el coordinador cambia [`ESTADO_TAREAS.md`](../Resultados/Coordinacion/ESTADO_TAREAS.md).

### 4.5 Cómo se comprobaron las entregas

| Entrega | Comprobación | Resultado |
|---|---|---|
| T02, entrega inicial (T04) | Re-ejecución completa en una copia aislada; comparación SHA-256 de 1248 archivos; extracción ráster independiente; KM y Cox propios; hashes de `guyot.py` y `extract.py` en 13 instantáneas; búsqueda de fugas de cifras publicadas | Reproducible; sin fugas. Defectos **D1** (escalones fusionados) y **D2** (E2.0 no probaba la extracción) → corrección |
| T02, corrección (T05) | Re-ejecución aislada: 4660/4661 archivos idénticos. Pruebas (22/23). Tolerancias con el mismo hash. 39 derivados clínicos idénticos antes y después del último cambio de `extract.py`. KM y Cox propios | Aceptada con observaciones O-T05-1 (prueba fallida) y O-T05-2 (dos líneas de texto editadas durante la ejecución final, sin efecto en las salidas) |
| T01 (T03) | Recálculo propio de las 88 comparaciones; 7 transformaciones de escala; retranscripción de 88 cifras y 88 rangos; 22 vectores α; análisis estático | Objeciones mayores aceptadas. Correcciones en `INFORME_T01.md` §8 |
| T03 (coordinador) | Lectura del código para confirmar H01 (l. 23–48, 87, 94; `parameters.py` l. 34–37) | Confirmado |
| T06 | Control de determinismo preespecificado | Superado. **Falta la revisión independiente** |

### 4.6 Costes de Cline

Comprobados con el último `totalCost` de cada registro `logs_cline/*.jsonl`. No se registra el coste de Claude Code.

| Sesión | USD | Fin |
|---|---|---|
| Prueba de créditos, 11-oct | 0,046 | completed |
| T02, entrega inicial (`T02_ronda1.jsonl`) | 9,072 | error: «The usage limit has been reached» |
| T02, corrección (`T02_ronda2_correccion1.jsonl`) | 9,111 | aborted (`external_abort`); la ejecución lanzada antes terminó con exit 0 |
| Prueba de créditos, 12-oct | 0,048 | completed |
| T02, cierre | 1,655 | completed |
| Prueba de créditos de T03 | 0,046 | completed |
| T03, sesión 1 (cortada por un error de fuente del coordinador) | 0,574 | cortada |
| T03, revisión (v2) | 2,735 | completed |
| **Total** | **≈ 23,29** | T02: 19,84; T03: 3,36 con su prueba de créditos |

### 4.7 Incidencias de la colaboración

- **T02, entrega inicial:** se agotó el límite de uso a las 44 iteraciones. La entrega se auditó tal como quedó.
- **T02, corrección:** la sesión fue interrumpida desde fuera (`external_abort`). El cierre se hizo en una sesión aparte, sin recálculos.
- **T03:** el primer encargo señalaba como fuente el PDF del preprint, que no contiene la ec. 4.1 ni la Tabla 2. Fue un error del coordinador. Se cortó la sesión y se reenvió la v2; la sesión cortada está en `T03_revision_T01/sesion1_cortada/`.
- **Antes de T03:** el coordinador corrigió una frase incorrecta suya sobre la definición de g en el código, y T03 confirmó la corrección.

---

## 5. Correcciones, discrepancias, pruebas fallidas y limitaciones

| # | Elemento | Tipo | Estado | Fuente |
|---|---|---|---|---|
| 1 | Definición de g: el script omite el factor α/100 de la ec. 4.1 | Discrepancia artículo–código | Se conserva; diagnóstico 88/88 | `INFORME_T01.md` §4.5 |
| 2 | H01: PK de P2 no conservada en las perturbaciones | Defecto del script de los autores | Cuantificado en T06 (relevante); el original no se modifica | T03; T06 |
| 3 | Factor 0,7 no declarado; calendarios desplazados 26/157/155 d; malla de P2; H sigmoide; consumo necrótico; λ_τ^eff de P2 = 0,5489; horizonte T | Discrepancias artículo–código | Se conservan como incertidumbre; efectos no cuantificados por separado | `INFORME_T01.md` §5 |
| 4 | PK: desfase de ±0,5 subpasos | Detalle del solucionador | Criterio no cumplido (3/6); se mantiene | `INFORME_T01.md` §3 |
| 5 | Erratas del coordinador (PK «4/6»; desfases «176/114 d»; fórmula de g) | Errores de redacción propios | Corregidos tras T03, con registro | `INFORME_T01.md` §8 |
| 6 | Comparador de T01: no etiqueta «parcial» por rango | Defecto menor del script propio | Sin efecto en los resultados; corregir si se reutiliza | T03-H05 |
| 7 | Ejecución de la Tabla 2 del 11-oct interrumpida | Incidencia | No evaluable; relanzada | `INFORME_T01.md` §4.2 |
| 8 | Intento 1 de T06 (SIGSEGV/SIGBUS en `MPI.init`) | Incidencia | Archivado; causa probable, no demostrada | preespecificación T06 §7 |
| 9 | D1 y D2 de T02 | Defectos del ejecutor (Cline) | Corregidos y verificados (T05) | T04, T05 |
| 10 | Prueba E2.0b, 7/400 curvas | Prueba fallida | Declarada; la prueba no se modificó | T05 O-T05-1 |

**Limitaciones principales de E1:**
- n = 2 pacientes calibrados a mano;
- versiones de bibliotecas de los autores desconocidas;
- solo el modelo 1D;
- la Tabla 2 se transcribió a partir del texto extraído, no de una imagen de la página;
- H1 está incompleta (falta E1.3);
- T06 no tiene revisión independiente;
- la novedad no está verificada (Scibilia 2024);
- toda la verificación cruzada la han hecho agentes de IA. El plan (§D.3) preveía una persona revisora con conocimiento de elementos finitos y bioestadística, y esa revisión humana experta no se ha hecho.

Detalle: [`INFORME_INTEGRADO_F0_F1.md`](INFORME_INTEGRADO_F0_F1.md) §6.

---

## 6. Pasos para reproducir

La guía ordenada y autocontenida para reproducir los resultados en otro equipo es el **Suplemento S5 del paper**. Incluye los comandos con rutas genéricas, el trabajo sobre copias limpias para no sobrescribir los resultados de referencia y los valores esperados en cada paso. Lo que sigue es un resumen.

1. **Obtener el código de los autores.** Descargar el commit `fa8e6229` de GitHub y comprobar el SHA-256 del zip (`e45a8cd30cf57efea8980a60a952816c3a725cf3627acecadca0d41b1312acce`). No se incluye en el proyecto.
2. **E1 original (T01):** seguir [`REPRODUCIR.md`](../Resultados/Trabajo_Claude/T01_phasefield/REPRODUCIR.md).
   - Imagen → prueba de humo (unos 40 s) → PK (segundos) → Tabla 2 (unos 309 min con 8 CPU; el equipo no debe suspenderse) → `compare_tabla2.py` → `diag_escala_tabla2.py`.
3. **E1, variante (T06):** seguir [`INFORME_T06.md`](../Resultados/Trabajo_Claude/T06_P2_H01/INFORME_T06.md) §4.
   - Contenedor con `--shm-size=1g`, sin otros procesos pesados (unos 184 min) → `analiza_t06.py` → `tablas_paper.py`.
   - El control de determinismo se lanza con `run_t06.sh`.
4. **E2 (T02):** seguir [`T02_ADRIATIC/REPRODUCIR.md`](../Resultados/Trabajo_Cline/T02_ADRIATIC/REPRODUCIR.md), en el entorno `venv_cline_T02`. Tarda minutos.
5. **Comparación esperada:**
   - T01: los valores `g_*` del log deben coincidir con `tabla2_comparacion.csv`;
   - T06: control idéntico al log de T01;
   - T02: hashes del manifiesto `manifest_sha256.csv` (en T05 coincidieron 4660 de 4661; la excepción son las rutas absolutas de `PROCEDENCIA.md`).

---

## 7. Qué respalda cada documento al paper

| Documento | Qué evidencia aporta | Secciones del paper |
|---|---|---|
| [`Primera_entrega_contribuciones_y_plan.md`](Primera_entrega_contribuciones_y_plan.md) | Hipótesis, tolerancias y criterios de continuar o descartar, **fijados antes de ejecutar** (10-oct). Contexto clínico (NLST, NELSON). Su sección E recoge el estado de ejecución | §1.1, §1.3, §3.2, §5 (hoja de ruta) |
| [`INFORME_INTEGRADO_F0_F1.md`](INFORME_INTEGRADO_F0_F1.md) | Resultados verificados de T01 y T02, discrepancias, limitaciones, licencias y trazabilidad (§10), incluida T06; §11: correspondencia con el paper | §3–§4, §6, §7.3, S2, S4 |
| Este documento | Simulaciones, entorno, comandos, reparto del trabajo y verificación de entregas | §3.1, §3.3, §7.4 |
| [`Estado_Paper_Doctoral_brechas.md`](Estado_Paper_Doctoral_brechas.md) | Título y alcance del paper, y lo que falta antes del envío | Nota de estado; §5–§6 |

---

## 8. Cuestiones que no se pudieron verificar

- **El valor de `multiprocessing.cpu_count()` dentro del contenedor (14).** Procede de T01 §4.1 y de T03-H07; no aparece impreso en los logs. Indicios indirectos: CPU media de 7,2 núcleos y hasta 48 PID en T06. No se ha relanzado ningún contenedor para comprobarlo, porque esta revisión no ejecuta nada.
- **La causa de la interrupción del 11-oct** (suspensión del equipo) **y la del intento 1 de T06** (`/dev/shm` y MPI). Ambas son probables, no demostradas.
- **Que los autores generaran la Tabla 2 con ×α/100,** y que la columna publicada de P2 se calculara con H01. Ambas cosas se infieren por coincidencia numérica; no hay documentación.
- **El efecto, por separado, de las discrepancias 3–9 y del desfase de la PK** sobre la dinámica tumoral.
- **Los resultados de T06,** que no tienen revisión independiente.
- **El coste de Claude Code,** que no está registrado.
- **El contenido completo del registro `prueba_delegacion.md`** (T00): solo contiene la versión de Python y «Modelo declarado: DESCONOCIDO». El proveedor y el modelo de Cline constan en los registros JSON redactados de la misma carpeta y en los de `logs_cline/`.
