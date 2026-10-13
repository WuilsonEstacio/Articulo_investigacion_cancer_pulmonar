"""Consulta Europe PMC (REST) para cada documento del inventario: identificadores, tipo de publicación,
correcciones/retractaciones (commentCorrectionList), citas y disponibilidad de texto completo.
Uso: python -I consulta_europepmc.py <salida.json>"""
import sys, json, urllib.request, urllib.parse, datetime
sys.stdout.reconfigure(encoding="utf-8")
Q = {
 'D01': 'DOI:"10.3390/jpm14050475"',
 'D02': 'TITLE:"phase-field model for non-small cell lung cancer under the effects of immunotherapy"',
 'D03': 'DOI:"10.1186/s12964-023-01332-9"',
 'D04': 'DOI:"10.1056/NEJMoa2404873"',
 'D05': 'DOI:"10.3390/curroncol32030146"',
 'D06': 'DOI:"10.3390/ijms241914516"',
 'D07': 'TITLE:"Modeling small cell lung cancer (SCLC) biology through deterministic and stochastic mathematical models"',
 'D08': 'DOI:"10.1056/NEJMoa1102873"',
 'D09': 'DOI:"10.1056/NEJMoa1911793"',
 'D10': 'TITLE:"Simulating non-small cell lung cancer with a multiscale agent-based model"',
}
out = {'fecha_consulta': datetime.datetime.now().isoformat(timespec='seconds'), 'servicio': 'https://www.ebi.ac.uk/europepmc/webservices/rest/search', 'resultados': {}}
for k, q in Q.items():
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode({'query': q, 'resultType': 'core', 'format': 'json', 'pageSize': 5})
    d = json.load(urllib.request.urlopen(url, timeout=60))
    res = []
    for r in d['resultList']['result']:
        res.append({f: r.get(f) for f in ('title','authorString','pubYear','doi','pmid','pmcid','source','isOpenAccess','citedByCount','pubTypeList','hasSuppl','hasData')} |
                   {'journal': r.get('journalInfo',{}).get('journal',{}).get('title'),
                    'correcciones': r.get('commentCorrectionList')})
    out['resultados'][k] = {'consulta': q, 'n': d.get('hitCount'), 'registros': res}
    for x in res[:2]:
        cc = x['correcciones']
        print(k, x['pubYear'], x['doi'], x['pmid'], x['pmcid'], x['journal'], 'citas', x['citedByCount'], '|', (x['title'] or '')[:70])
        if cc: print('    CORRECCIONES:', json.dumps(cc)[:400])
json.dump(out, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
