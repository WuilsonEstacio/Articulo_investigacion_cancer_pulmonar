# Resultados: cáncer de pulmón, contribuciones computacionales

**Estado (10-oct-2026):** primera entrega (revisión y plan). **No se ha ejecutado ninguna simulación del plan.** Los originales de `../Data_insumo` no se modificaron.

## Estructura

| Carpeta | Contenido |
|---|---|
| `00_extraccion_texto/` | Texto por página de cada PDF (`[p. N]`); `extraer_pdf.py`; `_reporte_extraccion.json` con SHA-256, páginas y páginas con poco texto |
| `01_inventario/` | `inventario_documentos.md` y `.csv`: identificadores, tipo, población, métodos, resultados, limitaciones, disponibilidad y estado de lectura |
| `02_matriz_evidencia/` | `matriz_evidencia.md` (pregunta → fuente → método → datos → resultado → limitación → oportunidad; evaluación crítica; extracción de modelos) y `fichas/D01…D10` (lectura detallada con citas y páginas) |
| `03_registro_busquedas/` | `registro_busquedas.md` y los scripts y JSON de cada consulta (Europe PMC, Crossref); texto de la versión publicada de D02 |
| `04_plan/` | **`Primera_entrega_contribuciones_y_plan.md`** (secciones A–D); `tabla_parametros_E1_phasefield.csv`; `tabla_insumos_E2_ADRIATIC.csv`; `requirements_propuesto.txt` |
| `99_verificaciones_exploratorias_lectores/` | Scripts de comprobaciones no planificadas que hicieron los lectores. **No son resultados** |
| `05_experimentos/` | (Se creará tras la autorización) Código, configuración, registros, resultados y figuras por experimento |

## Cadena de trazabilidad prevista

Fuente (ficha y página) → dato o parámetro (tablas de `04_plan`, con columna de fuente) → configuración (`05_experimentos/E*/config/*.yaml`) → ejecución (registro JSON con hash, semilla, versión y fecha) → resultado (CSV) → figura (PNG/SVG con procedencia en el pie) → conclusión (informe, separando lo reproducido, lo observado y las hipótesis).

## Convenciones

- **Etiquetas de evidencia:** [PUB] publicada; [OBS] observada; [COMP] computacional de terceros; [HIP] hipótesis; [SUP] supuesto; [LECTOR] cálculo o juicio de la revisión.
- **Citas de página:** `[p. N]` corresponde a la numeración del PDF. En NEJM se añade la página de la revista entre llaves cuando la ficha la indica.
