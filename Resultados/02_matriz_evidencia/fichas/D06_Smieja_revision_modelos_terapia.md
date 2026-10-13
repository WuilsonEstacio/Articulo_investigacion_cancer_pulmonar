# Ficha D06 — Smieja (2023). Revisión de modelos matemáticos para terapia del cáncer de pulmón

> Convención de ubicación: `[p. N]` = página del PDF (coincide con la paginación “N of 21” de la revista). `Ec. (n)` = numeración de ecuaciones del documento. `[ref n]` = número de referencia de la bibliografía de D06.
> Fuentes: texto extraído (`00_extraccion_texto/Mathematical Modeling Support for Lung Cancer Therapy—A Short Review.txt`) y verificación visual de las páginas 4–10 del PDF (ecuaciones).

---

## 1. Referencia completa

- **Autor:** Jaroslaw Smieja (Department of Systems Biology and Engineering, Silesian University of Technology, Gliwice, Polonia) [p. 1].
- **Título:** “Mathematical Modeling Support for Lung Cancer Therapy—A Short Review” [p. 1].
- **Revista:** *International Journal of Molecular Sciences* **2023**, *24*, 14516 (número de artículo; 21 páginas: “1 of 21” … “21 of 21”) [p. 1, p. 21].
- **DOI (tal como aparece):** `https://doi.org/10.3390/ijms241914516` [p. 1].
- **Fechas:** recibido el 3 jul 2023; revisado el 1 sep 2023; aceptado el 12 sep 2023; publicado el 25 sep 2023 [p. 1]. Editor académico: Francisco Torrens [p. 1].
- **Licencia:** CC BY 4.0 [p. 1]. **Financiación:** NCN grant DEC-2020/37/B/ST6/01959 [p. 16]. **Conflictos de interés:** ninguno declarado [p. 16].
- **Referencias:** 125 [p. 16–21].

## 2. Tipo de documento y subtipo de cáncer

- **Tipo:** revisión (“Review”, encabezado [p. 1]); **narrativa**, autodefinida como “short review”.
- **¿Método de búsqueda declarado?** **No reportado.** No hay bases de datos, cadenas de búsqueda, criterios de inclusión/exclusión ni diagrama PRISMA. La única mención a una búsqueda es ilustrativa: una consulta en PubMed sobre inmunoterapia del cáncer de pulmón “returns over 2300 articles published in the last year alone” [p. 2–3]. Las referencias se presentan explícitamente como “only sample references” [p. 13].
- **Subtipo cubierto:** **ambos (NSCLC y SCLC)**, con mayor peso en NSCLC. Se menciona la quimioterapia para NSCLC [ref 14] y SCLC [ref 15] [p. 2]; la SBRT para NSCLC [p. 2]; ejemplos de modelos para SCLC [ref 110 = D07], para NSCLC [ref 68] y para el carcinoma pulmonar de Lewis en ratón [ref 111] [p. 14]. Sin embargo, el **marco matemático presentado (Ec. 1–40) es genérico**, no específico de pulmón (lo reconoce el autor, [p. 14]).
- **Nota de vínculo:** D06 cita a D07 (Salgia et al., 2018) como su referencia [110] [p. 14, p. 20].

## 3. Objetivo

- Revisar “models that can be used to describe dynamics of lung cancer growth and its response to treatment at both cell population and intracellular processes levels” (resumen) [p. 1].
- “This work is focused on models that have been developed to describe cancer growth and therapy effects” [p. 1]; concluye con la aplicabilidad de estos modelos y las direcciones futuras [p. 1–2].
- Exclusiones declaradas: no trata la cirugía ni la ablación térmica guiada por imagen como modelos explícitos [p. 2]; omite el análisis de imagen y la dosimetría detallada en radioterapia [p. 7].

## 4. Catálogo de modelos citados

Notación general del documento: N(t) = vector de tipos celulares, U(t) = vector de modos de terapia y X(t) = otras variables (nutrientes, O₂, citoquinas); f = crecimiento, g = efecto de la terapia, h = flujo entre compartimentos, p = producción, q = degradación/utilización [p. 4]. **Ningún modelo del catálogo trae valores numéricos de parámetros**; todos los parámetros se dan solo de forma simbólica.

