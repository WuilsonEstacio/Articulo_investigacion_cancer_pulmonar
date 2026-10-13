"""Recupera resúmenes (Europe PMC) de trabajos externos clave para el contraste de novedad. Uso: python -I resumenes_clave.py <salida.json>"""
import sys, json, urllib.request, urllib.parse, datetime
sys.stdout.reconfigure(encoding="utf-8")
DOIS = ['10.1016/j.mbs.2024.109287','10.1038/s41416-025-03306-9','10.1007/s10585-023-10245-3','10.1038/s41467-025-63471-6',
        '10.1002/ijc.70045','10.64898/2026.09.10.26362768','10.1016/j.lana.2026.101476','10.1093/oncolo/oyag009',
        '10.1016/j.jtocrr.2025.100879','10.1200/go-25-00225','10.1208/s12248-026-01295-y','10.3934/mbe.2023828']
out = {'fecha_consulta': datetime.datetime.now().isoformat(timespec='seconds'), 'registros': []}
for doi in DOIS:
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode({'query': f'DOI:"{doi}"', 'format': 'json', 'resultType': 'core'})
    r = json.load(urllib.request.urlopen(url, timeout=60))['resultList']['result']
    if not r: print('SIN REGISTRO', doi); continue
    r = r[0]
    rec = {'doi': doi, 'titulo': r.get('title'), 'autores': r.get('authorString'), 'anio': r.get('pubYear'),
           'revista': r.get('journalInfo', {}).get('journal', {}).get('title'), 'pmid': r.get('pmid'), 'pmcid': r.get('pmcid'), 'resumen': r.get('abstractText')}
    out['registros'].append(rec)
    print(f"\n=== {rec['anio']} {rec['revista']} {doi} PMID {rec['pmid']} {rec['pmcid']}\n{rec['titulo']}\n{rec['autores'][:150]}\n{(rec['resumen'] or 'SIN RESUMEN')[:1800]}")
json.dump(out, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
