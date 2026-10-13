# Ficha D04 — ADRIATIC (durvalumab tras quimiorradioterapia en CPCP de estadio limitado)

> Convenciones. Las ubicaciones usan la paginación del PDF (1–15) y, entre llaves, la paginación de la revista (1313–1327): por ejemplo, [p. 7 {1319}].
> «No reportado» significa que el dato no está en el artículo principal. El Apéndice Suplementario (Fig. S1–S5, Tablas S1–S6, protocolo) **no** está en los insumos y no se consultó.
> Todo lo marcado **[Evaluación del lector]** es interpretación propia y no una afirmación del artículo.

## 0. Verificación realizada

| Elemento | Fuente usada | Verificación visual |
|---|---|---|
| Texto completo (15 págs.) | `00_extraccion_texto/Durvalumab-after-...txt` | — |
| Tabla 1 (características basales) | PDF p. 5 {1317} | **Sí**, renderizada a 110 dpi |
| Figura 1A (KM SG) + números en riesgo | PDF p. 6 {1318} | **Sí**, renderizada a 220 dpi. Además, extraje las palabras con sus coordenadas desde la capa de texto del PDF (PyMuPDF): coinciden al 100 % |
| Figura 1B (forest SG) | PDF p. 6 {1318} | **Sí**, a 170 dpi |
| Figura 2A (KM SLP) + números en riesgo | PDF p. 8 {1320} | **Sí**, a 220 dpi y con coordenadas: coinciden al 100 % |
| Figura 2B (forest SLP) | PDF p. 8 {1320} | **Sí**, a 170 dpi |
| Tabla 2 (respuestas) | PDF p. 10 {1322} | Solo texto extraído (orden lineal coherente) |
| Tabla 3 (eventos adversos) | PDF p. 12 {1324} | **Sí**, a 110 dpi |

Integridad del insumo: SHA-256 `44b9eb70e00ad09bd8d80c014b585dd85f6a2a8f1ac1e6b8bdd3d68503234d0c`, 15 páginas, sin páginas escaneadas (todas tienen capa de texto; `_reporte_extraccion.json`).

---

## 1. Referencia y versión

- Cheng Y, Spigel DR, Cho BC, Laktionov KK, Fang J, Chen Y, Zenke Y, Lee KH, Wang Q, Navarro A, Bernabe R, Buchmeier EL, Chang JW-C, Shiraishi Y, Goksu SS, Badzio A, Shi A, Daniel DB, Hoa NTT, Zemanova M, Mann H, Gowda H, Jiang H, Senan S, for the ADRIATIC Investigators. *Durvalumab after Chemoradiotherapy in Limited-Stage Small-Cell Lung Cancer.* N Engl J Med 2024;391(14):1313-27. DOI: 10.1056/NEJMoa2404873 [p. 1 {1313}].
- Versión: publicado en línea en NEJM.org el 13 de septiembre de 2024; número impreso del 10 de octubre de 2024 [p. 1]. El PDF se descargó de nejm.org el 14 de octubre de 2024 (pie de página).
- Registro: NCT03703297. Financiación: AstraZeneca [p. 1]. El patrocinador diseñó el ensayo y analizó los datos; la redacción médica, incluido el primer borrador, la financió el patrocinador [p. 3 {1315}].
- Contacto: S. Senan (Amsterdam UMC) [p. 1].
- Se trata del **primer análisis intermedio planificado** de SG y SLP. Los resultados del brazo durvalumab + tremelimumab siguen cegados [p. 1, p. 2].

## 2. Diseño

