# Verificaciones exploratorias de los lectores (no planificadas)

Durante la lectura de los insumos, los lectores delegados hicieron estas comprobaciones breves. Se conservan por transparencia.

**No son resultados del plan.** No tienen protocolo previo, no se usan como evidencia y no sustituyen a los experimentos E1–E3. Algunas rutas dentro de los scripts apuntan al área temporal de la sesión y no son ejecutables tal cual.

| Script | Lector / documento | Qué hace | Uso posterior |
|---|---|---|---|
| `scripts_D02_digitalizacion/*.py` | D02 (campo de fase) | Extraen coordenadas vectoriales de las Figs. 1, 2 y 5 del preprint para digitalizar volúmenes y curvas de fármaco | Los volúmenes digitalizados coinciden exactamente con el CSV público de los autores (inventario, nota 1). Se usará el CSV, no la digitalización |
| `d10_ode.py` | D10 (ABM EGFR) | Integra las ODE de las Tablas 1–2 tal como están publicadas | Resultado informal (ERK-PP ≈ 0; tasa de cambio ~100 veces menor que en la Fig. 6). **Se trata como hipótesis a contrastar en E3**, con protocolo fijado de antemano |
| `vec.py`, `vec2.py`, `words.py`, `render_rot.py` | D04, D08, D09 | Extraen trazados vectoriales y coordenadas de palabras y renderizan páginas rotadas para verificar tablas y números en riesgo | Verificación de transcripción |
| `check.py` | D01 | Recalcula valores de las tablas (LQ, etc.) para detectar incoherencias internas | Las incoherencias se documentan en la ficha D01 §14 |
| `scripts_D06_D07_render/*.py` | D06 y D07 | Renderizan y recortan páginas con ecuaciones | Verificación de transcripción |
