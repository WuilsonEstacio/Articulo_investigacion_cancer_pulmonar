# Ficha D07 — Salgia et al. (2018). Modelado de la biología del SCLC con modelos deterministas y estocásticos

> Convención de ubicación: `[p. N]` = página del PDF (1–17). La página de revista equivale a 26225 + N (p. ej., [p. 8] = p. 26233). `[ref n]` = número de referencia de la bibliografía de D07. Las ecuaciones de D07 **no están numeradas**; se identifican aquí como E1–E13 por orden de aparición.
> Fuentes: texto extraído (`00_extraccion_texto/Modeling small cell lung cancer (SCLC).txt`) y verificación visual de las páginas 7–11 del PDF (las ecuaciones salen ilegibles en el texto extraído).

---

## 1. Referencia completa

- **Autores:** Ravi Salgia, Isa Mambetsariev, Blake Hewelt, Srisairam Achuthan, Haiqing Li, Valeriy Poroyko, Yingyu Wang, Martin Sattler (City of Hope, Duarte, CA; Dana-Farber Cancer Institute; Harvard Medical School) [p. 1]. Correspondencia: Ravi Salgia [p. 1].
- **Título:** “Modeling small cell lung cancer (SCLC) biology through deterministic and stochastic mathematical models” [p. 1].
- **Revista:** *Oncotarget*, 2018, Vol. 9, (No. 40), pp: 26226–26242 [p. 1].
- **DOI:** **No reportado en el documento.** El PDF no imprime el DOI del propio artículo; solo aparecen DOIs de referencias. D06 cita este artículo como “Oncotarget 2018, 9, 26226–26242” también sin DOI visible ([ref 110 de D06]).
- **Fechas:** recibido el 7 mar 2018; aceptado el 24 abr 2018; publicado el 25 may 2018 [p. 1].
- **Licencia:** CC BY 3.0 [p. 1]. **Financiación:** NIH/NCI P30CA033572 y 1U54CA209978-01A1 [p. 12]. **Conflictos:** “None” [p. 12].
- **Material suplementario:** Supplementary Videos 1–4 (citados en [p. 4, 7, 9, 10]); **no incluidos** en el PDF analizado.
- **Referencias:** 114 [p. 12–17].

## 2. Tipo de documento y subtipo de cáncer

- **Tipo:** marcado como “Review” [p. 1], pero en la práctica es una **revisión narrativa/perspectiva híbrida**. Combina (a) una revisión de la biología y la clínica del SCLC [p. 3–6], (b) un panorama de clases de modelos [p. 6–11] y (c) **simulaciones ilustrativas propias** sin descripción metodológica completa: BioFVM (Fig. 3) [p. 7–8], modelo de capacidad de carga dinámica con metástasis (Fig. 4) [p. 8], burbujas de metástasis en JavaScript (Fig. 2) [p. 4–5], heterogeneidad CA (Fig. 5) [p. 10] y árbol fractal en Swift 3.1 (Fig. 1B) [p. 2].
- **¿Método de búsqueda declarado?** **No reportado** (no hay bases de datos, criterios ni periodo). “We reviewed mathematical models that have been developed for biological sciences and applied them in the context of small cell lung cancer” [p. 1].
- **Subtipo:** **solo SCLC**. Los modelos citados no son de pulmón: provienen de cáncer genérico, tumor cerebral [79] o mama [107].

## 3. Objetivo

- “Our goal is to develop an understanding of the mathematical basis of cancer in the context of small cell lung cancer (SCLC) growth, mutational heterogeneity, and mechanisms of metastasis” [p. 2].
- “The ultimate goal is to develop the stochastic and deterministic nature of this disease, to link this comprehensive set of tools back to its fractalness and to provide a platform for accurate biomarker development” [p. 1].
- Comunicar este entendimiento a clínicos y biólogos tumorales “in the hope of generating precise treatment maps” [p. 2].

## 4. Catálogo de modelos citados

