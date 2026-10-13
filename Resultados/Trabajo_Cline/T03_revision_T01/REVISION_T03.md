# Revisión independiente T03 de T01 — encargo v2

Fecha: 12 de octubre de 2026. Revisor: Cline. Estado: revisión finalizada; redactada progresivamente.

## Alcance y trazabilidad

Se han leído completos el encargo T03 v2 y el contrato T01 v1.0. Se mantiene la clasificación preespecificada de T01: **discrepancia; 0/88 con la salida directa; H1 no se cumple**. No se ejecutan simulaciones, FEniCS ni Docker. Sin consultas web, instalaciones, git ni comunicaciones externas. Solo se escribe en el directorio autorizado de T03.

Los archivos anteriores se trasladaron a `sesion1_cortada/` antes de crear esta revisión. No se usan como fuente publicada. Fuente de R1: texto extraído de la versión MBE 2023, no el PDF preprint de Data_insumo. El código de los autores se consulta en su ubicación original y no se redistribuye.

### Referencias locales (rutas absolutas)

Las claves siguientes identifican archivos completos; las citas posteriores añaden líneas, contadas desde 1. No se han copiado archivos ni fragmentos del código original.

- **ART**: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\03_registro_busquedas\MBE_2023_Wagner_texto_extraido.txt`.
- **INF**: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Claude\T01_phasefield\INFORME_T01.md`.
- **CON**: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Coordinacion\tareas\T01_phasefield_reproduccion_Claude.md`.
- **LSA**: `C:\Users\Administrador\PaperCancer_env\repos\immunotherapy-lung-cancer-fa8e6229d1540d33014a994f1ea309d6525597aa\reduced_models\local_sensitivity_analysis.py`.
- **PAR**: `C:\Users\Administrador\PaperCancer_env\repos\immunotherapy-lung-cancer-fa8e6229d1540d33014a994f1ea309d6525597aa\reduced_models\parameters.py`.
- **P2**: `C:\Users\Administrador\PaperCancer_env\repos\immunotherapy-lung-cancer-fa8e6229d1540d33014a994f1ea309d6525597aa\reduced_models\run_spherical_patient_2.py`.
- **RUN**: `C:\Users\Administrador\PaperCancer_env\repos\immunotherapy-lung-cancer-fa8e6229d1540d33014a994f1ea309d6525597aa\reduced_models\spherical_simulation_runner.py`.
- **SOL**: `C:\Users\Administrador\PaperCancer_env\repos\immunotherapy-lung-cancer-fa8e6229d1540d33014a994f1ea309d6525597aa\reduced_models\solvers.py`.
- **MED**: `C:\Users\Administrador\PaperCancer_env\repos\immunotherapy-lung-cancer-fa8e6229d1540d33014a994f1ea309d6525597aa\reduced_models\medicine_solver.py`.
- **COORD**: `C:\Users\Administrador\PaperCancer_env\repos\immunotherapy-lung-cancer-fa8e6229d1540d33014a994f1ea309d6525597aa\reduced_models\coordinate_systems.py`.
- **LOG**: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Claude\T01_phasefield\logs\tabla2_original_20261012T035307Z.log`.
- **PUB**: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Claude\T01_phasefield\data_derived\tabla2_publicada.csv`.
- **CMP**: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Claude\T01_phasefield\src\compare_tabla2.py`.
- **DIA**: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Claude\T01_phasefield\src\diag_escala_tabla2.py`.
- **PK**: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Claude\T01_phasefield\data_derived\pk_check.json`.
- **COR**: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Claude\T01_phasefield\data_derived\correspondencia_articulo_codigo.csv`.
- **REP**: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Claude\T01_phasefield\REPRODUCIR.md`.

## R1. Justificación del reescalado alfa/100

### Evidencia inicial

El script original usa perturbaciones centrales relativas de h = 0,001: los valores del parámetro son alfa·(1±h). Divide la diferencia de integrales por 2·h·alfa·Q_base. Por tanto devuelve una aproximación de (dQ/dalfa)/Q, no la elasticidad alfa·(dQ/dalfa)/Q. No aplica un factor multiplicativo adicional alfa/100. El factor 1/T de la definición de Q media cancela en el cociente.

