# Ficha D02 — Modelo de campo de fase para NSCLC bajo inmunoterapia

**Convenciones de esta ficha**
- `[p. N]` = página del PDF (numeración impresa "N/18" del pie de página, que coincide con la del archivo).
- "No reportado" = el documento no contiene la información.
- **[Lector]** = cálculo, inferencia o digitalización hecha por el lector; NO es una afirmación de los autores.
- Páginas verificadas visualmente (renderizadas desde el PDF con PyMuPDF a 150 dpi): **3, 4, 5, 6, 7, 8, 9, 10, 11, 13**. Además, las figuras 1, 2 y 5 (pp. 6, 8, 10) son gráficos vectoriales (matplotlib) y sus coordenadas se extrajeron directamente de los objetos vectoriales del PDF para digitalizar los datos (ver §6). El PDF original no se modificó.

---

## 1. Referencia bibliográfica

- **Autores:** Marvin Fritz, Christina Kuttler, J. Tinsley Oden, Pirmin Schlicke, Christian Schumann, Andreas Wagner (autor de correspondencia, wagneran@cit.tum.de), Barbara Wohlmuth [p. 1].
- **Título:** "A phase-field model for non-small cell lung cancer under the effects of immunotherapy" [p. 1].
- **Fuente:** arXiv:2303.09378v1 [math.NA], 16 Mar 2023 (sello lateral en [p. 1]). Fecha en el pie de página de todas las páginas: "March 17, 2023" [pp. 1–18]. Metadatos del PDF: creado con "LaTeX with hyperref", pdfTeX-1.40.21, 2023-03-17.
- **Revista / DOI del artículo:** No reportado. El documento no muestra ningún DOI propio ni nombre de revista (los DOI que aparecen corresponden a las referencias citadas).
- **Afiliaciones:** RICAM Linz (Austria); TU München (Alemania); Oden Institute, UT Austin (EE. UU.); Klinikverbund Allgäu, Kempten (Alemania) [p. 1].
- **¿Preprint o versión publicada?** **Preprint.** Razones: (i) identificador arXiv v1 en [p. 1]; (ii) no hay DOI, volumen ni paginación de revista; (iii) el formato (sección "Author summary", pie "fecha · N/18", "Methods & Materials" al final) corresponde a una plantilla de envío tipo PLOS, no a una maqueta final de editorial. No es posible verificar (sin web) si existe una versión publicada posterior; cualquier versión revisada podría diferir de esta.

## 2. Tipo de estudio, subtipo de cáncer, población

- **Tipo de estudio:** Modelado matemático mecanístico determinista (EDP de campo de fase tipo Cahn–Hilliard + nutrientes estacionarios + EDO farmacocinética), con calibración manual a datos retrospectivos de 2 pacientes ("proof of concept") y simulaciones contrafactuales de dosis/esquema [pp. 1, 3, 7–12].
- **Subtipo de cáncer:** Cáncer de pulmón de células no pequeñas (NSCLC) [pp. 1, 3, 6]. Histología (adenocarcinoma/escamoso), PD-L1, mutaciones: **No reportado**.
- **Estadio:** **No reportado** para ningún paciente. Solo se menciona que la inmunoterapia beneficia a "patients with advanced stages of cancer" en la introducción general [p. 2], que los datos incluyen "primary tumors and metastases" [p. 6] y que el Paciente 1 tuvo metástasis cerebrales [p. 7].
- **Número de pacientes:** 2 [pp. 1, 3, 6]. Edad, sexo, ECOG, línea de tratamiento, tratamientos previos: **No reportado**. Peso: Tabla 1 fija ω = 80 kg para ambos [p. 5] (no se indica si es medido o supuesto).
- **Centro y ética:** Clinic of Pneumology, Thoracic Oncology, Sleep and Respiratory Critical Care, Klinikverbund Allgäu (Alemania); aprobación de la Ethik-Kommission der Bayerischen Landesärztekammer (BLAEK), referencia 19021 (nota al pie 1) [p. 6].

**Paciente 1** [pp. 6–7; Tabla 1 p. 5]
- Fármaco: **Nivolumab**, cada 2 semanas, infusión IV de 30–60 min [p. 6].
- Dosis: d_τ = 0.24 g (= 240 mg) por administración [p. 4; Tabla 1, p. 5]. M_τ = "146.000" g/mol (notación con punto de miles; equivale a 146 000 g/mol — [Lector] confirmado al reproducir numéricamente la curva de la Fig. 2A, ver §13); t_{1/2} = 26.7 d [Tabla 1].
- Fechas: diagnóstico en t = 0; inicio de terapia t_S = 296 días [p. 6]. Eventos (Fig. 1A, [p. 6]): **E** = embolia pulmonar temporal ("Emblie" en la leyenda) que afecta calidad de datos y precisión LCAD [p. 7]; **P** = pausa de la inmunoterapia por metástasis cerebrales, momento en que los médicos diagnosticaron "complete remission for the primary tumor in the lung" [p. 7]; **D** = tratamiento con dexametasona [p. 6, leyenda Fig. 1].
- Esquema modelado: Ec. (11) [p. 7].
- [Lector] Posiciones de las líneas de eventos digitalizadas de Fig. 1A y Fig. 2A: E ≈ día 1135, P ≈ día 1655, D ≈ día 2240. La primera dosis simulada en Fig. 2A ocurre en el día ≈ 322 (no 296; ver §14).

**Paciente 2** [p. 7; Tabla 1 p. 5]
- Fármaco: **Pembrolizumab** 200 mg cada 3 semanas (Q3W); la terapia ya estaba en curso antes del primer dato [p. 7].
- Cambio a cada 6 semanas en t_{Q6W} = 514 días; fin de la terapia en t_{PD} = 1063 días; muerte (exitus letalis) en el día 1306 [p. 7]. "The final CT image shows a very large tumor mass that has spread over the entire lung" [p. 7].
- Tabla 1: d_τ = 0.20 g, M_τ = "143.600" g/mol, t_{1/2} = 22.0 d [p. 5].
- Esquema modelado: Ec. (12) [p. 7].
- [Lector] Líneas de eventos digitalizadas en Fig. 1B: Q3W ≈ 22, Q6W ≈ 671, PD ≈ 1218, EL ≈ 1431; en Fig. 2B (eje desplazado −114 d): Q6W ≈ 557, PD ≈ 1104, EL ≈ 1317. No coinciden con 514/1063/1306 del texto (ver §14).

## 3. Pregunta de investigación

Desarrollar un modelo matemático del crecimiento espacial de tumores sólidos de NSCLC "in a simple, deterministic setting" que incorpore el efecto de la inmunoterapia anti-PD-1 (nivolumab, pembrolizumab) y su influencia sobre la estructura espacial del tumor; aplicarlo a dos pacientes con desenlaces cualitativamente distintos y analizar qué relaciones de parámetros determinan esos desenlaces, con miras a uso pronóstico y a la elección de terapias [p. 3]. Secundariamente: explorar contrafactuales de dosis y esquema [pp. 10–11] y mostrar la extensión a 3D en geometría pulmonar del paciente [pp. 11–12].

