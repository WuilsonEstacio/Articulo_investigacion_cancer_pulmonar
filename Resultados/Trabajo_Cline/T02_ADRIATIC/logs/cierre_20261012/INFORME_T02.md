# INFORME T02 — Reconstrucción ADRIATIC

Fecha: 10-oct-2026. Estado: entregada para revisión, no aceptada.

## Resultado ejecutivo

Se reconstruyeron las cuatro curvas ITT (SG y SLP BICR; durvalumab/placebo). **18/18 cantidades H1 reproducidas** conforme al contrato v1.0 §5.2; no se modificaron tolerancias. La validación numérica no significa recuperación de los datos originales ni aceptación por el coordinador.

Los pseudo-IPD tienen 264/266 sujetos por brazo y desenlace [D04 PDF pp.6/8; comprobación en inventario]. No existe enlace entre sujetos de SG y SLP: son reconstrucciones marginales separadas, no una cohorte conjunta utilizable para análisis multidesenlace.

## Fuentes y método

- Artículo autorizado: Cheng et al., NEJM 2024;391:1313–27, DOI 10.1056/NEJMoa2404873. Curvas/riesgo: Fig.1A p.6 y Fig.2A p.8; medianas/tasas/eventos/seguimiento: p.7; forest p.6/8; PH: leyendas pp.7/9. Se verificó el SHA-256 contra la ficha D04.
- Método: Guyot et al., BMC Med Res Methodol 2012;12:9, DOI 10.1186/1471-2288-12-9, Methods, ecuaciones 1–9 y pasos 1–8. Versión editorial 1-feb-2012 consultada 10-oct-2026. Implementación Python independiente **basada en Guyot**, no copia exacta del R original.
- Diferencias declaradas previamente: búsqueda entera exhaustiva de censuras uniformes por intervalo, sin reiniciar artificialmente el riesgo; desempate por error de curva. El total de eventos guía el último intervalo; no se modifica retrospectivamente ningún evento previo. Si no puede alcanzarse el total se informa. Residuo administrativo censurado al extremo observado. Esto deja 140 frente a 139 eventos en SLP-D, dentro del 3 %, pero no es cumplimiento exacto de la restricción.
- Extracción vectorial: colores, centros de polígonos estrechos, contorno de menor complejidad; marcas rectangulares separadas y deduplicadas. Puntos/segmentos conservan página, trazado y coordenadas PDF. Ejes calibrados con 22 ticks x y 11 ticks y, verificados por código. No se emplearon medianas ni hitos para calibrar o reconstruir.
- Censura uniforme intraintervalo y redondeo de eventos son supuestos. Los tiempos aproximados no son tiempos originales. Riesgo calculado como número de tiempos >= t; empates con eventos antes de censuras. Las simulaciones usan el mismo código.
- Exclusiones respetadas: sin extrapolación, ajustes paramétricos, curación, RMST ni subgrupos. Cox no estratificado se usa solo para validación contractual. Sin instalaciones nuevas; entorno congelado.

Detalle preevaluación: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\CRITERIOS_PREESPECIFICADOS.md` y `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\DECISIONES_METODO.md`. Correcciones/incidencias: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\logs\INCIDENCIAS.md`.

## Validación principal (cálculo registrado)

Las tasas se muestran como probabilidades; diferencias en la misma escala. Fuente individual y tolerancia en cada fila del CSV de validación. Eventos y riesgo son entradas, por lo que su reproducción no es validación independiente.

| quantity | endpoint | arm | published | reconstructed | difference | classification |
| --- | --- | --- | --- | --- | --- | --- |
| eventos_totales | SG | durvalumab | 115 | 115 | 0 | reproducido |
| mediana | SG | durvalumab | 55.9 | 55.9368 | 0.0367647 | reproducido |
| S_24 | SG | durvalumab | 0.68 | 0.680036 | 3.62833e-05 | reproducido |
| S_36 | SG | durvalumab | 0.565 | 0.564465 | -0.000535135 | reproducido |
| eventos_totales | SG | placebo | 146 | 146 | 0 | reproducido |
| mediana | SG | placebo | 33.4 | 33.3875 | -0.0124813 | reproducido |
| S_24 | SG | placebo | 0.585 | 0.584837 | -0.000163134 | reproducido |
| S_36 | SG | placebo | 0.476 | 0.476232 | 0.000231855 | reproducido |
| eventos_totales | SLP | durvalumab | 139 | 140 | 1 | reproducido |
| mediana | SLP | durvalumab | 16.6 | 16.5446 | -0.0553517 | reproducido |
| S_18 | SLP | durvalumab | 0.488 | 0.490592 | 0.00259194 | reproducido |
| S_24 | SLP | durvalumab | 0.462 | 0.459732 | -0.00226804 | reproducido |
| eventos_totales | SLP | placebo | 169 | 169 | 0 | reproducido |
| mediana | SLP | placebo | 9.2 | 9.08767 | -0.112329 | reproducido |
| S_18 | SLP | placebo | 0.361 | 0.360957 | -4.27971e-05 | reproducido |
| S_24 | SLP | placebo | 0.342 | 0.34262 | 0.000619968 | reproducido |
| HR | SG | D vs P | 0.73 | 0.73026 | 0.000260385 | reproducido |
| HR | SLP | D vs P | 0.76 | 0.770193 | 0.0101926 | reproducido |

## Números en riesgo

Clasificaciones: {'reproducido': 85, 'parcialmente reproducido': 3}. No hay diferencias mayores de un sujeto. Las diferencias no nulas corresponden a la imposibilidad de lograr exactamente el entero siguiente con la inversión KM y censura uniforme; no se fuerza un reinicio del riesgo.

| quantity | endpoint | arm | published | reconstructed | difference | classification |
| --- | --- | --- | --- | --- | --- | --- |
| riesgo_24 | SG | durvalumab | 172 | 171 | -1 | parcialmente reproducido |
| riesgo_27 | SG | durvalumab | 162 | 161 | -1 | parcialmente reproducido |
| riesgo_15 | SG | placebo | 195 | 194 | -1 | parcialmente reproducido |

Tabla completa de los 88 controles:

