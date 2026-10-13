# Registro de búsquedas complementarias

**Fecha de todas las consultas:** 10-oct-2026.

**Ejecución:** scripts de Python en esta carpeta, con el JSON resultante (consulta, n de resultados y registros devueltos) junto a cada uno.

**Propósito:** (a) verificar identificadores y versiones de los insumos; (b) detectar correcciones o retractaciones; (c) localizar datos y código; (d) contrastar si las contribuciones candidatas ya están resueltas.

**Alcance real y límites:**
- No es una revisión sistemática ni cubre "toda la literatura".
- Las búsquedas son dirigidas, en Europe PMC (que indexa PubMed/MEDLINE, PMC y preprints), Crossref, GitHub y una búsqueda web general.
- No se consultaron Embase, Scopus ni Web of Science, ni registros de ensayos (salvo el NCT que figura en D04) ni actas de congresos (ASCO, ESMO, WCLC).
- Los registros de ensayos y los comunicados de patrocinadores no se consideran evidencia de resultados.
- Criterio de selección para leer resúmenes: relación directa con una contribución candidata (C1–C4) o con un insumo.

## 1. Verificación de identificadores, versiones y correcciones

| ID | Servicio | Consulta | Resultado | Archivo |
|---|---|---|---|---|
| Q01 | Europe PMC REST `search` (resultType=core) | Un DOI o título por insumo (D01–D10) | Los 10 identificados (DOI, PMID, PMCID). D02: existen la versión publicada en *Math Biosci Eng* 2023 (doi:10.3934/mbe.2023828) y un preprint de bioRxiv (doi:10.1101/2023.03.20.533400). El PDF de la carpeta es arXiv:2303.09378v1 | `consulta_europepmc.py`, `europepmc_identificadores.json` |
| Q02 | Europe PMC `commentCorrectionList` | Ídem | Sin erratas, correcciones ni retractaciones. Solo "Comment in" (D04: 3; D08: 15; D09: 8) y relaciones con preprints (D01, D02, D05) | Ídem |
| Q03 | Crossref `/works/{doi}` | 11 DOI (incluye preprint y versión publicada de D02) | `updated-by` y `update-to` vacíos en todos. Volumen y páginas confirmados | `consulta_crossref.py`, `crossref_actualizaciones.json` |
| Q04 | aimspress.com (editorial de MBE) | doi:10.3934/mbe.2023828 → PDF de acceso abierto | Descargado a una carpeta aislada del área temporal. Texto extraído en `MBE_2023_Wagner_texto_extraido.txt`. Diferencias con el preprint: inventario, nota 1 | — |
| Q05 | API de GitHub (solo lectura de metadatos y archivos de texto pequeños) | `repos/wagnandr/immunotherapy-lung-cancer` y su árbol | Repositorio creado el 16-mar-2023, último *push* el 14-ago-2023, **sin licencia**. Contiene CSV de 2 pacientes, código 1D/3D (FEniCS 2019.1.0), optimización y sensibilidad local. Se leyeron README, CSV, `parameters.py`, `medicine_solver.py`, `create_therapy_schedule.py` y `experimental_data.py`. **No se clonó ni ejecutó nada** | — |

## 2. Contraste de novedad

