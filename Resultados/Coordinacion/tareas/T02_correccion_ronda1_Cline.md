# T02: correcciones de la ronda 1 (1 de 2)

| Campo | Valor |
|---|---|
| Emisor | Claude Code (coordinador) |
| Fecha | 11-oct-2026 |
| Base | Auditoría T04: `Resultados\Trabajo_Claude\T04_auditoria_T02\AUDITORIA_T04.md` (léela entera antes de empezar) |
| Contrato | T02 v1.0. Siguen vigentes todas sus restricciones, carpetas, entorno y **tolerancias sin cambios** |
| Estado de envío | Enviado el 11-oct-2026 a las 22:40 hora local, tras confirmar el usuario que hay créditos y superarse la prueba `openai-codex` / `gpt-6-astra` (`logs_cline/prueba_creditos_20261011.jsonl`) |

## Qué se verificó y está bien (no lo cambies)

- La re-ejecución es reproducible byte a byte y las 14 pruebas pasan.
- No hay fuga de cifras publicadas.
- Las tolerancias y las decisiones de método no han cambiado.
- La extracción coincide con una extracción ráster independiente: mediana de 0,1 pp.

## D1: fusión de escalones en tramos empinados (obligatoria)

`extract.py`, líneas 28–39, descarta las franjas cuyo grosor vertical supera 0,55 pt. Por eso, varios escalones cortos consecutivos se fusionan en un solo salto. Ejemplo: SLP placebo entre x = 98,6 y 101,2 pt; unos 8 escalones en el polígono terminan como 25 eventos empatados en t = 3,838. Los demás casos están en `T04_auditoria_T02\data_derived\saltos_fusionados.csv`; en la SLP hay empates de hasta 31 y 34 eventos.

1. Conserva los resultados actuales: copia `data_derived/` a `logs/ronda0_original/` **antes** de cambiar nada.
2. Corrige la extracción para recuperar los escalones intermedios. Por ejemplo, deriva los niveles de meseta de los pares de bordes horizontales del polígono del trazo (separados ≈ 0,502 pt), sin depender del grosor vertical. Justifica el método en `DECISIONES_METODO.md`, en una sección nueva fechada, sin borrar la anterior.
3. Añade una prueba que compare, por curva, el número de mesetas extraídas con el número de niveles horizontales del polígono, y el empate máximo por tiempo.
4. Re-ejecuta todo. En el informe, muestra **primero el resultado original y después el corregido**, para:
   - las 18 cantidades H1;
   - los empates (máximo y número de tiempos distintos por curva);
   - la HR con Efron y con Breslow;
   - los números en riesgo.

## D2: E2.0 sin el paso de extracción (obligatoria)

El contrato, en §5.1 paso 5, pide «aplicar KM, extraer puntos y reconstruir». `simulate.py` pasa a `reconstruct()` las coordenadas exactas del KM, sin pasar por la extracción.

1. Conserva el E2.0 actual con la etiqueta «E2.0a: sin digitalización».
2. Añade E2.0b:
   - dibuja cada KM simulado en un PDF vectorial con la geometría de la Fig. 1A: mismas escalas en puntos, trazo relleno de 0,502 pt, marcas de censura rectangulares y colores de los brazos;
   - extrae las curvas con `extract.py`, el mismo código que en ADRIATIC;
   - reconstruye.

   Usa las mismas semillas. Si el tiempo no alcanza para 100 réplicas, haz las 20 primeras y decláralo.
3. Informa de las mismas métricas y tolerancias que en E2.0a, más el error de riesgo y el empate máximo.

## Reglas

- No cambies tolerancias ni criterios. No optimices contra medianas, tasas ni HR publicados.
- Máximo 4 procesos; hilos numéricos = 1.
- Al terminar, actualiza `INFORME_T02.md` (añade la sección «Ronda 1 de corrección») y `ENTREGA_LISTA.md` con el texto «Estado: entregada (ronda 1)».
- Registra las incidencias en `logs/INCIDENCIAS.md`.
