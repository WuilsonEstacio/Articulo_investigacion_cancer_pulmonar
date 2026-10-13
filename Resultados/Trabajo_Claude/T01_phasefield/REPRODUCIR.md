# Reproducción de T01 (Windows + Git Bash + Docker Desktop)

## Requisitos

- **Código de los autores:** `<PAPERCANCER_ENV>\repos\immunotherapy-lung-cancer-fa8e6229d1540d33014a994f1ea309d6525597aa\`, commit `fa8e6229`.
  - El repositorio no tiene licencia: no se redistribuye. Descárgalo de github.com/wagnandr/immunotherapy-lung-cancer y comprueba el SHA-256 del zip: `e45a8cd30cf57efea8980a60a952816c3a725cf3627acecadca0d41b1312acce`.
- **Docker Desktop.**
- **Entorno local para los scripts sin dolfin:** `<PAPERCANCER_ENV>\venv_claude_T01`, con Python 3.10, numpy 1.26.4, matplotlib 3.10.9 y pymupdf.
- **En Git Bash:** antepón `MSYS_NO_PATHCONV=1` a los comandos `docker run` para que los montajes funcionen.

## Variables

```bash
T01="<PROJECT_ROOT>/Resultados/Trabajo_Claude/T01_phasefield"
REPO="<PAPERCANCER_ENV>/repos/immunotherapy-lung-cancer-fa8e6229d1540d33014a994f1ea309d6525597aa"
RUNS="<PAPERCANCER_ENV>/runs_t01"
PY=<PAPERCANCER_ENV>/venv_claude_T01/Scripts/python.exe
```

## 1. Imagen

```bash
docker build -t papercancer/t01-fenics2019:1 "$T01/env"
```

Compara el resultado con `env/conda_explicit_lock.txt`. Para obtener exactamente los mismos paquetes, crea el entorno desde el bloqueo explícito dentro de una imagen de miniforge3, por ejemplo con `conda create -n t01 --file /env/conda_explicit_lock.txt` y la carpeta `env` montada en `/env` (añadido tras T03-H07).

## 2. Prueba de humo (unos 40 s; escribe `logs/smoke_test.json`)

```bash
MSYS_NO_PATHCONV=1 docker run --rm -v "$REPO:/repo:ro" -v "$T01/src:/src:ro" -v "$T01:/out" -v t01_jitcache:/root/.cache \
  papercancer/t01-fenics2019:1 python /src/smoke_test.py --days 10
```

## 3. Farmacocinética (sin dolfin; se ejecuta en el entorno local)

Los módulos de PK de los autores se importan desde `reduced_models`.

```bash
cd "$T01"
$PY src/pk_check.py "$REPO/reduced_models" data_derived/pk_check.json   # criterio original + series
$PY src/pk_check_trayectoria.py data_derived/pk_check_trayectoria.json   # comparación por trayectoria
$PY src/pk_localiza_error.py                                             # localización del error
$PY src/pk_diagnostico_esquema.py "$REPO/reduced_models" data_derived/pk_dosis_efectiva_por_administracion.csv
$PY src/fig_pk.py figures/fig_pk
```

## 4. Tabla 2 (309 min con 8 núcleos el 12-oct-2026; el equipo no debe suspenderse)

- **Paralelismo efectivo (T03-H07):** el script lanza `multiprocessing.cpu_count()` workers de joblib. Dentro del contenedor vale 14 (los núcleos del host), así que `--cpus 8` limita la cuota de CPU, no el número de workers. Las 11 tareas de cada paciente se reparten esa cuota.
- **Log:** en los comandos siguientes, sustituye `<UTC>` por la marca real. La ejecución de referencia es `logs/tabla2_original_20261012T035307Z.log`.

```bash
MSYS_NO_PATHCONV=1 docker run -d --name t01_tabla2 --cpus 8 \
  -v "$REPO:/repo:ro" -v "$T01/src:/src:ro" -v "$T01:/out" -v "$RUNS:/work" \
  -v t01_jitcache:/root/.cache -w /work papercancer/t01-fenics2019:1 bash /src/run_tabla2_original.sh
```

- Sin `--rm`, como en la ejecución de referencia: si la ejecución se interrumpe, el contenedor y su registro se conservan. Al terminar, comprueba `docker inspect -f '{{.State.ExitCode}}' t01_tabla2` y elimina el contenedor con `docker rm t01_tabla2`.
- El log queda en `logs/tabla2_original_<UTC>.log` y está completo cuando contiene `g_vt_list_p2 = [...]` y `fin_utc=`.
- Comparación con la tabla publicada:

```bash
cd "$T01"
$PY src/compare_tabla2.py logs/tabla2_original_<UTC>.log data_derived/tabla2_publicada.csv data_derived/tabla2
```

- Genera `data_derived/tabla2_comparacion.csv` y `data_derived/tabla2_resumen.json`.
- Diagnóstico de escala (no es criterio) y figura:

```bash
$PY src/diag_escala_tabla2.py data_derived/tabla2_comparacion.csv data_derived/tabla2
$PY src/fig_tabla2.py data_derived/tabla2_diag_escala.csv figures/fig_tabla2
```

- Referencia de la ejecución del 12-oct-2026: 309 min; log `logs/tabla2_original_20261012T035307Z.log`.