| quantity | endpoint | arm | published | reconstructed | difference | classification |
| --- | --- | --- | --- | --- | --- | --- |
| riesgo_0 | SG | durvalumab | 264 | 264 | 0 | reproducido |
| riesgo_3 | SG | durvalumab | 261 | 261 | 0 | reproducido |
| riesgo_6 | SG | durvalumab | 248 | 248 | 0 | reproducido |
| riesgo_9 | SG | durvalumab | 236 | 236 | 0 | reproducido |
| riesgo_12 | SG | durvalumab | 223 | 223 | 0 | reproducido |
| riesgo_15 | SG | durvalumab | 207 | 207 | 0 | reproducido |
| riesgo_18 | SG | durvalumab | 189 | 189 | 0 | reproducido |
| riesgo_21 | SG | durvalumab | 183 | 183 | 0 | reproducido |
| riesgo_24 | SG | durvalumab | 172 | 171 | -1 | parcialmente reproducido |
| riesgo_27 | SG | durvalumab | 162 | 161 | -1 | parcialmente reproducido |
| riesgo_30 | SG | durvalumab | 141 | 141 | 0 | reproducido |
| riesgo_33 | SG | durvalumab | 110 | 110 | 0 | reproducido |
| riesgo_36 | SG | durvalumab | 90 | 90 | 0 | reproducido |
| riesgo_39 | SG | durvalumab | 68 | 68 | 0 | reproducido |
| riesgo_42 | SG | durvalumab | 51 | 51 | 0 | reproducido |
| riesgo_45 | SG | durvalumab | 39 | 39 | 0 | reproducido |
| riesgo_48 | SG | durvalumab | 27 | 27 | 0 | reproducido |
| riesgo_51 | SG | durvalumab | 19 | 19 | 0 | reproducido |
| riesgo_54 | SG | durvalumab | 11 | 11 | 0 | reproducido |
| riesgo_57 | SG | durvalumab | 5 | 5 | 0 | reproducido |
| riesgo_60 | SG | durvalumab | 1 | 1 | 0 | reproducido |
| riesgo_63 | SG | durvalumab | 0 | 0 | 0 | reproducido |
| riesgo_0 | SG | placebo | 266 | 266 | 0 | reproducido |
| riesgo_3 | SG | placebo | 260 | 260 | 0 | reproducido |
| riesgo_6 | SG | placebo | 247 | 247 | 0 | reproducido |
| riesgo_9 | SG | placebo | 231 | 231 | 0 | reproducido |
| riesgo_12 | SG | placebo | 214 | 214 | 0 | reproducido |
| riesgo_15 | SG | placebo | 195 | 194 | -1 | parcialmente reproducido |
| riesgo_18 | SG | placebo | 175 | 175 | 0 | reproducido |
| riesgo_21 | SG | placebo | 164 | 164 | 0 | reproducido |
| riesgo_24 | SG | placebo | 151 | 151 | 0 | reproducido |
| riesgo_27 | SG | placebo | 143 | 143 | 0 | reproducido |
| riesgo_30 | SG | placebo | 123 | 123 | 0 | reproducido |
| riesgo_33 | SG | placebo | 97 | 97 | 0 | reproducido |
| riesgo_36 | SG | placebo | 80 | 80 | 0 | reproducido |
| riesgo_39 | SG | placebo | 62 | 62 | 0 | reproducido |
| riesgo_42 | SG | placebo | 44 | 44 | 0 | reproducido |
| riesgo_45 | SG | placebo | 31 | 31 | 0 | reproducido |
| riesgo_48 | SG | placebo | 23 | 23 | 0 | reproducido |
| riesgo_51 | SG | placebo | 19 | 19 | 0 | reproducido |
| riesgo_54 | SG | placebo | 8 | 8 | 0 | reproducido |
| riesgo_57 | SG | placebo | 5 | 5 | 0 | reproducido |
| riesgo_60 | SG | placebo | 1 | 1 | 0 | reproducido |
| riesgo_63 | SG | placebo | 0 | 0 | 0 | reproducido |
| riesgo_0 | SLP | durvalumab | 264 | 264 | 0 | reproducido |
| riesgo_3 | SLP | durvalumab | 212 | 212 | 0 | reproducido |
| riesgo_6 | SLP | durvalumab | 161 | 161 | 0 | reproducido |
| riesgo_9 | SLP | durvalumab | 135 | 135 | 0 | reproducido |
| riesgo_12 | SLP | durvalumab | 113 | 113 | 0 | reproducido |
| riesgo_15 | SLP | durvalumab | 105 | 105 | 0 | reproducido |
| riesgo_18 | SLP | durvalumab | 101 | 101 | 0 | reproducido |
| riesgo_21 | SLP | durvalumab | 98 | 98 | 0 | reproducido |
| riesgo_24 | SLP | durvalumab | 84 | 84 | 0 | reproducido |
| riesgo_27 | SLP | durvalumab | 78 | 78 | 0 | reproducido |
| riesgo_30 | SLP | durvalumab | 51 | 51 | 0 | reproducido |
| riesgo_33 | SLP | durvalumab | 51 | 51 | 0 | reproducido |
| riesgo_36 | SLP | durvalumab | 33 | 33 | 0 | reproducido |
| riesgo_39 | SLP | durvalumab | 21 | 21 | 0 | reproducido |
| riesgo_42 | SLP | durvalumab | 19 | 19 | 0 | reproducido |
| riesgo_45 | SLP | durvalumab | 10 | 10 | 0 | reproducido |
| riesgo_48 | SLP | durvalumab | 10 | 10 | 0 | reproducido |
| riesgo_51 | SLP | durvalumab | 4 | 4 | 0 | reproducido |
| riesgo_54 | SLP | durvalumab | 4 | 4 | 0 | reproducido |
| riesgo_57 | SLP | durvalumab | 0 | 0 | 0 | reproducido |
| riesgo_60 | SLP | durvalumab | 0 | 0 | 0 | reproducido |
| riesgo_63 | SLP | durvalumab | 0 | 0 | 0 | reproducido |
| riesgo_0 | SLP | placebo | 266 | 266 | 0 | reproducido |
| riesgo_3 | SLP | placebo | 208 | 208 | 0 | reproducido |
| riesgo_6 | SLP | placebo | 146 | 146 | 0 | reproducido |
| riesgo_9 | SLP | placebo | 122 | 122 | 0 | reproducido |
| riesgo_12 | SLP | placebo | 100 | 100 | 0 | reproducido |
| riesgo_15 | SLP | placebo | 88 | 88 | 0 | reproducido |
| riesgo_18 | SLP | placebo | 79 | 79 | 0 | reproducido |
| riesgo_21 | SLP | placebo | 76 | 76 | 0 | reproducido |
| riesgo_24 | SLP | placebo | 71 | 71 | 0 | reproducido |
| riesgo_27 | SLP | placebo | 69 | 69 | 0 | reproducido |
| riesgo_30 | SLP | placebo | 47 | 47 | 0 | reproducido |
| riesgo_33 | SLP | placebo | 47 | 47 | 0 | reproducido |
| riesgo_36 | SLP | placebo | 34 | 34 | 0 | reproducido |
| riesgo_39 | SLP | placebo | 23 | 23 | 0 | reproducido |
| riesgo_42 | SLP | placebo | 22 | 22 | 0 | reproducido |
| riesgo_45 | SLP | placebo | 15 | 15 | 0 | reproducido |
| riesgo_48 | SLP | placebo | 14 | 14 | 0 | reproducido |
| riesgo_51 | SLP | placebo | 5 | 5 | 0 | reproducido |
| riesgo_54 | SLP | placebo | 5 | 5 | 0 | reproducido |
| riesgo_57 | SLP | placebo | 0 | 0 | 0 | reproducido |
| riesgo_60 | SLP | placebo | 0 | 0 | 0 | reproducido |
| riesgo_63 | SLP | placebo | 0 | 0 | 0 | reproducido |

## Error de curva y extracción

La diferencia entre la curva extraída y KM en rejilla de 0,1 meses cumple la métrica solicitada; no es un estimador puro de error de digitalización, pues también incorpora error de reconstrucción. No existe una curva original numérica independiente con la que separar ambos componentes. Máximo global: 0.828122 puntos porcentuales. Sin prolongación más allá del trazado.

| endpoint | arm | max_absolute | mean_absolute | grid_months | grid_n | support_end |
| --- | --- | --- | --- | --- | --- | --- |
| SG | durvalumab | 0.00828122 | 0.00125025 | 0.1 | 603 | 60.2044 |
| SG | placebo | 0.00381057 | 0.00144387 | 0.1 | 610 | 60.9533 |
| SLP | durvalumab | 0.00710075 | 0.00272804 | 0.1 | 554 | 55.3627 |
| SLP | placebo | 0.00261896 | 0.00128551 | 0.1 | 559 | 55.8181 |

Auditoría geométrica:

| curva | page | path_id | points | support_end | unique_marks | origin_shift_probability | s0 | monotone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SG_durvalumab | 6 | 737 | 74 | 60.2044 | 133 | 0.000254547 | 1 | True |
| SG_placebo | 6 | 251 | 82 | 60.9533 | 107 | 0.000254547 | 1 | True |
| SLP_durvalumab | 8 | 720 | 46 | 55.3627 | 96 | -0.000141008 | 1 | True |
| SLP_placebo | 8 | 334 | 51 | 55.8181 | 77 | -0.000141008 | 1 | True |

Todas las curvas son monótonas, S(0)=1; los hitos de los puntos extraídos se comparan en la etapa de validación, sin alimentar la reconstrucción en las filas `scope=extraccion`. Los números en riesgo obtenidos de coordenadas de texto coinciden exactamente con la tabla autorizada. Los intervalos SLP 30–33 meses no tienen eventos ni censuras reconstruidos; el control está en las pruebas de integración. Las marcas visibles no permiten contar todos los censurados: pueden solaparse, duplicarse o representar empates; la tabla de coherencia muestra por intervalo salidas del riesgo, marcas y censuras reconstruidas. No se afirma haber recuperado su multiplicidad original.

## Validación informativa: IC, PH y seguimiento

Los IC KM usan Greenwood log-log. Se comparan sus extremos, sin tolerancia contractual. PH usa Schoenfeld escalado con transformación rank y Cox no estratificado; no se considera réplica exacta de la prueba publicada, cuyo ajuste y definición pueden diferir. El seguimiento es la distribución de tiempos entre sujetos censurados, tal como dice la p.7, no KM inverso. Las cifras descriptivas de censura no se usan para ajustar la reconstrucción. `NR` representa no alcanzado, no un tiempo extrapolado.

| quantity | endpoint | arm | published | reconstructed | difference | classification |
| --- | --- | --- | --- | --- | --- | --- |
| mediana_IC95_inferior | SG | durvalumab | 37.3 | 35.6193 | -1.68072 | no evaluable |
| mediana_IC95_superior | SG | durvalumab | NR | NR | — | no evaluable |
| S_24_IC95_inferior | SG | durvalumab | 0.619 | 0.619034 | 3.39414e-05 | no evaluable |
| S_24_IC95_superior | SG | durvalumab | 0.733 | 0.733417 | 0.000416535 | no evaluable |
| S_36_IC95_inferior | SG | durvalumab | 0.5 | 0.499178 | -0.000821633 | no evaluable |
| S_36_IC95_superior | SG | durvalumab | 0.625 | 0.62456 | -0.000439541 | no evaluable |
| seguimiento_censurados_mediana | SG | durvalumab | 37.2 | 37.2273 | 0.0272727 | no evaluable |
| seguimiento_censurados_minimo | SG | durvalumab | 0.1 | 1 | 0.9 | no evaluable |
| seguimiento_censurados_maximo | SG | durvalumab | 60.2 | 60.2044 | 0.00443181 | no evaluable |
| mediana_IC95_inferior | SG | placebo | 25.5 | 25.5337 | 0.033722 | no evaluable |
| mediana_IC95_superior | SG | placebo | 39.9 | 39.9207 | 0.0207268 | no evaluable |
| S_24_IC95_inferior | SG | placebo | 0.523 | 0.522422 | -0.000577991 | no evaluable |
| S_24_IC95_superior | SG | placebo | 0.643 | 0.64199 | -0.00100955 | no evaluable |
| S_36_IC95_inferior | SG | placebo | 0.413 | 0.412498 | -0.000502425 | no evaluable |
| S_36_IC95_superior | SG | placebo | 0.537 | 0.537145 | 0.0001452 | no evaluable |
| seguimiento_censurados_mediana | SG | placebo | 37.2 | 37.5 | 0.3 | no evaluable |
| seguimiento_censurados_minimo | SG | placebo | 0.7 | 0.5 | -0.2 | no evaluable |
| seguimiento_censurados_maximo | SG | placebo | 60.9 | 60.9533 | 0.0532813 | no evaluable |
| mediana_IC95_inferior | SLP | durvalumab | 10.2 | 10.1634 | -0.0366371 | no evaluable |
| mediana_IC95_superior | SLP | durvalumab | 28.2 | 28.2129 | 0.0128824 | no evaluable |
| S_18_IC95_inferior | SLP | durvalumab | 0.422 | 0.424955 | 0.00295522 | no evaluable |
| S_18_IC95_superior | SLP | durvalumab | 0.55 | 0.552877 | 0.00287701 | no evaluable |
| S_24_IC95_inferior | SLP | durvalumab | 0.396 | 0.393963 | -0.00203654 | no evaluable |
| S_24_IC95_superior | SLP | durvalumab | 0.525 | 0.522927 | -0.00207327 | no evaluable |
| seguimiento_censurados_mediana | SLP | durvalumab | 27.4 | 27.6875 | 0.2875 | no evaluable |
| seguimiento_censurados_minimo | SLP | durvalumab | 0 | 0.3 | 0.3 | no evaluable |
| seguimiento_censurados_maximo | SLP | durvalumab | 55.4 | 55.3627 | -0.0373037 | no evaluable |
| mediana_IC95_inferior | SLP | placebo | 7.4 | 7.25599 | -0.14401 | no evaluable |
| mediana_IC95_superior | SLP | placebo | 12.9 | 12.9388 | 0.0387874 | no evaluable |
| S_18_IC95_inferior | SLP | placebo | 0.299 | 0.299831 | 0.000831236 | no evaluable |
| S_18_IC95_superior | SLP | placebo | 0.422 | 0.422302 | 0.00030153 | no evaluable |
| S_24_IC95_inferior | SLP | placebo | 0.282 | 0.282319 | 0.000318751 | no evaluable |
| S_24_IC95_superior | SLP | placebo | 0.403 | 0.403661 | 0.000661125 | no evaluable |
| seguimiento_censurados_mediana | SLP | placebo | 27.7 | 29 | 1.3 | no evaluable |
| seguimiento_censurados_minimo | SLP | placebo | 0 | 0.230769 | 0.230769 | no evaluable |
| seguimiento_censurados_maximo | SLP | placebo | 55.8 | 55.8181 | 0.0181075 | no evaluable |
| HR_IC95_inferior | SG | D vs P | 0.57 | 0.571894 | 0.00189374 | no evaluable |
| HR_IC95_superior | SG | D vs P | 0.93 | 0.932481 | 0.00248133 | no evaluable |
| PH_p_rank | SG | D vs P | 0.91 | 0.944967 | 0.034967 | no evaluable |
| HR_IC95_inferior | SLP | D vs P | 0.61 | 0.615546 | 0.00554571 | no evaluable |
| HR_IC95_superior | SLP | D vs P | 0.95 | 0.963692 | 0.0136922 | no evaluable |
| PH_p_rank | SLP | D vs P | 0.79 | 0.85222 | 0.0622202 | no evaluable |

## E2.0: validación con verdad conocida

100 réplicas completas, cada una con ambos desenlaces y dos brazos: 400 reconstrucciones. Semillas 20261010–20261109. Tamaños 264/266 según D04 pp.6/8. Masa de evento por categorías mensuales, jitter y censura administrativa/temprana fijados como **supuestos de software**, no como datos del ensayo; valores completos en configuración. No se ajustó distribución paramétrica. Se conservaron verdad, pseudo-IPD y auditoría de intervalos para cada réplica. Las tasas de censoring pueden contrastarse en la tabla de poblaciones. El análisis compara estadísticas del KM/Cox verdadero de cada réplica con las del reconstruido, no con un HR generador.

