# Ficha D10: ABM multiescala EGFR-ERK en NSCLC (Wang et al., 2007)

**Convenciones.** `[p. N]` es la página del PDF original (1–14). Lo que no aparece en el documento se marca como **No reportado**. Las afirmaciones del lector van etiquetadas **[Evaluación del lector]** y el conocimiento ajeno al documento, **[Conocimiento externo del lector, no declarado en el documento]**.

**Páginas verificadas visualmente.** Rendericé con PyMuPDF a 150–300 dpi y revisé las páginas **3** (Fig. 1 y Tabla 1), **4** (Ecs. 2–5 y Tabla 2, con un recorte ampliado a 300 dpi), **5** (Fig. 2 y Tabla 3), **6** (ecuación de *search precision* y Fig. 3), **8** (Fig. 4), **9** (Fig. 5), **10** (Fig. 6) y **11** (Fig. 7). Las Tablas 1–3 del .txt coinciden con el PDF. Las ecuaciones 1–5 y todas las figuras salieron ilegibles en el .txt; aquí están transcritas desde la imagen.

---

## 1. Referencia completa

- **Autores:** Zhihui Wang, Le Zhang, Jonathan Sagotsky, Thomas S. Deisboeck (autor de correspondencia) [p. 1].
- **Título:** "Simulating non-small cell lung cancer with a multiscale agent-based model" [p. 1].
- **Revista:** *Theoretical Biology and Medical Modelling* 2007, **4**:50 (artículo 50, volumen 4) [p. 1].
- **DOI:** 10.1186/1742-4682-4-50 [p. 1].
- **Fechas:** recibido el 12-jun-2007, aceptado el 21-dic-2007, publicado el 21-dic-2007 [p. 1].
- **URL:** http://www.tbiomed.com/content/4/1/50. Acceso abierto con licencia CC-BY 2.0 [p. 1].
- **Afiliación:** Complex Biosystems Modeling Laboratory, Harvard-MIT (HST) Athinoula A. Martinos Center for Biomedical Imaging, Massachusetts General Hospital, Charlestown, MA [p. 1].
- **Financiación:** NIH CA 113004 (CViT) [p. 12].
- **Páginas:** 14, incluida una página de publicidad de BMC; las referencias ocupan las pp. 12–14.

## 2. Tipo de estudio

- **Tipo:** simulación teórica *in silico*. No genera datos experimentales propios [pp. 1, 6–11].
- **Subtipo:** modelo híbrido multiescala basado en agentes en 2D. Combina una red de 20 ODE intracelulares por célula, reglas discretas de fenotipo y campos químicos continuos (distribución gaussiana más difusión) sobre una rejilla de 200 × 200 [pp. 2, 4–6].
- **Datos de pacientes:** ninguno. Solo hay referencias bibliográficas; por ejemplo, la Tabla 3 cita [72], sobre niveles séricos de TGFα en pacientes con cáncer gastrointestinal [p. 5, p. 14].
- **Datos de líneas celulares:** ninguno propio.
  - Los parámetros cinéticos proceden de modelos publicados: [11] Kholodenko 1999, [12] Schoeberl 2002, [14] Hatakeyama 2003 y [39] Bhalla e Iyengar 1999 [p. 4, Tabla 2].
  - Los umbrales de glucosa proceden de [42], esferoides EMT6/Ro [p. 5, p. 13].
  - La concentración estándar de EGF procede de [51,52]: una línea NSCLC metastásica cerebral (Fang 1996) y una línea de cáncer de ovario (Kurachi 1991) [p. 7, pp. 13–14].

## 3. Pregunta de investigación

Los autores quieren entender cómo las concentraciones extrínsecas de ligando (EGF), a través de la dinámica molecular EGFR-ERK, gobiernan los cambios de fenotipo celular y, con ello, los patrones multicelulares del NSCLC. Lo formulan así: "provide insights into the externally triggered molecular-level dynamics that govern phenotypic changes and thus impact multicellular patterns in NSCLC" [p. 2]. En el resumen examinan "the relationship between extrinsic ligand concentrations, intrinsic molecular profiles and microscopic patterns" [p. 1].

Afirman que es el primer modelo multiescala de NSCLC [p. 2, p. 12]. El modelo extiende la plataforma de glioma del grupo [26–30] [p. 2].

## 4. Métodos: arquitectura multiescala

### 4(a) Nivel molecular: vía EGFR-ERK (20 especies, 19 reacciones, 20 ODE)

**Formulación.** Eq. (1) [p. 2] (transcrita desde la imagen):

$$\frac{d(X_i)}{dt}=\sum v_{\text{production}}-\sum v_{\text{consumption}}$$

Las técnicas son "exactly the same" que en [11,12] [p. 2]. El texto dice: "association and dissociation steps are characterized by first-order and second-order rate constants, respectively" [p. 2]. **[Evaluación del lector]** La frase parece invertida, porque la asociación es de 2.º orden. El resto del artículo y las unidades de la Tabla 2 son coherentes con la convención estándar.

