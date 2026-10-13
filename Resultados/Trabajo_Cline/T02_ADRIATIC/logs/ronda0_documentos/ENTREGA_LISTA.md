# Entrega T02

Estado: entregada

Fecha: 10-oct-2026. Pendiente de revisión del coordinador; no aceptada.

## Entregables
- `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\INFORME_T02.md`
- `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\src` y `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\tests`
- `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\config\config.yaml`
- `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\requirements_T02.txt`
- `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\logs`
- `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\data_derived` (coordenadas, pseudo-IPD, validación, simulación, procedencia)
- `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\figures` (PNG + SVG)
- `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\REPRODUCIR.md`
- `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\CRITERIOS_PREESPECIFICADOS.md` y `C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC\DECISIONES_METODO.md`

## Validación
18/18 cantidades H1 reproducidas; criterios contractuales sin cambios.

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

Riesgo: {'reproducido': 85, 'parcialmente reproducido': 3}. E2.0: 100 réplicas, 400 reconstrucciones; métricas completas en informe y CSV. Error de curva máximo global 0.828122 pp.

## Problemas abiertos
SLP-D 140 vs 139 eventos; tres riesgos con -1; revisión de adaptación de Guyot; tiempos individuales no identificables; fragilidad de cola; PH no directamente equivalente al análisis publicado. E2.0: 1800/1800 dentro de tolerancia, sin garantía fuera del diseño sintético. Ninguna corrección orientada a forzar concordancia.
