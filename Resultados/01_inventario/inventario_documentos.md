# Inventario de insumos: `Paper_Cancer/Data_insumo`

**Fecha de inspección:** 10-oct-2026.

**Acceso:** verificado (lectura). Los originales no se modificaron.

**Huellas SHA-256 y conteo de páginas:** `Resultados/00_extraccion_texto/_reporte_extraccion.json`.

**Contenido de la carpeta:** 12 archivos en el nivel raíz, sin subcarpetas.
- 10 PDF de artículos.
- 2 informes Markdown elaborados por nosotros en esta misma sesión (R1, R2).
- No hay datasets, notebooks, código, imágenes sueltas ni suplementos.

**Extracción de texto:** PyMuPDF, por página, con marcas `[p. N]` (`00_extraccion_texto/*.txt`).
- Todas las páginas tienen capa de texto: ninguna con menos de 200 caracteres, así que **no fue necesario OCR**.
- Las ecuaciones, tablas rotadas y figuras se extraen mal en el `.txt`. Por eso los lectores verificaron esas páginas renderizando el PDF a imagen. Cuando las figuras eran vectoriales, también extrajeron las coordenadas de los trazados (detalle en cada ficha).

**Lectura:** cada documento se leyó completo (métodos, resultados, tablas, figuras y anexos incluidos en el PDF) mediante seis lectores delegados. Debían citar ubicaciones con página y marcar `[Lector]` todo cálculo propio.
- Las fichas están en `02_matriz_evidencia/fichas/`.
- El coordinador comprobó contra el texto fuente las cifras críticas:
  - NLST 20,0 % y 247/309.
  - NELSON RR 0,76 y n = 13 195.
  - ADRIATIC: medianas 55,9 y 16,6 meses; IC 98,321 %.
  - Wang: rejilla de 200 × 200 e implementación en C/C++.
  - La serie de volúmenes de D02 frente al CSV público de los autores, con coincidencia exacta.
- Los suplementos de las revistas **no** están en la carpeta y no se leyeron, salvo cuando se indica.

## Tabla de inventario

