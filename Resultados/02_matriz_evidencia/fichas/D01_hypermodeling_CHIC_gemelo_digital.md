# Ficha D01: hipermodelo CHIC (Oncosimulator + hipomodelos) como gemelo digital del cáncer

> Fuente: texto extraído (`00_extraccion_texto/A Multidisciplinary Hyper-Modeling Scheme in Personalized.txt`, 37 páginas) y verificación visual del PDF original.
> **Páginas del PDF que verifiqué visualmente** (renderizadas a imagen con PyMuPDF): 5, 9, 10, 11, 12, 14, 15, 18, 19, 20, 22, 23, 30, 31, 32, 33. Las ecuaciones (2)–(10) y (A1)–(A9) se transcribieron desde esas imágenes, no desde el texto extraído.
> Convención: [p. N] = página del artículo (coincide con la página del PDF). Lo marcado **[Lector]** es interpretación mía y no afirmación de los autores.

---

## 1. Referencia completa

Kolokotroni E, Abler D, Ghosh A, Tzamali E, Grogan J, Georgiadi E, Büchler P, Radhakrishnan R, Byrne H, Sakkalis V, Nikiforaki K, Karatzanis I, McFarlane NJB, Kaba D, Dong F, Bohle RM, Meese E, Graf N, Stamatakos G; on behalf of the CHIC Project Consortium. *A Multidisciplinary Hyper-Modeling Scheme in Personalized In Silico Oncology: Coupling Cell Kinetics with Metabolism, Signaling Networks, and Biomechanics as Plug-In Component Models of a Cancer Digital Twin.* J. Pers. Med. 2024, 14, 475. doi:10.3390/jpm14050475. Recibido el 3 de marzo de 2024, aceptado el 17 de abril de 2024 y publicado el 29 de abril de 2024. Licencia CC BY 4.0 [p. 1].
Financiación: FP7 de la UE, acuerdo n.º 600841 "CHIC" [p. 29]. Ética: Ärztekammer des Saarlandes, 104/10 del 19 de agosto de 2013 (uso retrospectivo de datos de WT y NSCLC) [p. 29].

## 2. Tipo de estudio, cánceres modelados y datos de pacientes

- **Tipo de estudio:** artículo metodológico de modelado multiescala e integración ("hipermodelo"), con estudios de prueba de concepto *retrospectivos* sobre casos individuales. No es un ensayo clínico ni un estudio de cohorte [pp. 2–3, 17, 20].
- **Cánceres modelados: DOS.**
  1. **Cáncer de pulmón no microcítico (NSCLC), adenocarcinoma**, tratado con **radioterapia externa** ("Lung Oncosimulator") [p. 3; §3.1, pp. 17–20].
  2. **Tumor de Wilms (nefroblastoma, WT)**, tratado con **quimioterapia preoperatoria con vincristina y actinomicina D** [p. 3; §3.2, pp. 20–22].
  - **Glioblastoma:** no se modela. La única mención cerebral es que el acoplamiento OS–BMS "have been tested successfully for brain tumor simulation [39]" en trabajos previos [p. 12], y que el efecto de masa importa clínicamente "such as the brain" [p. 7].
- **Hay componentes específicos de cáncer de pulmón:** sí, el documento ES parcialmente de cáncer de pulmón:
  - Lung Oncosimulator con radioterapia y modelo LQ [pp. 3–4].
  - Hipomodelo molecular que incorpora mutaciones EGFR, KRAS, BRAF y "AML/ALK" para pulmón [p. 12], además de mutantes EGFR (L858R y deleciones) en la red ErbB [p. 4].
  - Hipomodelo metabólico con restricciones de clusters proteómicos de LADC (C15) y LSCC (C10) tomados de Li et al. [47] [p. 14, Tabla 3].
  - BMS con tejidos torácicos (pulmón, bronquios, hueso, órganos internos) [p. 16, Tabla 5; Fig. 6, p. 17].
  - Tabla 7 de parámetros del Oncosimulator para NSCLC [p. 18].
- **Datos de pacientes** (todos del proyecto CHIC, FP7-ICT-600841, anonimizados [p. 3]; Hospital Universitario del Sarre, Homburg [pp. 17, 20]):
  - **NSCLC: n = 1.** Mujer de 63 años con recurrencia de un adenocarcinoma estadio IB (pT2aN0M0, TNM 7.ª ed.), patrón acinar, grado II [p. 17]. Variables usadas:
    - Ki-67 = 23 %.
    - KRAS G12C, sin alteraciones de EGFR, BRAF, ALK ni ROS-1.
    - Expresión de 2549 miRNA en tejido tumoral y normal, con normalización por cuantiles.
    - Dos TC previas a la RT (volúmenes ≈ 4.5 y 5.5 cc, día 0 y día 98) y una TC de seguimiento a ~1 año (día 480, "no visible tumor") [p. 17; Fig. A2 y Tabla A1, p. 32].
    - Esquema de RT: 4 × 15 Gy (total 60 Gy) en los días 104, 107, 110 y 113 [Fig. A2, p. 32].
    - Supuesto: la mutación, los miRNA y el Ki-67 del primario se toman como válidos para la recurrencia [p. 17].
  - **WT: n = 2 en el análisis de respuesta (§3.2)** y **n = 3 en total**, porque aparece un "Case 3" en la Fig. 9 [p. 23] y en la Tabla A2 [p. 33]. Variables usadas:
    - miRNA séricos normalizados.
    - Esquema de quimioterapia (SIOP 2001/GPOH).
    - RM antes y después de la quimioterapia [p. 20].
    - Volúmenes: Caso 1 de 78.54 → 7.32 cc (−90.68 %); Caso 2 de 109 → 52 cc (−52.29 %); Caso 3 de 754.75 → 147.68 cc (−80.43 %) [Tabla A2, p. 33].
    - Sin biopsia ni histología disponibles [p. 20].
- **Los datos ya no son accesibles** ("ceased to be accessible one year after the completion of the CHIC project") [p. 29].

## 3. Pregunta y objetivo

