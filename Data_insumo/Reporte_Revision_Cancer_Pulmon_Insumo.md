# Reporte de Investigación: Cáncer de Pulmón y Oportunidades para Modelado Computacional

**Fecha de consulta de las fuentes:** 10 de octubre de 2026  
**Propósito:** síntesis de evidencia clínica, biológica, de modelado y de datos para orientar el diseño de investigación traslacional con IA.  
**Alcance:** revisión documental de las diez fuentes indicadas. No se descargaron imágenes ni datos voluminosos.

> **Nota de uso:** este documento sirve para formular hipótesis y diseños de investigación; no es una guía clínica ni sustituye decisiones de un equipo oncológico. Las indicaciones, aprobaciones y secuencias terapéuticas dependen del estadio, biomarcadores, condición del paciente, evidencia vigente y jurisdicción.

## 1. Resumen Ejecutivo

El cáncer de pulmón continúa siendo la principal causa mundial de muerte por cáncer. La OMS estima para 2022 unos **2,5 millones de casos nuevos y 1,8 millones de muertes**. El tabaquismo sigue siendo el principal factor prevenible, aunque la exposición a humo ajeno, contaminación, radón y carcinógenos ocupacionales también contribuye. La prevención, el control del tabaco y el tamizaje de personas de alto riesgo son componentes esenciales junto con el diagnóstico y el tratamiento [1].

Alrededor del 85 % de los casos corresponde a cáncer de pulmón de células no pequeñas (NSCLC/CPCNP); el resto incluye principalmente cáncer de pulmón de células pequeñas (SCLC/CPCP), clínicamente más agresivo [1]. El tratamiento del NSCLC se ha transformado por la caracterización molecular: un panel amplio de alteraciones accionables y la evaluación de PD-L1 pueden cambiar la elección de tratamiento. Las opciones abarcan cirugía, radioterapia, quimioterapia, inmunoterapia y terapias dirigidas, solas o combinadas y según estadio [2, 3].

Las diez simulaciones del grupo CISNET son modelos poblacionales de historia natural, tabaco, detección y mortalidad: permiten comparar políticas y estrategias de tamizaje, no elegir directamente el fármaco para un paciente individual [8]. Para IA, los repositorios aportan piezas complementarias, no una cohorte multimodal ya unificada: LIDC-IDRI ofrece TAC torácica y lecturas de nódulos de 1.018 casos; TCGA-LUSC tiene 504 casos en el catálogo clínico/genómico de GDC y una colección de imágenes identificada en IDC, pero no debe suponerse que cada caso tenga imagen y ómicas completas emparejadas [9, 10].

La oportunidad de mayor valor es construir sistemas validados externamente para: (1) detección y caracterización de nódulos, (2) estimación de riesgo y evolución con datos longitudinales, y (3) predicción multimodal de respuesta o recaída, siempre con cohortes clínicas que incluyan desenlaces y tratamiento. Ni LIDC-IDRI ni TCGA-LUSC, por sí solos, bastan para entrenar y validar un predictor generalizable de respuesta a inmunoterapia.

## 2. Marco Clínico y Biológico

### 2.1 Epidemiología y factores de riesgo

- **Carga mundial:** 2,5 millones de casos nuevos y 1,8 millones de muertes estimadas en 2022; el cáncer de pulmón ocupó el primer lugar tanto en incidencia como en mortalidad por cáncer [1].
- **Prevención:** la OMS estima que más de 1,3 millones de casos en hombres y cerca de 500.000 en mujeres podrían prevenirse; la mayoría se atribuye al tabaco (60–70 %), seguido por contaminación y exposición ocupacional [1].
- **Riesgos principales:** consumo de tabaco; humo de segunda mano; contaminación del aire interior y ambiental; radón; exposiciones laborales como asbesto, sílice y emisiones de diésel; algunas neumopatías crónicas y susceptibilidad genética [1].
- **Detección:** el tamizaje con TC de baja dosis puede reducir mortalidad en grupos de alto riesgo cuando existen selección, control de calidad, lectura apropiada y seguimiento de hallazgos. No equivale a recomendar TC indiscriminada a población general [1].

Las cifras de prevención y riesgo son estimaciones poblacionales, no probabilidades individuales. Un modelo de riesgo debe registrar exposiciones con suficiente detalle (intensidad y duración del tabaquismo, años desde el abandono, edad, comorbilidades y exposición ambiental/laboral) y validar su transportabilidad geográfica.

### 2.2 Subtipos histológicos

| Grupo | Rasgos de interés para investigación |
|---|---|
| **NSCLC/CPCNP** | Aproximadamente 85 % de los casos [1]. Incluye principalmente adenocarcinoma, carcinoma escamoso y carcinoma de células grandes, además de subtipos menos frecuentes [2]. El adenocarcinoma es el subtipo con mayor frecuencia de alteraciones accionables descritas en la revisión de terapias dirigidas [4]. |
| **SCLC/CPCP** | Menos frecuente y, por lo general, de comportamiento más agresivo [1]. Es un tumor neuroendocrino de alto grado; su clasificación terapéutica suele distinguir enfermedad limitada y extensa. La evidencia del PDQ proporcionado se centra en NSCLC, por lo que no debe extrapolarse sin una revisión clínica específica de SCLC. |

El diagnóstico integra histopatología, estadio anatómico, condición clínica y biomarcadores. La TC localiza lesiones y apoya estadificación, pero no reemplaza biopsia, evaluación anatomopatológica ni pruebas moleculares cuando están indicadas [1, 2].

### 2.3 Vías moleculares, biomarcadores y terapias dirigidas

La revisión de alteraciones genómicas accionables en NSCLC avanzado no escamoso informa prevalencias aproximadas que varían por población, método de ensayo y definición de cohorte [4]. Los porcentajes no son intercambiables entre poblaciones ni se deben interpretar como prevalencia universal.

