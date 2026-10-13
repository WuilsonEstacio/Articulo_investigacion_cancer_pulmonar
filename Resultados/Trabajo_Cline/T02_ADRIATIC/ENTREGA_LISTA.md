# Entrega T02 — Ronda 1 de corrección

Estado: entregada (ronda 1)

Pendiente de revisión del coordinador. No se declara aceptación.

- Informe original seguido de sección «Ronda 1 de corrección»: `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\INFORME_T02.md`.
- D1: extractor corregido, pares de bordes y comprobación de mesetas; D2: E2.0a conservado y E2.0b con 100 réplicas, PDF y extracción compartida.
- H1: 18/18 cantidades reproducidas; tolerancias/configuración/Guyot sin cambios.
- Riesgo corregido: 88 de 88 números en riesgo reproducidos.
- E2.0b: 1800/1800 evaluables en tolerancia; 0 no evaluables. Riesgo y empates en informe/CSV.
- Código y pruebas: `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\src`, `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\tests`. Configuración: `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\config\config.yaml`.
- Derivados clínicos, tablas original/corregido y ambas simulaciones: `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\data_derived`.
- Figuras PNG/SVG clínicas y E2.0a/b: `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\figures`.
- Reproducción: `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\REPRODUCIR.md`; entorno: `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\requirements_T02.txt`.
- Métodos/criterios: `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\DECISIONES_METODO.md`, `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\CRITERIOS_PREESPECIFICADOS.md`.
- Copia original: `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\logs\ronda0_original`; documentación/código originales: `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\logs\ronda0_documentos`; hashes: `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\logs\ronda0_original_sha256.csv`.
- Registros de ejecución y exit_code: `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\logs`. Incidencias: `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\logs\INCIDENCIAS.md`.

## Problemas abiertos
Tiempos individuales no identificables, censura uniforme aproximada, fragilidad de cola SG-D, simulación vectorial idealizada y PH no equivalente al análisis publicado. Los eventos y el riesgo son restricciones de entrada. Ninguna discrepancia se corrigió mediante ajuste a cifras publicadas. Revisión del coordinador pendiente.

## Cierre documental — 12-oct-2026

- Ejecución final: `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\logs\20261011_230459_401462.json`, exit_code=0, 1093,4884095 s (1093 s redondeados), 100 réplicas completas de E2.0b. Terminó el 11-oct-2026 a las 23:23:13 (-05:00), después de la interrupción de sesión de las 23:14 (`external_abort`, según el encargo).
- Batería completa: `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\logs\20261012_111552_310913.json`, **exit_code=1; 22 de 23 pruebas correctas**. Fallo abierto en `test_e20b_all_replicates_same_truth_and_diagnostics`: 168 mesetas extraídas frente a 169 verdaderas, réplica 13, SG, placebo. Siete filas discordantes en el CSV existente; detalles en incidencias. No se modificó nada para hacer pasar la prueba.
- Verificador: `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\logs\20261012_111659_804759.json`, **exit_code=0**, 4683 archivos con hashes. Sin comparación entre corridas; no subsana el fallo de la batería. Registro de actualización posterior del manifiesto en `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\logs\INCIDENCIAS.md`.
- Cierre sin relanzar pipeline ni cálculos científicos; resultados originales conservados antes de los corregidos. Estado de entrega sin declaración de aceptación; decisión pendiente del coordinador.