## 4. Métodos: modelo completo

### 4.1 Variables de estado

| Símbolo | Significado | Unidades | Ubicación |
|---|---|---|---|
| φ_P | Fracción de volumen de células tumorales proliferativas | adimensional [0,1] | [p. 3] |
| φ_N | Fracción de volumen de células necróticas | adimensional | [p. 3] |
| φ_T = φ_P + φ_N | Fracción de volumen tumoral total | adimensional | [p. 3] |
| μ_P | Potencial químico de φ_P | No reportado | [p. 3] |
| φ_{σ,v} | Concentración de nutrientes en la vasculatura | No reportado (adimensional implícito) | [p. 3] |
| φ_{σ,i} | Concentración de nutrientes en el espacio intersticial | No reportado (en Figs. 3–4 varía en ~[0.3, 1]; en Fig. 6 la barra de color va de 1.6e-01 a 3.4e+00) | [pp. 3, 8, 9, 11] |
| φ_τ | "Concentración" de agentes inmunoterapéuticos, un escalar para todo el pulmón | En la práctica, número de moléculas (eje "immunotherapy" ×1e17 en Fig. 2); no se declara unidad | [pp. 1, 3, 4, 8] |
| r | Coordenada radial (modelo 1D) | m (inferido: ejes de Figs. 3–4 hasta 0.04 = radio de 4 cm) | [pp. 5, 7, 8, 9] |
| t | Tiempo | días | [Tabla 1, p. 5] |
| Ω, ∂Ω, n, Γ | Dominio, frontera, normal exterior, variedad 2D de arterias/bronquios | — | [pp. 3–4] |

### 4.2 Modelo 3D completo (todas las ecuaciones, verificadas visualmente en pp. 3–4)

Ecuación (1) [p. 3] — Cahn–Hilliard generalizado con reacción:

$$
\partial_t \phi_P = \nabla\cdot\big(c_m\, m_P(\phi_P,\phi_T)\,\nabla \mu_P\big) + S_P(\phi_P,\phi_{\sigma,i},\phi_\tau) \quad \text{en } \Omega,
$$
$$
\mu_P = \partial_{\phi_P}\Psi(\phi_P,\phi_T) - \varepsilon_P^2\,\Delta\phi_P - \chi\,\phi_{\sigma,i} \quad \text{en } \Omega, \tag{1}
$$

Condiciones de contorno (sin número) [p. 3]:

$$
\frac{\partial \phi_P}{\partial n} = 0, \qquad \frac{\partial \mu_P}{\partial n} = 0 \quad \text{en } \partial\Omega .
$$

Definiciones (sin número) [p. 3]:

$$
\Psi(\phi_P,\phi_T) = \tilde\Psi(\phi_P) + \tilde\Psi(\phi_T),\qquad \tilde\Psi(\phi) = c_\Psi\,\phi^2(1-\phi)^2,\qquad m_P(\phi_P,\phi_T) = \phi_P^2\,(1-\phi_T)^2 .
$$

Ecuación (2) [p. 3] — término de reacción:

$$
S_P(\phi_P,\phi_{\sigma,i},\phi_\tau) = \lambda_P^{pro}\,\phi_{\sigma,i}\,(\phi_P)^{\lambda}\,\ln\!\left(\frac{1+\epsilon_g}{\phi_P+\epsilon_g}\right) - \left(\lambda_\tau^{\mathrm{eff}}\,\frac{1}{\omega}\right)\phi_P\,\frac{\phi_\tau}{\phi_\tau+\phi_\tau^{50}} - \lambda_{PN}\,\mathcal{H}(\sigma_{PN}-\phi_{\sigma,i})\,\phi_P . \tag{2}
$$

- 1er término: crecimiento gompertziano "acting on the tumor interface", regularizado con ε_g, proporcional al nutriente; λ ≥ 1 penaliza el crecimiento de concentraciones pequeñas e impide la diseminación por todo el pulmón [pp. 3–4].
- 2º término: muerte por inmunoterapia que "acts on the tumor volume"; 1/ω descrito como "the ratio of the lung weight to the body weight" [p. 4] (pero en Tabla 1 ω = "Patient weight" [kg], ver §14); forma Hill–Langmuir (exponente 1) siguiendo [16] [p. 4].
- 3er término: conversión a necrosis cuando φ_{σ,i} < σ_PN, activada por Heaviside 𝓗 [p. 4].
- −χφ_{σ,i} en μ_P: quimiotaxis [p. 4] (χ = 0 en todas las simulaciones, Tabla 1).

Ecuación (3) [p. 4] — necrosis (EDO puntual):

$$
\partial_t\phi_N = S_N(\phi_{\sigma,i},\phi_P),\qquad S_N(\phi_{\sigma,i},\phi_P) = \lambda_{PN}\,\mathcal{H}(\sigma_{PN}-\phi_{\sigma,i})\,\phi_P . \tag{3}
$$

Ecuaciones (4)–(5) [p. 4] — nutrientes estacionarios (siguiendo [55]):

$$
-\nabla\cdot\kappa_v\nabla\phi_{\sigma,v} = -\xi_{va}\phi_{\sigma,v} - \eta_{vi}\phi_{\sigma,v} + \eta_{iv}\phi_{\sigma,i} + \beta\,\delta_\Gamma \quad \text{en } \Omega, \tag{4}
$$
$$
-\nabla\cdot\kappa_i\nabla\phi_{\sigma,i} = \eta_{vi}\phi_{\sigma,v} - \eta_{iv}\phi_{\sigma,i} - \alpha_H(1-\phi_P)\phi_{\sigma,i} - \alpha_P\,\phi_P\,\phi_{\sigma,i} \quad \text{en } \Omega, \tag{5}
$$

con Neumann cero: ∂φ_{σ,v}/∂n = 0 y ∂φ_{σ,i}/∂n = 0 en ∂Ω [p. 4]. δ_Γ: distribución delta sobre la variedad 2D Γ (superficie de arterias y bronquios); β > 0 controla la entrada de nutrientes [p. 4]. Justificación de la estacionariedad: el tumor evoluciona en días–semanas, el nutriente es mucho más rápido [p. 4].

Ecuación (6) [p. 4] — farmacocinética:

$$
\partial_t\phi_\tau = -\frac{\ln(2)}{t_{1/2}}\,\phi_\tau + \frac{N_A}{M_\tau}\,d_\tau\,\mathbf{1}_{t\in I_\tau}, \tag{6}
$$

N_A = 6.022140857·10^23; M_τ masa molar; d_τ = 0.24 ("the administered dosage", sin unidad en el texto; [g] en Tabla 1) [p. 4]. I_τ ⊂ [0, ∞) es el conjunto de tiempos de administración [p. 4].

### 4.3 Modelo reducido 1D (simetría esférica) [p. 5, verificado visualmente]