Fuente: `C:\Users\Administrador\PaperCancer_env\repos\immunotherapy-lung-cancer-fa8e6229d1540d33014a994f1ea309d6525597aa\reduced_models\local_sensitivity_analysis.py`, líneas 67–104 y 131–155.

La extracción de la ec. 4.1 incluye explícitamente `100%`, no simplemente `100`. Debe distinguirse la convención porcentual de la evidencia numérica y evitar atribuir una operación histórica a los autores sin documentación.

### R1.1. Definición del artículo, interpretación y unidades

Reconstrucción de la fracción en ART:1056–1076 (p. 16), respetando el símbolo porcentual de la extracción:

\[
g_{f,\alpha}:=\frac{\partial_\alpha\overline Q(f)}{\overline Q(f)}\,\frac{\alpha}{100\%},
\qquad \overline Q(f):=\frac1T\int_0^T\int_\Omega f\,dx\,dt.
\]

Alfa es el valor base del parámetro que se perturba (cada fila de Tabla 2), no un único coeficiente universal ni necesariamente alfa_H o alfa_P. El texto define g como el cambio relativo de primer orden al variar ese parámetro un 1%. Aplicando Taylor a esa descripción, con delta_alfa=0,01·alfa, resulta delta_Q/Q ≈ (dQ/dalfa)/Q · alfa/100. Este es el fundamento matemático del factor numérico utilizado.

**No debe afirmarse que la notación literal basta por sí sola:** aparece «100%», y si se interpreta literalmente como el número 1, la fórmula daría la elasticidad (×alfa), no el cambio fraccional ante un 1%. La prosa contigua y la Tabla 2 favorecen la interpretación ×alfa/100. Se conserva esta salvedad de notación; no se consultó una imagen del PDF publicado y no se sustituye por el preprint. Tampoco se confunde el resultado fraccional g=0,011 con 0,011%: corresponde a aproximadamente 1,1% de cambio de Q ante un 1% de cambio de alfa.

El artículo denomina Q media «masa temporalmente promediada», pero las phi son fracciones volumétricas adimensionales (ART:112–117). La integral espacial tiene dimensión de volumen; usando metros, Q media está en m³, no en porcentaje ni en gramos. La integración temporal sin dividir por T está en m³·día; dividir por T recupera m³. Para Vvis se promedia el volumen visible, definido mediante un indicador espacial (ART:663–665), no se vuelve a integrar espacialmente un escalar volumen. El código integra fracciones/indicador con el peso esférico 4·pi·r² (COORD:18–41; SOL:475–493); la conversión a cm³, igual que 1/T, cancela en la razón normalizada. El /100 no procede de unidades de Q.

### R1.2. Fórmula del código y límite de la redacción corregida

LSA:8–10 aplica trapecios; 70–75 calcula la referencia; 83–99 construye alfa·(1±h), con h=0,001 (137). Las líneas 101–104 dividen por 2·h·alfa·Q_base. La separación entre extremos es 2·h·alfa; el paso absoluto por lado es h·alfa, como indica ART:1075–1076. Los resultados se agregan e imprimen sin nuevo reescalado (LSA:106–127).

**La corrección algebraica de INF:103–105 es exacta:** no calcula directamente la elasticidad; no multiplica finalmente por alfa ni divide por 100. Sin embargo, llamarlo sin reserva «derivada local normalizada» es inexacto para P2 por la reconstrucción de parámetros que sigue.

#### Inconsistencia de configuración en P2 (hallazgo H01)

| Campo no incluido en el vector de 11 parámetros | Referencia P2 | Perturbaciones + y − de P2 |
|---|---:|---:|
| MED_mas (g/mol) | 143600 | 146000 |
| MED_dos (g) | 0,20 | 0,24 |
| MED_tim (días) | 22 | 26,7 |

La referencia usa LSA:23–31. La reconstrucción de LSA:35–48 solo conserva las once componentes y deja esos campos en los valores por defecto de PAR:34–37. LSA:87–95 utiliza esa reconstrucción en ambas perturbaciones. P2:111–148 no los repone; RUN:57 pasa el objeto al sistema; SOL:907–911 lo entrega al solucionador PK; MED:30–42 usa los tres valores. La verificación propia evalúa únicamente constantes del árbol sintáctico: no importa ni ejecuta módulos de los autores.