- **General:** presentar un esquema de hipermodelado capaz de "combine models of diverse cancer aspects regardless of their underlying method or scale". Integra datos clínicos, de tratamiento, de imagen y genómicos, y permite reemplazar hipomodelos por otros equivalentes [p. 2].
- **Preguntas clínicas de las pruebas de concepto:**
  - **NSCLC:** predecir si habrá recurrencia (mediante la TCP) y el volumen del tumor un año después de la RT, comparando 3 escenarios [p. 18].
  - **WT:** relacionar el perfil proliferativo con la respuesta a la quimioterapia neoadyuvante y saber si el tumor se reducirá [pp. 20–21, 24].
  - **Forma y posición:** evaluarlas mediante la distancia entre centros de masa [§3.3, pp. 21–22].

## 4. Métodos por componente

**Arquitectura** [Fig. 2, p. 9]. Son cinco hipomodelos:
- **Oncosimulator (OS):** el integrador, desarrollado por ICCS/NTUA.
- **Molecular:** de UPenn.
- **Metabólico:** de FORTH.
- **Vasculatura:** de Oxford.
- **Biomecánica (BMS):** de Berna.

Hay dos tipos de acoplamiento:
- **Secuencial/unidireccional** (molecular → OS) mediante TAVERNA, que pasa el CKR como argumento de línea de comandos [p. 9].
- **Iterativo/dinámico** (OS ↔ vasculatura ↔ metabólico, y OS ↔ BMS) mediante MUSCLE 2 [pp. 10–11].

### 4.1 Oncosimulator: cinética celular discreta (§2.1.1, pp. 3–4; Tabla 1, pp. 8–9)

- **Malla:** red 3D de vóxeles cúbicos ("Geometrical Cells", GC) de **1 u 8 mm³** cada uno [p. 3]. Método discreto en eventos y en estados. Dos barridos de malla: uno para la citocinética y otro para la expansión o contracción espacial [p. 4].
- **Jerarquía celular** [p. 3]:
  - Las células madre (stem) se dividen simétricamente con probabilidad $P_{sym}$ y, en caso contrario, asimétricamente, dando una stem + una LIMP.
  - Las LIMP hacen $N_{LIMP}$ mitosis y pasan a DIFF.
  - Las stem y LIMP pueden estar en ciclo (G1, S, G2, M) o en G0.
  - Tras la mitosis pasan a G0 con probabilidad $P_{sleep}$, regulada por la disponibilidad de nutrientes y oxígeno.
  - En G0 permanecen un tiempo $T_{G0}$; después vuelven a G1 con probabilidad $P_{G0toG1}$ o mueren por necrosis.
  - Las stem y LIMP sufren apoptosis espontánea con tasa $R_A$. Las DIFF sufren apoptosis con tasa $R_{ADiff}$ o necrosis con tasa $R_{NDiff}$.
  - Los restos apoptóticos y necróticos se eliminan en $T_A$ y $T_N$.
- **Quimioterapia** [p. 3]: una fracción (CKR) de las stem y LIMP queda letalmente dañada y sigue un ciclo rudimentario antes de morir por apoptosis, en una fase que depende del fármaco. El efecto es instantáneo en el momento de la administración. **No hay PK/PD explícito** en este artículo: la farmacocinética entra solo a través del CKR de la literatura [Tabla 8, p. 20].
- **Radioterapia** [pp. 3–4]: las células letalmente dañadas mueren por necrosis tras unas pocas mitosis. La probabilidad de impacto depende de la fase del ciclo. Se usa el modelo LQ:

$$S(D)=\exp\left[-(\alpha D+\beta D^{2})\right] \qquad (1)\ [p.\,4]$$

  Aquí $D$ es la dosis en Gy, $\alpha$ está en Gy⁻¹ y $\beta$ en Gy⁻².
- **Implementación:** C++14 [p. 4]. Los algoritmos de movimiento celular están en [9]. Los análisis de sensibilidad previos están en [14, 19–21].

### 4.2 Hipomodelo molecular: señalización (§2.1.2, pp. 4–5; §2.3.1, pp. 12–13)

- **Red ErbB → Ras/Raf/MAPK y PI3K/AKT:** adaptada de Chen et al. 2009 [22]. Son EDO de acción de masas con **504 especies, 827 reacciones y 252 parámetros**. Solo se considera EGF (no HRG). Incluye internalización y reciclaje de receptores y mutantes de EGFR constitutivamente activos (L858R y deleciones) [p. 4].
- **Red TP53 de respuesta al daño del ADN:** adaptada de Choi et al. 2012 [23]. Es un modelo **booleano** de **16 nodos**, "with 160 negative and 218 positive feedbacks" [p. 4]. Tiene tres atractores:
  - Progresión del ciclo: punto fijo con cyclin-G alta y p53 baja.
  - Apoptosis: punto fijo con p53 alta y caspasa alta.
  - Senescencia: atractor cíclico con oscilaciones de p53 y Mdm2.

  [pp. 4–5]
- **Interfaz entre módulos:** los nodos comunes son **Erk, Akt y PTEN**. Los estados continuos de las EDO se umbralizan antes de pasar al módulo booleano. El módulo booleano devuelve la fracción de activación de esos nodos a las EDO. Se supone separación de escalas (las EDO son rápidas y se trata a p53 como pseudo-estacionario) y se itera hasta que p53 converge a un atractor [p. 5].
- **Personalización** [p. 12]:
  - Se seleccionan los **5–10 miRNA sobreexpresados** y se buscan sus dianas en miRTarBase [45].
  - Las proteínas diana se fijan en niveles de actividad o concentración más bajos, en función de la expresión relativa al control.
  - **En pulmón** se añade además el estado mutacional de EGFR, KRAS, BRAF y "AML/ALK".
- **Ajuste del CKR por quimioterapia** (WT), suponiendo supervivencia de Poisson con $CKR=1-e^{-kt}$:

$$\frac{k_{adj}}{k_{lit}}=\frac{\ln\left(1-CKR_{adj}\right)}{\ln\left(1-CKR_{lit}\right)} \qquad (10)\ [p.\,12]$$

  El cociente $k_{adj}/k_{lit}$ se obtiene simulando el paciente frente a un control sin inicialización por miRNA. Para combinaciones de fármacos se suman las constantes de velocidad, no los CKR [p. 12].
- **Radiación** [pp. 12–13]: el modelo booleano solo captura el término lineal. ATM se activa "according to a probability exp(−aD)", y la supervivencia se corrige después con el término cuadrático $\beta$, tomado de la literatura.
- **Salida:** se promedia sobre condiciones de factor de crecimiento y expresión de receptores. Da la probabilidad media de muerte celular, que se traduce a CKR y se pasa al OS [p. 13].
- **Implementación:** COPASI 4.20 para las EDO y Python 2.7 para el modelo booleano [p. 5]. **Los parámetros y la sensibilidad están en la tesis de Ghosh 2019 [24], no en el artículo** [p. 5].