| Alteración/biomarcador | Relevancia clínica y computacional |
|---|---|
| **EGFR** | Mutaciones comunes (deleción del exón 19 y L858R) y otras variantes. Los inhibidores de tirosina cinasa (TKI), incluidos osimertinib y fármacos relacionados, se usan en enfermedad con alteración susceptible; también existen contextos adyuvantes y posquimiorradioterapia descritos por NCI [3, 4]. |
| **ALK** | Fusiones; la revisión informa alrededor de 5 % en la cohorte específica estudiada. Inhibidores como alectinib/lorlatinib; el NCI informa aprobación de alectinib adyuvante en NSCLC ALK positivo resecado [3, 4]. |
| **ROS1, RET, NTRK** | Fusiones/reordenamientos con terapias dirigidas disponibles (p. ej., inhibidores de ROS1, selpercatinib para RET y larotrectinib para NTRK, según alteración y contexto) [3, 4]. |
| **BRAF V600E** | Alteración para la que existen combinaciones BRAF/MEK (dabrafenib/trametinib; también encorafenib/binimetinib en enfermedad metastásica según NCI) [3]. |
| **MET** | El salto del exón 14 es accionable; NCI cita capmatinib y tepotinib [3, 4]. |
| **KRAS G12C** | Diana tratable con inhibidores específicos en determinados escenarios; el NCI advierte que opciones como sotorasib y adagrasib se usan tras tratamientos previos y que enlentecer progresión no implica automáticamente demostrar beneficio de supervivencia [3]. |
| **ERBB2/HER2** | Mutaciones, amplificaciones y expresión proteica son entidades distintas; deben representarse por separado en datos y modelos [4]. |
| **PD-L1** | Biomarcador complementario a pruebas moleculares, medido en tejido, que contribuye a decisiones de inmunoterapia; no es una medida equivalente a carga mutacional ni sustituye el panel genómico [4]. |

La revisión recomienda pruebas moleculares amplias en adenocarcinoma de NSCLC y en ciertos carcinomas escamosos u otros subtipos, con relevancia especial en pacientes con poca o ninguna historia tabáquica [4]. En términos de arquitectura de datos, los resultados deben conservar gen, variante, método, muestra, fecha y límites de detección; agrupar todo como “mutación positiva” perdería información accionable.

## 3. Estado del Arte en Tratamientos e Investigación Reciente

### 3.1 Tratamiento estándar: principios dependientes del estadio

La selección de tratamiento requiere histología, estadio, operabilidad, estado funcional y perfil molecular. El PDQ del NCI es una síntesis viva de evidencia; la versión para pacientes no constituye una pauta formal de decisiones [2].

- **Enfermedad temprana resecable:** cirugía (incluidas resecciones anatómicas o sublobares en pacientes seleccionados); quimioterapia y/o inmunoterapia perioperatoria o adyuvante según estadio y elegibilidad; terapia dirigida adyuvante para alteraciones específicas como EGFR o ALK en los contextos indicados. Radioterapia estereotáctica puede ser alternativa local en pacientes no candidatos a cirugía [1–3].
- **NSCLC localmente avanzado no resecable:** habitualmente quimiorradioterapia concomitante en pacientes aptos, con terapia de consolidación según biomarcadores, respuesta y elegibilidad. NCI describe resultados de osimertinib después de quimioterapia y radioterapia para NSCLC estadio III con EGFR mutado no resecable [3].
- **Enfermedad metastásica:** si existe una alteración accionable, se prioriza el tratamiento dirigido apropiado; sin una diana tratable, la inmunoterapia sola o combinada con quimioterapia se selecciona según PD-L1, histología y situación clínica. La quimioterapia basada en platino continúa siendo una plataforma importante [2–4].
- **SCLC:** la estrategia depende de enfermedad limitada/extensa. El PDQ aportado se centra en NSCLC y no es base suficiente para resumir todo el algoritmo de SCLC. Como evidencia específica adicional, ADRIATIC estudió durvalumab de consolidación tras quimiorradioterapia concurrente basada en platino en pacientes con SCLC limitado sin progresión [13]; no debe extrapolarse este resultado a enfermedad extensa ni a pacientes con progresión.
- **Cuidados de soporte y paliativos:** manejo de síntomas, toxicidades y calidad de vida forma parte de la atención en todas las etapas [1].

Las terapias dirigidas han extendido el control de enfermedad, pero la resistencia adquirida, heterogeneidad intratumoral, metástasis cerebrales y toxicidad siguen siendo problemas clínicos [4]. La revisión de organoides propone modelos derivados de pacientes para cribado farmacológico y medicina de precisión; reconoce que faltan estudios prospectivos que demuestren utilidad para decisiones clínicas [6].

### 3.2 Investigación emergente y vacíos científicos

El NCI describe investigación continua en cirugía, inmunoterapia y terapias dirigidas; destaca mejoras en terapias ALK con actividad intracraneal, uso adyuvante de terapias dirigidas, tratamiento de NSCLC con ROS1/BRAF/MET/RET/NTRK y nuevas opciones para KRAS G12C [3]. El NCI también señala que la inmunoterapia beneficia solo a una fracción de pacientes con NSCLC y que se investigan combinaciones con quimioterapia u otros fármacos, lo que refuerza la necesidad de predictores prospectivamente validados [3]. La revisión de *Nature Reviews Clinical Oncology* se titula **“The next generation of immunotherapies for lung cancers”** (2025), señalando un foco reciente en ampliar y mejorar inmunoterapias [7].

**Limitación de revisión:** la página de Nature devolvió error HTTP 406 durante esta consulta. Se verificaron metadatos bibliográficos (título, autores, volumen, páginas y fecha) mediante Crossref, pero no se pudo inspeccionar el texto completo ni atribuirle hallazgos específicos. Por tanto, aquí se usa como indicador bibliográfico de una línea de investigación, no como base para enumerar sus resultados.

Vacíos prioritarios para investigación traslacional:

1. **Resistencia y heterogeneidad:** explicar por qué lesiones y subclones con perfiles diferentes responden de modo desigual, e integrar biopsia repetida o líquida cuando esté disponible.
2. **Predicción individual de beneficio:** separar asociación pronóstica de efecto predictivo del tratamiento; para inferir beneficio terapéutico se requieren comparadores y control de confusión, idealmente datos de ensayos o diseños causales robustos.
3. **Biomarcadores de inmunoterapia:** combinar PD-L1, genómica, histología, microambiente, imagen y variables clínicas con validación en cohortes externas y diversidad poblacional.
4. **Diagnóstico temprano y sobrediagnóstico:** equilibrar sensibilidad para cáncer clínicamente relevante con falsos positivos, procedimientos innecesarios, radiación y detección de lesiones indolentes.
5. **Modelos preclínicos:** evaluar si la respuesta ex vivo en organoides se reproduce en pacientes, incluyendo limitaciones de microambiente inmune, tiempo de cultivo, tasa de establecimiento y sesgo de selección [6].
6. **Equidad y aplicabilidad:** la representación desigual por etnia, sexo, tabaquismo, sistema sanitario y centro puede degradar calibración y rendimiento fuera de la población de entrenamiento.

## 4. Modelos Existentes y Repositorios Computacionales

### 4.1 CISNET: familia de modelos de historia natural de cáncer de pulmón

