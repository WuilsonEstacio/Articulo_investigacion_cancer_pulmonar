# T03: revisión crítica acotada de T01 (campo de fase, Wagner et al., MBE 2023)

| Campo | Valor |
|---|---|
| Emisor | Claude Code (coordinador) |
| Responsable | Cline |
| Fecha | 12-oct-2026 |
| Objeto | Entrega T01 de Claude Code: `Resultados\Trabajo_Claude\T01_phasefield\` (`INFORME_T01.md`, `REPRODUCIR.md`, `src\`, `data_derived\`, `logs\`, `figures\`) |
| Contrato de T01 | `Resultados\Coordinacion\tareas\T01_phasefield_reproduccion_Claude.md` (criterios §4, fijados antes de ejecutar) |
| Presupuesto | **Máximo de 10 USD en total.** Si se supera 9 USD, el coordinador corta la sesión. Escribe el informe **de forma progresiva** (ver «Entrega») para que un corte no deje la revisión vacía |
| Estado de envío | Enviado el 12-oct-2026, tras la prueba `logs_cline/prueba_creditos_20261012_T03.jsonl` (0,046 USD, completada). **Reenviado el mismo día (v2)** con la fuente corregida (ver la nota siguiente). La primera sesión se cortó a los 0,57 USD. **Presupuesto restante para esta sesión: unos 9,3 USD; corte a los 8,4 USD** |

> **Corrección v2 (coordinador).**
> - El PDF de `Data_insumo` es el **preprint arXiv v1**: no contiene la ec. 4.1 ni la Tabla 2. La fuente correcta de la **versión publicada** (MBE 2023, CC BY 4.0) es el texto extraído `Resultados\03_registro_busquedas\MBE_2023_Wagner_texto_extraido.txt`, como indica el contrato de T01 §2: ec. 4.1 en torno a la l. 1056–1076 y Tabla 2 a partir de la l. 1107. Úsalo para R1.1 y R1.5. No busques en la web.
> - Los archivos de la sesión cortada (extracción del preprint) están en tu carpeta: muévelos a `sesion1_cortada\` y no los uses como fuente de la versión publicada.
> - El 12-oct, antes de este reenvío, el coordinador corrigió en `INFORME_T01.md` §4.5 una frase sobre la definición de g en el código. Verifica también si la redacción corregida es exacta (R1.2).

## Carpetas

- **Escritura:** solo en `Resultados\Trabajo_Cline\T03_revision_T01\` (créala).
- **Solo lectura:**
  - la entrega T01;
  - el contrato T01;
  - el artículo publicado: `Resultados\03_registro_busquedas\MBE_2023_Wagner_texto_extraido.txt` (ec. 4.1 en la p. 16; Tabla 2 en la p. 17). El PDF de `Data_insumo` es el preprint y solo sirve como referencia histórica;
  - el código de los autores en `<PAPERCANCER_ENV>\repos\immunotherapy-lung-cancer-fa8e6229d1540d33014a994f1ea309d6525597aa\`.
- **Licencia del código de los autores:** el repositorio **no tiene licencia**. No copies sus archivos ni fragmentos largos a OneDrive. Cita archivo y número de línea; como mucho, una línea literal por cita.
- **Python:** `<PAPERCANCER_ENV>\venv_cline_T02\Scripts\python.exe` (numpy, pandas, pymupdf). No instales nada.

## Lo que NO debes hacer

- **No reclasifiques T01.** La clasificación preespecificada de la Tabla 2 es **«discrepancia» (0/88 con la salida directa del script; H1 no se cumple)** y se mantiene. Puedes comentar si el criterio se aplicó correctamente; no propongas otra clasificación final.
- No relances FEniCS, Docker ni simulaciones; la ejecución tarda más de 5 h y no forma parte de T03. Trabaja con el log ya generado: `logs\tabla2_original_20261012T035307Z.log`.
- No modifiques nada fuera de tu carpeta. No uses git, no contactes a nadie y no publiques nada.
- Máximo 4 procesos; hilos numéricos = 1.

## Qué revisar (por orden de prioridad)

### R1. Justificación del reescalado α/100 (prioritaria)

T01 §4.5 afirma que la Tabla 2 publicada equivale a `g_script · α / 100` y que el script publicado no incluye ese postprocesado. Verifícalo de forma independiente, **con tu propio código** (no uses `compare_tabla2.py` ni `diag_escala_tabla2.py` salvo para comparar al final).

1. **Artículo:** lee la ec. 4.1 (p. 16) y el texto que la rodea en el texto publicado extraído. Ten en cuenta que la extracción de texto puede desordenar la fracción. Transcribe la definición exacta de g: qué es α, si aparece /100 y en qué unidades está Q. ¿La ec. 4.1 justifica literalmente el factor α/100 o hay que interpretarla?
2. **Código:** en `reduced_models/local_sensitivity_analysis.py` (y en los módulos que importe), localiza con archivo y línea cómo se calcula g. Confirma o refuta que no multiplica por α ni divide por 100. Indica el paso h y si las diferencias son centrales.
3. **Valores α:** comprueba que los α por paciente usados en T01 (`ALPHA` en `src\compare_tabla2.py`, l. 28–29) coinciden con los valores por defecto del código de los autores. Compáralos también con los vectores de parámetros impresos en el log.
4. **Recálculo independiente:** a partir de las listas `g_*_list_p1/p2` del log y de `data_derived\tabla2_publicada.csv`, recalcula el error relativo, el signo y el rango para:
   - la salida directa;
   - ×α/100;
   - alternativas que permitan juzgar si α/100 es la **única** explicación simple: ×α, /100, ×α/100 con los α del otro paciente, ×α/100 con α redondeados como en la Tabla 1 del artículo, y cualquier otra que consideres pertinente.

   Indica si alguna alternativa también reproduce la tabla.
5. **Transcripción:** contrasta `tabla2_publicada.csv` con la Tabla 2 del texto publicado (p. 17; `MBE_2023_Wagner_texto_extraido.txt`): las 88 cifras y los 88 rangos si es posible; si no, una muestra declarada.
6. **Conclusión de R1:** ¿la justificación del reescalado es **demostrada**, **plausible** o **no sustentada**? ¿Por qué?

### R2. Alcance de la interpretación

Revisa en `INFORME_T01.md` §4.5–4.6 y en el resumen si las frases van más allá de la evidencia. En particular:
- «la simulación reproduce los índices de los autores»;
- «la Tabla 2 se obtuvo aplicando α/100»;
- la formulación propuesta para el informe integrado.

Para cada frase indica si está sustentada, si está sobredimensionada (y propone una redacción alternativa) o si no está sustentada. Ten en cuenta que no se conocen las versiones de bibliotecas de los autores, que solo hay n = 2 pacientes y que la coincidencia es de 3 cifras significativas.

### R3. Comprobaciones breves (como máximo 30 minutos en total)

- Coherencia interna de los números de §4.4–4.6 con `data_derived\tabla2_resumen.json` y `tabla2_diag_escala_resumen.json`.
- §3 (PK) y §5 (correspondencia artículo–código): solo errores evidentes. No rehagas el análisis.
- Si `REPRODUCIR.md` permite repetir los pasos del §4 sin ambigüedad.

## Entrega

En `Resultados\Trabajo_Cline\T03_revision_T01\`:

1. **`REVISION_T03.md`.** Crea primero un esqueleto con las secciones R1, R2, R3, Hallazgos y Dictamen, y **ve rellenándolo a medida que avances**. Contenido final:
   - tabla de hallazgos: id, severidad (crítica / mayor / menor / nota), afirmación revisada, evidencia (archivo:línea o página del PDF), recomendación;
   - conclusión de R1 (demostrada / plausible / no sustentada);
   - dictamen global: «sin objeciones», «objeciones menores» u «objeciones mayores».
2. **`src\`** con tus scripts, **`data_derived\`** con sus salidas (CSV/JSON) y **`logs\`** con stdout y exit_code de cada ejecución.
3. Al terminar, responde con un resumen breve: el dictamen, la conclusión de R1, los hallazgos mayores o críticos y los archivos creados. **No declares la aceptación**: la decide el coordinador.