| Clase de modelo | Ecuación tal como aparece (LaTeX) | Parámetros y valores numéricos (con unidades) | Referencia original citada | ¿Pulmón? ¿NSCLC/SCLC? | Página |
|---|---|---|---|---|---|
| ABM/CA (BioFVM), reacción–difusión de O₂ — **E1** | $\frac{\partial pO_2}{\partial t}=D_{oxy}\nabla^2 pO_2-\lambda_{oxy}pO_2-\sum_{cells\ i}U_{i,oxy}\,pO_2$ | $D_{oxy}$, $\lambda_{oxy}$, $U_{i,oxy}$: **valores no reportados** | [81] Ghaffarizadeh, Friedman, Macklin, 2016 (BioFVM) | Aplicado a SCLC “with some adjustments to values that would favor SCLC” | [p. 7–8] |
| PK espacial del fármaco — **E2** | $\frac{\partial c}{\partial t}=D_c\nabla^2 c-\lambda_c c-\sum_{cells\ i}U_{i,c}\,c$ | $D_c$, $\lambda_c$, $U_{i,c}$: no reportados. **Dosis: 5 μM en t = 528 (Day 22)** | [81] | SCLC (simulación ilustrativa) | [p. 8] |
| PD: exposición acumulada — **E3** | $E_i(t)=\int_0^t c(s)\,ds$ | — | [81] | SCLC (ilustrativo) | [p. 8] |
| PD: respuesta saturable (Hill h = 1) — **E4** | $R_i(t)=\frac{E_i(t)}{\alpha_i+E_i(t)}$ | $\alpha$ = “exposure for a half-maximum effect” (valor no reportado); **h = 1** | [81] | SCLC (ilustrativo) | [p. 8] |
| ABM: tasa de nacimiento dependiente de O₂ y fármaco — **E5** | $b_i(t)=\begin{cases} b_{i,P}\,(1-\eta_iR_i(t)) & \text{if } pO_{2,P}<pO_2\\ b_{i,P}\left(\frac{pO_2-pO_{2,N}}{pO_{2,P}-pO_{2,N}}\right)(1-\eta_iR_i(t)) & \text{if } pO_{2,N}<pO_2\le pO_{2,P}\\ 0 & \text{if } pO_2\le pO_{2,N}\end{cases}$ | $b_{i,P}$, $\eta_i$, $pO_{2,P}$, $pO_{2,N}$: no reportados. Ajuste SCLC: “increasing the birth rate by .025” (**sin unidades**) | Macklin et al., vía [81] | SCLC (ilustrativo) | [p. 7, p. 9] |
| ABM: necrosis por hipoxia — **E6** | $d_{i,N}(t)=\begin{cases}0 & \text{if } pO_{2,N}<pO_2\\ d^{*}_{i,N} & \text{if } pO_2\le pO_{2,N}\end{cases}$ (en el PDF el lado izquierdo aparece como $d_i(t)$) | $d^{*}_{i,N}$ “is a constant” (valor no reportado). Ajuste SCLC: “3% rate of necrosis for perinecrotic tumor cells” | [81] | SCLC (ilustrativo) | [p. 7, p. 9] |
| ABM: apoptosis inducida por fármaco — **E7** | $d_{i,A}(t)=d^{*}_{i,A}+(d^{max}_{i,A}-d^{*}_{i,A})R_i(t)$ | $d^{*}_{i,A}$, $d^{max}$ (“maximum rate of apoptosis”): no reportados | [81] | SCLC (ilustrativo) | [p. 9] |
| ABM estocástico: probabilidades por paso — **E8** (tal como está impreso) | $P(\text{cell division})=1-\exp(d_{i,A}(t)\Delta t)$; $P(\text{apoptotic death})=1-\exp(b_i(t)\Delta t)$; $P(\text{necrotic death})=1-\exp(-d_{i,N}(t)\Delta t)$ | $\Delta t$ no reportado. **Ver §10**: las tasas $b_i$ y $d_{i,A}$ aparecen intercambiadas y sin signo negativo | [81] | SCLC (ilustrativo) | [p. 9] |
| ABM estocástico: lisis — **E9** | $P(\text{cell lysis})=1-\exp\left(-\frac{1}{T_{i,D}}\Delta t\right)$ | $T_{i,D}$ = duración de la muerte celular (valor no reportado; “duration of necrosis and cell death are the same”) | [81] | SCLC (ilustrativo) | [p. 8, p. 9] |
| ABM: ajustes cualitativos SCLC (sin ecuación) | Hill “viable cell” = **4**; vida media viable modificada (más apoptosis con el tiempo; menor tiempo apoptosis→necrosis por hipoxia); inicio con **una célula en t = 0** | Valores base no reportados | [81], [75] Macklin & Edgerton, 2010 | SCLC (ilustrativo) | [p. 7–8] |
| Capacidad de carga dinámica (angiogénesis) — **E10** | $\frac{dK}{dt}=\phi C-\varphi C^{\frac{2}{3}}$, donde “ϕ and φ represent constant positive rates of angiogenesis stimulation and inhibition, respectively” | Fig. 4: **λ = 0.192, φ = 5.85, ϕ = 0.00873** (**sin unidades**; “parameters used by Enderling and Chaplain [90]”). λ no aparece en ninguna ecuación del documento | Ecuación: [91] Hahnfeldt et al., 1999; parámetros: [90] Enderling & Chaplain, 2014 | Aplicado a SCLC sin calibración declarada | [p. 8 (Fig. 4), p. 9] |
| Crecimiento tumoral (proliferativo/quiescente) | Sin ecuación; solo las condiciones: quiescencia $\alpha-\beta=0$; proliferativo $\alpha>\beta$; deplecionante $\alpha<\beta$ (α = fracción de células que se dividen; β = fracción que muere) | Sin valores | [90] Enderling & Chaplain, 2014 | No pulmonar | [p. 9] |
| Carga metastásica (Fig. 4) | Sin ecuación en el documento | “parameters from Benzekry et al. [114]” (**valores no reportados**). Cualitativamente, la carga metastásica crece “exponentially” al acercarse el primario a K | [114] Benzekry, Gandolfi, Hahnfeldt, 2014 | Aplicado a SCLC (ilustrativo) | [p. 8] |
| PDE de invasión ácido-mediada (Gatenby–Gawlinski) — **E11** | $\frac{\partial C}{\partial t}=\nabla\cdot\left(D_C(1-\upsilon)\nabla C\right)+\rho C(1-C)$; $\frac{\partial m}{\partial t}=\nabla^2 m+\delta(C-m)$; $\frac{\partial \upsilon}{\partial t}=\upsilon(1-\upsilon)-\gamma m\upsilon$ | $D_C$ (difusión), ρ (proliferación), δ (producción/decaimiento de H⁺), γ (degradación de la MEC): **sin valores** (forma adimensional) | [92] Gatenby & Gawlinski, 1996 | No pulmonar | [p. 9–10] |
| Haptotaxis / invasión (continuo y discreto) | Sin ecuación propia (“modified version of” la ecuación de $m$) | — | [93] Anderson et al., 2000; [94] Anderson & Chaplain, 1998 (paseo aleatorio sesgado) | No pulmonar | [p. 10] |
| Crecimiento logístico | Solo implícito: término $\rho C(1-C)$ en E11 y “logistic growth for normal tissue” | — | [92] | No pulmonar | [p. 9–10] |
| Exponencial | Solo cualitativo (“first order kinetics such as ordinary differential equations” [p. 6]; crecimiento metastásico “exponentially” [p. 8]) | — | — | — | [p. 6, p. 8] |
| Gompertz / von Bertalanffy | — | — | **No reportado** | — | — |
| Radioterapia LQ | — | — | **No reportado** (solo se menciona la RT torácica como tratamiento clínico) | — | [p. 3] |
| Resistencia (modelo) | — | — | **No reportado como modelo**; se mencionan biológicamente la quimiorresistencia y los “cancer attractors … responsible for resistance” | — | [p. 3, p. 6] |
| Inmunoterapia (modelo) | — | — | **No reportado** como modelo; se citan inhibidores de checkpoint (pembrolizumab, nivolumab/ipilimumab), anticuerpos biespecíficos y CAR-T [p. 11] | — | [p. 6, p. 11] |
| Caos tumor–sano–inmune | Sin ecuación | — | [95] Itik & Banks, 2010 (modelo 3D con caos determinista); control por álgebra de Lie [97] Shahzad, 2016; teoría de grupos [96] Rietman et al., 2011 | Genérico | [p. 10] |
| Atractores de redes génicas (paisaje), tipo on/off | Sin ecuación. Transición normal→cáncer: “MDM2 on, CDK2 on, RB off”; reversión: “RB goes on, CDK2 and CDK4 off, and off of MDM2” | — | [69] Huang et al., 2009; [70] Jia et al., 2017; [71] Ao et al., 2008; [72] Li & Wang, 2014 | Aplicación sugerida a SCLC (por el papel de RB) | [p. 6] |
| Redes EMT híbridas (microRNA–FT) | Sin ecuación | — | [48] Lu et al., 2013 (tristabilidad); [49] Lu et al., 2013; [50] George et al., 2017 | Genérico | [p. 4] |
| Booleano | — | — | **No reportado explícitamente**; lo más cercano son los estados on/off de [72] | — | [p. 6] |
| Señalización p53 / NF-κB / EGFR (modelos) | — | — | **No reportado** (TP53 aparece solo como mutación) | — | — |
| CA clásicos y Potts | Sin ecuación | — | Conway “Game of Life” [82]; CA celular [83–87] y subcelular [88, 89]; Qi et al. [86] (estados normal/canceroso/complejo/muerto); Potts celular [77], [78]; ABM espacial de cúmulos (tumor cerebral) [79] Mansury et al., 2002; híbrido discreto-continuo [80] Anderson, 2005; CA multinivel [74]; multiescala [76] | No pulmonar | [p. 6–7, p. 9] |
| Heterogeneidad mutacional CA (Fig. 5) | Sin ecuación ni reglas | Sin valores | Simulación propia (Supplementary Video 4) | SCLC (ilustrativo) | [p. 10] |
| Metástasis por órganos (Fig. 2) | Sin ecuación; “javascript bubble chart”, estado final fijado por los porcentajes de Nakazawa et al. | 60.6 % con metástasis a distancia; hígado 20.3 %, hueso 18.3 %, cerebro 15.5 %, pulmón 10.0 %, suprarrenal 6.0 % | [42] Nakazawa et al., 2012 | **Sí, SCLC (datos clínicos)** | [p. 4–5] |
| Fractal: dimensión de similitud — **E12** | $D_S=-\frac{\ln N}{\ln r}$ | N = número de copias no solapadas; r (< 1) = razón de escala | [101] Falconer, 1990 | Propuesta para SCLC | [p. 11] |
| Fractal: box-counting y multifractal (sin ecuación explícita) — **E13** (descriptiva) | Exponente de Hölder α (α_min, α_max); espectro multifractal $f(\alpha)$ | — | [102] Levy-Vehel & Berroir, 1992; [105, 106, 107]; aplicación en mama a la predicción de respuesta a quimio: [107] Vasiljevic et al., 2015 | Propuesta para SCLC (histología, ADN, imagen radiológica); aplicación previa en mama | [p. 11] |

