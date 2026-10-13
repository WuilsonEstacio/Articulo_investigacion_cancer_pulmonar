"""Auditoria local independiente: sin importar ni ejecutar codigo de autores/T01."""
import ast
import csv
import hashlib
import json
import math
import operator
import os
from pathlib import Path
import re
import statistics

for variable in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[variable] = '1'

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT.parents[1]
T01 = RESULTS / 'Trabajo_Claude' / 'T01_phasefield'
REPO = Path(r'C:\Users\Administrador\PaperCancer_env\repos\immunotherapy-lung-cancer-fa8e6229d1540d33014a994f1ea309d6525597aa\reduced_models')
ARTICLE = RESULTS / '03_registro_busquedas' / 'MBE_2023_Wagner_texto_extraido.txt'
OUT = ROOT / 'data_derived'
FIELDS = ['pro_P', 'MED_eff', 'landa', 'landa_HN', 'sigma_HN', 'mob_P', 'eps_P', 'pot_P', 'kappa', 'alpha_healthy', 'alpha_tumor']
METRICS = {'phiT': 't', 'phiP': 'p', 'phiN': 'n', 'Vvis': 'vt'}


def text(path):
    return path.read_text(encoding='utf-8-sig')


def numeric(node):
    """Evaluacion restringida de constantes numericas del AST, sin exec/eval."""
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp):
        ops = {ast.Mult: operator.mul, ast.Div: operator.truediv, ast.Add: operator.add, ast.Sub: operator.sub}
        return ops[type(node.op)](numeric(node.left), numeric(node.right))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -numeric(node.operand)
    raise ValueError(ast.dump(node))


def dump_csv(name, rows):
    assert rows
    with (OUT / name).open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def quantile(values, probability):
    values = sorted(values)
    position = (len(values) - 1) * probability
    lower = int(position)
    return values[lower] + (position - lower) * (values[min(lower + 1, len(values) - 1)] - values[lower])