**Fig. 1** [p. 3] es el diagrama cinético. En la vía, el EGF se une a EGFR; el complejo se dimeriza en (EGF-EGFR)2 y se autofosforila (v3, con ATP→ADP). Después siguen la defosforilación v4 (libera Pi), el reclutamiento y la fosforilación de PLCγ (v5–v7), y la defosforilación de PLCγ-P (v8, libera Pi). PLCγ-P se inactiva en PLCγ-P-I (v9) o activa PKC (v10). PKC* activa Raf (v11), Raf* fosforila MEK (v12, v14) y MEK-PP fosforila ERK (v16, v18). Las fosfatasas son v13, v15, v17 y v19. ERK-PP conduce a un nodo "Cell Cycle" que no está formalizado en las ODE.

**Tabla 1: ecuaciones cinéticas y concentraciones iniciales** [p. 3] (verificada visualmente)

| Reactante | Variable molecular | C. inicial [nM] | ODE |
|---|---|---|---|
| X1 | EGF | to be varied | d(X1)/dt = −v1 |
| X2 | EGFR | 80 | d(X2)/dt = −v1 |
| X3 | EGF-EGFR | 0 | d(X3)/dt = v1 − 2v2 |
| X4 | (EGF-EGFR)2 | 0 | d(X4)/dt = v2 + v4 − v3 |
| X5 | EGF-EGFR-P | 0 | d(X5)/dt = v3 + v7 − v4 − v5 |
| X6 | PLCγ | 10 | d(X6)/dt = v8 − v5 |
| X7 | EGF-EGFR-PLCγ | 0 | d(X7)/dt = v5 − v6 |
| X8 | EGF-EGFR-PLCγ-P | 0 | d(X8)/dt = v6 − v7 |
| X9 | PLCγ-P | 0 | d(X9)/dt = v7 − v8 − v9 − v10 |
| X10 | PLCγ-P-I | 0 | d(X10)/dt = v9 |
| X11 | PKC | 10 | d(X11)/dt = −v10 |
| X12 | PKC* | 0 | d(X12)/dt = v10 − v11 |
| X13 | Raf | 100 | d(X13)/dt = −v11 |
| X14 | Raf* | 0 | d(X14)/dt = v11 − v12 − v14 |
| X15 | MEK | 120 | d(X15)/dt = v13 − v12 |
| X16 | MEK-P | 0 | d(X16)/dt = v12 + v15 − v13 − v14 |
| X17 | MEK-PP | 0 | d(X17)/dt = v14 − v15 − v16 − v18 |
| X18 | ERK | 100 | d(X18)/dt = v17 − v16 |
| X19 | ERK-P | 0 | d(X19)/dt = v16 + v19 − v17 − v18 |
| X20 | ERK-PP | 0 | d(X20)/dt = v18 − v19 |

Nota de la tabla: "PKC* and Raf * indicate the activated form of PKC and Raf, respectively" [p. 3].

**Tabla 2: parámetros cinéticos** [p. 4] (verificada visualmente). Unidades según el pie de la tabla: concentraciones y Km (K4, K8, K11–K19) en [nM]; constantes de 1.er orden en [s⁻¹]; de 2.º orden en [nM⁻¹·s⁻¹]; V4, V8 y V11–V19 en [nM·s⁻¹].

| Reacción | Ecuación | Parámetro 1 | Parámetro 2 | Ref. |
|---|---|---|---|---|
| v1 | k1·X1·X2 − k−1·X3 | k1 = 0.003 | k−1 = 0.06 | [11] |
| v2 | k2·X3·X3 − k−2·X4 | k2 = 0.01 | k−2 = 0.1 | [11] |
| v3 | k3·X4 − k−3·X5 | k3 = 1 | k−3 = 0.01 | [11] |
| v4 | V4·X5/(K4 + X5) | V4 = 450 | K4 = 50 | [11] |
| v5 | k5·X5·X6 − k−5·X7 | k5 = 0.06 | k−5 = 0.2 | [11] |
| v6 | k6·X7 − k−6·X8 | k6 = 1 | k−6 = 0.05 | [11] |
| v7 | k7·X8 − k−7·X5·X9 | k7 = 0.3 | k−7 = 0.006 | [11] |
| v8 | V8·X9/(K8 + X9) | V8 = 1 | K8 = 100 | [11] |
| v9 | k9·X9 − k−9·X10 | k9 = 1 | k−9 = 0.03 | [11] |
| v10 | k10·X9·X11 − k−10·X12 | k10 = 0.214 | k−10 = 5.25 | Estimate |
| v11 | V11·X12·X13/(K11 + X13) | V11 = 4 | K11 = 64 | [39] |
| v12 | V12·X14·X15/[K12·(1 + X16/K14) + X15] | V12 = 3.5 | K12 = 317 | [14] |
| v13 | V13·X16/[K13·(1 + X17/K15) + X16] | V13 = 0.058 | K13 = 2200 | [12] |
| v14 | V14·X14·X16/[K14·(1 + X15/K12) + X16] | V14 = 2.9 | K14 = 317 | [12] |
| v15 | V15·X17/[K15·(1 + X16/K13) + X17] | V15 = 0.058 | K15 = 60 | [12] |
| v16 | V16·X17·X18/[K16·(1 + X19/K18) + X18] | V16 = 9.5 | K16 = 1.46 × 10⁵ | [12] |
| v17 | V17·X19/[K17·(1 + X20/K19) + X19] | V17 = 0.3 | K17 = 160 | [12] |
| v18 | V18·X17·X19/[K18·(1 + X18/K16) + X19] | V18 = 16 | K18 = 1.46 × 10⁵ | [12] |
| v19 | V19·X20/[K19·(1 + X19/K17) + X20] | V19 = 0.27 | K19 = 60 | [12] |