### 4.3 Hipomodelo de vasculatura: transporte de glucosa (§2.1.3, pp. 5–6; §2.3.4, p. 15; Apéndice B, pp. 31–32)

- **Motivación:** el modelo de Hahnfeldt et al. [25], escrito así [p. 5, verificado]:

$$T'=-\alpha T\log\left(\frac{T}{K}\right) \qquad (2)$$
$$K'=-\alpha_2K+bT-dKT^{2/3} \qquad (3)$$

  Las ecuaciones (2)–(3) se presentan como **motivación**. El hipomodelo que se usa realmente es la ec. (4).
- **Modelo usado:** reacción–difusión estacionaria en la región tumoral. Fuera del tumor $c=c_n$ (Fig. 1) [p. 6]:

$$D\nabla^{2}c-\lambda Pc+\rho V(c_n-c)=0 \qquad (4)\ [p.\,6]$$

  donde $c$ es la glucosa, $P$ el número o la fracción de células viables, $V$ la fracción volumétrica de vasos (fija en el tiempo), $D$ la difusividad, $\lambda$ el consumo y $\rho$ el aporte vascular.
- **Discretización:** diferencias finitas en una malla 3D regular, la misma rejilla que el OS para evitar interpolaciones [p. 6].
- **Implementación:** Chaste (C++) con MUSCLE, ejecutable autónomo. **El código está en GitHub** [27] [p. 6].
- **Verificación** (Apéndice B): con $\bar x = xR$ y $\bar c = c\,c_n$, tal como está escrito [p. 31]:

$$\nabla^{2}\bar c-\phi_1^{2}\bar c+\phi_2^{2}=0 \qquad (A6)$$

  $$\phi_2=\sqrt{\tfrac{R^2}{D}\rho V},\qquad \phi_1=\sqrt{\tfrac{R^2}{D}(\lambda P+\rho V)}$$

  En forma esférica, el artículo imprime: $\frac{1}{r^{2}}\frac{d}{dr}\left(r^{2}\frac{d^{2}c}{dr^{2}}\right)-\phi_1^{2}c+\phi_2^{2}=0$ (A7), con $c'(0)=0$ y $c(1)=1$. La solución analítica es:

$$c(r)=\left(1-\frac{\phi_2^{2}}{\phi_1^{2}}\right)\frac{\sinh(\phi_1 r)}{r\,\sinh(\phi_1)}+\frac{\phi_2^{2}}{\phi_1^{2}} \qquad (A8)$$

  Con $R=100$ mm, los valores de la Tabla 4, $10^9$ células y $V=1$, se obtiene $\phi_1=160$ y $\phi_2=80$ [p. 31].
- **Relación con el crecimiento** (Greenspan [101]): $R^{2}\frac{dR}{dt}=\int_0^{R(t)} s\,c\,r^{2}\,dr$ (A9) [p. 32].

### 4.4 Hipomodelo metabólico: genoma completo con FBA (§2.1.4, pp. 6–7; §2.3.3, pp. 13–15)

- **Red:** Recon1 [32] con **1496 ORF, 3742 reacciones y 2766 metabolitos** [p. 7]. La función objetivo es la biomasa, con una restricción de capacidad solvente siguiendo a Shlomi et al. [10] [p. 7].
- **Estrategia de maximización del lactato** (dos pasos, tipo FVA):
  1. Maximizar el crecimiento.
  2. Maximizar la secreción de lactato con la condición crecimiento ≥ k·óptimo, bajando k iterativamente hasta encontrar solución, con una tolerancia de lactato de 0.01 µmol/mgDW/h.

  Desviaciones del 90–99 % respecto al crecimiento óptimo bastan para producir lactato [p. 7].
- **Captación de glucosa** con Michaelis–Menten [pp. 9–10, verificado]:

$$v_{bound}=v_{max}\,\frac{C}{K_m+C} \qquad (5)$$

  Se supone que $v_{bound}=v_{max}$ cuando $C=C_{max}=0.9$ kg m⁻³ [p. 10].
- **Personalización por tumor** [pp. 13–14]:
  - Las reacciones catalizadas por proteínas sobreexpresadas reciben una cota inferior de 0.1 µmol/mgDW/h, y las de genes reprimidos una cota superior de 0.
  - Para NSCLC se usan los clusters de Li et al. 2014 [47]: **C15 (LADC)** = NAT10, NME2, OAT, PPAT, SHMT2, GART, PAICS, SRM, UMPS, QARS, ABCE1, ABCF2 y ACOT7 (se excluyen OAT y SHMT2). **C10 (LSCC)** = ADSS, ATP2A2, CTPS1, IMPDH2, PKM2 y PTGES3 (se excluye SGPL1) [Tabla 3, p. 14].
  - **Para WT** se usa el modelo genérico por falta de datos [p. 14].
- **Salidas** [Fig. 4, p. 15, verificada]: tiempo de proliferación, lactato y captación de glucosa en función de la glucosa normalizada. La leyenda de la Fig. 4a da el tiempo mínimo de proliferación: **genérico 13.1 h, C10 16.4 h y C15 31.1 h**.
- **Implementación:** COBRA Toolbox 1.3.1, MATLAB R2008 y GLPK [p. 7].

### 4.5 Simulador biomecánico, BMS (§2.1.5, pp. 7–8; §2.2.3, pp. 11–12; §2.3.5, pp. 15–17)

- **Método:** elementos finitos (FEM) con material elástico lineal sobre una anatomía específica del paciente. La malla es tetraédrica, generada a partir de la segmentación de imagen, y los bordes externos del dominio están fijos [pp. 8, 15–16]. Se implementa con CGAL, VTK y FEBio [p. 8].
- **Deformación de crecimiento** [p. 11, verificada]:

$$\epsilon_{growth}(\mathbf{x})=\left(\frac{c(\mathbf{x})}{c_0}\right)^{1/3}-1 \qquad (8)$$

  Aquí $c_0$ es la capacidad de carga máxima fija.
