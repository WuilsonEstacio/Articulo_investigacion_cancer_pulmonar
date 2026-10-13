"""Consulta Crossref: relaciones de actualización (errata/retractación vía 'updated-by'/'update-to') y relaciones de preprint.
Uso: python -I consulta_crossref.py <salida.json>"""
import sys, json, urllib.request, datetime
DOIS = {'D01':'10.3390/jpm14050475','D02_pub':'10.3934/mbe.2023828','D02_preprint':'10.1101/2023.03.20.533400',
        'D03':'10.1186/s12964-023-01332-9','D04':'10.1056/NEJMoa2404873','D05':'10.3390/curroncol32030146',
        'D06':'10.3390/ijms241914516','D07':'10.18632/oncotarget.25360','D08':'10.1056/NEJMoa1102873',
        'D09':'10.1056/NEJMoa1911793','D10':'10.1186/1742-4682-4-50'}
out = {'fecha_consulta': datetime.datetime.now().isoformat(timespec='seconds'), 'servicio': 'https://api.crossref.org/works/{doi}', 'resultados': {}}
for k, doi in DOIS.items():
    try:
        m = json.load(urllib.request.urlopen(urllib.request.Request('https://api.crossref.org/works/' + doi, headers={'User-Agent': 'research-inventory/1.0'}), timeout=60))['message']
        rec = {'titulo': (m.get('title') or [''])[0], 'revista': (m.get('container-title') or [''])[0], 'emitido': m.get('issued'),
               'updated_by': m.get('updated-by'), 'update_to': m.get('update-to'), 'relation': m.get('relation'),
               'volumen': m.get('volume'), 'paginas': m.get('page'), 'articulo': m.get('article-number')}
    except Exception as e:
        rec = {'error': str(e)}
    out['resultados'][k] = {'doi': doi, **rec}
    print(k, doi, rec.get('revista'), rec.get('volumen'), rec.get('paginas') or rec.get('articulo'), '| updated_by:', rec.get('updated_by'), '| relation:', list((rec.get('relation') or {}).keys()))
json.dump(out, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
