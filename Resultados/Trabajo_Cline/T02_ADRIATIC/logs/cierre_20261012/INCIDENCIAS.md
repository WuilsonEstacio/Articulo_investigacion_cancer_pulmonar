# Registro de incidencias y decisiones posteriores

## 10-oct-2026: inspección inicial

Las llamadas iniciales inspeccionaron el entorno y PDF antes de crear el envoltorio de ejecución. Intérprete exclusivo: `C:\Users\Administrador\PaperCancer_env\venv_cline_T02\Scripts\python.exe`. Importaciones comprobadas: numpy, scipy, pandas, matplotlib, fitz (aviso de deprecación), lifelines, yaml; el código definitivo usa pymupdf. La inspección se conserva en `pdf_inspection.json` y las páginas renderizadas; no hay duración precisa para esas llamadas exploratorias y no se inventa. Una impresión de texto de PDF falló por codificación cp1252; se repitió con stdout UTF-8. No se alteraron datos ni resultados.

## 10-oct-2026 19:26: evaluación clínica original

Registro `20261010_192632_085176.json` y copia completa `clinical_20261010_192645_...` (nombre exacto en directorio). Las 18 cantidades H1 satisfacen las tolerancias. SLP durvalumab: 140 frente a 139 eventos. Riesgo: SG-D 24 y 27 meses, SG-P 15 meses, diferencia -1. No se cambia el algoritmo para hacer coincidir estos valores.

## 10-oct-2026 19:27: ejecución E2.0 interrumpida

El comando síncrono excedió el límite de 30 segundos de la herramienta; la inspección de procesos confirmó que no seguía activo. Quedaron 11 réplicas completas y una posible réplica parcial. Se conserva el stdout `20261010_192706_357878.txt` y el snapshot asociado. No hay JSON final de ese proceso porque el envoltorio también fue terminado; estado = interrumpido, duración exacta no disponible, nunca éxito. Se relanzó desde réplica 0 en proceso desacoplado mediante Start-Process, mismo intérprete y algoritmo, mismo diseño y semillas. Los CSV de simulación parciales se regeneran determinísticamente; los parámetros no cambian.

## 10-oct-2026: ampliación descriptiva

Tras la evaluación inicial se agrega seguimiento entre sujetos censurados (mediana y rango), directamente descrito en PDF p.7, solo como auditoría informativa sin tolerancias. No se usa KM reverso porque el artículo define explícitamente el seguimiento entre censurados. No cambia la reconstrucción, H1 ni los criterios. El informe debe distinguir esta comparación descriptiva de la validación independiente. Las discrepancias de tiempos de censura son esperables bajo la asignación uniforme y no se corregirán con información de seguimiento.

## 10-oct-2026: revisión de método y documentación

Consulta web verificada de Guyot et al. DOI 10.1186/1471-2288-12-9, versión editorial 1-feb-2012, Springer Nature/BMC, sección Methods, pasos 1–8. Las ecuaciones de inversión y censura uniforme corresponden a las ecuaciones 4, 6 y 7; la búsqueda exhaustiva y la conservación del riesgo calculado son adaptaciones declaradas. No se implementa literalmente el actualizador de las ecuaciones 8/9 ni el paso 7 de supresión de eventos finales. Se mantiene el código original de reconstrucción y se remite la adaptación a revisión del coordinador. La consulta no acredita por sí sola la afirmación de consulta anterior; esta nota deja constancia de la revisión efectivamente visible ahora.

E2.0 terminó con exit_code=0 en el registro 20261010_192827_386284.json: 217,52 segundos, 100 réplicas y 1800 comparaciones evaluables dentro de tolerancia. El texto preliminar del informe que sugería fallos de tolerancia se corrigió antes de generar la entrega; no hubo cambios de algoritmo ni de criterios. La ejecución clínica precedió a E2.0 (desviación del orden enumerado en contrato §5.1); se declara y no se presenta la simulación como cegada a los resultados clínicos. No hubo ajustes del método a partir de estos resultados.

La corrida parcial inicial de simulación no se archivó íntegramente antes del relanzamiento: sus CSV fueron sobrescritos. Se conservan stdout y snapshot de código, pero no se afirma conservación íntegra de esa corrida. Las ejecuciones clínicas sí se archivaron íntegramente antes de la ampliación descriptiva.

## 10-oct-2026 19:35: generación de informe interrumpida

El comando que encadenaba clinical y report excedió 30 segundos. Clinical terminó correctamente (20261010_193530_040243.json); report empezó con 20261010_193543_049471.txt y fue interrumpido, sin JSON final. Se confirmó que no seguía activo y se relanzó solamente report en segundo plano: 20261010_193631_588732.json, exit_code=0. Las 14 pruebas pasaron (20261010_193643_570369.json). Comparación binaria de los cuatro pseudo-IPD frente al archivo clínico original: sin cambios. Se corrigió una frase que decía que la auditoría de hitos se ejecutaba antes de reconstruir: los puntos son previos, pero la comparación se calcula en validate después de la reconstrucción; no alimenta el algoritmo.