| Clase de modelo | Ecuación tal como aparece (LaTeX) | Parámetros / valores numéricos | Referencia original citada | ¿Pulmón? ¿NSCLC/SCLC? | Página |
|---|---|---|---|---|---|
| Marco general ODE (población) | Ec. (1): $\frac{dN}{dt}=f(N(t),X(t),U(t))-g(N(t),U(t),X(t))+h(N(t),X(t),U(t))$ | Simbólicos; no hay valores | [51] Swierniak, Kimmel, Smieja et al., 2016 (libro), como introducción general | Genérico | [p. 4] |
| Marco general ODE (moléculas) | Ec. (2): $\frac{dX}{dt}=p(N(t),X(t),U(t))-q(N(t),X(t))$ | Simbólicos | [51] | Genérico | [p. 4] |
| Flujo entre compartimentos (incluye reclutamiento de quiescentes / fármacos citostáticos) | Ec. (3): $h_i(N(t),U(t),X(t))=a_i\cdot N(t)$, con $a_i=a_i(U(t))$ | $a_i$: vector de parámetros; sin valores | No se cita una referencia específica | Genérico | [p. 4] |
| Crecimiento exponencial | Ec. (4): $f(N(t),U(t),X(t))=\rho_1 N(t),\quad N(0)=N_0$ | $\rho_1$: tasa de crecimiento; sin valor | [51] (para variantes con $\rho=\rho(X(t),U(t))$) | Genérico | [p. 5] |
| Crecimiento logístico | Ec. (5): $f(N(t),U(t),X(t))=\rho_2 N(t)\left(1-\frac{N(t)}{K}\right),\quad N(0)=N_0$ | $\rho_2$, $K$ (capacidad de carga); sin valores | No hay una referencia específica | Genérico | [p. 5] |
| Crecimiento de Gompertz | Ec. (6): $f(N(t),U(t),X(t))=-\rho_3 N\ln\frac{N}{N_0},\quad N(0)=N_0$ | $\rho_3$; sin valor. Ver la observación del lector en §10 (el denominador es $N_0$, no $K$) | No hay una referencia específica | Genérico | [p. 5] |
| Von Bertalanffy | — | — | **No reportado** | — | — |
| Producción lineal | Ec. (7): $p_i(N(t),X(t))=\sum_i k_i N_i(t)$ | $k_i$; sin valores | — | Genérico | [p. 5] |
| Producción tipo Michaelis–Menten | Ec. (8): $p_i(N(t),X(t))=\sum_i \frac{k_{i1}N_i(t)}{k_{i2}+N_i(t)}$ | $k_{i1},k_{i2}$; sin valores | — | Genérico | [p. 5] |
| Degradación lineal | Ec. (9): $q_i(N(t),X(t))=k_{deg\_i}X_i(t)$ | $k_{deg\_i}$; sin valor | — | Genérico | [p. 5] |
| Captación bilineal | Ec. (10): $q_i(N(t),X(t))=\sum_i\sum_j k_{ij}N_i(t)X_j(t)$ | $k_{ij}$; sin valores | — | Genérico | [p. 5] |
| Captación tipo Michaelis–Menten | Ec. (11): $q_i(N(t),X(t))=\sum_i\sum_j \frac{k_{ij1}N_i(t)X_j(t)}{k_{ij2}+X_i(t)}$ | $k_{ij1},k_{ij2}$; sin valores | — | Genérico | [p. 5] |
| Cirugía (salto de condición) | Sin ecuación numerada: $N_i \rightarrow \mu N_i,\ \mu\le 1$ (con $\mu$ muestreado de una distribución a priori; $\mu=0$ = resección total, $\mu=1$ = cirugía ineficaz) | $\mu$; sin distribución especificada | — | Genérico (aplicable también a la ablación térmica) | [p. 5] |
| Quimioterapia (log-kill de Skipper) | Ec. (12): $g_i(N(t),U(t),X(t))=c_{ij}N_i(t)U_j(t)$ | $c_{ij}$; sin valor | [52] Skipper, Schabel, Wilcox, 1964 | Genérico (leucemia experimental en la fuente original, según el título de la ref.) | [p. 6] |
| Quimioterapia con PK | Ec. (13): $g_i(N(t),U(t),X(t))=c_{ij}N_i(t)c_j(t)$ | $c_{ij}$ | — | Genérico | [p. 6] |
| PK de un compartimento | Ec. (14): $\frac{dc_j}{dt}=U_j(t)-kc_j(t),\quad c_j(0)=0$ | $k$ (eliminación); sin valor | — | Genérico | [p. 6] |
| Combinación de fármacos con PD (sinergia) | Ec. (15): $g_i(N(t),U(t),X(t))=N(t)S_{3\_1}(t)+N(t)S_{3\_2}(t)$ | — | [53] Niu et al., 2020 (birinapant/paclitaxel en células de **cáncer de páncreas**) | **No pulmonar** | [p. 6] |
| PD con tránsito (Hill + sensibilización Ψ) | Ec. (16): $\frac{dS_{1\_i}}{dt}=\frac{1}{\tau_i}\cdot\left(\frac{K_{max\_i}c_i^{\gamma_i}(t)}{c_i^{\gamma_i}(t)+(\Psi\cdot KC_{50\_i})^{\gamma_i}}-S_{1\_i}\right)$ | $K_{max\_i}$ (tasa máxima de muerte), $KC_{50\_i}$, $\gamma_i$ (Hill), $\tau_i$ (tiempo medio de tránsito), $\Psi$ (Ψ≤1 sinergia; Ψ=1 aditivo; Ψ≥1 antagonismo). Sin valores | [53]; revisión de sinergia: [54] Chen et al., 2015 | No pulmonar | [p. 6] |
| PD, compartimento 2 | Ec. (17), **tal como está impresa**: $\frac{dS_{2\_i}}{dt}=\frac{1}{\tau_i}\cdot(S_{1\_i}-S_{1\_i})$ (probable errata, ver §10) | — | [53] | No pulmonar | [p. 6] |
| PD, compartimento 3 | Ec. (18): $\frac{dS_{3\_i}}{dt}=\frac{1}{\tau_i}\cdot(S_{2\_i}-S_{3\_i})$ | — | [53] | No pulmonar | [p. 6] |
| Radioterapia: modelo lineal-cuadrático (LQ) | Ec. (19): $g_i(N(t),U(t),X(t))=(\alpha d+\beta d^2)N$ | $\alpha,\beta$; **sin valores numéricos** | Formulación original: [55] Lea & Catcheside, 1942; relación usada: [56] Fowler, 1989 | Genérico | [p. 6–7] |
| Radioterapia: dosis biológicamente efectiva (BED) | Ec. (20), tal como está impresa: $d=nd_i\left(1+\frac{d}{\alpha/\beta}\right)-\ln\left(\frac{2(T-T_k)}{\alpha T_p}\right)$ | $n$ (número de fracciones), $d_i$ (dosis por fracción, **Gy**), $T$ (duración total del ciclo), $T_p$ (tiempo de duplicación de la población tumoral, **días**), $T_k$ (retardo hasta el inicio de la repoblación, **días**). Sin valores | [57] Fowler, 2010; modificaciones: [58] Victori & Buffa, 2019 | Genérico | [p. 7] |
| Radioterapia: SBRT / modelo microdosimétrico-cinético (MKM) | Sin ecuación en el documento. En [60], el MKM se acopla a un ODE compartimental (células activas, en reposo y no divisorias) | Sin valores | MKM: [59] Hawkins, 1996; combinación ODE+MKM: [60] Nakano et al., 2023 (SBRT) | El documento no declara el órgano de [60] | [p. 7] |
| Antiangiogénico: Gompertz limitado por vasculatura | Ec. (21): $f_1(N(t),U(t),X(t))=-\rho_3N_1\ln\frac{N_1}{N_2},\quad N_1(0)=N_{10}$ | $\rho_3$; sin valor | [63] Hahnfeldt et al., 1999; comparación de 6 variantes: [64] Świerniak, 2009 | Genérico en D06 | [p. 7] |
| Antiangiogénico: dinámica de la vasculatura | Ec. (22): $f_2(N(t),U(t),X(t))=k_1N_1-k_2N_2N_1^{2/3},\quad N2(0)=N_{20}$ | $k_1$ (estimulación), $k_2$ (inhibición); sin valores | [63] | Genérico | [p. 7] |
| Antiangiogénico: efecto del fármaco | Ec. (23): $g_2(N(t),U(t),X(t))=c_2N_2(t)U(t)$, con $g_1=0$ | $c_2$; sin valor | [63] | Genérico | [p. 7–8] |
| Inmunoterapia: presa–depredador (muerte tumoral) | Ec. (24): $g_1(N(t),U(t),X(t))=k_1N_1(t)N_2(t)$ | $k_1$; sin valor | No se cita una referencia específica (“simplest model”) | Genérico | [p. 8] |
| Inmunoterapia: activación de efectores | Ec. (25): $f_2(N(t),U(t),X(t))=k_2N_1(t)$ | $k_2$ | — | Genérico | [p. 8] |
| Inmunoterapia: inyección de efectores | Ec. (26): $f_2(N(t),U(t),X(t))=k_2N_1(t)+U(t)$ | — | [65] DePillis et al., 2013 (melanoma, según el título) | No pulmonar | [p. 8] |
| Inmunoterapia: pérdida de efectores | Lineal (en el texto): $g_2=p_1N_2(t)$; Ec. (27): $g_2(N(t),U(t),X(t))=p_1N_2(t)+p_2N_1(t)N_2(t)$ | $p_1,p_2$; sin valores | [66] Foryś, Waniewski, Zhivkov, 2006 | Genérico | [p. 8] |
| Inmunoterapia: interacción con tasa limitada (ratio-dependiente) | Ec. (28): $g_1(N(t),U(t),X(t))=k_1\left(\frac{N_2/N_1}{k_2+N_2/N_1}\right)N_1(t)$ | $k_1,k_2$ | [67] Woelke et al., 2010 | Genérico | [p. 8] |
| Inmunoterapia: heterogeneidad de macrófagos (M1/M2) | Sin ecuación | Sin valores | [68] Bartha & Eftimie, 2022 | **Sí, NSCLC** | [p. 8, p. 14–15] |
| Terapia dirigida + inmunoterapia (FGFR, PD-1/PD-L1) | Ec. (29): $p_1(N(t),U(t),X(t))=k_1X_1^2+k_2X_2+k_3N_1$ | $k_1..k_3$; sin valores | [69] Okuneye et al., 2021 (**cáncer de vejiga**, FGFR3, según el título) | **No pulmonar** | [p. 8] |
| Terapia dirigida (degradación del receptor) | Ec. (30): $q_1(N(t),U(t),X(t))=\frac{c_1N_2}{1+c_2X_2/N_1}$ | $c_1,c_2$ | [69] | No pulmonar | [p. 9] |
| Terapia combinada: radioquimioterapia | Ec. (31): $g_i(N(t),U(t),X(t))=k_1c(t)N(t)+k_2(\alpha d+\beta d^2)N(t)$, con $U(t)=[U_1(t)\,d]$ | $k_1,k_2,\alpha,\beta$; sin valores | [71] Geng, Paganetti, Grassberger, 2017 | **Sí, NSCLC** (según el título de [71]) | [p. 9] |
| Quimioinmunoterapia / radioinmunoterapia | Sin ecuación (suma de términos PK + quimio) | — | [72] El Haout et al., 2021; [73] Khalili & Vatankhah, 2023; [74] Friedrich et al., 2021; [75] Bekker et al., 2022 | Genérico | [p. 9] |
| Sensibilización quimio→radio / termorradiosensibilización | Sin ecuación (modificación de los parámetros LQ) | — | [76] Powathil et al., 2013; [77] De Mendoza et al., 2021 | Genérico | [p. 9] |
| Resistencia (sensibles/resistentes) | Sin ecuación numerada: factor multiplicativo $\gamma\in[0,1]$ sobre la pérdida de la población sensible (impreso “γ ∈ [01]”) | $\gamma$; sin valor | Ejemplo para resistencia a inhibidores de checkpoint en **cáncer de pulmón**: [78] Ciccolini et al., 2020 | Sí, pulmón (en [78]) | [p. 9] |
| Resistencia + antiangiogénico + quimio | Sin ecuación | — | [79] Bodzioch et al., 2021 (modelo general, “not specific for lung cancer”, [p. 15]) | No | [p. 9, p. 15] |
| Metástasis compartimental | Sin ecuación (compartimentos adicionales dentro de Ec. 1–2) | — | [81] Rhodes & Hillen, 2019 | Genérico | [p. 9] |
| PDE de reacción–difusión–quimiotaxis (células) | Ec. (32): $\frac{\partial N}{\partial t}=f(N)-\nabla\cdot(N\chi(X)\nabla X)+\nabla\cdot D\nabla N$ | $D$, $\chi(\cdot)$; sin valores | [82] Murray, 2003 | Genérico | [p. 10] |
| PDE (atrayente) | Ec. (33): $\frac{\partial X}{\partial t}=p(X,N)+\nabla\cdot D_X\nabla X$ | $D_X$; sin valor | [82] | Genérico | [p. 10] |
| PDE estructurada por fenotipo de resistencia | Ec. (34): $\frac{\partial N}{\partial t}=f(N(t),U(t),X(t))-g(N(t),U(t),X(t))$, con $x\in[0,1]$ | — | [83] Pouchol et al., 2018 | Genérico | [p. 10] |
| PDE de resistencia: pérdida | Ec. (35): $g=d(x,U(t))\rho(t)N(t,x)$ | $d(\cdot)$: forma no especificada | [83] | Genérico | [p. 10] |
| PDE de resistencia: población total | Ec. (36): $\rho(t)=\int_0^1 N(t,x)\,dx$ | — | [83] | Genérico | [p. 10] |
| Distribución de tamaños de metástasis (Iwata) | Ec. (37): $\frac{\partial\rho(x,t)}{\partial t}+\frac{\partial g(x)\rho(x,t)}{\partial x}=0$ | $g(x)$ gompertziana en [84] | [84] Iwata, Kawasaki, Shigesada, 2000 | Genérico | [p. 10] |
| Iwata: condición inicial | Ec. (38): $\rho(0,x)=0$ | — | [84] | Genérico | [p. 10] |
| Iwata: condición de frontera | Ec. (39): $g(1)\rho(1,t)=\int_1^\infty\beta(x)\rho(x,t)\,dx+\beta(x_p(t))$ | — | [84] | Genérico | [p. 10] |
| Iwata: tasa de emisión de metástasis | Ec. (40): $\beta(x)=mx^{\alpha}$ | $m,\alpha$; sin valores | [84] | Genérico | [p. 10] |
| ABM / híbrido / multiescala | Sin ecuaciones. Descripción conceptual: rejilla 2D de agentes más una rejilla suplementaria de concentraciones (Figura 1), reglas probabilísticas y necesidad de múltiples corridas | — | [85] Ford Versypt, 2021; “discrete dynamic network models” [86]; aplicaciones: quimio [87], radio [88], antiangiogénico [89], inmuno [90, 91] | Genérico; [122] Pennisi et al., 2010 (ABM de metástasis pulmonares vs. sistema inmune) | [p. 11–12, p. 15] |
| Pacientes virtuales / población | Sin ecuación (mismo modelo con distintos parámetros; evaluación por curvas de Kaplan–Meier) | — | [92] Agur et al., 2020; [93] Świerniak et al., 2020 | Genérico | [p. 12] |
| Señalización intracelular (ODE) | Forma de la Ec. (2) [p. 13]; sin ecuaciones específicas | — | Métodos: [94] Kardynska et al., 2023; lógica difusa [95]; redes de Petri [96]; otros [97] | Genérico | [p. 13] |
| Red p53 | Sin ecuación | — | [103] Charan et al., 2023; [104] Konrath et al., 2023 | Genérico | [p. 14] |
| JAK/STAT | Sin ecuación | — | [99] Kalliara et al., 2022; [105] Lee et al., 2021 | Genérico | [p. 14] |
| NF-κB | Sin ecuación | — | [98] Paszek et al., 2020; [106] Cheemanapalli et al., 2023 | Genérico | [p. 14] |
| Daño/reparación del ADN (ATM–PTEN–p53) | Sin ecuación (redes de Petri + ODE) | — | [96] Gutowska et al., 2022 | Genérico | [p. 14] |
| NRF2 | Sin ecuación | — | [107] Liu, Pi, Zhang, 2022 | Genérico | [p. 14] |
| Wnt | Sin ecuación | — | [108] Hochman et al., 2017 | Genérico | [p. 14] |
| Ciclo celular | Sin ecuación | — | [109] Tyson & Novák, 2022 | Genérico | [p. 14] |
| EGFR (modelo dinámico) | — | — | **No reportado como modelo matemático**; EGFR solo se menciona como actor molecular o diana (TKI) [43, 44, 48] [p. 3] | — | [p. 3] |
| Booleano | — | — | **No reportado** (solo “discrete dynamic network models” [86], lógica difusa [95] y redes de Petri [96]) | — | [p. 11, p. 13] |
| Fractal | — | — | **No reportado** | — | — |
| Estocástico | Sin ecuación; la estocasticidad se atribuye a las reglas probabilísticas de los ABM | — | [85] | Genérico | [p. 10–11] |
| Modelos específicos de pulmón citados en la Discusión (sin ecuaciones) | — | — | SCLC [110] (= D07); NSCLC [68]; carcinoma de Lewis en ratón inmunocompetente [111] Curtis & Frieboes, 2019; metronómica en pulmón [113] Bondarenko et al., 2021; efectos adversos en NSCLC [114] Siewe & Friedman, 2022; fraccionamiento RT en NSCLC [115] Dionysiou & Stamatakos, 2006; vinorelbina metronómica en NSCLC [117] Barbolosi et al., 2014, y ensayo de fase I [118] Barlesi et al., 2022; ensayos in silico de inmunoterapia [119] Creemers et al., 2023; PD-1 neoadyuvante en NSCLC [120] Jafarnejad et al., 2019; metástasis inmunomediada [121] Rhodes & Hillen, 2020; carga metastásica en NSCLC con inmunoterapia [123] Schlicke et al., 2021 | Sí | [p. 14–15] |