| Ítem | Dato | Ubicación |
|---|---|---|
| Tipo | Fase 3, multicéntrico, doble ciego, aleatorizado, controlado con placebo, en curso | [p. 2 {1314}] |
| Aleatorización | Inicialmente **1:1:1** (D : D+T : placebo). Tras una enmienda en **noviembre de 2020** pasó a **1:1** (D : placebo) | [p. 2–3] |
| Brazo D (durvalumab) | Durvalumab 1500 mg + placebo de tremelimumab cada 4 semanas × 4 dosis; después, durvalumab 1500 mg cada 4 semanas | [p. 2] |
| Brazo D+T | Durvalumab 1500 mg + tremelimumab 75 mg cada 4 semanas × 4 dosis; después, durvalumab 1500 mg cada 4 semanas | [p. 2] |
| Brazo placebo | Placebo de durvalumab + placebo de tremelimumab cada 4 semanas × 4; después, placebo de durvalumab cada 4 semanas | [p. 2–3] |
| Vía | Intravenosa (todos los fármacos y placebos) | [p. 3] |
| Duración | Máximo 24 meses, o hasta progresión determinada por el investigador, toxicidad inaceptable o retirada del consentimiento | [p. 3] |
| Ventana | Aleatorización dentro de los 42 días siguientes al fin de la QRT | [p. 3] |
| Estratificación | Estadio (I o II frente a III) y PCI (sí frente a no) | [p. 1, p. 3] |
| Inclusión: histología/estadio | CPCP de estadio limitado confirmado por histología o citología; estadio I, II o III (AJCC 8.ª ed. / IASLC). En estadio I–II, enfermedad médicamente inoperable | [p. 2] |
| Inclusión: QRT | Sin progresión tras QRT concurrente definitiva con platino. «Concurrente» significa que la RT debía empezar antes del final del ciclo 2 de QT (detalles en la Fig. S1, no disponible) | [p. 2] |
| Inclusión: PCI | PCI tras la QRT y antes de aleatorizar, a criterio del investigador (opcional) | [p. 2] |
| Inclusión: PS | ≥18 años; PS OMS 0 o 1 | [p. 2] |
| Exclusión | Antecedente de neumonitis de grado ≥2; cualquier toxicidad no resuelta de grado ≥2 (CTCAE v4.03) por la QRT previa | [p. 2] |
| Reclutamiento | 28 sep 2018 – 18 ago 2021: **939 inscritos**, **730 aleatorizados** (D 264; D+T 200; placebo 266) | [p. 4 {1316}] |
| Por cohorte | 600 aleatorizados antes de la enmienda y 130 después | [p. 4] |
| Población ITT de este informe | 530 (D 264 + placebo 266) | [p. 4] |
| Tamaño planificado | ~724 aleatorizados (ITT) | [p. 3] |
| Recibieron ≥1 dosis | D 263; placebo 265 | [p. 4] |
| Población de seguridad | D 262; placebo 265. Un paciente asignado a D recibió también tremelimumab y se contará en el grupo D+T | [p. 7; Tabla 3, nota †, p. 13] |
| Fecha de corte | 15 de enero de 2024 | [p. 1, p. 7] |
| Mediana de seguimiento, SG (censurados) | D 37,2 meses (rango 0,1–60,2); placebo 37,2 meses (0,7–60,9) | [p. 7 {1319}] |
| Mediana de seguimiento, SLP (censurados) | D 27,4 meses (0,0–55,4); placebo 27,7 meses (0,0–55,8) | [p. 7] |
| Completaron 24 meses | D 88 (33,5 %); placebo 70 (26,4 %) | [p. 7] |
| Discontinuaron | D 175 (66,5 %); placebo 195 (73,6 %). Por progresión: 121 (46,0 %) frente a 154 (58,1 %). Por EA: 43 (16,3 %) frente a 29 (10,9 %) | [p. 7] |
| Infusiones | Mediana 9 (rango 1–26) en ambos grupos; media 12,9 (D) frente a 11,8 (placebo) | [p. 7] |
| Terapia subsiguiente (ITT) | Cualquiera: 95 (36,0 %) frente a 127 (47,7 %). Quimioterapia citotóxica: 82 (31,1 %) frente a 114 (42,9 %). Inmunoterapia en la 1.ª terapia subsiguiente: 17 (6,4 %) frente a 31 (11,7 %) | [p. 7] |

## 3. Desenlaces y plan estadístico

- **Primarios (dobles)**: SG y SLP, durvalumab frente a placebo. La SLP se evaluó por revisión central independiente ciega (BICR) según RECIST 1.1 [p. 3].
- **Secundarios con control de alfa**: SG y SLP, D+T frente a placebo [p. 3].
- **Otros secundarios reportados**: respuesta objetiva, SLP a 18 y 24 meses, SG a 24 y 36 meses y seguridad. La línea basal tumoral para la respuesta es la evaluación en la aleatorización, es decir, después de la QRT [p. 3].
- **Multiplicidad**: procedimiento jerárquico de pruebas múltiples que controla el error tipo I bilateral al 5 % entre los cuatro desenlaces citados (Fig. S2, no disponible) [p. 3].
- **Alfa en este análisis intermedio** [p. 3]:
  - SG: umbral **0,01679** (bilateral), dentro de un nivel global de 4,5 %.
  - SLP: umbral **0,00184** al nivel de 0,5 % y **0,02805** al nivel global de 5 % tras reciclar alfa desde la SG. La significación de la SLP se alcanzó con alfa reciclado.
  - Los IC «no estándar» corresponden a esos umbrales: **98,321 %** para la SG y **99,816 % / 97,195 %** para la SLP [p. 4].
- **Métodos** [p. 4]: Kaplan–Meier. Medianas con IC95 % por Brookmeyer–Crowley con transformación log–log. Log-rank estratificado (SG ajustada por PCI; SLP ajustada por estadio y PCI). HR por Cox estratificado. IC por verosimilitud de perfil. Riesgos proporcionales evaluados con gráficos log(−log) y una covariable dependiente del tiempo. En los subgrupos se usó Cox **no estratificado** con el grupo como única covariable.
- **Prueba de riesgos proporcionales**: SG p = 0,91 [p. 7, leyenda de la Fig. 1]; SLP p = 0,79 [p. 9, leyenda de la Fig. 2].
- **Fracción de información, número de eventos objetivo y límites de la siguiente análisis**: No reportado en el texto principal (remite al Suplemento).
- **Brazo D+T**: el comité independiente de datos y seguridad determinó que **no se cruzó** el límite preespecificado de SG para D+T frente a placebo, por lo que sus resultados siguen cegados hasta el próximo análisis [p. 3–4].

## 4. Resultados transcritos

### 4.1 Características basales (Tabla 1, [p. 5 {1317}], ITT)