Supuestos: φ_P = φ_P(r), φ_{σ,v} = φ_{σ,v}(r) ⇒ μ_P, φ_{σ,i}, φ_N dependen solo de r [p. 5]. Las ecuaciones de necrosis (3) y fármaco (6) no cambian; φ_{σ,v} se aproxima por "a pre-given constant value" [p. 5] (valor: **No reportado**).

$$
\partial_t\phi_P = \frac{1}{r^2}\frac{\partial}{\partial r}\left( (c_m m_P(\phi_P,\phi_T))\, r^2 \frac{\partial\mu_P}{\partial r}\right) + S_P(\phi_P,\phi_{\sigma,i},\phi_\tau) \quad \text{en } \Omega, \tag{7}
$$
$$
\mu_P = \partial_{\phi_P}\Psi(\phi_P,\phi_T) - \epsilon_P^2\,\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial\phi_P}{\partial r}\right) - \chi\,\phi_\sigma \quad \text{en } \Omega, \tag{8}
$$
$$
\frac{\partial\phi_P}{\partial r} = 0, \qquad \frac{\partial\mu_P}{\partial r} = 0 \quad \text{en } \partial\Omega, \tag{9}
$$
$$
-\kappa_i\,\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial\phi_{\sigma,i}}{\partial r}\right) = \eta_{vi}\phi_{\sigma,v} - \eta_{iv}\phi_{\sigma,i} - \alpha_H(1-\phi_P)\phi_{\sigma,i} - \alpha_P\phi_P\phi_{\sigma,i} \quad \text{en } \Omega. \tag{10}
$$

(En (8) aparece "χφ_σ" sin subíndice i: errata probable; irrelevante porque χ = 0.) El término r^{-2} no causa problemas porque en la forma débil se usa la medida 4πr²dr [p. 6].

### 4.4 Esquemas de administración [p. 7, verificado visualmente]

$$
I_\tau := \left\{ t : t_S + 14\cdot k \le t \le t_S + 14\cdot k + \tfrac{1}{24},\ \text{with } t \le t_P \right\} \tag{11}
$$
(Paciente 1; k no se declara explícitamente en (11), sí en (12)).

$$
I_\tau := \left\{ t : t_S + 21 k \le t \le t_S + 21 k + \tfrac{1}{24},\ t \le t_{Q6W},\ k\in\mathbb{N} \right\} \cup \left\{ t : t_{Q6W} + 42 k \le t \le t_{Q6W} + 42 k + \tfrac{1}{24},\ t \le t_{PD},\ k\in\mathbb{N} \right\} \tag{12}
$$
(Paciente 2.) Cada administración se modela como una infusión de duración 1/24 d (1 h).

### 4.5 Observable comparado con los datos [p. 7]

$$
V_{vis} = \int_\Omega \mathbf{1}_{\{x\in\Omega:\ \phi(x) > 0.3\}}(x)\,dx
$$
(sin número). Justificación: "In CT images, only a small part of the tumor cells are visible" [p. 7]. No se precisa si φ = φ_T o φ_P (**ambigüedad**). En 3D se usa también umbral 0.3 para contornos de proliferativas y necróticas [p. 11].

### 4.6 Condiciones iniciales

- **No reportadas explícitamente** (sin fórmulas ni radio inicial).
- Paciente 1: "We start with an initial tumor volume with enough temporal distance from the previous therapy window" [p. 7]. Fig. 3A (t = 1): tumor completamente proliferativo φ_P ≈ 1 hasta r ≈ 0.005–0.006 m, φ_N = 0, φ_{σ,i} ≈ 0.31 en el centro → ≈ 0.97 en r = 0.012 [p. 8, visual]. [Lector] En Fig. 2A la simulación comienza en el día ≈ 176 del eje de datos, con V_vis ≈ 1.161 cm³, exactamente el valor del 3.er dato observado (los dos primeros datos, días 0 y 56, quedan fuera de la simulación).
- Paciente 2: "the first data point is ignored and a plausible tumor volume is assumed" [p. 9]. Fig. 4A: φ_P ≈ 1 hasta r ≈ 0.004 m, φ_N = 0, φ_{σ,i} ≈ 0.38 en el centro [p. 9, visual]. [Lector] V_vis inicial digitalizado ≈ 0.50 cm³ en Fig. 2B y ≈ 0.43 cm³ en Fig. 5B (no coinciden). φ_τ inicial: [Lector] la curva de Fig. 2B arranca ya cerca del estado periódico (pico ≈ 1.0·10^17 en t ≈ 14 d); valor inicial no reportado.

### 4.7 Dominio y geometría

- **1D:** esfera de radio 4 cm, 500 elementos [p. 7].
- **3D:** geometría pulmonar y vasculatura del Paciente 1 extraídas de su CT "at the therapy's onset" [p. 13]; pulmón segmentado con 3D Slicer, simplificado con 3D Builder (Microsoft) y Blender, remallado grueso con gmsh; vasculatura con la extensión vmtk de Slicer [p. 13]; refinamiento local cerca de la posición inicial del tumor (Fig. 7B) [pp. 13–14]. Número de elementos/nodos, tamaño de malla, posición/tamaño inicial del tumor: **No reportado**.

### 4.8 Discretización numérica [p. 13, verificado visualmente; p. 7]

- FEM con funciones base lineales a trozos para φ_P, μ_P, φ_N, φ_{σ,v}, φ_{σ,i} [p. 13].
- Ec. (1): esquema semi-implícito; fuentes, sumideros y movilidades explícitos; función de corte ("cutoff") en los términos de la derecha porque Cahn–Hilliard no garantiza 0 ≤ φ_P ≤ 1 (forma de la función: **No reportada**) [p. 13].
- Splitting convexo–cóncavo (Eyre [60]) [p. 13]:
$$
\tilde\Psi_i = \tfrac{3}{2}c_\Psi\phi^2,\qquad \tilde\Psi_e = c_\Psi\left(-2\phi^3 - \tfrac12\phi^2 + \phi^4\right),
$$
$\tilde\Psi_e$ cóncava en $\left[\tfrac12-\tfrac{1}{\sqrt3},\ \tfrac12+\tfrac{1}{\sqrt3}\right]\supset[0,1]$; $\Psi_i(\phi_P,\phi_N)=\tilde\Psi_i(\phi_P)+\tilde\Psi_i(\phi_P+\phi_N)$, $\Psi_e(\phi_P,\phi_N)=\tilde\Psi_e(\phi_P)+\tilde\Psi_e(\phi_P+\phi_N)$; cóncava si $\phi_P\in\left[\tfrac12-\tfrac{1}{\sqrt3},\ \tfrac12+\tfrac{1}{\sqrt3}-\phi_N\right]\supset[0,1-\phi_N]$. Sin fuentes: estabilidad de gradiente incondicional con Ψ_i implícito y Ψ_e explícito. ([Lector] comprobado: Ψ̃_i + Ψ̃_e = c_Ψ φ²(1−φ)².)
- Solver lineal: MINRES con precondicionador diagonal por bloques (generalización de [61]); bloques invertidos con multigrid algebraico (PETSc [62]):
$$
\mathcal{P} := \begin{pmatrix} (c_m\tau)K_m + \sqrt{c_m\tau}\,M & \\ & \epsilon^2 K_1 + \frac{6c_\Psi}{\sqrt{c_m\tau}}\,M \end{pmatrix} \tag{13}
$$
(K_m, K_1, M no se definen; τ aquí es el paso de tiempo, colisión de notación con el fármaco.)
- Ec. (3): Euler explícito. Ecs. (4)–(5): φ_P explícito; como η_iv = 0 se desacoplan y se resuelven con Gradiente Conjugado + AMG [p. 13].
- Ec. (6): Euler explícito con paso mucho menor [p. 13]: Δt = 1/24 d para el tumor y 32 subpasos para φ_τ [p. 7].
- Software: FEniCS [63] [p. 13]. Versión, hardware, tiempo de cómputo: **No reportado**.