**[Evaluación del lector] Observaciones de unidades y consistencia sobre las tablas tal como están publicadas:**

- **Unidades de V11, V12, V14, V16 y V18.** El pie de tabla les asigna [nM·s⁻¹]. Sin embargo, en v11, v12, v14, v16 y v18 multiplican la concentración de una enzima (X12, X14 o X17), así que dimensionalmente deberían estar en [s⁻¹] (son kcat). El pie de tabla es impreciso.
- **Conservación de masa.** Las ODE de la Tabla 1 restan las especies catalíticas como si fueran consumidas:
  - PKC* (X12) se descuenta en v11.
  - Raf* (X14) se descuenta en v12 y v14.
  - MEK-PP (X17) se descuenta en v16 y v18.
  - En consecuencia, el total de MEK no se conserva: d(X15+X16+X17)/dt = −v16 − v18. Tampoco se conservan el total de Raf (−v12 − v14) ni el de PKC (−v11).
  - El total de ERK sí se conserva: d(X18+X19+X20)/dt = 0.
  - Puede tratarse de una decisión de diseño o de un error de transcripción; el artículo no lo comenta.
- **K16 y K18.** Valen 1.46 × 10⁵ nM. Con ERK ≈ 100 nM, v16 y v18 quedan prácticamente lineales y muy lentos (véase la sección 12).
- **Acoplamiento X1 ↔ entorno.** La concentración inicial de EGF es "to be varied" [p. 3]. No se especifica cómo el EGF local del entorno se asigna a X1 en cada paso de tiempo. **No reportado.**
- **Lectura de ROC.** Los paneles de la Fig. 6 [p. 10] están rotulados "Change of PLCγ (nM)" (empieza en 10 nM y decae) y "ROC of PLCγ (nM/s)" (positiva). Esto sugiere que ROC_PLC ≈ −d(X6)/dt, pero no se define explícitamente.
- **Especie de "ERK" en ROC_ERK.** No se dice si se refiere a X18 (ERK), a X20 (ERK-PP) o a otra. **No reportado.**

### 4(b) Nivel celular: reglas de decisión fenotípica [pp. 5–6, Fig. 3]

- **Fenotipos:** proliferación, migración, quiescencia y muerte [p. 5].
- **Muerte:** la glucosa local cae por debajo de 8 mM [42] [p. 5].
- **Quiescencia** [p. 5]. La célula queda quiescente en cualquiera de estos casos:
  - la glucosa local está entre 8 y 16 mM;
  - no cumple las condiciones de migración o proliferación;
  - no encuentra una posición vacía.
- **Migración:** la decide la tasa de cambio de PLCγ (ROC_PLC). Si ROC_PLC supera el umbral T_PLC, la célula "has the potential to migrate" [p. 6]. Justificación: [43–46].
- **Proliferación:** la decide la tasa de cambio de ERK (ROC_ERK) frente al umbral T_ERK [p. 6]. Justificación: [33, 47–50].
- **Valores de T_PLC y T_ERK: No reportados** en ninguna parte del artículo.
- **Matriz de decisión** (Fig. 3, p. 6, verificada visualmente):

| Condición | Resultado |
|---|---|
| (i) ROC_PLC < T_PLC y ROC_ERK < T_ERK | Sin cambio ("No change") |
| (ii) ROC_PLC > T_PLC y ROC_ERK < T_ERK | Migración |
| (iii) ROC_PLC < T_PLC y ROC_ERK > T_ERK | Proliferación |
| (iv) ROC_PLC > T_PLC y ROC_ERK > T_ERK | **Regla A:** migración. **Regla B:** proliferación |

  Las condiciones (i)–(iii) son las "general rules"; A y B, las "special rules" [p. 6]. Para (iv) los autores dicen: "in the absence of any specific experimental data … we explored two hypotheses" [p. 6].
- **Selección de posición (*search precision*)** [p. 6]. Ecuación sin número, transcrita desde la imagen:

$$T_{ij}=\psi\cdot L_{ij}+(1-\psi)\cdot\varepsilon_{ij},\qquad \varepsilon\sim N(\mu,\sigma^2),\ \psi\in[0,1]$$

  - Con ψ = 0 la célula hace un paseo aleatorio; con ψ = 1 elige la posición de mayor glucosa.
  - ψ = 0.7, tomado de [27] porque "tends to lead to the highest average velocity" [p. 6].
  - L_ij se remite a [27] y **no se define en este artículo**.
  - Valores de μ y σ²: **No reportados**.
  - Candidatos: "those grid points surrounding the cell" [p. 6]. No se dice si es vecindad de Moore u otra. **No reportado.**
- **Ocupación:** una célula por punto de rejilla [p. 4]. Si una célula no encuentra posición libre, queda quiescente y vuelve a buscar en el siguiente paso [p. 6].
- **Herencia molecular de la célula hija, duración del ciclo celular y reinicio de las ODE tras la división: No reportados.** El nodo "Cell Cycle" de la Fig. 1 no está formalizado.
- **Orden de actualización de agentes** (secuencial o aleatorio): **No reportado.**

### 4(c) Nivel microambiente [pp. 4–5, Tabla 3]