| Característica | Durvalumab (N=264) | Placebo (N=266) |
|---|---|---|
| Edad mediana (rango), años | 62 (28–84) | 62 (28–79) |
| Sexo masculino, n (%) | 178 (67,4) | 188 (70,7) |
| Raza: blanca | 130 (49,2) | 137 (51,5) |
| Raza: asiática | 131 (49,6) | 121 (45,5) |
| Raza: negra | 1 (0,4) | 3 (1,1) |
| Raza: otra | 2 (0,8) | 5 (1,9) |
| Región: Asia | 129 (48,9) | 120 (45,1) |
| Región: Europa | 94 (35,6) | 112 (42,1) |
| Región: Norte o Sudamérica | 41 (15,5) | 34 (12,8) |
| PS OMS 0 | 132 (50,0) | 126 (47,4) |
| PS OMS 1 | 132 (50,0) | 140 (52,6) |
| Fumador actual o exfumador | 241 (91,3) | 240 (90,2) |
| Estadio TNM I o II¶ | 33 (12,5) | 34 (12,8) |
| Estadio TNM III¶ | 231 (87,5) | 232 (87,2) |
| QT 1.er ciclo: cisplatino–etopósido | 173 (65,5) | 178 (66,9) |
| QT 1.er ciclo: carboplatino–etopósido | 91 (34,5) | 88 (33,1) |
| RT una vez al día | 195 (73,9) | 187 (70,3) |
| RT dos veces al día | 69 (26,1) | 79 (29,7) |
| Mejor respuesta a la QRT: RC | 31 (11,7) | 34 (12,8) |
| Mejor respuesta a la QRT: RP | 191 (72,3) | 200 (75,2) |
| Mejor respuesta a la QRT: EE | 42 (15,9) | 32 (12,0) |
| Fin de la QRT a aleatorización: <14 días | 32 (12,1) | 32 (12,0) |
| 14 a <28 días | 79 (29,9) | 80 (30,1) |
| ≥28 días | 153 (58,0) | 154 (57,9) |
| PCI antes de aleatorizar¶ | 142 (53,8) | 143 (53,8) |

¶ = factor de estratificación según el CRF electrónico.

Totales en el texto [p. 4]: mediana de edad 62 años; exfumadores 68,5 %; fumadores actuales 22,3 %; estadio III 87,4 %; cisplatino–etopósido 66,2 % y carboplatino–etopósido 33,8 %; **88,3 % recibió 4 ciclos de QT**; RT una vez al día 72,1 % y dos veces al día 27,9 %; **93,6 % recibió la dosis de RT recomendada** (60–66 Gy una vez al día o 45 Gy dos veces al día); PCI 53,8 %. Los pacientes negros fueron el 0,8 % de la población total del ensayo (Tabla S2) [p. 4].

### 4.2 Supervivencia global (Fig. 1A, [p. 6 {1318}]; texto [p. 7 {1319}])

| Medida | Durvalumab | Placebo |
|---|---|---|
| Muertes / total (%) | 115/264 (43,6) | 146/266 (54,9) |
| Mediana de SG (IC95 %), meses | **55,9 (37,3–NR)** | **33,4 (25,5–39,9)** |
| SG a 24 meses (IC95 %) | **68,0 % (61,9–73,3)** | **58,5 % (52,3–64,3)** |
| SG a 36 meses (IC95 %) | **56,5 % (50,0–62,5)** | **47,6 % (41,3–53,7)** |
| HR estratificado de muerte | **0,73 (IC 98,321 %: 0,54–0,98); P = 0,01** (umbral 0,01679) | |
| HR con IC95 % (fila «All patients» del forest) | 0,73 (0,57–0,93) | |
| Madurez | 261 muertes (49,2 %) [p. 7] | |

### 4.3 Supervivencia libre de progresión, BICR (Fig. 2A, [p. 8 {1320}]; texto [p. 7])

| Medida | Durvalumab | Placebo |
|---|---|---|
| Eventos / total (%) | 139/264 (52,7) | 169/266 (63,5) |
| Mediana de SLP (IC95 %), meses | **16,6 (10,2–28,2)** | **9,2 (7,4–12,9)** |
| SLP a 18 meses (IC95 %) | **48,8 % (42,2–55,0)** | **36,1 % (29,9–42,2)** |
| SLP a 24 meses (IC95 %) | **46,2 % (39,6–52,5)** | **34,2 % (28,2–40,3)** |
| HR estratificado de progresión o muerte | **0,76 (IC 99,816 %: 0,53–1,08) (IC 97,195 %: 0,59–0,98); P = 0,02** (umbral 0,02805 tras reciclar alfa) | |
| HR con IC95 % (fila «All patients» del forest) | 0,76 (0,61–0,95) | |
| Madurez | 308 eventos (58,1 %) [p. 7] | |
| Composición de los eventos [p. 9, leyenda de la Fig. 2] | Progresión RECIST: 126. Muerte sin progresión: 13 | Progresión: 158. Muerte sin progresión: 11 |
| Sitio de progresión (categorías no excluyentes) | Lesiones diana 31; no diana 5; nuevas 94 | Lesiones diana 31; no diana 13; nuevas 128 |

Las SG a 24/36 meses y SLP a 18/24 meses no tienen comparación formal (p) reportada.

### 4.4 TABLAS DE NÚMEROS EN RIESGO (transcripción literal, verificada visualmente y con coordenadas)

**Fig. 1A — Supervivencia global (ITT), [p. 6 {1318}].** Eje x: «Months since Randomization», de 0 a 63 cada 3 meses.

