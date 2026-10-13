"""Segunda ronda de búsquedas (Europe PMC): datos abiertos del grupo Kuttler/Schlicke y replicaciones. Uso: python -I busquedas_novedad_2.py <salida.json>"""
import sys, json, urllib.request, urllib.parse, datetime
sys.stdout.reconfigure(encoding="utf-8")
Q = {
 'B11_Schlicke_Kuttler_Schumann': 'AUTH:"Schlicke P" AND AUTH:"Kuttler C"',
 'B12_Kuttler_NSCLC_inmunoterapia': 'AUTH:"Kuttler C" AND (immunotherapy OR "checkpoint") AND (lung OR NSCLC)',
 'B13_replicacion_ABM_EGFR': '(replication OR reproduction OR reproducibility OR "re-implementation") AND ("agent-based" OR multiscale) AND EGFR AND "lung cancer"',
 'B14_reproducibilidad_modelos_oncologia': '(reproducibility OR replicability) AND ("mathematical oncology" OR "computational oncology" OR "tumor growth model")',
 'B15_ADRIATIC_extrapolacion_cura': '(ADRIATIC OR "limited-stage small cell") AND (durvalumab) AND ("cure model" OR "mixture cure" OR "restricted mean survival" OR "non-proportional hazards" OR extrapolation)',
}
out = {'fecha_consulta': datetime.datetime.now().isoformat(timespec='seconds'), 'servicio': 'Europe PMC REST search', 'busquedas': {}}
for k, q in Q.items():
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode({'query': q, 'format': 'json', 'pageSize': 12, 'resultType': 'lite', 'sort': 'P_PDATE_D desc'})
    d = json.load(urllib.request.urlopen(url, timeout=60))
    recs = [{f: r.get(f) for f in ('title','authorString','pubYear','journalTitle','doi','pmid','pmcid','citedByCount')} for r in d['resultList']['result']]
    out['busquedas'][k] = {'consulta': q, 'orden': 'fecha desc', 'n_resultados': d.get('hitCount'), 'primeros': recs}
    print(f"\n### {k}  (n={d.get('hitCount')})")
    for r in recs: print(f"  - {r['pubYear']} | {(r['title'] or '')[:120]} | {r['journalTitle']} | {r['doi']} | {r['pmcid']}")
json.dump(out, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