CISNET reúne **diez modelos desarrollados independientemente por investigadores de ocho instituciones**. Su pregunta central es poblacional: cómo cambian incidencia y mortalidad bajo escenarios de control del tabaco, TC de baja dosis, criterios/frecuencia de tamizaje, detección y tratamiento [8].

Modelos registrados [8]:

1. BCCRI-LunCan (BC Cancer, Lung Cancer Screening Model).
2. BCCRI-Smoking (BC Cancer, Lung Cancer Smoking Model).
3. MISCAN-Lung (Erasmus Medical Center).
4. Smoking-Lung Cancer Macro Model (Georgetown University).
5. LCPM (Massachusetts General Hospital/Harvard Medical School).
6. Modelo de MD Anderson Cancer Center.
7. Modelo de Mount Sinai.
8. OncoSim-Lung (CPAC-StatCan).
9. LCOS (Stanford University).
10. YLCM (Yale University).

**Componentes metodológicos descritos por CISNET:**

- Un generador de historias de tabaquismo simula trayectorias individuales usando patrones históricos poblacionales; se apoya en fuentes como NHIS, CPS-I/II y Human Mortality Database.
- Cada modelo incorpora una relación dosis-respuesta entre historia tabáquica y riesgo. Seis modelos usan variantes del modelo mecanístico de expansión clonal en dos etapas (TSCE), con parametrizaciones distintas; otros usan módulos probabilísticos, funciones logísticas calibradas o modelos de riesgo como Bach/PLCOm2012/PLCOall2014/LCRAT.
- La progresión se representa con estados de Markov en algunos modelos y con volumen tumoral/carga metastásica en otros. Se varían supuestos por histología, estadio, tamaño, localización y sensibilidad de detección.
- Los datos de NLST y PLCO informan la historia natural y los efectos de detección. Las simulaciones permiten explorar beneficios y daños de cientos de estrategias de tamizaje, como sobrediagnóstico, cambios de estadio y mortalidad evitada [8].

**Utilidad y límites:** permiten comparar contrafactuales y apoyar políticas de tamizaje poblacional; sus estimaciones dependen de calibración, supuestos de progresión y transportabilidad de datos de EE. UU. No son modelos de visión artificial ni predictores de respuesta individual. Una línea técnica valiosa sería enlazar una estimación individual de riesgo de IA con un modelo de microsimulación poblacional, preservando por separado incertidumbre de predicción y supuestos de intervención.

## 5. Inventario de Datasets de Imágenes y Datos Ómicos (TCIA / IDC)

La consulta fue de metadatos y páginas descriptivas solamente; **no se descargaron DICOM, TAC ni archivos de imagen pesados**.

### 5.1 LIDC-IDRI (TCIA)

- **Volumen:** 1.018 casos con imágenes de TC torácica clínica [9].
- **Modalidad:** TC (CT) de tórax. El conjunto no debe describirse como colección PET/CT; la página y la descripción del artículo refieren TC.
- **Anotaciones:** archivos XML con lecturas de cuatro radiólogos torácicos expertos. El protocolo tuvo fase de lecturas independientes ciegas y fase de revisión consensuada/no ciega. Registra lesiones clasificadas como nódulos de al menos 3 mm, nódulos menores de 3 mm y lesiones no-nódulo de al menos 3 mm, además de contornos/mediciones y características anotadas [9].
- **Uso potencial:** detección, localización, segmentación y caracterización de nódulos; análisis de variabilidad interobservador y aprendizaje con etiquetas probabilísticas o consenso.
- **Limitaciones:** una anotación de nódulo no es necesariamente cáncer confirmado. La colección no ofrece por sí sola desenlaces longitudinales uniformes, tratamiento, respuesta o genómica emparejada. El desacuerdo entre lectores es información útil, no simplemente “ruido” que deba borrarse.

La página de TCIA fue accesible solo de forma limitada en la extracción de contenido, pero la descripción del conjunto y el artículo técnico asociado documentan los 1.018 casos y el procedimiento de anotación [9].

### 5.2 TCGA-LUSC en NCI Imaging Data Commons (IDC)

- **Cohorte clínica/genómica:** el catálogo del Genomic Data Commons (GDC) informa **504 casos** para el proyecto TCGA-LUSC (Lung Squamous Cell Carcinoma) y 32.404 archivos disponibles en el proyecto al momento de consulta. El número de archivos no equivale al número de imágenes ni a una cantidad uniforme de modalidades por paciente [10].
- **Imágenes en IDC:** la colección TCGA-LUSC está listada en los recursos de imágenes de TCIA/IDC y el enlace indicado apunta a un carrito/selección compartida [10]. IDC permite explorar y analizar imágenes normalizadas; su contenido incluye estudios DICOM asociados a la cohorte, cuya disponibilidad concreta depende de sujeto y versión.
- **Datos integrables:** la caracterización TCGA incluye datos clínicos y moleculares/genómicos; para vincularlos con imágenes deben verificarse identificadores de sujeto/estudio, disponibilidad y correspondencia de muestra. El uso requiere mantener la estructura de datos, la procedencia y los términos de uso aplicables.
- **Advertencia analítica:** no asumir 504 estudios radiológicos, ni emparejamiento completo entre imagen diagnóstica, tumor, ómicas y desenlace. Deben contabilizarse los casos efectivamente enlazables tras consultar los manifiestos actuales de GDC e IDC. LUSC es principalmente histología escamosa y no representa por sí sola todos los subtipos de cáncer pulmonar.

**Auditoría recomendada antes del modelado:** extraer manifiestos/metadata (sin necesidad de bajar imágenes), resumir modalidad, número de estudios/series por paciente, fechas relativas a diagnóstico/tratamiento, histología, estadio, variables moleculares, desenlaces y campos faltantes. Separar datos públicos de acceso controlado y documentar versiones y criterios de enlace. Para reproducibilidad, guardar identificadores pseudonimizados y un diccionario de variables, sin publicar información identificable.

## 6. Oportunidades para la Creación de Nuevos Modelos / Propuesta de Investigación

### 6.1 Líneas de modelos priorizadas

**A. Detección y caracterización de nódulos en TC**

- Entrenar detector 3D para proponer nódulos, con segmentación opcional y salida por lesión: localización, tamaño, probabilidad de malignidad/riesgo y nivel de incertidumbre.
- Usar LIDC-IDRI para preentrenamiento/benchmark de detección y segmentación; representar por separado lecturas individuales y consenso, y ponderar la incertidumbre entre radiólogos.
- No etiquetar automáticamente todos los nódulos LIDC como malignos/benignos: la tarea debe definirse según etiqueta real disponible (detección de lesión vs. clasificación clínica).
- Métricas: sensibilidad por escaneo a tasas de falsos positivos preespecificadas, FROC, sensibilidad por lesión, Dice/IoU para segmentación, calibración y evaluación por tamaño/localización.