| Mes | 0 | 3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 | 39 | 42 | 45 | 48 | 51 | 54 | 57 | 60 | 63 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Durvalumab | 264 | 261 | 248 | 236 | 223 | 207 | 189 | 183 | 172 | 162 | 141 | 110 | 90 | 68 | 51 | 39 | 27 | 19 | 11 | 5 | 1 | 0 |
| Placebo | 266 | 260 | 247 | 231 | 214 | 195 | 175 | 164 | 151 | 143 | 123 | 97 | 80 | 62 | 44 | 31 | 23 | 19 | 8 | 5 | 1 | 0 |

**Fig. 2A — Supervivencia libre de progresión, BICR (ITT), [p. 8 {1320}].** Eje x de 0 a 63 cada 3 meses.

| Mes | 0 | 3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 | 39 | 42 | 45 | 48 | 51 | 54 | 57 | 60 | 63 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Durvalumab | 264 | 212 | 161 | 135 | 113 | 105 | 101 | 98 | 84 | 78 | 51 | 51 | 33 | 21 | 19 | 10 | 10 | 4 | 4 | 0 | 0 | 0 |
| Placebo | 266 | 208 | 146 | 122 | 100 | 88 | 79 | 76 | 71 | 69 | 47 | 47 | 34 | 23 | 22 | 15 | 14 | 5 | 5 | 0 | 0 | 0 |

**Durvalumab + tremelimumab**: no hay curvas ni números en riesgo, porque el brazo está cegado (n = 200) [p. 1, p. 4].
**Otras curvas KM en el artículo principal**: ninguna. La duración de la respuesta se presenta en la Fig. S5, que no está disponible.

### 4.5 Subgrupos (forest plots, todos legibles; HR con IC95 % de Cox no estratificado)

**SG — Fig. 1B [p. 6 {1318}]** (muertes/n (%) D; muertes/n (%) P; HR (IC95 %))

| Subgrupo | Durvalumab | Placebo | HR (IC95 %) |
|---|---|---|---|
| Todos (ITT) | 115/264 (43,6) | 146/266 (54,9) | 0,73 (0,57–0,93) |
| Edad <65 | 69/160 (43,1) | 83/162 (51,2) | 0,76 (0,55–1,04) |
| Edad ≥65 | 46/104 (44,2) | 63/104 (60,6) | 0,70 (0,48–1,02) |
| Hombre | 79/178 (44,4) | 108/188 (57,4) | 0,70 (0,52–0,93) |
| Mujer | 36/86 (42) | 38/78 (49) | 0,83 (0,52–1,31) |
| Blanca | 60/130 (46,2) | 77/137 (56,2) | 0,75 (0,53–1,05) |
| Asiática | 53/131 (40,5) | 64/121 (52,9) | 0,72 (0,50–1,04) |
| Asia | 51/129 (39,5) | 62/120 (51,7) | 0,72 (0,50–1,04) |
| Europa | 41/94 (44) | 64/112 (57,1) | 0,67 (0,45–0,98) |
| Norte o Sudamérica | 23/41 (56) | 20/34 (59) | 0,98 (0,54–1,80) |
| PS 0 | 48/133 (36,1) | 74/131 (56,5) | 0,55 (0,38–0,79) |
| PS 1 | 67/131 (51,1) | 72/135 (53,3) | 0,94 (0,67–1,31) |
| Fumador actual o exfumador | 108/241 (44,8) | 138/240 (57,5) | 0,72 (0,56–0,92) |
| No fumador | 7/23 (30) | 8/26 (31) | NC (<10 muertes por grupo) |
| Estadio I–II | 11/33 (33) | 12/34 (35) | 0,92 (0,40–2,11) |
| Estadio III | 104/231 (45,0) | 134/232 (57,8) | 0,71 (0,55–0,91) |
| Carboplatino–etopósido | 31/91 (34) | 46/88 (52) | 0,56 (0,35–0,89) |
| Cisplatino–etopósido | 84/173 (48,6) | 100/178 (56,2) | 0,82 (0,61–1,10) |
| RT una vez al día | 92/195 (47,2) | 107/187 (57,2) | 0,72 (0,55–0,95) |
| RT dos veces al día | 23/69 (33) | 39/79 (49) | 0,68 (0,40–1,14) |
| RC a la QRT | 12/31 (39) | 15/34 (44) | 0,90 (0,41–1,92) |
| RP a la QRT | 88/191 (46,1) | 116/200 (58,0) | 0,76 (0,57–1,00) |
| EE a la QRT | 15/42 (36) | 15/32 (47) | 0,54 (0,25–1,13) |
| QRT→aleatorización <14 días | 14/32 (44) | 24/32 (75) | 0,47 (0,24–0,91) |
| 14 a <28 días | 37/79 (47) | 51/80 (64) | 0,59 (0,38–0,90) |
| ≥28 días | 64/153 (41,8) | 71/154 (46,1) | 0,90 (0,64–1,27) |
| PCI sí | 53/142 (37,3) | 67/143 (46,9) | 0,75 (0,52–1,07) |
| PCI no | 62/122 (50,8) | 79/123 (64,2) | 0,71 (0,51–0,99) |

**SLP — Fig. 2B [p. 8 {1320}]** (eventos/n (%))

