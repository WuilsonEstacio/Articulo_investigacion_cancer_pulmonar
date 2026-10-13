# T05: auditoría de la ronda 1 de corrección de T02 (ADRIATIC, Cline)

| Campo | Valor |
|---|---|
| Auditor | Claude Code (coordinador) |
| Fecha | 12-oct-2026 (hora local) |
| Objeto | `Trabajo_Cline/T02_ADRIATIC/`, ronda 1 de corrección (encargo `Coordinacion/tareas/T02_correccion_ronda1_Cline.md`) y su cierre (`T02_correccion_ronda1_cierre_Cline.md`) |
| Base | Auditoría T04 (`Trabajo_Claude/T04_auditoria_T02/AUDITORIA_T04.md`): defectos D1 y D2 |
| **Dictamen** | **Aceptada, con observaciones documentadas (§3).** No se necesita la segunda ronda |

## 1. Contexto de ejecución

- La sesión de Cline de la ronda 1 se interrumpió el 11-oct a las 23:14 (`external_abort`; 70 iteraciones; 9,11 USD). Antes de la interrupción ya había lanzado la ejecución completa `logs/20261011_230459_401462.json`, que terminó con exit_code 0 (1093 s).
- El 12-oct, tras una prueba de créditos (0,048 USD), se relanzó a Cline solo para el cierre: pruebas, incidencias y coherencia documental, sin recálculos. Terminó con `finishReason: completed` (18 iteraciones; 1,66 USD; registro `logs_cline/T02_ronda2_cierre.jsonl`).
- Resultado del cierre: 23 pruebas, de las que 22 pasan y 1 falla (O-T05-1). Cline la registró sin corregirla, como pedía el encargo.

## 2. Verificaciones

| # | Verificación | Método | Resultado |
|---|---|---|---|
| V1 | Reproducibilidad | Copia aislada en el scratchpad (`src`, `config`, `tests`, documentos y archivo de la ronda 0) y `run_logged.py pipeline.py --stage all` con `venv_cline_T02` e hilos = 1. SHA-256 de `data_derived/`, `figures/` y `requirements_T02.txt` frente a la entrega (`src/compara_rerun.py`) | exit 0 en 225 s. **4660 de 4661 archivos idénticos**, incluidas las 200 carpetas de E2.0b con sus PDF y las figuras. Solo difiere `PROCEDENCIA.md`, por las rutas absolutas, como en T04 (`data_derived/rerun_vs_entrega.json`, `logs/rerun_pipeline_all.json`) |
| V2 | Pruebas | `unittest discover` sobre la copia re-ejecutada | 23 pruebas: 22 pasan y 1 falla, la misma que registró Cline (`logs/rerun_unittest.txt`). Ver O-T05-1 |
| V3 | Tolerancias y criterios | SHA-256 de `config.yaml` y `CRITERIOS_PREESPECIFICADOS.md` frente a `logs/ronda0_documentos`; `DECISIONES_METODO.md` frente a su versión de la ronda 0 | `config.yaml` y `CRITERIOS` **idénticos**. `DECISIONES` conserva íntegro el texto original como prefijo y añade dos secciones fechadas: «Ronda 1: D1 y D2 (antes de evaluar la corrección)» y «23:04: precisión finita en E2.0b». `guyot.py`, `validate.py` y `simulate.py` no han cambiado |
| V4 | Sin ajuste a posteriori | Hash de `extract.py` en las 20 instantáneas de `run_logged`; comparación de los derivados clínicos de la primera ejecución corregida (`clinical_20261011_224630_431867`, `extract.py` `432ff154…`) con los finales (`4e1be6f0…`) | `extract.py` se modificó a las 23:04 tras el fallo de precisión de E2.0b. Los **39 archivos clínicos son idénticos byte a byte** antes y después (salvo `PROCEDENCIA.md`), de modo que el cambio no alteró ningún resultado clínico |
| V5 | D1 corregido | `src/merged_steps.py` (el mismo de T04) sobre los derivados corregidos: niveles horizontales del polígono dentro de cada salto | **0 saltos con niveles intermedios** (en T04 había 16). Empates y tiempos distintos idénticos a `round1_ties.csv`: empate máximo SG-D 5→3, SG-P 6→2, SLP-D 31→6 y SLP-P 34→9. La prueba de Cline `test_polygon_levels_plateaus_and_maximum_tie_per_curve` pasa (mesetas = niveles del polígono en las 4 curvas clínicas) |
| V6 | KM y Cox independientes | `src/km_cox_indep.py` (propio, sin lifelines) sobre los pseudo-IPD corregidos | Coinciden con Cline. HR SG: Efron 0,73030 y Breslow 0,73045. HR SLP: Efron 0,77147 y Breslow 0,77230. Medianas: SG-D 55,94; SG-P 33,39; SLP-D 16,54; SLP-P 9,18. La diferencia Efron–Breslow en la SLP pasa de 0,0049 a 0,0008 (`data_derived/km_cox_indep.json`) |
| V7 | D2: E2.0b existe y usa la extracción | Lectura de `simulate_digitized.py` y recuento de artefactos | `from extract import extract_pdf` y `reconstruct()` sobre los puntos extraídos. **100 réplicas** con las mismas semillas que E2.0a (20261010 + r) y verdad idéntica byte a byte. 200 `km.pdf`. 1800/1800 comparaciones dentro de tolerancia y error de riesgo 0. E2.0a se conserva byte a byte (la prueba pasa) |
| V8 | Orden «original primero, después corregido» | `INFORME_T02.md`, `round1_h1.csv`, `round1_risks.csv`, `round1_hr.csv` y `round1_ties.csv` | El informe presenta «Resultado original» (l. 281) antes de «Resultado corregido» (l. 414), y E2.0a antes de E2.0b. **H1: 18/18 en ambas versiones.** Riesgo: original 85 reproducidos y 3 parciales; corregido 88/88. Eventos de SLP-P: 169 → 170 (publicado 169; dentro del ±3 %). Mediana de SLP-P: 9,09 → 9,18 (publicada 9,2) |
| V9 | Cierre de Cline | Diferencias entre `src/`, `tests/` y `config/` y la instantánea de la ejecución final | No hay cambios científicos en el cierre. Sí hay dos diferencias de **solo texto** entre la instantánea del inicio de la ejecución final (23:04:59) y el código entregado: el título de una figura en `reporting.py` (23:08) y un párrafo del informe en `round1.py` (23:05), editados por Cline mientras la ejecución seguía en curso. V1 demuestra que el código entregado produce exactamente las salidas entregadas (O-T05-2) |

