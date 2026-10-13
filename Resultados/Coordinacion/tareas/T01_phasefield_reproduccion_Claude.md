# Contrato de tarea T01: reproducción del modelo de campo de fase y verificación de la Tabla 2 (F0–F1)

| Campo | Valor |
|---|---|
| **Identificador** | T01 |
| **Responsable** | **Claude Code** (coordinador) |
| **Revisión independiente** | Revisión crítica acotada por Cline (tarea T03, tras la entrega) y re-ejecución de comprobaciones por el coordinador |
| **Versión** | 1.0 (10-oct-2026) |

## 1. Objetivo y alcance

**F0:**
- Identificar la versión publicada y la revisión del repositorio.
- Revisar los requisitos, los términos de uso y la correspondencia entre artículo, código y datos.
- Preparar un entorno aislado.

**F1:**
- Ejecutar el código original **sin modificar su lógica**.
- Reproducir los índices de sensibilidad local de la **Tabla 2** de Wagner et al., *Math Biosci Eng* 2023;20:18670–94 (88 valores: 11 parámetros × 4 métricas × 2 pacientes) y su procedimiento.
- Reproducir la farmacocinética (ec. 6).
- Comprobar la correspondencia entre la Tabla 1 y el código.

**Fuera del alcance:**
- Recalibrar parámetros, hacer perfiles de verosimilitud o comparar con modelos ODE.
- Predicción fuera de muestra.
- Modelo 3D.
- Ampliar el modelo.

## 2. Fuentes

| Fuente | Ubicación |
|---|---|
| Artículo publicado (MBE 2023, doi:10.3934/mbe.2023828) | `Resultados\03_registro_busquedas\MBE_2023_Wagner_texto_extraido.txt`: Tabla 1 [p. 6], ec. 4.1 y método [p. 16], Tabla 2 [p. 17], disponibilidad de código [p. 20] |
| Preprint (D02, arXiv:2303.09378v1) | `Data_insumo\A phase-field model for non-small cell lung cancer under the.pdf`; ficha D02. **Solo como referencia histórica** |
| Repositorio | github.com/wagnandr/immunotherapy-lung-cancer, **commit `fa8e6229d1540d33014a994f1ea309d6525597aa`** (14-ago-2023, "adds script for local sensitivity analysis"), es decir, el último commit, posterior a la aceptación del artículo (23-ago-2023 [p. 1]). Zip SHA-256 `e45a8cd30cf57efea8980a60a952816c3a725cf3627acecadca0d41b1312acce`, descomprimido en `<PAPERCANCER_ENV>\repos\` (fuera de OneDrive; **no se redistribuye**) |

## 3. Carpeta exclusiva

`Resultados\Trabajo_Claude\T01_phasefield\` (código propio, configuraciones, registros, datos derivados, figuras e informe). El código de los autores **no** se copia aquí: se referencia por commit y ruta.

## 4. Criterios de aceptación (fijados antes de ejecutar)

### 4.1 Tabla 2

Cada uno de los 88 valores se compara con el publicado mediante el error relativo |g_rep − g_pub| / |g_pub|.

Tolerancia: **≤ 10 % (reproducido)**. Justificación:
- (a) La tabla publica 3 cifras significativas: el redondeo aporta ≤ 0,5 %.
- (b) Diferencia central con h = 10⁻³ y cancelación numérica de Q⁺ − Q⁻ (cambio relativo del orden de 10⁻⁵ a 10⁻⁴ en Q̄): con la precisión de doble y las tolerancias del solucionador lineal, el error relativo esperado en g puede ser de varios por ciento en los índices más pequeños (≈ 10⁻⁴).
- (c) Diferencias de versión de las bibliotecas (PETSc, dolfin) en solucionadores iterativos.

Clasificación:
- **Reproducido:** ≤ 10 % y mismo signo.
- **Parcialmente reproducido:** 10–50 % con el mismo signo, o cumple la tolerancia pero difiere en el orden de rango (ranking) publicado.
- **Discrepancia:** > 50 % o signo opuesto.
- **No evaluable:** el cálculo no puede ejecutarse.

Criterio global: **H1 se cumple si ≥ 80 % de los 88 valores están "reproducidos"** (plan, E1, H1).

Se compara además el **orden de rangos** (los números entre paréntesis de la Tabla 2).

### 4.2 Farmacocinética

Pico y valle periódicos de φ_τ frente a la fórmula analítica de la ec. 6 discretizada como en el código: error relativo ≤ 0,1 %.

### 4.3 Correspondencia artículo–código

Lista de cada parámetro de la Tabla 1 frente a su valor efectivo en el código, clasificado como coincide, redondeo o discrepancia.

## 5. Entregables

- `INFORME_T01.md`.
- `src/` (envoltorios propios; ninguna modificación de la lógica original).
- `config/`.
- `logs/`.
- `data_derived/`: g reproducidos frente a publicados; correspondencia de parámetros.
- `figures/`.
- `REPRODUCIR.md`.
- Dependencias: entorno local `<PAPERCANCER_ENV>\venv_claude_T01` e imagen o entorno con FEniCS 2019.1.0 (pendiente, ver bloqueos).

## 6. Bloqueos conocidos

- **dolfin (FEniCS 2019.1.0) no existe para Windows en conda-forge.** Solo hay DOLFINx, cuya API es incompatible (`conda search`, 10-oct-2026). `solvers.py` y `spherical_simulation_runner.py` importan `dolfin`. Ejecutar el código original sin modificarlo requiere Linux: Docker Desktop está instalado pero detenido. **Arrancarlo y descargar una imagen requiere consultar al usuario.**
- **El repositorio no tiene licencia:** se usa solo para la reproducción privada; no se redistribuye. Se prepara un borrador de consulta a los autores, que no se envía.