| ID | Archivo | Referencia | IDs | Tipo | Cáncer / población | Pregunta | Métodos (resumen) | Resultados principales (ubicación) | Limitaciones clave | Datos / código / suplementos | Estado de lectura y problemas |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D01 | `A Multidisciplinary Hyper-Modeling Scheme in Personalized.pdf` (37 pp.) | Kolokotroni E, et al. *J Pers Med* 2024;14:475 | doi:10.3390/jpm14050475 · PMID 38793058 · PMC11122096 | Modelo matemático / simulación (gemelo digital multiescala) | **CPCNP (adenocarcinoma) con RT, n = 1 paciente**, y tumor de Wilms con QT, 2 casos analizados; proyecto CHIC | Acoplar cinética celular (Oncosimulator) con metabolismo, señalización y biomecánica | Hipermodelo discreto en vóxeles, LQ, TCP de Poisson, ODE ErbB (504 especies), red booleana p53, FBA, FEM | TCP mediana 4×10⁻¹²; volumen a 1 año 0,908 mm³ frente a TC sin tumor (ficha D01 §7) | n = 1 en pulmón; validación anecdótica; incoherencias internas (ficha §14) | Datos **ya no accesibles** [p. 29]; código cerrado salvo vasculatura (github.com/jmsgrogan/Chic) [p. 29] | Completo. Verificadas visualmente las pp. 5, 9–12, 14, 15, 18–20, 22, 23 y 30–33 |
| D02 | `A phase-field model for non-small cell lung cancer under the.pdf` (18 pp.) | Fritz M, Kuttler C, Oden JT, Schlicke P, Schumann C, Wagner A, Wohlmuth B. **Preprint arXiv:2303.09378v1** (16-mar-2023) | **Versión publicada:** Wagner A, Schlicke P, Fritz M, et al. *Math Biosci Eng* 2023;20(10):18670–94. doi:10.3934/mbe.2023828 · PMID 38052574. También en bioRxiv, doi:10.1101/2023.03.20.533400 | Modelo matemático (campo de fase Cahn–Hilliard + nutrientes + farmacocinética) con calibración a pacientes | **CPCNP con anti-PD-1, n = 2** (P1 nivolumab; P2 pembrolizumab); estadio no reportado | ¿Describe el modelo la evolución tumoral bajo inmunoterapia? | Modelo 1D radial y 3D (FEniCS); 4 parámetros calibrados a mano por paciente | Ajuste cualitativo; contrafactuales de dosis (ficha D02 §8) | Sin función de pérdida, sin incertidumbre, sin validación externa; inconsistencias (ficha §14) | **El preprint no tiene datos ni código. La versión publicada sí: github.com/wagnandr/immunotherapy-lung-cancer, con CSV de volúmenes de ambos pacientes y código, sin licencia** (ver nota 1) | Completo. Verificadas pp. 3–11 y 13. **Documento superado por la versión publicada:** cambian parámetros (nota 1) |
| D03 | `Applications of lung cancer organoids .pdf` (13 pp.) | Li H, et al. *Cell Commun Signal* 2023;21:350 | doi:10.1186/s12964-023-01332-9 · PMID 38057851 · PMC10698950 | Revisión narrativa | Pulmón (LUAD, LUSC, CPCP); organoides | Estado del arte de organoides para medicina de precisión | Revisión sin método de búsqueda declarado | Concordancia >80 % (ref. 56); establecimiento 41 % y 17 % "puros" (ref. 90) (ficha D03) | No es fuente primaria; citas de otros cánceres usadas como apoyo (refs. 92, 93) | No aplica | Completo. Tablas 1–2 son imágenes, verificadas visualmente |
| D04 | `Durvalumab-after-Chemoradiotherapy-in-Limited-Stage-Small-Cell-Lung-Cancer.pdf` (15 pp.) | Cheng Y, Spigel DR, Cho BC, et al. (ADRIATIC). *N Engl J Med* 2024;391:1313–27 | doi:10.1056/NEJMoa2404873 · PMID 39268857 · NCT03703297 | **Ensayo clínico fase 3**, doble ciego (primer análisis intermedio) | **CPCP de estadio limitado** sin progresión tras QRT concurrente; n = 530 (D 264 / P 266) | ¿Mejora la consolidación con durvalumab la SG y la SLP? | Cox estratificado, Kaplan–Meier, jerarquía con reciclado de alfa | SG HR 0,73 (IC 98,321 % 0,54–0,98); SLP HR 0,76 (IC 97,195 % 0,59–0,98) [p. 1, 7] | Análisis intermedio; mediana de SG frágil; brazo D+T cegado (ficha D04 §6) | Suplemento no incluido. Curvas KM vectoriales con números en riesgo (ficha §4.4, §7) | Completo. Verificadas pp. 5, 6, 8 y 12 |
| D05 | `lUNG CANCER TARGETED THERAPY.pdf` (15 pp.) | Bouchard N, Daaboul N. *Curr Oncol* 2025;32:146 | doi:10.3390/curroncol32030146 · PMID 40136350 · PMC11941068 | Revisión narrativa | CPCNP con alteraciones accionables | Estado de la terapia dirigida en 2025 | Revisión sin método de búsqueda | Unos 60 resultados de ensayos tabulados (ficha D05) | Tabla 1 sin fuentes; errores de cita; una cifra de un comunicado de prensa | No aplica | Completo |
| D06 | `Mathematical Modeling Support for Lung Cancer Therapy—A Short Review.pdf` (21 pp.) | Smieja J. *Int J Mol Sci* 2023;24:14516 | doi:10.3390/ijms241914516 · PMID 37833963 · PMC10572824 | Revisión narrativa de modelos | CPCNP > CPCP | Catálogo de modelos de crecimiento y tratamiento | Revisión con 40 ecuaciones en notación unificada | **No da valores numéricos de parámetros** (ficha D06 §5) | Erratas en ecs. 6, 17 y 20 (ficha D06) | No aplica | Completo. Ecuaciones verificadas visualmente |
| D07 | `Modeling small cell lung cancer (SCLC) .pdf` (17 pp.) | Salgia R, et al. *Oncotarget* 2018;9(40):26226–42 | doi:10.18632/oncotarget.25360 · PMID 29899855 · PMC5995226 | Revisión / perspectiva con simulaciones ilustrativas | **CPCP** | Modelos deterministas y estocásticos de la biología del CPCP | ABM/BioFVM, Hahnfeldt, Gatenby, fractales | Parámetros genéricos o ilustrativos; posible inversión ϕ/φ (ficha D07) | Simulaciones propias poco reproducibles; erratas | No aplica | Completo. El DOI no aparece en el PDF; se obtuvo de Europe PMC y Crossref |
| D08 | `Reduced Lung-Cancer Mortality with Low-Dose Computed Tomographic Screening.pdf` (22 pp.) | National Lung Screening Trial Research Team. *N Engl J Med* 2011;365:395–409 | doi:10.1056/NEJMoa1102873 · PMID 21714641 · PMC4356534 | **Ensayo clínico aleatorizado** (cribado) | 53 454 personas de alto riesgo, EE. UU.; TCBD frente a radiografía de tórax | ¿Reduce la TCBD la mortalidad por cáncer de pulmón? | 3 rondas anuales; positivo con nódulo ≥4 mm | Reducción de la mortalidad por cáncer de pulmón de 20,0 % (IC 95 % 6,8–26,7) [p. 8]; NNS 320 | Comparador radiografía; sin sobrediagnóstico cuantificado (ficha D08 §7–8) | Manuscrito de autor de PMC. Suplemento no incluido | Completo. Tablas rotadas verificadas visualmente (pp. 14–19, 21–22) |
| D09 | `Reduced Lung-Cancer Mortality.pdf` (12 pp.) | de Koning HJ, et al. (NELSON). *N Engl J Med* 2020;382:503–13 | doi:10.1056/NEJMoa1911793 · PMID 31995683 | **Ensayo clínico aleatorizado** (cribado) | 13 195 varones (más 2594 mujeres en análisis de subgrupo), Países Bajos y Bélgica; TC volumétrica frente a no cribado | ¿Reduce la TC volumétrica la mortalidad? | 4 rondas (0, 1, 3 y 5,5 años); manejo por volumen y tiempo de duplicación | RR 0,76 (IC 95 % 0,61–0,94) a 10 años en varones [p. 7/508] | Umbrales en mm³ solo en el suplemento (no incluido); dos recuentos de muertes (ficha D09 §10) | Versión del editor (repositorio Radboud). Suplemento no incluido | Completo. Verificadas pp. 6–9 |
| D10 | `Simulating non-small cell lung cancer with a multiscale agent-based .pdf` (14 pp.) | Wang Z, Zhang L, Sagotsky J, Deisboeck TS. *Theor Biol Med Model* 2007;4:50 | doi:10.1186/1742-4682-4-50 · PMID 18154660 · PMC2259313 | Modelo matemático / simulación (ABM multiescala), **sin datos de pacientes** | CPCNP (teórico); parámetros de otros tipos celulares [p. 12] | Dinámica de expansión según la señalización EGFR–ERK | 20 ODE por célula + reglas fenotípicas + difusión 2D; C/C++ | Transición de fase en el umbral de EGF (ficha D10 §6) | Umbrales T_PLC y T_ERK no publicados; sin validación cuantitativa; sin análisis de sensibilidad | **Código no disponible** | Completo. Verificadas pp. 3–6 y 8–11 |
| R1 | `Reporte_Revision_Cancer_Pulmon_Insumo.md` | Informe propio (v1) | — | **Documento derivado, no evidencia** | — | — | — | — | — | — | Excluido de la matriz de evidencia (nota 2) |
| R2 | `Reporte_Revision_Cancer_Pulmon_Insumo_v2.md` | Informe propio (v2) generado en esta sesión | — | **Documento derivado, no evidencia** | — | — | — | — | — | — | Excluido de la matriz de evidencia. Sus cifras de IDC, GDC y CISNET proceden de consultas externas registradas en esa entrega |

