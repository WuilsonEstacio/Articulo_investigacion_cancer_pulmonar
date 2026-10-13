# Prompt para reanudar (11-oct-2026, 23:00 hora local)

> Copia el bloque de abajo, desde «INICIO DEL PROMPT» hasta «FIN DEL PROMPT», en una nueva sesión de Claude Code abierta en `<PROJECT_ROOT>`.

---

## INICIO DEL PROMPT

Actúa como investigador principal y coordinador de la fase F0–F1. **No repitas trabajo ya hecho.** Las restricciones vigentes son las mismas que en `Resultados\Coordinacion\PUNTO_DE_CONTROL_20261010.md`: Data_insumo no se toca; no se recalibra; no se cambian tolerancias; el código de los autores no se redistribuye; no se contacta a nadie ni se publica nada; Cline no se sustituye sin avisarme; no hay que lanzar en paralelo ejecuciones pesadas.

### Estado al pausar (11-oct-2026, 23:00 hora local = 04:00 UTC del 12-oct)

Lee primero `Resultados\Coordinacion\ESTADO_TAREAS.md` y este archivo.

| Tarea | Estado | Dónde |
|---|---|---|
| T01: Tabla 2 (Claude) | **En ejecución** desde las 22:53 hora local (03:53 UTC del 12-oct), en el contenedor Docker `t01_tabla2` (sin `--rm`, `--cpus 8`; unas 4,5 h). Hay un proceso temporal que mantiene el equipo despierto (PowerShell independiente `C:SERSADMINISTRADORPAPERCANCER_ENVMANTENER_DESPIERTO.PS1`, PID 44884) y que se retira solo al terminar el contenedor | Log: `Resultados\Trabajo_Claude\T01_phasefield\logs\tabla2_original_20261012T035307Z.log` |
| T01: resto | Borradores de `INFORME_T01.md` y `REPRODUCIR.md` hechos; la sección de la Tabla 2 está vacía. `figures/fig_pk.png/.svg` hecha. PK: parcialmente reproducida | `Trabajo_Claude\T01_phasefield\` |
| T02 (Cline) | **Ronda 1 de corrección en ejecución** desde las 22:38 hora local (D1: fusión de escalones; D2: E2.0b con extracción). Original conservado en `logs\ronda0_original\` | Encargo: `Coordinacion\tareas\T02_correccion_ronda1_Cline.md`. Registro: `<PAPERCANCER_ENV>\logs_cline\T02_ronda2_correccion1.jsonl` |
| T04 (auditoría de T02) | Aceptada; dictamen sobre T02: requiere corrección | `Trabajo_Claude\T04_auditoria_T02\AUDITORIA_T04.md` |
| T03 (revisión de T01 por Cline) | Pendiente, tras cerrar T01 | — |

### Cambio temporal del plan de energía (autorizado por el usuario)

Para que no se suspenda el equipo, el 11-oct a las 23:31 se puso la suspensión con corriente en «nunca» (`powercfg /change standby-timeout-ac 0`; el valor original era 25 min). El proceso independiente `<PAPERCANCER_ENV>\restaurar_suspension.ps1` (PID 25960) la restaura al terminar el contenedor, o a las 08:00 del 12-oct como límite. **Al retomar, comprueba** en `<PAPERCANCER_ENV>\restaurar_suspension.log` que aparece «restaurado». Si no aparece, ejecuta `powercfg /change standby-timeout-ac 25`.

### Pasos

1. **Tabla 2.**
   - Ejecuta `docker ps -a`. Si `t01_tabla2` aparece como `Exited`, comprueba con `docker inspect -f '{{.State.ExitCode}}' t01_tabla2` y el final del log que existan `g_vt_list_p2 = [...]` y `fin_utc=`.
   - **Si está completo,** ejecuta desde `Trabajo_Claude\T01_phasefield`, con `<PAPERCANCER_ENV>\venv_claude_T01\Scripts\python.exe`:
     `python src/compare_tabla2.py logs/tabla2_original_20261012T035307Z.log data_derived/tabla2_publicada.csv data_derived/tabla2`
     Clasifica según el contrato: reproducido ≤ 10 %; parcial 10–50 %; discrepancia > 50 % o signo opuesto; H1 si ≥ 80 % reproducido. Compara también los rangos y diagnostica la escala de g (×α/100) **solo como explicación**. Completa `INFORME_T01.md` §4, haz la figura de g reproducido frente a publicado y elimina el contenedor (`docker rm t01_tabla2`).
   - **Si está incompleto o murió:** guarda `docker logs t01_tabla2` y el log, diagnostica la causa y **avísame antes de relanzar**.
   - Si quedara vivo un proceso `pwsh` con `mantener_despierto.ps1` sin contenedor activo, ciérralo.
2. **T02.**
   - **Actualización (23:24 hora local):** la sesión de Cline se cortó a las 23:14 (`external_abort`, no por límite de uso; 70 iteraciones; 9,11 USD). Su ejecución completa de la corrección **terminó con exit_code 0** (`Trabajo_Cline\T02_ADRIATIC\logs61011_230459_401462.json`, 1093 s). Faltan los pasos finales de Cline: las pruebas y la actualización de `INFORME_T02.md` y `ENTREGA_LISTA.md`. Haz primero la prueba corta de créditos (unos 0,05 USD). Si pasa, relanza a Cline **solo** para cerrar esos pasos, sin rehacer cálculos; si no pasa, avísame. Audita de todos modos los resultados.
   - Si el registro de Cline tiene `run_result` con `finishReason: completed`, audita la corrección como en T04:
     - re-ejecución aislada;
     - comprobar que D1 está corregido (empates, niveles del polígono) y que E2.0b existe;
     - verificar que las tolerancias no han cambiado;
     - comprobar el orden «original primero, corregido después».
     Después asigna el estado: aceptada o requiere corrección (queda una ronda).
   - Si terminó con «The usage limit has been reached»: compara con `logs\ronda0_original\`, no integres nada a medias y avísame.
3. **Integración** (solo con resultados respaldados): informe con 10 secciones en `Resultados\Integrado\` (reparto real del trabajo, métodos, resultados verificados, comparaciones, discrepancias, limitaciones con n = 2, licencias, reproducción, recomendación y tabla de trazabilidad), y copia a `Paper_final\`. **Infórmame antes de integrar.**
4. Actualiza `ESTADO_TAREAS.md` en cada cambio de estado.

### Cline

Comando base: `cline.cmd -P openai-codex -m gpt-6-astra --thinking high --json -t <s> -c <cwd> "<prompt>" < /dev/null`, con el binario en `<PAPERCANCER_ENV>\cline\node_modules\.bin\`. Antes de cada nuevo encargo, haz una prueba corta.

## FIN DEL PROMPT