| endpoint | quantity | total | evaluable | not_evaluable | both_not_reached | bias | mae | p95_absolute | max_absolute | within_tolerance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SG | HR | 100 | 100 | 0 | 0 | 0.000268298 | 0.00123106 | 0.00316746 | 0.00608341 | 100 |
| SG | S_24 | 200 | 200 | 0 | 0 | 6.87411e-06 | 0.000169222 | 0.000414088 | 0.000610159 | 200 |
| SG | S_36 | 200 | 200 | 0 | 0 | 6.27911e-05 | 0.000528411 | 0.00136708 | 0.00195562 | 200 |
| SG | eventos_totales | 200 | 200 | 0 | 0 | 0.03 | 0.03 | 0 | 2 | 200 |
| SG | mediana | 200 | 200 | 0 | 0 | 0.0121872 | 0.0613809 | 0.246254 | 2.1043 | 200 |
| SLP | HR | 100 | 100 | 0 | 0 | 1.77086e-06 | 0.000887717 | 0.00202138 | 0.00435177 | 100 |
| SLP | S_18 | 200 | 200 | 0 | 0 | -4.85823e-06 | 0.000245223 | 0.000669823 | 0.000875397 | 200 |
| SLP | S_24 | 200 | 200 | 0 | 0 | 3.07043e-06 | 0.000224685 | 0.000587365 | 0.00084159 | 200 |
| SLP | eventos_totales | 200 | 200 | 0 | 0 | 0.005 | 0.005 | 0 | 1 | 200 |
| SLP | mediana | 200 | 200 | 0 | 0 | 0.00487052 | 0.00505039 | 0 | 0.618078 | 200 |

Evaluable excluye medianas no finitas; `both_not_reached` informa cuando ambas son no alcanzadas. Una mediana no alcanzada no se inventa. Las simulaciones prueban censura/redondeo, pero no reproducen todos los artefactos de digitalización del PDF. El desempeño es condicional al diseño sintético, no garantía universal. Errores fuera de las tolerancias se conservan y no provocaron cambios de método.

Resultado calculado: 1800/1800 comparaciones evaluables dentro de tolerancia; 0 no evaluables. En esta corrida todas las medianas se alcanzaron. Esto no es una prueba de casos de mediana no alcanzada, que se cubren en pruebas unitarias mediante datos completamente censurados.

Fracción censurada simulada por brazo (cálculo de los 100 conjuntos):

| endpoint | arm | mean | min | max |
| --- | --- | --- | --- | --- |
| SG | durvalumab | 0.528939 | 0.450758 | 0.587121 |
| SG | placebo | 0.401316 | 0.342105 | 0.473684 |
| SLP | durvalumab | 0.327992 | 0.272727 | 0.371212 |
| SLP | placebo | 0.232444 | 0.172932 | 0.296992 |

El diseño aproxima el tamaño y calendario de riesgo del ensayo, pero no iguala su fracción de censura por brazo, especialmente en SLP. Por ello E2.0 no es una calibración exacta a la censura de ADRIATIC. No se ajustaron las masas sintéticas después de observar este resultado. Máxima diferencia absoluta de riesgo simulado: 0 sujetos.

## Problemas abiertos y limitaciones

1. SLP durvalumab: 140 eventos reconstruidos frente a 139 publicados; no se ha forzado coincidencia retroactiva. Requiere revisión de la adaptación del algoritmo y del límite de redondeo, aunque satisface el umbral contractual.
2. Tres controles de riesgo con -1 sujeto; no hay diferencia >1. Distribución intraintervalo de censuras no identificable, especialmente en tiempos cercanos a cero y en la cola.
3. Mediana SG-D depende de muy pocos sujetos en riesgo (D04 §6, tabla de riesgo PDF p.6). Los IC de pseudo-IPD no incluyen error de extracción/reconstrucción ni sustituyen incertidumbre clínica original.
4. No se cuenta con covariables de estratificación ni suplemento. HR/PH no estratificados y seguimiento son aproximaciones, no reproducción del modelo ajustado original.
5. Revisión independiente del coordinador pendiente; no se declara aceptación. Las pruebas unitarias y de integración se registran aparte.
6. E2.0 se ejecutó después de la primera validación clínica, a diferencia del orden enumerado en el contrato; no se presenta como validación cegada. La corrida parcial interrumpida de E2.0 no se archivó íntegramente antes del relanzamiento: se conservan código y stdout, no todos sus CSV originales. Las corridas clínicas originales sí están archivadas.

## Reproducibilidad y archivos

Comandos absolutos en `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\REPRODUCIR.md`. Fuentes no modificadas, un solo hilo numérico y ejecuciones registradas con versión, fecha, duración, semillas y hashes. La corrida E2.0 síncrona inicial quedó interrumpida por el límite de herramienta y se relanzó sin cambios de diseño; véase registro de incidencias.

Resultados CSV en `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\data_derived`; figuras PNG/SVG en `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\figures`; código en `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\src`; pruebas en `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\tests`. Cada evaluación clínica conserva copia en logs. Solo el archivo de comunicaciones permitido se escribe fuera del directorio exclusivo.


## Ronda 1 de corrección

Fecha de corrección: 11-oct-2026 (hora local de inicio). Estado: entregada (ronda 1). Pendiente de revisión del coordinador.

Se conserva arriba el informe original íntegro. La auditoría T04 detectó D1 (mesetas fusionadas) y D2 (E2.0 sin extracción). Los resultados vigentes son los corregidos que siguen. No se cambiaron Guyot, semillas, diseño, configuración ni tolerancias. No se optimizó contra estadísticas publicadas.

