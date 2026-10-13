#!/usr/bin/env bash
# T06 · H01: re-simulación de P2 con los parámetros farmacocinéticos de P2 conservados en las perturbaciones,
# más un control de determinismo con el fallo original (componente 1). Ver PREESPECIFICACION_T06.md.
#
# Uso desde Windows (Git Bash), en la carpeta T06_P2_H01:
#   MSYS_NO_PATHCONV=1 docker run -d --name t06_p2_h01 --cpus 8 \
#     -v "<repo>:/repo:ro" -v "<T06>/src:/src:ro" -v "<T06>:/out" -v "<runs>:/work" \
#     -v t01_jitcache:/root/.cache -w /work papercancer/t01-fenics2019:1 bash /src/run_t06.sh
set -uo pipefail
export PYTHONPATH=/repo/reduced_models:/src
mkdir -p /out/logs /out/data_derived /work/main/output /work/control/output
STAMP=$(date -u +%Y%m%dT%H%M%SZ)
LOG=/out/logs/t06_p2_h01_${STAMP}.log
LOGC=/out/logs/t06_control_bug_${STAMP}.log
ts() { while IFS= read -r line; do printf '%s %s\n' "$(date -u +%H:%M:%S)" "$line"; done; }
{
  echo "inicio_utc=$(date -u +%FT%TZ)"
  echo "commit=fa8e6229d1540d33014a994f1ea309d6525597aa"
  for f in local_sensitivity_analysis.py run_spherical_patient_2.py parameters.py; do
    echo "sha256_${f}=$(sha256sum /repo/reduced_models/$f | cut -d' ' -f1)"; done
  for f in run_p2_h01.py t06_runner.py control_p2_bug.py run_t06.sh; do echo "sha256_src_${f}=$(sha256sum /src/$f | cut -d' ' -f1)"; done
  echo "nproc_visible=$(nproc)"
  python -c "import dolfin, numpy, scipy, joblib; print('dolfin', dolfin.__version__, 'numpy', numpy.__version__, 'scipy', scipy.__version__, 'joblib', joblib.__version__)"
} | tee "$LOG"

( cd /work/control && { time python -u /src/control_p2_bug.py 1 ; } 2>&1 | ts > "$LOGC"; echo "control_exit=${PIPESTATUS[0]}" >> "$LOGC" ) &
PID_C=$!

cd /work/main
{ time python -u /src/run_p2_h01.py ; } 2>&1 | ts | tee -a "$LOG"
MAIN_EXIT=${PIPESTATUS[0]}
wait $PID_C
echo "main_exit=${MAIN_EXIT}" | tee -a "$LOG"
tail -n 3 "$LOGC" | sed 's/^/control: /' | tee -a "$LOG"
echo "fin_utc=$(date -u +%FT%TZ)" | tee -a "$LOG"
CTRL_EXIT=$(grep -o 'control_exit=[0-9]*' "$LOGC" | cut -d= -f2)
[ "$MAIN_EXIT" = "0" ] && [ "$CTRL_EXIT" = "0" ]