## Duplicados, versiones y relevancia

- **No hay duplicados.** D08 y D09 tienen títulos parecidos ("Reduced Lung-Cancer Mortality…"), pero son ensayos distintos: NLST 2011 y NELSON 2020.
- **Versiones:**
  - D02 es un preprint superado (nota 1).
  - D08 es el manuscrito de autor, no la maqueta de NEJM. No se cotejó página a página con la versión de la revista; las cifras citadas proceden del manuscrito.
  - D09 es la versión del editor.
- **Correcciones y retractaciones:** Europe PMC (`commentCorrectionList`) y Crossref (`updated-by`) no registran ninguna errata, corrección ni retractación para los 10 DOI. Solo hay comentarios y editoriales ("Comment in") para D04, D08 y D09, y relaciones con preprints para D01, D02 y D05. Consulta del 10-oct-2026; detalle en `03_registro_busquedas/`.
- **Relevancia:**
  - Todos los documentos tratan de cáncer de pulmón.
  - **D04 y D07 son de CPCP; D02, D05, D06 y D10, de CPCNP.** D01 es pulmón (CPCNP) más Wilms. D08 y D09 son de cribado en población de alto riesgo (todas las histologías).
  - **No se mezclarán resultados entre CPCP y CPCNP, ni entre poblaciones de cribado y de tratamiento.**