Copia original verificada: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\logs\ronda0_original`; manifiesto `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\logs\ronda0_original_sha256.csv`. Código/documentos originales: `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\logs\ronda0_documentos`.

### D1: método y resultados originales primero

Se emparejan bordes horizontales opuestos separados aproximadamente 0,502 pt, sin filtro de grosor de franja ni mínimo de longitud de meseta. Se incluyen segmentos con desnivel de 0,001 pt por precisión del PDF. Las mesetas cortas pueden tener bordes no solapados. Se guardan los segmentos de cada pareja, y se exige unicidad y continuidad. La calibración textual, elección de contorno y marcas permanecen iguales. Justificación fechada en DECISIONES_METODO.md.

#### Resultado original

**18 cantidades H1** (tasas en probabilidad, no porcentaje):

| quantity | endpoint | arm | published | reconstructed | difference | tolerance | classification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| eventos_totales | SG | durvalumab | 115 | 115 | 0 | 3.45 | reproducido |
| mediana | SG | durvalumab | 55.9 | 55.9368 | 0.0367647 | 3 | reproducido |
| S_24 | SG | durvalumab | 0.68 | 0.680036 | 3.62833e-05 | 0.02 | reproducido |
| S_36 | SG | durvalumab | 0.565 | 0.564465 | -0.000535135 | 0.02 | reproducido |
| eventos_totales | SG | placebo | 146 | 146 | 0 | 4.38 | reproducido |
| mediana | SG | placebo | 33.4 | 33.3875 | -0.0124813 | 1 | reproducido |
| S_24 | SG | placebo | 0.585 | 0.584837 | -0.000163134 | 0.02 | reproducido |
| S_36 | SG | placebo | 0.476 | 0.476232 | 0.000231855 | 0.02 | reproducido |
| eventos_totales | SLP | durvalumab | 139 | 140 | 1 | 4.17 | reproducido |
| mediana | SLP | durvalumab | 16.6 | 16.5446 | -0.0553517 | 1 | reproducido |
| S_18 | SLP | durvalumab | 0.488 | 0.490592 | 0.00259194 | 0.02 | reproducido |
| S_24 | SLP | durvalumab | 0.462 | 0.459732 | -0.00226804 | 0.02 | reproducido |
| eventos_totales | SLP | placebo | 169 | 169 | 0 | 5.07 | reproducido |
| mediana | SLP | placebo | 9.2 | 9.08767 | -0.112329 | 1 | reproducido |
| S_18 | SLP | placebo | 0.361 | 0.360957 | -4.27971e-05 | 0.02 | reproducido |
| S_24 | SLP | placebo | 0.342 | 0.34262 | 0.000619968 | 0.02 | reproducido |
| HR | SG | D vs P | 0.73 | 0.73026 | 0.000260385 | 0.03 | reproducido |
| HR | SLP | D vs P | 0.76 | 0.770193 | 0.0101926 | 0.03 | reproducido |

**Empates y tiempos distintos**: event_times son tiempos distintos de evento; all_times incluyen censuras.

| version | endpoint | arm | plateaus | events | max_tie | distinct_event_times | distinct_all_times | times_with_at_least_5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| original | SG | durvalumab | 73 | 115 | 5 | 72 | 221 | 1 |
| original | SG | placebo | 81 | 146 | 6 | 80 | 200 | 4 |
| original | SLP | durvalumab | 45 | 140 | 31 | 40 | 161 | 6 |
| original | SLP | placebo | 50 | 169 | 34 | 49 | 142 | 5 |

**HR no estratificada Efron/Breslow**, sin nueva tolerancia; score Efron se contrasta con lifelines:

| version | endpoint | efron_lifelines | efron_score | breslow_score |
| --- | --- | --- | --- | --- |
| original | SG | 0.73026 | 0.73026 | 0.731158 |
| original | SLP | 0.770193 | 0.770193 | 0.775103 |

**88 números en riesgo**, con diferencia en cada tiempo (restricciones de entrada, no validación independiente):

| quantity | endpoint | arm | published | reconstructed | difference | tolerance | classification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| riesgo_0 | SG | durvalumab | 264 | 264 | 0 | — | reproducido |
| riesgo_3 | SG | durvalumab | 261 | 261 | 0 | — | reproducido |
| riesgo_6 | SG | durvalumab | 248 | 248 | 0 | — | reproducido |
| riesgo_9 | SG | durvalumab | 236 | 236 | 0 | — | reproducido |
| riesgo_12 | SG | durvalumab | 223 | 223 | 0 | — | reproducido |
| riesgo_15 | SG | durvalumab | 207 | 207 | 0 | — | reproducido |
| riesgo_18 | SG | durvalumab | 189 | 189 | 0 | — | reproducido |
| riesgo_21 | SG | durvalumab | 183 | 183 | 0 | — | reproducido |
| riesgo_24 | SG | durvalumab | 172 | 171 | -1 | — | parcialmente reproducido |
| riesgo_27 | SG | durvalumab | 162 | 161 | -1 | — | parcialmente reproducido |
| riesgo_30 | SG | durvalumab | 141 | 141 | 0 | — | reproducido |
| riesgo_33 | SG | durvalumab | 110 | 110 | 0 | — | reproducido |
| riesgo_36 | SG | durvalumab | 90 | 90 | 0 | — | reproducido |
| riesgo_39 | SG | durvalumab | 68 | 68 | 0 | — | reproducido |
| riesgo_42 | SG | durvalumab | 51 | 51 | 0 | — | reproducido |
| riesgo_45 | SG | durvalumab | 39 | 39 | 0 | — | reproducido |
| riesgo_48 | SG | durvalumab | 27 | 27 | 0 | — | reproducido |
| riesgo_51 | SG | durvalumab | 19 | 19 | 0 | — | reproducido |
| riesgo_54 | SG | durvalumab | 11 | 11 | 0 | — | reproducido |
| riesgo_57 | SG | durvalumab | 5 | 5 | 0 | — | reproducido |
| riesgo_60 | SG | durvalumab | 1 | 1 | 0 | — | reproducido |
| riesgo_63 | SG | durvalumab | 0 | 0 | 0 | — | reproducido |
| riesgo_0 | SG | placebo | 266 | 266 | 0 | — | reproducido |
| riesgo_3 | SG | placebo | 260 | 260 | 0 | — | reproducido |
| riesgo_6 | SG | placebo | 247 | 247 | 0 | — | reproducido |
| riesgo_9 | SG | placebo | 231 | 231 | 0 | — | reproducido |
| riesgo_12 | SG | placebo | 214 | 214 | 0 | — | reproducido |
| riesgo_15 | SG | placebo | 195 | 194 | -1 | — | parcialmente reproducido |
| riesgo_18 | SG | placebo | 175 | 175 | 0 | — | reproducido |
| riesgo_21 | SG | placebo | 164 | 164 | 0 | — | reproducido |
| riesgo_24 | SG | placebo | 151 | 151 | 0 | — | reproducido |
| riesgo_27 | SG | placebo | 143 | 143 | 0 | — | reproducido |
| riesgo_30 | SG | placebo | 123 | 123 | 0 | — | reproducido |
| riesgo_33 | SG | placebo | 97 | 97 | 0 | — | reproducido |
| riesgo_36 | SG | placebo | 80 | 80 | 0 | — | reproducido |
| riesgo_39 | SG | placebo | 62 | 62 | 0 | — | reproducido |
| riesgo_42 | SG | placebo | 44 | 44 | 0 | — | reproducido |
| riesgo_45 | SG | placebo | 31 | 31 | 0 | — | reproducido |
| riesgo_48 | SG | placebo | 23 | 23 | 0 | — | reproducido |
| riesgo_51 | SG | placebo | 19 | 19 | 0 | — | reproducido |
| riesgo_54 | SG | placebo | 8 | 8 | 0 | — | reproducido |
| riesgo_57 | SG | placebo | 5 | 5 | 0 | — | reproducido |
| riesgo_60 | SG | placebo | 1 | 1 | 0 | — | reproducido |
| riesgo_63 | SG | placebo | 0 | 0 | 0 | — | reproducido |
| riesgo_0 | SLP | durvalumab | 264 | 264 | 0 | — | reproducido |
| riesgo_3 | SLP | durvalumab | 212 | 212 | 0 | — | reproducido |
| riesgo_6 | SLP | durvalumab | 161 | 161 | 0 | — | reproducido |
| riesgo_9 | SLP | durvalumab | 135 | 135 | 0 | — | reproducido |
| riesgo_12 | SLP | durvalumab | 113 | 113 | 0 | — | reproducido |
| riesgo_15 | SLP | durvalumab | 105 | 105 | 0 | — | reproducido |
| riesgo_18 | SLP | durvalumab | 101 | 101 | 0 | — | reproducido |
| riesgo_21 | SLP | durvalumab | 98 | 98 | 0 | — | reproducido |
| riesgo_24 | SLP | durvalumab | 84 | 84 | 0 | — | reproducido |
| riesgo_27 | SLP | durvalumab | 78 | 78 | 0 | — | reproducido |
| riesgo_30 | SLP | durvalumab | 51 | 51 | 0 | — | reproducido |
| riesgo_33 | SLP | durvalumab | 51 | 51 | 0 | — | reproducido |
| riesgo_36 | SLP | durvalumab | 33 | 33 | 0 | — | reproducido |
| riesgo_39 | SLP | durvalumab | 21 | 21 | 0 | — | reproducido |
| riesgo_42 | SLP | durvalumab | 19 | 19 | 0 | — | reproducido |
| riesgo_45 | SLP | durvalumab | 10 | 10 | 0 | — | reproducido |
| riesgo_48 | SLP | durvalumab | 10 | 10 | 0 | — | reproducido |
| riesgo_51 | SLP | durvalumab | 4 | 4 | 0 | — | reproducido |
| riesgo_54 | SLP | durvalumab | 4 | 4 | 0 | — | reproducido |
| riesgo_57 | SLP | durvalumab | 0 | 0 | 0 | — | reproducido |
| riesgo_60 | SLP | durvalumab | 0 | 0 | 0 | — | reproducido |
| riesgo_63 | SLP | durvalumab | 0 | 0 | 0 | — | reproducido |
| riesgo_0 | SLP | placebo | 266 | 266 | 0 | — | reproducido |
| riesgo_3 | SLP | placebo | 208 | 208 | 0 | — | reproducido |
| riesgo_6 | SLP | placebo | 146 | 146 | 0 | — | reproducido |
| riesgo_9 | SLP | placebo | 122 | 122 | 0 | — | reproducido |
| riesgo_12 | SLP | placebo | 100 | 100 | 0 | — | reproducido |
| riesgo_15 | SLP | placebo | 88 | 88 | 0 | — | reproducido |
| riesgo_18 | SLP | placebo | 79 | 79 | 0 | — | reproducido |
| riesgo_21 | SLP | placebo | 76 | 76 | 0 | — | reproducido |
| riesgo_24 | SLP | placebo | 71 | 71 | 0 | — | reproducido |
| riesgo_27 | SLP | placebo | 69 | 69 | 0 | — | reproducido |
| riesgo_30 | SLP | placebo | 47 | 47 | 0 | — | reproducido |
| riesgo_33 | SLP | placebo | 47 | 47 | 0 | — | reproducido |
| riesgo_36 | SLP | placebo | 34 | 34 | 0 | — | reproducido |
| riesgo_39 | SLP | placebo | 23 | 23 | 0 | — | reproducido |
| riesgo_42 | SLP | placebo | 22 | 22 | 0 | — | reproducido |
| riesgo_45 | SLP | placebo | 15 | 15 | 0 | — | reproducido |
| riesgo_48 | SLP | placebo | 14 | 14 | 0 | — | reproducido |
| riesgo_51 | SLP | placebo | 5 | 5 | 0 | — | reproducido |
| riesgo_54 | SLP | placebo | 5 | 5 | 0 | — | reproducido |
| riesgo_57 | SLP | placebo | 0 | 0 | 0 | — | reproducido |
| riesgo_60 | SLP | placebo | 0 | 0 | 0 | — | reproducido |
| riesgo_63 | SLP | placebo | 0 | 0 | 0 | — | reproducido |
#### Resultado corregido

**18 cantidades H1** (tasas en probabilidad, no porcentaje):

| quantity | endpoint | arm | published | reconstructed | difference | tolerance | classification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| eventos_totales | SG | durvalumab | 115 | 115 | 0 | 3.45 | reproducido |
| mediana | SG | durvalumab | 55.9 | 55.9368 | 0.0367638 | 3 | reproducido |
| S_24 | SG | durvalumab | 0.68 | 0.68022 | 0.000220431 | 0.02 | reproducido |
| S_36 | SG | durvalumab | 0.565 | 0.564953 | -4.74342e-05 | 0.02 | reproducido |
| eventos_totales | SG | placebo | 146 | 146 | 0 | 4.38 | reproducido |
| mediana | SG | placebo | 33.4 | 33.3875 | -0.0124813 | 1 | reproducido |
| S_24 | SG | placebo | 0.585 | 0.585396 | 0.000395778 | 0.02 | reproducido |
| S_36 | SG | placebo | 0.476 | 0.476687 | 0.000686976 | 0.02 | reproducido |
| eventos_totales | SLP | durvalumab | 139 | 140 | 1 | 4.17 | reproducido |
| mediana | SLP | durvalumab | 16.6 | 16.5446 | -0.0553526 | 1 | reproducido |
| S_18 | SLP | durvalumab | 0.488 | 0.489575 | 0.00157458 | 0.02 | reproducido |
| S_24 | SLP | durvalumab | 0.462 | 0.463947 | 0.00194728 | 0.02 | reproducido |
| eventos_totales | SLP | placebo | 169 | 170 | 1 | 5.07 | reproducido |
| mediana | SLP | placebo | 9.2 | 9.18209 | -0.0179052 | 1 | reproducido |
| S_18 | SLP | placebo | 0.361 | 0.361439 | 0.000439424 | 0.02 | reproducido |
| S_24 | SLP | placebo | 0.342 | 0.343078 | 0.00107769 | 0.02 | reproducido |
| HR | SG | D vs P | 0.73 | 0.730295 | 0.00029548 | 0.03 | reproducido |
| HR | SLP | D vs P | 0.76 | 0.771465 | 0.0114654 | 0.03 | reproducido |

**Empates y tiempos distintos**: event_times son tiempos distintos de evento; all_times incluyen censuras.

| version | endpoint | arm | plateaus | events | max_tie | distinct_event_times | distinct_all_times | times_with_at_least_5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| corregido | SG | durvalumab | 109 | 115 | 3 | 108 | 257 | 0 |
| corregido | SG | placebo | 133 | 146 | 2 | 132 | 252 | 0 |
| corregido | SLP | durvalumab | 90 | 140 | 6 | 88 | 209 | 5 |
| corregido | SLP | placebo | 101 | 170 | 9 | 100 | 192 | 4 |

**HR no estratificada Efron/Breslow**, sin nueva tolerancia; score Efron se contrasta con lifelines:

| version | endpoint | efron_lifelines | efron_score | breslow_score |
| --- | --- | --- | --- | --- |
| corregido | SG | 0.730295 | 0.730295 | 0.730446 |
| corregido | SLP | 0.771465 | 0.771465 | 0.772303 |

**88 números en riesgo**, con diferencia en cada tiempo (restricciones de entrada, no validación independiente):

| quantity | endpoint | arm | published | reconstructed | difference | tolerance | classification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| riesgo_0 | SG | durvalumab | 264 | 264 | 0 | — | reproducido |
| riesgo_3 | SG | durvalumab | 261 | 261 | 0 | — | reproducido |
| riesgo_6 | SG | durvalumab | 248 | 248 | 0 | — | reproducido |
| riesgo_9 | SG | durvalumab | 236 | 236 | 0 | — | reproducido |
| riesgo_12 | SG | durvalumab | 223 | 223 | 0 | — | reproducido |
| riesgo_15 | SG | durvalumab | 207 | 207 | 0 | — | reproducido |
| riesgo_18 | SG | durvalumab | 189 | 189 | 0 | — | reproducido |
| riesgo_21 | SG | durvalumab | 183 | 183 | 0 | — | reproducido |
| riesgo_24 | SG | durvalumab | 172 | 172 | 0 | — | reproducido |
| riesgo_27 | SG | durvalumab | 162 | 162 | 0 | — | reproducido |
| riesgo_30 | SG | durvalumab | 141 | 141 | 0 | — | reproducido |
| riesgo_33 | SG | durvalumab | 110 | 110 | 0 | — | reproducido |
| riesgo_36 | SG | durvalumab | 90 | 90 | 0 | — | reproducido |
| riesgo_39 | SG | durvalumab | 68 | 68 | 0 | — | reproducido |
| riesgo_42 | SG | durvalumab | 51 | 51 | 0 | — | reproducido |
| riesgo_45 | SG | durvalumab | 39 | 39 | 0 | — | reproducido |
| riesgo_48 | SG | durvalumab | 27 | 27 | 0 | — | reproducido |
| riesgo_51 | SG | durvalumab | 19 | 19 | 0 | — | reproducido |
| riesgo_54 | SG | durvalumab | 11 | 11 | 0 | — | reproducido |
| riesgo_57 | SG | durvalumab | 5 | 5 | 0 | — | reproducido |
| riesgo_60 | SG | durvalumab | 1 | 1 | 0 | — | reproducido |
| riesgo_63 | SG | durvalumab | 0 | 0 | 0 | — | reproducido |
| riesgo_0 | SG | placebo | 266 | 266 | 0 | — | reproducido |
| riesgo_3 | SG | placebo | 260 | 260 | 0 | — | reproducido |
| riesgo_6 | SG | placebo | 247 | 247 | 0 | — | reproducido |
| riesgo_9 | SG | placebo | 231 | 231 | 0 | — | reproducido |
| riesgo_12 | SG | placebo | 214 | 214 | 0 | — | reproducido |
| riesgo_15 | SG | placebo | 195 | 195 | 0 | — | reproducido |
| riesgo_18 | SG | placebo | 175 | 175 | 0 | — | reproducido |
| riesgo_21 | SG | placebo | 164 | 164 | 0 | — | reproducido |
| riesgo_24 | SG | placebo | 151 | 151 | 0 | — | reproducido |
| riesgo_27 | SG | placebo | 143 | 143 | 0 | — | reproducido |
| riesgo_30 | SG | placebo | 123 | 123 | 0 | — | reproducido |
| riesgo_33 | SG | placebo | 97 | 97 | 0 | — | reproducido |
| riesgo_36 | SG | placebo | 80 | 80 | 0 | — | reproducido |
| riesgo_39 | SG | placebo | 62 | 62 | 0 | — | reproducido |
| riesgo_42 | SG | placebo | 44 | 44 | 0 | — | reproducido |
| riesgo_45 | SG | placebo | 31 | 31 | 0 | — | reproducido |
| riesgo_48 | SG | placebo | 23 | 23 | 0 | — | reproducido |
| riesgo_51 | SG | placebo | 19 | 19 | 0 | — | reproducido |
| riesgo_54 | SG | placebo | 8 | 8 | 0 | — | reproducido |
| riesgo_57 | SG | placebo | 5 | 5 | 0 | — | reproducido |
| riesgo_60 | SG | placebo | 1 | 1 | 0 | — | reproducido |
| riesgo_63 | SG | placebo | 0 | 0 | 0 | — | reproducido |
| riesgo_0 | SLP | durvalumab | 264 | 264 | 0 | — | reproducido |
| riesgo_3 | SLP | durvalumab | 212 | 212 | 0 | — | reproducido |
| riesgo_6 | SLP | durvalumab | 161 | 161 | 0 | — | reproducido |
| riesgo_9 | SLP | durvalumab | 135 | 135 | 0 | — | reproducido |
| riesgo_12 | SLP | durvalumab | 113 | 113 | 0 | — | reproducido |
| riesgo_15 | SLP | durvalumab | 105 | 105 | 0 | — | reproducido |
| riesgo_18 | SLP | durvalumab | 101 | 101 | 0 | — | reproducido |
| riesgo_21 | SLP | durvalumab | 98 | 98 | 0 | — | reproducido |
| riesgo_24 | SLP | durvalumab | 84 | 84 | 0 | — | reproducido |
| riesgo_27 | SLP | durvalumab | 78 | 78 | 0 | — | reproducido |
| riesgo_30 | SLP | durvalumab | 51 | 51 | 0 | — | reproducido |
| riesgo_33 | SLP | durvalumab | 51 | 51 | 0 | — | reproducido |
| riesgo_36 | SLP | durvalumab | 33 | 33 | 0 | — | reproducido |
| riesgo_39 | SLP | durvalumab | 21 | 21 | 0 | — | reproducido |
| riesgo_42 | SLP | durvalumab | 19 | 19 | 0 | — | reproducido |
| riesgo_45 | SLP | durvalumab | 10 | 10 | 0 | — | reproducido |
| riesgo_48 | SLP | durvalumab | 10 | 10 | 0 | — | reproducido |
| riesgo_51 | SLP | durvalumab | 4 | 4 | 0 | — | reproducido |
| riesgo_54 | SLP | durvalumab | 4 | 4 | 0 | — | reproducido |
| riesgo_57 | SLP | durvalumab | 0 | 0 | 0 | — | reproducido |
| riesgo_60 | SLP | durvalumab | 0 | 0 | 0 | — | reproducido |
| riesgo_63 | SLP | durvalumab | 0 | 0 | 0 | — | reproducido |
| riesgo_0 | SLP | placebo | 266 | 266 | 0 | — | reproducido |
| riesgo_3 | SLP | placebo | 208 | 208 | 0 | — | reproducido |
| riesgo_6 | SLP | placebo | 146 | 146 | 0 | — | reproducido |
| riesgo_9 | SLP | placebo | 122 | 122 | 0 | — | reproducido |
| riesgo_12 | SLP | placebo | 100 | 100 | 0 | — | reproducido |
| riesgo_15 | SLP | placebo | 88 | 88 | 0 | — | reproducido |
| riesgo_18 | SLP | placebo | 79 | 79 | 0 | — | reproducido |
| riesgo_21 | SLP | placebo | 76 | 76 | 0 | — | reproducido |
| riesgo_24 | SLP | placebo | 71 | 71 | 0 | — | reproducido |
| riesgo_27 | SLP | placebo | 69 | 69 | 0 | — | reproducido |
| riesgo_30 | SLP | placebo | 47 | 47 | 0 | — | reproducido |
| riesgo_33 | SLP | placebo | 47 | 47 | 0 | — | reproducido |
| riesgo_36 | SLP | placebo | 34 | 34 | 0 | — | reproducido |
| riesgo_39 | SLP | placebo | 23 | 23 | 0 | — | reproducido |
| riesgo_42 | SLP | placebo | 22 | 22 | 0 | — | reproducido |
| riesgo_45 | SLP | placebo | 15 | 15 | 0 | — | reproducido |
| riesgo_48 | SLP | placebo | 14 | 14 | 0 | — | reproducido |
| riesgo_51 | SLP | placebo | 5 | 5 | 0 | — | reproducido |
| riesgo_54 | SLP | placebo | 5 | 5 | 0 | — | reproducido |
| riesgo_57 | SLP | placebo | 0 | 0 | 0 | — | reproducido |
| riesgo_60 | SLP | placebo | 0 | 0 | 0 | — | reproducido |
| riesgo_63 | SLP | placebo | 0 | 0 | 0 | — | reproducido |

#### Comprobación de mesetas corregidas

| curva | paired_horizontal_levels | points | support_end | unique_marks |
| --- | --- | --- | --- | --- |
| SG_durvalumab | 109 | 110 | 60.2044 | 133 |
| SG_placebo | 133 | 134 | 60.9533 | 107 |
| SLP_durvalumab | 90 | 91 | 55.3627 | 96 |
| SLP_placebo | 101 | 102 | 55.8181 | 77 |

El número de puntos incluye un punto adicional de fin de soporte. La prueba cuenta de forma independiente los pares de niveles horizontales y compara las ordenadas una a una con las mesetas extraídas; además recalcula el empate máximo y los tiempos distintos de cada pseudo-IPD. Un empate residual no identifica eventos originales: persisten redondeo de curva e inversión KM.


#### Errores de curva corregida

| endpoint | arm | max_absolute | mean_absolute | grid_months | grid_n | support_end |
| --- | --- | --- | --- | --- | --- | --- |
| SG | durvalumab | 0.00866088 | 0.00107749 | 0.1 | 603 | 60.2044 |
| SG | placebo | 0.00415459 | 0.00154749 | 0.1 | 610 | 60.9533 |
| SLP | durvalumab | 0.00901819 | 0.00306199 | 0.1 | 554 | 55.3627 |
| SLP | placebo | 0.00326925 | 0.00199606 | 0.1 | 559 | 55.8181 |

### D2: E2.0a: sin digitalización (original)

100 réplicas, 400 reconstrucciones, semillas 20261010–20261109. Se conserva la simulación original y se reejecuta sin cambiar su código; se comprueba identidad con la copia de ronda 0.

| endpoint | quantity | total | evaluable | not_evaluable | both_not_reached | bias | mae | p95_absolute | max_absolute | within_tolerance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SG | HR | 100 | 100 | 0 | 0 | 0.000268298 | 0.00123106 | 0.00316746 | 0.00608341 | 100 |
| SG | S_24 | 200 | 200 | 0 | 0 | 6.87411e-06 | 0.000169222 | 0.000414088 | 0.000610159 | 200 |
| SG | S_36 | 200 | 200 | 0 | 0 | 6.27911e-05 | 0.000528411 | 0.00136708 | 0.00195562 | 200 |
| SG | eventos_totales | 200 | 200 | 0 | 0 | 0.03 | 0.03 | 0 | 2 | 200 |
| SG | mediana | 200 | 200 | 0 | 0 | 0.0121872 | 0.0613809 | 0.246254 | 2.1043 | 200 |
| SLP | HR | 100 | 100 | 0 | 0 | 1.77086e-06 | 0.000887717 | 0.00202138 | 0.00435177 | 100 |
| SLP | S_18 | 200 | 200 | 0 | 0 | -4.85823e-06 | 0.000245223 | 0.000669823 | 0.000875397 | 200 |
| SLP | S_24 | 200 | 200 | 0 | 0 | 3.07043e-06 | 0.000224685 | 0.000587365 | 0.00084159 | 200 |
| SLP | eventos_totales | 200 | 200 | 0 | 0 | 0.005 | 0.005 | 0 | 1 | 200 |
| SLP | mediana | 200 | 200 | 0 | 0 | 0.00487052 | 0.00505039 | 0 | 0.618078 | 200 |

Error máximo de riesgo E2.0a: 0 sujetos.


### D2: E2.0b: con extracción vectorial (corregido)

100 réplicas completas, 400 reconstrucciones y 1800 comparaciones; **no se redujo a 20 réplicas**. Mismas semillas y poblaciones verdaderas que E2.0a. Cada par KM se dibuja en un PDF reabierto por extract_pdf: escala y posiciones textuales de Fig.1A, polígonos rellenos de 0,502 pt, colores de brazos, marcas de censura rectangulares 0,502 ×5 pt y riesgo. No se pasan coordenadas KM exactas a reconstruct.

| endpoint | quantity | total | evaluable | not_evaluable | both_not_reached | bias | mae | p95_absolute | max_absolute | within_tolerance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SG | HR | 100 | 100 | 0 | 0 | 0.000422701 | 0.00134336 | 0.00366587 | 0.00894599 | 100 |
| SG | S_24 | 200 | 200 | 0 | 0 | 6.87411e-06 | 0.000169222 | 0.000414088 | 0.000610159 | 200 |
| SG | S_36 | 200 | 200 | 0 | 0 | 6.27911e-05 | 0.000528411 | 0.00136708 | 0.00195562 | 200 |
| SG | eventos_totales | 200 | 200 | 0 | 0 | 0.02 | 0.04 | 0 | 2 | 200 |
| SG | mediana | 200 | 200 | 0 | 0 | 0.0121878 | 0.0613827 | 0.246252 | 2.1043 | 200 |
| SLP | HR | 100 | 100 | 0 | 0 | 1.54123e-06 | 0.000887487 | 0.00202138 | 0.00435177 | 100 |
| SLP | S_18 | 200 | 200 | 0 | 0 | -4.85823e-06 | 0.000245223 | 0.000669823 | 0.000875397 | 200 |
| SLP | S_24 | 200 | 200 | 0 | 0 | 3.07043e-06 | 0.000224685 | 0.000587365 | 0.00084159 | 200 |
| SLP | eventos_totales | 200 | 200 | 0 | 0 | 0.005 | 0.005 | 0 | 1 | 200 |
| SLP | mediana | 200 | 200 | 0 | 0 | 0.00487094 | 0.00505212 | 5.61851e-06 | 0.618079 | 200 |

Resultado E2.0b: 1800/1800 evaluables dentro de las tolerancias originales; 0 no evaluables. Las discrepancias se conservan sin reajustes.

| endpoint | arm | reconstructions | max_risk_error | mean_risk_error | max_tie | true_max_tie | extraction_max_absolute | extraction_mean_absolute |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SG | durvalumab | 100 | 0 | 0 | 3 | 1 | 0.00749062 | 2.22887e-07 |
| SG | placebo | 100 | 0 | 0 | 2 | 1 | 0.00382034 | 1.62516e-07 |
| SLP | durvalumab | 100 | 0 | 0 | 2 | 1 | 0.00378787 | 1.59252e-07 |
| SLP | placebo | 100 | 0 | 0 | 2 | 1 | 3.03733e-07 | 1.00532e-07 |

Los 8.800 controles de riesgo por tiempo se conservan en `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\data_derived\simulation_b_risks.csv`; diferencias >1 sujetos: 0. Riesgo sin tolerancia contractual fija. Empates sin umbral clínico nuevo. Errores de extracción en probabilidad sobre rejilla de 0,1 meses, dentro del soporte común.

Los PDF sintéticos prueban contornos vectoriales y marcas, no ruido ráster ni todos los salientes de unión del editor de ADRIATIC. Se conservan también tiempo/ordenada de cada meseta para distinguir error de coordenadas de error KM. La asignación uniforme de censuras sigue siendo aproximada. E2.0b no garantiza exactitud fuera de este diseño ni recupera los datos originales.

Incidencia conservada: la primera corrida E2.0b falló en la réplica 40 (semilla 20261050), SLP-placebo, por una anchura de meseta de −0,0000076294 pt tras cuantización PDF. Se archivaron todos los derivados parciales antes de aplicar a la anchura el margen geométrico ya declarado de 0,002 pt: colapsar sus extremos en el promedio sin eliminar el nivel. Se añadió regresión con esa semilla y se reejecutaron las 100 réplicas, sin cambios de tolerancias clínicas ni omisiones. Detalle y registro de la corrida fallida en logs/INCIDENCIAS.md y DECISIONES_METODO.md. Esta limitación de resolución puede introducir empates residuales; no se inventan tiempos más precisos que el PDF.


### Estado numérico y limitaciones tras la corrección

- H1 corregido: 18/18 cantidades reproducidas con criterios sin cambios.

- Riesgo corregido: {'reproducido': 88}; desviación máxima 0 sujetos.

- Eventos, como entrada, no son validación independiente; resultados por brazo:

| quantity | endpoint | arm | published | reconstructed | difference | tolerance | classification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| eventos_totales | SG | durvalumab | 115 | 115 | 0 | 3.45 | reproducido |
| eventos_totales | SG | placebo | 146 | 146 | 0 | 4.38 | reproducido |
| eventos_totales | SLP | durvalumab | 139 | 140 | 1 | 4.17 | reproducido |
| eventos_totales | SLP | placebo | 169 | 170 | 1 | 5.07 | reproducido |

- Continúan las limitaciones originales: pseudo-IPD aproximados, censuras no identificables, cola SG-D frágil, ausencia de covariables y PH no directamente equivalente. SG y SLP son reconstrucciones marginales sin enlace entre sujetos. La ronda queda entregada, no aceptada.
