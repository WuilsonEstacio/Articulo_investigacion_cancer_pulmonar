"""Genera las tablas del paper a partir de los CSV (sin transcripción manual) y las inserta entre marcadores:
  <!-- TABLA_88_INICIO --> ... <!-- TABLA_88_FIN -->   Tabla 4 (88 índices: publicado, crudo, ×α/100 y P2 corregido por H01)
  <!-- TABLA_H01_INICIO --> ... <!-- TABLA_H01_FIN -->   Tabla 5 (44 índices de P2: original frente a corregido), si existe el marcador
Uso: python -I tablas_paper.py <paper.md> <T01 data_derived/tabla2_comparacion.csv> [<T06 data_derived/t06_88_corregido.csv>]
"""
import sys, csv, re

paper, t01_csv = sys.argv[1], sys.argv[2]
t06_csv = sys.argv[3] if len(sys.argv) > 3 else None
SIM = {'lambda_P_pro': 'λ_P^pro', 'lambda_tau_eff': 'λ_τ^eff', 'lambda': 'λ', 'lambda_PN': 'λ_PN', 'sigma_PN': 'σ_PN',
       'c_m': 'c_m', 'eps_P': 'ε_P', 'c_Psi': 'c_Ψ', 'kappa_i': 'κ_i', 'alpha_H': 'α_H', 'alpha_P': 'α_P'}
QOI = {'g_phiT': 'φ_T', 'g_phiP': 'φ_P', 'g_phiN': 'φ_N', 'g_Vvis': 'V_vis'}

t01 = list(csv.DictReader(open(t01_csv, encoding='utf-8')))
t06 = {(r['paciente'], r['parametro'], r['indice']): r for r in csv.DictReader(open(t06_csv, encoding='utf-8'))} if t06_csv else {}


def e(x, n=3):
    return f'{float(x):.{n}e}'.replace('e-0', 'e-').replace('e+0', 'e+')


def pct(x):
    return f'{100 * float(x):.3f} %'


lin = ['**Table 4. Local sensitivity indices: published values vs released-script output (raw), rescaled ×α/100, and (P2) '
       'rescaled after correcting H01.** Published values are those of Table 2 of Wagner et al. [2023] (CC BY 4.0), with ranks in parentheses. '
       'Rel. err. = |g − g_pub|/|g_pub|. Δ_H01 = (g_corr − g_orig)/|g_orig|. '
       f'Source: `tabla2_comparacion.csv`{" and `t06_88_corregido.csv`" if t06 else ""}.',
       '',
       '| Pt | Parameter | QoI | Published (rank) | Raw script | ×α/100 | Rel. err. | P2 corrected ×α/100 (rank) | Rel. err. | Δ_H01 |',
       '|---|---|---|---|---|---|---|---|---|---|']
for r in t01:
    k = (r['paciente'], r['parametro'], r['indice'])
    g_esc = float(r['g_script']) * float(r['alpha_defecto']) / 100
    err = abs(g_esc - float(r['g_publicado'])) / abs(float(r['g_publicado']))
    if r['paciente'] == 'P2' and k in t06:
        c = t06[k]
        extra = f"{e(c['g_esc_corr'], 3)} ({c['rango_corr']}) | {pct(c['err_pub_corr'])} | {100 * float(c['delta_rel']):+.3f} %"
    elif r['paciente'] == 'P2':
        extra = '[PENDING] | | '
    else:
        extra = '— (not affected) | | '
    lin.append(f"| {r['paciente']} | {SIM[r['parametro']]} | {QOI[r['indice']]} | {e(r['g_publicado'], 2)} ({r['rango_publicado']}) | "
               f"{e(r['g_script'], 3)} | {e(g_esc, 3)} | {pct(err)} | {extra} |")
bloque88 = '\n'.join(lin)

bloqueH01 = None
if t06:
    lin = ['**Table 5. Patient 2: sensitivity indices (×α/100) with the original configuration (H01) and after correction.** '
           'Ranks by |g| within each QoI. Published values: Wagner et al. [2023], Table 2 (CC BY 4.0). Source: `t06_p2_indices.csv`.', '',
           '| Parameter | QoI | Original (rank) | Corrected (rank) | Δ_H01 | Published (rank) |', '|---|---|---|---|---|---|']
    for r in t01:
        k = (r['paciente'], r['parametro'], r['indice'])
        if r['paciente'] != 'P2':
            continue
        c = t06[k]
        lin.append(f"| {SIM[r['parametro']]} | {QOI[r['indice']]} | {e(c['g_esc_orig'], 3)} ({c['rango_orig']}) | "
                   f"{e(c['g_esc_corr'], 3)} ({c['rango_corr']}) | {100 * float(c['delta_rel']):+.3f} % | "
                   f"{e(c['g_publicado'], 2)} ({c['rango_publicado']}) |")
    bloqueH01 = '\n'.join(lin)

txt = open(paper, encoding='utf-8').read()


def poner(txt, nombre, bloque):
    patron = re.compile(rf'(<!-- {nombre}_INICIO -->)(.*?)(<!-- {nombre}_FIN -->)', re.S)
    if not patron.search(txt):
        return txt, False
    return patron.sub(lambda m: m.group(1) + '\n' + bloque + '\n' + m.group(3), txt), True


txt, ok88 = poner(txt, 'TABLA_88', bloque88)
okH = False
if bloqueH01:
    txt, okH = poner(txt, 'TABLA_H01', bloqueH01)
open(paper, 'w', encoding='utf-8').write(txt)
print('TABLA_88:', ok88, '| TABLA_H01:', okH, '| filas T06:', len(t06))