- **Rejilla:** 2D, 200 × 200 puntos, p(i, j) con índices enteros [p. 4, Fig. 2].
- **Fuente de nutrientes:** una sola fuente, en p(150, 150), que simula un vaso sanguíneo en corte transversal [p. 4].
- **Células semilla:** M × N centradas en la rejilla; en los resultados, 7 × 7 = 49 [p. 4, p. 6]. Según la Fig. 2 [p. 5], el bloque está centrado aproximadamente en p(100, 100). Los IDs de esquina son 0 (1,1), 6 (M,1), 42 (1,N) y 48 (M,N). El texto dice "left to right, bottom to top" [p. 6].
  - **[Evaluación del lector]** Hay una ambigüedad: la tabla de la Fig. 2 asigna Cell 6 a (M,1) y la llama "top-left" [p. 7], mientras que el gráfico rotula el eje vertical como M y el horizontal como N.
- **Campos iniciales** (Ecs. 2–4) [p. 4], transcritos desde la imagen, con d_ij = distancia a la fuente:

$$EGF^{ij}=T_m\cdot\exp(-2d_{ij}^2/\sigma_t^2)$$
$$Glucose^{ij}=G_a+(G_m-G_a)\cdot\exp(-2d_{ij}^2/\sigma_g^2)$$
$$Oxygen^{ij}=O_a+(O_m-O_a)\cdot\exp(-2d_{ij}^2/\sigma_o^2)$$

- **Difusión** (Eq. 5) [p. 4], transcrita desde la imagen:

$$\frac{\partial M^{ij}}{\partial t}=D_M\cdot\nabla^2 M^{ij},\qquad t=1,2,3,\dots$$

  M es uno de los tres cues y t un paso de tiempo. Los cues difunden "with a fixed rate" durante toda la simulación [p. 4].
- **Coeficientes:** Tabla 3, transcrita en la sección 5 [p. 5]. Además, "(see also [30] for more details)" [p. 4].
- **Anchuras σ_t, σ_g y σ_o: No reportadas.** No aparecen en la Tabla 3, aunque el texto afirma que "The coefficients in Eqs. (2–5) are listed in Table 3" [p. 4].
- **Consumo y secreción:**
  - La glucosa es "continuously taken up by cells" [p. 4]; tasa **No reportada**.
  - Las células consumen EGF propio y el secretado por células adyacentes, en forma autocrina y paracrina [40,41] [p. 4]. Tasas de secreción y consumo de EGF: **No reportadas**.
  - Consumo de oxígeno: **No reportado.** El oxígeno no interviene en ninguna regla de decisión descrita.
- **Contorno:** solo p(150, 150) se repone en cada paso; el resto de puntos no se repone [p. 4]. Condición en los bordes de la rejilla (Dirichlet, Neumann o periódica): **No reportada.**
- **Escalas físicas:**
  - Espaciado de rejilla (µm por punto): **No reportado.**
  - Duración de un paso de tiempo en segundos: **No reportada.**
  - Discretización numérica del laplaciano: **No reportada.**
  - **[Evaluación del lector]** Los coeficientes D vienen en m²·s⁻¹, pero sin Δx ni Δt no pueden convertirse a unidades de rejilla.

### 4(d) Algoritmo, pasos de tiempo y software

- **Lenguaje:** "Our algorithm was implemented in C/C++" [p. 6].
- **Bucle por paso** [pp. 4–5]:
  1. Cada célula integra su red molecular.
  2. El sistema registra el perfil molecular de cada célula para decidir su fenotipo en el paso siguiente.
  3. Entre pasos se actualizan EGF, glucosa y O₂ según la Eq. (5).
- **Parada:** la simulación termina cuando la primera célula alcanza la fuente [p. 5, p. 7].
- **Integrador de ODE, paso interno, tolerancias y número de segundos de ODE por paso de ABM: No reportados.**
- **Hardware y tiempo de cómputo: No reportados.**
- **Visualización:** **No reportado.** **[Evaluación del lector]** Los gráficos tienen estilo MATLAB, pero el artículo no lo dice.

## 5. Tabla de parámetros