**B. Riesgo de cáncer y apoyo al tamizaje**

- Integrar historia tabáquica, edad, comorbilidades y hallazgos seriados de TC para predecir riesgo absoluto a horizonte definido, progresión de nódulo o beneficio neto de seguimiento.
- Evaluar utilidad clínica con calibración, curvas de decisión y carga de falsos positivos; comparar contra criterios clínicos vigentes y modelos de riesgo establecidos.
- Vincular en una fase posterior con CISNET para simular consecuencias poblacionales bajo distintos intervalos y umbrales. Mantener explícita la incertidumbre entre el predictor individual y el modelo poblacional.

**C. Radiogenómica para histología/alteraciones accionables**

- Estudiar asociaciones entre imagen, subtipo y alteraciones (EGFR, KRAS, ALK y otras), sin presentar inferencia radiológica de genotipo como sustituto de secuenciación.
- TCGA-LUSC puede apoyar preguntas en histología escamosa y relaciones imagen-ómicamente enlazadas, solo tras verificar cantidad/calidad de pares disponibles. LIDC-IDRI no proporciona genómica clínica vinculada.
- Evaluar generalización por centro, escáner, protocolo, sexo, edad y subgrupos clínicos.

**D. Predicción de respuesta, recaída o supervivencia**

- Construir un modelo multimodal con TC basal/longitudinal, histopatología, PD-L1, genómica, tratamiento y variables clínicas. Definir desenlace con precisión (p. ej., respuesta radiológica, supervivencia libre de progresión o recurrencia a horizonte fijo).
- Para predicción de respuesta a inmunoterapia se necesitan cohortes tratadas con medición de respuesta y comparadores apropiados; LIDC-IDRI no contiene esos desenlaces y TCGA-LUSC no debe asumirse como dataset completo de tratamiento/respuesta.
- Distinguir **pronóstico** (riesgo de desenlace) de **predicción de beneficio diferencial** (quién se beneficia más con un tratamiento). Esta última requiere diseño comparativo y ajuste de confusión/selección.
- Métricas: AUROC y AUPRC para clasificación; C-index, Brier y calibración temporal para supervivencia; análisis de subgrupos y utilidad clínica, además de intervalos de confianza.

**E. Organoides para sensibilidad farmacológica**

- Vincular perfil molecular y ensayo ex vivo de organoides derivados de pacientes con respuesta clínica para construir modelos de sensibilidad o priorización de fármacos.
- Incluir controles de reproducibilidad, éxito/fallo de cultivo, tiempo hasta resultado y correspondencia temporal entre tejido, tratamiento y desenlace. La evidencia actual es prometedora como plataforma de modelado y cribado, pero aún requiere validación prospectiva para uso decisional [6].

### 6.2 Pipeline metodológico sugerido

1. **Pregunta clínica y protocolo:** especificar población, intervención/uso previsto, comparador, desenlace, horizonte temporal y umbral de decisión; elaborar protocolo previo al análisis.
2. **Inventario y permisos:** consultar metadatos y manifiestos de TCIA/IDC/GDC sin descargar todo; identificar restricciones de uso, unidades de análisis, identificadores y número real de pares enlazables.
3. **Curación de datos:** armonizar DICOM, unidades/orientación, segmentaciones, nomenclatura de mutaciones y fechas; mantener datos originales inmutables y registrar cada transformación.
4. **Etiquetado:** conservar anotaciones de cada lector y reglas de consenso; adjudicar patología/desenlace con fuente verificable; medir faltantes y error de etiqueta.
5. **Partición sin fuga:** separar entrenamiento/validación/prueba a nivel de paciente, nunca a nivel de cortes o lesiones del mismo paciente. Si hay centros, reservar al menos un centro o cohorte externa para evaluación.
6. **Modelado y baseline:** comparar baselines clínicos/tabulares con modelos de imagen y multimodales; calibrar probabilidades y estimar incertidumbre. No sobreajustar a la métrica del conjunto de prueba.
7. **Validación:** medir discriminación, calibración, robustez a escáner/protocolo, subgrupos, errores clínicamente relevantes y utilidad neta; evaluación temporal y externa antes de uso clínico.
8. **Interpretabilidad y gobernanza:** conservar trazabilidad de predicciones, control de versiones, documentación de sesgos, revisión por clínicos, vigilancia de deriva y proceso para actualización.
9. **Validación prospectiva:** evaluación silenciosa y luego estudio de impacto antes de integrar el sistema al flujo clínico. El rendimiento retrospectivo no demuestra beneficio en pacientes.

### 6.3 Diseño inicial recomendado

**Proyecto piloto:** “Detección y caracterización reproducible de nódulos pulmonares en TC con incertidumbre interobservador”.

- **Fase 1:** benchmark con LIDC-IDRI, detección de nódulos ≥3 mm y análisis de desempeño frente a cada lector y al consenso.
- **Fase 2:** validación externa en una cohorte distinta con criterios de referencia clínicos y protocolos de adquisición diversos.
- **Fase 3:** estudio de utilidad para priorización de lectura/seguimiento, con medición prospectiva de falsos positivos, tiempo, derivaciones y diagnósticos relevantes.
- **Extensión traslacional:** radiogenómica o predicción de respuesta solo después de obtener una cohorte independiente con patología, pruebas moleculares, tratamiento y desenlaces bien enlazados.

Esta secuencia aprovecha etiquetas de imagen disponibles sin confundirlas con diagnóstico oncológico ni prometer cura. Para acercarse a impacto terapéutico, la prioridad es construir conjuntos longitudinales con calidad clínica y evaluación prospectiva, además de algoritmos técnicamente sólidos.

## 7. Lectura Crítica de la Evidencia Clínica

### 7.1 Tamizaje: eficacia demostrada no equivale a programa efectivo

Los ensayos aleatorizados incluidos en la carpeta local aportan una base clínica que complementa la ficha de la OMS:

| Ensayo | Diseño y población | Resultado principal reportado | Lectura crítica |
|---|---|---|---|
| **NLST** [11] | 53.454 personas de alto riesgo en 33 centros de EE. UU.; tres rondas anuales de TC de baja dosis frente a radiografía de tórax. | 247 frente a 309 muertes por cáncer de pulmón por 100.000 personas-año; reducción relativa reportada de mortalidad de 20,0 % (IC 95 %: 6,8–26,7; p=0,004). | El comparador fue radiografía, no ausencia de tamizaje. La selección de población, umbral de positividad y manejo de falsos positivos afectan la transferibilidad. |
| **NELSON** [12] | Ensayo aleatorizado de TC volumétrica de baja dosis frente a no tamizaje en personas de alto riesgo; lectura volumétrica y seguimiento según volumen/tiempo de duplicación. | A diez años: mortalidad de 2,50 frente a 3,30 muertes por 1.000 personas-año en tamizaje/control; reducción relativa simple derivada de las tasas ≈24 %. | La población, frecuencia de rondas y protocolo difieren de NLST; la reducción calculada a partir de tasas no sustituye al estimador primario del ensayo. Su estrategia volumétrica pone de relieve el valor de seguimiento longitudinal, no solo clasificación de una TC aislada. |

La consecuencia para un producto de IA es doble. Primero, el endpoint clínicamente valioso no es “detectar más nódulos”, sino reducir mortalidad o enfermedad avanzada con balance favorable entre beneficio y daño. Segundo, una herramienta de lectura debe evaluarse junto con el protocolo de seguimiento: tasa de falsos positivos, procedimientos invasivos, cánceres de intervalo, cánceres indolentes detectados, tiempo de diagnóstico y diferencias por subgrupos. Un AUROC alto, por sí solo, no demuestra que el tamizaje asistido mejore desenlaces.

### 7.2 Inmunoterapia en SCLC limitado: evidencia clínica específica

El ensayo fase III ADRIATIC evaluó durvalumab (con o sin tremelimumab) frente a placebo después de quimiorradioterapia concurrente basada en platino en SCLC de estadio limitado sin progresión. En el análisis interino publicado, durvalumab se asoció con mediana de supervivencia global de **55,9 frente a 33,4 meses** (HR de muerte 0,73; IC 98,321 %: 0,54–0,98; p=0,01) y mediana de supervivencia libre de progresión de **16,6 frente a 9,2 meses** (HR 0,76; IC 97,195 %: 0,59–0,98; p=0,02) [13].

Este hallazgo es una señal terapéutica relevante, pero su población es concreta: pacientes con SCLC limitado que completaron quimiorradioterapia y no progresaron. No se debe extrapolar a NSCLC, SCLC extenso, pacientes que progresan durante quimiorradioterapia ni a predicción individual basada en imágenes sin validación. Para un proyecto de IA, ADRIATIC ejemplifica por qué deben conservarse línea y secuencia de tratamiento, estado de enfermedad al inicio de consolidación, elegibilidad y censura temporal en vez de codificar solamente “recibió inmunoterapia”.

### 7.3 Fuerza y límites del conjunto de fuentes

- Las fichas de OMS y NCI son síntesis institucionales útiles para panorama y opciones terapéuticas; no reemplazan la consulta de guías clínicas locales ni del protocolo completo del ensayo.
- Los ensayos NLST, NELSON y ADRIATIC permiten afirmaciones de eficacia causal en las poblaciones aleatorizadas estudiadas; sus estimadores no son directamente comparables si cambian el comparador, elegibilidad, endpoint o seguimiento.
- Las revisiones de alteraciones moleculares, organoides e inmunoterapia resumen literatura, pero no son ensayos de efectividad de una nueva herramienta de IA [4, 6, 7, 14].
- Las publicaciones de modelos mecanísticos/digital twins son evidencia de factibilidad metodológica. Un ajuste retrospectivo, una simulación o dos ejemplos clínicos no equivalen a validación prospectiva, utilidad clínica ni aprobación regulatoria [15–19].
- Esta revisión no es una revisión sistemática: las fuentes fueron preseleccionadas por el solicitante y no hubo protocolo de búsqueda exhaustiva, deduplicación, evaluación formal del riesgo de sesgo ni metaanálisis. Las conclusiones son de síntesis orientadora y las limitaciones de acceso están declaradas.

## 8. Modelado Computacional: De la Simulación Tumoral al Modelo Poblacional

Los modelos de la carpeta local muestran escalas y objetivos distintos. Es importante no llamar “IA clínica” a todo modelo matemático ni confundir una simulación mecanística con un predictor entrenado en una cohorte.

| Familia y fuente | Unidad/escala y método | Aporte potencial | Madurez/limitación para traducción |
|---|---|---|---|
| **CISNET** [8] | Individuo y población; historia de tabaquismo, riesgo, historia natural, detección, estadio y mortalidad mediante microsimulación/modelos de estados, dosis-respuesta mecanística o funciones de riesgo. | Comparar escenarios contrafactuales de prevención y tamizaje; cuantificar beneficios y daños a largo plazo. | Resultados dependen de calibración, supuestos y poblaciones principalmente estadounidenses. No predice respuesta farmacológica de un individuo ni lee imágenes. |
| **ODE/PDE y modelos híbridos** [15] | Dinámica temporal agregada mediante ecuaciones diferenciales ordinarias (ODE); distribución espacial y gradientes con ecuaciones en derivadas parciales (PDE); acoplamiento con farmacocinética/farmacodinámica o biología celular. | Interpretar cinética tumoral, heterogeneidad espacial y relación entre tratamiento y crecimiento; producir hipótesis mecanísticas. | La elección de estructura y parámetros puede no ser identificable a partir de mediciones clínicas escasas; requiere calibración, análisis de sensibilidad e incertidumbre. |
| **Agente-based multiescala** [17] | Células como agentes discretos acoplados a señalización intracelular EGFR–ERK y estímulos espaciales; el artículo de Wang et al. reporta un esquema 2D. | Representar heterogeneidad, migración y respuesta emergente que un modelo agregado puede ocultar. | Es un modelo mecanístico temprano, no una herramienta validada en cohortes prospectivas ni una prueba de que el fenotipo simulado anticipe desenlaces clínicos. |
| **Phase-field para NSCLC e inmunoterapia** [16] | Formulación determinista basada en Cahn–Hilliard para evolución espacial de células tumorales proliferativas y necróticas; el trabajo explora dos pacientes tratados con inmunoterapia. | Probar cómo incorporar forma/espacio tumoral y mediciones seriadas a un modelo de crecimiento bajo tratamiento. | Demostración exploratoria. N pequeño, supuestos simplificados y dependencia de datos longitudinales; no demuestra superioridad sobre modelos simples ni beneficio clínico. |
| **Modelos SCLC deterministas/estocásticos** [18] | Marcos conceptuales que combinan dinámica clonal, mutación/deriva y selección, además de capas genómicas y fenotípicas. | Organizar hipótesis sobre heterogeneidad, evolución clonal y biomarcadores en una enfermedad agresiva. | Revisión/modelado conceptual; exige datos longitudinales y perturbaciones experimentales para discriminar mecanismos alternativos. |
| **Hipermodelo/digital twin** [19] | Arquitectura modular que propone acoplar cinética celular, metabolismo, señalización y biomecánica con datos ómicos, clínicos e imágenes. | Reutilizar componentes e integrar escalas para simulación individual. | “Digital twin” describe la arquitectura aspiracional, no validación clínica. Requiere estandarización de interfaces, observabilidad de parámetros, actualización temporal y evaluación prospectiva. |
| **Organoides derivados de paciente** [6, 14] | Modelo ex vivo tridimensional; ensayos farmacológicos asociados a tejido tumoral y perfil molecular. | Cribado de combinaciones y puente entre biología tumoral y respuesta a fármacos. | No reproduce completamente sistema inmune, vasculatura ni microambiente; hay sesgo por éxito de cultivo, tiempo y selección. Debe correlacionarse prospectivamente con respuesta real. |