### 4.9 Modelo de fármaco / inmunoterapia

- Inmunoterapia pasiva anti-PD-1 (eje PD-1/PD-L1) [p. 3].
- Un único escalar φ_τ para todo el pulmón (sin distribución espacial) [p. 1].
- PK: cinética de primer orden con vida media t_{1/2} (26.7 d nivolumab; 22.0 d pembrolizumab) y entrada de orden cero durante 1/24 d por dosis [Ec. 6, p. 4; Ecs. 11–12, p. 7; Tabla 1].
- PD: efecto Emax/Hill–Langmuir con n = 1, EC50 = φ_τ^{50} = 1.012·10^16 ("[mol]" en Tabla 1, pero por magnitud es un número de moléculas), escalado por λ_τ^{eff}/ω [Ec. 2; Tabla 1].
- [Lector] Consecuencia literal de (6): cada dosis aporta N_A d_τ/(24 M_τ) moléculas (la tasa no se divide por la duración del intervalo). Para el Paciente 1: 4.125·10^16 por dosis; estado periódico pico 1.354·10^17, valle 9.41·10^16 — coincide con lo digitalizado en Fig. 2A (salto de la 1.ª dosis 0.412·10^17; picos 1.353·10^17; valles 0.948·10^17).

## 5. Tabla de parámetros (Tabla 1 [p. 5], verificada visualmente)

Origen: los autores solo declaran que d_τ, M_τ y t_{1/2} "are known a priori from the given therapy" [p. 11] y que λ_P^{pro}, λ, λ_PN y λ_τ^{eff} son específicos del paciente y calibrados manualmente [pp. 7, 9, 11]. Para el resto **no se indica fuente ni justificación** (se registra como "Supuesto/no justificado"). "Rango explorado" = valores usados en el documento.

| Símbolo | Significado | Valor 1D P1 | Valor 1D P2 | Valor 3D P1 | Unidad | Rango explorado | Origen | Ubicación |
|---|---|---|---|---|---|---|---|---|
| c_m | Movilidad de proliferativas | 5·10⁻⁴ | 5·10⁻⁴ | 5·10⁻⁴ | m²/d | — | No justificado | Tabla 1 |
| λ_P^{pro} | Tasa de proliferación | 0.38 | 0.0038 | 0.53 | 1/d | 0.0038–0.53 | Calibrado manual (1D); 3D sin explicación | Tabla 1; pp. 7, 9 |
| λ | Exponente (penaliza crecimiento a baja concentración) | 2 | 1 | 2 | – | {1, 2} | Calibrado manual | Tabla 1; pp. 7, 9, 11 |
| λ_PN | Tasa proliferativa→necrótica | 0.1 | 20 | 0.025 | 1/d | 0.025–20 | Calibrado manual (1D); 3D sin explicación | Tabla 1; pp. 7, 9 |
| σ_PN | Umbral de nutriente para necrosis | 0.2 | 0.2 | 0.2 | – | — | No justificado | Tabla 1 |
| ε_P | Ancho de interfase | 5·10⁻⁴ | 5·10⁻⁴ | 5·10⁻⁴ | m | — | No justificado | Tabla 1 |
| c_Ψ | Escala del doble pozo | 2 | 2 | 2 | – | — | No justificado | Tabla 1 |
| ε_g | Regularización Gompertz | 0.1 | 0.1 | 0.1 | – | — | No justificado | Tabla 1 |
| χ | Quimiotaxis | 0 | 0 | 0 | – | — | Desactivado | Tabla 1 |
| κ_v | Difusión de nutriente en vasculatura | – | – | 10⁻³ | m²/d | — | No justificado | Tabla 1 |
| κ_i | Difusión en intersticio | 10⁻⁵ | 10⁻⁵ | 10⁻⁵ | m²/d | — | No justificado | Tabla 1 |
| ξ_va | Acoplamiento arterias pequeñas–grandes | – | – | 0 | 1/d | — | Desactivado | Tabla 1 |
| η_vi | Acoplamiento vasculatura→intersticio | 1 | 1 | 1 | 1/d | — | No justificado | Tabla 1 |
| η_iv | Acoplamiento intersticio→vasculatura | 0 | 0 | 0 | 1/d | — | Desactivado (p. 13) | Tabla 1; p. 13 |
| α_H | Consumo de nutriente, células sanas | 4 | 4 | 4 | 1/d | — | No justificado | Tabla 1 |
| α_P | Consumo, proliferativas | 1 | 1 | 1 | 1/d | — | No justificado | Tabla 1 |
| β | Fuente desde vasos grandes | – | – | 0.1 | m/d | — | No justificado | Tabla 1 |
| λ_τ^{eff} | Efecto inmunoterapéutico | 4.49 | **0.55** (Tabla) / **0.499** (texto p. 9) | 4.49 | kg/d | 0.499–4.49 | Calibrado manual | Tabla 1; pp. 7, 9 |
| φ_τ^{50} | Concentración de semirrespuesta | 1.012·10¹⁶ | 1.012·10¹⁶ | 1.012·10¹⁶ | "mol" (de facto nº moléculas) | — | No justificado (el formato Hill–Langmuir sigue [16]) | Tabla 1; p. 4 |
| d_τ | Dosis por intervalo | 0.24 | 0.20 | 0.24 | g | P1: 18–100 % (Fig. 5A); P2: ×2, ×10 (p. 11, sin figura) | Conocido (terapia) | Tabla 1; p. 11 |
| M_τ | Masa molar | 146.000 (=146 000) | 143.600 (=143 600) | 146.000 | g/mol | — | Conocido | Tabla 1; p. 11 |
| t_{1/2} | Vida media sérica | 26.7 | 22.0 | 26.7 | d | — | Conocido | Tabla 1; p. 11 |
| ω | Peso del paciente | 80 | 80 | 80 | kg | — | No justificado (igual para ambos) | Tabla 1 |
| N_A | Constante de Avogadro | 6.022140857·10²³ | — | — | 1/mol | — | Constante | p. 4 |