Por tanto, en P2 el cociente realmente tiene la estructura [Q(alfa+delta; beta_defecto)−Q(alfa−delta; beta_defecto)]/[2·delta·Q(alfa; beta_P2)]. El numerador diferencia alrededor de una configuración farmacocinética y el denominador normaliza con otra. No es la sensibilidad local convencional en una configuración única. En P1 no aparece esta pérdida de campos. **El defecto de construcción queda demostrado estáticamente; su efecto cuantitativo en los índices no se conoce.** No se afirma que produzca necesariamente un cambio grande, ni que los autores hayan usado otra implementación.

### R1.3. Valores alfa y log

Orden: lambda_P_pro, lambda_tau_eff, lambda, lambda_PN, sigma_PN, c_m, eps_P, c_Psi, kappa_i, alfa_H, alfa_P.

- P1: (0,360675; 5,2395; 2; 0,1; 0,2; 0,0005; 0,0005; 2; 0,00001; 1; 4).
- P2: (0,0037785; 0,5489; 1; 20; 0,2; 0,0005; 0,0005; 2; 0,00001; 1; 4).

Derivados de LSA:13–63 y PAR:16–31. Coinciden con CMP:28–29, consultado solo después del cálculo independiente, y con los 22 vectores completos del LOG (incluidos los de P1 impresos tras la etiqueta Patient 2 por el orden de vaciado de salida). La asignación se hizo por sus valores, no por esa etiqueta. Los vectores de 11 componentes **no muestran** los tres campos PK omitidos: su coincidencia no descarta H01.

Para la alternativa Tabla 1 se usaron 0,36 y 5,2 en P1, 0,0038 y 0,54 en P2; el resto no cambia (ART:320–410). El 0,54 publicado no es el redondeo correcto de 0,5489, que sería 0,55; se usa tal como está publicado, no se corrige silenciosamente.

### Resultados independientes ya verificados

La primera ejecución de `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T03_revision_T01\src\revisar_t03.py` terminó con exit_code=0. No usa los comparadores de T01 para calcular. Contrastó las 88 cifras y los 88 rangos con el texto publicado: todos coinciden. Los 22 vectores base impresos (11 por paciente) coinciden con los valores derivados estáticamente de los parámetros originales.

| Transformación | Error relativo máximo (%) | ≤10% y signo / 88 | Rangos / 88 | Igualdad al redondear a 3 cifras / 88 |
|---|---:|---:|---:|---:|
| Directa | 1,00218 × 10^9 | 0 | 8 | 0 |
| ×alfa/100 | 0,449402 | 88 | 88 | 88 |
| ×alfa | 9930,727 | 0 | 88 | 0 |
| /100 | 10021749,946 | 12 | 8 | 12 |
| ×alfa del otro paciente/100 | 19938,652 | 56 | 25 | 56 |
| ×alfa de Tabla 1/100 | 1,812175 | 88 | 88 | 74 |
| ×alfa/101 (control sin justificación teórica) | 1,435051 | 88 | 88 | 0 |

La concordancia a tres cifras significativas de ×alfa/100 sí queda demostrada para este log y esta tabla; no demuestra el procedimiento histórico. Las alternativas con los valores de Tabla 1 y con divisor 101 también cumplen el umbral del 10% y todos los rangos: ese umbral no identifica una explicación única.

### R1.4–R1.5. Precisión, alternativas y transcripción

Todos los errores se calculan como |g_calculado−g_publicado|/|g_publicado|. Los rangos son por |g| descendente, dentro de cada paciente y métrica. Todas las alternativas conservan 88/88 signos. Para ×alfa/100: mediana 0,0682682%, p90 0,220842% y máximo 0,449402%, en P1/lambda_P_pro/phiT (0,01095056581 frente a 0,0110). Los 88 resultados redondean a los 88 números impresos: la frase sobre tres cifras de INF:117 está sustentada, no es solo una comparación con el 10%.

