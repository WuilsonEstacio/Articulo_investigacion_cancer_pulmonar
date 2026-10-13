# Reproducción T02 en Windows PowerShell

Único intérprete autorizado: `C:\Users\Administrador\PaperCancer_env\venv_cline_T02\Scripts\python.exe`. No se requiere instalación adicional. Versiones exactas en requirements_T02.txt, dentro de la carpeta exclusiva indicada abajo. Fuentes solo lectura; rutas en configuración. Nunca ejecutar con `python` sin ruta ni con otro entorno.

## Regenerar todos los resultados

El comando `all` no consume resultados previos: extrae el PDF, reconstruye, valida, ejecuta 100 réplicas y genera informe/figuras/entrega. Sobrescribe derivados, pero conserva logs y archivos clínicos evaluados. Duración orientativa local: varios minutos. Una terminal normal puede esperar; no aplicar un timeout de 30 segundos.

```powershell
$root = 'C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC'
$python = 'C:\Users\Administrador\PaperCancer_env\venv_cline_T02\Scripts\python.exe'
& $python "$root\src\run_logged.py" "$root\src\pipeline.py" --stage all
if ($LASTEXITCODE -ne 0) { throw 'Pipeline fallido: revisar logs' }
& $python "$root\src\run_logged.py" -m unittest discover -s "$root\tests" -v
if ($LASTEXITCODE -ne 0) { throw 'Pruebas fallidas' }
& $python "$root\src\run_logged.py" "$root\src\verify_outputs.py"
if ($LASTEXITCODE -ne 0) { throw 'Verificacion fallida' }
```

Las pruebas de integración requieren el pipeline terminado; no usan cifras publicadas para modificar el algoritmo. Son 14 pruebas (7 unitarias y 7 de integración). La prueba completamente censurada comprueba una mediana no alcanzada. Se verifica el SHA-256 del PDF autorizado.

## Terminal con límite breve de ejecución

Lanzar únicamente una corrida; no ejecutar otra mientras siga activa. El envoltorio establece un hilo numérico y comprueba el intérprete.

```powershell
$root = 'C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC'
$python = 'C:\Users\Administrador\PaperCancer_env\venv_cline_T02\Scripts\python.exe'
$arguments = '"' + $root + '\src\run_logged.py" "' + $root + '\src\pipeline.py" --stage all'
$p = Start-Process -FilePath $python -ArgumentList $arguments -WorkingDirectory $root -RedirectStandardOutput "$root\logs\all_launcher_stdout.txt" -RedirectStandardError "$root\logs\all_launcher_stderr.txt" -PassThru
$p.Id
```

Consultar el stdout del lanzador y el JSON fechado en la carpeta absoluta `$root\logs`. Solo `exit_code: 0` y la terminación del proceso demuestran finalización; disponer de CSV parciales no basta. En Windows el lanzador de un entorno virtual puede delegar al ejecutable base: la comprobación de `sys.executable` dentro del proceso sigue exigiendo el entorno autorizado. No se invoca directamente el Python global.

## Etapas y auditoría

La opción `--stage clinical` regenera extracción, pseudo-IPD y validación; `--stage simulation` regenera E2.0; `--stage report` requiere las dos etapas previas. Usarlas mediante el mismo envoltorio absoluto anterior. E2.0 conserva 400 archivos de verdad, 400 reconstrucciones y 400 auditorías. Semillas y supuestos en configuración.

Para verificar identidad de los derivados entre dos corridas, copiar el manifiesto dentro de la carpeta exclusiva antes de la segunda corrida y compararlo después:

```powershell
$root = 'C:\Users\Administrador\OneDrive - bisionconsulting.com\Documentos\Paper_Cancer\Resultados\Trabajo_Cline\T02_ADRIATIC'
$python = 'C:\Users\Administrador\PaperCancer_env\venv_cline_T02\Scripts\python.exe'
Copy-Item -LiteralPath "$root\manifest_sha256.csv" -Destination "$root\logs\baseline_sha256.csv"
# Ejecutar de nuevo el comando all y esperar su terminación antes de comparar.
& $python "$root\src\run_logged.py" "$root\src\verify_outputs.py" --compare "$root\logs\baseline_sha256.csv"
```

El manifiesto incluye fuentes de código, pruebas, configuración, datos, figuras y documentos de entrega. Excluye logs variables, cachés y el propio manifiesto. Los SVG tienen identificadores estables y no llevan fecha variable. Las fuentes originales no se distribuyen.