## 5. Valores numéricos de parámetros biológicos para cáncer de pulmón

**No hay parámetros biológicos pulmón-específicos derivados de datos** (ni tiempos de duplicación, ni tasas de crecimiento calibradas, ni α/β, ni constantes PK). Los únicos valores numéricos de modelo son:

| Valor | Contexto | Fuente declarada | Página | Comentario |
|---|---|---|---|---|
| λ = 0.192; φ = 5.85; ϕ = 0.00873 (sin unidades) | Crecimiento con capacidad de carga dinámica (Fig. 4A) | “parameters used by Enderling and Chaplain [90]” (la ecuación de K se atribuye a Hahnfeldt [91]) | [p. 8] | No calibrados a SCLC. **[Nota del lector, no verificada en el corpus]**: estos valores coinciden con los que recuerdo de Hahnfeldt et al. 1999 (λ en día⁻¹; b = 5.85 día⁻¹ y d = 0.00873 día⁻¹·mm⁻², ajustados en carcinoma pulmonar de Lewis murino); allí 5.85 era la **estimulación** y 0.00873 la **inhibición**, al revés de la asignación ϕ/φ que resulta de D07. Hay que verificarlo en [91]. |
| +0.025 en la tasa de nacimiento | Ajuste BioFVM “to favor SCLC” | Autores (sin dato fuente) | [p. 7] | Sin unidades ni valor base. |
| Hill de célula viable = 4 | Ajuste BioFVM | Autores | [p. 7] | — |
| 3 % de necrosis en células perinecróticas | Ajuste BioFVM “to fit our carrying capacity obtained in Figure 4” | Autores | [p. 7] | Calibrado contra otra simulación (Fig. 4), no contra datos. |
| Fármaco 5 μM en t = 528 (Day 22) | Simulación BioFVM | Autores | [p. 8] | Unidad temporal implícita en horas (528 h = 22 d). Fármaco no identificado. |
| Hill de respuesta al fármaco h = 1 | E4 | [81] | [p. 8] | — |
| Necrosis inicia a > 180 h; instantáneas a 12, 180 y 300 h; dominio de aproximadamente ±400–500 μm; escala de O₂ 5–35 (unidades no rotuladas) | Fig. 3 | Simulación propia | [p. 7] | Salida de simulación, no parámetro biológico. |