## Notas

**Nota 1. D02: preprint frente a versión publicada.** La versión de *Math Biosci Eng* 2023 (descargada de aimspress.com, texto en `03_registro_busquedas/MBE_2023_Wagner_texto_extraido.txt`) difiere del preprint:
- **Parámetros de la Tabla 1:**
  - λ_P^pro: 0,36 / 0,0038 / 0,47 (antes 0,38 / 0,0038 / 0,53).
  - λ_τ^eff: 5,2 / 0,54 / 4,49 (antes 4,49 / 0,55 / 4,49).
  - λ_PN en 3D: 0,05 (antes 0,025).
  - **α_H = 1 y α_P = 4** (en el preprint estaban intercambiados: 4 y 1).
  - ω se redefine como "Ratio of the patient weight to the lung weight".
- **Contenido:** añade un análisis de sensibilidad **local** (ec. 4.1, Tabla 2).
- **Disponibilidad:** añade la sección "Code and data availability", que remite a `github.com/wagnandr/immunotherapy-lung-cancer`.
  - El repositorio se creó el 16-mar-2023 y su último *push* fue el 14-ago-2023. No tiene licencia declarada.
  - Contiene `data/tumor/pirmin-tumor-pat1.csv` (21 tiempos: volumen, RECIST y WHO) y `pat2.csv` (15 filas, 11 volúmenes numéricos, más una última anotación "(sehr gross)" en el día 1484).
  - Contiene además mallas, código en Python/FEniCS 2019.1.0, optimización por mínimos cuadrados y sensibilidad local.
- **Los datos del CSV coinciden exactamente** (21/21 y 11/11 valores y días) con la digitalización vectorial independiente que hizo el lector a partir del preprint. Esto valida ambos.
- **Consecuencia:** cualquier reproducción debe hacerse contra la **versión publicada y su repositorio**, no contra el preprint de la carpeta.

**Nota 2. R1.** Al inicio de esta sesión R1 medía 27 760 bytes (18:01). En la inspección mide 52 096 bytes (modificado a las 18:11). El cambio no lo hizo este análisis. R1 y R2 se tratan como documentos derivados y no se usan como fuente de evidencia.
