# Estado del paper doctoral: qué tenemos y qué falta

**Documento:** `Paper_final/Paper_Doctoral_Cancer_Pulmon_PhaseField.md` (borrador v0.3), con versión en español en `Paper_Doctoral_Cancer_Pulmon_PhaseField_ES.md`. **Fecha:** 13-oct-2026.

## 1. Lo que ya tenemos (respaldado por ejecuciones registradas y verificación independiente)

| Bloque | Evidencia | Dónde | Estado |
|---|---|---|---|
| Entorno reproducible (Docker, FEniCS 2019.1.0, bloqueo conda) | Imagen propia y prueba de humo | `Trabajo_Claude/T01_phasefield/env/` | Hecho |
| Farmacocinética (ec. 2.6) | ODE y dosis total exactas; 3 de 6 extremos ≤ 0,1 % | T01 §3 | Hecho (parcialmente reproducido) |
| Tabla 2 (88 índices), salida directa | 0/88; H1 rechazada | T01 §4 | Hecho |
| Tabla 2 reescalada ×α/100 (diagnóstico) | 88/88 a 3 cifras; error máx. 0,449 %; rangos 88/88 | T01 §4.5 y T03 R1 | Hecho y verificado |
| Correspondencia artículo–código | 35 elementos; 9 discrepancias + H01 | T01 §5 | Hecho y verificado (T03) |
| Revisión independiente | Objeciones mayores H01 y H02, aceptadas | `Trabajo_Cline/T03_revision_T01/` | Hecho |
| Defecto H01 (configuración farmacocinética de P2) | Confirmado en el código | T01 §4.5 y §5 n.º 10 | Hecho |
| **Efecto cuantitativo de H01** | Re-simulación de P2 (T06): **relevante** (mediana 12,6 %, máx. 45,2 %, 7 rangos de V_vis reordenados, sin cambios de signo); determinismo exacto | `Trabajo_Claude/T06_P2_H01/INFORME_T06.md` | Hecho. **Sin revisión independiente todavía** |
| Protocolo de auditoría probado en otro problema (ADRIATIC, CPCP) | H1 18/18; D1 y D2 corregidos; prueba fallida declarada | T02, T04, T05 | Hecho (solo suplementario; no se combina con el modelo de CPCNP) |
| Informe integrado F0–F1 | 11 secciones, trazabilidad, T06 y correspondencia con el paper | `Resultados/Integrado/` y `Paper_final/` | Hecho |
| Documento metodológico | Simulaciones, entorno, comandos, reparto del trabajo con los agentes de IA y verificación de entregas | `Paper_final/METODOLOGIA_SIMULACIONES_Y_COLABORACION_IA.md` | Hecho |

## 2. Título y alcance

El título describe ahora lo que el paper contiene: *«Computational Reproducibility Audit of a Published Phase-Field Model of Non-Small Cell Lung Cancer under Anti-PD-1 Immunotherapy (Wagner et al., 2023): Pharmacokinetic Verification, Sensitivity-Index Rescaling and a Configuration Defect»*.
- Atribuye el modelo a Wagner et al. (2023): este trabajo es la auditoría, no el modelo.
- No promete calibración ni optimización, que **no se han hecho**. Siguen en el §5 del paper como trabajo futuro (puntos 5–7 de la tabla siguiente).
- El factor α/100 es el reescalado que define el índice de sensibilidad, no un parámetro calibrado.

### 2.1 Brechas científicas (por prioridad)

| # | Brecha | Por qué importa | Esfuerzo estimado | Requiere |
|---|---|---|---|---|
| 1 | ~~Efecto de H01 (T06)~~ **Hecho** (13-oct). Falta una revisión independiente de T06, como se hizo con T01 (T03), si va a sostener una conclusión del paper | Coherencia con el protocolo de verificación (§3.3 del paper) | Cline, ~3 USD | Autorización |
| 2 | **Reimplementación independiente 1D y verificación entre códigos** (E1.3; segunda parte de H1, L2 ≤ 5 %) | Sin ella H1 queda incompleta y la reproducción depende de un solo código | Días | Autorización |
| 3 | **Trayectorias V_vis(t) de P1 y P2 frente a los datos** (Fig. 3 del artículo; E1.2) | Es la figura central de cualquier paper de modelado y aún no la hemos regenerado | ~1–2 h de cómputo | Autorización |
| 4 | Convergencia en malla (250/500/1000) y en paso de tiempo (1/12, 1/24, 1/48) | Sin ella no se puede separar el error numérico del de modelo | Horas de cómputo | Autorización |
| 5 | **Calibración por verosimilitud y perfiles** (F2; H2) | Paso necesario antes de cualquier uso terapéutico (etapa 3 del §5 del paper) | Semanas (≈ 500 simulaciones por perfil) | Autorización y **permiso de los autores para publicar análisis nuevos con sus datos** |
| 6 | Comparadores ODE (H3) y predicción fuera de muestra (H4) | Valor añadido frente a modelos simples | Semanas | Ídem |
| 7 | Optimización de dosis restringida | Etapa 6 del §5 del paper | Solo después de 5–6 | Ídem |
| 8 | Modelo 3D | Fuera del alcance actual | Alto | — |