### 8.1 Oportunidad de integración sin “caja negra”

Una arquitectura de investigación factible sería una **cadena de modelos con responsabilidades explícitas**, no un único sistema monolítico:

1. **Percepción de imagen:** segmenta tumor/nódulo y calcula rasgos con incertidumbre.
2. **Estado clínico-molecular:** representa histología, estadio, variantes, biomarcadores, tratamiento y comorbilidad.
3. **Modelo temporal:** estima trayectoria observada y distribuciones de desenlace; puede incorporar un modelo mecanístico o survival ML.
4. **Simulación de política:** alimenta escenarios de umbral y frecuencia de seguimiento a modelos poblacionales tipo CISNET.
5. **Evaluación de utilidad:** compara decisiones sugeridas frente a práctica habitual, considerando daños, recursos y equidad.

La imagen debe actuar como medición y no como sustituto automático del mecanismo biológico. Si un modelo predice respuesta a tratamiento, el diseño debe separar el riesgo basal del efecto diferencial del tratamiento; si predice crecimiento, debe distinguir incertidumbre de segmentación, de parámetros y del modelo estructural.

## 9. Propuesta de Investigación Traslacional

### 9.1 Proyecto recomendado

**Título de trabajo:** *Modelo multimodal, calibrado y externo de caracterización longitudinal de nódulos pulmonares para priorización de seguimiento en TC de baja dosis*.

**Justificación:** LIDC-IDRI tiene anotaciones multilector útiles para detección/localización, mientras que los ensayos de tamizaje indican que el beneficio poblacional depende del protocolo y del seguimiento, no solo de la detección [9, 11, 12]. Ninguna de esas piezas proporciona por sí misma el desenlace clínico longitudinal necesario para estimar riesgo real; por tanto, el proyecto tiene dos fases y no atribuye diagnóstico maligno a las etiquetas de nódulo del repositorio.

### 9.2 Pregunta, hipótesis y objetivos

- **Pregunta:** en adultos con nódulos pulmonares detectados por TC de baja dosis, ¿añadir características de imagen longitudinales y predicción calibrada a variables clínicas mejora la priorización de seguimiento frente al protocolo clínico estándar sin aumentar procedimientos innecesarios?
- **Hipótesis primaria:** incorporar cambio longitudinal del nódulo (volumen, morfología y crecimiento) a factores clínicos mejora la calibración y utilidad neta para identificar cáncer clínicamente relevante a un horizonte predefinido, comparado con imagen basal y reglas clínicas.
- **Objetivo técnico 1:** desarrollar y validar detección/segmentación y seguimiento de lesión con LIDC-IDRI, preservando las lecturas separadas de los radiólogos.
- **Objetivo clínico 2:** desarrollar predictor de riesgo en una cohorte externa con resultados diagnósticos longitudinales y variables clínicas, sin usar LIDC-IDRI como fuente de etiqueta de cáncer confirmado.
- **Objetivo de impacto 3:** evaluar retrospectivamente si una estrategia asistida podría reducir falsos positivos/procedimientos sin elevar cánceres de intervalo; posteriormente, realizar validación prospectiva silenciosa antes de cualquier intervención.

### 9.3 Diseño y población

1. **Fase técnica retrospectiva:** pacientes/casos del repositorio LIDC-IDRI; unidad primaria paciente/TC y unidad secundaria lesión. Tarea primaria: detección/localización de nódulos ≥3 mm según anotaciones disponibles. Evaluación de segmentación solo en lesiones con contornos elegibles y definición explícita de consenso.
2. **Fase de validación clínica externa:** cohorte institucional o multicéntrica de TC de baja dosis con adjudicación clínica/patológica, fecha de exploración, historia tabáquica, seguimiento y desenlaces. Inclusión, exclusión y horizonte de predicción se definirán antes de observar resultados. Esta cohorte no está contenida en los datasets revisados y requerirá aprobación ética, acuerdos de datos y cálculo formal del tamaño muestral.
3. **Población objetivo:** grupo elegible para evaluación de nódulos/tamizaje bajo criterios clínicos locales. No entrenar ni desplegar sobre población general a partir de cohortes enriquecidas en cáncer.
4. **Comparadores:** (a) protocolo clínico vigente; (b) modelo tabular clínico; (c) modelo de imagen basal; (d) modelo multimodal longitudinal. Registrar explícitamente decisiones, intervenciones y cambios de protocolo.

### 9.4 Variables y desenlaces

| Dominio | Variables mínimas |
|---|---|
| Paciente | Edad, sexo, consumo de tabaco (paquetes-año, estado actual/previo, fecha de abandono), comorbilidad pulmonar y factores de riesgo disponibles. |
| Imagen | TC DICOM, fabricante/protocolo, grosor de corte, dosis si disponible, segmentación por lesión, localización, volumen/diámetro, densidad/subtipo radiológico y evolución temporal. |
| Referencia diagnóstica | Histopatología y subtipo cuando exista; diagnóstico clínico adjudicado; benignidad solo con estándar/seguimiento preespecificado, no por ausencia de registro. |
| Proceso asistencial | Recomendación, intervalo de control, pruebas adicionales, biopsia/cirugía, complicaciones y tiempo a diagnóstico. |
| Desenlace primario propuesto | Cáncer de pulmón clínicamente relevante confirmado dentro de horizonte temporal predefinido, con protocolo de adjudicación y censura establecido antes del análisis. |
| Desenlaces de balance | Falsos positivos, procedimientos invasivos sin cáncer, cánceres de intervalo, sobrediagnóstico si es estimable, retraso diagnóstico, radiación acumulada y desigualdad de rendimiento. |

**Definición de “clínicamente relevante”:** debe acordarse con oncología, radiología, neumología y pacientes; no es intercambiable con cualquier nódulo anotado ni con todo cáncer detectado por tamizaje.

