"""T06 · H01: índices de sensibilidad local de P2 con los parámetros farmacocinéticos de P2 conservados en las perturbaciones.

Llama a la función ORIGINAL run_local_sensitivity_analysis (repositorio montado en solo lectura, commit fa8e6229) sin
modificarla. El único cambio es el argumento `runner`: t06_runner.runner_p2_corr, que restablece MED_mas / MED_dos /
MED_tim a los valores de default_parameters_patient2() antes de cada simulación y registra las integrales Q.
Uso (dentro del contenedor, con PYTHONPATH=/repo/reduced_models:/src):  python -u /src/run_p2_h01.py
"""
import sys, os
sys.path.insert(0, '/src')
sys.path.insert(0, '/repo/reduced_models')
import local_sensitivity_analysis as lsa  # código original, sin cambios
from t06_runner import runner_p2_corr, REF_PK

if __name__ == '__main__':
    print('pk_referencia_P2', REF_PK, flush=True)
    print('Patient 2 (H01 corregido)', flush=True)
    final_time = float(os.environ.get('T06_FINAL_TIME', 1102))  # solo la prueba de humo usa otro valor
    print('final_time', final_time, flush=True)
    lsa.run_local_sensitivity_analysis(dt=1 / 24., final_time=final_time, h=1e-3, name='p2',
                                       default_params=lsa.default_parameters_patient2(), runner=runner_p2_corr)