### 2.2 Brechas de datos (§5 del paper: LIDC-IDRI y TCGA-LUSC)

- **Ninguna de las dos colecciones contiene volumetría longitudinal bajo inmunoterapia con registro de dosis,** así que no sirven para calibrar este modelo paciente a paciente. En el paper se les asignan papeles auxiliares:
  - LIDC-IDRI: modelo de error de medición entre observadores y segmentación;
  - TCGA-LUSC: geometría basal, histología y covariables genómicas.
- **Pendiente:**
  - verificar los datos descriptivos de ambas colecciones (número de casos, modalidades, condiciones de uso de TCIA y acceso controlado de TCGA) en sus fuentes oficiales;
  - decidir si se solicita acceso;
  - buscar cohortes con TC seriadas bajo anti-PD-1: datos de ensayos vía Vivli (como Ghaffari Laleh 2022) o una cohorte institucional con aprobación ética.
- No se ha hecho ninguna descarga ni solicitud.

### 2.3 Brechas formales y de publicación

| # | Brecha | Estado |
|---|---|---|
| 1 | **Novedad.** Scibilia et al. 2024 (*Math. Biosci.*, doi:10.1016/j.mbs.2024.109287): según su resumen, compara cuatro modelos EDO de inmunoedición para predecir la progresión con inhibidores de puntos de control en cáncer de pulmón; no audita el modelo de campo de fase. Falta leer el texto completo (de pago) y repetir la búsqueda de citas y de fe de erratas de MBE 2023 | Pendiente. **No se puede afirmar novedad** |
| 2 | **Permisos:** el repositorio no tiene licencia y los datos de pacientes no tienen licencia de reutilización | **Bloqueante para publicar.** El borrador de consulta a los autores existe, no se ha enviado y habría que ampliarlo con H01 y α/100 |
| 3 | 28 referencias marcadas † (no cotejadas con su fuente). Ahora todo el material ajeno está citado y su reutilización se declara en el §7.7 del paper | Verificar las † antes de enviar. **Pasar un detector de similitud** (iThenticate o Turnitin) |
| 4 | Figura 2 (esquema del pipeline) | Por dibujar |
| 5 | Autoría, contribuciones, financiación, revista objetivo y normas del programa doctoral | Por definir (tú) |
| 6 | **Uso de IA en la elaboración del manuscrito.** Declarado en el §7.4: Claude y Cline figuran como herramientas de asistencia y Wuilson Estacio como quien manejó las herramientas de IA, el IDE y el entorno de cómputo | Verificar las políticas de la revista y del programa de doctorado y adaptar la declaración a sus requisitos |
| 7 | Idioma: el manuscrito está en inglés, con una traducción al español; este documento de estado, en español | Confirmar el idioma de envío |
| 8 | **Revisión humana experta** (elementos finitos y bioestadística), prevista en el plan (§D.3). Hasta ahora, toda la verificación cruzada la han hecho agentes de IA | Pendiente |

## 3. Recomendación

1. ~~Cerrar T06 e integrar su resultado~~: hecho. Opcional: revisión independiente de T06 por Cline.
2. Autorizar los puntos 3 y 4 de §2.1 (trayectorias y convergencia). Son baratos y completan la parte de reproducción.
3. Decidir sobre la consulta a los autores. Sin ella, el paper solo puede publicarse como auditoría de reproducibilidad, sin análisis nuevos de los datos de pacientes.
4. Si se quiere ampliar el paper más allá de la auditoría, planificar F2 (punto 5 del §2.1).