## 5. Valores numéricos de parámetros biológicos para cáncer de pulmón

**El documento no reporta ningún valor numérico de parámetros biológicos** (ni tiempos de duplicación, tasas de crecimiento, α, β, α/β, Tk, Tp, constantes PK/PD, ni constantes inmunes). Solo define las unidades de algunos símbolos: $d_i$ en Gy, $T_p$ en días y $T_k$ en días [p. 7].

Para obtener parámetros pulmón-específicos habría que consultar las fuentes primarias que el propio documento cita como modelos de pulmón (ver §8).

## 6. Datos clínicos o experimentales mencionados

| Dato | Cifra exacta | Fuente citada | Página |
|---|---|---|---|
| Casos anuales de cáncer de pulmón proyectados | 3,8 millones en 2050 | [2] Sharma, 2022 | [p. 1] |
| Supervivencia relativa a 3 años | “increased to 31%” | [3] Siegel et al., 2022 | [p. 1] |
| Literatura sobre inmunoterapia en pulmón | “over 2300 articles published in the last year alone” (PubMed) | Consulta del autor; no se dan fecha ni cadena | [p. 2–3] |
| SBRT | Estándar de cuidado para NSCLC precoz inoperable u oligometastásico | [25], [26] | [p. 2] |
| Horizonte de simulación (modelos poblacionales) | Meses (crecimiento/efecto directo) a años, “usually 2 or 5”, para curvas de supervivencia | Sin referencia | [p. 14] |
| Duración de experimentos para señalización | “between 1 and 12 h”; una fracción menor a 24 o 48 h | Sin referencia | [p. 14] |
| Datos de imagen disponibles | “usually … for two time points (before and after treatment)” | Sin referencia | [p. 12] |
| Fraccionamiento en NSCLC (in silico) | CHART con irradiación de fin de semana vs. HART-weekend: “almost the same long term-effects on locoregional NSCLC tumor control” | [115] | [p. 14] |
| Vinorelbina metronómica (NSCLC) | Protocolo contraintuitivo propuesto por modelado y confirmado por un ensayo clínico (“better efficacy”); no se dan cifras | [117], [118] | [p. 15] |
| Dosis < MTD en NSCLC | “longer survival times and a lower level of drug resistance”; sin cifras y **sin referencia explícita en la frase** | (¿[113]? no indicado) | [p. 15] |