| Símbolo | Significado | Valor | Unidad | Origen | Ubicación |
|---|---|---|---|---|---|
| k1, k−1 … V19, K19 | Constantes cinéticas v1–v19 | véase la Tabla 2 (sección 4a) | s⁻¹, nM⁻¹·s⁻¹, nM, nM·s⁻¹ | [11] v1–v9; estimado en v10; [39] v11; [14] v12; [12] v13–v19 | Tabla 2, p. 4 |
| X1(0) | EGF intracelular inicial | "to be varied" | nM | — | Tabla 1, p. 3 |
| X2(0) | EGFR | 80 (800 en la Fig. 7) | nM ("per system") | No especificado | Tabla 1, p. 3; p. 11 |
| X6(0) | PLCγ | 10 | nM | "See Table 2 for references" | Tabla 1, p. 3 |
| X11(0) | PKC | 10 | nM | ídem | Tabla 1, p. 3 |
| X13(0) | Raf | 100 | nM | ídem | Tabla 1, p. 3 |
| X15(0) | MEK | 120 | nM | ídem | Tabla 1, p. 3 |
| X18(0) | ERK | 100 | nM | ídem | Tabla 1, p. 3 |
| Resto de Xi(0) | Complejos y formas fosforiladas | 0 | nM | — | Tabla 1, p. 3 |
| Tm | Concentración máxima de EGF | 2.56 | "Nm" (probablemente una errata de nM) | [72,73] | Tabla 3, p. 5 |
| Ga | Glucosa normal | 17.0 | mM | [72,73] | Tabla 3, p. 5 |
| Gm | Glucosa máxima | 57.0 | mM | [72,73] | Tabla 3, p. 5 |
| Oa | Oxígeno normal | 0.0017 | "DC" (unidad no definida) | [72,73] | Tabla 3, p. 5 |
| Om | Oxígeno máximo | 0.0025 | "DC" | [72,73] | Tabla 3, p. 5 |
| D_EGF | Difusión de EGF | 6.7 × 10⁻¹¹ | m²·s⁻¹ | [72,73] | Tabla 3, p. 5 |
| D_Glucose | Difusión de glucosa | 5.18 × 10⁻¹¹ | m²·s⁻¹ | [72,73] | Tabla 3, p. 5 |
| D_Oxygen | Difusión de O₂ | 8.0 × 10⁻⁹ | m²·s⁻¹ | [72,73] | Tabla 3, p. 5 |
| σ_t, σ_g, σ_o | Anchura de las gaussianas iniciales | **No reportado** | — | — | Ecs. 2–4, p. 4 |
| — | Umbral de muerte por glucosa | < 8 | mM | [42] | p. 5 |
| — | Rango de quiescencia por glucosa | 8–16 | mM | [42] (implícito) | p. 5 |
| T_PLC | Umbral de ROC_PLC | **No reportado** | (nM/s, según la Fig. 6) | — | p. 6 |
| T_ERK | Umbral de ROC_ERK | **No reportado** | (nM/s) | — | p. 6 |
| ψ | Precisión de búsqueda | 0.7 | adimensional | [27] | p. 6 |
| μ, σ² | Media y varianza del error ε | **No reportado** | — | — | p. 6 |
| L_ij | Función de evaluación de posición | definida en [27], no aquí | — | [27] | p. 6 |
| — | Rejilla | 200 × 200 | puntos | Supuesto de diseño | p. 4 |
| — | Posición de la fuente | p(150, 150) | índice | Supuesto | p. 4 |
| M × N | Células semilla | 7 × 7 = 49 | células | Supuesto | p. 6 |
| — | EGF "estándar" | 2.56 nM (p. 7, Tabla 3) / "2.65 × 1.0 nM" (pp. 7, 10, 11) | nM | [51,52], "rescaled to fit our model" | p. 7 |
| — | Tasas de consumo de glucosa y EGF, secreción de EGF, Δx, Δt | **No reportado** | — | — | — |

**[Evaluación del lector]** El texto dice que "most of the pathway's parameters, including rate constants and initial component concentrations were obtained from the experimental literature" [p. 12]. Sin embargo, la Tabla 2 cita sobre todo modelos computacionales previos ([11], [12], [14], [39]), no mediciones directas.

## 6. Experimentos simulados y resultados

Las lecturas numéricas "≈" proceden de inspeccionar visualmente las figuras y son aproximadas; las cifras sin "≈" están en el texto o en los pies de figura.

### 6.1 Regla A frente a regla B con EGF estándar de 2.56 nM (Fig. 4, p. 8; texto p. 7)

- **Regla A:** primero hay proliferación *in situ* y después una migración extensa hacia la fuente [p. 7].
  - Instantáneas en los pasos 1, 40, 80, 120 y 145 [Fig. 4a, p. 8].
  - La corrida termina hacia el paso 145.
  - Al final hay ≈ 175 células en total, de las cuales ≈ 140 son migratorias y ≈ 18 proliferativas y ≈ 17 quiescentes; ninguna muerta [Fig. 4b izquierda].
- **Regla B:** la expansión es concéntrica y estacionaria, sin expansión espacial apreciable por motilidad [p. 7].
  - Instantáneas en los pasos 1, 125, 250, 375 y 500 [Fig. 4a].
  - Al paso 500 hay ≈ 1980 células en total: ≈ 920 muertas, ≈ 690 quiescentes, ≈ 350 proliferativas y ≈ 20 migratorias [Fig. 4b derecha].
  - El tiempo de ejecución es "considerably longer" [p. 7]. **[Evaluación del lector]** Tampoco se aclara si la corrida B se detuvo en el paso 500 sin que ninguna célula llegara a la fuente.
- **Comparación de poblaciones:** "for rule B, the [total] cell population … exceeds the one achieved through rule A by a factor of 10" [p. 7].
- **Fenotipos:** el texto dice que ambas reglas generan "all three cell phenotypes" [p. 7]. Sin embargo, la Fig. 4b muestra además células muertas (gris) en la regla B.

### 6.2 Peso de las reglas especiales (Fig. 5, p. 9)

- **Regla A:** la mayoría de las migraciones se deben a ella y no a la regla general. Pendiente del ajuste lineal por mínimos cuadrados: **1.40 cells/step** [Fig. 5a, p. 9].
- **Regla B:** pendiente de las proliferaciones mediadas por la regla B: **0.03 cells/step** [Fig. 5b, p. 9].
- **Conclusión de los autores:** la influencia de la regla A sobre la migración es "more substantial" que la de la regla B sobre la proliferación [p. 7].
- **Caída final de la curva roja:** se debe a la terminación de la corrida [pie de la Fig. 5].
- **Pico inicial:** en ambos casos hay un pico de ≈ 49 proliferaciones hacia el paso 10–12; es decir, las 49 semillas proliferan a la vez [Fig. 5, lectura visual].