- **Presión y dirección de mínima presión:** $p(\mathbf{x})=\tfrac13\mathrm{tr}(\sigma(\mathbf{x}))$ [p. 11], y la dirección es [p. 12]:

$$\mathbf{d}(\mathbf{x})=-\frac{\nabla p(\mathbf{x})}{\lVert\nabla p(\mathbf{x})\rVert} \qquad (9)$$

- **Uso en el OS:** se devuelve como ángulos polar y azimutal [Fig. 2, p. 9; Fig. 3, p. 11] para dirigir el desplazamiento de células.

### 4.6 Acoplamientos: qué variable pasa de un modelo a otro

| De → A | Variable transferida | Tipo de acoplamiento | Ubicación |
|---|---|---|---|
| Molecular → OS | CKR (promedio de la probabilidad de muerte, por fármaco o por dosis) | Secuencial (TAVERNA, argumento CLI) | p. 9, p. 13, Fig. 2 |
| OS → Vasculatura | Geometría tumoral y población por GC (proliferantes, quiescentes, diferenciadas, apoptóticas y necróticas) | Dinámico (MUSCLE) | p. 10 |
| Vasculatura → Metabólico | Campo de glucosa normalizado $c/c_n$ por GC | Dinámico | p. 10 |
| Metabólico → OS | Tasa local de proliferación $a$ por GC, que se convierte en $P_{sleep}$ con la ec. (6) | Dinámico | p. 10 |
| OS → BMS | Mapa de concentración celular $c(\mathbf{x})$, interpolado de la malla regular a la no estructurada | Dinámico | p. 11, Fig. 3 |
| BMS → OS | Dirección de mínima presión $\mathbf{d}(\mathbf{x})$ (ángulos φ, θ) | Dinámico | p. 12, Fig. 3 |

**Transformación metabólica → OS** [p. 10, verificada en imagen]:

$$P_{sleep}=\frac{1-e^{aT_c}/2}{1-\left(P_{G0toG1}/T_{G0}\right)/\left(a+1/T_{G0}\right)} \qquad (6)$$

La ec. (6) se deriva de la relación de crecimiento con jerarquía stem/progenitora (ec. 7 de [20]):

$$e^{(\alpha+R_A)T_C}=\left(1+P_{sym}\right)\left(1-P_{sleep}+P_{sleep}\frac{P_{G0toG1}/T_{G0}}{R_A+1/T_{G0}+\alpha}\right) \qquad (7)$$

La ec. (6) se obtiene con $P_{sym}=1$ y $R_A=0$. Además, $T_{C,max}=\ln 2/\alpha$, y si $T_C$ es mayor, $P_{sleep}<0$ [p. 10]. **[Lector]** Comprobé algebraicamente que (6) se sigue de (7) bajo esos supuestos.

**Lo que NO se acopla** [p. 26]: el consumo de glucosa que calcula el modelo metabólico no se devuelve a la vasculatura. Los vasos son estáticos. No se modelan oxígeno, glutamina ni sistema inmune.

### 4.7 Parametrización del OS: tumores virtuales con LHS (§2.3.2, p. 13; Apéndice A, p. 30, verificado)

- **Restricciones de entrada:** $T_d$ (de dos imágenes) y GF (Ki-67), más rangos de fracción stem, necrótica y apoptótica.
- **Muestreo:** `lhsdesign` de MATLAB sobre los parámetros independientes, reescalados con $a_p+(b_p-a_p)x_p$ (A1).
- **Parámetros dependientes:** $P_{sleep}$ se obtiene con la ec. (6), y $P_{sym}$ y $R_{NDiff}$ con:

$$P_{sym}=\frac{e^{(a+R_A)T_c}}{1-P_{sleep}+P_{sleep}\frac{P_{G0toG1}}{T_{G0}}\Big/\left(a+R_A+\frac{1}{T_{G0}}\right)}-1,\quad a=\ln 2/T_d \qquad (A2)$$

$$R_{NDiff}=\frac{1-P_{sym}}{\frac{1}{A}\left(\frac{1}{GF}-1\right)-B}-a-R_{ADiff} \qquad (A3)$$

$$A=\frac{a+R_A}{e^{(a+R_A)T_C}-1}\ (A4),\qquad B=\frac{1-P_{sym}}{a+R_A+\frac{1}{T_{G0}}}P_{sleep}\ (A5)$$

- **Exclusiones:** se descartan las combinaciones con $P_{sleep}$ o $R_{NDiff}$ negativos y las que tienen la fracción stem fuera de rango [p. 19].
- **TCP de Poisson** [p. 19]: $TCP=\exp(-N)$, donde $N$ es el número de CSC supervivientes al final del tratamiento. Se supone una densidad celular de $10^6$ células/mm³.

## 5. Tabla de parámetros