## 6. Datos clínicos o experimentales mencionados (cifras exactas)

| Dato | Cifra | Ref. | Página |
|---|---|---|---|
| Supervivencia global a 5 años | “less than 7%” | [14] | [p. 3] |
| Supervivencia a 5 años / muertes | “less than 20% and more than 30,000 deaths per year” (SCLC “recalcitrant” en EE. UU.) | Sin referencia | [p. 3] |
| Curación en LD | “approximately a quarter of patients with LD can be cured” | Sin referencia directa | [p. 3] |
| Tratamiento LD | Platino + etopósido con RT torácica una o dos veces al día antes del 3.er ciclo | [15–18] | [p. 3] |
| Mediana de supervivencia | LD: 15–20 meses; ED: 5.5 meses | Sin referencia directa (la frase siguiente cita [19]) | [p. 3] |
| Segunda línea | Topotecán | [20, 21] | [p. 3] |
| Mejora de la supervivencia a 5 años | “only marginally improved in the past 40 years” | [14, 22] | [p. 3] |
| Carga mutacional | ~175 mutaciones por tumor; 5.5 a 7.4 mutaciones por Mb | [25, 26] | [p. 3] |
| TP53 / RB1 | TP53 100 %, RB1 93 % (casos sin cromotripsis) | [31] | [p. 3] |
| Disrupción E2F/RB1 (EZH2) | 96 % de los SCLC | [32] | [p. 3–4] |
| NOTCH inactivado | ~25 % de los tumores | [31] | [p. 4] |
| DLL3 | Expresado en > 80 % de los SCLC | Sin referencia directa (la frase siguiente cita [34]) | [p. 4] |
| Amplificación MYC | ~16 % | [25] | [p. 4] |
| Metástasis (cohorte retrospectiva) | 251 pacientes (diagnosticados en 1999–2000); 152 (60.6 %) con metástasis a distancia: hígado 20.3 %, hueso 18.3 %, cerebro 15.5 %, pulmón 10.0 %, suprarrenal 6.0 % | [42] | [p. 4] |
| ADAM-12 | 73 % de las muestras; otros ADAM, 10–40 %; el knockdown en H1688 reduce el crecimiento, la invasión y la metástasis | [59] | [p. 5] |
| CD44 / hialuronidasa | Expresión “low or absent” | [60, 61] | [p. 5] |
| Mutaciones MET R988C y T1010I | Alteran la morfología, la adhesión y la formación de colonias en H446 | [38] | [p. 5] |
| Inhibidor de CXCR4 AMD3100 (xenoinjerto ortotópico) | Reduce la formación de metástasis en un 43 %; cisplatino/etopósido reducen el crecimiento pero no las metástasis | [68] | [p. 6] |