## 7. Vacíos y desafíos declarados por el autor

- Pocos modelos son específicos de pulmón: “relatively few of them are focused specifically on lung cancer” [p. 14].
- Incluso los modelos ajustados a datos de pulmón “do not take into account phenomena that are specific for lung cancer only” [p. 14].
- “comprehensive modeling studies comparing the effects of different radiotherapy options hardly exist” [p. 2].
- El LQ no funciona bien a dosis altas (SBRT) [p. 7].
- Calibración: “Tuning parameters … constitutes a very difficult and delicate task due to lack of adequate, dense measurement data” [p. 12].
- Los modelos ODE no capturan la heterogeneidad [p. 9]; los PDE no capturan la estocasticidad [p. 10]; los ABM carecen de métodos analíticos y tienen un alto coste computacional [p. 12].
- Los modelos intracelulares “have hardly been used to build multiscale models” y se basan en líneas celulares in vitro sin contexto tisular [p. 14]; está abierta la pregunta de su transferibilidad a pulmón (p53, NF-κB, Wnt, NRF2) [p. 15].
- Pocos trabajos sobre efectos adversos [p. 15].
- Desafíos listados [p. 15]: (i) ajustar modelos a datos de inmunoterapia en pulmón [15, 125]; (ii) convertir modelos estructurales (grafos) de metástasis o redes regulatorias en modelos dinámicos; (iii) vincular los modelos de sinergia de fármacos con los de crecimiento; (iv) desarrollar modelos multiescala específicos de pulmón con metástasis/resistencia.
- Expectativa: “only gradual progress”, con impacto clínico procedente sobre todo de los modelos poblacionales [p. 16].

