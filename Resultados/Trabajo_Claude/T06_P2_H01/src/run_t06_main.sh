#!/usr/bin/env bash
# T06 · intento 2: solo la corrida principal (P2 con H01 corregido). El control de determinismo ya terminó con éxito en el
# intento 1 (logs/t06_control_bug_20261012T231050Z.log; data_derived/control_bug_comp1.json).
# Cambios de ENTORNO respecto del intento 1 (sin cambios de lógica): contenedor con --shm-size=1g, sin el control concurrente
# y con reintento automático (máx. T06_MAX_INTENTOS) si algún worker de loky muere al importar dolfin (MPI.init).
# Uso: MSYS_NO_PATHCONV=1 docker run -d --name t06_p2_h01b --cpus 8 --shm-size=1g -v "<repo>:/repo:ro" -v "<T06>/src:/src:ro" \
#        -v "<T06>:/out" -v "<runs>:/work" -v t01_jitcache:/root/.cache -w /work papercancer/t01-fenics2019:1 bash /src/run_t06_main.sh
set -uo pipefail
export PYTHONPATH=/repo/reduced_models:/src
MAX=${T06_MAX_INTENTOS:-3}
mkdir -p /out/logs /out/data_derived /work/main/output
ts() { while IFS= read -r line; do printf '%s %s\n' "$(date -u +%H:%M:%S)" "$line"; done; }
for k in $(seq 1 "$MAX"); do
  STAMP=$(date -u +%Y%m%dT%H%M%SZ)
  LOG=/out/logs/t06_p2_h01_${STAMP}.log
  {
    echo "inicio_utc=$(date -u +%FT%TZ)"; echo "intento=${k}/${MAX} (contenedor: intento 2 de T06)"
    echo "commit=fa8e6229d1540d33014a994f1ea309d6525597aa"
    for f in local_sensitivity_analysis.py run_spherical_patient_2.py parameters.py; do
      echo "sha256_${f}=$(sha256sum /repo/reduced_models/$f | cut -d' ' -f1)"; done
    for f in run_p2_h01.py t06_runner.py run_t06_main.sh; do echo "sha256_src_${f}=$(sha256sum /src/$f | cut -d' ' -f1)"; done
    echo "shm=$(df -m /dev/shm | tail -1 | awk '{print $2}')MB"
    python -c "import dolfin, numpy, scipy, joblib; print('dolfin', dolfin.__version__, 'numpy', numpy.__version__, 'scipy', scipy.__version__, 'joblib', joblib.__version__)"
  } | tee "$LOG"
  export T06_QDIR=/out/data_derived/q_corr
  rm -rf /out/data_derived/q_corr
  cd /work/main
  { time python -u /src/run_p2_h01.py ; } 2>&1 | ts | tee -a "$LOG"
  EXIT=${PIPESTATUS[0]}
  echo "main_exit=${EXIT}" | tee -a "$LOG"
  echo "fin_utc=$(date -u +%FT%TZ)" | tee -a "$LOG"
  if [ "$EXIT" = "0" ]; then exit 0; fi
  if grep -q 'TerminatedWorkerError' "$LOG"; then
    mkdir -p "/out/logs/intento2_reintento${k}_fallido"
    mv "$LOG" "/out/logs/intento2_reintento${k}_fallido/"
    [ -d /out/data_derived/q_corr ] && mv /out/data_derived/q_corr "/out/logs/intento2_reintento${k}_fallido/q_corr"
    echo "reintento ${k} fallido por TerminatedWorkerError; se reintenta" >> /out/logs/t06_reintentos.txt
  else
    exit "$EXIT"
  fi
done
exit 1
