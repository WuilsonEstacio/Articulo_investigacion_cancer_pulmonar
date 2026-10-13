"""Validacion de solo lectura de los productos T03, sin importar codigo externo."""
import ast
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    for script in (ROOT / 'src').glob('*.py'):
        ast.parse(script.read_text(encoding='utf-8'), filename=str(script))
        print(f'Sintaxis correcta: {script}')
    summary = json.loads((ROOT / 'data_derived' / 'revision_resumen.json').read_text(encoding='utf-8'))
    assert summary['alfa_T01_coincide']
    for path, expected in summary['sha256_entradas'].items():
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == expected, path
    print('Las cinco entradas con hash conservan su contenido.')
    for filename, count in [('transcripcion_88.csv', 88), ('alfa_verificacion.csv', 22), ('alternativas_616.csv', 616)]:
        with (ROOT / 'data_derived' / filename).open(encoding='utf-8', newline='') as handle:
            rows = list(csv.DictReader(handle))
        assert len(rows) == count
        print(f'{filename}: {count} registros correctos.')
        if filename == 'transcripcion_88.csv':
            assert all(r['valor_igual'] == r['rango_igual'] == 'True' for r in rows)
        if filename == 'alternativas_616.csv':
            scaled = [r for r in rows if r['alternativa'] == 'alfa_div_100']
            assert len(scaled) == 88
            assert all(r['redondeo_3cs_igual'] == r['rango_igual'] == r['signo_igual'] == 'True' for r in scaled)
    report = (ROOT / 'REVISION_T03.md').read_text(encoding='utf-8')
    for section in ['## R1.', '## R2.', '## R3.', '## Hallazgos', '## Dictamen']:
        assert section in report
    assert 'OBJECIONES MAYORES' in report and 'R1: PLAUSIBLE' in report
    assert 'salida directa 0/88; H1 no se cumple' in report
    assert 'Pendiente:' not in report and 'Dictamen provisional' not in report
    assert (ROOT / 'sesion1_cortada' / 'REVISION_T03.md').is_file()
    for log in ['revision_independiente.log', 'revision_final.log']:
        assert 'exit_code=0' in (ROOT / 'logs' / log).read_text(encoding='utf-8-sig')
    print('Informe completo, clasificacion conservada y sesion anterior aislada.')
    for path in sorted(ROOT.rglob('*')):
        if path.is_file() and 'sesion1_cortada' not in path.parts:
            print(f'ENTREGA {path} ({path.stat().st_size} bytes)')
    print('VALIDACION FINAL: todas las comprobaciones superadas.')


if __name__ == '__main__':
    main()