# Reproducción T02 en Windows PowerShell

Único intérprete autorizado: `<PAPERCANCER_ENV>\venv_cline_T02\Scripts\python.exe`. No se requiere instalación adicional. Versiones exactas en requirements_T02.txt, dentro de la carpeta exclusiva indicada abajo. Fuentes solo lectura; rutas en configuración. Nunca ejecutar con `python` sin ruta ni con otro entorno.

## Regenerar todos los resultados

El comando `all` regenera los cálculos: extrae el PDF, reconstruye, valida, ejecuta 100 réplicas de E2.0a y otras 100 de E2.0b con las mismas poblaciones y genera informe/figuras/entrega. Sobrescribe derivados, pero conserva logs y archivos clínicos evaluados. **En ronda 1 el informe comparativo requiere además las copias históricas inmutables** indicadas al final: no son entradas del algoritmo, sino los resultados originales que deben aparecer antes de los corregidos. Duración orientativa local: varios minutos. Una terminal normal puede esperar; no aplicar un timeout de 30 segundos.

```powershell
$root = '<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC'
$python = '<PAPERCANCER_ENV>\venv_cline_T02\Scripts\python.exe'
& $python "$root\src\run_logged.py" "$root\src\pipeline.py" --stage all
if ($LASTEXITCODE -ne 0) { throw 'Pipeline fallido: revisar logs' }
& $python "$root\src\run_logged.py" -m unittest discover -s "$root\tests" -v
if ($LASTEXITCODE -ne 0) { throw 'Pruebas fallidas' }
& $python "$root\src\run_logged.py" "$root\src\verify_outputs.py"
if ($LASTEXITCODE -ne 0) { throw 'Verificacion fallida' }
```

Las pruebas de integración requieren el pipeline terminado; no usan cifras publicadas para modificar el algoritmo. Las 14 pruebas originales se conservan y se añaden 9 de ronda 1 (4 unitarias y 5 de integración). La prueba completamente censurada comprueba una mediana no alcanzada. Se verifica el SHA-256 del PDF autorizado.

## Terminal con límite breve de ejecución

Lanzar únicamente una corrida; no ejecutar otra mientras siga activa. El envoltorio establece un hilo numérico y comprueba el intérprete.

```powershell
$root = '<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC'
$python = '<PAPERCANCER_ENV>\venv_cline_T02\Scripts\python.exe'
$arguments = '"' + $root + '\src\run_logged.py" "' + $root + '\src\pipeline.py" --stage all'
$p = Start-Process -FilePath $python -ArgumentList $arguments -WorkingDirectory $root -RedirectStandardOutput "$root\logs\all_launcher_stdout.txt" -RedirectStandardError "$root\logs\all_launcher_stderr.txt" -PassThru
$p.Id
```

Consultar el stdout del lanzador y el JSON fechado en la carpeta absoluta `$root\logs`. Solo `exit_code: 0` y la terminación del proceso demuestran finalización; disponer de CSV parciales no basta. En Windows el lanzador de un entorno virtual puede delegar al ejecutable base: la comprobación de `sys.executable` dentro del proceso sigue exigiendo el entorno autorizado. No se invoca directamente el Python global.

## Etapas y auditoría

La opción `--stage clinical` regenera extracción, pseudo-IPD y validación; `--stage simulation` regenera E2.0a y E2.0b; `--stage report` requiere las dos etapas previas. Usarlas mediante el mismo envoltorio absoluto anterior. E2.0a conserva 400 archivos de verdad, 400 reconstrucciones y 400 auditorías. E2.0b añade 200 PDF (réplica/desenlace), 400 reconstrucciones y todos sus puntos, segmentos, pares de bordes, marcas, riesgos y auditorías. Semillas y supuestos en configuración, sin cambios respecto a ronda 0.

Para verificar identidad de los derivados entre dos corridas, copiar el manifiesto dentro de la carpeta exclusiva antes de la segunda corrida y compararlo después:

```powershell
$root = '<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC'
$python = '<PAPERCANCER_ENV>\venv_cline_T02\Scripts\python.exe'
Copy-Item -LiteralPath "$root\manifest_sha256.csv" -Destination "$root\logs\baseline_sha256.csv"
# Ejecutar de nuevo el comando all y esperar su terminación antes de comparar.
& $python "$root\src\run_logged.py" "$root\src\verify_outputs.py" --compare "$root\logs\baseline_sha256.csv"
```

El manifiesto incluye fuentes de código, pruebas, configuración, datos, figuras y documentos de entrega. Excluye logs variables, cachés y el propio manifiesto. Los SVG tienen identificadores estables y no llevan fecha variable. Las fuentes originales no se distribuyen.

## Ronda 1: originales y comparación

No sobrescribir ni regenerar como si fueran corregidos:
- `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\logs\ronda0_original`: 1.235 derivados previos a D1/D2.
- `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\logs\ronda0_original_sha256.csv`: hashes verificados antes de editar.
- `<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\logs\ronda0_documentos`: código, pruebas, configuración e informe originales.

`<PROJECT_ROOT>\Resultados\Trabajo_Cline\T02_ADRIATIC\src\round1.py` genera las tablas comparativas de 18 cantidades H1, 88 riesgos, empates y HR Efron/Breslow; conserva el informe original íntegro y añade la sección «Ronda 1 de corrección». E2.0a conserva nombres originales; E2.0b tiene prefijo `simulation_b` dentro de la carpeta absoluta de derivados. Los PDF de E2.0b son sintéticos: página 1, no páginas del ensayo. Las geometrías se obtienen del PDF autorizado en solo lectura, no de cifras de mediana, tasas ni HR.