Otros parámetros numéricos/implícitos no incluidos en la Tabla 1:
- Umbral de visibilidad 0.3 [p. 7]; radio del dominio 1D 4 cm, 500 elementos, Δt = 1/24 d, 32 subpasos [p. 7].
- t_S = 296 d (P1), t_{Q6W} = 514 d, t_{PD} = 1063 d (P2) [pp. 6–7]; t_P (P1): valor numérico **No reportado** en el texto.
- φ_{σ,v} constante en 1D: **No reportado**. [Lector] Con η_vi = 1, η_iv = 0, α_H = 4 y φ_P = 0, el equilibrio lejos del tumor es φ_{σ,i} = φ_{σ,v}/4; como Figs. 3–4 muestran φ_{σ,i} → ≈1 lejos del tumor, sugiere φ_{σ,v} ≈ 4 (inferencia, no confirmada).
- Condiciones iniciales (radio, perfil): **No reportado**.

**Conteo [Lector]:** 23 filas en la Tabla 1 (+ N_A). En 1D activos ≈ 19 (κ_v, ξ_va, β no aplican). Calibrados por paciente: 4 (λ_P^{pro}, λ, λ_PN, λ_τ^{eff}). No reportados pero necesarios: φ_{σ,v}, condición inicial (radio/volumen), φ_τ(0) para P2, offset temporal entre el eje de datos y el de simulación, función de corte.

## 6. Datos de pacientes

- **Fuente:** volumetría anonimizada de tumores primarios y metástasis desde cortes CT rutinarios, procesados con syngo.CT Lung CAD (LCAD) de Siemens Healthineers en syngo.Via [p. 6]. Mediciones: volumen tumoral segmentado manualmente, RECIST v1.1 [58] y criterio bidimensional OMS (WHO) [p. 6].
- **Forma de publicación:** solo gráficos (Fig. 1 [p. 6]; los volúmenes reaparecen como "real" en Figs. 2 y 5 [pp. 8, 10]). **No hay tabla numérica, suplemento ni repositorio.** Fechas de cada CT: no listadas.
- **Digitalización [Lector]:** extraída de los marcadores vectoriales del PDF (Fig. 1, p. 6) y calibrada con las líneas de rejilla; error esperado < 1 % del rango del eje. **No son datos publicados por los autores.** Tiempo en días del eje de cada figura.

**Paciente 1 — Fig. 1A (eje t: 0 = diagnóstico). 21 tiempos × 3 medidas.**

| t (d) | Volumen "LCAD" (cm³) | RECIST (mm) | WHO (mm²) |
|---|---|---|---|
| 0 | 1.330 | 19.3 | 327 |
| 56 | 1.477 | 19.5 | 250 |
| 176 | 1.161 | 16.0 | 187 |
| 247 | 0.835 | 16.0 | 187 |
| 267 | 1.120 | 17.9 | 198 |
| 322 | 2.922 | 22.9 | 365 |
| 378 | 1.171 | 19.1 | 210 |
| 469 | 0.387 | 11.8 | 70 |
| 658 | 0.072 | 6.7 | 40 |
| 729 | 0.312 | 11.1 | 74 |
| 792 | 0.220 | 10.1 | 77 |
| 939 | 0.112 | 9.1 | 45 |
| 1015 | 0.317 | 14.6 | 124 |
| 1121 | 0.409 | 15.5 | 145 |
| 1288 | 0.471 | 15.6 | 178 |
| 1541 | 0.123 | 8.5 | 53 |
| 1764 | 0.112 | 8.8 | 46 |
| 1862 | 0.290 | 8.9 | 25 |
| 2163 | 0.170 | 9.6 | 51 |
| 2255 | 0.120 | 7.4 | 27 |
| 2346 | 0.100 | 5.8 | 24 |

(Los mismos 21 volúmenes aparecen como "real" en Fig. 2A con idéntico eje temporal.)

**Paciente 2 — Fig. 1B (eje t de Fig. 1B; en Fig. 2B/5B el eje está desplazado −114 d, primer dato en t = 0).** 11 volúmenes; RECIST y WHO solo para los 6 primeros.

| t Fig. 1B (d) | t Fig. 2B (d) | Volumen "Manual" (cm³) | RECIST ("cm" según eje) | WHO ("cm²" según eje) |
|---|---|---|---|---|
| 114 | 0 | 0.067 (ignorado en la calibración, p. 9) | 13.5 | 81 |
| 156 | 42 | 0.388 | 12.4 | 116 |
| 218 | 104 | 0.172 | 9.5 | 61 |
| 285 | 171 | 0.120 | 8.3 | 37 |
| 404 | 290 | 0.087 | 8.8 | 44 |
| 499 | 385 | 0.067 | 8.3 | 37 |
| 684 | 570 | 0.051 | – | – |
| 827 | 713 | 0.047 | – | – |
| 986 | 872 | 0.050 | – | – |
| 1125 | 1011 | 0.037 | – | – |
| 1266 | 1152 | 0.065 | – | – |

**Total de observaciones [Lector]:** P1: 21 volúmenes (19 dentro de la ventana simulada); P2: 11 volúmenes (10 usados). Solo el volumen se usa para el ajuste (Figs. 2, 5); RECIST/WHO solo se muestran. No hay datos de la expansión final del tumor del P2 en la figura más allá del último punto (0.065 cm³), aunque el texto afirma que el CT final muestra una gran masa [p. 7].

## 7. Calibración

- **Parámetros ajustados:** λ_P^{pro}, λ_τ^{eff}, λ, λ_PN, por paciente [pp. 7, 9, 11]. En 3D (P1), λ_P^{pro} = 0.53 y λ_PN = 0.025 difieren de 1D sin que se explique cómo se obtuvieron [Tabla 1].
- **Datos:** volumen tumoral visible vs. V_vis simulado [pp. 7, 9; Fig. 2].
- **Método:** "manually calibrated" [pp. 7, 9]. **No hay algoritmo de optimización, función de pérdida, métrica de bondad de ajuste ni intervalos de confianza.**
- **Manipulación de datos:** P2: "the first data point is ignored and a plausible tumor volume is assumed" [p. 9]. P1: [Lector] la simulación arranca en el 3.er dato (día ≈176), los dos primeros no se modelan.
- **Calibración vs. validación:** **no se separan**. Toda la serie (incluyendo el desenlace) se usa para inferir parámetros: "inferred over the whole simulation time, including the clinical outcomes" [p. 12].
- **Predicción fuera de muestra:** **ninguna**. Las simulaciones de dosis/esquema (Fig. 5) son contrafactuales no verificables.
- **Bondad de ajuste [Lector, de valores digitalizados en Fig. 2]:**
  - P1 (19 puntos, t ≥ 176): RMSE ≈ 0.39 cm³, MAE ≈ 0.22 cm³, error máx. ≈ 1.15 cm³ (día 267: sim 2.27 vs obs 1.12), MAPE ≈ 48 %. Tras el día ~700 la simulación es casi constante (≈ 0.165 cm³) y no reproduce las oscilaciones observadas 0.07–0.47 cm³ (p. ej., el repunte 0.32–0.47 cm³ en días 1015–1288).
  - P2 (10 puntos, excluyendo el primero): RMSE ≈ 0.044 cm³, MAE ≈ 0.027 cm³, MAPE ≈ 24 %; mayor error en t = 104 d (sim 0.29 vs obs 0.17).

