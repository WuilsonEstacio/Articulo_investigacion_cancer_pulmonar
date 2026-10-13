#!/usr/bin/env bash
# T01 · F1: ejecuta SIN MODIFICAR el script original local_sensitivity_analysis.py
# (repositorio wagnandr/immunotherapy-lung-cancer, commit fa8e6229d1540d33014a994f1ea309d6525597aa),
# que calcula los índices de sensibilidad local de la Tabla 2 (MBE 2023).
#
# Uso desde Windows (Git Bash), en la carpeta T01_phasefield:
#   MSYS_NO_PATHCONV=1 docker run --rm --cpus 8 \
#     -v "<repo>:/repo:ro" -v "<T01>/src:/src:ro" -v "<T01>:/out" -v "<runs>:/work" \
#     -v t01_jitcache:/root/.cache -w /work papercancer/t01-fenics2019:1 bash /src/run_tabla2_original.sh
#
# Ajuste de entorno (no de lógica): se crea el directorio 'output/' en el directorio de trabajo,
# porque solvers.py escribe archivos CSV en 'output/' aunque output_enabled=False.
set -euo pipefail
mkdir -p output
LOG=/out/logs/tabla2_original_$(date -u +%Y%m%dT%H%M%SZ).log
{
  echo "inicio_utc=$(date -u +%FT%TZ)"
  echo "commit=fa8e6229d1540d33014a994f1ea309d6525597aa"
  echo "script=/repo/reduced_models/local_sensitivity_analysis.py (sin modificar)"
  echo "sha256_script=$(sha256sum /repo/reduced_models/local_sensitivity_analysis.py | cut -d' ' -f1)"
  echo "nproc_visible=$(nproc) OMP_NUM_THREADS=${OMP_NUM_THREADS:-}"
  python -c "import dolfin, numpy, scipy, joblib; print('dolfin', dolfin.__version__, 'numpy', numpy.__version__, 'scipy', scipy.__version__, 'joblib', joblib.__version__)"
} | tee "$LOG"
cd /work
( time python -u /repo/reduced_models/local_sensitivity_analysis.py ) 2>&1 \
  | while IFS= read -r line; do printf '%s %s\n' "$(date -u +%H:%M:%S)" "$line"; done | tee -a "$LOG"
echo "fin_utc=$(date -u +%FT%TZ)" | tee -a "$LOG"