| Subgrupo | Durvalumab | Placebo | HR (IC95 %) |
|---|---|---|---|
| Todos (ITT) | 139/264 (52,7) | 169/266 (63,5) | 0,76 (0,61–0,95) |
| Edad <65 | 83/160 (51,9) | 98/162 (60,5) | 0,77 (0,58–1,03) |
| Edad ≥65 | 56/104 (53,8) | 71/104 (68,3) | 0,77 (0,54–1,10) |
| Hombre | 96/178 (53,9) | 120/188 (63,8) | 0,80 (0,61–1,04) |
| Mujer | 43/86 (50) | 49/78 (63) | 0,71 (0,47–1,08) |
| Blanca | 65/130 (50,0) | 90/137 (65,7) | 0,68 (0,49–0,93) |
| Asiática | 72/131 (55,0) | 75/121 (62,0) | 0,91 (0,66–1,26) |
| Asia | 70/129 (54,3) | 73/120 (60,8) | 0,91 (0,65–1,26) |
| Europa | 46/94 (49) | 75/112 (67,0) | 0,60 (0,41–0,86) |
| Norte o Sudamérica | 23/41 (56) | 21/34 (62) | 0,88 (0,49–1,61) |
| PS 0 | 60/133 (45,1) | 82/131 (62,6) | 0,64 (0,46–0,90) |
| PS 1 | 79/131 (60,3) | 87/135 (64,4) | 0,91 (0,67–1,24) |
| Fumador actual o exfumador | 129/241 (53,5) | 154/240 (64,2) | 0,78 (0,62–0,99) |
| No fumador | 10/23 (43) | 15/26 (58) | 0,62 (0,27–1,37) |
| Estadio I–II | 14/33 (42) | 19/34 (56) | 0,71 (0,35–1,42) |
| Estadio III | 125/231 (54,1) | 150/232 (64,7) | 0,77 (0,61–0,98) |
| Carboplatino–etopósido | 44/91 (48) | 57/88 (65) | 0,61 (0,41–0,90) |
| Cisplatino–etopósido | 95/173 (54,9) | 112/178 (62,9) | 0,86 (0,65–1,13) |
| RT una vez al día | 108/195 (55,4) | 122/187 (65,2) | 0,77 (0,60–1,00) |
| RT dos veces al día | 31/69 (45) | 47/79 (59) | 0,72 (0,45–1,13) |
| RC a la QRT | 15/31 (48) | 18/34 (53) | 1,00 (0,50–1,99) |
| RP a la QRT | 106/191 (55,5) | 130/200 (65,0) | 0,81 (0,62–1,04) |
| EE a la QRT | 18/42 (43) | 21/32 (66) | 0,50 (0,26–0,94) |
| QRT→aleatorización <14 días | 18/32 (56) | 27/32 (84) | 0,45 (0,24–0,83) |
| 14 a <28 días | 43/79 (54) | 50/80 (62) | 0,89 (0,59–1,34) |
| ≥28 días | 78/153 (51,0) | 92/154 (59,7) | 0,79 (0,58–1,07) |
| PCI sí | 65/142 (45,8) | 84/143 (58,7) | 0,73 (0,53–1,01) |
| PCI no | 74/122 (60,7) | 85/123 (69,1) | 0,80 (0,59–1,09) |

No se reportan p de interacción.

### 4.6 Respuesta objetiva (Tabla 2, [p. 10 {1322}]; BICR; incluye respuestas confirmadas y no confirmadas)

| | Durvalumab | Placebo |
|---|---|---|
| Evaluables (enfermedad medible tras la QRT) | 175 | 169 |
| ORR, n; % (IC95 %) | 53; 30,3 (23,6–37,7) | 54; 32,0 (25,0–39,6) |
| RC | 5/175 (2,9) | 4/169 (2,4) |
| RP | 48/175 (27,4) | 50/169 (29,6) |
| EE ≥7 semanas | 94/175 (53,7) | 76/169 (45,0) |
| Progresión | 24/175 (13,7) | 33/169 (19,5) |
| No evaluable | 4/175 (2,3) | 6/169 (3,6) |
| Mediana de la duración de respuesta (IC95 %), meses | 33,0 (22,4–NR) | 27,7 (9,6–NR) |
| Respuesta en curso a 12 meses | 74 % (59–84) | 60 % (44–73) |
| Respuesta en curso a 18 meses | 71 % (57–82) | 55 % (39–68) |

No evaluables por no tener enfermedad medible tras la QRT: 89 (D) y 97 (placebo). Hubo 8 RP no confirmadas en D; en placebo, 1 RC y 9 RP no confirmadas [p. 10].

### 4.7 Seguridad (Tabla 3, [p. 12 {1324}]; población de seguridad: D N=262, P N=265)