Si además del signo y la tolerancia se exige coincidencia de rango conforme a CON:54, las siete alternativas de la tabla obtienen respectivamente 0, 88, 0, 2, 21, 88 y 88 valores reproducidos. Son conteos **diagnósticos**, nunca una reclasificación de T01.

×alfa/100 es la única de estas siete alternativas que recupera las 88 cifras al redondear a tres cifras significativas, pero no se ha probado unicidad entre todas las transformaciones posibles. El control /101 exhibe la falta de identificación bajo el umbral del 10%; no es una propuesta científica rival. Cambiar alfa por el del otro paciente conserva las siete componentes comunes (56 cifras), pero falla en las otras: su pequeña mediana de error no implica concordancia global.

La transcripción fue **completa**, no una muestra: ART:1119–1319 contra PUB:2–23, 88 números con signo y 88 rangos, sin discrepancias. El CSV propio registra para cada cifra la línea del texto publicado. Esta comprobación valida contra el texto extraído, no contra una nueva inspección visual de la página publicada.

### R1.6. Conclusión

**R1: PLAUSIBLE**, con fuerte respaldo numérico y teórico, como explicación del postprocesado de la tabla. Queda **demostrada la concordancia numérica** de ×alfa/100 con este log y estas 88 cifras, y queda demostrada su ausencia como operación final en el script. La descripción en palabras de la ec. 4.1 justifica el factor mediante Taylor; la notación «100%» requiere explicitar la interpretación. No queda demostrado que los autores generaran históricamente la tabla aplicando ese postprocesado a este mismo script/entorno ni que esa sea la única diferencia metodológica. H01 impide convertir la concordancia en validación íntegra de la sensibilidad local de P2.

## R2. Alcance de la interpretación

| Frase de T01 | Evaluación | Redacción recomendada |
|---|---|---|
| «La simulación reproduce los índices de los autores» (INF:120) | Sobredimensionada si significa validar el método; sustentada solo como concordancia numérica tras transformación. | «Las salidas del log, reescaladas por alfa/100, coinciden con los 88 valores publicados al redondear a tres cifras y conservan todos los rangos.» |
| «La única diferencia es un postprocesado» (INF:120) | No sustentada como exclusividad; H01 y las discrepancias ya listadas en §5 impiden afirmarlo. | «El reescalado explica la diferencia numérica observada, pero no valida por sí solo la implementación del procedimiento.» |
| «La Tabla 2 se obtuvo aplicando alfa/100» (INF:120) | Sobredimensionada como hecho histórico. INF:121 la llama inferencia, pero no elimina la afirmación categórica anterior. | «Los resultados son compatibles con un postprocesado alfa/100; no se documenta cómo los autores generaron la tabla.» |
| «88 valores coinciden [...] a tres cifras significativas» (INF:117) | Sustentada: comprobación explícita 88/88. | Mantener, especificando «al redondear» y el máximo de 0,4494%. |
| «La discrepancia se explica íntegramente por la diferencia de definición» (INF:131; resumen INF:12; INF:142) | Sobredimensionada si se extiende del ajuste numérico a todo el método. | «La discrepancia de escala observada se elimina, a la precisión publicada, mediante alfa/100; subsisten limitaciones metodológicas.» |
| Formulación para informe integrado (INF:132) | Necesita matiz: interpretación porcentual, carácter diagnóstico y H01. | Usar la propuesta siguiente. |

**Propuesta para el informe integrado:** «Con la salida directa del script, la Tabla 2 mantiene la clasificación preespecificada de discrepancia (0/88; H1 no se cumple). Como diagnóstico, multiplicar por alfa/100 —coherente con interpretar g como cambio relativo ante una variación del parámetro del 1%— recupera las 88 cifras al redondear a tres cifras significativas y los 88 rangos (error máximo 0,4494%). La coincidencia respalda, pero no demuestra, ese postprocesado histórico. Además, las perturbaciones de P2 no conservan tres parámetros PK de la referencia; su efecto no se ha cuantificado. No se infiere validación predictiva ni clínica.»

Los 88 índices proceden de **dos pacientes calibrados**, no de 88 observaciones clínicas independientes. Las versiones de las bibliotecas de los autores son desconocidas (INF:26,150–151). Los residuos son compatibles con el redondeo; no es necesario ni está demostrado atribuirlos a versiones concretas. La revisión no estima convergencia numérica, identificabilidad ni generalización fuera de muestra.