### 9.5 Plan analítico y criterios de éxito

- **Partición:** dividir por paciente y, en la fase clínica, preferir validación temporal y por centro. Ningún corte, serie, lesión o visita de un paciente puede aparecer simultáneamente en entrenamiento y prueba. Aplicar control explícito de fuga por identificador, fechas, duplicados y preprocesamiento.
- **Detección:** FROC/sensibilidad por TC a tasas preespecificadas de falsos positivos; sensibilidad por lesión con estratos de tamaño y densidad. Reportar rango de lectores/consenso, no solo una etiqueta fusionada.
- **Segmentación:** Dice/IoU como métricas técnicas secundarias, junto con error de volumen y repetibilidad interobservador; una buena superposición geométrica no garantiza buena decisión clínica.
- **Riesgo:** AUROC y AUPRC si clasificación; calibración en el horizonte clínico, Brier, sensibilidad/especificidad en umbral operativo y curvas de decisión. Para supervivencia: C-index/time-dependent AUC, Brier dependiente del tiempo, Kaplan–Meier por grupos solo como análisis descriptivo.
- **Comparación:** evaluar mejora frente a protocolo y baseline en calibración, beneficio neto y carga asistencial; informar intervalos de confianza por bootstrap agrupado por paciente/centro.
- **Muestreo y potencia:** calcular tamaño muestral a partir de incidencia de evento, prevalencia, horizonte, número de parámetros, precisión de calibración y diferencias de utilidad clínicamente relevantes. No usar reglas genéricas de “80/20” como justificación de potencia.
- **Subgrupos:** medir calibración y error por sexo, edad, tabaquismo, centro, equipo/protocolo y subtipos de nódulo; evaluar si los cambios observados son compatibles con tamaño de muestra suficiente.
- **Incertidumbre:** separar incertidumbre aleatoria (variabilidad/ruido de lectura) de incertidumbre epistémica (modelo fuera de distribución). Definir abstención o revisión humana para casos de baja confianza.
- **Éxito:** desempeño externo calibrado y beneficio neto en umbrales elegidos por clínicos antes del análisis, sin deterioro significativo en subgrupos ni incremento inaceptable de procedimientos; si no se cumplen criterios, el resultado válido puede ser no desplegar.

### 9.6 Amenazas a validez y mitigaciones

| Amenaza | Ejemplo | Mitigación |
|---|---|---|
| Fuga de datos | Cortes del mismo CT repartidos entre train/test o series posteriores en entrenamiento y basal en prueba. | Partición por paciente y temporal; auditoría de IDs/fechas y pipeline completo dentro de cada fold. |
| Sesgo de espectro | Cohorte de casos de cáncer confirmados frente a controles sanos fáciles. | Cohorte consecutiva de práctica real, con espectro de benignidad, nódulos indeterminados y comorbilidad. |
| Sesgo de verificación | Biopsia disponible solo en sospechosos; benignidad asignada por falta de seguimiento. | Definir referencia compuesta y duración de seguimiento; modelar censura/faltantes. |
| Confusión por tratamiento | Pacientes de alto riesgo reciben más pruebas/tratamiento. | Emular diseño objetivo; registrar indicación/tiempo y separar pronóstico de estimación causal del efecto terapéutico. |
| Dominio/escáner | El modelo aprende fabricante, reconstrucción o centro en lugar de señal tumoral. | Validación externa, armonización documentada, prueba leave-one-site-out y análisis de desempeño por dominio. |
| Etiquetas ruidosas | Lectores discrepan; “consenso” suprime incertidumbre. | Conservar anotaciones individuales, modelar desacuerdo y análisis de sensibilidad frente a distintas reglas de consenso. |
| Desbalance/desenlace raro | Alta exactitud aparente por predecir benignidad. | AUPRC, calibración, utilidad y reporte de sensibilidad en umbrales clínicos, no accuracy aislada. |
| Cambios temporales | Nuevos criterios, terapias o protocolos tras la cohorte histórica. | Validación temporal, monitorización de deriva y revalidación antes de actualización. |

### 9.7 Ruta de ejecución y decisiones de avance

| Etapa | Entregable | Criterio de avance |
|---|---|---|
| 0. Factibilidad | Inventario de metadatos, cohortes disponibles, permisos, números enlazables y protocolo de desenlace. | Existe una cohorte externa con seguimiento suficiente y referencia diagnóstica auditable. |
| 1. Benchmark | Detector/segmentador reproducible en LIDC-IDRI y análisis de lector/incertidumbre. | Rendimiento por lesión aceptable en umbral clínico acordado; ausencia de fuga; inferencia replicable. |
| 2. Validación externa | Predictor longitudinal clínico-imagen en cohortes separadas temporal y geográficamente. | Calibración y beneficio neto reproducidos; análisis de subgrupos sin señal de daño no mitigado. |
| 3. Evaluación silenciosa | Predicciones sin influir en atención real, comparación con proceso estándar. | Flujo técnico seguro, tasa de alertas viable y concordancia prospectiva. |
| 4. Estudio de impacto | Ensayo pragmático o estudio prospectivo de implementación aprobado. | Evidencia de mejor proceso o desenlace con balance beneficio/daño y supervisión ética/regulatoria. |

No se fija un calendario ni un número de pacientes artificial: ambos dependen de disponibilidad de cohorte, prevalencia del desenlace, tasa de seguimiento y recursos de adjudicación.

## 10. Arquitectura de Datos, Ética y Gobernanza

### 10.1 Modelo relacional mínimo

Organizar los datos mediante entidades separadas y claves pseudonimizadas:

`paciente → episodio clínico → estudio de imagen → serie → lesión → anotación/segmentación → muestra → ensayo molecular → tratamiento → evaluación de respuesta → desenlace`.

Cada elemento debe llevar fuente, fecha, unidad, versión, estado de calidad y relación de procedencia. Una persona puede tener múltiples estudios, lesiones, biopsias y tratamientos; aplanar todo en una fila puede mezclar temporalidades o enlazar una muestra con la lesión equivocada.

### 10.2 Controles indispensables

- Validar deidentificación de encabezados DICOM y de metadatos derivados; recordar que fechas y combinaciones raras pueden reidentificar indirectamente.
- Determinar condiciones de acceso/uso para GDC, IDC, TCIA y datos clínicos institucionales; no asumir que “público” significa libre de obligaciones.
- Limitar acceso por rol, mantener registro de consultas y separar llave de reidentificación en entorno controlado.
- Documentar licencias, procedencia, versiones, transformaciones y criterios de exclusión. Mantener manifiesto y hash de archivos, no copias duplicadas sin control.
- Presentar el proyecto a revisión ética y privacidad local; clasificar el sistema según su uso previsto y verificar requisitos regulatorios antes de uso clínico.
- Incluir oncología, radiología torácica, patología, estadística, informática clínica, pacientes y responsables de privacidad desde diseño hasta comunicación de resultados.
- Preparar un model card/protocolo público que declare población, centro, protocolo de TC, etiqueta objetivo, horizonte, fallos conocidos, incertidumbre y usos no previstos.

