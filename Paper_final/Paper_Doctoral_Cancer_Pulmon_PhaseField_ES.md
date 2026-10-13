# Auditoría de reproducibilidad computacional de un modelo de campo de fase publicado para el cáncer de pulmón de células no pequeñas bajo inmunoterapia anti-PD-1 (Wagner et al., 2023): verificación farmacocinética, reescalado del índice de sensibilidad y un defecto de configuración

**Autor:** Wuilson Estacio

> **Estado del manuscrito (interno).** Versión en español del borrador de trabajo v0.3 (13 de octubre de 2026, con los resultados de T06 y los documentos complementarios integrados). El original es `Paper_Doctoral_Cancer_Pulmon_PhaseField.md`, en inglés; si hay diferencias, prevalece el original. Todos los resultados numéricos proceden de ejecuciones registradas en `Resultados/` y se pueden rastrear mediante la tabla del Suplemento S4. Las afirmaciones marcadas **[PENDIENTE]** dependen de análisis aún no realizados. Estado y brechas: `Paper_final/Estado_Paper_Doctoral_brechas.md`. El modelo auditado, sus ecuaciones, los valores de sus parámetros, los datos de los pacientes y el código son obra de Wagner et al. [2023]; este manuscrito solo aporta la auditoría. No se ha verificado la novedad (aún no se ha leído completo Scibilia et al. [2024]), y reutilizar los datos de los pacientes en una publicación requiere la confirmación de los autores originales (§7.3).
>
> **Documentos complementarios.** La evidencia de este borrador está documentada en [METODOLOGIA_SIMULACIONES_Y_COLABORACION_IA.md](METODOLOGIA_SIMULACIONES_Y_COLABORACION_IA.md) (simulaciones, entorno, comandos y reparto del trabajo entre la persona investigadora y los agentes de IA), [INFORME_INTEGRADO_F0_F1.md](INFORME_INTEGRADO_F0_F1.md) (resultados verificados y trazabilidad) y [Primera_entrega_contribuciones_y_plan.md](Primera_entrega_contribuciones_y_plan.md) (hipótesis y tolerancias fijadas antes de ejecutar). En el §7.6 se indica qué respalda cada uno.

## Tabla de contenido