| ID | Consulta (Europe PMC salvo indicación) | n | Hallazgos relevantes (leídos en resumen) | Implicación |
|---|---|---|---|---|
| B01 | `AUTH:"Schlicke P" AND (lung OR NSCLC)` | 11 | **Scibilia KR, Schlicke P, Schneller F, Kuttler C. *Math Biosci* 2024** (doi:10.1016/j.mbs.2024.109287): 4 modelos ODE, incluido uno de respuesta retardada, para predecir progresión bajo inhibidores de punto de control en pulmón. Exactitud 77 % (sensibilidad 70 %, especificidad 81 %), calibrados con el diámetro mayor; superan a un enfoque de ML. Benzekry, Schlicke et al. 2024 (metástasis cerebrales, n = 31). Schlicke et al. *Br J Cancer* 2026 (Gompertz con capacidad de carga compartida, datos murinos) | **C1:** el mismo grupo ya comparó ODE mínimas en pacientes con inmunoterapia, aunque **no** (según el resumen) el modelo de campo de fase frente a ODE en estos 2 pacientes. **Pendiente:** leer el texto completo de Scibilia 2024 (no está en PMC) para comprobar qué datos usa y si incluye estos pacientes |
| B02 | `CITES:38052574_MED` | 0 | Sin citas indexadas de la versión publicada de D02 | No se detecta ninguna reproducción ni extensión publicada |
| B03 | Modelos clásicos de crecimiento + ICI + CPCNP | 44 | FDA, Malinou et al. *Oncologist* 2026: tasa de crecimiento g en 10 495 pacientes de 22 ensayos | Contexto para C1: los modelos simples de regresión-crecimiento ya se usan a gran escala |
| B16 | `TITLE:"Classical mathematical models for prediction of response to chemotherapy and immunotherapy"` | 2 | **Ghaffari Laleh N, et al. *PLoS Comput Biol* 2022** (PMC8903251): 6 modelos clásicos en 1472 pacientes; el de Gompertz ofrece el mejor equilibrio. Datos de OAK, POPLAR, BIRCH y FIR **vía Vivli (acceso controlado)**; código en github.com/KatherLab/ImmunotherapyModels | C1: referencia metodológica para los comparadores parsimoniosos. Los datos a gran escala requieren solicitud |
| B11, B12 | Grupo Kuttler/Schlicke | 7 / 6 | Schlicke et al. *Theor Biol Med Model* 2021 (PMC8170801): datos "available from the corresponding author on reasonable request" (texto completo leído en esa sección) | Los datos del grupo no son abiertos, salvo los 2 pacientes del repositorio de D02 |
| B04 | ADRIATIC + costo-efectividad / supervivencia particionada / reconstrucción | 44 | ≥5 análisis de costo-efectividad 2025–2026 (Tsai *JTO CRR* 2025; Jani *JCO GO* 2025; *TLCR* 2025; *J Cancer Res Ther* 2026; *Front Oncol* 2025) con modelos de supervivencia particionada a partir de ADRIATIC | **C2:** reconstruir y extrapolar **no es novedoso** por sí solo. La contribución tendría que centrarse en la incertidumbre estructural y en la validación temporal (ver plan) |
| B05 | ADRIATIC 2025–2026 | 147 | FC poblacional y exposición-respuesta (*AAPS J* 2026); subgrupo China; resultados por PCI (*JTO* 2026); corrigendum de resultados reportados por pacientes (*JTO* 2026) | No se encontró, en los primeros resultados, un análisis final de SG publicado |
| W01 | Búsqueda web estándar: "ADRIATIC durvalumab limited-stage SCLC updated overall survival final analysis 2025 2026" | — | Solo análisis de 2024 (ASCO y ESMO 2024, aprobación de la FDA). Ningún análisis final encontrado | **Verificar de nuevo antes de ejecutar C2.** Fuentes: ascopost.com (dic-2024), ilcn.org, businesswire.com (comunicados; no son evidencia) |
| B18 | Texto completo (Europe PMC `fullTextXML`) de PMC12605132 (Tsai et al., *JTO CRR* 2025) y PMC12432599 (*TLCR* 2025). Búsqueda de términos de métodos de supervivencia | — | **Tsai 2025:** digitalización con WebPlotDigitizer y `digitise()` en R (Guyot); exponencial, Weibull, gamma, gamma generalizada, log-logística y **log-normal (elegida por AIC/BIC)**; horizonte de vida. **TLCR 2025:** GetData Graph Digitizer; exponencial, Weibull, Gompertz, log-logística y log-normal; **Weibull elegida** por inspección visual, plausibilidad clínica y AIC/BIC. **Ninguno** menciona modelos de curación, splines (Royston–Parmar) ni RMST | **C2:** dos análisis sobre el mismo ensayo eligen distribuciones distintas para extrapolar, lo que evidencia incertidumbre estructural no cuantificada. Hueco concreto: comparación sistemática de modelos (incluidos curación y splines) con validación temporal interna. Los otros 3 análisis de costo-efectividad no se revisaron (sin acceso abierto verificado) |
| B19 | `AUTH:"Scibilia KR"` | 2 | Solo la versión de revista (sin PMCID ni preprint) y un comentario de 2025 en *Cancer Res* (PMC12614879) | El texto completo de Scibilia 2024 sigue pendiente (acceso de pago) |
| B15 | ADRIATIC + modelos de cura, RMST, riesgos no proporcionales, extrapolación | 18 | Ningún trabajo específico de RMST o curación sobre ADRIATIC entre los primeros resultados | Indicio (no prueba) de un hueco para C2 |
| B06 | (NELSON OR NLST) + microsimulación + calibración/validación | 177 | **de Nijs K, et al. *Int J Cancer* 2025** (PMC12496006): MISCAN-Lung reproduce NELSON con datos individuales (sensibilidad por estadio e histología). Salgado et al. *Lancet Reg Health Am* 2026: modelo CISNET adaptado a Argentina | **C4:** calibrar con NLST y validar con NELSON con datos agregados **ya está superado** por modelos con datos individuales. Baja novedad |
| B08 | NLST + seguimiento extendido | 160 | **Welz M, et al. *Nat Commun* 2025** (PMC12394595): heterogeneidad de la efectividad del cribado en NLST y NELSON con datos individuales y ML | Refuerza la conclusión sobre C4 |
| B09 | NELSON + sobrediagnóstico | 576 | Revisión sistemática de sobrediagnóstico (*Mol Oncol* 2026) | Contexto |
| B07 | `CITES:18154660_MED` (D10) | 60 | Sin replicaciones del modelo entre los 8 primeros (orden por relevancia) | **C3:** no se detectó replicación, pero la búsqueda no es exhaustiva. Pendiente revisar los 60 títulos |
| B13, B14 | Replicación o reproducibilidad de ABM EGFR / modelos oncológicos | 504 / 404 | Resultados no pertinentes (búsqueda poco específica) | Sin conclusión. Se requiere revisar ReScience C y búsqueda manual |
| B10 | "tumor growth inhibition" + ICI + pulmón | 2502 | Poco específica | Descartada |