## 7. Vacíos y desafíos declarados por los autores

- “Computational models thus far have mostly focused on comprehensive cancer biology models rather than individualized disease models” [p. 1].
- “to date there are no effective methods for early screening and detection for SCLC” [p. 3].
- Los avances se apoyan en líneas celulares in vitro, que “may not be suitable for unraveling the sequence of events” de la iniciación [p. 3].
- La población de células madre del SCLC “is not well defined” [p. 3].
- El CA de Qi et al. “did not explicitly consider growth promoting factors … and growth inhibiting factors” [p. 9].
- Los ODE no consideran variables espaciales [p. 9].
- “As we go forward from here, we have to be able to incorporate mathematical modeling in SCLC … we should be able to study the potential for mechanisms of resistance” [p. 10].
- “The effective utilization of mathematical models to these therapies is hampered in part by the availability of quantitative in vitro experimental data and clinical results” [p. 11].
- “the models presented here are not perfect” [p. 11–12].
- Hace falta entender la metástasis como una secuencia de rupturas de simetría [p. 12].

## 8. Evaluación del lector *(interpretación propia)*

- **[Lector] Profundidad:** baja-media en lo matemático. Casi la mitad del texto es biología y clínica del SCLC [p. 2–6]. Las clases de modelos se describen superficialmente y casi todas las ecuaciones son de modelos genéricos (BioFVM/Macklin, Hahnfeldt, Gatenby–Gawlinski). Ningún modelo se calibra ni se valida con datos de SCLC, salvo la Fig. 2, cuyo estado final se fija con porcentajes clínicos [42].
- **[Lector] Simulaciones propias poco reproducibles:** faltan los valores base de BioFVM, el paso temporal, el tamaño del dominio, las unidades de la tasa de nacimiento, la identidad del fármaco y la ecuación de crecimiento de C en la Fig. 4 (λ se da sin ecuación). No se reporta código ni repositorio (solo se mencionan “MATLAB model scripts”, [p. 8]). Además, BioFVM se describe como simulador de “cellular automaton models” [p. 7], pero las reglas citadas son las del marco de Macklin (agentes off-lattice/difusión).
- **[Lector] Sesgo de selección:** no hay método de búsqueda. Predominan referencias clásicas (1975–2016) y autocitas del grupo Salgia en la parte biológica ([22–24, 36–39, 43, 44, 57, 62, 63]). El énfasis fractal y caótico es conceptual (“hypothesized”, [p. 2]) y no se acompaña de un análisis de imágenes SCLC cuantificado.
- **[Lector] Utilidad como fuente de parámetros:** **no es fuente primaria**. Para parámetros habría que consultar:
  - Dinámica angiogénica y capacidad de carga → [91] Hahnfeldt et al., 1999 (Cancer Res 59:4770–4775; la ref. de D07 imprime “4770–05”) y [90] Enderling & Chaplain, 2014.
  - Metástasis y dormancia → [114] Benzekry, Gandolfi & Hahnfeldt, 2014 (PLoS One 9:e84249).
  - Parámetros del ABM (O₂, nacimiento/muerte, umbrales pO₂) → [81] Ghaffarizadeh et al., 2016, y [75] Macklin & Edgerton, 2010.
  - Invasión ácido-mediada → [92] Gatenby & Gawlinski, 1996.
  - Distribución metastásica SCLC (dato clínico) → [42] Nakazawa et al., 2012.
  - Carga mutacional y genómica (posibles tasas de mutación para modelos estocásticos) → [25] Peifer et al., 2012; [26] Rudin et al., 2012; [31] George et al., 2015.
  - Paisaje y atractores → [72] Li & Wang, 2014.
  - Multifractal para predecir la respuesta a quimio (en mama) → [107] Vasiljevic et al., 2015.