def main():
    OUT.mkdir(exist_ok=True)
    parameter_tree = ast.parse(text(REPO / 'parameters.py'))
    cls = next(n for n in parameter_tree.body if isinstance(n, ast.ClassDef) and n.name == 'TumorModelParameters')
    defaults = {n.target.id: numeric(n.value) for n in cls.body if isinstance(n, ast.AnnAssign)}
    local_tree = ast.parse(text(REPO / 'local_sensitivity_analysis.py'))
    functions = {n.name: n for n in local_tree.body if isinstance(n, ast.FunctionDef)}
    parameters = {}
    for patient in (1, 2):
        call = functions[f'default_parameters_patient{patient}'].body[0].value
        parameters[f'P{patient}'] = defaults | {k.arg: numeric(k.value) for k in call.keywords}
    alpha = {p: [v[f] for f in FIELDS] for p, v in parameters.items()}
    reconstruction = functions['vector_to_parameters'].body[0].value
    preserved = [k.arg for k in reconstruction.keywords]
    assert preserved == FIELDS
    resets = {p: {k: {'base': v, 'perturbaciones': defaults[k]} for k, v in values.items()
                  if k not in preserved and v != defaults[k]} for p, values in parameters.items()}
    assert set(resets['P2']) == {'MED_mas', 'MED_dos', 'MED_tim'}
    assert resets['P1'] == {}

    log_path = T01 / 'logs' / 'tabla2_original_20261012T035307Z.log'
    log = text(log_path)
    lists = {(f'P{p}', metric): ast.literal_eval(values) for metric, p, values in
             re.findall(r'g_(t|p|n|vt)_list_p([12]) = (\[[^\]]+\])', log)}
    assert len(lists) == 8 and all(len(v) == 11 and all(map(math.isfinite, v)) for v in lists.values())
    clean_log = re.sub(r'(?m)^\d\d:\d\d:\d\d\s?', '', log)
    vectors = re.findall(r'(?m)^\d+\s+\[([^\]]+)\],\s*\[', clean_log)
    vector_counts = {'P1': 0, 'P2': 0}
    for vector in vectors:
        values = [float(v) for v in vector.split()]
        matches = [p for p in alpha if all(math.isclose(a, b, rel_tol=1e-12) for a, b in zip(values, alpha[p]))]
        assert len(values) == 11 and len(matches) == 1
        vector_counts[matches[0]] += 1
    assert vector_counts == {'P1': 11, 'P2': 11}

    with (T01 / 'data_derived' / 'tabla2_publicada.csv').open(encoding='utf-8-sig', newline='') as handle:
        published = list(csv.DictReader(handle))
    assert len(published) == 22
    article_lines = text(ARTICLE).splitlines()
    start = article_lines.index('Table 2.')
    finish = next(i for i in range(start, len(article_lines)) if '[p. 18]' in article_lines[i])
    entries = []
    pattern = re.compile(r'([−-]?\d+\.\d+) × 10([−-]?\d+)')
    for i in range(start, finish):
        match = pattern.fullmatch(article_lines[i].strip())
        if match:
            value = float(match[1].replace('−', '-')) * 10 ** int(match[2].replace('−', '-'))
            rank = int(article_lines[i + 1].strip().strip('()'))
            entries.append((value, rank, i + 1))
    assert len(entries) == 88
    transcription = []
    base = []
    for row in published:
        p, index = row['paciente'], int(row['indice_codigo'])
        for metric, log_metric in METRICS.items():
            value, rank, source_line = entries[len(base)]
            pub = float(row[f'g_{metric}'])
            pub_rank = int(row[f'rango_{metric}'])
            equal = math.isclose(pub, value, rel_tol=1e-14)
            transcription.append(dict(paciente=p, parametro=row['parametro'], metrica=metric,
                                      linea_articulo=source_line, valor_texto=value, valor_csv=pub,
                                      rango_texto=rank, rango_csv=pub_rank, valor_igual=equal, rango_igual=rank == pub_rank))
            base.append(dict(paciente=p, parametro=row['parametro'], indice=index, metrica=metric,
                             publicado=pub, rango_publicado=pub_rank, directo=lists[p, log_metric][index]))
    assert all(r['valor_igual'] and r['rango_igual'] for r in transcription)
    dump_csv('transcripcion_88.csv', transcription)
    rounded = {p: values.copy() for p, values in alpha.items()}
    rounded['P1'][:2] = [0.36, 5.2]
    rounded['P2'][:2] = [0.0038, 0.54]
    alternative_factors = {
        'directa': lambda p, i: 1,
        'alfa_div_100': lambda p, i: alpha[p][i] / 100,
        'por_alfa': lambda p, i: alpha[p][i],
        'div_100': lambda p, i: 0.01,
        'alfa_otro_paciente_div_100': lambda p, i: alpha['P2' if p == 'P1' else 'P1'][i] / 100,
        'alfa_tabla1_div_100': lambda p, i: rounded[p][i] / 100,
        'alfa_div_101': lambda p, i: alpha[p][i] / 101,
    }
    summaries, comparisons = {}, []
    for alternative, factor in alternative_factors.items():
        rows = []
        for b in base:
            scale = factor(b['paciente'], b['indice'])
            result = b['directo'] * scale
            error = abs(result - b['publicado']) / abs(b['publicado'])
            same_sign = result * b['publicado'] > 0
            rows.append(b | dict(alternativa=alternative, factor=scale, resultado=result, error_relativo=error,
                                 signo_igual=same_sign, redondeo_3cs_igual=float(format(result, '.3g')) == b['publicado']))
        for row in rows:
            group = sorted((r for r in rows if r['paciente'] == row['paciente'] and r['metrica'] == row['metrica']),
                           key=lambda r: abs(r['resultado']), reverse=True)
            row['rango_calculado'] = next(i + 1 for i, r in enumerate(group) if r['indice'] == row['indice'])
            row['rango_igual'] = row['rango_calculado'] == row['rango_publicado']
            err = row['error_relativo']
            row['clase_diagnostica'] = ('discrepancia' if not row['signo_igual'] or err > 0.5 else
                                       'reproducido' if err <= 0.1 and row['rango_igual'] else 'parcialmente reproducido')
        errors = [r['error_relativo'] for r in rows]
        summaries[alternative] = dict(n=88, error_mediana=statistics.median(errors), error_p90=quantile(errors, 0.9),
                                      error_max=max(errors), signos=sum(r['signo_igual'] for r in rows),
                                      rangos=sum(r['rango_igual'] for r in rows),
                                      tolerancia_signo=sum(r['error_relativo'] <= 0.1 and r['signo_igual'] for r in rows),
                                      tolerancia_signo_rango=sum(r['clase_diagnostica'] == 'reproducido' for r in rows),
                                      redondeo_3cs=sum(r['redondeo_3cs_igual'] for r in rows))
        comparisons.extend(rows)
    dump_csv('alternativas_616.csv', comparisons)
    dump_csv('alfa_verificacion.csv', [dict(paciente=p, indice=i, parametro_codigo=f, alfa=alpha[p][i],
                                         alfa_tabla1=rounded[p][i], vectores_log_coincidentes=vector_counts[p])
                                        for p in alpha for i, f in enumerate(FIELDS)])
    # Comparacion posterior al calculo propio; no se importa ningun comparador T01.
    comparison_tree = ast.parse(text(T01 / 'src' / 'compare_tabla2.py'))
    alpha_node = next(n.value for n in comparison_tree.body if isinstance(n, ast.Assign)
                      and any(isinstance(t, ast.Name) and t.id == 'ALPHA' for t in n.targets))
    alpha_t01 = {k.value: [numeric(x) for x in v.elts] for k, v in zip(alpha_node.keys, alpha_node.values)}
    assert alpha_t01 == alpha
    coherence = {}
    for filename, alternative in [('tabla2_resumen.json', 'directa'), ('tabla2_diag_escala_resumen.json', 'alfa_div_100')]:
        reference = json.loads(text(T01 / 'data_derived' / filename))
        mine = summaries[alternative]
        coherence[filename] = all(math.isclose(reference[k], mine[v], rel_tol=1e-12) for k, v in
                                 [('err_rel_mediana', 'error_mediana'), ('err_rel_p90', 'error_p90'),
                                  ('err_rel_max', 'error_max'), ('rangos_coinciden', 'rangos')])
    assert all(coherence.values())
    pk = json.loads(text(T01 / 'data_derived' / 'pk_check.json'))
    pk_pass = sum(v[k] <= 0.001 for v in pk.values() for k in ['err_rel_pico', 'err_rel_valle'])
    assert pk_pass == 3
    assert summaries['directa']['tolerancia_signo'] == 0
    assert summaries['alfa_div_100']['tolerancia_signo_rango'] == 88
    sources = [ARTICLE, log_path, T01 / 'data_derived' / 'tabla2_publicada.csv', REPO / 'parameters.py', REPO / 'local_sensitivity_analysis.py']
    summary = dict(alternativas=summaries, transcripcion_valores=88, transcripcion_rangos=88,
                   alfa_T01_coincide=alpha_t01 == alpha,
                   vectores_log=vector_counts, parametros_no_preservados=resets, coherencia_T01=coherence,
                   pk_extremos_cumplen=pk_pass, pk_extremos_total=6,
                   sha256_entradas={str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
                   limitacion='No simulaciones; no se identifica causalmente el postprocesado historico.')
    (OUT / 'revision_resumen.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print('VALIDACION: todas las aserciones superadas; 88 valores y 88 rangos contrastados.')


if __name__ == '__main__':
    main()