## 8. Evaluación del lector *(interpretación propia, no del documento)*

- **[Lector] Profundidad:** es una revisión **didáctica y metodológica**. Unifica la notación (Ec. 1–2) y muestra formas canónicas, pero no compara cuantitativamente los modelos, no tabula parámetros ni evalúa el ajuste o la validación. La parte intracelular (sección 4) es solo un listado de referencias sin ecuaciones [p. 13–14].
- **[Lector] Sesgo de selección:** no hay método de búsqueda, así que la selección es discrecional. Hay una proporción apreciable de autocitas o citas del grupo del autor ([51], [93], [94], [96], [98], [99], [101]). Varias ecuaciones ilustrativas provienen de modelos **no pulmonares** (páncreas [53], vejiga [69], melanoma [65]), lo que el autor señala parcialmente (“original notation is changed”, [p. 8]).
- **[Lector] Utilidad como fuente de parámetros:** **nula como fuente primaria**: no contiene valores. Sirve como **mapa de referencias primarias**. Para cada tipo de parámetro habría que consultar:
  - α, β, α/β, Tp y Tk en NSCLC con radioquimioterapia → [71] Geng et al., 2017 (Sci Rep 7:13542); fórmula BED → [57] Fowler, 2010; parámetros SBRT/MKM → [60] Nakano et al., 2023, y [59] Hawkins, 1996.
  - Parámetros de crecimiento y fraccionamiento en NSCLC → [115] Dionysiou & Stamatakos, 2006.
  - PK/PD de vinorelbina metronómica → [117] Barbolosi et al., 2014, y [118] Barlesi et al., 2022.
  - Resistencia clonal con metronómica en NSCLC → [113] Bondarenko et al., 2021.
  - Inmunidad (macrófagos M1/M2) en NSCLC → [68] Bartha & Eftimie, 2022; PD-1 neoadyuvante (QSP) → [120] Jafarnejad et al., 2019; carga metastásica con inmunoterapia → [123] Schlicke et al., 2021; metástasis vs. sistema inmune (ABM) → [122] Pennisi et al., 2010.
  - Quimio + inmuno en carcinoma de Lewis → [111] Curtis & Frieboes, 2019.
  - Angiogénesis (Ec. 21–23) → [63] Hahnfeldt et al., 1999 (el documento no dice en qué tumor se calibró).
  - Toxicidad / esteroides con anti-CTLA-4 → [114] Siewe & Friedman, 2022.
