# T02: criterios fijados antes de extraer o evaluar

Fecha de preespecificación: 10-oct-2026. Contrato T02 v1.0, §5.2; plan E2 H1.

Se compararán SG y SLP BICR, ITT, durvalumab y placebo. Son pseudo-IPD, no datos originales.

| Cantidad | Criterio contractual |
|---|---|
| Eventos por brazo | error relativo absoluto <= 0,03 |
| Tasas SG24/36 y SLP18/24 | error absoluto <= 0,02 en probabilidad |
| HR no estratificado | error absoluto <= 0,03 respecto a 0,73 SG / 0,76 SLP |
| Medianas | error absoluto <= 1 mes; SG durvalumab <= 3 meses |
| Riesgo | informar todos los tiempos; explicar diferencias absolutas >1 |

Clasificación operacional fijada antes de resultados: **reproducido** si satisface la tolerancia; **discrepancia** si no la satisface; **no evaluable** si falta estimación, referencia o criterio comparable. Para riesgo: igualdad exacta = reproducido; diferencia de 1 = parcialmente reproducido; mayor de 1 = discrepancia descriptiva (no se introduce una tolerancia de aceptación). No se usará «parcialmente reproducido» para rescatar incumplimientos de tolerancias numéricas. Los IC, seguimiento y prueba PH son informativos: se reportan con «no evaluable» para aceptación por carecer de tolerancia contractual y/o método publicado suficientemente especificado. H1 se juzga sobre las 18 cantidades con tolerancias (4 eventos, 4 medianas, 8 tasas, 2 HR).

No se cambiarán criterios tras ver errores. Se conservarán resultados originales y se documentarán primero errores de programación y justificaciones antes de cualquier corrección. No se optimizará contra medianas, tasas ni HR publicados.

E2.0: 100 conjuntos de dos brazos, n=264/266 (D04 PDF pp.6/8), ambos desenlaces; semilla base 20261010 (decisión de diseño). Simulación no paramétrica discreta con censura independiente administrativa, tiempos en meses, rejilla de riesgo cada 3 meses. Parámetros de simulación son supuestos de ensayo de software, no cifras clínicas. Se registrarán verdad, reconstrucción y errores por réplica, incluyendo medianas no alcanzadas. No se ajustarán modelos paramétricos. Se usarán KM y Cox no estratificado solamente.

Diagnóstico PH: Schoenfeld escalado, transformación de tiempo rank, lifelines; comparación informativa, no equivalencia con análisis estratificado publicado. Los eventos y números en riesgo son restricciones de entrada: su reproducción no constituye validación independiente. Las tasas, medianas y HR son validadores externos al algoritmo.

No extrapolación; las curvas, errores y KM se limitarán a su soporte observado. No RMST, curación ni subgrupos. Ejecución secuencial con hilos numéricos limitados a 1.