## 3. Observaciones (sin corrección obligatoria)

### O-T05-1: la prueba `test_e20b_all_replicates_same_truth_and_diagnostics` falla por un límite de resolución, no por un defecto

- En 7 de las 400 curvas de E2.0b, la extracción tiene una meseta menos que el KM verdadero. Son las réplicas 13/SG-P, 28/SG-D, 42/SG-P, 42/SLP-P, 82/SLP-D, 93/SLP-D y 95/SG-P.
- `src/meseta_perdida_cual.py` identifica el nivel ausente en cada caso (`data_derived/e20b_meseta_perdida_cual.csv`):
  - **5 casos:** mesetas de **2·10⁻⁶ a 1,3·10⁻⁵ pt** de ancho, es decir, dos eventos separados entre 5·10⁻⁷ y 3·10⁻⁶ meses. Son más estrechas que la precisión de las coordenadas del PDF y que el margen geométrico declarado de 0,002 pt.
  - **2 casos (réplicas 13 y 95):** el nivel terminal S = 0, de **ancho nulo** porque el último sujeto tiene un evento en el último tiempo. Ese nivel no se puede dibujar.
- **Efecto:** ninguno medible. El error de riesgo es 0, el error de extracción máximo ronda 3·10⁻⁷ y las 1800 comparaciones de esas réplicas están dentro de tolerancia. Las 4 curvas clínicas de ADRIATIC no pierden ningún nivel (V5).
- **Valoración:** la prueba exige igualdad de recuento incluso para niveles que no se pueden representar. La frase de `DECISIONES_METODO.md` (23:04), «sin eliminar el nivel», es inexacta para mesetas de ancho inferior a la precisión del PDF o nulo.
- No se pide modificar la prueba: cambiarla después de ver el fallo sería mover el criterio. El fallo se conserva y se declara como limitación en el informe integrado.

### O-T05-2: procedencia de la ejecución final

- La instantánea `logs/20261011_230459_401462_source` no coincide exactamente con el código entregado: hay dos líneas de texto distintas (V9).
- Queda subsanado por V1: la re-ejecución con el código entregado reproduce byte a byte las 4660 salidas.
- Para ejecuciones futuras: no editar `src/` mientras haya una ejecución en curso.

### O-T05-3: alcance de E2.0b

- Los PDF sintéticos son vectoriales e ideales, sin ruido ráster ni todos los salientes de unión del editor del artículo. Cline lo declara.
- Por eso E2.0b valida la cadena de extracción y reconstrucción con geometría de la Fig. 1A, pero no la robustez frente a figuras ráster.

### O-T05-4: empates residuales en la SLP

- Quedan empates de 5–9 eventos en t ≈ 1,6–1,9 y en t = 3,668 meses, en ambos brazos.
- `merged_steps.py` no encuentra niveles intermedios del polígono en esos saltos: corresponden a **un único escalón vertical** en la figura publicada. Lo que pase dentro de ese escalón no se puede resolver a partir del PDF.
- No se interpreta clínicamente.

### Recordatorio de T04 (vigente)

- El total de eventos y los números en riesgo son **entradas** del algoritmo de Guyot. Su reproducción no constituye una validación independiente.
- Las cantidades H1 (medianas, tasas hito y HR) se heredan de la curva extraída.

## 4. Clasificación para la integración

- **T02, ronda 1: aceptada.**
- H1: 18/18 «reproducido» (verificado de forma independiente, V6).
- D1 y D2: corregidos y verificados (V5, V7).
- Los pseudo-IPD corregidos (`data_derived/pseudo_ipd_*.csv`) pueden usarse como insumo, con la etiqueta «reconstrucción Guyot de figura vectorial; tiempos individuales no identificables».
- Las limitaciones O-T05-1 a O-T05-4 y las de T04 (O1–O3) se trasladan al informe integrado.

## 5. Archivos de esta auditoría

- `src/merged_steps.py` y `src/km_cox_indep.py`: copiados de T04 sin cambios.
- `src/compara_rerun.py`, `src/mesetas_perdidas_e20b.py` y `src/meseta_perdida_cual.py`: nuevos. Entorno `venv_claude_T01`, ejecución con `python -I`.
- `data_derived/`: `saltos_fusionados.csv` (vacío: 0 saltos), `km_cox_indep.json`, `rerun_vs_entrega.json`, `e20b_mesetas_perdidas.csv` y `e20b_meseta_perdida_cual.csv`.
- `logs/`: `rerun_pipeline_all.json`, `rerun_all_stdout.txt`, `rerun_unittest.txt`, `merged_steps_stdout.txt` y `km_cox_stdout.txt`.
- La copia aislada de la re-ejecución está en el scratchpad de la sesión (temporal; no forma parte de la entrega).