| Símbolo | Significado | Valor | Unidad | Rango | Origen | Página/Tabla |
|---|---|---|---|---|---|---|
| GC | Volumen de vóxel | 1 u 8 | mm³ | — | Diseño | p. 3 |
| $T_c$ | Duración del ciclo celular | — | h | NSCLC 20–134; WT 11–50 | [53,54]; WT [75,77,78]; límite superior por el metabolismo | Tabla 7 p. 18; Tabla 9 p. 21 |
| $T_{G0}$ | Duración de G0 | — | h | 96–240 (ambos) | [55] | Tablas 7 y 9 |
| $T_N$ | Tiempo de necrosis + eliminación | — | h | NSCLC 1–100; WT 1–200 | [56,57] + estimación | Tablas 7 y 9 |
| $T_A$ | Tiempo de apoptosis + eliminación | — | h | 1–25 | [58–60] | Tablas 7 y 9 |
| $N_{LIMP}$ | Mitosis de LIMP antes de diferenciarse | — | — | 13–24 | Estimación (frecuencia de TIC) | Tablas 7 y 9 |
| $R_A$ | Apoptosis de stem/LIMP | — | h⁻¹ | 0–0.001 | Estimación | Tablas 7 y 9 |
| $R_{ADiff}$ | Apoptosis de DIFF | — | h⁻¹ | NSCLC 0.0001–0.02; WT 0–0.02 | Extensión de [61–64] | Tablas 7 y 9 |
| $R_{NDiff}$ | Necrosis de DIFF | Derivado (A3) | h⁻¹ | — | Calculado a partir de GF | Tablas 7 y 9; p. 30 |
| $P_{G0toG1}$ | Reentrada desde G0 | — | — | 0–0.2 | No reportado | Tablas 7 y 9 |
| $P_{sleep}$ | Paso a G0 tras la mitosis | Derivado (ec. 6) | — | — | Metabolismo | Tablas 7 y 9; p. 10 |
| $P_{sym}$ | Fracción de divisiones simétricas | Derivado (A2) | — | NSCLC <0.3 | [65,66] + $T_d$ | Tablas 7 y 9 |
| CKR (NSCLC) | Fracción letal por fracción de RT | 0.905 (15 Gy); 0.712 (10 Gy) | — | — | Modelo molecular | Tabla 6 p. 18; Tabla 7 |
| CKR (WT) | Fracción letal por quimioterapia | Caso 1: 0.916; Caso 2: 0.673 (combo), 0.28 (solo VCR) | — | — | Modelo molecular | Tabla 8 p. 20 |
| CKR_lit | CKR de la literatura | VCR 0.28; ACT 0.4; combo 0.568 | — | — | [14] S3, [75,76] | Tabla 8 p. 20 |
| $\alpha$, $\beta$ | Radiosensibilidad LQ | 0.35; 0.035 | Gy⁻¹; Gy⁻² | — | [52] | Tabla 6 p. 18 |
| $\alpha/\beta$ | Cociente LQ | — | Gy | 4–10 | [67] | Tabla 7 |
| T proliferación (NSCLC) | Tiempo de proliferación celular calculado por el metabolismo | 70 | h | — | Modelo metabólico | Tabla 7 |
| T proliferación (WT) | Ídem | 13.1 / 20 / 50 (texto); 13 / 30 / 50 (Fig. 8) | h | ~13–50 | Fig. 4a | p. 20; Fig. 8 p. 22 |
| Stem/vivas | Fracción de CSC | — | — | 0.00001–0.00025 | [68] | Tabla 7 |
| GF | Fracción de crecimiento | NSCLC 23 % (Ki-67); WT 10/25/50 % | — | WT 0–80 % | Paciente; [79–81] | Tablas 7 y 9; p. 20 |
| $T_d$ | Tiempo de duplicación del volumen | NSCLC ≈370 d; WT 11/25/40 d | d | WT 11–40 | Imágenes del paciente; [82,83] | Tablas 7 y 9; p. 20 |
| Necróticas/total | Restricción | — | — | NSCLC <30 %; WT 0–100 % | [69,70]; [84] | Tablas 7 y 9 |
| Apoptóticas/total | Restricción | — | — | NSCLC <5 % | [71] | Tabla 7 |
| Densidad celular | Densidad tumoral | 10⁶ | células/mm³ | — | Supuesto | p. 19 |
| $C_{max}$ | Glucosa máxima | 0.9 | kg·m⁻³ | — | [49] | Tabla 2 p. 14 |
| $K_m$ | Constante de Michaelis–Menten | 0.2704 | kg·m⁻³ | — | [49] | Tabla 2 |
| $C_{enz}$ | Masa enzimática total | 0.078 | mg·(mgDW)⁻¹ | — | [10] | Tabla 2 |
| — | Cota inferior para genes sobreexpresados | 0.1 | µmol·(mgDW)⁻¹·h⁻¹ | "Different bounds have also been tested" | [35] | Tabla 2; p. 14 |
| — | Cota superior para genes reprimidos | 0 | — | — | Este trabajo | Tabla 2 |
| — | Rango del flujo de glucosa | — | µmol·(mgDW)⁻¹·h⁻¹ | [0, 1.2] | [10] | Tabla 2 |
| — | Tolerancia de secreción de lactato | 0.01 | µmol·(mgDW)⁻¹·h⁻¹ | — | [35] | Tabla 2 |
| $D$ | Difusividad de la glucosa | 0.396 | mm²·h⁻¹ | — | [50] | Tabla 4 p. 15 |
| $\lambda$ | Consumo de glucosa | 7.6×10⁻¹⁰ | (células)⁻¹·h⁻¹ | — | Modificado de [50] | Tabla 4 |
| $c_n$ | Glucosa en la región no tumoral | 0.9 | "kg·m3" (sic; probablemente kg·m⁻³) | — | Igual que en el modelo metabólico | Tabla 4 |
| $\rho V$ | Eficiencia de aporte vascular | 0.25 | h⁻¹ | — | "User chosen/fit to data" | Tabla 4 |
| $E$, $\nu$ (WT) | Riñón 5.3×10³ / 0.40; hueso 1.0×10⁹ / 0.30; otros tejidos 5.0×10³ / 0.40; tumor 20.0×10³ / 0.40 | — | Pa / — | — | No reportado (supuesto) | Tabla 5 p. 16 |
| $E$, $\nu$ (NSCLC) | Pulmón 5.0×10³ / 0.40; hueso 1.0×10⁹ / 0.30; otros tejidos, órganos internos y bronquios 5.0×10³ / 0.40; **tumor 10.0×10³ / 0.40** | — | Pa / — | — | No reportado | Tabla 5 p. 16 |
| $c_0$ | Capacidad de carga en el BMS | No reportado (valor numérico) | — | — | — | p. 11 |
| Red ErbB | Tamaño | 504 especies, 827 reacciones, 252 parámetros | — | — | Chen 2009 [22]; valores en [24] | p. 4 |
| Red p53 | Tamaño | 16 nodos | — | — | Choi 2012 [23] | p. 4 |

## 6. Calibración y validación

- **NSCLC** (calibración a una sola paciente):
  - Se adapta con la fase de progresión previa a la RT: GF = 0.23 y $T_d$ ≈ 370 d, a partir de dos TC (4.5 → 5.5 cc en 98 días) [pp. 18, 32].
  - LHS de **200 combinaciones**, con exclusiones [p. 19].
  - La "validación" consiste en comparar con la TC de un año después (sin tumor visible) [p. 20], más la posición y la forma al día 98 [Fig. A2, p. 32; §3.3].
  - **No hay métricas cuantitativas de error del volumen.** Los autores reconocen: "follow-up data beyond this period would be needed to properly validate" [p. 20].