## 8. Resultados (cifras exactas)

**1D, Paciente 1** [pp. 7–9; Figs. 2A, 3]
- Parámetros: λ_P^{pro} = 0.38, λ_τ^{eff} = 4.49, λ = 2, λ_PN = 0.1 [p. 7].
- V_vis "qualitatively follows the segmented data points" [p. 7]; tras pocos meses φ_τ alcanza un estado cuasi-periódico [p. 7]. La inmunoterapia elimina las proliferativas; al final solo quedan necróticas y el tumor permanece controlado sin fármaco [p. 7] — "in agreement with our clinical observations" (remisión completa del primario) [pp. 7, 9].
- Fig. 3 (t = 1, 148, 192, 640 según los títulos de los paneles): A inicial totalmente proliferativo con caída de nutriente; B antes de la terapia, núcleo parcialmente necrótico; C durante la terapia, "unexpected increase of nutrients near the necrotic tumor core" y "large undershoot of the proliferative cells" (φ_P < 0 visible); D capa proliferativa se contrae, queda núcleo necrótico [pp. 7–9].
- [Lector, digitalizado]: V_vis máx. ≈ 3.35 cm³ en día ≈ 322; V_vis final ≈ 0.165 cm³; masa necrótica final ≈ 0.21·10⁻⁶ (unidad del eje "mass", probablemente m³); masa proliferativa final ≈ 3·10⁻¹⁰; φ_τ pico ≈ 1.35·10^17.

**1D, Paciente 2** [p. 9; Figs. 2B, 4]
- Parámetros: λ_P^{pro} = 0.0038, λ_τ^{eff} = 0.499 (texto; 0.55 en Tabla 1), λ = 1, λ_PN = 20 [p. 9].
- El tumor visible disminuye hasta autosostenerse y se mantiene constante; el paso a Q6W reduce φ_τ sin impacto visible; las células se diseminan por todo el pulmón → aumento continuo de la masa total; luego crecimiento "exponencial" del tumor visible, "in line with the observed outcome" [p. 9].
- Fig. 4: a 170 d núcleo necrótico + capa proliferativa; a 600 d la capa colapsa; a "1.175 days" (= 1175 d) tumor diseminado, nutriente baja de 1 a ≈0.9 y se inicia separación de fases con crecimiento drástico [pp. 9–10]. [Lector] En Fig. 4B–D φ_T supera 1 (≈1.08) y φ_P muestra valores ligeramente negativos.
- [Lector, digitalizado]: V_vis sale del rango del gráfico (>0.5 cm³) en t ≈ 1200 d (eje Fig. 2B), es decir, tras el fin de la terapia (PD ≈ 1104 en ese eje); masa total ≈ 3.9·10⁻⁵ al final.

**Contrafactuales** [pp. 10–11; Fig. 5]
- P1, dosis al 23 %, 22 % y 18 % (reducción de 77, 78 y 82 %) [p. 10]: 23 % erradica antes del fin de la terapia; 22 % deja células residuales → recaída que supera el volumen máximo antes del fin de la ventana simulada; 18 % → equilibrio (control sin erradicación) y recrecimiento al suspender. "50 percent of the dosage would have been more than enough to cure the cancer" [p. 10].
- P2, esquemas Q3W/Q6W (original), Q3W continuo, Q3W/Q6W extendido sin pausa: extender "had close to no effect"; Q3W continuo retrasa el crecimiento ≈ 3 meses [pp. 10–11]. Con Q3W, duplicar la dosis retrasa el crecimiento explosivo ≈ medio año; ×10 ≈ un año adicional (sin figura) [p. 11]. El tumor "cannot be cured with the used drug" porque el término Hill–Langmuir satura [p. 11].
- [Lector] Fig. 5B usa φ_τ con picos ≈ 7.3·10^16 (Q3W), coherente con los parámetros PK del P2 de la Tabla 1; en cambio Fig. 2B no (ver §14).

**3D, Paciente 1** [pp. 11–12; Fig. 6]
- Déficit de nutriente cerca del tumor desde el día 20, máximo a 140 d; a 300 d el efecto desaparece; núcleo necrótico a 60 d desplazado hacia la zona pobre en nutrientes; tamaño máximo a 140 d "shortly before the immunotherapy starts"; capa proliferativa residual orientada hacia la fuente de nutrientes; al final mayormente necrótico [pp. 11–12]. Instantáneas: días 20, 60, 140, 190, 200, 220, 240, 280, 300, 450 [Fig. 6]. **No hay comparación cuantitativa 3D vs. datos.**

## 9. Sensibilidad, incertidumbre, identificabilidad

- **Hecho:** (i) observaciones cualitativas sobre λ (λ = 2 localiza; λ = 1 disemina y produce crecimiento explosivo) [pp. 7, 11]; (ii) exploración de un factor (dosis: 18/22/23/100 % en P1; ×2, ×10 en P2; esquemas en P2) [pp. 10–11]; (iii) reconocimiento cualitativo de compensación λ_P^{pro}–λ_τ^{eff}: "have to counterbalance each other. Especially for Patient 2 ... they are hard to determine" [p. 11].
- **No hecho:** análisis de sensibilidad local o global (Sobol, Morris), cuantificación de incertidumbre (bayesiana o frecuentista), análisis de identificabilidad estructural o práctica (perfiles de verosimilitud), estudio de convergencia de malla/paso de tiempo, sensibilidad al umbral 0.3, a la condición inicial o a la geometría (salvo la mención cualitativa de que la geometría importa [p. 10]).

## 10. Limitaciones declaradas por los autores

- Simplicidad deliberada: "in a simple, deterministic setting" [p. 3]; "To keep the model as simple as possible, we do not explicitly model hypoxic cell species" [p. 3].
- Ajuste solo cualitativo: "our model can qualitatively describe observations during immunotherapy" [p. 1]; "a preliminary proof of concept" [p. 12].
- Dependencia de parámetros inferidos con el desenlace: "strongly depends on patient-specific parameters unknown a priori and inferred over the whole simulation time, including the clinical outcomes" [p. 12].
- Estimación de parámetros pendiente: "the parameter estimation should be addressed in particular" [p. 12]; necesidad de grandes conjuntos de datos y priors poblacionales [p. 12].
- Identificabilidad: λ_P^{pro} y λ_τ^{eff} "are hard to determine" para P2 [p. 11].
- Geometría: "the simulation geometry does play a role" en el crecimiento explosivo del P2 [p. 10].
- Numérica: Cahn–Hilliard "does not guarantee the boundedness, 0 ≤ φ_P ≤ 1", se usa una función de corte [p. 13].
- Calidad de datos: embolia que influye "the data quality and LCAD accuracy" (P1) [p. 7]; primer dato del P2 ignorado [p. 9].