| Evento | D, cualquier grado | D, grado 3–4 | P, cualquier grado | P, grado 3–4 |
|---|---|---|---|---|
| Cualquier EA | 247 (94,3) | **64 (24,4)** | 234 (88,3) | **64 (24,2)** |
| EA serio (incluye muerte) | 78 (29,8) | — | 64 (24,2) | — |
| EA con desenlace de muerte | **7 (2,7)** | — | **5 (1,9)** | — |
| EA que lleva a discontinuación | **43 (16,4)** | — | **28 (10,6)** | — |
| EA que lleva a interrupción de dosis | 91 (34,7) | — | 76 (28,7) | — |
| EA inmunomediado | 84 (32,1) | 14 (5,3) | 27 (10,2) | 4 (1,5) |
| Neumonitis por radiación | 60 (22,9) | 3 (1,1) | 62 (23,4) | 5 (1,9) |
| Neumonitis | 28 (10,7) | 3 (1,1) | 16 (6,0) | 2 (0,8) |
| **Neumonitis o neumonitis por radiación (agrupada)** | **100 (38,2)** | **8 (3,1)** | **80 (30,2)** | **7 (2,6)** |
| Neumonitis o neumonitis por radiación → discontinuación | **23 (8,8)** | — | **8 (3,0)** | — |
| Hipotiroidismo | 42 (16,0) | 0 | 10 (3,8) | 0 |
| Hipertiroidismo | 27 (10,3) | 0 | 4 (1,5) | 0 |
| Disminución del apetito | 44 (16,8) | 0 | 34 (12,8) | 0 |
| Tos | 40 (15,3) | 0 | 32 (12,1) | 0 |
| Prurito | 34 (13,0) | 0 | 19 (7,2) | 0 |
| Náusea | 33 (12,6) | 0 | 29 (10,9) | 0 |
| Mareo | 32 (12,2) | 0 | 20 (7,5) | 0 |
| Fatiga | 32 (12,2) | 1 (0,4) | 34 (12,8) | 4 (1,5) |
| Diarrea | 29 (11,1) | 5 (1,9) | 22 (8,3) | 0 |
| Neumonía | 29 (11,1) | 7 (2,7) | 20 (7,5) | 9 (3,4) |
| Exantema | 28 (10,7) | 1 (0,4) | 16 (6,0) | 0 |
| Estreñimiento | 27 (10,3) | 0 | 26 (9,8) | 0 |
| Cefalea | 24 (9,2) | 1 (0,4) | 35 (13,2) | 0 |
| Anemia | 23 (8,8) | 3 (1,1) | 16 (6,0) | 3 (1,1) |
| Artralgia | 18 (6,9) | 0 | 29 (10,9) | 1 (0,4) |
| Hiperglucemia | 11 (4,2) | 3 (1,1) | 10 (3,8) | 0 |
| Hipertensión | 9 (3,4) | 3 (1,1) | 4 (1,5) | 0 |
| Lipasa aumentada | 8 (3,1) | 5 (1,9) | 7 (2,6) | 4 (1,5) |
| Amilasa aumentada | 7 (2,7) | 3 (1,1) | 3 (1,1) | 0 |
| EPOC | 6 (2,3) | 1 (0,4) | 7 (2,6) | 4 (1,5) |
| Embolia pulmonar | 6 (2,3) | 5 (1,9) | 4 (1,5) | 3 (1,1) |

Otros datos de seguridad del texto [p. 9 {1321}]:
- EA relacionados con el tratamiento: 67,2 % frente a 48,7 %; de grado 3–4, 8,8 % frente a 6,0 % (Tabla S3).
- EA relacionados que llevaron a discontinuación: 11,5 % frente a 5,7 %.
- EA serios relacionados: 12,2 % frente a 6,4 %.
- Eventos de hipotiroidismo 13,7 % frente a 3,4 % y de neumonitis 11,8 % frente a 3,0 % (EA inmunomediados, Tabla S6).
- Neumonitis o neumonitis por radiación de **grado 5**: 1 paciente (0,4 %) en D y ninguno en placebo [p. 9, p. 11].

**Muertes por EA** [Tabla 3, nota §, p. 13]:
- Durvalumab (7): neumonía (2), neumonía bacteriana (2), encefalopatía (1), insuficiencia cardiaca (1) y neumonitis (1). El investigador consideró posiblemente relacionadas la encefalopatía y la neumonitis (2 pacientes, 0,8 %).
- Placebo (5): neumonía (2), COVID-19 (1), sepsis (1) y carcinoma escamoso de hipofaringe (1).
- Ventana de registro de EA: hasta 90 días tras la última dosis o hasta el inicio de la siguiente terapia sistémica, lo que ocurriera primero.

## 5. Limitaciones declaradas por los autores

1. El ensayo no tenía potencia para comparaciones de subgrupos; los subgrupos deben interpretarse con cautela [p. 11 {1323}].
2. Subrepresentación de personas negras (0,8 % de la población del ensayo) [p. 4, p. 11].
3. Parte de los EA probablemente se debió a la QRT previa y a la enfermedad de base, como muestra el grupo placebo [p. 11].
4. La SG del grupo placebo (mediana de 33,4 meses) superó las referencias históricas, como CONVERT (25,4–30,0 meses). Los autores lo atribuyen a la selección de pacientes sin progresión tras la QRT, a la exclusión de toxicidad persistente de grado ≥2, a mejoras de la RT y, posiblemente, al acceso a quimioinmunoterapia en la recaída [p. 11].
5. Es un análisis intermedio y el brazo D+T sigue cegado [p. 1, p. 2, p. 4].
6. El uso temprano de inmunoterapia podría afectar la utilidad de los regímenes con inmunoterapia en la recaída (re-tratamiento según la respuesta inicial y el intervalo libre de tratamiento) [p. 13 {1325}].