- **WT** (adaptación inversa):
  - 27 perfiles: 3 $T_d$ × 3 GF × 3 tiempos de proliferación.
  - **60 tumores virtuales por perfil.**
  - El CKR se fija con el modelo molecular.
  - La reducción de volumen predicha se compara con la observada (90.68 % en el Caso 1 y 52.29 % en el Caso 2) para identificar los perfiles compatibles [pp. 20–21; Fig. 8, p. 22; Tabla A2].
  - **No se cuantifica en número** la proporción de perfiles compatibles: el resultado se da gráficamente.
- **Forma y posición** [§3.3, pp. 21–22]:
  - Registro rígido de las imágenes y distancia entre centros de masa.
  - NSCLC: **≈2 cm** entre el tumor simulado y el observado.
  - WT: "about 2 cm".
- **Validación del molecular:** "Partial clinical validation" con volúmenes antes y después de la quimioterapia frente a la probabilidad de muerte; el detalle está en [24] [p. 5].
- **Verificación de la vasculatura:** comparación con la solución analítica (A8); "good agreement, within deviations at r = 1" [Fig. A1, p. 31].
- **Métricas formales** (RMSE, CCC, AUC, etc.): No reportado.

## 7. Resultados clave

- **Tabla 6, CKR por fracción de RT** (LQ frente a molecular) [p. 18]:
  - 5 Gy: 0.928 vs 0.433.
  - 10 Gy: 0.999 vs 0.712.
  - 15 Gy: 1.000 vs 0.905.
  - 20 Gy: 1.000 vs 0.979.

  El modelo molecular da valores más bajos que el LQ a dosis bajas y converge con él a dosis altas.
- **NSCLC, TCP y volumen a un año** [p. 19; Fig. 7]:
  - **Escenario 1** (15 Gy, el esquema real): TCP mediana **4×10⁻¹²** (IQR 2×10⁻²²–7×10⁻⁵); volumen mediano **0.908 mm³** ("IQR: 0.909–0.912").
  - **Escenario 2** (10 Gy): TCP de 0; volumen mediano **78 mm³** (IQR 77–79).
  - **Escenario 3** (RT un mes antes): TCP mediana **7×10⁻¹²** (IQR 7×10⁻²⁰–9×10⁻⁶).
  - Diámetro equivalente ≈ **0.97 mm**, "below the detection limit", coherente con la TC sin tumor visible [p. 20].
- **WT, CKR ajustado** [Tabla 8, p. 20]:
  - Caso 1 (VCR 1 mg/m², ACT 650 µg/kg): probabilidad media de muerte 0.527 → **CKR 0.916**. Sin fármaco: 0.179.
  - Caso 2 (VCR 0.83 + ACT 540): 0.149 → **CKR 0.673**. Solo VCR: 0.112 → 0.28.

  El modelo capta "the increased chemosensitivity of case 1" [p. 21].
- **WT, perfiles proliferativos** [Fig. 8, p. 22]:
  - En el Caso 1, la mayoría de los tumores virtuales predicen una reducción alta.
  - En el Caso 2, algunos perfiles son incompatibles con lo observado. Según la figura (lectura visual aproximada), los de $T_d$ = 11 d y GF = 0.25–0.50 quedan cerca del 52 % observado.
- **Metabolismo** [Fig. 4]: la captación de glucosa es similar entre fenotipos, pero el tiempo de proliferación y el lactato difieren. Tiempos mínimos: genérico 13.1 h, C10 16.4 h y C15 31.1 h.
- **Forma** [pp. 22, 26]: el NSCLC en crecimiento conserva una forma compacta, coherente con lo observado. Los WT en regresión "dissolve from one side, forming a porous and partially disconnected structure".

## 8. Sensibilidad e incertidumbre

- **OS:** "Thorough sensitivity analyses have been conducted and reported in a number of publications [14,19–21]" [p. 4]. **No se repiten en este artículo.**
- **Molecular:** "local and parametric sensitivity analysis, are reported in detail in [24]" [p. 5].
- **Incertidumbre paramétrica del OS:** se trata con un ensamble de tumores virtuales LHS (200 en NSCLC; 60 por perfil en WT) y se informan medianas e IQR [pp. 13, 19–20].
- **Metabolismo:** "Different bounds have also been tested… the level of flux bound substantially alters the metabolic capabilities" [p. 14]. Los resultados de esa prueba no se muestran.
- **BMS:** no hay análisis de sensibilidad. Las propiedades mecánicas no son específicas del paciente [p. 26].
- **Vasculatura:** solo verificación analítica [Apéndice B].

## 9. Limitaciones declaradas

- "the multiscale clinical data used… ceased to be accessible one year after the completion of the CHIC project" [p. 29].
- Solo glucosa: "glucose is assumed to be the only limiting resource" [p. 25]. El consumo es independiente del oxígeno [p. 15].
- "the vasculature is assumed to be 'static' in the current model" [p. 26]. El consumo metabólico no se retroalimenta a la vasculatura [p. 26].
- p53 booleano: "we are only able to account for the dose-independent part (the linear term involving α)" [p. 12].
- BMS: "uncertainty in mechanical tissue parameters (not patient-specific) and the lack of well-defined boundary conditions" [p. 26]. Hay errores de interpolación en el mapeo OS↔BMS [p. 26].
- La evaluación de la posición depende del registro de imagen: "introduces an uncertainty in the relative positioning" [p. 26].
- "morphological changes in the healthy tissue… not taken into account" [p. 26]. Tampoco se modelan microambiente ni sistema inmune [p. 26].
- NSCLC: sin biopsia de la recurrencia, por lo que se usan los datos del primario [p. 17]. El tumor virtual se supone homogéneo [p. 17].
- WT: sin biopsia ni histología. Para el Caso 1 "Dosage was assumed based on other patients" [p. 20].
- "additional retrospective validation work… is needed" [p. 28].
- El metabolismo de WT usa el modelo genérico por falta de datos [p. 14].

## 10. Evaluación del lector [Lector]

