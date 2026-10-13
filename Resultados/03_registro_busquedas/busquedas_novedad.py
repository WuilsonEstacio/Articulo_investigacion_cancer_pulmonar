"""Búsquedas de contraste de novedad en Europe PMC. Registra consulta, fecha, n de resultados y los 8 primeros (orden por relevancia).
Uso: python -I busquedas_novedad.py <salida.json>"""
import sys, json, urllib.request, urllib.parse, datetime
sys.stdout.reconfigure(encoding="utf-8")
Q = {
 'B01_grupo_phasefield': 'AUTH:"Schlicke P" AND (lung OR NSCLC)',
 'B02_phasefield_citas': 'CITES:38052574_MED',
 'B03_crecimiento_ICI_modelos_clasicos': '(TITLE:"tumor growth" OR TITLE:"tumour growth" OR TITLE:"mathematical model") AND (immunotherapy OR "immune checkpoint") AND ("non-small cell lung" OR NSCLC) AND (Gompertz OR logistic OR exponential)',
 'B04_ADRIATIC_reconstruccion': '(ADRIATIC OR "limited-stage small-cell") AND durvalumab AND ("cost-effectiveness" OR "partitioned survival" OR "reconstructed" OR "individual patient data")',
 'B05_ADRIATIC_actualizacion': 'ADRIATIC AND durvalumab AND "limited-stage" AND (PUB_YEAR:2025 OR PUB_YEAR:2026)',
 'B06_NELSON_NLST_microsimulacion': '(NELSON OR NLST) AND (microsimulation OR "natural history model") AND ("lung cancer" ) AND (calibrat* OR validat*)',
 'B07_Wang2007_citas': 'CITES:18154660_MED',
 'B08_NLST_seguimiento_extendido': 'NLST AND ("extended follow-up" OR "long-term follow-up") AND "lung cancer mortality"',
 'B09_NELSON_sobrediagnostico': 'NELSON AND overdiagnosis AND "lung cancer"',
 'B10_ICI_crecimiento_reanalisis_ensayos': '"tumor growth inhibition" AND (atezolizumab OR durvalumab OR pembrolizumab) AND ("lung cancer" OR NSCLC) AND (model)',
}
out = {'fecha_consulta': datetime.datetime.now().isoformat(timespec='seconds'), 'servicio': 'Europe PMC REST search', 'busquedas': {}}
for k, q in Q.items():
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode({'query': q, 'format': 'json', 'pageSize': 8, 'resultType': 'lite'})
    d = json.load(urllib.request.urlopen(url, timeout=60))
    recs = [{f: r.get(f) for f in ('title','authorString','pubYear','journalTitle','doi','pmid','pmcid','citedByCount')} for r in d['resultList']['result']]
    out['busquedas'][k] = {'consulta': q, 'n_resultados': d.get('hitCount'), 'primeros': recs}
    print(f"\n### {k}  (n={d.get('hitCount')})  {q}")
    for r in recs: print(f"  - {r['pubYear']} | {(r['title'] or '')[:115]} | {r['journalTitle']} | {r['doi']} | cit {r['citedByCount']}")
json.dump(out, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