La revisión de E2.0 detecta menor censura sintética que la observada, especialmente en SLP. Se informa como limitación del diseño prescrito, sin retocar parámetros tras la evaluación.

## 11-oct-2026 — Ronda 1: conservación y geometría

Lectura completa en orden del canal, encargo, auditoría T04 y CSV de saltos fusionados, y contrato original. Se consultó la fecha local del equipo: 11-oct-2026 (el reloj local inicial mostraba 22:38, antes de la hora 22:40 escrita en el mensaje de coordinación; se conserva la fecha/hora efectiva de cada log sin corregir el reloj).

Antes de editar se conservaron los 1.235 archivos de data_derived en logs/ronda0_original y se verificaron los SHA-256; manifiesto logs/ronda0_original_sha256.csv. Código, pruebas, configuración y documentos originales en logs/ronda0_documentos. Ninguna escritura en Trabajo_Claude ni Data_insumo. No se usó git ni se instalaron paquetes.

La inspección geométrica exploratoria no evaluó objetivos clínicos. Detectó que exigir igualdad exacta de las ordenadas perdería tres mesetas con desnivel de ≈0,001 pt debido a precisión del PDF; la regla se documentó antes de evaluar la corrección. También hay salientes de unión de medio grosor que no deben contarse como mesetas. La corrección empareja bordes opuestos y verifica continuidad, sin filtrar por grosor vertical. Las 109/133/90/101 mesetas de SG-D/SG-P/SLP-D/SLP-P se obtuvieron antes de reconstruir.

Primera clínica corregida: logs/20261011_224620_892960.json, exit_code=0, 11,97 s. H1 18/18 dentro de tolerancias. SLP-D conserva 140 frente a 139 eventos; SLP-P pasa de 169 a 170 frente a 169. No se altera Guyot ni se corrigen retrospectivamente estos resultados. El informe mostrará original antes de corregido.

## 11-oct-2026 — Ronda 1: pruebas preliminares

logs/20261011_224938_097280.json, exit_code=1: dos pruebas geométricas pasaron; el ejemplo artificial de Cox era simétrico y producía HR=1 tanto con Efron como Breslow, por lo que no servía para exigir diferencia entre métodos. Se cambió exclusivamente el conjunto artificial a uno asimétrico con empates; no se cambió el estimador, ninguna tolerancia contractual ni los datos clínicos. Las tres pruebas unitarias de la ronda pasan en logs/20261011_225013_110601.json, exit_code=0. Incluyen pérdida deliberada de un borde, mesetas más cortas que el grosor y PDF sintético determinista reabierto por extract_pdf.

La corrida integral de ronda 1 se lanzó con Start-Process, sin timeout de 30 s, una sola corrida científica activa y hilos numéricos=1. E2.0a se reejecuta sin editar su implementación y E2.0b emplea las 100 semillas originales. Éxito pendiente de JSON con exit_code=0 y pruebas integrales; no se considera éxito un CSV parcial.

## 11-oct-2026 22:54 — prevención de superar cuatro procesos

La inspección de procesos mostró cuatro entradas de sistema operativo durante una corrida (envoltorio y pipeline, cada uno con lanzador del venv y proceso delegado). El pipeline original invocaba pip freeze como otro subproceso al final: habría excedido el límite estricto de cuatro. Se detuvo únicamente el proceso hijo propio de esta corrida antes de llegar a ese paso; el envoltorio cerró el registro logs/20261011_225023_712938.json con exit_code=4294967295, no éxito. Se conservaron todos los derivados parciales en logs/ronda1_infraestructura_parcial/data_derived antes del relanzamiento. Los resultados científicos y semillas no cambian.

Se sustituyó exclusivamente la invocación de pip freeze por la misma orden ejecutada en el proceso existente, capturando stdout y verificando su código de retorno. No se instala nada ni se lanza otro intérprete. Se reejecutará all desde réplica 0. Esta modificación de infraestructura evita superar cuatro entradas de proceso incluso en freeze; se verificará igualdad de requirements_T02.txt con la copia original.

## 11-oct-2026 23:04 — E2.0b detecta precisión finita de PDF

logs/20261011_225447_337597.json: exit_code=1, 456,28 s. E2.0a terminó 100/100; E2.0b conservó 40 réplicas completas y falló durante la 40 (semilla 20261050, SLP-placebo) por anchura de meseta −0,0000076294 pt. Se archivó data_derived completo en logs/ronda1_precision_pdf_parcial/data_derived antes del cambio. Se conserva el PDF fallido y sus segmentos. Se extiende la comprobación de anchura al margen geométrico de 0,002 pt ya declarado: colapso de extremos no resolubles en su promedio, sin eliminar mesetas ni tocar criterios clínicos. Prueba de regresión con la semilla afectada. Justificación añadida a DECISIONES_METODO.md después de los resultados originales, sin borrarlos. Se reejecutará all con las 100 semillas, sin reducir a las primeras 20 ni omitir la réplica fallida.

Una consulta de hashes en PowerShell combinada con espera de 20 segundos excedió el timeout de la herramienta; era solo lectura y no interrumpió el pipeline desacoplado. La verificación de hashes completa queda para las pruebas registradas, sin declarar éxito de aquella consulta.