- **[Lector] Fortaleza:** la arquitectura modular está bien documentada (qué variable fluye y en qué dirección; Fig. 2 y Fig. 3). El puente explícito metabolismo → $P_{sleep}$ (ec. 6) y el ajuste del CKR (ec. 10) son ideas transferibles y sencillas.
- **[Lector] Debilidad crítica para la evidencia:** la validación clínica es **anecdótica**. Hay n = 1 en NSCLC y n = 2–3 en WT, sin métricas cuantitativas, sin conjunto de prueba independiente y con datos ya no disponibles. El resultado en NSCLC ("tumor no detectable a un año") es poco discriminante, porque también lo produciría un modelo nulo con CKR alto.
- **[Lector] Incoherencias internas detectadas:**
  1. **Fig. A1:** según la ec. (A8), en el interior $\bar c\approx\phi_2^2/\phi_1^2$, lo que da 0.25 para (160, 80), 0.40 para (126, 80) y 0.58 para (105, 80). Sin embargo, en la Fig. A1c la curva etiquetada "φ1 = 160" está en ≈0.57 y la de "φ1 = 105" en ≈0.25, y la escala de la Fig. A1b tiene un mínimo de 0.568 para (160, 80). Las etiquetas parecen intercambiadas. Recalculé $\phi_1=159.7$ y $\phi_2=79.5$ con la Tabla 4, lo que confirma el valor interior ≈0.247.
  2. **Ec. (A7):** está impresa con $d^2c/dr^2$ dentro del paréntesis. El laplaciano esférico correcto lleva $dc/dr$. Además, la adimensionalización está escrita como "$\bar x = xR$, $\bar c = c\,c_n$", que parece invertida.
  3. **Escenario 1:** se informa una mediana de 0.908 con un "IQR 0.909–0.912", es decir, una mediana fuera del IQR.
  4. **Diámetro equivalente de 0.97 mm:** coincide con $V^{1/3}$ (arista de un cubo, 0.968 mm), no con el diámetro de una esfera equivalente, que sería 1.20 mm.
  5. **$T_d$:** con 4.5 → 5.5 cc en 98 días se obtiene $T_d$ ≈ 338 d, frente a los "≈370 d" informados. La diferencia puede deberse al redondeo de los volúmenes.
  6. **Tiempo de proliferación intermedio en WT:** 20 h en el texto [p. 20] y 30 h en la Fig. 8 [p. 22].
  7. **Apéndice C.1:** habla de "MRI" y de "prior to chemotherapy" para el caso de pulmón, que se trató con RT y se siguió con TC [p. 32]. El pie de la Fig. A2 dice "chemotherapy protocols".
  8. **Casos de WT:** la §3.2 usa los Casos 1 y 2, pero la Fig. 9 muestra los Casos 2 y 3 [p. 23].
  9. **Dosis de actinomicina:** "45 mg/kg" [p. 20] es probablemente µg/kg. En la Tabla 8 aparecen 650 y 540 µg/kg sin explicar si son dosis acumuladas.
  10. **Apéndice A:** lista $P_{sym}$ como independiente y luego lo deriva con (A2). También menciona "CKF" y α/β entre los parámetros del LHS, sin definirlos en la Tabla 1.
  11. **Doble uso de $a$/$\alpha$:** en la ec. (6) es la tasa metabólica de proliferación ($\ln2/T_{prolif}$); en (A2) es $\ln 2/T_d$. Además, $\alpha$ también es la radiosensibilidad del LQ. Esta ambigüedad de notación afecta a la reproducibilidad.
  12. **El "Lung Oncosimulator" fija el CKR de cada fracción** a partir del modelo molecular (0.905 para 15 Gy), en lugar de usar el LQ directamente. Por eso el TCP depende críticamente de un único número no validado.
- **[Lector] Calidad de la evidencia para nuestra matriz:** baja para eficacia predictiva; media-alta como referencia de arquitectura de gemelo digital y de parametrización por tumores virtuales.

## 11. Disponibilidad de código y datos (citas textuales)

- "Regarding the computer codes, these have been developed and built in house by the modelling partners of the CHIC consortium and are not 'open access', with the exception of the vasculature hypomodel." [p. 29]
- "The code can be found on GitHub [27]." Ref. 27: "Vasculature Hypomodel Code. Available online: https://github.com/jmsgrogan/Chic" [pp. 6, 34]
- "the multiscale clinical data used for the needs of the work reported ceased to be accessible one year after the completion of the CHIC project… Meta-data are included in Appendix C." [p. 29]

## 12. Reproducibilidad en Python

| Componente | ¿Reproducible aislado con lo publicado? | Qué hay | Qué falta |
|---|---|---|---|
| **OS, cinética de compartimentos** (stem/LIMP/DIFF; G1, S, G2, M, G0; apoptosis y necrosis) | **Parcialmente**, como versión no espacial (EDO o eventos discretos por compartimento) | Estructura de compartimentos y transiciones [p. 3]; Tabla 1; rangos en las Tablas 7 y 9; fórmulas (6), (7) y (A1)–(A5); LQ (1); TCP = exp(−N) | Duración de cada fase (G1, S, G2, M) como fracción de $T_c$; las reglas espaciales de movimiento celular (están en [9]); el ciclo "rudimentario" post-tratamiento (número de mitosis antes de morir); la dependencia de fase del daño por RT; la ec. 47 de [21] (S2) para interpretar (A3); el valor de $c_0$ |
| Parametrización LHS de tumores virtuales | **Sí** | (A1)–(A5), rangos, criterios de exclusión. Las fórmulas son evaluables: lo probé con valores de la Tabla 7 y dan $P_{sleep}$ ≈ 0.19 y $P_{sym}$ ≈ 0.24 en un ejemplo | Semilla, N exacto antes de las exclusiones, distribución de α/β |
| Vasculatura (ec. 4) | **Sí** | Ecuación, parámetros (Tabla 4), solución analítica (A8) y código en GitHub | Mapa $V(\mathbf{x})$ real (se supuso V = 1) |
| Ajuste del CKR (ec. 10) y TCP | **Sí** (como fórmula) | Ec. (10), CKR_lit | El cociente $k_{adj}/k_{lit}$ requiere el modelo molecular |
| Molecular (ErbB EDO + p53 booleano) | **No con lo publicado** | Topología citada (Chen 2009, Choi 2012), nodos de interfaz | Los 252 parámetros, los umbrales de discretización, las reglas booleanas y la lista de miRNA y dianas (todo en la tesis [24]) |
| Metabólico (FBA con Recon1) | **Parcialmente**: Recon1 es público y COBRApy puede reemplazar a COBRA/MATLAB | Algoritmo de dos pasos, cotas (Tabla 2), genes (Tabla 3), $v_{max}$ de Michaelis–Menten | La correspondencia exacta entre genes y reacciones usada, el valor de $v_{max}$, la secuencia de k, y la conversión de la tasa de biomasa en tiempo de proliferación |
| BMS (FEM) | Parcialmente, con FEniCS o FEBio | Ecs. (8)–(9), E y ν (Tabla 5), condición de borde fija | $c_0$, las mallas (los datos no están disponibles), el algoritmo de redistribución celular en el OS |