- **[Lector] Calidad formal:** hay erratas en las ecuaciones (Ec. 6, 17 y 20; ver §10) que impiden reproducir los modelos copiando literalmente sin contrastarlos con la fuente original.

## 9. Oportunidades de simulación reproducible (solo con lo contenido en el documento)

Todas requieren **parámetros externos**, porque D06 no aporta valores. Se listan las estructuras que pueden implementarse directamente:

1. **Comparar crecimiento exponencial, logístico y Gompertz** (Ec. 4–6) [p. 5], con escenarios de cirugía como salto $N\to\mu N$ con $\mu$ aleatorio [p. 5]. Requiere corregir el Gompertz (usar $K$ en lugar de $N_0$; ver §10).
2. **Quimioterapia log-kill con PK de un compartimento** (Ec. 12–14) [p. 6]: comparar dosis MTD frente a metronómica (motivado por [117, 118], [p. 15]).
3. **Combinación de dos fármacos con PD de tránsito y parámetro de sinergia Ψ** (Ec. 15–18) [p. 6]: barrido Ψ<1, =1 y >1, corrigiendo la Ec. 17 a $(S_{1}-S_{2})$.
4. **Radioterapia LQ con BED** (Ec. 19–20) [p. 7] y **radioquimioterapia aditiva** (Ec. 31) [p. 9]: comparar esquemas de fraccionamiento (convencional vs. hiperfraccionado con o sin fin de semana, motivado por [115], [p. 14]); usar la forma estándar del término de repoblación (ver §10).
5. **Hahnfeldt antiangiogénico** (Ec. 21–23) [p. 7–8]: respuesta a $U(t)$ continuo vs. pulsado.
6. **Tumor–inmune presa-depredador** (Ec. 24–28) [p. 8]: comparar la interacción bilineal frente a la ratio-dependiente y añadir la inyección de efectores $U(t)$ (Ec. 26).
7. **Resistencia binaria con factor γ** [p. 9] y **resistencia continua estructurada por fenotipo** (Ec. 34–36) [p. 10].
8. **Distribución de tamaños de metástasis de Iwata** (Ec. 37–40) [p. 10]: resolver por método de características, con $g(x)$ Gompertz.
9. **Cohorte de pacientes virtuales** (parámetros muestreados) con curvas de Kaplan–Meier como salida [p. 12].