## R3. Comprobaciones breves

Revisión documental breve, sin rehacer PK ni ejecutar los modelos; prioridad y esfuerzo concentrados en R1/R2.

1. **Coherencia de Tabla 2:** los dos JSON de T01 concuerdan con los errores mediana/p90/máximo y rangos calculados de forma independiente (tolerancia numérica 1e−12). Son los archivos absolutos `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Claude\T01_phasefield\data_derived\tabla2_resumen.json` y `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Claude\T01_phasefield\data_derived\tabla2_diag_escala_resumen.json`. Se confirman 88 discrepancias directas y la aplicación del criterio global negativo. La pequeña diferencia del último decimal del p90 entre implementaciones carece de relevancia.
2. **Detalle latente del comparador:** CMP:34–43 y DIA:16 clasifican por error/signo, aunque CON:54 exige «parcialmente reproducido» cuando el rango difiere. Los rangos se calculan aparte sin modificar esa etiqueta. No cambia el resultado actual (todos fallan directamente; todos cumplen reescalados); conviene corregirlo antes de reutilizar esos scripts.
3. **PK:** INF:10 dice 4/6 extremos dentro del 0,1%, pero PK:8–29 e INF:34–38 dan **3/6**, con tres incumplimientos: valle P1 Q2W (0,106546%), valle P2 Q3W (0,129313%) y pico P2 Q6W (0,129136%). Es un error del resumen, no una nueva clasificación. No se rehace ni se objeta aquí el diagnóstico de medio subpaso; su efecto tumoral sigue no cuantificado, como reconoce INF:59.
4. **Correspondencia:** la entrada de g sigue «por evaluar» en COR:36 y en INF:11, aunque §4.5 ya la evalúa. El resumen debe sincronizarse. Los desfases de origen temporal no deben confundirse con discrepancias de terapia: usando la alineación que declara COR:33–34, 322−296=26 días para inicio P1, 671−514=157 para Q6W P2 y 1218−1063=155 para fin P2; no 176 y 114 días de discrepancia como podría entenderse de INF:139–140. Son aritmética sobre la correspondencia existente, no una nueva validación de la cronología clínica. Se conserva la advertencia sobre 0,5489 frente a 0,54.
5. **Reproducción documental:** REP:48–72 permite reconstruir el flujo original→log→comparación→diagnóstico→figura para una persona que sustituya el marcador `<UTC>` por el nombre real. No es completamente literal: ese marcador con corchetes angulares no debe pegarse en Bash sin sustituirlo; la ruta concreta del log ya aparece en REP:72. Para reproducir exactamente el entorno se remite al lock (REP:26), pero falta el comando explícito para construirlo desde él. Recomendación: dar comandos con el log real y construcción bloqueada, y explicitar procesos/hilos efectivos; el Docker `--cpus 8` no limita por sí solo el número de workers (INF:68–70). No se relanzó el flujo ni se promete reproducibilidad bit a bit. El plazo estimado de 4,5 h en REP:48 es inferior a los 309 minutos registrados, detalle menor.

## Hallazgos