### 6.3 Barrido de EGF con la regla A y transición de fase en la célula 48 (Fig. 6, p. 10; texto p. 7)

- **Barrido:** EGF desde "2.65 × 1.0 nM" hasta "2.65 × 50.0 nM", "by an incremental increase of 0.1 nM in each simulation" [p. 7].
  - **[Evaluación del lector]** El incremento real es 0.1 en el multiplicador (0.265 nM), lo que implica unas 491 corridas.
- **A más EGF, finalización más rápida:** las corridas con EGF alto terminan antes [p. 7].
- **Transición de fase en la célula 48:**
  - Las proliferaciones disminuyen de forma gradual y desaparecen entre **2.65 × 31.1 y 2.65 × 31.2 nM** (≈ 82.4 y 82.7 nM) [p. 7; pie de la Fig. 6, p. 10].
  - Los picos de ROC_PLC y el punto de inflexión de ROC_ERK se adelantan al aumentar el EGF [p. 7].
  - Lectura visual de la Fig. 6 [p. 10]:

| EGF (multiplicador × 2.65 nM) | Fin de la corrida | Pico de ROC_PLC | ROC_ERK máx. |
|---|---|---|---|
| ×1.0 | ≈ paso 148 | sin pico; ≈ 0.045 nM/s al final | ≈ 5.7 × 10⁻⁶ nM/s |
| ×31.1 | ≈ paso 133 | ≈ 0.22 nM/s en el paso ≈ 100 | ≈ 0.04 nM/s |
| ×31.2 | ≈ paso 104 | ≈ 0.24 nM/s en el paso ≈ 75 | ≈ 0.034 nM/s |
| ×50.0 | ≈ paso 101 | ≈ 0.26 nM/s en el paso ≈ 65 | ≈ 0.05 nM/s |

- **Otras células de esquina:** en las células 0, 6 y 42 no aparece transición de fase ("data not shown") [p. 7].
- **Robustez:** la transición se mantiene si el centro del bloque inicial se sortea en el cuadrado p(100,100)–p(110,110) (**5 runs, data not shown**) [pp. 7–8].

### 6.4 Sobreexpresión de EGFR: 800 nM frente a 80 nM (Fig. 7, p. 11; texto p. 11)

- **Efecto general:** hay "even *more* migration and does so *earlier*" [p. 11].
- **Transición de fase:** se produce antes, entre **2.65 × 5.9 y 2.65 × 6.0 nM** (≈ 15.6 y 15.9 nM) [pie de la Fig. 7, p. 11].
- **Rates máximos:** los ROC_PLC y ROC_ERK máximos alrededor de la transición son menores que en la Fig. 6 [pie de la Fig. 7].
  - Lectura visual de ROC_PLC: ≈ 0.098, ≈ 0.16 y ≈ 0.18 nM/s.
  - Lectura visual de ROC_ERK: ≈ 0.017, ≈ 0.030 y ≈ 0.019 nM/s.
- **Carácter preliminar:** los autores lo presentan como "preliminary data" [p. 11].

## 7. Calibración y validación

- **Calibración formal:** no hay ajuste de parámetros a datos. Los parámetros se toman de la literatura y uno es estimado (v10) [p. 4, p. 12]. El EGF estándar está "rescaled to fit our model" sin explicar cómo [p. 7].
- **Validación cuantitativa:** **ninguna.** No se compara ningún resultado numérico con datos experimentales de NSCLC.
- **Correspondencia cualitativa, solo narrativa:**
  - Más EGF da un tumor más agresivo, en línea con [5–8] [p. 10].
  - La sensibilidad a señales migratorias concuerda con datos de células de cáncer de mama [57,58] [p. 10].
  - El comportamiento "no proliferation, just migration" se ha descrito en varias líneas [59,60] y en células humanas no cancerosas [61] [p. 10].
  - La sobreexpresión de EGFR amplifica la señal, como en [66] (células epiteliales mamarias) [pp. 11–12].
- **Validación pendiente según los propios autores:** "future works will have to include not only proper experimental verification of the estimated parameters and evaluation of the simulation results" [p. 12]. Describen el modelo como un paso hacia "a fully validated in silico model" [p. 12].

## 8. Sensibilidad, incertidumbre y estocasticidad

- **Fuente de estocasticidad:** el término ε ~ N(μ, σ²) en la selección de posición [p. 6]. Las ODE son deterministas.
- **Réplicas:** las Figs. 4 y 5 muestran una única corrida por regla ("the two simulation runs reported in Fig. 4") [p. 7]. En las Figs. 6 y 7 se muestran 4 y 3 corridas, una por concentración.
- **Robustez:** solo 5 corridas con el centro del bloque inicial aleatorio, "data not shown" [p. 8].
- **Semillas aleatorias: No reportadas.**
- **Dispersión** (intervalos, desviaciones): **No reportada.**
- **Análisis de sensibilidad paramétrica:** **no realizado.** Se propone como trabajo futuro ("techniques such as sensitivity analysis to help determine the effects of parameter uncertainties on model outcome [67]") [p. 12].
- **Exploración paramétrica real:** el barrido de EGF (×1.0 a ×50.0, paso 0.1), dos niveles de EGFR (80 y 800 nM) y dos reglas especiales (A y B). ψ queda fijo en 0.7.

## 9. Limitaciones declaradas