- **[Lector] Valor principal:** ofrece un contexto clínico y biológico SCLC cuantitativo (supervivencia, frecuencias de mutación, patrón metastásico) útil para **definir escenarios y objetivos de calibración**, más que parámetros cinéticos.

## 9. Oportunidades de simulación reproducible (apoyadas en lo que contiene el documento)

1. **Capacidad de carga dinámica de Hahnfeldt** (E10, [p. 9]) con λ = 0.192, φ = 5.85 y ϕ = 0.00873 (Fig. 4, [p. 8]): reproducir cualitativamente la Fig. 4A. **Requiere** la ecuación de crecimiento de C, que D07 no da (consultar [91]), y resolver la ambigüedad ϕ/φ (§10).
2. **Patrón de metástasis SCLC**: modelo compartimental o multinomial cuyo estado final reproduzca 60.6 % de metástasis a distancia con hígado 20.3 %, hueso 18.3 %, cerebro 15.5 %, pulmón 10.0 % y suprarrenal 6.0 % ([42], [p. 4]); equivale a la Fig. 2 [p. 5].
3. **ABM con microambiente de O₂ y fármaco** (E1–E9, [p. 8–9]): implementar en PhysiCell/BioFVM o en código propio y comprobar dos salidas reportadas, el inicio de la necrosis a > 180 h (Fig. 3, [p. 7]) y la respuesta al fármaco 5 μM en t = 528 h [p. 8]. Hacen falta los valores base de [81]; deben corregirse las probabilidades de división y apoptosis (§10).
4. **Invasión ácido-mediada de Gatenby–Gawlinski** (E11, [p. 9]) en 1D adimensional: análisis de frentes de invasión según δ, γ y $D_C$ (sin valores en D07; tomarlos de [92]).
5. **Dimensión fractal** (E12 y box-counting, [p. 11]) sobre imágenes histológicas de SCLC (tipo Fig. 1C, [p. 2]): pipeline reproducible de box-counting y espectro multifractal $f(\alpha)$.
6. **Escenario de supervivencia**: usar las medianas LD 15–20 meses y ED 5.5 meses [p. 3] como objetivo de calibración para cohortes virtuales. Es un dato clínico sin referencia directa en la frase, por lo que convendría verificarlo.

