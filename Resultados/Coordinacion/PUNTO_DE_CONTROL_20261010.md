# Punto de control: 10-oct-2026, 19:45 (hora local)

Pausa solicitada por el usuario: se agotaron los créditos de Cline.

## Estado de cada tarea

| ID | Estado | Detalle |
|---|---|---|
| T00 | aceptada | Delegación a Cline CLI verificada |
| T01 (Claude) | en ejecución | El script original de la Tabla 2 sigue en el contenedor Docker `t01_tabla2` (inicio 00:33 UTC del 11-oct; duración estimada de unas 4 h). No depende de Cline. Al terminar, el log queda en `Trabajo_Claude/T01_phasefield/logs/tabla2_original_20261011T003301Z.log` y debe contener las líneas `g_*_list_p1/p2 = [...]` |
| T02 (Cline) | entregada (ronda 1 interrumpida por el límite de uso) | Archivos en `Trabajo_Cline/T02_ADRIATIC/`. Declara 18/18 cantidades reproducidas. **No aceptado ni auditado** |
| T03 (Cline) | pendiente | Requiere créditos de Cline |
| T04 (Claude) | pendiente | Siguiente paso |

## Cómo retomar

1. **Tabla 2.**
   - Comprobar si el contenedor terminó: `docker ps`. Si no aparece `t01_tabla2`, el proceso ha terminado.
   - Ver el final del log.
   - Ejecutar la comparación:
     `python src/compare_tabla2.py logs/tabla2_original_20261011T003301Z.log data_derived/tabla2_publicada.csv data_derived/tabla2`
     usando `PaperCancer_env/venv_claude_T01`, desde `Trabajo_Claude/T01_phasefield`.
   - Si el log no contiene las listas g (por ejemplo, porque se apagó el equipo), relanzar con el comando de `src/run_tabla2_original.sh` (ver la sección 3 del resumen de la sesión). La caché JIT de FEniCS persiste en el volumen `t01_jitcache`.
2. **T04: auditoría de T02.** Leer `INFORME_T02.md`, `CRITERIOS_PREESPECIFICADOS.md`, `DECISIONES_METODO.md` y `logs/INCIDENCIAS.md`. Re-ejecutar `REPRODUCIR.md` con `PaperCancer_env/venv_cline_T02`. Comprobar:
   - que las tolerancias no cambiaron a posteriori;
   - que no haya fuga: que los conteos de eventos y las medianas publicadas no se usen como objetivo de ajuste sin declararlo;
   - que no haya extrapolación ni RMST;
   - las coordenadas extraídas frente a las páginas 6 y 8 del PDF.
3. **Cline.** Cuando haya créditos, verificar de nuevo el proveedor y el modelo (gpt-6-astra) con una prueba corta antes de asignar correcciones de T02 (máximo 2 rondas) o T03. No sustituir a Cline por otro agente sin indicarlo.
4. **Integración.** Escribir el informe final en `Resultados/Integrado/`, con 10 secciones y la tabla de trazabilidad. Scibilia 2024 sigue sin revisar, por lo que no se puede afirmar novedad.

## Recursos activos al pausar
- Docker Desktop: en marcha, con el contenedor `t01_tabla2` (8 CPU). Para detenerlo, si se necesita el equipo: `docker stop t01_tabla2`. En ese caso habrá que relanzar la Tabla 2.
- Cline: no queda ningún proceso activo; se terminó el demonio `cline-hub` (PID 12804).
- `Data_insumo`: sin cambios.
