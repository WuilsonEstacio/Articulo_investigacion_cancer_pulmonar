# INFORME T06: efecto de H01 en los índices de sensibilidad de P2

| Campo | Valor |
|---|---|
| Responsable | Claude Code |
| Fecha | 13-oct-2026 (ejecución del 12 al 13-oct, UTC) |
| Preespecificación | `PREESPECIFICACION_T06.md`, escrita antes de lanzar; §6–§7 añadidas después, con las incidencias de ejecución. Ningún criterio ha cambiado |
| **Resultado** | **Efecto de H01 en P2: relevante** según el criterio preespecificado |

## 1. Ejecución

| Elemento | Detalle |
|---|---|
| Intento 1 (contenedor `t06_p2_h01`, 23:10–23:47 UTC) | **Corrida principal fallida.** Tras la simulación de referencia, varios workers de loky cayeron en `MPI.init()` al importar dolfin (SIGSEGV/SIGBUS). Exit 1, sin OOM. Archivado en `logs/intento1_fallido_SIGBUS/` |
| Control de determinismo (intento 1, concurrente) | **Exit 0.** `data_derived/control_bug_comp1.json` y `logs/t06_control_bug_20261012T231050Z.log` |
| Intento 2 (contenedor `t06_p2_h01b`, 23:52–02:55 UTC) | **Exit 0, sin OOM**, 183,6 min, sin necesidad de reintento. Cambios solo de entorno: `--shm-size=1g`, sin procesos concurrentes y reintento automático disponible. Log: `logs/t06_p2_h01_20261012T235219Z.log` |
| Recursos (intento 2) | Pico de memoria 1,36 GiB de 7,48 (mediana 1,31); CPU media 7,2 núcleos (máx. 9,6); 177 muestras (`logs/docker_stats.csv`) |
| Registros Q | 23 simulaciones. Las 22 perturbadas llegaron con 146000 / 0,24 / 26,7 y se corrigieron a 143600 / 0,20 / 22; la de referencia ya traía los valores de P2 (`data_derived/q_corr/`) |

## 2. Resultados (`src/analiza_t06.py` → `data_derived/t06_resumen.json`, `t06_p2_indices.csv`, `t06_88_corregido.csv`; `figures/fig_h01.png`)

### 2.1 Determinismo

El componente 1 de P2 (λ_τ,eff), recalculado **con el fallo original**, da g_φT, g_φP, g_φN y g_Vvis **idénticos** al log de T01 (diferencia relativa de 0,0). Se cumple el criterio (≤ 10⁻⁸): la ejecución es determinista y los cambios se atribuyen a H01.

**Magnitud del fallo (dato del control):** con los parámetros farmacocinéticos de P1, Q̄(φT) de las simulaciones perturbadas es un ~15 % menor que en la referencia (3,14·10⁻³ frente a 3,71·10⁻³).

### 2.2 Efecto de H01 en los 44 índices de P2

| Métrica | Mediana \|Δ\| | Máx. \|Δ\| | Cambios de rango |
|---|---|---|---|
| φT | 16,0 % | 24,1 % | 0 |
| φP | 16,0 % | 27,1 % | 0 |
| φN | 3,4 % | 7,6 % | 0 |
| V_vis | 38,9 % | 45,2 % | 7 de 11 |
| **Total (44)** | **12,6 %** | **45,2 %** | **7** |

- **Sin cambios de signo.** Los mayores cambios están en V_vis: α_H −45,2 %, λ_PN −43,1 %, σ_PN −40,0 %, α_P −39,0 % y κ_i +38,9 %.
- **Rangos en V_vis:** α_P sigue siendo el 1.º. Cambian: ε_P (4→2), α_H (2→3), σ_PN (3→4), κ_i (5→6), λ_τ,eff (6→5), λ_PN (10→11) y λ_P,pro (11→10).
- **Clase preespecificada: relevante** (máx. > 10 % y cambios de rango).

### 2.3 Comparación con la Tabla 2 publicada (tras ×α/100)

| Conjunto | ≤ 10 % | Igual a 3 cifras | Error mediano | Error máx. |
|---|---|---|---|---|
| P2 original (con H01) | 44/44 | 44/44 | 0,07 % | 0,31 % |
| P2 corregido | 19/44 | 1/44 | 12,7 % | 45,2 % |
| 88 (P1 original + P2 corregido) | 63/88 | 45/88 | 0,42 % | 45,2 % |

Que la tabla publicada coincida con la configuración defectuosa y no con la corregida refuerza que **los valores publicados de P2 contienen H01**. Es una inferencia por coincidencia numérica, no está documentada.

## 3. Interpretación y límites

- Los índices publicados de P2, sobre todo los de V_vis, que es la magnitud observable en TC, están sesgados por H01 hasta un 45 %, y el orden de sus parámetros secundarios no es fiable.
- No cambia ningún signo, y el parámetro más influyente de cada métrica se mantiene.
- **Mecanismo plausible, no aislado:** mayor exposición al fármaco, porque P1 tiene más dosis y mayor semivida, y respuesta no lineal de V_vis por el umbral de 0,3.
- La corrección es una **variante declarada**. La clasificación de T01 (discrepancia, 0/88 con el script tal cual) no cambia.
- Sigue habiendo n = 2 pacientes: esto informa sobre la integridad del análisis publicado, no sobre la biología.

## 4. Reproducción

```bash
# desde T06_P2_H01, en Git Bash
MSYS_NO_PATHCONV=1 docker run -d --name t06_p2_h01b --cpus 8 --shm-size=1g -v "$REPO:/repo:ro" -v "$T06/src:/src:ro" \
  -v "$T06:/out" -v "$RUNS:/work" -v t01_jitcache:/root/.cache -w /work papercancer/t01-fenics2019:1 bash /src/run_t06_main.sh
# control de determinismo: src/run_t06.sh (ejecuta el control junto a la corrida principal; usar --shm-size=1g)
python -I src/analiza_t06.py ../T01_phasefield/logs/tabla2_original_20261012T035307Z.log logs/t06_p2_h01_<UTC>.log ../T01_phasefield/data_derived/tabla2_publicada.csv
python -I src/tablas_paper.py <paper.md> ../T01_phasefield/data_derived/tabla2_comparacion.csv data_derived/t06_88_corregido.csv
```

El código de los autores (commit `fa8e6229`) se monta en solo lectura y no se modifica ni se redistribuye.