1. Parámetros heterogéneos: "this data naturally originated from a variety of often stationary experimental settings and different cell types" [p. 12].
2. Datos de menor calidad que series temporales: "represents a less desirable and reliable input than time series data that come from one experimental setting only" [p. 12].
3. Parámetros estimados: "some parameters had to be estimated" [p. 12].
4. Simplificación de la vía: "in reality these molecules fulfil their functions by interacting with a multitude of other molecular species" [p. 2]. También: "a pathway model cannot be a biological representation in every detail" [p. 12].
5. Falta PI3K/PTEN/AKT; se plantea añadirla [p. 12].
6. Faltan interacciones célula-célula y célula-matriz, y un entorno más heterogéneo [p. 12].
7. Falta modelar la regulación al alza o a la baja de moléculas clave por la tumorigénesis; la Fig. 7 es un primer paso [p. 11].
8. Regla (iv) sin respaldo: "in the absence of any specific experimental data" [p. 6]. Además, "rule B did not receive similar attention in our analysis" [p. 10].
9. Fuente no reabastecida no explorada (trabajo futuro) [p. 12].

## 10. Evaluación del lector

- **[Evaluación del lector] Validez biológica.**
  - El modelo es una prueba de concepto. La decisión fenotípica se basa en derivadas temporales (ROC) de PLCγ y ERK frente a umbrales cuyos valores no se publican, y el desempate (iv) es una hipótesis explícita.
  - El "nivel NSCLC" está en la selección de moléculas, que tienen relevancia documentada en NSCLC [31–35], no en los parámetros.
  - La estequiometría publicada consume las enzimas catalíticas (PKC*, Raf*, MEK-PP), lo que es atípico.
  - La geometría (una sola fuente puntual, 2D, campo gaussiano) es una abstracción del grupo de glioma reutilizada [pp. 2, 4].
  - El "phase transition" es un umbral discreto cruzado por una señal continua. Su interpretación como transición de fase es fenomenológica.
- **[Evaluación del lector] Sin validación.** No hay comparación cuantitativa con datos de NSCLC (sección 7), y los resultados clave se apoyan en corridas únicas.
- **[Conocimiento externo del lector, no declarado en el documento] Origen celular de los parámetros.**
  - [11] (Kholodenko 1999) es un modelo de hepatocitos de rata.
  - [12] (Schoeberl 2002) es un modelo calibrado en células HeLa.
  - [14] (Hatakeyama 2003) trata la señalización por heregulina en células de cáncer de mama (MCF-7).
  - [39] (Bhalla e Iyengar 1999) es un modelo genérico de redes de señalización.
  - Los umbrales de glucosa vienen de esferoides EMT6/Ro, carcinoma mamario murino [42; título en p. 13].
  - La difusión de EGF procede de cerebro de rata [73; título en p. 14].
  - El documento solo reconoce "different cell types" [p. 12]. **Ningún parámetro procede de células NSCLC**, salvo, en parte, la concentración de EGF [51].
- **[Evaluación del lector] Relevancia actual.**
  - No se modelan los TKI de EGFR (gefitinib, erlotinib, osimertinib) ni las mutaciones activadoras de EGFR (L858R, del19, T790M), aunque la ref. [1] trata mutaciones de EGFR y la [17] la sensibilidad a gefitinib [p. 12].
  - Tampoco se modelan KRAS, la vía PI3K/AKT (reconocido en p. 12), la internalización o tráfico del receptor ni la retroalimentación negativa ERK→SOS/Raf.
  - Es útil como antecedente histórico y como plantilla arquitectónica (ODE por agente → umbral → fenotipo), no como modelo predictivo actual.
- **[Evaluación del lector] Inconsistencias internas.**
  - EGF estándar: 2.56 nM [p. 7; Tabla 3] frente a 2.65 × 1.0 nM [pp. 7, 10, 11].
  - Unidad "Nm" en Tm y "DC" sin definir para el oxígeno [Tabla 3].
  - "Incremental increase of 0.1 nM" cuando el incremento es del multiplicador [p. 7].
  - Color de las proliferativas: "light blue" en el texto [p. 7] frente a azul oscuro en el pie de la Fig. 4 [p. 8].
  - Pie de la Tabla 2 con unidades de V incompatibles con las kcat de v11, v12, v14, v16 y v18.

## 11. Disponibilidad de código y datos

- **Código:** **No reportado.** No hay enlace, repositorio ni archivo suplementario. Lo único relacionado: "Our algorithm was implemented in C/C++" [p. 6], y en las contribuciones, "ZW developed the NSCLC model (algorithm and code)" [p. 12].
- **Datos de salida: No reportados.**
- **Sección de disponibilidad:** el artículo no tiene ninguna.

## 12. Reproducibilidad

**Reproducible con lo publicado.** El **submodelo molecular aislado** (20 ODE, Tablas 1–2) puede implementarse íntegramente en Python con `scipy.integrate.solve_ivp`, ya que están todas las ecuaciones, constantes y condiciones iniciales.

**[Evaluación del lector] Verificación exploratoria.** Implementé las Tablas 1–2 tal como están publicadas (LSODA, 3000 s, EGF fijo como condición inicial, sin entorno). Fue un script temporal en el scratchpad; no se guardó en el proyecto. Resultados:

- **Estabilidad numérica:** el sistema es estable y no produce concentraciones negativas.
- **PLCγ:** X6 decae desde 10 nM; −dX6/dt alcanza máximos de ≈ 0.012, 0.54 y 0.69 nM/s con EGF de 2.56, 82.7 y 132.5 nM.
- **ERK:** X20 (ERK-PP) es prácticamente nula (< 10⁻³ nM) y −dX18/dt queda ≤ 5 × 10⁻⁴ nM/s. Esto parece deberse a K16 = K18 = 1.46 × 10⁵ nM.
- **Discrepancia con la Fig. 6:** ROC_ERK llega allí hasta ≈ 0.05 nM/s, unas 100 veces más.
- **Interpretación:** puede significar que (a) el código original difiere de las tablas; (b) "ERK" en ROC_ERK no se refiere a X18; (c) el EGF del entorno se inyecta de forma continua; o (d) el mapeo de pasos de ABM a segundos no es trivial. **No es posible decidirlo con lo publicado.**

**Reproducible solo de forma cualitativa:**

- la diferencia de patrón entre las reglas A y B (migración dirigida frente a crecimiento concéntrico) [Fig. 4];
- la existencia de un umbral de EGF por encima del cual una célula deja de proliferar;
- el desplazamiento de ese umbral hacia valores menores al aumentar EGFR [Figs. 6–7].

**Lo que falta para una reproducción cuantitativa de las Figs. 4–7:**

1. Los valores de **T_PLC y T_ERK** [p. 6]. Son críticos.
2. La definición operativa de ROC: qué especie se usa (X6 o PLCγ total; X18 o X20) y si es derivada instantánea o diferencia entre pasos.
3. La **duración de un paso de tiempo** (s) y el tiempo de integración de las ODE por paso.
4. Las anchuras **σ_t, σ_g y σ_o** de las Ecs. 2–4.
5. El **espaciado de rejilla** (Δx), el esquema numérico del laplaciano y las condiciones de borde.
6. Las tasas de **consumo de glucosa** y de **secreción y consumo de EGF**, y cómo el EGF local se asigna a X1 en cada paso.
7. La función **L_ij** (remitida a [27]), los valores de **μ y σ²** de ε y la vecindad de búsqueda.
8. Qué ocurre en la división: herencia del estado de las ODE, reinicio y destino de la hija.
9. El orden de actualización de agentes, las semillas y el número de réplicas.
10. Las unidades del oxígeno ("DC") y la función del O₂ en las reglas, que no está descrita.

**Conclusión.** El submodelo molecular sí es reproducible de forma aislada; el ABM completo, no sin supuestos adicionales sustanciales.

## 13. Problemas de extracción

- **Ecuaciones 1–5 y ecuación T_ij:** en el .txt salen fragmentadas, con símbolos en líneas separadas [txt, líneas 169–180 y 417–497]. Están transcritas aquí desde el PDF renderizado [pp. 2, 4, 6].
- **Figuras 1–7:** el texto embebido sale como basura (glifos de fuentes Symbol, por ejemplo "+,*-,.-*", "!Ȗ") [txt de pp. 3, 6, 8–11]. Las figuras se revisaron visualmente.
- **Tablas 1–3:** extraídas en una columna por celda, pero con valores correctos. Coinciden con el PDF en las pp. 3–5.
- **Superíndices:** "1.46 × 105" en el .txt corresponde a 1.46 × 10⁵. "6.7 × 10-11" corresponde a 6.7 × 10⁻¹¹. "m2·s-1" corresponde a m²·s⁻¹.
- **Errores tipográficos del original** (no son de la extracción): "Nm" en Tm; "DC" sin definir; "may seems" [p. 10].
- **Página 14:** mezcla publicidad de BMC con las referencias 51 (continuación) a 73.
- **Pérdidas de información:** ninguna detectada en el texto corrido.

## 14. Citas textuales clave

1. "A novel, data-driven switch that is operated by two key molecules, i.e. phospholipase Cγ (PLCγ) and extracellular signal-regulated kinase (ERK), processes the phenotypic decision at the cellular level." [p. 2]
2. "Our model is based on a total of 20 ordinary differential equations (ODEs) and uses exactly the same modeling techniques as other pathway analysis studies" [p. 2]
3. "Only the nutrient source, p(150, 150), is replenished at each time step while all other grid points are not." [p. 4]
4. "Cell death is triggered when the on site glucose concentration drops below 8 mM [42]." [p. 5]
5. "if ROC_PLC exceeds a certain set threshold, T_PLC, the cell has the potential to migrate." [p. 6]
6. "in the absence of any specific experimental data … we explored two hypotheses: 'rule A' yielding migration advantage … whereas 'rule B' resulting in a proliferation advantage" [p. 6]
7. "this concentration is derived from the literature [51,52] and has been rescaled to fit our model as a benchmark starting point" [p. 7]
8. "for rule B, the [total] cell population of the tumor system exceeds the one achieved through rule A by a factor of 10." [p. 7]
9. "if the ligand concentration starts to exceed 2.65 × 31.2 nM, its proliferative trait entirely disappears." [p. 7]
10. "Slopes of the fitting curves are 1.40 cells/step in (a) and 0.03 cells/step in (b), respectively." [p. 9, pie de la Fig. 5]
11. "this data naturally originated from a variety of often stationary experimental settings and different cell types." [p. 12]
12. "future works will have to include not only proper experimental verification of the estimated parameters and evaluation of the simulation results but also … sensitivity analysis" [p. 12]
