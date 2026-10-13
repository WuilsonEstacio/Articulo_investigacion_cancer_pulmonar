"""Tercera ronda (Europe PMC): comparaciones de modelos clásicos de crecimiento con datos de ensayos de ICI. Uso: python -I busquedas_novedad_3.py <salida.json>"""
import sys, json, urllib.request, urllib.parse, datetime
sys.stdout.reconfigure(encoding="utf-8")
Q = {'B16_Laleh_modelos_clasicos': 'TITLE:"Classical mathematical models for prediction of response to chemotherapy and immunotherapy"',
     'B17_modelos_crecimiento_atezolizumab_datos_ensayo': '("tumor growth" OR "tumour growth" OR "tumor dynamics") AND (OAK OR POPLAR OR BIRCH OR FIR) AND atezolizumab AND (model)'}
out = {'fecha_consulta': datetime.datetime.now().isoformat(timespec='seconds'), 'busquedas': {}}
for k, q in Q.items():
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode({'query': q, 'format': 'json', 'pageSize': 6, 'resultType': 'core'})
    d = json.load(urllib.request.urlopen(url, timeout=60))
    recs = [{'titulo': r.get('title'), 'autores': (r.get('authorString') or '')[:120], 'anio': r.get('pubYear'), 'doi': r.get('doi'), 'pmcid': r.get('pmcid'), 'resumen': r.get('abstractText')} for r in d['resultList']['result']]
    out['busquedas'][k] = {'consulta': q, 'n_resultados': d.get('hitCount'), 'primeros': recs}
    print(f"\n### {k} (n={d.get('hitCount')})")
    for r in recs[:4]: print(f"- {r['anio']} | {r['titulo']} | {r['doi']} | {r['pmcid']}\n  {(r['resumen'] or '')[:1100]}")
json.dump(out, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