| ID | Severidad | Afirmación revisada | Evidencia | Recomendación |
|---|---|---|---|---|
| H01 | **mayor** | Sensibilidad local de P2 alrededor de una referencia única; «única diferencia: postprocesado» | LSA:23–48,70,87–104; PAR:34–37; P2:111–148; RUN:57; SOL:907–911; MED:30–42. Análisis estático propio confirmado. | Documentar los tres campos PK restablecidos y limitar la interpretación. Una eventual corrección y nueva simulación requiere otra tarea; no cambiar aquí clasificación ni código T01. |
| H02 | **mayor** | Obtención histórica de Tabla 2 y explicación «íntegra» presentadas como hechos | INF:120–132 y 142; ART:1059–1076; alternativas numéricas propias. | Separar concordancia demostrada de postprocesado histórico plausible; eliminar exclusividad y usar la formulación integrada propuesta. |
| H03 | menor | Ec. 4.1 justifica literalmente alfa/100 | ART:1059–1076; INF:103. | Conservar el símbolo porcentual y explicar Taylor/convención, sin sustituir 100% por 100 silenciosamente. |
| H04 | menor | Resumen PK: 4/6 extremos cumplen | INF:10 frente a INF:34–38 y PK:8–29. | Corregir a 3/6; mantener clasificación original. |
| H05 | menor | Clasificador implementa íntegramente el criterio de rango | CON:54; CMP:34–43,65–66; DIA:16–24. | Incorporar el rango al etiquetado si se reutiliza. No afecta a los dos resultados presentes. |
| H06 | menor | Correspondencia actualizada y magnitud de desfases | COR:33–36; INF:11,139–142. | Actualizar estado de g y distinguir cambio de origen temporal de discrepancia clínica. |
| H07 | menor | Reproducción sin ambigüedad literal | REP:26,48–72; INF:68–70. | Dar log concreto, comando de entorno bloqueado y límites de paralelismo explícitos. |
| H08 | nota | Transcripción, alfa y cifras diagnósticas | ART:1119–1319; PUB:2–23; CMP:28–29; LOG; salidas propias. | Sin corrección numérica: 88 cifras/88 rangos de la transcripción correctos; ×alfa/100 coincide a tres cifras. |

## Dictamen

**DICTAMEN GLOBAL: OBJECIONES MAYORES.** Dos hallazgos mayores (H01–H02), ninguno clasificado como crítico. **R1: PLAUSIBLE** como explicación del procedimiento/postprocesado histórico; **concordancia numérica demostrada** dentro del alcance verificado.

No se cuestiona el cómputo del diagnóstico de escala ni la transcripción. Se objeta extender esa concordancia a una validación completa del método y presentar como probado el modo histórico de generación de Tabla 2. La aceptación corresponde exclusivamente al coordinador.

**Clasificación original de T01 mantenida: discrepancia; salida directa 0/88; H1 no se cumple.**

## Entregables y validación

Todo lo nuevo está dentro de `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T03_revision_T01`:

- `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T03_revision_T01\REVISION_T03.md`: esta revisión.
- `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T03_revision_T01\src\revisar_t03.py`: cálculo independiente con biblioteca estándar, AST restringido, comprobaciones y hashes de entradas; nunca importa el código original ni los comparadores T01.
- `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T03_revision_T01\src\validar_entrega.py`: validación final de productos y entradas.
- `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T03_revision_T01\data_derived\transcripcion_88.csv`: contraste completo, con líneas de ART.
- `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T03_revision_T01\data_derived\alfa_verificacion.csv`: 22 componentes y valores publicados alternativos.
- `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T03_revision_T01\data_derived\alternativas_616.csv`: 7×88 comparaciones individuales, errores, signos, rangos, redondeo y etiquetas diagnósticas.
- `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T03_revision_T01\data_derived\revision_resumen.json`: resúmenes, campos PK omitidos, coherencia con T01 y SHA-256.
- Registros en `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T03_revision_T01\logs\revision_independiente.log`, `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T03_revision_T01\logs\revision_final.log` y `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T03_revision_T01\logs\validacion_entrega.log`, con salida y exit_code.
- Archivo histórico aislado: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T03_revision_T01\sesion1_cortada`.

Reejecución en PowerShell (un proceso Python; sin simulaciones ni instalaciones):

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
$env:OMP_NUM_THREADS='1'; $env:OPENBLAS_NUM_THREADS='1'
$env:MKL_NUM_THREADS='1'; $env:NUMEXPR_NUM_THREADS='1'
& 'C:\Users\Administrador\PaperCancer_env\venv_cline_T02\Scripts\python.exe' -B 'C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T03_revision_T01\src\revisar_t03.py'
& 'C:\Users\Administrador\PaperCancer_env\venv_cline_T02\Scripts\python.exe' -B 'C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T03_revision_T01\src\validar_entrega.py'
```

Limitaciones operativas: no se dispone de contador de gasto USD desde estas herramientas; se redujeron las operaciones a lecturas y dos scripts propios. No se afirma un importe consumido. No se verifican el PDF publicado ni las versiones originales de bibliotecas; no se cuantifica el efecto de H01 mediante simulación.