## 10. Problemas de extracción y de contenido

- **Texto extraído:** las ecuaciones 5, 6, 8, 11, 16–18, 20–22 y 29–30 salen fragmentadas (fracciones y paréntesis perdidos). Se **verificaron visualmente en el PDF** (páginas 5–10, renderizadas con PyMuPDF); las transcripciones de la tabla §4 siguen el PDF.
- **Erratas del documento original** (observación del lector, verificable dentro del propio documento):
  - **Ec. (6)** Gompertz: $-\rho_3N\ln(N/N_0)$ con $N(0)=N_0$ da $f=0$ en $t=0$; como está impresa, la solución sería constante ($N\equiv N_0$). Lo esperable es un denominador de capacidad de carga ($K$); la Ec. (21) sí usa $N_2$ como límite.
  - **Ec. (17)**: $(S_{1\_i}-S_{1\_i})$ es idénticamente 0; por la estructura de cadena de tránsito de las Ec. 16 y 18 debería ser $(S_{1\_i}-S_{2\_i})$.
  - **Ec. (20)** BED: dentro del paréntesis aparece $d$ en lugar de $d_i$, y el término de repoblación se imprime como $\ln\left(\frac{2(T-T_k)}{\alpha T_p}\right)$. La forma habitual de Fowler es $\frac{\ln 2\,(T-T_k)}{\alpha T_p}$ [conocimiento del lector; verificar en ref. 57].
  - **Ψ** [p. 6]: “Ψ ≤ 1 sinergia … Ψ ≥ 1 antagonismo” se solapan en Ψ=1 (deberían ser desigualdades estrictas).
  - **[p. 8]** “X − 1(t)” es una errata por $X_1(t)$; **[p. 9]** “γ ∈ [01]” por $[0,1]$; **[p. 7]** “N2(0)” por $N_2(0)$.
  - **[p. 6]** Se describe la relación dosis–regresión como “linear logarithmic” (Skipper).