- [Resumen](#resumen)
- [1. Introducción](#1-introduccion)
  - [1.1 Contexto clínico](#11-contexto-clinico)
  - [1.2 Modelos de campo de fase del crecimiento tumoral](#12-modelos-de-campo-de-fase-del-crecimiento-tumoral)
  - [1.3 El modelo auditado y por qué importa la reproducibilidad](#13-el-modelo-auditado-y-por-que-importa-la-reproducibilidad)
  - [1.4 Objetivos y contribución](#14-objetivos-y-contribucion)
- [2. Marco matemático y farmacocinético](#2-marco-matematico-y-farmacocinetico)
  - [2.1 Ecuaciones de campo de fase](#21-ecuaciones-de-campo-de-fase)
  - [2.2 Acoplamiento farmacocinético](#22-acoplamiento-farmacocinetico)
  - [2.3 Índices de sensibilidad local y el factor α/100](#23-indices-de-sensibilidad-local-y-el-factor-100)
  - [2.4 El defecto de configuración H01](#24-el-defecto-de-configuracion-h01)
- [3. Implementación computacional y auditoría de reproducibilidad](#3-implementacion-computacional-y-auditoria-de-reproducibilidad)
  - [3.1 Entorno de ejecución en contenedor](#31-entorno-de-ejecucion-en-contenedor)
  - [3.2 Criterios de reproducción preespecificados](#32-criterios-de-reproduccion-preespecificados)
  - [3.3 Protocolo de verificación](#33-protocolo-de-verificacion)
  - [3.4 Correspondencia artículo–código](#34-correspondencia-articulocodigo)
- [4. Resultados y discusión comparativa](#4-resultados-y-discusion-comparativa)
  - [4.1 Farmacocinética](#41-farmacocinetica)
  - [4.2 Tabla 2: índices publicados, brutos y reescalados](#42-tabla-2-indices-publicados-brutos-y-reescalados)
  - [4.3 Efecto de corregir H01 sobre la sensibilidad del paciente 2](#43-efecto-de-corregir-h01-sobre-la-sensibilidad-del-paciente-2)
  - [4.4 Discusión](#44-discusion)
- [5. Pipeline propuesto para la terapia personalizada](#5-pipeline-propuesto-para-la-terapia-personalizada)
- [6. Conclusiones y trabajo futuro](#6-conclusiones-y-trabajo-futuro)
- [7. Declaraciones](#7-declaraciones)
  - [7.1 Disponibilidad de datos y código](#71-disponibilidad-de-datos-y-codigo)
  - [7.2 Ética](#72-etica)
  - [7.3 Licencias y permisos (bloqueante para publicar)](#73-licencias-y-permisos-bloqueante-para-publicar)
  - [7.4 Uso de herramientas de IA](#74-uso-de-herramientas-de-ia)
  - [7.5 Contribuciones de los autores y financiación](#75-contribuciones-de-los-autores-y-financiacion)
  - [7.6 Documentos complementarios y mapa de la evidencia](#76-documentos-complementarios-y-mapa-de-la-evidencia)
  - [7.7 Reutilización de material de terceros y atribución](#77-reutilizacion-de-material-de-terceros-y-atribucion)
- [Referencias](#referencias)
- [Material suplementario](#material-suplementario)
  - [S5. Reproducción paso a paso en otro equipo](#s5-reproduccion-paso-a-paso-en-otro-equipo)

---

## Resumen

**Antecedentes.** Los modelos de campo de fase específicos de cada paciente para el crecimiento tumoral bajo inmunoterapia se proponen cada vez más como base para optimizar el tratamiento del cáncer de pulmón de células no pequeñas (CPCNP). Su valor depende de que los resultados publicados puedan regenerarse a partir del código y los datos liberados. Auditamos la reproducibilidad computacional de un modelo publicado de tipo Cahn–Hilliard para el CPCNP bajo tratamiento anti-PD-1 (Wagner et al., *Math. Biosci. Eng.* 2023). El modelo acopla fases tumorales proliferativa y necrótica, un campo estacionario de nutrientes y un modelo farmacocinético (PK) monocompartimental del anticuerpo.

**Métodos.**
- El código de los autores, sin modificar (FEniCS/dolfin 2019.1.0), se ejecutó en un contenedor Docker con versiones bloqueadas.
- Se aplicaron tolerancias preespecificadas a:
  - (i) el modelo PK, frente a su solución analítica;
  - (ii) los 88 índices de sensibilidad local de la Tabla 2 publicada (11 parámetros × 4 cantidades de interés × 2 pacientes);
  - (iii) una correspondencia de 35 elementos entre el artículo y el código.
- Un revisor independiente (un segundo agente de IA, con su propio código) auditó el análisis.
- Ese revisor encontró un defecto en el script de sensibilidad: las simulaciones perturbadas del paciente 2 vuelven a los parámetros PK por defecto (H01). Se corrigió en una variante declarada y se cuantificó su efecto.

**Resultados.**
- **PK:** la EDO y la dosis total administrada se reprodujeron exactamente. La tolerancia preespecificada del 0,1 % en picos y valles se cumplió en 3 de 6 extremos, por un desfase de medio subpaso en la ventana de infusión.
- **Tabla 2, salida del script:** se reprodujeron 0 de 88 índices publicados (error relativo mediano ≈ 2,3 × 10⁴ %), así que se rechazó la hipótesis de reproducción preespecificada.
- **Tabla 2, reescalada (diagnóstico):** el script devuelve $\partial_\alpha\bar Q/\bar Q$. Al multiplicar por $\alpha/100$, el factor que implica la definición verbal de la ec. 4.1 del artículo, se recuperaron los 88 valores impresos a tres cifras significativas y los 88 rangos (error relativo máximo 0,449 %). De siete transformaciones candidatas, solo esta lo consiguió. La concordancia respalda, pero no demuestra, cómo se generó la tabla publicada.
- **H01:** las simulaciones perturbadas del paciente 2 usaron los parámetros del fármaco del paciente 1. Al re-simular P2 con sus propios parámetros PK, sus 44 índices cambiaron una mediana del 12,6 % (máximo 45,2 %), sin cambios de signo. Se reordenaron 7 de los 11 rangos del volumen visible, un efecto «relevante» según los umbrales preespecificados. Un control de determinismo reprodujo la salida original bit a bit, de modo que el cambio se debe solo a la corrección. Los valores corregidos de P2 coinciden con la tabla publicada en solo 1 de 44 casos, lo que es coherente con que los valores publicados contengan el defecto.
- **Correspondencia artículo–código:** nueve discrepancias adicionales, entre ellas un factor 0,7 no declarado en el término de muerte por fármaco y desfases de 26 a 157 días en los calendarios de tratamiento.

**Conclusiones.**
- El análisis de sensibilidad publicado solo puede regenerarse tras un paso de posprocesado que el script liberado no contiene.
- Para uno de sus dos pacientes, los índices publicados arrastran un defecto de configuración que los desplaza hasta un 45 % y reordena el ranking de parámetros del volumen visible.
- Por estos hallazgos, y con solo n = 2 pacientes calibrados a mano, los parámetros del modelo aún no pueden respaldar una optimización de dosis. El siguiente paso necesario es calibrar la PK y los parámetros tumorales con análisis de identificabilidad.
- Proponemos un pipeline por etapas que conecta los datos de imagen con la calibración por verosimilitud y la validación fuera del periodo de ajuste, antes de cualquier uso terapéutico.

**Palabras clave:** cáncer de pulmón de células no pequeñas; modelo de campo de fase; Cahn–Hilliard; inmunoterapia; farmacocinética; reproducibilidad computacional; análisis de sensibilidad; Docker.

---

## 1. Introducción

### 1.1 Contexto clínico

- **Carga de enfermedad.** El cáncer de pulmón es la primera causa de muerte por cáncer en el mundo. En torno al 85 % de los casos son CPCNP, con una supervivencia a cinco años de aproximadamente el 22 % [Bray 2018, citado en Wagner 2023, ref. 19].
- **Tratamiento.** El CPCNP se trata con cirugía, quimioterapia, radioterapia y, cada vez más, inmunoterapia [Zappa & Mousa 2016].
- **Inhibidores de puntos de control inmunitario.** Los anticuerpos monoclonales anti-PD-1 (nivolumab, pembrolizumab) restauran la actividad efectora de los linfocitos T que las células tumorales suprimen mediante la expresión de PD-L1/PD-L2 [Wagner 2023, §1].
- **Heterogeneidad de la respuesta.** La respuesta a estos fármacos varía mucho entre pacientes. Predecir la trayectoria tumoral de un paciente concreto bajo un calendario concreto sigue siendo un problema abierto [Wagner 2023, §1; Rockne & Scott 2019].
- **Evidencia poblacional.** Los ensayos de cribado documentan la magnitud de la enfermedad a escala poblacional: el cribado con TC de baja dosis redujo la mortalidad por cáncer de pulmón un 20,0 % frente a la radiografía de tórax en el NLST [NLST 2011] y un 24 % frente a la ausencia de cribado en los hombres de NELSON a 10 años [de Koning 2020]. Esta evidencia no informa directamente sobre la dinámica individual bajo tratamiento, que es la escala que se aborda aquí.

### 1.2 Modelos de campo de fase del crecimiento tumoral

- **Representación de interfaz difusa.** Los modelos de campo de fase (de interfaz difusa) representan los componentes del tejido como fracciones de volumen $\phi(\mathbf x,t)\in[0,1]$ que cambian a lo largo de interfaces de anchura finita $\varepsilon$.
  - **Ecuación de Cahn–Hilliard** [Cahn & Hilliard 1958]: flujo de gradiente conservativo en $H^{-1}$ de una energía libre de Ginzburg–Landau [Ginzburg & Landau 1950] $\int\Psi(\phi)+\tfrac{\varepsilon^2}{2}|\nabla\phi|^2$. Modela la separación de fases y la adhesión celular con conservación de masa; los términos de reacción añaden crecimiento y muerte.
  - **Ecuación de Allen–Cahn** [Allen & Cahn 1979]: su equivalente no conservativo en $L^2$. Se usa cuando la variable de fase no es una cantidad conservada.
- **Modelado tumoral.** Los sistemas de Cahn–Hilliard multiespecie acoplados al transporte de nutrientes y fármacos son una familia consolidada [Cristini & Lowengrub 2010; Lowengrub et al. 2009]. Los modelos de dos especies con acoplamiento de nutrientes se han analizado y verificado [Garcke et al. 2016; Frigeri et al. 2015; Lee et al. 2015], ampliado a diez especies [Lima et al. 2014] y acoplado a redes vasculares 1D [Fritz et al. 2021].
- **Tratamiento numérico.** Suele basarse en la separación convexo–cóncava, que garantiza estabilidad energética incondicional [Eyre 1998], y en elementos finitos [Logg et al. 2012].

### 1.3 El modelo auditado y por qué importa la reproducibilidad

Wagner et al. [2023] propusieron un modelo de este tipo y lo calibraron con volumetría longitudinal por TC de pacientes con CPCNP bajo tratamiento anti-PD-1. El modelo, sus ecuaciones, los valores de sus parámetros, los datos de los pacientes y el código son obra suya [Wagner 2023; Wagner 2023, preprint; Wagner 2023, code repository]; este paper los audita y no propone un modelo nuevo.
- **Datos:** dos pacientes (P1: nivolumab Q2W; P2: pembrolizumab Q3W→Q6W), publicados junto con el código.
- **Parámetros:** cuatro parámetros específicos de cada paciente se ajustaron a mano ($\lambda_P^{pro}$, $\lambda_\tau^{eff}$, $\lambda$, $\lambda_{PN}$).
- **Análisis:** se publicó un análisis de sensibilidad local (su Tabla 2) para jerarquizar la influencia de los parámetros. Los propios autores señalan la estimación de parámetros y la identificabilidad como problemas abiertos [Wagner 2023].

Estos modelos son candidatos para explorar dosis in silico. Por eso, cualquier uso posterior (calibración, identificabilidad, optimización de dosis) exige primero comprobar que los números publicados pueden regenerarse a partir de los materiales liberados.

### 1.4 Objetivos y contribución

**Objetivos:**
- **O1.** Ejecutar el código liberado, sin modificar, en un entorno bloqueado, y contrastar criterios de reproducción preespecificados para el modelo PK y para los 88 índices de sensibilidad.
- **O2.** Explicar cualquier discrepancia de forma diagnóstica, sin alterar la clasificación preespecificada.
- **O3.** Someter el análisis a una revisión independiente y cuantificar el efecto de cualquier defecto encontrado.
- **O4.** A partir de ello, definir qué hace falta para que el modelo pueda respaldar una calibración farmacocinética y una optimización terapéutica.

**Contribuciones:**
- Una reproducción del modelo publicado en contenedor y con registro completo.
- La identificación de la transformación exacta que conecta el script liberado con la Tabla 2 publicada.
- El hallazgo y la cuantificación de un defecto de configuración (H01) en el análisis de sensibilidad publicado.
- Una hoja de ruta por etapas hacia un uso calibrado y validado.

---

## 2. Marco matemático y farmacocinético

Las ecuaciones (1)–(4), los valores de parámetros de la Tabla 1 y la notación se reproducen del artículo publicado [Wagner 2023, §2 y Tabla 1], distribuido con licencia Creative Commons Atribución 4.0 (CC BY 4.0). La ecuación (5) reproduce su definición de sensibilidad (su ec. 4.1); las ecs. (6)–(8) describen nuestra lectura de su código liberado [Wagner 2023, code repository]. Las diferencias del código liberado se recogen en §3.4.

### 2.1 Ecuaciones de campo de fase

**Especies y dominio.** Sea $\Omega$ un dominio de tejido pulmonar que contiene:
- las fracciones de volumen tumoral proliferativa ($\phi_P$) y necrótica ($\phi_N$), con tumor total $\phi_T=\phi_P+\phi_N$ y tejido sano $\phi_H=1-\phi_T$;
- las concentraciones de nutrientes vascular ($\phi_{\sigma,v}$) e intersticial ($\phi_{\sigma,i}$);
- un agente inmunoterapéutico ($\phi_\tau$).

**Fase proliferativa.** Evoluciona según un sistema de Cahn–Hilliard generalizado:

$$
\partial_t\phi_P=\nabla\cdot\big(c_m\,m_P(\phi_P,\phi_T)\nabla\mu_P\big)+S_P(\phi_P,\phi_{\sigma,i},\phi_\tau),\qquad
\mu_P=\partial_{\phi_P}\Psi(\phi_P,\phi_T)-\varepsilon_P^2\Delta\phi_P-\chi\,\phi_{\sigma,i},
\tag{1}
$$

con condiciones de Neumann homogéneas para $\phi_P$ y $\mu_P$, y:
- el potencial de doble pozo $\Psi=\tilde\Psi(\phi_P)+\tilde\Psi(\phi_T)$, con $\tilde\Psi(\phi)=c_\Psi\phi^2(1-\phi)^2$;
- la movilidad degenerada $m_P=(\phi_P^+)^2(1-\phi_T^+)^2$, donde $(\cdot)^+$ es un truncamiento a $[0,1]$.

**Término de reacción:**

$$
S_P=\lambda_P^{pro}\,\phi_{\sigma,i}\,(\phi_P^+)^{\lambda}\ln\!\frac{1+\epsilon_g}{\phi_P^++\epsilon_g}
\;-\;\frac{\lambda_\tau^{eff}}{\omega}\,\phi_P\,\frac{\phi_\tau}{\phi_\tau+\phi_\tau^{50}}
\;-\;\lambda_{PN}\,H(\sigma_{PN}-\phi_{\sigma,i})\,\phi_P ,
\tag{2}
$$

Sus tres términos son:
- crecimiento gompertziano [Gompertz 1825] dependiente de nutrientes, en el que $\lambda\ge1$ penaliza el crecimiento a concentraciones bajas;
- un término de muerte de tipo Emax (Hill–Langmuir) inducido por el fármaco [Hill 1910];
- la conversión hipóxica a necrosis por debajo del umbral de nutrientes $\sigma_{PN}$.

**Fase necrótica:** $\partial_t\phi_N=\lambda_{PN}H(\sigma_{PN}-\phi_{\sigma,i})\phi_P$.

**Nutrientes:** reacción–difusión cuasiestacionaria. En el modelo reducido, la ecuación intersticial es

$$
-\kappa_i\,\nabla^2\phi_{\sigma,i}=\eta_{vi}\phi_{\sigma,v}-\eta_{iv}\phi_{\sigma,i}-\alpha_H(1-\phi_P-\phi_N)\phi_{\sigma,i}-\alpha_P\phi_P\phi_{\sigma,i}.
\tag{3}
$$

**Modelo 1D reducido** (el usado en todo este trabajo). La simetría esférica da las versiones radiales de (1)–(3), con la medida $4\pi r^2dr$ en la forma débil. Configuración:
- radio de 4 cm;
- elementos finitos lineales a trozos [Logg et al. 2012; Logg & Wells 2010];
- paso de tiempo de 1/24 d, con 32 subpasos PK;
- integración temporal semiimplícita con separación convexo–cóncava [Eyre 1998].

**Observable.** El volumen tumoral visible es $V_{vis}(t)=\int_\Omega\mathbf 1\{\phi_T>0{,}3\}\,d\mathbf x$, que se compara con la volumetría por TC.

### 2.2 Acoplamiento farmacocinético

La cantidad de anticuerpo en el pulmón sigue un modelo lineal monocompartimental con eliminación de primer orden e infusión de orden cero:

$$
\partial_t\phi_\tau=-\frac{\ln 2}{t_{1/2}}\,\phi_\tau+\frac{N_A}{M_\tau}\,d_\tau\,\mathbf 1_{t\in I_\tau},
\tag{4}
$$

Sus términos:
- $t_{1/2}$ es la semivida sérica;
- $M_\tau$ es la masa molar;
- $d_\tau$ es la dosis por administración;
- $N_A$ es el número de Avogadro;
- $I_\tau$ es la unión de las ventanas de infusión de 1 h que fija el calendario de cada paciente:
  - P1: cada 14 d desde $t_S$;
  - P2: cada 21 d y, desde $t_{Q6W}$ hasta $t_{PD}$, cada 42 d.

La acción del fármaco entra en (2) a través de $\phi_\tau/(\phi_\tau+\phi_\tau^{50})$, escalada por el cociente de pesos pulmón/cuerpo $1/\omega$.

**Tabla 1. Parámetros farmacocinéticos y específicos de cada paciente (modelo 1D, valores publicados).** Reproducida de Wagner et al. [2023], Tabla 1 (CC BY 4.0).

| Símbolo | Significado | P1 | P2 |
|---|---|---|---|
| $d_\tau$ | dosis por administración (g) | 0,24 | 0,20 |
| $M_\tau$ | masa molar (g/mol) | 146 000 | 143 600 |
| $t_{1/2}$ | semivida sérica (d) | 26,7 | 22,0 |
| $\phi_\tau^{50}$ | cantidad de fármaco para el efecto semimáximo (moléculas) | 1,012 × 10¹⁶ | 1,012 × 10¹⁶ |
| $\omega$ | cociente de pesos cuerpo/pulmón | 80 | 80 |
| $\lambda_P^{pro}$ (1/d) | tasa de proliferación | 0,36 | 0,0038 |
| $\lambda_\tau^{eff}$ (1/d) | efecto inmunoterapéutico | 5,2 | 0,54 |
| $\lambda$ | exponente de la ley de crecimiento | 2 | 1 |
| $\lambda_{PN}$ (1/d) | tasa proliferativo→necrótico | 0,1 | 20 |

Parámetros comunes: $c_m=5\times10^{-4}$, $\varepsilon_P=5\times10^{-4}$, $c_\Psi=2$, $\sigma_{PN}=0{,}2$, $\kappa_i=10^{-5}$, $\alpha_H=1$, $\alpha_P=4$, $\epsilon_g=0{,}1$, $\chi=0$.

Los valores PK de P1 corresponden al nivolumab y los de P2 al pembrolizumab [Wagner 2023, Tabla 1 y ref. 16].

### 2.3 Índices de sensibilidad local y el factor α/100

**Definición publicada.** Para un campo escalar $f\in\{\phi_T,\phi_P,\phi_N,V_{vis}\}$, se define la masa promediada en el tiempo $\bar Q(f)=\tfrac1T\int_0^T\!\int_\Omega f\,d\mathbf x\,dt$. El artículo define el índice de sensibilidad local del parámetro $\alpha$ como

$$
g_{f,\alpha}:=\frac{\partial_\alpha\bar Q(f)}{\bar Q(f)}\cdot\frac{\alpha}{100\,\%},
\tag{5}
$$

y lo describe verbalmente como «el cambio relativo [de $\bar Q$] a primer orden al variar $\alpha$ un 1 por ciento» [Wagner 2023, p. 16].

**Interpretación del factor.** Un desarrollo de Taylor de primer orden con $\Delta\alpha=0{,}01\,\alpha$ da $\Delta\bar Q/\bar Q\approx(\partial_\alpha\bar Q/\bar Q)\,\alpha/100$. Esta es la lectura que se adopta aquí.
- Si se lee literalmente «100 %» = 1, la ec. (5) sería en cambio la elasticidad $(\partial_\alpha\bar Q/\bar Q)\,\alpha$.
- Tanto la definición verbal como los valores publicados (§4.2) respaldan la lectura $\alpha/100$.
- Con esa lectura, $g=0{,}011$ significa que $\bar Q$ cambia aproximadamente un 1,1 % cuando $\alpha$ cambia un 1 %.

**Lo que calcula el script liberado** (`local_sensitivity_analysis.py`, ll. 101–104):

$$
g^{\text{script}}_{f,\alpha}=\frac{\bar Q\big(f;\alpha(1+h)\big)-\bar Q\big(f;\alpha(1-h)\big)}{2h\,\alpha\,\bar Q(f;\alpha)}\;\approx\;\frac{\partial_\alpha\bar Q}{\bar Q},\qquad h=10^{-3},
\tag{6}
$$

con las integrales temporales evaluadas por la regla del trapecio. Por tanto,

$$
g^{\text{publicado}}\;\overset{?}{=}\;g^{\text{script}}\cdot\frac{\alpha}{100}.
\tag{7}
$$

**Estatus de (7).** La ecuación (7) es una **hipótesis** sobre cómo se obtuvo la tabla publicada, que se contrasta en §4.2. El factor $\alpha/100$ es un reescalado de la definición de un índice de sensibilidad. **No es un parámetro calibrado del modelo.**

### 2.4 El defecto de configuración H01

**Qué hace el código.**
- En el script liberado, la simulación de referencia de P2 usa los parámetros PK del paciente ($M_\tau=143\,600$, $d_\tau=0{,}20$, $t_{1/2}=22$).
- Las simulaciones perturbadas se reconstruyen a partir de un vector de 11 parámetros que no contiene esos campos (`vector_to_parameters`, ll. 35–48) [Wagner 2023, code repository].
- En consecuencia, vuelven a los valores por defecto de `parameters.py` (146 000; 0,24; 26,7), que son los valores del nivolumab de P1.

**Consecuencia para P2.** La ec. (6) se evalúa como

$$
g^{\text{script,H01}}_{f,\alpha}=\frac{\bar Q(f;\alpha(1+h),\beta_{\text{def}})-\bar Q(f;\alpha(1-h),\beta_{\text{def}})}{2h\,\alpha\,\bar Q(f;\alpha,\beta_{\text{P2}})},
\tag{8}
$$

donde $\beta$ denota el triplete PK: el numerador deriva en torno a una exposición al fármaco distinta de la que lo normaliza.

**P1 no se ve afectado,** porque sus valores por defecto coinciden con sus propios valores PK.

---

## 3. Implementación computacional y auditoría de reproducibilidad

### 3.1 Entorno de ejecución en contenedor

**Imagen.**
- dolfin 2019.1.0 no tiene versión para Windows, y la imagen oficial de FEniCS usa un formato de manifiesto que Docker 29 ya no admite.
- Por eso construimos la imagen Docker [Merkel 2014] `papercancer/t01-fenics2019:1` a partir de conda-forge [conda-forge community 2015] (miniforge3; Python 3.10.22; fenics-dolfin 2019.1.0 [Logg & Wells 2010; Alnæs et al. 2015]; numpy 1.26.4 [Harris et al. 2020]; scipy 1.15.2 [Virtanen et al. 2020]; petsc 3.25.6 [Balay et al., PETSc manual]; joblib 1.6.0 [Joblib developers]).
- El conjunto exacto de paquetes está congelado en un archivo de bloqueo explícito de conda.

**Tratamiento del código y los datos.**
- El repositorio de los autores (commit `fa8e6229`, sin licencia) se monta en solo lectura y se ejecuta sin modificar.
- Nuestros envoltorios lo referencian por commit y ruta; no se copia ni se redistribuye.

**Equipo y recursos.**
- El equipo anfitrión tenía 14 núcleos, de los que se asignaron 8 CPU al contenedor (`--cpus 8`); la máquina virtual de Docker disponía de 7,5 GiB de RAM.
- El script lanza `cpu_count()` workers de joblib (14 dentro del contenedor, según el informe de T01; el valor no aparece en los registros), así que sus 11 tareas paralelas por paciente comparten la cuota de 8 CPU.
- La memoria no fue un factor limitante:
  - la ejecución completa de la Tabla 2 terminó sin ninguna terminación por falta de memoria;
  - en la ejecución de corrección de P2 (23 simulaciones, 11 workers en paralelo; 177 muestras, una cada 60 s), la memoria del contenedor alcanzó un pico de 1,36 GiB (18 % de 7,48 GiB; mediana 1,31 GiB), con un uso medio de CPU de 7,2 núcleos.

**Incidencias de estabilidad** (documentadas; ninguna alteró ningún cálculo):
- Una primera ejecución completa (11 oct 2026) se interrumpió, probablemente porque el equipo entró en modo de espera moderno (registro de eventos de Windows; no demostrado). Se relanzó con una solicitud al sistema operativo para mantener el equipo activo y sin eliminación automática del contenedor.
- En la ejecución de corrección de H01, los workers de loky morían de forma intermitente (SIGSEGV/SIGBUS) dentro de `MPI.init()`, que dolfin llama al importarse (MPICH 5.0.1 [MPICH]), cuando arrancaban muchos a la vez:
  - el primer intento completo falló tras su simulación de referencia, sin ningún evento de falta de memoria;
  - la hipótesis principal es una contención por memoria compartida (`/dev/shm`, 64 MB por defecto en Docker), plausible pero no demostrada;
  - el segundo intento amplió `/dev/shm` a 1 GiB, eliminó los procesos concurrentes y añadió un reintento automático; terminó sin necesitar ningún reintento (código de salida 0; 183,6 min).

  Todos los intentos están archivados con sus registros.
- **Coste:** el cálculo completo de la Tabla 2 (2 pacientes × 23 simulaciones) tardó 309 min de tiempo real; la ejecución de corrección, solo de P2, 184 min.

### 3.2 Criterios de reproducción preespecificados

Los criterios se fijaron en un contrato de tarea **antes** de la ejecución.

| Objetivo | Métrica | Reproducido | Parcialmente | Discrepancia |
|---|---|---|---|---|
| PK (ec. 4) | último pico y valle periódicos frente a la solución analítica | ≤ 0,1 % | — | > 0,1 % |
| Tabla 2 (88 índices) | error relativo y signo | ≤ 10 %, mismo signo | 10–50 %, mismo signo (o dentro de tolerancia pero con rango distinto) | > 50 % o cambio de signo |
| Hipótesis global H1 | — | ≥ 80 % de los 88 índices «reproducidos» | | |

La tolerancia del 10 % contempla:
- el redondeo a tres cifras significativas (≤ 0,5 %);
- la cancelación en las diferencias centradas con $h=10^{-3}$;
- las diferencias de versión del solucionador y de las bibliotecas.

Los autores no indicaron sus versiones.

### 3.3 Protocolo de verificación

**Verificación independiente.** Los números T remiten al registro de tareas del proyecto. Los resultados de T01 se verificaron de forma independiente antes de integrarlos. Los de T06 (§4.3) se apoyan en un análisis preespecificado y en un control de determinismo exacto bit a bit, pero **todavía no tienen revisión independiente**.
- **T01, ejecución.** Ejecución sin modificar, verificación PK, Tabla 2 y correspondencia artículo–código (35 elementos).
- **T03, revisión crítica independiente.** La realizó un segundo agente con su propio código, que leyó los scripts de los autores mediante análisis estático, sin importarlos. Abarcó:
  - el recálculo de todas las comparaciones;
  - siete transformaciones de escala alternativas;
  - una retranscripción completa de los 88 valores y rangos publicados a partir del texto del artículo;
  - la verificación de los 22 vectores de parámetros.

  La revisión planteó dos objeciones mayores:
  - H01, el defecto de configuración;
  - H02, una interpretación que iba más allá de la evidencia en nuestro primer borrador.

  Ambas se aceptaron. La redacción de este manuscrito sigue las recomendaciones del revisor.
- **T06, variante de corrección declarada.** Se re-simuló P2 con la rutina de sensibilidad de los autores sin modificar. El único cambio fue la función de simulación, que restaura el triplete PK de P2 antes de cada ejecución perturbada y registra las integrales $\bar Q$. El plan de análisis y las clases de efecto se preespecificaron antes del lanzamiento. Un control de determinismo recalculó una componente de P2 con el defecto original.

**Contraste en una tarea de reconstrucción no relacionada (T02, T04, T05).** El mismo protocolo de ejecutar, auditar y corregir se aplicó a otro problema: reconstruir datos individuales de pacientes a partir de las curvas vectoriales de Kaplan–Meier del ensayo ADRIATIC (cáncer de pulmón de células pequeñas en estadio limitado) [Cheng et al. 2024; Guyot et al. 2012]. Se hizo en tres pasos:
- un agente ejecutó la reconstrucción;
- una auditoría independiente la re-ejecutó byte a byte, volvió a extraer las curvas por rasterización y reajustó los modelos de Kaplan–Meier [Kaplan & Meier 1958] y de Cox [Cox 1972] con código independiente;
- las 18 cantidades preespecificadas ya se reproducían en la entrega original;
- una ronda de corrección resolvió dos defectos, en la extracción de las curvas (escalones fusionados) y en el diseño de la validación con verdad conocida, y las 18 cantidades siguieron dentro de tolerancia.

Se mantuvo y declaró un fallo residual de una prueba unitaria, en lugar de editarlo a posteriori: 7 de 400 curvas sintéticas pierden un escalón más estrecho que la precisión de las coordenadas del PDF.

Esta tarea trata de otra enfermedad. Se presenta solo como evidencia del comportamiento del protocolo de auditoría (Suplemento S2) y **no** se combina con el modelo de CPCNP.

### 3.4 Correspondencia artículo–código

De los 35 elementos revisados:
- 21 coinciden (3 dentro del redondeo y 1 tras una conversión de unidades);
- el código resuelve 5 elementos que el artículo deja sin especificar;
- 9 son discrepancias, que se mantienen como incertidumbre y no se «corrigen» (Tabla 2).

H01 (§2.4) es un defecto adicional del script de sensibilidad.

**Tabla 2. Discrepancias entre el artículo publicado y el código liberado.**

| N.º | Elemento | Artículo | Código |
|---|---|---|---|
| 1 | Índice de sensibilidad | ec. (5), con α/100 | ec. (6), sin α/100 |
| 2 | Término de muerte por fármaco | $\lambda_\tau^{eff}/\omega$, $\omega=80$ | factor adicional 0,7 ($\omega$ efectivo ≈ 114,3) |
| 3 | Inicio del tratamiento de P1 | día 296 | día 322 de la línea temporal de los datos (26 d más tarde) |
| 4 | Inicio de Q6W / fin del tratamiento de P2 | días 514 / 1063 | días 671 / 1218 (157 / 155 d más tarde) |
| 5 | Malla de P2 | 500 elementos | 1000 elementos |
| 6 | Función de Heaviside $H$ | función escalón | sigmoide suave (pendiente 30) |
| 7 | Consumo de nutrientes | células proliferativas y necróticas | las células necróticas no consumen |
| 8 | $\lambda_\tau^{eff}$ de P2 | 0,54 | 0,5489 (se redondea a 0,55) |
| 9 | Horizonte $T$ de la Tabla 2 | «fin del tratamiento» | 9 d (P1) y 2 d (P2) antes del final |

Los calendarios del código coinciden con las figuras del preprint de los autores [Wagner 2023, preprint].

---

## 4. Resultados y discusión comparativa

### 4.1 Farmacocinética

**Reproducido exactamente.**
- El `MedicineSolver` original reproduce la EDO (4).
- En las 136 administraciones (96 de P1 y 40 de P2), la dosis administrada es igual a la nominal.
- A lo largo de toda la trayectoria, el percentil 99 del error relativo puntual es 1,7 × 10⁻⁵ (P1) y 2,1 × 10⁻⁵ (P2).

**Criterio preespecificado no cumplido.** El criterio de picos y valles se cumple en **3 de 6** extremos:

| Calendario | Error del pico | Error del valle |
|---|---|---|
| P1, Q2W | 0,0017 % | 0,107 % |
| P2, Q3W | 0,0020 % | 0,129 % |
| P2, Q6W | 0,129 % | 0,0021 % |

**Causa.** Todos los excesos proceden de una sola muestra por dosis, al principio o al final de la infusión. La ventana de infusión efectiva está desplazada ±0,5 subpasos PK (≈ 56 s), un detalle de discretización del solucionador.

**Clasificación: parcialmente reproducido.** Su efecto sobre la dinámica tumoral no se cuantificó por separado. La concordancia de la Tabla 2 en §4.2 indica que no altera los índices de sensibilidad a la precisión publicada.

### 4.2 Tabla 2: índices publicados, brutos y reescalados

**Salida bruta del script (criterio preespecificado).** El script liberado se ejecutó sin modificar para ambos pacientes (código de salida 0; 309 min). Su salida no coincide con **ninguno** de los 88 índices publicados:
- error relativo: mediana 228, percentil 90 de 2,0 × 10⁵ y máximo de 1,0 × 10⁷ (como fracciones);
- concordancia de signo: 88/88;
- concordancia de rango: 8/88.

Por tanto, la hipótesis de reproducción H1 se **rechaza**, y esta clasificación se mantiene.

**Salida reescalada (diagnóstico).** Al aplicar la ec. (7) se recuperan todos los valores impresos:

**Tabla 3. Concordancia de la salida transformada del script con la Tabla 2 publicada** (88 índices; recálculo independiente, T03).

| Transformación de $g^{\text{script}}$ | Error relativo máx. | Dentro del 10 %, mismo signo | Rangos iguales | Iguales tras redondear a 3 c.s. |
|---|---|---|---|---|
| ninguna (bruta) | 1,0 × 10⁹ % | 0 | 8 | 0 |
| **× α / 100** | **0,449 %** | **88** | **88** | **88** |
| × α (elasticidad) | 9 931 % | 0 | 88 | 0 |
| / 100 | 1,0 × 10⁷ % | 12 | 8 | 12 |
| × α del otro paciente / 100 | 19 939 % | 56 | 25 | 56 |
| × α redondeado como en la Tabla 1 / 100 | 1,81 % | 88 | 88 | 74 |
| × α / 101 (control negativo) | 1,44 % | 88 | 88 | 0 |

Otras cifras del reescalado × α / 100:
- error relativo mediano 0,068 %, percentil 90 del 0,22 %;
- mayor residuo: P1, $\lambda_P^{pro}$, $\bar Q(\phi_T)$, con 0,01095 frente al 0,0110 publicado.

**Qué muestra la Tabla 3.**
- La tolerancia del 10 % por sí sola no identifica la transformación: el divisor de control 101 también la supera.
- La coincidencia exacta tras el redondeo señala a $\alpha/100$.
- Esto **respalda, pero no demuestra,** que la tabla publicada se obtuviera aplicando la ec. (5) a la salida del script. El repositorio no documenta ese paso.

El reescalado elimina la discrepancia de escala, pero no valida por sí mismo el procedimiento, como muestra §4.3.

La Tabla 4 recoge los 88 valores (Figura 1: `figuras/fig_tabla2.png`).

<!-- TABLA_88_INICIO -->
**Tabla 4. Índices de sensibilidad local: valores publicados frente a la salida del script liberado (bruta), reescalada ×α/100 y, en P2, reescalada tras corregir H01.** Los valores publicados son los de la Tabla 2 de Wagner et al. [2023] (CC BY 4.0), con el rango entre paréntesis. Err. rel. = |g − g_pub|/|g_pub|. Δ_H01 = (g_corr − g_orig)/|g_orig|. Fuente: `tabla2_comparacion.csv` y `t06_88_corregido.csv`.

| Pac. | Parámetro | Cantidad | Publicado (rango) | Script bruto | ×α/100 | Err. rel. | P2 corregido ×α/100 (rango) | Err. rel. | Δ_H01 |
|---|---|---|---|---|---|---|---|---|---|
| P1 | λ_P^pro | φ_T | 1,10e-2 (3) | 3,036e+0 | 1,095e-2 | 0,449 % | — (no afectado) | |  |
| P1 | λ_P^pro | φ_P | 9,02e-3 (2) | 2,502e+0 | 9,023e-3 | 0,030 % | — (no afectado) | |  |
| P1 | λ_P^pro | φ_N | 1,42e-2 (4) | 3,941e+0 | 1,421e-2 | 0,093 % | — (no afectado) | |  |
| P1 | λ_P^pro | V_vis | 1,02e-2 (5) | 2,825e+0 | 1,019e-2 | 0,117 % | — (no afectado) | |  |
| P1 | λ_τ^eff | φ_T | -3,55e-3 (7) | -6,776e-2 | -3,550e-3 | 0,004 % | — (no afectado) | |  |
| P1 | λ_τ^eff | φ_P | -5,08e-3 (6) | -9,701e-2 | -5,083e-3 | 0,052 % | — (no afectado) | |  |
| P1 | λ_τ^eff | φ_N | -9,57e-4 (10) | -1,826e-2 | -9,565e-4 | 0,049 % | — (no afectado) | |  |
| P1 | λ_τ^eff | V_vis | -5,16e-3 (7) | -9,845e-2 | -5,158e-3 | 0,034 % | — (no afectado) | |  |
| P1 | λ | φ_T | -1,64e-2 (1) | -8,196e-1 | -1,639e-2 | 0,044 % | — (no afectado) | |  |
| P1 | λ | φ_P | -1,37e-2 (1) | -6,827e-1 | -1,365e-2 | 0,335 % | — (no afectado) | |  |
| P1 | λ | φ_N | -2,10e-2 (3) | -1,051e+0 | -2,103e-2 | 0,132 % | — (no afectado) | |  |
| P1 | λ | V_vis | -1,50e-2 (4) | -7,514e-1 | -1,503e-2 | 0,187 % | — (no afectado) | |  |
| P1 | λ_PN | φ_T | 1,77e-3 (10) | 1,767e+0 | 1,767e-3 | 0,163 % | — (no afectado) | |  |
| P1 | λ_PN | φ_P | -2,20e-4 (10) | -2,197e-1 | -2,197e-4 | 0,127 % | — (no afectado) | |  |
| P1 | λ_PN | φ_N | 5,13e-3 (8) | 5,130e+0 | 5,130e-3 | 0,007 % | — (no afectado) | |  |
| P1 | λ_PN | V_vis | 2,32e-3 (10) | 2,324e+0 | 2,324e-3 | 0,193 % | — (no afectado) | |  |
| P1 | σ_PN | φ_T | 1,05e-2 (4) | 5,227e+0 | 1,045e-2 | 0,435 % | — (no afectado) | |  |
| P1 | σ_PN | φ_P | -1,30e-3 (9) | -6,491e-1 | -1,298e-3 | 0,145 % | — (no afectado) | |  |
| P1 | σ_PN | φ_N | 3,03e-2 (2) | 1,517e+1 | 3,034e-2 | 0,145 % | — (no afectado) | |  |
| P1 | σ_PN | V_vis | 3,01e-2 (2) | 1,503e+1 | 3,006e-2 | 0,128 % | — (no afectado) | |  |
| P1 | c_m | φ_T | -2,10e-4 (11) | -4,203e+1 | -2,101e-4 | 0,067 % | — (no afectado) | |  |
| P1 | c_m | φ_P | -2,08e-4 (11) | -4,154e+1 | -2,077e-4 | 0,156 % | — (no afectado) | |  |
| P1 | c_m | φ_N | -2,14e-4 (11) | -4,286e+1 | -2,143e-4 | 0,146 % | — (no afectado) | |  |
| P1 | c_m | V_vis | -3,41e-4 (11) | -6,817e+1 | -3,408e-4 | 0,049 % | — (no afectado) | |  |
| P1 | ε_P | φ_T | 8,81e-3 (5) | 1,762e+3 | 8,810e-3 | 0,003 % | — (no afectado) | |  |
| P1 | ε_P | φ_P | 6,78e-3 (3) | 1,357e+3 | 6,784e-3 | 0,064 % | — (no afectado) | |  |
| P1 | ε_P | φ_N | 1,22e-2 (5) | 2,447e+3 | 1,224e-2 | 0,307 % | — (no afectado) | |  |
| P1 | ε_P | V_vis | 7,66e-3 (6) | 1,532e+3 | 7,661e-3 | 0,012 % | — (no afectado) | |  |
| P1 | c_Ψ | φ_T | -4,62e-3 (6) | -2,308e-1 | -4,615e-3 | 0,108 % | — (no afectado) | |  |
| P1 | c_Ψ | φ_P | -3,60e-3 (7) | -1,800e-1 | -3,600e-3 | 0,004 % | — (no afectado) | |  |
| P1 | c_Ψ | φ_N | -6,33e-3 (7) | -3,167e-1 | -6,333e-3 | 0,048 % | — (no afectado) | |  |
| P1 | c_Ψ | V_vis | -4,25e-3 (9) | -2,126e-1 | -4,252e-3 | 0,058 % | — (no afectado) | |  |
| P1 | κ_i | φ_T | -2,87e-3 (8) | -2,871e+4 | -2,871e-3 | 0,036 % | — (no afectado) | |  |
| P1 | κ_i | φ_P | 1,52e-3 (8) | 1,520e+4 | 1,520e-3 | 0,008 % | — (no afectado) | |  |
| P1 | κ_i | φ_N | -1,03e-2 (6) | -1,030e+5 | -1,030e-2 | 0,022 % | — (no afectado) | |  |
| P1 | κ_i | V_vis | -2,15e-2 (3) | -2,155e+5 | -2,155e-2 | 0,218 % | — (no afectado) | |  |
| P1 | α_H | φ_T | -2,51e-3 (9) | -2,508e-1 | -2,508e-3 | 0,081 % | — (no afectado) | |  |
| P1 | α_H | φ_P | -6,53e-3 (4) | -6,525e-1 | -6,525e-3 | 0,070 % | — (no afectado) | |  |
| P1 | α_H | φ_N | 4,29e-3 (9) | 4,291e-1 | 4,291e-3 | 0,028 % | — (no afectado) | |  |
| P1 | α_H | V_vis | -4,37e-3 (8) | -4,373e-1 | -4,373e-3 | 0,076 % | — (no afectado) | |  |
| P1 | α_P | φ_T | 1,28e-2 (2) | 3,195e-1 | 1,278e-2 | 0,152 % | — (no afectado) | |  |
| P1 | α_P | φ_P | -6,25e-3 (5) | -1,562e-1 | -6,246e-3 | 0,059 % | — (no afectado) | |  |
| P1 | α_P | φ_N | 4,50e-2 (1) | 1,125e+0 | 4,498e-2 | 0,041 % | — (no afectado) | |  |
| P1 | α_P | V_vis | 3,09e-2 (1) | 7,725e-1 | 3,090e-2 | 0,005 % | — (no afectado) | |  |
| P2 | λ_P^pro | φ_T | 4,13e-2 (2) | 1,093e+3 | 4,129e-2 | 0,024 % | 4,714e-2 (2) | 14,151 % | +14,178 % |
| P2 | λ_P^pro | φ_P | 4,17e-2 (2) | 1,103e+3 | 4,167e-2 | 0,077 % | 4,758e-2 (2) | 14,091 % | +14,179 % |
| P2 | λ_P^pro | φ_N | 6,19e-4 (11) | 1,638e+1 | 6,189e-4 | 0,012 % | 6,581e-4 (11) | 6,314 % | +6,326 % |
| P2 | λ_P^pro | V_vis | 1,75e-3 (11) | 4,621e+1 | 1,746e-3 | 0,233 % | 1,711e-3 (10) | 2,242 % | -2,013 % |
| P2 | λ_τ^eff | φ_T | -2,08e-2 (4) | -3,782e+0 | -2,076e-2 | 0,194 % | -2,217e-2 (4) | 6,564 % | -6,771 % |
| P2 | λ_τ^eff | φ_P | -2,09e-2 (4) | -3,811e+0 | -2,092e-2 | 0,099 % | -2,234e-2 (4) | 6,884 % | -6,778 % |
| P2 | λ_τ^eff | φ_N | -3,41e-3 (7) | -6,210e-1 | -3,408e-3 | 0,044 % | -3,461e-3 (7) | 1,509 % | -1,554 % |
| P2 | λ_τ^eff | V_vis | -6,74e-3 (6) | -1,227e+0 | -6,736e-3 | 0,064 % | -6,105e-3 (5) | 9,417 % | +9,359 % |
| P2 | λ | φ_T | -1,82e-1 (1) | -1,822e+1 | -1,822e-1 | 0,132 % | -2,052e-1 (1) | 12,750 % | -12,602 % |
| P2 | λ | φ_P | -1,84e-1 (1) | -1,839e+1 | -1,839e-1 | 0,046 % | -2,071e-1 (1) | 12,551 % | -12,603 % |
| P2 | λ | φ_N | -1,71e-3 (8) | -1,714e-1 | -1,714e-3 | 0,258 % | -1,846e-3 (8) | 7,927 % | -7,649 % |
| P2 | λ | V_vis | -5,02e-3 (7) | -5,023e-1 | -5,023e-3 | 0,055 % | -5,093e-3 (7) | 1,451 % | -1,395 % |
| P2 | λ_PN | φ_T | 3,61e-4 (11) | 1,804e-3 | 3,608e-4 | 0,045 % | 4,470e-4 (11) | 23,812 % | +23,867 % |
| P2 | λ_PN | φ_P | 3,28e-4 (11) | 1,638e-3 | 3,276e-4 | 0,119 % | 4,144e-4 (11) | 26,336 % | +26,487 % |
| P2 | λ_PN | φ_N | 3,94e-3 (5) | 1,970e-2 | 3,940e-3 | 0,006 % | 3,956e-3 (5) | 0,411 % | +0,404 % |
| P2 | λ_PN | V_vis | 2,17e-3 (10) | 1,085e-2 | 2,169e-3 | 0,029 % | 1,234e-3 (11) | 43,152 % | -43,135 % |
| P2 | σ_PN | φ_T | 2,17e-3 (8) | 1,083e+0 | 2,165e-3 | 0,226 % | 2,682e-3 (8) | 23,589 % | +23,869 % |
| P2 | σ_PN | φ_P | 1,97e-3 (8) | 9,829e-1 | 1,966e-3 | 0,216 % | 2,486e-3 (8) | 26,215 % | +26,488 % |
| P2 | σ_PN | φ_N | 2,36e-2 (3) | 1,182e+1 | 2,364e-2 | 0,160 % | 2,373e-2 (3) | 0,566 % | +0,405 % |
| P2 | σ_PN | V_vis | 1,33e-2 (3) | 6,659e+0 | 1,332e-2 | 0,130 % | 7,996e-3 (4) | 39,880 % | -39,958 % |
| P2 | c_m | φ_T | 4,45e-3 (6) | 8,903e+2 | 4,452e-3 | 0,035 % | 5,164e-3 (6) | 16,051 % | +16,011 % |
| P2 | c_m | φ_P | 4,50e-3 (6) | 9,001e+2 | 4,501e-3 | 0,016 % | 5,220e-3 (6) | 16,010 % | +15,990 % |
| P2 | c_m | φ_N | -8,46e-4 (10) | -1,692e+2 | -8,462e-4 | 0,022 % | -8,828e-4 (10) | 4,355 % | -4,332 % |
| P2 | c_m | V_vis | -2,79e-3 (8) | -5,582e+2 | -2,791e-3 | 0,032 % | -2,817e-3 (8) | 0,974 % | -0,941 % |
| P2 | ε_P | φ_T | 1,52e-2 (5) | 3,039e+3 | 1,519e-2 | 0,036 % | 1,759e-2 (5) | 15,720 % | +15,761 % |
| P2 | ε_P | φ_P | 1,54e-2 (5) | 3,074e+3 | 1,537e-2 | 0,206 % | 1,779e-2 (5) | 15,498 % | +15,736 % |
| P2 | ε_P | φ_N | -3,52e-3 (6) | -7,042e+2 | -3,521e-3 | 0,029 % | -3,657e-3 (6) | 3,898 % | -3,868 % |
| P2 | ε_P | V_vis | -1,09e-2 (4) | -2,174e+3 | -1,087e-2 | 0,280 % | -1,115e-2 (2) | 2,279 % | -2,567 % |
| P2 | c_Ψ | φ_T | -3,15e-3 (7) | -1,573e-1 | -3,146e-3 | 0,135 % | -3,630e-3 (7) | 15,252 % | -15,407 % |
| P2 | c_Ψ | φ_P | -3,18e-3 (7) | -1,592e-1 | -3,183e-3 | 0,109 % | -3,673e-3 (7) | 15,500 % | -15,375 % |
| P2 | c_Ψ | φ_N | 9,14e-4 (9) | 4,572e-2 | 9,143e-4 | 0,036 % | 9,458e-4 (9) | 3,476 % | +3,439 % |
| P2 | c_Ψ | V_vis | 2,54e-3 (9) | 1,272e-1 | 2,545e-3 | 0,195 % | 2,792e-3 (9) | 9,935 % | +9,720 % |
| P2 | κ_i | φ_T | -1,66e-3 (10) | -1,663e+4 | -1,663e-3 | 0,183 % | -2,064e-3 (10) | 24,326 % | -24,098 % |
| P2 | κ_i | φ_P | -1,52e-3 (10) | -1,515e+4 | -1,515e-3 | 0,309 % | -1,919e-3 (10) | 26,268 % | -26,659 % |
| P2 | κ_i | φ_N | -1,76e-2 (4) | -1,758e+5 | -1,758e-2 | 0,130 % | -1,763e-2 (4) | 0,187 % | -0,317 % |
| P2 | κ_i | V_vis | -9,74e-3 (5) | -9,742e+4 | -9,742e-3 | 0,025 % | -5,956e-3 (6) | 38,849 % | +38,864 % |
| P2 | α_H | φ_T | -3,64e-2 (3) | -3,640e+0 | -3,640e-2 | 0,009 % | -4,097e-2 (3) | 12,545 % | -12,535 % |
| P2 | α_H | φ_P | -3,71e-2 (3) | -3,706e+0 | -3,706e-2 | 0,105 % | -4,167e-2 (3) | 12,313 % | -12,431 % |
| P2 | α_H | φ_N | 3,44e-2 (2) | 3,445e+0 | 3,445e-2 | 0,143 % | 3,462e-2 (2) | 0,645 % | +0,501 % |
| P2 | α_H | V_vis | 1,71e-2 (2) | 1,710e+0 | 1,710e-2 | 0,025 % | 9,372e-3 (3) | 45,192 % | -45,178 % |
| P2 | α_P | φ_T | 2,14e-3 (9) | 5,361e-2 | 2,144e-3 | 0,202 % | 2,618e-3 (9) | 22,328 % | +22,082 % |
| P2 | α_P | φ_P | 1,76e-3 (9) | 4,400e-2 | 1,760e-3 | 0,008 % | 2,236e-3 (9) | 27,072 % | +27,062 % |
| P2 | α_P | φ_N | 4,35e-2 (1) | 1,088e+0 | 4,353e-2 | 0,059 % | 4,370e-2 (1) | 0,451 % | +0,391 % |
| P2 | α_P | V_vis | 2,48e-2 (1) | 6,199e-1 | 2,480e-2 | 0,012 % | 1,512e-2 (1) | 39,018 % | -39,011 % |
<!-- TABLA_88_FIN -->

### 4.3 Efecto de corregir H01 sobre la sensibilidad del paciente 2

<!-- H01_RESULTADOS_INICIO -->
**Diseño (preespecificado antes del lanzamiento).**
- Se llamó a la rutina de sensibilidad de los autores, sin modificar, para P2 (dt = 1/24 d, T = 1102 d, h = 10⁻³).
- El único cambio fue la función de simulación: antes de cada una de las 23 simulaciones, restaura el triplete de P2 $(M_\tau,d_\tau,t_{1/2})=(143\,600,\;0{,}20,\;22)$ y registra las integrales $\bar Q$.
- Los registros confirman el defecto y su corrección:
  - las 22 simulaciones perturbadas llegaron con el triplete por defecto (146 000; 0,24; 26,7) y se corrigieron;
  - la simulación de referencia ya tenía los valores de P2.
- **Clases de efecto**, definidas de antemano sobre $\Delta_{H01}=(g_{corr}-g_{orig})/|g_{orig}|$:
  - *despreciable*: máx. $|\Delta|\le0{,}5$ %, sin cambios de signo ni de rango;
  - *menor*: ≤ 10 %;
  - *relevante*: > 10 %, o cualquier cambio de signo o de rango.

**Control de determinismo.** La componente 1 de P2 ($\lambda_\tau^{eff}$) se recalculó **con** el defecto original. Los cuatro índices fueron idénticos a los de la ejecución original en todas las cifras impresas (diferencia relativa 0,0). Por tanto, las simulaciones son deterministas y todos los cambios que siguen se deben a la corrección.

**Magnitud del defecto.** En ese control, las simulaciones perturbadas (con los parámetros del fármaco de P1: más dosis y semivida más larga) dieron una masa tumoral total promediada en el tiempo un 15 % menor que la de referencia ($\bar Q(\phi_T)$ = 3,14 × 10⁻³ frente a 3,71 × 10⁻³). Los índices originales de P2 dividen, por tanto, una derivada tomada con una exposición al fármaco entre una masa tomada con otra.

**Efecto sobre los 44 índices de P2: relevante** (Tabla 5; Figura 3: `figuras/fig_h01.png`).

| Cantidad de interés | \|Δ_H01\| mediana | \|Δ_H01\| máx. | Cambios de rango (de 11) |
|---|---|---|---|
| $\bar Q(\phi_T)$ | 16,0 % | 24,1 % | 0 |
| $\bar Q(\phi_P)$ | 16,0 % | 27,1 % | 0 |
| $\bar Q(\phi_N)$ | 3,4 % | 7,6 % | 0 |
| $\bar Q(V_{vis})$ | 38,9 % | 45,2 % | 7 |
| **Los 44** | **12,6 %** | **45,2 %** | **7** |

- **Signos:** ningún índice cambia de signo.
- **Mayores cambios:** todos en el volumen visible. $\alpha_H$ (−45,2 %), $\lambda_{PN}$ (−43,1 %), $\sigma_{PN}$ (−40,0 %), $\alpha_P$ (−39,0 %) y $\kappa_i$ (+38,9 %).
- **Ranking del volumen visible:** el primer parámetro ($\alpha_P$) no cambia, pero se reordenan las posiciones 2–6 y 10–11. En particular, $\varepsilon_P$ sube del puesto 4 al 2 y $\alpha_H$ baja del 2 al 3.
- **Parámetros calibrados:**
  - para $\lambda_P^{pro}$ y $\lambda$, los índices de masa total cambian +14,2 % y −12,6 %;
  - para el parámetro de efecto del fármaco, $\lambda_\tau^{eff}$, el índice de masa total cambia −6,8 % y el de volumen visible +9,4 %.

**Concordancia de los valores corregidos de P2 con la tabla publicada.**
- Los valores de P2 con la configuración original coinciden 44/44 a tres cifras significativas (§4.2).
- Los corregidos coinciden solo en 1/44 (19/44 dentro del 10 %; error mediano 12,7 %).
- En los 88 índices (P1 sin cambios, P2 corregido), 45/88 coinciden a tres cifras significativas y 81/88 rangos son iguales.
- Este contraste es una prueba más de que la columna publicada de P2 se obtuvo con la configuración defectuosa.

<!-- TABLA_H01_INICIO -->
**Tabla 5. Paciente 2: índices de sensibilidad (×α/100) con la configuración original (H01) y tras la corrección.** Rangos por |g| dentro de cada cantidad de interés. Valores publicados: Wagner et al. [2023], Tabla 2 (CC BY 4.0). Fuente: `t06_p2_indices.csv`.

| Parámetro | Cantidad | Original (rango) | Corregido (rango) | Δ_H01 | Publicado (rango) |
|---|---|---|---|---|---|
| λ_P^pro | φ_T | 4,129e-2 (2) | 4,714e-2 (2) | +14,178 % | 4,13e-2 (2) |
| λ_P^pro | φ_P | 4,167e-2 (2) | 4,758e-2 (2) | +14,179 % | 4,17e-2 (2) |
| λ_P^pro | φ_N | 6,189e-4 (11) | 6,581e-4 (11) | +6,326 % | 6,19e-4 (11) |
| λ_P^pro | V_vis | 1,746e-3 (11) | 1,711e-3 (10) | -2,013 % | 1,75e-3 (11) |
| λ_τ^eff | φ_T | -2,076e-2 (4) | -2,217e-2 (4) | -6,771 % | -2,08e-2 (4) |
| λ_τ^eff | φ_P | -2,092e-2 (4) | -2,234e-2 (4) | -6,778 % | -2,09e-2 (4) |
| λ_τ^eff | φ_N | -3,408e-3 (7) | -3,461e-3 (7) | -1,554 % | -3,41e-3 (7) |
| λ_τ^eff | V_vis | -6,736e-3 (6) | -6,105e-3 (5) | +9,359 % | -6,74e-3 (6) |
| λ | φ_T | -1,822e-1 (1) | -2,052e-1 (1) | -12,602 % | -1,82e-1 (1) |
| λ | φ_P | -1,839e-1 (1) | -2,071e-1 (1) | -12,603 % | -1,84e-1 (1) |
| λ | φ_N | -1,714e-3 (8) | -1,846e-3 (8) | -7,649 % | -1,71e-3 (8) |
| λ | V_vis | -5,023e-3 (7) | -5,093e-3 (7) | -1,395 % | -5,02e-3 (7) |
| λ_PN | φ_T | 3,608e-4 (11) | 4,470e-4 (11) | +23,867 % | 3,61e-4 (11) |
| λ_PN | φ_P | 3,276e-4 (11) | 4,144e-4 (11) | +26,487 % | 3,28e-4 (11) |
| λ_PN | φ_N | 3,940e-3 (5) | 3,956e-3 (5) | +0,404 % | 3,94e-3 (5) |
| λ_PN | V_vis | 2,169e-3 (10) | 1,234e-3 (11) | -43,135 % | 2,17e-3 (10) |
| σ_PN | φ_T | 2,165e-3 (8) | 2,682e-3 (8) | +23,869 % | 2,17e-3 (8) |
| σ_PN | φ_P | 1,966e-3 (8) | 2,486e-3 (8) | +26,488 % | 1,97e-3 (8) |
| σ_PN | φ_N | 2,364e-2 (3) | 2,373e-2 (3) | +0,405 % | 2,36e-2 (3) |
| σ_PN | V_vis | 1,332e-2 (3) | 7,996e-3 (4) | -39,958 % | 1,33e-2 (3) |
| c_m | φ_T | 4,452e-3 (6) | 5,164e-3 (6) | +16,011 % | 4,45e-3 (6) |
| c_m | φ_P | 4,501e-3 (6) | 5,220e-3 (6) | +15,990 % | 4,50e-3 (6) |
| c_m | φ_N | -8,462e-4 (10) | -8,828e-4 (10) | -4,332 % | -8,46e-4 (10) |
| c_m | V_vis | -2,791e-3 (8) | -2,817e-3 (8) | -0,941 % | -2,79e-3 (8) |
| ε_P | φ_T | 1,519e-2 (5) | 1,759e-2 (5) | +15,761 % | 1,52e-2 (5) |
| ε_P | φ_P | 1,537e-2 (5) | 1,779e-2 (5) | +15,736 % | 1,54e-2 (5) |
| ε_P | φ_N | -3,521e-3 (6) | -3,657e-3 (6) | -3,868 % | -3,52e-3 (6) |
| ε_P | V_vis | -1,087e-2 (4) | -1,115e-2 (2) | -2,567 % | -1,09e-2 (4) |
| c_Ψ | φ_T | -3,146e-3 (7) | -3,630e-3 (7) | -15,407 % | -3,15e-3 (7) |
| c_Ψ | φ_P | -3,183e-3 (7) | -3,673e-3 (7) | -15,375 % | -3,18e-3 (7) |
| c_Ψ | φ_N | 9,143e-4 (9) | 9,458e-4 (9) | +3,439 % | 9,14e-4 (9) |
| c_Ψ | V_vis | 2,545e-3 (9) | 2,792e-3 (9) | +9,720 % | 2,54e-3 (9) |
| κ_i | φ_T | -1,663e-3 (10) | -2,064e-3 (10) | -24,098 % | -1,66e-3 (10) |
| κ_i | φ_P | -1,515e-3 (10) | -1,919e-3 (10) | -26,659 % | -1,52e-3 (10) |
| κ_i | φ_N | -1,758e-2 (4) | -1,763e-2 (4) | -0,317 % | -1,76e-2 (4) |
| κ_i | V_vis | -9,742e-3 (5) | -5,956e-3 (6) | +38,864 % | -9,74e-3 (5) |
| α_H | φ_T | -3,640e-2 (3) | -4,097e-2 (3) | -12,535 % | -3,64e-2 (3) |
| α_H | φ_P | -3,706e-2 (3) | -4,167e-2 (3) | -12,431 % | -3,71e-2 (3) |
| α_H | φ_N | 3,445e-2 (2) | 3,462e-2 (2) | +0,501 % | 3,44e-2 (2) |
| α_H | V_vis | 1,710e-2 (2) | 9,372e-3 (3) | -45,178 % | 1,71e-2 (2) |
| α_P | φ_T | 2,144e-3 (9) | 2,618e-3 (9) | +22,082 % | 2,14e-3 (9) |
| α_P | φ_P | 1,760e-3 (9) | 2,236e-3 (9) | +27,062 % | 1,76e-3 (9) |
| α_P | φ_N | 4,353e-2 (1) | 4,370e-2 (1) | +0,391 % | 4,35e-2 (1) |
| α_P | V_vis | 2,480e-2 (1) | 1,512e-2 (1) | -39,011 % | 2,48e-2 (1) |
<!-- TABLA_H01_FIN -->
<!-- H01_RESULTADOS_FIN -->

### 4.4 Discusión

**Qué se reproduce.**
- El pipeline de simulación, el esquema numérico y el modelo PK pueden ejecutarse todavía siete años después de la versión FEniCS 2019.1 y tres años después de la publicación, siempre que se reconstruya y bloquee el entorno (§3.1).
- El código ejecutado regenera los valores de sensibilidad publicados a tres cifras significativas una vez aplicada la ec. (5).
- Es un resultado más fuerte que una «concordancia cualitativa», y localiza la discrepancia original en un único paso de posprocesado, documentado aquí.

**Qué no se reproduce.** Quien use los materiales liberados no obtendrá la Tabla 2 publicada. La discrepancia es de varios órdenes de magnitud y su tamaño varía según el parámetro, porque $\alpha$ va de $10^{-5}$ a 20. Los rangos también se desordenan, de modo que el ranking de parámetros que motiva la discusión del artículo no puede recuperarse de la salida del script. Como las formas verbal y simbólica de la ec. (5) son ambiguas en sí mismas («100 %»), recomendamos informar directamente de la elasticidad $(\partial_\alpha\bar Q/\bar Q)\,\alpha$, con unidades explícitas.

**Integridad de la configuración.** H01 muestra que reproducir los números impresos no garantiza la corrección metodológica. Los índices publicados de P2 se reproducen con precisión *precisamente porque* se ejecutó la misma configuración defectuosa.
- **Tamaño del efecto.** Corregirla desplaza los índices una mediana del 12,6 % y hasta un 45 %. Es mucho más que la concordancia del 0,45 %, a nivel de redondeo, que logra la reproducción.
- **Dónde importa.** El efecto se concentra en la cantidad observable clínicamente, el volumen visible en TC, cuyo ranking de parámetros se reordena en 7 de 11 posiciones.
- **Por qué.** El mecanismo plausible es la exposición al fármaco. Los parámetros del fármaco de P1 (dosis 0,24 g frente a 0,20 g; semivida 26,7 d frente a 22 d) aumentan la exposición al anticuerpo y reducen la masa tumoral media en torno a un 15 %. El volumen visible, definido por un umbral, responde de forma no lineal a los cambios de masa cerca del corte de visibilidad de 0,3. Este mecanismo no se aisló experimentalmente.
- **No hay que invertir ninguna conclusión.** Ningún índice cambia de signo y se conserva el parámetro principal de cada cantidad.
- **Recomendaciones para leer la tabla de los autores.** No conviene apoyarse en los rankings de los parámetros secundarios de P2, sobre todo en $V_{vis}$. Cualquier reutilización de la tabla debería acompañarse de una columna corregida.

**Implicaciones para la calibración y la optimización.**
- Los índices locales, de un parámetro cada vez y en un único punto elegido a mano, no dicen nada sobre la identificabilidad práctica.
- En P2, además, se calcularon en torno a una configuración PK incoherente.
- Por tanto, el ranking de sensibilidad no puede usarse para decidir qué parámetros calibrar o cuáles pueden fijarse.
- Una calibración por verosimilitud con perfiles de verosimilitud (§5) debe preceder a cualquier uso terapéutico.

**Limitaciones.**
- n = 2 pacientes, ambos calibrados a mano por los autores originales, así que nada de lo presentado informa sobre la validez predictiva ni la eficacia.
- Se desconocen las versiones de las bibliotecas de los autores originales. Los residuos (≤ 0,45 %) son compatibles con el redondeo por sí solo.
- La tabla publicada se contrastó con el texto extraído del artículo, no con una imagen de la página.
- Solo se auditó el modelo radial 1D.
- Aún no se ha realizado la segunda parte de la hipótesis H1 preespecificada: la verificación frente a una reimplementación independiente (error L2 ≤ 5 % en $V_{vis}$).
- Los análisis los realizaron agentes de IA bajo supervisión humana (§7.4).

---

## 5. Pipeline propuesto para la terapia personalizada

La auditoría define qué debe estar disponible antes de que el modelo pueda respaldar la **calibración farmacocinética y de los parámetros tumorales** y, más adelante, la **optimización terapéutica**.

El pipeline es una propuesta: **no se ha ejecutado ninguna de sus etapas**, y cada una requiere autorización, acuerdos de acceso a datos y criterios preespecificados.

**Figura 2 (esquema, por dibujar).** Imagen → volumetría con incertidumbre → geometría y datos PK → calibración e identificabilidad → comparación de modelos → validación fuera del periodo de ajuste → exploración de dosis con restricciones.

**Etapa 0. Base reproducible.** Cerrar las brechas de reproducción que quedan:
- una reimplementación 1D independiente, verificada frente a la original (L2 ≤ 5 % en $V_{vis}$);
- la convergencia en malla y en paso de tiempo (250/500/1000 elementos; dt = 1/12, 1/24, 1/48 d);
- una rutina de sensibilidad corregida que informe de elasticidades.

**Etapa 1. Imagen y volumetría con error de medición.** La calibración paciente a paciente necesita **TC longitudinales durante el tratamiento, con registro de dosis**, y ningún conjunto de datos público las ofrece. Las colecciones públicas cumplen papeles auxiliares:
- **LIDC-IDRI** (TC torácicas con anotaciones de nódulos por varios lectores [Armato et al. 2011]):
  - entrenamiento y evaluación comparativa de la segmentación de nódulos;
  - sobre todo, un **modelo empírico del error volumétrico entre observadores**, que aporta la varianza de medición $\sigma^2$ de la verosimilitud (Etapa 3). No es una fuente de dinámica bajo tratamiento.
- **TCGA-LUSC** (CPCNP escamoso con perfil genómico [TCGA 2012] e imagen basal en TCIA [Clark et al. 2013]):
  - distribuciones a priori de la geometría tumoral y de la heterogeneidad propia de la histología;
  - covariables genómicas para futuros modelos jerárquicos.

  No proporciona trayectorias bajo inmunoterapia.
- **Cohortes durante el tratamiento**, imprescindibles para calibrar: los datos de los autores (con permiso), datos de ensayos mediante plataformas de acceso controlado (p. ej., Vivli [Vivli], como en Ghaffari Laleh et al. 2022) o cohortes institucionales con aprobación ética.

**Etapa 2. Geometría y datos PK.**
- Primero, la geometría radial 1D. Las mallas 3D de pulmón y vasculatura específicas de cada paciente (3D Slicer [Fedorov et al. 2012] y vmtk [Antiga et al. 2008], como en el trabajo original [Wagner 2023]), solo cuando estén validados los resultados 1D.
- PK de cada fármaco a partir de la ficha técnica o de valores de PK poblacional ($t_{1/2}$, $M_\tau$, dosis y calendario), con las fechas exactas de administración.

**Etapa 3. Calibración por verosimilitud e identificabilidad.**
- Modelo de medición log-normal, $\log V_{obs}=\log V_{vis}(\theta)+\varepsilon$, $\varepsilon\sim\mathcal N(0,\sigma^2)$, con $\sigma$ informada por la Etapa 1.
- Estimación por máxima verosimilitud de $(\lambda_P^{pro},\lambda_\tau^{eff},\lambda_{PN})$ con ≥ 20 arranques múltiples, para cada $\lambda\in\{1,2\}$.
- Perfiles de verosimilitud [Raue et al. 2009]: un parámetro es identificable en la práctica si su perfil cruza $\chi^2_1(0{,}95)/2=1{,}92$ a ambos lados dentro del intervalo de búsqueda. La observación de los autores de que $\lambda_P^{pro}$ y $\lambda_\tau^{eff}$ son difíciles de determinar lleva a la hipótesis de que no son identificables conjuntamente en P2.
- Sensibilidad global (p. ej., índices de Sobol [Sobol 2001]) sobre la región calibrada, en lugar de índices locales en un único punto.

**Etapa 4. Comparación de modelos.**
- Comparadores EDO parsimoniosos con la misma PK y el mismo término Emax: crecimiento exponencial, de Gompertz [Gompertz 1825] y logístico [Verhulst 1838] con muerte por fármaco.
- Comparación mediante AICc [Hurvich & Tsai 1989] y BIC [Schwarz 1978], considerando equivalentes los modelos con $|\Delta\mathrm{AICc}|\le2$.

**Etapa 5. Validación fuera del periodo de ajuste.**
- Pronósticos con origen móvil [Tashman 2000]: calibrar hasta la TC $k$ y predecir las TC $k+1\ldots k+3$.
- Comparación pareada de los errores en log-volumen frente a los comparadores.
- Bandas de bootstrap paramétrico [Efron & Tibshirani 1993] (≥ 200 réplicas), declaradas como incertidumbre de los parámetros bajo el modelo y no como intervalos de confianza clínicos.

**Etapa 6. Exploración de dosis con restricciones.** Solo si las Etapas 3–5 tienen éxito:
- calendarios contrafactuales (dosis, intervalo, pausas de tratamiento) evaluados mediante la distribución predictiva a posteriori de $V_{vis}$, dentro de los rangos aprobados en la ficha técnica;
- los resultados siguen siendo hipótesis para contrastar de forma prospectiva, **no** recomendaciones de tratamiento.

**Gobernanza.**
- Preregistro de los criterios antes de cada etapa.
- Ejecución en contenedor y con registro, como en §3.
- Revisión independiente de cada etapa.
- Licencias claras para el código y los datos. El repositorio original no tiene licencia actualmente (§7.3).

---

## 6. Conclusiones y trabajo futuro

1. **El modelo se ejecuta y su farmacocinética es correcta.** El modelo de campo de fase de CPCNP liberado se ejecuta en un contenedor bloqueado, y su componente PK reproduce exactamente la solución analítica y la dosis total. La tolerancia preespecificada de picos y valles no se cumple por un desfase de discretización de medio subpaso.
2. **La Tabla 2 no se reproduce tal como se publicó el código.** La tabla de sensibilidad publicada no se obtiene con el script liberado (0/88). Se recupera exactamente (88/88 a tres cifras significativas, error máximo 0,449 %) con el reescalado α/100 que implica la definición verbal del artículo, y que el script omite.
3. **Un defecto de configuración afecta a P2.** Los índices de sensibilidad publicados de P2 se calcularon con simulaciones perturbadas que usan los parámetros PK del fármaco equivocado (H01). Corregirlo cambia los 44 índices una mediana del 12,6 % (hasta un 45,2 %) y reordena 7 de los 11 rangos del volumen visible, sin cambios de signo. Es un efecto relevante según los criterios preespecificados, verificado frente a un control de determinismo exacto bit a bit.
4. **La base de evidencia es escasa.** Con dos pacientes calibrados a mano, nueve discrepancias entre artículo y código e índices locales en un único punto, el modelo aún no está preparado para afirmaciones sobre calibración farmacocinética u optimización terapéutica.

**Hoja de ruta:**
- **(i)** Reimplementación independiente y estudio de convergencia.
- **(ii)** Calibración por verosimilitud con análisis de identificabilidad mediante perfiles.
- **(iii)** Comparación con modelos EDO parsimoniosos.
- **(iv)** Validación fuera del periodo de ajuste.
- **(v)** Acceso a cohortes de imagen longitudinal durante el tratamiento.
- **(vi)** Solo entonces, exploración de dosis con restricciones.

Antes de publicar, debe consultarse a los autores originales sobre la licencia del código, la reutilización de los datos, el paso α/100 y H01.

---

## 7. Declaraciones

### 7.1 Disponibilidad de datos y código

| Material | Ubicación |
|---|---|
| Nuestros envoltorios, registros y datos derivados | `Resultados/Trabajo_Claude/T01_phasefield/` y `T06_P2_H01/` |
| Revisión independiente | `Resultados/Trabajo_Cline/T03_revision_T01/` |
| Receta Docker y bloqueo de conda | `T01_phasefield/env/` |
| Código original | github.com/wagnandr/immunotherapy-lung-cancer, commit `fa8e6229` (no redistribuido; sin licencia) |

### 7.2 Ética

Los datos de los pacientes son mediciones volumétricas anonimizadas publicadas por los autores originales, con la aprobación ética BLAEK 19021 [Wagner 2023, p. 7]. Este trabajo los usó solo para reproducir resultados publicados.

### 7.3 Licencias y permisos (bloqueante para publicar)

- El repositorio original no tiene licencia. Se usó de forma privada, sin modificar y sin redistribuirlo.
- Publicar análisis derivados de los datos de los pacientes, o redistribuir código modificado, requiere el permiso de los autores.
- Existe un borrador de consulta, pero **no se ha enviado**.

### 7.4 Uso de herramientas de IA

Se usaron herramientas de IA generativa como **herramientas de asistencia**, bajo supervisión humana. No son autoras y se citan como software [Anthropic, Claude Code; Cline; OpenAI, gpt-6-astra; Microsoft, Visual Studio Code].
- **Claude Code** (Anthropic), ejecutado como extensión del entorno de desarrollo Visual Studio Code. Coordinó las tareas, ejecutó las simulaciones de T01 y T06, auditó T02 (T04, T05) y redactó los borradores de este manuscrito y de sus documentos complementarios a partir de los análisis registrados.
- **Cline** (interfaz de línea de comandos 3.0.70), con el modelo de OpenAI gpt-6-astra (proveedor `openai-codex`). Hizo la reconstrucción de ADRIATIC (T02) y la revisión independiente de T01 (T03).

**Quién manejó las herramientas.** Las herramientas de IA, el entorno de desarrollo (Visual Studio Code) y el entorno de cómputo (Docker) los manejó Wuilson Estacio.

**Verificación.** Todos los resultados se obtuvieron de ejecuciones registradas. Cline revisó los resultados de T01 de Claude Code (T03) y Claude Code auditó la reconstrucción T02 de Cline (T04, T05). Los resultados de T06 (§4.3) todavía no tienen revisión independiente, y ninguna tarea ha tenido aún una revisión humana experta. El autor es responsable del contenido.

**Pendiente.** Aún no se han verificado las políticas sobre el uso de IA de la revista de destino ni del programa de doctorado. Antes del envío, esta declaración debe adaptarse a sus requisitos.

### 7.5 Contribuciones de los autores y financiación

[PENDIENTE]

### 7.6 Documentos complementarios y mapa de la evidencia

Se indica la evidencia que aporta cada documento. Las dos líneas de trabajo se mantienen separadas: **E1** es el modelo de campo de fase de CPCNP auditado en este paper; **E2** (ADRIATIC, cáncer de pulmón de células pequeñas) es una reconstrucción de curvas de supervivencia que solo sirve para mostrar el comportamiento del protocolo de auditoría. **E2 no valida, no calibra ni respalda de ningún otro modo el modelo de E1.**

| Documento | Evidencia que aporta | Respalda |
|---|---|---|
| [METODOLOGIA_SIMULACIONES_Y_COLABORACION_IA.md](METODOLOGIA_SIMULACIONES_Y_COLABORACION_IA.md) | Qué simulaciones se ejecutaron, rotuladas como originales (código de los autores, sin modificar), variante corregida (H01) o pendientes. Datos, parámetros, versiones, entorno Docker, comandos, duraciones y resultados. Qué tareas hicieron la persona investigadora, Claude Code y Cline, cómo se delegaron mediante contratos escritos y cómo se comprobó cada entrega. Ejecuciones y pruebas fallidas, correcciones y limitaciones | §3.1, §3.3, §4.3, §7.4 |
| [INFORME_INTEGRADO_F0_F1.md](INFORME_INTEGRADO_F0_F1.md) | Resultados verificados de T01 (Tabla 2, PK, correspondencia artículo–código) y de T02/T04/T05 (ADRIATIC), cada uno con su clasificación preespecificada y su verificación independiente. Discrepancias, limitaciones, licencias y una tabla afirmación → archivo → ejecución → verificación (§10), incluida T06 | §3.2–3.4, §4.1–4.3, §6, §7.3, S2, S4 |
| [Primera_entrega_contribuciones_y_plan.md](Primera_entrega_contribuciones_y_plan.md) | El plan del 10 de octubre de 2026, escrito antes de cualquier simulación: hipótesis H1–H4, tolerancias, criterios para continuar o detenerse en cada fase y las cifras de contexto clínico (NLST, NELSON). Su sección E recoge qué se ejecutó, qué no y qué secciones del paper respalda cada parte | §1.1, §1.3, §3.2, §5 |

Las copias canónicas de los dos informes están en `Resultados/Integrado/` y `Resultados/04_plan/`. Las copias enlazadas aquí son idénticas.

**Correspondencia entre tareas y secciones** (números T como en §3.3):

| Tarea | Línea | Qué aporta | Secciones del paper |
|---|---|---|---|
| T01 | E1, código original | Verificación PK, Tabla 2 (46 simulaciones FEM, 309 min), correspondencia artículo–código | §2.3, §3.1–3.4, §4.1–4.2; Tablas 2–4; Fig. 1 |
| T03 | E1, revisión (sin simulaciones) | Recálculo independiente, alternativas de escala, comprobación de la transcripción; hallazgos H01 y H02 | §2.4, §3.3; Tabla 3 |
| T06 | E1, variante corregida | Re-simulación de P2 con H01 corregido (23 simulaciones, 184 min) más un control de determinismo (3 simulaciones) | §2.4, §3.1, §4.3; Tablas 4–5; Fig. 3 |
| T02, T04, T05 | Solo E2 | Reconstrucción de ADRIATIC y sus auditorías | Solo §3.3 (contraste del protocolo) y S2 |

### 7.7 Reutilización de material de terceros y atribución

| Material | Titular y licencia | Uso en este trabajo |
|---|---|---|
| Ecuaciones del modelo (ecs. 1–4), definición de sensibilidad (ec. 5), valores de parámetros (Tabla 1), valores de sensibilidad publicados (columnas «Publicado» de las Tablas 4–5), definición citada en §2.3 | Wagner et al. [2023], *Math. Biosci. Eng.*; CC BY 4.0 | Se reproducen con atribución en cada uso, para verificarlos, sin alterar su significado |
| Código fuente (commit `fa8e6229`) | Wagner et al. [2023, code repository]; **sin licencia** (todos los derechos reservados por defecto) | Se ejecutó de forma privada y sin modificar. No se copia ni se redistribuye. Solo se cita por archivo y número de línea |
| Datos volumétricos de los pacientes | Publicados por Wagner et al. [2023] con la aprobación ética BLAEK 19021; sin licencia de datos | Solo se usan para reproducir resultados publicados. Publicar requiere el permiso de los autores (§7.3) |
| Curvas de supervivencia de ADRIATIC | Cheng et al. [2024], *N. Engl. J. Med.*; copyright de la editorial | Se extraen datos numéricos para un análisis secundario (solo S2). No se reproduce ninguna figura del artículo original |
| Software (FEniCS/DOLFIN, PETSc, NumPy, SciPy, joblib, MPICH, conda-forge, Docker) | Sus desarrolladores, con sus licencias de código abierto | Se usan tal como se publican; se citan en las referencias |

---

## Referencias

Las referencias marcadas con † no se han cotejado con el documento original en este proyecto y deben verificarse antes del envío. Las demás se cotejaron en la base documental del proyecto, en la lista de referencias de Wagner et al. (2023) o, para los datos bibliográficos, en la página de la editorial o del archivo (13 de octubre de 2026). Se mantienen en su forma original, en inglés.

- Allen SM, Cahn JW (1979). A microscopic theory for antiphase boundary motion and its application to antiphase domain coarsening. *Acta Metall.* 27:1085–1095. †
- Alnæs MS, Blechta J, Hake J, Johansson A, Kehlet B, Logg A, Richardson C, Ring J, Rognes ME, Wells GN (2015). The FEniCS Project Version 1.5. *Arch. Numer. Softw.* 3(100):9–23. doi:10.11588/ans.2015.100.20553.
- Anthropic. Claude Code [software: AI coding agent], run as a Visual Studio Code extension. https://claude.com/claude-code (accessed October 2026).
- Antiga L, Piccinelli M, Botti L, Ene-Iordache B, Remuzzi A, Steinman DA (2008). An image-based modeling framework for patient-specific computational hemodynamics. *Med. Biol. Eng. Comput.* 46:1097–1112. †
- Armato SG III, et al. (2011). The Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI): a completed reference database of lung nodules on CT scans. *Med. Phys.* 38:915–931. †
- Balay S, et al. PETSc/TAO Users Manual. Argonne National Laboratory, ANL-21/39 (revision for the release in use; PETSc 3.25.6 used here). https://petsc.org †
- Bray F, Ferlay J, Soerjomataram I, Siegel RL, Torre LA, Jemal A (2018). Global cancer statistics 2018: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. *CA Cancer J. Clin.* 68:394–424. doi:10.3322/caac.21492.
- Cahn JW, Hilliard JE (1958). Free energy of a nonuniform system. I. Interfacial free energy. *J. Chem. Phys.* 28:258–267. †
- Cheng Y, et al. (2024). Durvalumab after chemoradiotherapy in limited-stage small-cell lung cancer. *N. Engl. J. Med.* 391:1313–1327. doi:10.1056/NEJMoa2404873.
- Clark K, et al. (2013). The Cancer Imaging Archive (TCIA): maintaining and operating a public information repository. *J. Digit. Imaging* 26:1045–1057. †
- Cline. Cline command-line interface, version 3.0.70 [software: AI coding agent]. https://cline.bot (accessed October 2026).
- conda-forge community (2015). The conda-forge Project: Community-based Software Distribution Built on the conda Package Format and Ecosystem. Zenodo. doi:10.5281/zenodo.4774216.
- Cox DR (1972). Regression models and life-tables. *J. R. Stat. Soc. B* 34:187–220. †
- Cristini V, Lowengrub J (2010). *Multiscale Modeling of Cancer.* Cambridge University Press. doi:10.1017/cbo9780511781452.
- de Koning HJ, et al. (2020). Reduced lung-cancer mortality with volume CT screening in a randomized trial. *N. Engl. J. Med.* 382:503–513. †
- Efron B, Tibshirani RJ (1993). *An Introduction to the Bootstrap.* Chapman & Hall, New York. †
- Eyre DJ (1998). Unconditionally gradient stable time marching the Cahn–Hilliard equation. *MRS Online Proc. Lib.* 529:39–46. doi:10.1557/proc-529-39.
- Fedorov A, et al. (2012). 3D Slicer as an image computing platform for the Quantitative Imaging Network. *Magn. Reson. Imaging* 30:1323–1341. †
- Frigeri S, Grasselli M, Rocca E (2015). On a diffuse interface model of tumour growth. *Eur. J. Appl. Math.* 26:215–243. doi:10.1017/s0956792514000436.
- Fritz M, Jha PK, Köppl T, Oden JT, Wohlmuth B (2021). Analysis of a new multispecies tumor growth model coupling 3D phase-fields with a 1D vascular network. *Nonlinear Anal. Real World Appl.* 61:103331. doi:10.1016/j.nonrwa.2021.103331.
- Garcke H, Lam KF, Sitka E, Styles V (2016). A Cahn–Hilliard–Darcy model for tumour growth with chemotaxis and active transport. *Math. Models Methods Appl. Sci.* 26:1095–1148. doi:10.1142/s0218202516500263.
- Ghaffari Laleh N, et al. (2022). Classical mathematical models for prediction of response to chemotherapy and immunotherapy. *PLoS Comput. Biol.* 18:e1009822. †
- Ginzburg VL, Landau LD (1950). On the theory of superconductivity. *Zh. Eksp. Teor. Fiz.* 20:1064–1082. †
- Gompertz B (1825). On the nature of the function expressive of the law of human mortality, and on a new mode of determining the value of life contingencies. *Phil. Trans. R. Soc. Lond.* 115:513–583. †
- Guyot P, Ades AE, Ouwens MJNM, Welton NJ (2012). Enhanced secondary analysis of survival data: reconstructing the data from published Kaplan–Meier survival curves. *BMC Med. Res. Methodol.* 12:9. doi:10.1186/1471-2288-12-9.
- Harris CR, et al. (2020). Array programming with NumPy. *Nature* 585:357–362. †
- Hill AV (1910). The possible effects of the aggregation of the molecules of haemoglobin on its dissociation curves. *J. Physiol.* 40(Suppl.):iv–vii. †
- Hurvich CM, Tsai CL (1989). Regression and time series model selection in small samples. *Biometrika* 76:297–307. †
- Joblib developers. joblib: running Python functions as pipeline jobs, version 1.6.0 [software]. https://joblib.readthedocs.io †
- Kaplan EL, Meier P (1958). Nonparametric estimation from incomplete observations. *J. Am. Stat. Assoc.* 53:457–481. †
- Lee HG, Kim Y, Kim J (2015). Mathematical model and its fast numerical method for the tumor growth. *Math. Biosci. Eng.* 12:1173–1187. doi:10.3934/mbe.2015.12.1173.
- Lima EABF, Oden JT, Almeida RC (2014). A hybrid ten-species phase-field model of tumor growth. *Math. Models Methods Appl. Sci.* 24:2569–2599. doi:10.1142/s0218202514500304.
- Logg A, Mardal KA, Wells G (2012). *Automated Solution of Differential Equations by the Finite Element Method: The FEniCS Book.* Springer. doi:10.1007/978-3-642-23099-8.
- Logg A, Wells GN (2010). DOLFIN: automated finite element computing. *ACM Trans. Math. Softw.* 37(2). doi:10.1145/1731022.1731030.
- Lowengrub JS, Frieboes HB, Jin F, et al. (2009). Nonlinear modelling of cancer: bridging the gap between cells and tumours. *Nonlinearity* 23:R1. doi:10.1088/0951-7715/23/1/r01.
- Merkel D (2014). Docker: lightweight Linux containers for consistent development and deployment. *Linux J.* 2014(239):2.
- Microsoft. Visual Studio Code [software: development environment]. https://code.visualstudio.com (accessed October 2026).
- MPICH. MPICH: high-performance portable MPI, version 5.0.1 [software]. https://www.mpich.org †
- National Lung Screening Trial Research Team (2011). Reduced lung-cancer mortality with low-dose computed tomographic screening. *N. Engl. J. Med.* 365:395–409. †
- OpenAI. gpt-6-astra [large language model], accessed through the provider `openai-codex` in Cline (accessed October 2026).
- Raue A, et al. (2009). Structural and practical identifiability analysis of partially observed dynamical models by exploiting the profile likelihood. *Bioinformatics* 25:1923–1929. †
- Rockne RC, Scott JG (2019). Introduction to mathematical oncology. *JCO Clin. Cancer Inform.* 3:1–4. doi:10.1200/CCI.19.00010.
- Schlicke P, Kuttler C, Schumann C (2021). How mathematical modeling could contribute to the quantification of metastatic tumor burden under therapy: insights in immunotherapeutic treatment of non-small cell lung cancer. *Theor. Biol. Med. Model.* 18:1–15.
- Schwarz G (1978). Estimating the dimension of a model. *Ann. Stat.* 6:461–464. †
- Scibilia KR, Schlicke P, Schneller F, Kuttler C (2024). Predicting resistance and pseudoprogression: are minimalistic immunoediting mathematical models capable of forecasting checkpoint inhibitor treatment outcomes in lung cancer? *Math. Biosci.* 109287. doi:10.1016/j.mbs.2024.109287. PMID 39218211.
- Sobol IM (2001). Global sensitivity indices for nonlinear mathematical models and their Monte Carlo estimates. *Math. Comput. Simul.* 55:271–280. †
- Tashman LJ (2000). Out-of-sample tests of forecasting accuracy: an analysis and review. *Int. J. Forecast.* 16:437–450. †
- The Cancer Genome Atlas Research Network (2012). Comprehensive genomic characterization of squamous cell lung cancers. *Nature* 489:519–525. †
- Verhulst PF (1838). Notice sur la loi que la population suit dans son accroissement. *Corresp. Math. Phys.* 10:113–121. †
- Virtanen P, et al. (2020). SciPy 1.0: fundamental algorithms for scientific computing in Python. *Nat. Methods* 17:261–272. †
- Vivli. Vivli – Center for Global Clinical Research Data [data-sharing platform]. https://vivli.org †
- Wagner A, Schlicke P, Fritz M, Kuttler C, Oden JT, Schumann C, Wohlmuth B (2023). A phase-field model for non-small cell lung cancer under the effects of immunotherapy. *Math. Biosci. Eng.* 20:18670–18694. doi:10.3934/mbe.2023828.
- Wagner A, Schlicke P, Fritz M, Kuttler C, Oden JT, Schumann C, Wohlmuth B (2023, preprint). A phase-field model for non-small cell lung cancer under the effects of immunotherapy. arXiv:2303.09378 (v1, 16 March 2023).
- Wagner A, et al. (2023, code repository). immunotherapy-lung-cancer [source code and patient data]. GitHub: https://github.com/wagnandr/immunotherapy-lung-cancer, commit fa8e6229d1540d33014a994f1ea309d6525597aa (14 August 2023). No licence.
- Zappa C, Mousa SA (2016). Non-small cell lung cancer: current treatment and future advances. *Transl. Lung Cancer Res.* 5. doi:10.21037/tlcr.2016.06.07.

---

## Material suplementario

- **S1. Registros de ejecución y sumas de verificación.** Véanse `T01_phasefield/logs/`, `T06_P2_H01/logs/` y las cabeceras SHA-256 de cada registro.
- **S2. Contraste del protocolo en ADRIATIC (T02/T04/T05).** Véase `Resultados/Integrado/INFORME_INTEGRADO_F0_F1.md` §3.3–3.5 y §5.2, incluida la prueba unitaria fallida (`test_e20b_all_replicates_same_truth_and_diagnostics`). Falla en 7 de 400 curvas sintéticas porque los escalones más estrechos que la precisión de las coordenadas del PDF no pueden representarse. No tiene efecto medible en ninguna métrica, y se mantuvo y declaró en lugar de modificarla a posteriori.
- **S3. Informe de revisión independiente (T03).** Véase `Resultados/Trabajo_Cline/T03_revision_T01/REVISION_T03.md`.
- **S4. Trazabilidad.** Afirmación → archivo → ejecución → verificación: `Resultados/Integrado/INFORME_INTEGRADO_F0_F1.md` §10. Para H01 (T06), véase la tabla siguiente.

| Afirmación | Fuente | Ejecución | Verificación |
|---|---|---|---|
| H01 corregido en las 22 ejecuciones perturbadas | `T06_P2_H01/data_derived/q_corr/*.json` (campos `pk_antes`/`pk_usado`) | `logs/t06_p2_h01_20261012T235219Z.log` (exit 0) | `t06_resumen.json` → `registros_q` |
| Determinismo (exacto bit a bit) | `T06_P2_H01/data_derived/control_bug_comp1.json` | `logs/t06_control_bug_20261012T231050Z.log` (exit 0) | Comparado con el registro de T01 |
| Δ_H01 de los 44 índices de P2; clase «relevante» | `T06_P2_H01/data_derived/t06_p2_indices.csv`, `t06_resumen.json` | `src/analiza_t06.py` | Criterios en `PREESPECIFICACION_T06.md` (redactado antes del lanzamiento) |
| 88 valores (P1 original, P2 corregido) | `T06_P2_H01/data_derived/t06_88_corregido.csv` | ídem | — |
| Recursos e incidencias | `T06_P2_H01/logs/docker_stats.csv`, `docker_inspect_final.txt`, `intento1_fallido_SIGBUS/` | — | — |

### S5. Reproducción paso a paso en otro equipo

Los pasos deben seguirse en orden:
- Los pasos 1–4 lo preparan todo.
- Los pasos 5–8 reproducen los resultados de este paper (línea E1).
- El paso 9 es el contraste opcional con ADRIATIC (línea E2), que no valida el modelo de E1.

**Reglas para todas las ejecuciones:**
- Nunca ejecutar a la vez las dos ejecuciones pesadas (pasos 6 y 7).
- Impedir que el equipo se suspenda mientras duran.
- Escribir siempre las ejecuciones nuevas en una carpeta aparte, nunca en las carpetas de referencia: los scripts de análisis sobrescriben sus salidas, y el lanzador del paso 7 borra y reescribe `data_derived/q_corr`.

**Shell.** Los comandos son de bash (Linux, macOS, o Windows con Git Bash). En Git Bash, anteponer `MSYS_NO_PATHCONV=1` a cada `docker run`.

**Más detalle.** `Resultados/Trabajo_Claude/T01_phasefield/REPRODUCIR.md`, `T06_P2_H01/INFORME_T06.md` §4 y el documento metodológico complementario, §6.

**Paso 0. Requisitos.**
- **Docker:** Docker Desktop en Windows y macOS, con al menos 8 CPU y unos 8 GB de memoria asignados a su máquina virtual. Las ejecuciones originales usaron 8 CPU y alcanzaron un pico de 1,4 GiB.
- **Python 3.10 fuera de Docker** para los scripts de análisis. El entorno original tenía numpy 1.26.4, matplotlib 3.10.9 y pymupdf.
- **Tiempo:** unas 9 h de cálculo en total. En el equipo original:
  - Tabla 2: 309 min;
  - control de determinismo: 37 min;
  - corrección de P2: 184 min.
- **Archivos del proyecto:** una copia de la carpeta `Resultados/` de este proyecto, con nuestros envoltorios, la receta Docker, el archivo de bloqueo, los registros de referencia y los datos derivados. El código de los autores no está incluido (paso 1).

**Paso 1. Obtener el código de los autores en el commit auditado.**
1. Descargar `github.com/wagnandr/immunotherapy-lung-cancer` en el commit `fa8e6229d1540d33014a994f1ea309d6525597aa` como zip.
2. Comprobar su SHA-256: `e45a8cd30cf57efea8980a60a952816c3a725cf3627acecadca0d41b1312acce`.
3. Descomprimirlo fuera de la carpeta del proyecto.
4. Comprobar que `reduced_models/local_sensitivity_analysis.py` tiene SHA-256 `e44eb9a974c0b8584b0f6922ee60d5b21cc0c0b9cb988d94f53dafbb5f96b3a8`. Cada registro imprime este hash en su cabecera.

El repositorio no tiene licencia: no se modifica ni se redistribuye.

**Paso 2. Crear copias de trabajo limpias.** Se copian nuestros scripts y se eliminan de las copias las salidas de referencia. La única entrada que se conserva es la tabla publicada transcrita.

```bash
P=/ruta/a/Paper_Cancer                      # copia del proyecto
REPO=/ruta/a/immunotherapy-lung-cancer-fa8e6229d1540d33014a994f1ea309d6525597aa
W=/ruta/a/reejecucion                       # carpeta nueva y vacía
REF="$P/Resultados/Trabajo_Claude"          # resultados de referencia (solo lectura)
mkdir -p "$W"
cp -r "$REF/T01_phasefield" "$W/T01"; cp -r "$REF/T06_P2_H01" "$W/T06"
cp "$REF/T01_phasefield/data_derived/tabla2_publicada.csv" "$W/"
rm -rf "$W"/T01/{data_derived,logs,figures} "$W"/T06/{data_derived,logs,figures}
mkdir -p "$W"/T01/{data_derived,logs,figures} "$W"/T06/{data_derived,logs,figures} \
         "$W"/runs_t01 "$W"/runs_t06/main/output "$W"/runs_t06/control/output
mv "$W/tabla2_publicada.csv" "$W/T01/data_derived/"
```

**Paso 3. Construir el contenedor.**

```bash
docker build -t papercancer/t01-fenics2019:1 "$W/T01/env"
docker run --rm papercancer/t01-fenics2019:1 python -c \
  "import dolfin, numpy, scipy, joblib; print(dolfin.__version__, numpy.__version__, scipy.__version__, joblib.__version__)"
```

- **Versiones esperadas:** 2019.1.0, 1.26.4, 1.15.2 y 1.6.0.
- **Paquetes fijados:** el Dockerfile solo fija python 3.10, fenics-dolfin 2019.1.0 y numpy < 2, así que una construcción posterior puede resolver otras versiones de SciPy o PETSc.
- **Conjunto exacto de paquetes:** crear el entorno a partir de `env/conda_explicit_lock.txt` (`conda create -n fx --file conda_explicit_lock.txt` dentro de un contenedor miniforge3; `REPRODUCIR.md` §1).
- **Equipos ARM** (p. ej., Apple silicon): necesitan `--platform linux/amd64`, porque el bloqueo es para linux-64.

Ni la vía del bloqueo ni la de ARM se han ejecutado en este proyecto.

**Paso 4. Prueba de humo (unos 40 s).**

```bash
docker run --rm -v "$REPO:/repo:ro" -v "$W/T01/src:/src:ro" -v "$W/T01:/out" \
  -v t01_jitcache:/root/.cache papercancer/t01-fenics2019:1 python /src/smoke_test.py --days 10
```

Escribe `logs/smoke_test.json`. En el equipo original tardó 2,24 s por día simulado en P1 y 1,01 s en P2.

**Paso 5. Farmacocinética (segundos, sin Docker).**

```bash
cd "$W/T01" && python src/pk_check.py "$REPO/reduced_models" data_derived/pk_check.json
```

Esperado (§4.1): 3 de 6 extremos dentro del 0,1 %, con errores máximos de 0,107 %, 0,129 % y 0,129 %. El resto de diagnósticos de la PK está en `REPRODUCIR.md` §3.

**Paso 6. Tabla 2 con el código original (unas 5 h).**

```bash
docker run -d --name t01_tabla2 --cpus 8 \
  -v "$REPO:/repo:ro" -v "$W/T01/src:/src:ro" -v "$W/T01:/out" -v "$W/runs_t01:/work" \
  -v t01_jitcache:/root/.cache -w /work papercancer/t01-fenics2019:1 bash /src/run_tabla2_original.sh
docker wait t01_tabla2 && docker rm t01_tabla2      # imprime el código de salida; esperado 0
cd "$W/T01"
python src/compare_tabla2.py logs/tabla2_original_*.log data_derived/tabla2_publicada.csv data_derived/tabla2
python src/diag_escala_tabla2.py data_derived/tabla2_comparacion.csv data_derived/tabla2
python src/fig_tabla2.py data_derived/tabla2_diag_escala.csv figures/fig_tabla2
```

**Esperado (§4.2):**
- salida bruta del script: 0/88 reproducidos, signos 88/88 y rangos 8/88;
- con ×α/100: 88/88 iguales a tres cifras significativas, error máximo 0,449 %.

Para comparar los índices brutos con la ejecución de referencia:

```bash
diff <(grep -o 'g_[a-z]*_list_p[12] = .*' logs/tabla2_original_*.log) \
     <(grep -o 'g_[a-z]*_list_p[12] = .*' "$REF/T01_phasefield/logs/tabla2_original_20261012T035307Z.log")
```

- **En el equipo original,** el control de determinismo (paso 7) coincidió con este registro en todas las cifras impresas.
- **En otro equipo,** pueden aparecer diferencias en las últimas cifras; no se ha verificado.

**Paso 7. P2 con H01 corregido (unas 3,7 h). Empezar solo cuando haya terminado el paso 6.**

Primero, el control de determinismo. Recalcula la componente 1 de P2 *con* el defecto original (37 min):

```bash
docker run --rm --cpus 8 --shm-size=1g -e PYTHONPATH=/repo/reduced_models:/src \
  -v "$REPO:/repo:ro" -v "$W/T06/src:/src:ro" -v "$W/T06:/out" -v "$W/runs_t06/control:/work" \
  -v t01_jitcache:/root/.cache -w /work papercancer/t01-fenics2019:1 python -u /src/control_p2_bug.py 1
```

En este proyecto el control se ejecutó dentro de `run_t06.sh`, en paralelo con el primer intento de la ejecución principal. Ejecutarlo por separado, como arriba, usa el mismo script, pero no se ha hecho así en este proyecto.

Después, la ejecución corregida:

```bash
docker run -d --name t06_p2_h01b --cpus 8 --shm-size=1g \
  -v "$REPO:/repo:ro" -v "$W/T06/src:/src:ro" -v "$W/T06:/out" -v "$W/runs_t06:/work" \
  -v t01_jitcache:/root/.cache -w /work papercancer/t01-fenics2019:1 bash /src/run_t06_main.sh
docker wait t06_p2_h01b && docker rm t06_p2_h01b    # esperado 0
```

- **`--shm-size=1g` es imprescindible.** Sin él, el primer intento falló al arrancar los workers (§3.1).
- **Reintentos automáticos:** el lanzador reintenta hasta tres veces si un worker muere al arrancar.

**Paso 8. Analizar la ejecución corregida y comparar.**

```bash
cd "$W/T06"
python -I src/analiza_t06.py "$W"/T01/logs/tabla2_original_*.log logs/t06_p2_h01_*.log \
  "$W/T01/data_derived/tabla2_publicada.csv"
```

El script escribe `data_derived/t06_resumen.json`, `t06_p2_indices.csv`, `t06_88_corregido.csv` y `figures/fig_h01.png` dentro de `$W/T06`.

**Esperado (§4.3):**
- diferencia de determinismo 0,0 en los cuatro índices;
- las 22 ejecuciones perturbadas llegan con el triplete PK por defecto y se corrigen;
- mediana |Δ| del 12,6 % y máximo del 45,2 %;
- 0 cambios de signo y 7 cambios de rango;
- clase «relevante»;
- los valores corregidos de P2 coinciden con la tabla publicada en 1/44 casos a tres cifras significativas.

**Tablas 4 y 5.** Para regenerarlas, ejecutar `python -I src/tablas_paper.py <copia del paper> "$W/T01/data_derived/tabla2_comparacion.csv" data_derived/t06_88_corregido.csv` sobre una **copia** del manuscrito. Después, comparar los bloques entre las marcas `TABLA_88` y `TABLA_H01` con los publicados aquí.

**Paso 9 (opcional; línea E2, ADRIATIC).** Seguir `Resultados/Trabajo_Cline/T02_ADRIATIC/REPRODUCIR.md` (PowerShell) en un entorno de Python 3.10 creado a partir de `requirements_T02.txt`. Antes de ejecutarlo:
- ajustar `project_root` y `python` en `config/config.yaml` al nuevo equipo;
- colocar una copia propia del PDF del artículo de NEJM en la ruta que indica el contrato de T02. El pipeline comprueba su SHA-256, y el PDF no se redistribuye.

**Esperado:**
- 18/18 cantidades preespecificadas;
- 22 de 23 pruebas correctas. La que falla es el caso conocido del límite de resolución (S2).

**Qué cambiará respecto de las ejecuciones originales:**
- los tiempos de ejecución y las marcas de tiempo;
- el ID de la imagen Docker;
- si las versiones de las bibliotecas difieren, posiblemente las últimas cifras impresas.

La referencia para juzgar una reproducción son las clasificaciones y las cifras indicadas arriba.