## 10. Problemas de extracción y de contenido

- **Texto extraído:** **todas las ecuaciones** (E1–E12) salen ilegibles o desordenadas en el .txt ([p. 8–11]). Se transcribieron desde el PDF renderizado (PyMuPDF, 130–300 dpi) y se verificaron los glifos Unicode de los símbolos griegos.
- **Ambigüedad ϕ/φ (E10 y Fig. 4):** según los glifos del PDF, la ecuación es $\frac{dK}{dt}=\phi C-\varphi C^{2/3}$ (ϕ U+03D5 = estimulación, φ U+03C6 = inhibición), y la leyenda de la Fig. 4 asigna **φ (U+03C6) = 5.85** y **ϕ (U+03D5) = 0.00873**. Así, la estimulación valdría 0.00873 y la inhibición 5.85, lo que parece invertido (ver la nota del lector en §5). Además, λ = 0.192 no está definido en ninguna ecuación. Por último, la ecuación de K impresa no incluye el factor K en el término de inhibición; el lector cree que el original de Hahnfeldt sí lo incluye, pero debe verificarse en [91].
- **E8 (probabilidades del ABM):** tal como está impresa, P(división) usa $d_{i,A}$ y P(apoptosis) usa $b_i$, ambas sin signo negativo en el exponente. Con tasas positivas eso daría probabilidades negativas. Lo coherente es $1-\exp(-b_i\Delta t)$ para la división y $1-\exp(-d_{i,A}\Delta t)$ para la apoptosis, una errata evidente dentro del propio documento.
- **E6:** en la figura de ecuaciones el lado izquierdo es $d_i(t)$, pero el texto y E8 lo tratan como $d_{i,N}$ (necrosis).
- **[p. 10]:** el texto reutiliza dos veces la ecuación de $m$ (“∂m/∂t = ∇²m + δ(C − m)”) donde parece referirse al sistema completo o a otra ecuación (haptotaxis de Anderson [93]). Probable error de maquetación del original.
- **Unidades:** la tasa de nacimiento (+0.025), λ, φ, ϕ y la escala de O₂ de la Fig. 3 no tienen unidades; t = 528 se asocia a “Day 22”, de donde se infieren horas.
- **Referencia [91]:** las páginas impresas son “4770–05” (D06 imprime 4770–4775 para la misma obra). En el texto se escribe “Hahnefeldt”.
- **Suplementos:** los Supplementary Videos 1–4 no están disponibles en el corpus.
- **DOI propio:** no impreso en el PDF.

## 11. Citas textuales clave

1. “We reviewed mathematical models that have been developed for biological sciences and applied them in the context of small cell lung cancer (SCLC)” [p. 1].
2. “Computational models thus far have mostly focused on comprehensive cancer biology models rather than individualized disease models” [p. 1].
3. “Most patients are not diagnosed at an early stage, have metastatic disease and face limited treatment options with an overall 5-year survival of less than 7%” [p. 3].
4. “A retrospective study analyzed 251 SCLC patients … and found 152 (60.6%) with distant metastases” [p. 4].
5. “by increasing the birth rate by .025 and increasing the viable cell Hill coefficient to 4 to simulate our growth rate in Figure 4” [p. 7].
6. “The necrosis of the tumor initiates at > 180 hours” (Fig. 3) [p. 7].
7. “λ = 0.192, φ = 5.85, and ϕ = 0.00873, parameters used by Enderling and Chaplain [90]” (Fig. 4) [p. 8].
8. “ODE can be utilized to study tumor kinetics, PDE on tumor-stroma interactions, and chaos theory on geometry and symmetry breaking [113] in metastasis” [p. 12].
9. “The effective utilization of mathematical models to these therapies is hampered in part by the availability of quantitative in vitro experimental data and clinical results” [p. 11].
10. “Even though the models presented here are not perfect, they provide us with the tools to allow us to breakdown the mechanisms of growth and metastasis” [p. 11–12].