- **Atribuciones que conviene verificar:** [ref 86] (England et al., 2023, “discrete event simulation” de rutas diagnósticas) se cita como ejemplo de “discrete dynamic network models” para ABM [p. 11]; parece una cita desplazada. [ref 115] tiene un título referido a “fast growing solid tumors”, pero el texto la presenta como un estudio de NSCLC [p. 14]. La afirmación sobre dosis < MTD en NSCLC [p. 15] no lleva referencia.
- La Figura 1 [p. 12] es conceptual (ABM) y no contiene datos.

## 11. Citas textuales clave

1. “relatively few of them are focused specifically on lung cancer” [p. 14].
2. “even models whose parameters were fitted to clinical data of lung cancer patients do not take into account phenomena that are specific for lung cancer only” [p. 14].
3. “Tuning parameters for these models constitutes a very difficult and delicate task due to lack of adequate, dense measurement data” [p. 12].
4. “Bioimaging data are usually available (if they are available at all) for two time points (before and after treatment)” [p. 12].
5. “Sadly, comprehensive modeling studies comparing the effects of different radiotherapy options hardly exist” [p. 2].
6. “The LQ model does not work well with high radiation doses, characteristic for stereotactic body radiation therapy” [p. 7].
7. “Chemotherapy effects are most often modeled following Skipper’s laws [52], stating that the relationship between dose and tumor regression is linear logarithmic” [p. 6].
8. “these models have hardly been used to build multiscale models and thus facilitate the development of new treatment protocols” [p. 14].
9. “It is one of a few cases, when modeling was actually followed by a clinical trial that tested its applicability” [p. 15].
10. “in the near future, one should expect only gradual progress and the impact on clinical practice coming mostly from population-level modeling” [p. 16].