## 6. Evaluación del lector **[Evaluación del lector]**

- **Madurez de los datos.**
  - SG: 49,2 % de eventos (261/530). SLP: 58,1 % (308/530) [p. 7].
  - La mediana de SG del brazo durvalumab (55,9 meses) se alcanza en la cola de la curva. Según la figura, la curva de durvalumab cae de ≈50 % a ≈43 % alrededor del mes 56, cuando había entre 11 y 5 pacientes en riesgo (meses 54 y 57; Fig. 1A).
  - Por tanto, esa mediana depende de muy pocos pacientes y es inestable: el límite superior del IC es NR y el inferior, 37,3. Para comparar o modelar conviene usar las tasas a 24 y 36 meses y el HR, no la mediana.
- **Análisis intermedio.**
  - Detenerse por eficacia en un análisis intermedio tiende a sobrestimar el efecto (sesgo de los ensayos truncados).
  - El límite superior del IC 98,321 % de la SG (0,98) está cerca de 1. En la SLP, el IC 99,816 % (0,53–1,08) incluye 1, y la significación se alcanzó solo con alfa reciclado.
  - Las cifras deben tratarse como provisionales hasta el análisis final. La fracción de información no se reporta en el texto principal.
- **Coherencia SLP–respuesta.** La ORR fue similar (30,3 % frente a 32,0 %). El beneficio se manifiesta en la duración (DoR, SLP), no en la tasa de respuesta, lo que es compatible con un efecto de consolidación.
- **Generalizabilidad.**
  - Solo incluye pacientes que ya superaron la QRT concurrente sin progresión ni toxicidad de grado ≥2, con PS 0–1 y aleatorizados dentro de 42 días.
  - Excluye QRT secuencial y PS ≥2.
  - El 87 % estaba en estadio III. Hubo pocos pacientes negros y solo 75 de las Américas.
  - El reloj empieza en la aleatorización, no en el diagnóstico. Para modelar desde el diagnóstico hay que añadir la duración de la QRT más el intervalo hasta la aleatorización (en la Tabla 1, el 58 % superó los 28 días); la duración exacta de la QRT no se reporta en el texto principal.
  - Existe además un sesgo de selección y supervivencia condicionada (landmark) respecto a cohortes desde el diagnóstico.
- **Subgrupos.**
  - Hay heterogeneidad aparente: PS 0 (HR 0,55) frente a PS 1 (0,94); intervalo <14 días (0,47) frente a ≥28 días (0,90); cisplatino (0,82) frente a carboplatino (0,56); Norte o Sudamérica (0,98).
  - No hay p de interacción, hay comparaciones múltiples y los IC son amplios. Es hipótesis, no evidencia.
- **Terapia posterior.** El placebo recibió más terapia subsiguiente (47,7 % frente a 36,0 %) y más inmunoterapia (11,7 % frente a 6,4 %). Esto puede diluir algo la diferencia en SG.
- **Seguridad.** Los EA de grado 3–4 fueron similares, pero hubo más discontinuación por neumonitis (8,8 % frente a 3,0 %), más EA inmunomediados (32,1 % frente a 10,2 %) y una muerte por neumonitis.
- **Qué NO se puede concluir.**
  - Nada sobre durvalumab + tremelimumab, que sigue cegado.
  - Nada sobre la supervivencia a 5 años ni sobre una fracción de curación (la cola tiene menos de 20 pacientes en riesgo después de 51 meses).
  - Nada sobre la eficacia en QRT secuencial, PS 2, estadio I–II operable o pacientes que progresan durante la QRT.
  - No hay comparación con inmunoterapia concurrente con la QRT.
  - No se reportan calidad de vida ni costo-efectividad en este artículo.
  - Los subgrupos no permiten seleccionar pacientes.
  - La mediana de SG de 55,9 meses no es un parámetro robusto.

## 7. Aptitud para reconstruir datos individuales (IPD; método de Guyot et al. 2012)

| Curva | ¿Números en riesgo? | Tiempos | Eventos totales | Datos de validación |
|---|---|---|---|---|
| SG, durvalumab | **Sí** | 0–63 meses cada 3 meses (22 puntos) | **115** | Mediana 55,9; SG24 68,0 %; SG36 56,5 %; HR 0,73 |
| SG, placebo | **Sí** | Ídem | **146** | Mediana 33,4; SG24 58,5 %; SG36 47,6 % |
| SLP, durvalumab | **Sí** | Ídem | **139** (126 progresiones + 13 muertes) | Mediana 16,6; SLP18 48,8 %; SLP24 46,2 %; HR 0,76 |
| SLP, placebo | **Sí** | Ídem | **169** (158 + 11) | Mediana 9,2; SLP18 36,1 %; SLP24 34,2 % |
| D+T (SG/SLP) | **No**: brazo cegado | — | — | — |
| Duración de respuesta | No (Fig. S5, no disponible) | — | 22 y 23 eventos | Medianas 33,0 / 27,7 |