## 11. Evaluación del lector (crítica)

- **n = 2 pacientes**, sin cohorte de validación; ningún resultado es generalizable.
- **Datos vs. parámetros:** P1 ≈ 19 volúmenes y P2 ≈ 10 volúmenes en la ventana simulada, frente a 4 parámetros calibrados por paciente + ≈15 fijados sin justificación + condiciones iniciales y φ_{σ,v} libres no reportados. El cociente datos/parámetros efectivos es bajo y los parámetros "fijos" no tienen fuente, por lo que el ajuste depende de muchas decisiones no documentadas.
- **Sobreajuste / ajuste ad hoc:** calibración manual sin función objetivo; descarte de un dato (P2) y de dos datos iniciales (P1, inferido); la calidad de ajuste es modesta (MAPE ≈ 48 % P1, ≈ 24 % P2, [Lector]) y la dinámica tardía del P1 (repuntes 0.3–0.47 cm³) no se captura.
- **Identificabilidad:** λ_P^{pro}/λ_τ^{eff} compensados (reconocido por los autores); λ es discreto ({1, 2}) y determina cualitativamente el desenlace (localizado vs. explosivo); el valor de λ del P2 parece elegido para reproducir el desenlace conocido (muerte), no inferido de datos previos. La variación de λ_PN en tres órdenes de magnitud (0.1 vs 20) entre pacientes sugiere mala identificabilidad. Los valores 1D y 3D del mismo paciente difieren (λ_P^{pro} 0.38 vs 0.53; λ_PN 0.1 vs 0.025).
- **Validación externa:** ausente. No hay predicción prospectiva ni hold-out temporal. El crecimiento final del P2 no tiene datos de volumen graficados que lo confirmen cuantitativamente (último dato 0.065 cm³).
- **Supuestos biológicos fuertes:** fármaco como escalar único para todo el pulmón sin distribución espacial ni dinámica inmune (no hay células T, PD-1/PD-L1 explícitos); efecto citotóxico directo proporcional a ocupación tipo Emax; estacionariedad de nutrientes; simetría esférica en 1D; crecimiento solo en interfaz; necrosis por umbral duro (Heaviside); peso 80 kg igual para ambos; "visibilidad" por umbral 0.3 arbitrario; un solo tumor modelado pese a que los datos incluyen metástasis.
- **Inconsistencias internas** (detalle en §14): λ_τ^{eff} del P2 (0.55 vs 0.499); Fig. 2B parece simulada con PK del nivolumab (P1) y no del pembrolizumab (P2); desfases temporales entre texto y figuras; definición de ω contradictoria; unidad de φ_τ^{50}. Afectan directamente la reproducibilidad.
- **Afirmaciones fuertes poco sustentadas:** "50 percent of the dosage would have been more than enough to cure the cancer" [p. 10] se basa en un único conjunto de parámetros manual, sin incertidumbre.
- **Positivo:** ecuaciones completas y parámetros tabulados; PK reproducible exactamente; geometría 3D de paciente real; datos graficados en formato vectorial (digitalizables con alta precisión).

## 12. Disponibilidad de código, datos y suplementos

- **Sección "Data availability":** No existe en el documento.
- **Código:** No reportado. Solo se indica "For our implementation, we use the FEniCS framework [63]" [p. 13]. No hay URL de repositorio (GitHub/Zenodo).
- **Datos:** No publicados en forma numérica; solo Fig. 1 [p. 6]. Anonimizados y con aprobación ética BLAEK 19021 [p. 6]; no se indica vía de acceso.
- **Suplementos:** No reportado / no hay.
- **URLs que aparecen:** solo herramientas en referencias: https://www.blender.org/ (ref. 65), www.vmtk.org/ (ref. 67), https://www.taylorfrancis.com/books/9781136977381 (ref. 2) [pp. 14, 18].
- **Malla 3D / geometría del paciente:** no disponible.

## 13. Reproducibilidad

**Reproducible con la información publicada (Python):**
1. **Curvas de φ_τ (paneles centrales de Figs. 2A, 5A, 5B)** — Ec. (6) + Ecs. (11)–(12) + Tabla 1. [Lector] Verificado analíticamente: P1 pico periódico 1.354·10^17 y valle 9.41·10^16 vs. 1.353·10^17 / 0.948·10^17 digitalizados; Fig. 5B Q3W pico ≈ 7.2·10^16 coherente con PK del P2. Solo falta fijar el origen temporal (primera dosis en día ≈322 en Fig. 2A, no 296).
2. **Datos observados (Fig. 1)** — digitalizables con precisión desde los vectores del PDF (tablas en §6).
3. **Modelo 1D radial (Figs. 2, 3, 4, 5)** — parcialmente reproducible. Ecuaciones (7)–(10), (3), (6) y Tabla 1 están completas, pero **falta**: valor de φ_{σ,v}; condición inicial (radio y perfil de φ_P, φ_τ(0) en P2); forma exacta de la función de corte; qué campo entra en V_vis (φ_T o φ_P); correspondencia exacta entre el eje temporal de datos y el de simulación (P1 empieza en día ≈176; t_S); unidades del eje "mass"; qué valor de λ_τ^{eff} del P2 es el correcto (0.55 o 0.499) y qué PK se usó en Fig. 2B. Implementable con FEniCSx/scikit-fem o diferencias finitas en coordenadas esféricas (500 elementos en 4 cm, Δt = 1/24 d). La reproducción será cualitativa salvo que se recuperen estos datos de los autores.
4. **3D (Fig. 6)** — no reproducible: falta la geometría/malla del paciente, la vasculatura Γ y la condición inicial.

**Versión reducida derivada directamente de las ecuaciones del artículo (EDO espacialmente homogénea):** si φ_P, φ_N y φ_{σ,i} son uniformes, los términos de flujo de (1)/(7) se anulan y (5)/(10) pasan a algebraicos, de modo que el sistema se reduce a:

$$
\frac{d\phi_P}{dt} = \lambda_P^{pro}\,\phi_{\sigma,i}\,\phi_P^{\lambda}\ln\!\frac{1+\epsilon_g}{\phi_P+\epsilon_g} - \frac{\lambda_\tau^{\mathrm{eff}}}{\omega}\,\phi_P\,\frac{\phi_\tau}{\phi_\tau+\phi_\tau^{50}} - \lambda_{PN}\,\mathcal{H}(\sigma_{PN}-\phi_{\sigma,i})\,\phi_P,
$$
$$
\frac{d\phi_N}{dt} = \lambda_{PN}\,\mathcal{H}(\sigma_{PN}-\phi_{\sigma,i})\,\phi_P,\qquad
\phi_{\sigma,i} = \frac{\eta_{vi}\,\phi_{\sigma,v}}{\eta_{iv} + \alpha_H(1-\phi_P) + \alpha_P\,\phi_P},
$$
más la Ec. (6) sin cambios. Útil para: estudiar el umbral de dosis (balance crecimiento vs. λ_τ^{eff}/ω · Emax), efectos de esquema y la compensación λ_P^{pro}–λ_τ^{eff} (identificabilidad). **Qué se pierde:** (i) la distinción interfaz/volumen (en el artículo el crecimiento actúa en la interfaz y la terapia en el volumen, mecanismo central de las Figs. 3–4); (ii) el observable V_vis por umbral 0.3 (en la EDO no hay volumen; habría que introducir un mapeo masa→volumen que el artículo no define); (iii) la formación de núcleo necrótico por gradiente de nutriente (con nutriente uniforme la necrosis es todo-o-nada); (iv) la diseminación por todo el dominio con λ = 1 y la separación de fases que genera el crecimiento explosivo del P2; (v) cualquier efecto de geometría. Por tanto **no puede reproducir cuantitativamente las Figs. 2–5**; sirve solo como modelo de juguete de la parte de reacción + PK/PD.

## 14. Problemas de extracción e inconsistencias del documento

**Problemas de extracción del .txt (corregidos verificando el PDF visualmente):**
- Ecuaciones (1)–(13) y la definición de V_vis fragmentadas (superíndices/subíndices y fracciones desarmados, p. ej. "λpro P φσ,i (φP )λ ln 1 + ϵg φP + ϵg") [pp. 3–5, 7, 13]. Transcritas en §4 desde las imágenes.
- Tabla 1 linealizada: se pierde qué valores abarcan las tres columnas (P1 1D, P2 1D, P1 3D) y qué celdas son "-" [p. 5]. Reconstruida en §5.
- Figuras 1, 2, 3, 4, 5 reducidas a etiquetas de ejes sueltas [pp. 6, 8–10]; Fig. 6 y 7 son imágenes 3D sin texto útil [pp. 11, 14]. Datos recuperados por extracción vectorial (§6).
- "1e" y "6"/"5" en ejes de masa: el signo menos se pierde ("1e−6", "1e−5") [pp. 8, 10].
- "Allg¨au", "Landes¨arztekammer": diacríticos separados [pp. 1, 6].

**Inconsistencias en el propio documento (no son errores de extracción):**
1. λ_τ^{eff} del P2: 0.55 en Tabla 1 [p. 5] vs. 0.499 en el texto [p. 9].
2. [Lector] Fig. 2B (P2): las curvas de φ_τ tienen picos ≈ 1.0·10^17 (Q3W) y ≈ 0.62·10^17 (Q6W), lo que coincide exactamente con la PK del **nivolumab/P1** (0.24 g, 146 000 g/mol, 26.7 d: pico periódico teórico 0.98·10^17 y 0.62·10^17) y no con la del P2 de la Tabla 1 (0.72·10^17 y 0.48·10^17). La Fig. 5B sí es coherente con la PK del P2 (picos ≈ 7.3·10^16). Además, V_vis inicial difiere entre Fig. 2B (≈0.50) y Fig. 5B (≈0.43).
3. Cronología: texto t_S = 296 d (P1) [p. 6] vs. primera dosis simulada en el día ≈322 en Fig. 2A [Lector]. P2: texto Q6W = 514, PD = 1063, EL = 1306 [p. 7] vs. Fig. 1B 671/1218/1431 y Fig. 2B 557/1104/1317 [Lector]. t_P del P1 no se da numéricamente.
4. ω: "1/ω is the ratio of the lung weight to the body weight" [p. 4] vs. "ω [kg] Patient weight" [Tabla 1, p. 5].
5. φ_τ^{50} con unidad "[mol]" pero valor 1.012·10^16 comparable a números de moléculas [Tabla 1].
6. Unidades de d_τ: sin unidad en [p. 4]; [g] en Tabla 1.
7. Fig. 1A rotula "LCAD [cm³]" mientras el texto habla de "manually segmented tumor volume" [p. 6]; Fig. 1B rotula "Manual [cm³]".
8. Fig. 1B: RECIST en "cm" (8–13.5) y WHO en "cm²" (37–116) parecen incompatibles con volúmenes de 0.04–0.39 cm³; probable error de unidades en los ejes [Lector].
9. Notación: "λ_τ^{φEFF}" [p. 11] vs. "λ_τ^{eff}" [pp. 4–5, 7, 9]; ε_P vs ϵ_P; "χφ_σ" en (8); τ usado como paso de tiempo en (13); "Hill–Langmuire" [p. 11]; "Emblie" [p. 6]; "tree weekly" [p. 6]; "non-small-scale cell lung cancer" [p. 1].
10. "1.175 days" = 1175 días (separador de miles) [pp. 9, 10]; "146.000"/"143.600" g/mol = 146 000/143 600.
11. Fig. 3C: el pie dice "Just after therapy starts" [p. 8]; el texto lo describe como "a snapshot taken during the therapy" [p. 9].
12. Fig. 6: necróticas en naranja según el pie [p. 11] y "yellow" según el texto [p. 11].
13. Abstract/Discusión: "qualitatively" [pp. 1, 12] vs. Author summary: "we can quantitatively describe the tumor's behavior with some parameter set" [p. 2].
14. [Lector] Violación de cotas pese al "cutoff": φ_T > 1 y φ_P < 0 visibles en Figs. 3C y 4B–D [pp. 8–9].

## 15. Citas textuales clave (≤ 40 palabras cada una)

1. "we show that our model can qualitatively describe observations during immunotherapy by fitting our model parameters to existing patient data." [p. 1]
2. "Datasets from two clinical patients were available to verify our model." [p. 6]
3. "In CT images, only a small part of the tumor cells are visible." [p. 7]
4. "The manually calibrated parameters are λ_P^pro = 0.38, λ_τ^eff = 4.49, λ = 2 and λ_PN = 0.1." [p. 7]
5. "With respect to the tumor volumes in the topmost plot, the first data point is ignored and a plausible tumor volume is assumed, more in line with the previous values." [p. 9]
6. "We point out that, especially in the case of explosive growth in the second patient, the simulation geometry does play a role." [p. 10]
7. "Finally, we note that even considering safety margins, 50 percent of the dosage would have been more than enough to cure the cancer." [p. 10]
8. "It appears that according to our model, the given tumor cannot be cured with the used drug, and the therapy only manages to prolong the patient's life by a certain time." [p. 11]
9. "The parameters λ_P^pro and λ_τ^φEFF have to counterbalance each other. Especially for Patient 2 where both growth and therapy are always active, they are hard to determine." [p. 11]
10. "This is considered a preliminary proof of concept for the presented model." [p. 12]
11. "The model simulation strongly depends on patient-specific parameters unknown a priori and inferred over the whole simulation time, including the clinical outcomes." [p. 12]
12. "Since the Cahn–Hilliard equation does not guarantee the boundedness, 0 ≤ φ_P ≤ 1, we use a cutoff function on all right-hand side terms to achieve stability." [p. 13]