## 3. Consultas de la entrega anterior (informe v2)

Se reutilizan como contexto, no como evidencia de esta entrega:
- Páginas de OMS, NCI, PMC, Nature, CISNET, TCIA e IDC.
- API de GDC e índice `idc-index` v25 de IDC.

Detalle en `Data_insumo/Reporte_Revision_Cancer_Pulmon_Insumo_v2.md`, tabla "Trazabilidad de acceso".

## 4. Pendientes de búsqueda antes de ejecutar

1. Texto completo de Scibilia et al. 2024 (*Math Biosci*): datos usados, posible solapamiento con los 2 pacientes de D02 y modelos comparados. **Condición de novedad de C1.**
2. Resuelto parcialmente (B18): los dos análisis de costo-efectividad abiertos usan modelos paramétricos estándar, con distinta elección, y no usan curación, splines ni RMST. Faltan los otros 3 (*JCO GO* 2025, *Front Oncol* 2025, *J Cancer Res Ther* 2026). **Condición de novedad de C2.**
3. Actas de ASCO, ESMO y WCLC 2025–2026 sobre ADRIATIC (análisis final de SG o del brazo durvalumab + tremelimumab).
4. ReScience C y los 60 trabajos que citan a D10. **Condición de novedad de C3.**
5. Fuentes primarias de los parámetros cinéticos de D10 (sus refs. 11, 12, 14 y 39), necesarias para diagnosticar discrepancias.