- **Censurados por arm** [Evaluación del lector, por resta]: SG 149 (D) y 120 (P); SLP 125 (D) y 97 (P).
- **Calidad de la figura para digitalizar**:
  - Las curvas son **gráficos vectoriales** en el PDF, no imágenes rasterizadas (0 imágenes en las págs. 6 y 8). Durvalumab es un relleno naranja RGB ≈ (0,89, 0,62, 0,25) y placebo, un relleno azul RGB ≈ (0,36, 0,53, 0,77). Los ejes y las etiquetas de los ticks están en la capa de texto (eje x 0–63 cada 3 meses; eje y 0–100 cada 10 %).
  - Es viable extraer las coordenadas exactas de los escalones desde los trazados vectoriales con PyMuPDF (`page.get_drawings()`), con una precisión muy superior a la digitalización manual.
  - Precaución: las marcas de censura (ticks verticales) son del mismo color y se superponen a la curva. Hay que separarlas del escalón, por ejemplo filtrando segmentos verticales cortos y aislados. Hay muchos censurados agrupados entre los meses 27 y 60.
  - No lo ejecuté: solo comprobé que los trazados existen.
- **Viabilidad** [Evaluación del lector]: **alta** para las cuatro curvas D/P. Tienen números en riesgo en 22 tiempos, eventos totales por brazo, medianas, tasas de referencia con IC y HR para validar (la reconstrucción debería reproducir un HR ≈ 0,73 y ≈ 0,76; el HR del artículo es estratificado, así que puede haber pequeñas diferencias).
- **Limitaciones de la reconstrucción**:
  1. La cola tras unos 45 meses tiene pocos pacientes en riesgo, con gran incertidumbre.
  2. En la SLP, los números en riesgo son idénticos en los meses 30 y 33 (51/51 en D; 47/47 en P). Esto implica que nadie salió del conjunto en riesgo en (30, 33]; el algoritmo debe aceptar ese intervalo con 0 eventos y 0 censuras, y conviene comprobar que la curva no muestre escalones allí.
  3. Hay una caída precoz pronunciada de la SLP entre los meses 0 y 6 por las evaluaciones programadas (agrupación de eventos en las visitas de imagen). Los eventos son censurados por intervalo de hecho; Guyot asume tiempos continuos.
  4. Para la PCI o el estadio no hay curvas por subgrupo, solo HR.

## 8. Problemas de extracción

1. En el `.txt`, el texto de las Figs. 1 y 2 está desordenado: los números en riesgo aparecen intercalados con los ticks del eje. **No debe usarse el .txt para los números en riesgo.** Uso la transcripción de §4.4, verificada visualmente y con las coordenadas de las palabras del PDF.
2. Discrepancias menores de denominador:
   - Discontinuación por EA: 43 (16,3 %) y 29 (10,9 %) en el texto [p. 7], frente a 43 (16,4 %) y 28 (10,6 %) en la Tabla 3 [p. 12]. Los denominadores difieren (263/265 frente a 262/265) y probablemente también la definición (motivo principal de discontinuación frente a EA que lleva a discontinuación).
   - Hubo 263 pacientes con ≥1 dosis [p. 4], pero la población de seguridad de D es 262 [p. 7].
3. La fila «All patients» del forest (HR 0,73, IC95 % 0,57–0,93; y 0,76, 0,61–0,95) no aclara si es estratificada o no. El texto dice que los subgrupos usan Cox no estratificado [p. 4].
4. El Suplemento (Fig. S1–S5, Tablas S1–S6, protocolo, plan estadístico con número de eventos objetivo y fracción de información) no está disponible.
5. Los rangos de seguimiento de la SLP empiezan en 0,0 [p. 7]. [Inferencia del lector] Probablemente hay censura en el tiempo 0 (pacientes sin evaluación tumoral posbasal); el artículo no lo explica.

## 9. Citas clave (textuales, ≤40 palabras)

1. «Durvalumab therapy led to significantly longer overall survival than placebo (median, 55.9 months [95% CI, 37.3 to not reached] vs. 33.4 months [95% CI, 25.5 to 39.9]; hazard ratio for death, 0.73; 98.321% CI, 0.54 to 0.98; P = 0.01)» [p. 1].
2. «median 16.6 months [95% CI, 10.2 to 28.2] vs. 9.2 months [95% CI, 7.4 to 12.9]; hazard ratio for progression or death, 0.76; 97.195% CI, 0.59 to 0.98; P = 0.02» [p. 1].
3. «Results of the first planned interim analysis of the two primary end points … are reported; results in the durvalumab–tremelimumab group remain blinded.» [p. 1].
4. «Randomization occurred within 42 days after the completion of chemoradiotherapy and was stratified according to disease stage (I or II vs. III) and receipt of prophylactic cranial irradiation (yes vs. no).» [p. 3].
5. «The significance level for the testing of overall survival at this interim analysis was 0.01679 (two-sided) at the overall 4.5% level» [p. 3].
6. «As of the data-cutoff date, 261 patients had died (data maturity, 49.2%).» [p. 7].
7. «Statistical significance for the analysis of progression-free survival was achieved by means of the alpha-recycling multiple testing procedure framework» [p. 3].
8. «Pneumonitis or radiation pneumonitis with a maximum grade of 3 or 4 occurred in 3.1% of the patients in the durvalumab group and in 2.6% of those in the placebo group.» [p. 1].
9. «the data should be interpreted with caution because our trial was not powered for subgroup comparisons.» [p. 11].
10. «Black patients, who made up 0.8% of the overall trial population, were underrepresented» [p. 4].