## Referencias y trazabilidad de fuentes

1. **OMS.** Cáncer de pulmón: datos y estadísticas. https://www.who.int/es/news-room/fact-sheets/detail/lung-cancer  
2. **National Cancer Institute (NCI).** Tratamiento del cáncer de pulmón de células no pequeñas (PDQ), versión para pacientes; consulta adicional de la sección especificada. https://www.cancer.gov/espanol/tipos/pulmon/paciente/tratamiento-pulmon-celulas-no-pequenas-pdq  
   Sección solicitada: https://www.cancer.gov/espanol/tipos/pulmon/paciente/tratamiento-pulmon-celulas-no-pequenas-pdq#_164  
   Versión técnica para profesionales, consultada para contexto de tratamiento: https://www.cancer.gov/types/lung/hp/non-small-cell-lung-treatment-pdq  
3. **NCI.** Lung Cancer Research. https://www.cancer.gov/types/lung/research  
4. Bouchard N, Daaboul N. *Lung Cancer: Targeted Therapy in 2025.* Current Oncology. 2025;32:146. DOI: 10.3390/curroncol32030146. PMCID: PMC11941068. https://pmc.ncbi.nlm.nih.gov/articles/PMC11941068/  
5. **NCI PDQ.** La URL corresponde a la sección solicitada del mismo resumen listado en la referencia 2; no se contabiliza como una fuente clínica independiente. https://www.cancer.gov/espanol/tipos/pulmon/paciente/tratamiento-pulmon-celulas-no-pequenas-pdq#_164  
6. **Revisión de organoides derivados de pacientes con cáncer pulmonar.** PMCID: PMC10698950. https://pmc.ncbi.nlm.nih.gov/articles/PMC10698950/  
7. Zhao S, Zhao H, Yang W, Zhang L. *The next generation of immunotherapies for lung cancers.* Nature Reviews Clinical Oncology. 2025;22:592–616. DOI: 10.1038/s41571-025-01035-9. https://www.nature.com/articles/s41571-025-01035-9  
   **Trazabilidad:** la página del editor devolvió HTTP 406 en esta revisión; los metadatos bibliográficos se verificaron vía https://api.crossref.org/works/10.1038/s41571-025-01035-9. No se atribuyen aquí detalles del texto no accesible.
8. **CISNET.** Lung Model Registry. https://cisnet.cancer.gov/resources/model-registry/lung-models/  
9. **The Cancer Imaging Archive (TCIA).** LIDC-IDRI; incluye enlace y documentación del conjunto. Artículo técnico del consorcio: https://doi.org/10.1118/1.3528204. Página de colección: https://www.cancerimagingarchive.net/collection/lidc-idri/  
10. **NCI Imaging Data Commons (IDC), TCGA-LUSC** (selección compartida indicada) y **Genomic Data Commons (GDC), resumen del proyecto TCGA-LUSC**. https://portal.imaging.datacommons.cancer.gov/explore/?shared_cart=doiJNLP-TCGA-LUSC-01-30-2017 ; https://api.gdc.cancer.gov/projects/TCGA-LUSC?expand=summary
11. National Lung Screening Trial Research Team. *Reduced Lung-Cancer Mortality with Low-Dose Computed Tomographic Screening.* N Engl J Med. 2011;365:395–409. DOI: 10.1056/NEJMoa1102873. https://doi.org/10.1056/NEJMoa1102873
12. de Koning HJ, van der Aalst CM, de Jong PA, et al. *Reduced Lung-Cancer Mortality with Volume CT Screening in a Randomized Trial.* N Engl J Med. 2020;382:503–513. DOI: 10.1056/NEJMoa1911793. https://doi.org/10.1056/NEJMoa1911793
13. Cheng Y, et al. *Durvalumab after Chemoradiotherapy in Limited-Stage Small-Cell Lung Cancer (ADRIATIC).* N Engl J Med. 2024;391:1313–1327. DOI: 10.1056/NEJMoa2404873. https://doi.org/10.1056/NEJMoa2404873
14. Li Y, et al. *Applications of lung cancer organoids in precision medicine and drug testing.* Cell Communication and Signaling. 2023;21:350. DOI: 10.1186/s12964-023-01332-9. https://doi.org/10.1186/s12964-023-01332-9. Corresponde al artículo científico de la referencia 6.
15. Smieja J. *Mathematical Modeling Support for Lung Cancer Therapy—A Short Review.* Int J Mol Sci. 2023;24:14516. DOI: 10.3390/ijms241914516. https://doi.org/10.3390/ijms241914516
16. Wagner A, Schlicke P, Fritz M, et al. *A phase-field model for non-small cell lung cancer under the effects of immunotherapy.* Mathematical Biosciences and Engineering. 2023;20:18670–18694. DOI: 10.3934/mbe.2023828. https://doi.org/10.3934/mbe.2023828
17. Wang Z, Zhang L, Sagotsky J, Deisboeck TS. *Simulating non-small cell lung cancer with a multiscale agent-based model.* Theoretical Biology and Medical Modelling. 2007;4:50. DOI: 10.1186/1742-4682-4-50. https://doi.org/10.1186/1742-4682-4-50
18. Salgia R, Mambetsariev I, Hewelt B, et al. *Modeling small cell lung cancer (SCLC) biology through deterministic and stochastic mathematical models.* Oncotarget. 2018;9:26226–26242. https://doi.org/10.18632/oncotarget.25330
19. Kolokotroni E, Abler D, Ghosh A, et al. *A Multidisciplinary Hyper-Modeling Scheme in Personalized In Silico Oncology: Coupling Cell Kinetics with Metabolism, Signaling Networks, and Biomechanics as Plug-In Component Models of a Cancer Digital Twin.* J Pers Med. 2024;14:475. DOI: 10.3390/jpm14050475. https://doi.org/10.3390/jpm14050475

### Nota de los archivos locales revisados

Además de las diez URLs solicitadas, se leyeron los artículos PDF que ya estaban en `Data_insumo`. Las referencias 11–19 identifican los documentos adicionales usados para profundizar tamizaje, SCLC, organoides y modelado. No se descargaron nuevos PDF o imágenes para esta revisión.
