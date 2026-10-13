# Licencias y términos de uso

Verificado el 10-oct-2026. Esto no es asesoramiento jurídico; para usos que vayan más allá de la verificación privada, consúltese a la persona responsable de cumplimiento normativo.

## 1. Modelo de campo de fase (T01)

| Elemento | Términos identificados | Evidencia | Uso permitido en esta fase | Operaciones bloqueadas |
|---|---|---|---|---|
| Artículo Wagner et al., *MBE* 2023;20:18670–94 | **CC BY 4.0** ("© 2023 the Author(s), licensee AIMS Press… Creative Commons Attribution License") | Texto extraído, p. 25 | Citar y reutilizar tablas y figuras con atribución, incluida la comparación con la Tabla 2 | Ninguna |
| Preprint arXiv:2303.09378v1 (D02) | No revisado en detalle (licencia arXiv no verificada) | — | Solo como referencia histórica | — |
| Repositorio `wagnandr/immunotherapy-lung-cancer` (commit `fa8e6229`) | **Sin licencia**: la API de GitHub `/license` responde 404 y `license: null`. Repositorio público. Sin licencia explícita rige el copyright por defecto de los autores. Los Términos de Servicio de GitHub permiten ver el contenido y crear forks dentro de GitHub | Consulta a la API de GitHub, 10-oct-2026 | **Descarga y ejecución privada para verificar los resultados publicados**: práctica habitual de reproducción, sin redistribución. El artículo invita a usarlo ("The data and code used for the simulations are available at…", p. 20) | **Redistribuir** el código (copiarlo a nuestras carpetas compartidas o publicarlo), publicar versiones modificadas y relicenciarlo |
| Datos de pacientes (`data/tumor/pirmin-tumor-pat{1,2}.csv`) | Mediciones volumétricas **anonimizadas** de 2 pacientes; aprobación ética BLAEK n.º 19021 (p. 7); ofrecidas "for the simulations" (p. 20); **sin licencia de datos** | Artículo pp. 7 y 20; repositorio | Uso para reproducir los resultados publicados | **Publicar análisis nuevos derivados** (por ejemplo, recalibraciones o perfiles de verosimilitud en la fase siguiente) sin confirmar con los autores los términos de reutilización. **Redistribuir** los CSV |

**Medidas aplicadas:**
- El código y los datos de los autores se guardan **fuera de OneDrive** (`<PAPERCANCER_ENV>\repos\`) y no se copian a las carpetas del proyecto.
- Nuestros envoltorios los **referencian** por commit y ruta.
- Nuestros resultados derivados (índices g reproducidos, series de farmacocinética) se guardan en el proyecto solo para uso interno.

## 2. ADRIATIC (T02)

| Elemento | Términos | Uso en esta fase |
|---|---|---|
| Cheng et al., *NEJM* 2024 (PDF en `Data_insumo`) | Copyright de la Massachusetts Medical Society (no es acceso abierto con licencia CC) | Extraer datos numéricos de las figuras para un análisis secundario. Es un uso científico habitual (los métodos de reconstrucción de datos individuales se publican de forma rutinaria), pero **reproducir las figuras originales** en una publicación requeriría permiso. Nuestras figuras muestran curvas reconstruidas, no copias del original |
| Datos individuales reconstruidos | Aproximación derivada; **no** son los datos individuales del ensayo | Uso interno. Si se publica, debe etiquetarse como reconstrucción, citando a Guyot 2012 y a la fuente |

## 3. Borrador de consulta a los autores (NO ENVIADO; requiere decisión del usuario)

> **Para:** Andreas Wagner (TUM; autor de correspondencia en D02: wagneran@cit.tum.de). Con copia sugerida a Pirmin Schlicke y Christina Kuttler.
> **Asunto:** Reutilización del código y de los datos de "A phase-field model for non-small cell lung cancer under the effects of immunotherapy" (MBE 2023)
>
> Estimado Dr. Wagner:
>
> Hemos reproducido de forma independiente, con fines de verificación, los índices de sensibilidad local de la Tabla 2 de su artículo, usando el repositorio público `wagnandr/immunotherapy-lung-cancer` (commit fa8e622). Queremos agradecerles que pusieran a disposición código y datos.
>
> El repositorio no incluye un archivo de licencia y querríamos asegurarnos de utilizarlo correctamente. Le agradeceríamos que nos indicara:
> 1. Bajo qué términos podemos reutilizar el código (por ejemplo, ¿consideran añadir una licencia abierta?).
> 2. Si los volúmenes tumorales anonimizados de los dos pacientes pueden usarse en análisis metodológicos adicionales (estimación de parámetros e identificabilidad) que podrían publicarse con la debida citación, y si existe alguna condición derivada de la aprobación ética (BLAEK 19021).
> 3. Si existe trabajo posterior de su grupo sobre la estimación de parámetros de este modelo, para evitar duplicar esfuerzos y, en su caso, citarlo. Hemos visto Scibilia et al., *Math Biosci* 2024.
>
> Además, hemos encontrado algunas diferencias menores entre el artículo y el código (por ejemplo, un factor 0,7 en el término de la inmunoterapia y las fechas de inicio de la terapia), que con gusto les compartiremos.
>
> Atentamente,
> [Nombre, afiliación]
