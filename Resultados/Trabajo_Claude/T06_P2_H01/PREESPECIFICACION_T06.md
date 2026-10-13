# T06: efecto de H01 en los índices de sensibilidad de P2. Preespecificación

| Campo | Valor |
|---|---|
| Responsable | Claude Code |
| Fecha | 12-oct-2026, **escrito antes de lanzar la simulación** |
| Autorización | Usuario, 12-oct-2026: «Re-simulación en Docker para corregir P2 (H01)» |
| Origen | Hallazgo H01 de T03 (`Trabajo_Cline/T03_revision_T01/REVISION_T03.md`), verificado por el coordinador |

## 1. Qué se corrige

- **Fallo en el script original.** En `local_sensitivity_analysis.py` (commit `fa8e6229`), la simulación de referencia de P2 usa MED_mas = 143600 g/mol, MED_dos = 0,20 g y MED_tim = 22 d (`default_parameters_patient2`, l. 23–32). Las simulaciones perturbadas ± se reconstruyen con `vector_to_parameters` (l. 35–48), que solo traslada los 11 parámetros del vector. Por eso usan los valores por defecto de `parameters.py`: 146000 g/mol; 0,24 g; 26,7 d.
- **Corrección (variante declarada, no reproducción):**
  - se llama a la función original `run_local_sensitivity_analysis` **sin modificarla**, con los mismos dt = 1/24 d, T = 1102 d y h = 10⁻³ y el mismo paralelismo joblib;
  - el único cambio es el argumento `runner`: un envoltorio propio (`src/run_p2_h01.py`) que, antes de cada simulación, restablece los tres campos farmacocinéticos a los valores de la referencia de P2 y después llama al `run_patient_2_parametrized` original;
  - el envoltorio registra los campos antes y después de la corrección, el vector de parámetros y las integrales Q de cada simulación (`data_derived/q_corr/`).
- **No se modifica ni se copia el código de los autores** (repositorio sin licencia; montado en solo lectura).
- **P1 no se repite.** `default_parameters_patient1` solo fija campos del vector, más MED_dos = 0,240, que coincide con el valor por defecto, así que H01 no afecta a P1.

## 2. Control de determinismo (fijado antes de ejecutar)

- `src/control_p2_bug.py` recalcula, **con el fallo original** (`vector_to_parameters` sin corregir), el componente 1 de P2 (λ_τ,eff): referencia, + y −.
- Aplica la misma fórmula del código: g = (Q⁺ − Q⁻)/(2·h·α·Q₀).
- Los 4 valores (g_φT, g_φP, g_φN, g_Vvis) se comparan con los del log original `T01_phasefield/logs/tabla2_original_20261012T035307Z.log`.
- **Criterio:** diferencia relativa ≤ 10⁻⁸ en los 4 → ejecución determinista, y los cambios de T06 se atribuyen a H01. En caso contrario, se informa la diferencia como nivel de ruido y los cambios de H01 se interpretan frente a ese nivel.

## 3. Métricas y clasificación del efecto de H01 (fijadas antes de ejecutar)

Para los 44 índices de P2 (11 parámetros × 4 métricas):
1. **Cambio relativo:** Δ_rel = (g_corr − g_orig)/|g_orig|, con g_orig del log de T01. Es idéntico en escala directa y tras ×α/100, porque α no cambia.
2. Cambios de signo y cambios de rango (orden por |g| en cada métrica).
3. Comparación de g_corr·α/100 con la Tabla 2 publicada: número de valores con error ≤ 10 %, número que coincide al redondear a 3 cifras significativas, y error máximo.

**Clasificación del efecto de H01 en P2:**

| Clase | Condición |
|---|---|
| **Despreciable** | max \|Δ_rel\| ≤ 0,5 % (por debajo de la resolución de 3 cifras de la Tabla 2), sin cambios de signo ni de rango |
| **Menor** | max \|Δ_rel\| entre 0,5 % y 10 %, sin cambios de signo ni de rango |
| **Relevante** | max \|Δ_rel\| > 10 %, o algún cambio de signo o de rango |

## 4. Lo que no cambia

- La clasificación de T01 (discrepancia, 0/88 con la salida directa del script original) **se mantiene**: se refiere al script publicado.
- T06 es una **variante corregida**. Sus 88 valores (P1 original y P2 corregido) se presentan aparte y rotulados como tales.
- No se recalibra ningún parámetro ni se cambian dt, T ni h.

## 5. Ejecución

- Contenedor `t06_p2_h01`: imagen `papercancer/t01-fenics2019:1`, `--cpus 8`, sin `--rm`.
- Lanzador `src/run_t06.sh`: ejecución principal y control en paralelo, cada uno en su propio directorio de trabajo.
- Logs en `logs/`. Muestreo de memoria y CPU del contenedor cada 60 s en `logs/docker_stats.csv`.
- **Éxito:** exit code 0 en ambos procesos, sin OOM, con `g_*_list_p2` y `fin_utc` en el log.

## 6. Prueba de humo previa (horizonte de 5 d; no es un resultado)

1. **Primer intento: falló.** El envoltorio definido en `__main__` se serializaba por valor y los workers de loky caían con SIGSEGV al importar dolfin.
2. **Diagnóstico:** el runner original, lanzado por la misma vía, funciona con y sin PYTHONPATH.
3. **Arreglo:** el envoltorio pasa al módulo importable `src/t06_runner.py` y se serializa por referencia, como el original. Con esto la prueba pasa: exit 0 y 23 simulaciones. La simulación de referencia ya traía los parámetros farmacocinéticos de P2; las 22 perturbadas traían 146000 / 0,24 / 26,7 y se corrigieron.
4. **Coherencia del control:** a 5 d, el g_φT del componente 1 calculado con `control_p2_bug.py` (−0,018382303257740772) es idéntico, en todas las cifras impresas, al que da la función original por la misma vía.

No se ha cambiado ningún criterio de los §2–§3.

## 7. Intento 1 (12-oct, 23:10–23:47 UTC): la corrida principal falló; el control terminó bien

- **Corrida principal:**
  - la simulación de referencia de P2 terminó (23:47:12);
  - al arrancar los 11 workers de loky, varios cayeron con SIGSEGV/SIGBUS en `dolfin/parameter/__init__.py:69` (`cpp.MPI.init()`, MPICH 5.0.1): `TerminatedWorkerError`, exit 1, sin OOM y con un pico de memoria de 1,28 GiB de 7,48;
  - archivada en `logs/intento1_fallido_SIGBUS/`.
- **Control de determinismo:** exit 0 (`data_derived/control_bug_comp1.json`). Se conserva y no se repite.
- **Causa probable, no demostrada:** fallo intermitente de la inicialización de MPI cuando arrancan muchos procesos a la vez en un contenedor con `/dev/shm` = 64 MB. En este intento convivían unos 16 procesos con MPI (principal + control); las corridas que funcionaron tenían como mucho 12. Datos que la debilitan: una prueba de humo con 1 GB de `/dev/shm` y 12 procesos midió un pico de solo 13 MB, y la prueba de humo n.º 1 falló sin el control concurrente.
- **Intento 2** (`src/run_t06_main.sh`, contenedor `t06_p2_h01b`). Solo cambia el entorno:
  - `--shm-size=1g`;
  - sin el control concurrente;
  - reintento automático (máximo 3) solo ante `TerminatedWorkerError`, archivando cada intento fallido.
- Ni la lógica, ni los parámetros, ni los criterios cambian.