**[Lector]** El núcleo más reproducible es la **cinética de compartimentos con jerarquía stem/LIMP/DIFF + G0 + RT por LQ/CKR + TCP de Poisson, parametrizada con LHS restringido por $T_d$ y GF**, en su versión no espacial. Lo crítico que falta es la distribución de las fases del ciclo y la regla de muerte post-irradiación (número de mitosis abortivas), que deben tomarse de Dionysiou 2004 [15] y Kolokotroni 2016 [21].

## 13. Transferibilidad a cáncer de pulmón

- **El documento menciona el pulmón de forma explícita y sustancial:** NSCLC adenocarcinoma es uno de los dos casos de estudio [pp. 1–3, 17–20, 24], con componentes específicos (§2 de esta ficha).
- **Partes genéricas, reutilizables tal cual:**
  - La arquitectura de acoplamiento (Fig. 2).
  - La jerarquía celular del OS.
  - El puente metabolismo → $P_{sleep}$ (ec. 6).
  - El LHS con restricciones $T_d$/GF (Apéndice A).
  - El TCP de Poisson.
  - La vasculatura (ec. 4).
  - La ecuación de deformación de crecimiento (ec. 8).
- **Parámetros que habría que reemplazar o recalibrar para una cohorte de pulmón:**
  - $T_d$ y GF por paciente (de las TC seriadas y el Ki-67).
  - α, β y α/β para el fraccionamiento real: el artículo usa α = 0.35 y β = 0.035 de [52], con rango α/β de 4–10. Ojo: 4 × 15 Gy es un esquema de tipo SBRT, donde el LQ es discutible **[Lector]**.
  - CKR por dosis por fracción (Tabla 6), que depende del modelo molecular no disponible.
  - Rangos de $T_c$ (20–134 h), fracción stem (1e-5–2.5e-4), necrosis (<30 %) y apoptosis (<5 %) [Tabla 7].
  - E del tumor pulmonar (10 kPa) y del parénquima (5 kPa) [Tabla 5].
  - Cluster metabólico C15 (LADC) o C10 (LSCC) según la histología [Tabla 3].
- **Lo que no cubre:** quimioterapia en pulmón (solo RT en este artículo; el cisplatino doblete está en [21]), inmunoterapia, terapias dirigidas (EGFR-TKI), hipoxia/oxígeno, ni cohortes.

## 14. Problemas de extracción

- **Ecuaciones** (2), (3), (6), (7), (8), (9), (10), (A2)–(A9): el texto extraído las fragmentó (exponentes y fracciones separados, p. ej. "dKT\n2\n3", "Psleep =\n1 −eaTc/2"). **Las transcribí desde las imágenes** de las pp. 5, 10, 11, 12, 30 y 31.
- **Tablas 1–9 y A1–A2:** se extrajeron en una sola columna. Las reconstruí y las verifiqué visualmente (Tablas 2–3 en p. 14, Tabla 4 en p. 15, Tablas 6–7 en p. 18, Tabla 8 en p. 20, Tablas A1–A2 en pp. 32–33). La Tabla 5 (p. 16) y la Tabla 9 (p. 21) no las verifiqué visualmente, pero su estructura en el texto es inequívoca.
- **Figuras** 2, 3, 4, 7, 8, 9, A1, A2 y A3: su contenido solo es accesible en imagen. Las verifiqué y extraje las etiquetas relevantes (tiempos de proliferación en la Fig. 4a; días de RT en la Fig. A2; casos de WT en la Fig. 9; esquemas de quimioterapia en la Fig. A3: Caso 1 ACT días 7 y 21, VCR días 7, 14, 21 y 28, imagen en el día 35; Caso 2 ACT días 3 y 17, VCR días 3, 10, 17 y 24, imagen en el día 28; Caso 3 ACT días 8 y 22, VCR días 8, 15, 22 y 29, imagen en el día 41).
- **Figuras 1, 5 y 6:** no las verifiqué visualmente (geometría del dominio y mallas FEM).
- **Renderizado:** `pdftoppm` no estaba disponible para el lector de PDF. Rendericé las páginas con PyMuPDF a 110 dpi; la resolución fue suficiente para leer ecuaciones y tablas.

## 15. Citas textuales clave (≤ 40 palabras)

1. "Two specific cancer types, Wilms tumor (nephroblastoma) and non-small cell lung cancer, are addressed as proof-of-concept study cases." [p. 1]
2. "the Lung Oncosimulator, a model of lung tumor response-to-external beam radiotherapy, and the Wilms tumor, WT, (Nephroblastoma) Oncosimulator, a model of Wilms tumor response to preoperative combined chemotherapy treatment of actinomycin and vincristine." [p. 3]
3. "a reasonable first approximation is to translate the proliferation rate, a, of the cell population to the fraction of newborn cells entering quiescent state, Psleep, within the population." [p. 10]
4. "For lung cancer, the model additionally, incorporates the sequencing information by considering the mutational status of EGFR, KRAS, BRAF, and AML/ALK." [p. 12]
5. "We consider that a set of model parameter values constitutes a virtual tumor." [p. 13]
6. "If consistent results can be demonstrated for the considered set of virtual tumors… this result may be considered robust to the uncertainty in parameter values." [p. 13]
7. "a TCP close to zero is estimated (median TCP: 4 × 10−12, IQR: 2 × 10−22–7 × 10−5), suggesting that the tumor will recur." [p. 19]
8. "Even though hypermodel predictions seem consistent with reality, follow-up data beyond this period would be needed to properly validate the hypermodel, for the specific clinical case." [p. 20]
9. "the only personalized data utilized that could affect the predicted outcome were the serum miRNA expression data." [p. 21]
10. "Its simulated and observed positions at the second imaging time point are approximately 2 cm apart." [p. 22]
11. "these have been developed and built in house by the modelling partners of the CHIC consortium and are not 'open access', with the exception of the vasculature hypomodel." [p. 29]
12. "additional retrospective validation work for the developed hypermodels and Oncosimulators is needed in order to fully substantiate and support their 'candidacy' for undergoing validation through prospective clinical trials." [p. 28]
