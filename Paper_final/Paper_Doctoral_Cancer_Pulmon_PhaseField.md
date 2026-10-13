# Computational Reproducibility Audit of a Published Phase-Field Model of Non-Small Cell Lung Cancer under Anti-PD-1 Immunotherapy (Wagner et al., 2023): Pharmacokinetic Verification, Sensitivity-Index Rescaling and a Configuration Defect

**Author:** Wuilson Estacio

> **Manuscript status (internal).** Working draft v0.3, 13 October 2026 (T06 results and companion documents integrated). All numerical results come from logged executions in `Resultados/` and are traceable through the table in Supplementary S4. Statements tagged **[PENDING]** depend on analyses not yet completed. Status and gaps: `Paper_final/Estado_Paper_Doctoral_brechas.md`. The model audited here, its equations, parameter values, patient data and code are the work of Wagner et al. [2023]; this manuscript contributes only the audit. Novelty has not been verified (Scibilia et al. [2024] not yet read in full), and re-use of the patient data for publication requires confirmation from the original authors (§7.3).
>
> **Companion documents.** The evidence behind this draft is documented in [METODOLOGIA_SIMULACIONES_Y_COLABORACION_IA.md](METODOLOGIA_SIMULACIONES_Y_COLABORACION_IA.md) (simulations, environment, commands and the division of work between the researcher and the AI agents), [INFORME_INTEGRADO_F0_F1.md](INFORME_INTEGRADO_F0_F1.md) (verified results and traceability) and [Primera_entrega_contribuciones_y_plan.md](Primera_entrega_contribuciones_y_plan.md) (hypotheses and tolerances fixed before execution). See §7.6 for what each supports.

## Table of Contents

- [Abstract](#abstract)
- [1. Introduction](#1-introduction)
  - [1.1 Clinical context](#11-clinical-context)
  - [1.2 Phase-field models of tumour growth](#12-phase-field-models-of-tumour-growth)
  - [1.3 The model audited and why reproducibility matters](#13-the-model-audited-and-why-reproducibility-matters)
  - [1.4 Objectives and contribution](#14-objectives-and-contribution)
- [2. Mathematical and Pharmacokinetic Framework](#2-mathematical-and-pharmacokinetic-framework)
  - [2.1 Phase-field equations](#21-phase-field-equations)
  - [2.2 Pharmacokinetic coupling](#22-pharmacokinetic-coupling)
  - [2.3 Local sensitivity indices and the α/100 factor](#23-local-sensitivity-indices-and-the-100-factor)
  - [2.4 The H01 configuration defect](#24-the-h01-configuration-defect)
- [3. Computational Implementation and Reproducibility Audit](#3-computational-implementation-and-reproducibility-audit)
  - [3.1 Containerised execution environment](#31-containerised-execution-environment)
  - [3.2 Pre-specified reproduction criteria](#32-pre-specified-reproduction-criteria)
  - [3.3 Verification protocol](#33-verification-protocol)
  - [3.4 Article–code correspondence](#34-articlecode-correspondence)
- [4. Results and Comparative Discussion](#4-results-and-comparative-discussion)
  - [4.1 Pharmacokinetics](#41-pharmacokinetics)
  - [4.2 Table 2: published, raw and rescaled indices](#42-table-2-published-raw-and-rescaled-indices)
  - [4.3 Impact of correcting H01 on the sensitivity of patient 2](#43-impact-of-correcting-h01-on-the-sensitivity-of-patient-2)
  - [4.4 Discussion](#44-discussion)
- [5. Proposed Pipeline for Personalised Therapy](#5-proposed-pipeline-for-personalised-therapy)
- [6. Conclusions and Future Work](#6-conclusions-and-future-work)
- [7. Declarations](#7-declarations)
  - [7.1 Data and code availability](#71-data-and-code-availability)
  - [7.2 Ethics](#72-ethics)
  - [7.3 Licensing and permissions (blocking for publication)](#73-licensing-and-permissions-blocking-for-publication)
  - [7.4 Use of AI tools](#74-use-of-ai-tools)
  - [7.5 Author contributions and funding](#75-author-contributions-and-funding)
  - [7.6 Companion documents and evidence map](#76-companion-documents-and-evidence-map)
  - [7.7 Reuse of third-party material and attribution](#77-reuse-of-third-party-material-and-attribution)
- [References](#references)
- [Supplementary material](#supplementary-material)
  - [S5. Step-by-step reproduction on another computer](#s5-step-by-step-reproduction-on-another-computer)

---

## Abstract

**Background.** Patient-specific phase-field models of tumour growth under immunotherapy are increasingly proposed as building blocks for therapy optimisation in non-small cell lung cancer (NSCLC). Their value depends on whether published results can be regenerated from the released code and data. We audited the computational reproducibility of a published Cahn–Hilliard-type model of NSCLC under anti-PD-1 therapy (Wagner et al., *Math. Biosci. Eng.* 2023), which couples proliferative and necrotic tumour phases, a stationary nutrient field, and a one-compartment antibody pharmacokinetic (PK) model.

**Methods.**
- The authors' unmodified code (FEniCS/dolfin 2019.1.0) was executed in a version-locked Docker container.
- Pre-specified tolerances were applied to:
  - (i) the PK model, against its closed-form solution;
  - (ii) the 88 local sensitivity indices of the published Table 2 (11 parameters × 4 quantities of interest × 2 patients);
  - (iii) a 35-item correspondence between article and code.
- An independent reviewer (a second AI agent with its own code) audited the analysis.
- A defect it found in the sensitivity script was corrected in a declared variant and its effect was quantified. The defect: the perturbed simulations of patient 2 revert to default PK parameters (H01).

**Results.**
- **PK:** the ODE and the total delivered dose were reproduced exactly. The pre-specified 0.1 % peak/trough tolerance was met in 3 of 6 extrema, owing to a half-substep shift of the infusion window.
- **Table 2, script output:** 0/88 published indices were reproduced (median relative error ≈ 2.3 × 10⁴ %), so the pre-specified reproduction hypothesis was rejected.
- **Table 2, rescaled (diagnostic):** the script returns $\partial_\alpha\bar Q/\bar Q$. Multiplying by $\alpha/100$, the factor implied by the verbal definition of the article's Eq. 4.1, recovered all 88 printed values at three significant figures and all 88 ranks (maximum relative error 0.449 %). Of seven candidate transformations, only this one did so. The agreement supports, but does not prove, how the published table was generated.
- **H01:** the perturbed simulations of patient 2 used the drug parameters of patient 1. Re-running P2 with its own PK parameters changed its 44 indices by a median of 12.6 % (maximum 45.2 %), with no sign changes. 7 of 11 visible-volume ranks were reordered, which is a "relevant" effect under pre-specified thresholds. A determinism control reproduced the original output bit-for-bit, so the change is attributable to the correction alone. The corrected P2 values match the published table in only 1 of 44 cases, consistent with the published values carrying the defect.
- **Article–code correspondence:** nine further discrepancies, including an undeclared factor of 0.7 in the drug-kill term and offsets of 26–157 days in the therapy schedules.

**Conclusions.**
- The published sensitivity analysis can be regenerated only after a post-processing step that the released script does not contain.
- For one of its two patients, the published indices carry a configuration defect that shifts them by up to 45 % and reorders the visible-volume parameter ranking.
- These findings, together with n = 2 manually calibrated patients, mean the model's parameters cannot yet support dose optimisation. Pharmacokinetic and tumour-parameter calibration with identifiability analysis is the necessary next step.
- We propose a staged pipeline linking imaging data to likelihood-based calibration and out-of-time validation before any therapeutic use.

**Keywords:** non-small cell lung cancer; phase-field model; Cahn–Hilliard; immunotherapy; pharmacokinetics; computational reproducibility; sensitivity analysis; Docker.

---

## 1. Introduction

### 1.1 Clinical context

- **Burden.** Lung cancer is the leading cause of cancer death worldwide. About 85 % of cases are NSCLC, with a five-year survival of roughly 22 % [Bray 2018, as cited in Wagner 2023, ref. 19].
- **Treatment.** NSCLC is treated with surgery, chemotherapy, radiotherapy and, increasingly, immunotherapy [Zappa & Mousa 2016].
- **Immune checkpoint inhibitors.** Monoclonal antibodies against PD-1 (nivolumab, pembrolizumab) restore T-cell effector activity that tumour cells suppress through PD-L1/PD-L2 expression [Wagner 2023, §1].
- **Response heterogeneity.** Responses to these drugs differ widely between patients. Predicting a given patient's tumour trajectory under a given schedule remains an open problem [Wagner 2023, §1; Rockne & Scott 2019].
- **Population evidence.** Screening trials document the scale of the disease at population level: low-dose CT screening reduced lung-cancer mortality by 20.0 % versus chest radiography in the NLST [NLST 2011] and by 24 % versus no screening in NELSON men at 10 years [de Koning 2020]. This evidence does not bear directly on individual on-treatment dynamics, which is the scale addressed here.

### 1.2 Phase-field models of tumour growth

- **Diffuse-interface representation.** Phase-field (diffuse-interface) models represent tissue constituents as volume fractions $\phi(\mathbf x,t)\in[0,1]$ that change across interfaces of finite width $\varepsilon$.
  - **Cahn–Hilliard equation** [Cahn & Hilliard 1958]: a conserved $H^{-1}$ gradient flow of a Ginzburg–Landau free energy [Ginzburg & Landau 1950] $\int\Psi(\phi)+\tfrac{\varepsilon^2}{2}|\nabla\phi|^2$. It models phase separation and cell–cell adhesion with mass conservation, to which reaction terms add growth and death.
  - **Allen–Cahn equation** [Allen & Cahn 1979]: the non-conserved $L^2$ counterpart. It is used when the phase variable is not a conserved quantity.
- **Tumour modelling.** Multispecies Cahn–Hilliard systems coupled to nutrient and drug transport are an established family [Cristini & Lowengrub 2010; Lowengrub et al. 2009]. Two-species models with nutrient coupling have been analysed and verified [Garcke et al. 2016; Frigeri et al. 2015; Lee et al. 2015], extended to ten species [Lima et al. 2014] and coupled to 1D vascular networks [Fritz et al. 2021].
- **Numerics.** Their numerical treatment typically relies on convex–concave splitting for unconditional energy stability [Eyre 1998] and on finite elements [Logg et al. 2012].

### 1.3 The model audited and why reproducibility matters

Wagner et al. [2023] proposed a model of this type and calibrated it to longitudinal CT volumetry of NSCLC patients under anti-PD-1 therapy. The model, its equations, parameter values, patient data and code are their work [Wagner 2023; Wagner 2023, preprint; Wagner 2023, code repository]; this paper audits them and does not propose a new model.
- **Data:** two patients (P1: nivolumab Q2W; P2: pembrolizumab Q3W→Q6W), released with the code.
- **Parameters:** four patient-specific parameters were tuned manually ($\lambda_P^{pro}$, $\lambda_\tau^{eff}$, $\lambda$, $\lambda_{PN}$).
- **Analysis:** a local sensitivity analysis (their Table 2) was reported to rank parameter influence. The authors themselves identify parameter estimation and identifiability as open problems [Wagner 2023].

Because such models are candidates for in-silico dose exploration, any downstream use (calibration, identifiability, dose optimisation) requires first establishing that the published numbers can be regenerated from the released artefacts.

### 1.4 Objectives and contribution

**Objectives:**
- **O1.** Execute the released code unmodified in a locked environment, and test pre-specified reproduction criteria for the PK model and for all 88 sensitivity indices.
- **O2.** Explain any discrepancy diagnostically, without altering the pre-specified classification.
- **O3.** Subject the analysis to independent review, and quantify the effect of any defect found.
- **O4.** On that basis, define what is required before the model can support pharmacokinetic calibration and therapeutic optimisation.

**Contributions:**
- A fully logged, containerised reproduction of the published model.
- The identification of the exact transformation linking the released script to the published Table 2.
- The discovery and quantification of a configuration defect (H01) in the published sensitivity analysis.
- A staged roadmap toward calibrated, validated use.

---

## 2. Mathematical and Pharmacokinetic Framework

Equations (1)–(4), the parameter values of Table 1 and the notation are reproduced from the published article [Wagner 2023, §2 and Table 1], which is distributed under a Creative Commons Attribution 4.0 (CC BY 4.0) licence. Equation (5) restates their sensitivity definition (their Eq. 4.1); Eqs. (6)–(8) describe our reading of their released code [Wagner 2023, code repository]. Departures in the released code are listed in §3.4.

### 2.1 Phase-field equations

**Species and domain.** Let $\Omega$ be a lung-tissue domain containing:
- proliferative ($\phi_P$) and necrotic ($\phi_N$) tumour volume fractions, with total tumour $\phi_T=\phi_P+\phi_N$ and healthy tissue $\phi_H=1-\phi_T$;
- vascular ($\phi_{\sigma,v}$) and interstitial ($\phi_{\sigma,i}$) nutrient concentrations;
- an immunotherapeutic agent ($\phi_\tau$).

**Proliferative phase.** It evolves by a generalised Cahn–Hilliard system:

$$
\partial_t\phi_P=\nabla\cdot\big(c_m\,m_P(\phi_P,\phi_T)\nabla\mu_P\big)+S_P(\phi_P,\phi_{\sigma,i},\phi_\tau),\qquad
\mu_P=\partial_{\phi_P}\Psi(\phi_P,\phi_T)-\varepsilon_P^2\Delta\phi_P-\chi\,\phi_{\sigma,i},
\tag{1}
$$

with homogeneous Neumann conditions for $\phi_P$ and $\mu_P$, and:
- the double-well potential $\Psi=\tilde\Psi(\phi_P)+\tilde\Psi(\phi_T)$, with $\tilde\Psi(\phi)=c_\Psi\phi^2(1-\phi)^2$;
- the degenerate mobility $m_P=(\phi_P^+)^2(1-\phi_T^+)^2$, where $(\cdot)^+$ is a cut-off to $[0,1]$.

**Reaction term:**

$$
S_P=\lambda_P^{pro}\,\phi_{\sigma,i}\,(\phi_P^+)^{\lambda}\ln\!\frac{1+\epsilon_g}{\phi_P^++\epsilon_g}
\;-\;\frac{\lambda_\tau^{eff}}{\omega}\,\phi_P\,\frac{\phi_\tau}{\phi_\tau+\phi_\tau^{50}}
\;-\;\lambda_{PN}\,H(\sigma_{PN}-\phi_{\sigma,i})\,\phi_P ,
\tag{2}
$$

The three terms are:
- Gompertzian [Gompertz 1825], nutrient-driven growth, in which $\lambda\ge1$ penalises growth at low concentrations;
- an Emax (Hill–Langmuir) kill term driven by the drug [Hill 1910];
- hypoxic conversion to necrosis below the nutrient threshold $\sigma_{PN}$.

**Necrotic phase:** $\partial_t\phi_N=\lambda_{PN}H(\sigma_{PN}-\phi_{\sigma,i})\phi_P$.

**Nutrients:** quasi-stationary reaction–diffusion. In the reduced model, the interstitial equation is

$$
-\kappa_i\,\nabla^2\phi_{\sigma,i}=\eta_{vi}\phi_{\sigma,v}-\eta_{iv}\phi_{\sigma,i}-\alpha_H(1-\phi_P-\phi_N)\phi_{\sigma,i}-\alpha_P\phi_P\phi_{\sigma,i}.
\tag{3}
$$

**Reduced 1D model** (used throughout this work). Spherical symmetry gives the radial versions of (1)–(3), with the measure $4\pi r^2dr$ in the weak form. Settings:
- radius 4 cm;
- piecewise-linear finite elements [Logg et al. 2012; Logg & Wells 2010];
- time step 1/24 d, with 32 PK substeps;
- semi-implicit time stepping with convex–concave splitting [Eyre 1998].

**Observable.** The visible tumour volume is $V_{vis}(t)=\int_\Omega\mathbf 1\{\phi_T>0.3\}\,d\mathbf x$, compared with CT volumetry.

### 2.2 Pharmacokinetic coupling

The antibody amount in the lung follows a one-compartment linear model with first-order elimination and zero-order infusion:

$$
\partial_t\phi_\tau=-\frac{\ln 2}{t_{1/2}}\,\phi_\tau+\frac{N_A}{M_\tau}\,d_\tau\,\mathbf 1_{t\in I_\tau},
\tag{4}
$$

Its terms:
- $t_{1/2}$ is the serum half-life;
- $M_\tau$ is the molar mass;
- $d_\tau$ is the dose per administration;
- $N_A$ is Avogadro's number;
- $I_\tau$ is the union of 1-h infusion windows given by each patient's schedule:
  - P1: every 14 d from $t_S$;
  - P2: every 21 d, then every 42 d from $t_{Q6W}$ until $t_{PD}$.

Drug action enters (2) through $\phi_\tau/(\phi_\tau+\phi_\tau^{50})$, scaled by the lung-to-body weight ratio $1/\omega$.

**Table 1. Pharmacokinetic and patient-specific parameters (1D model, published values).** Reproduced from Wagner et al. [2023], Table 1 (CC BY 4.0).

| Symbol | Meaning | P1 | P2 |
|---|---|---|---|
| $d_\tau$ | dose per administration (g) | 0.24 | 0.20 |
| $M_\tau$ | molar mass (g/mol) | 146 000 | 143 600 |
| $t_{1/2}$ | serum half-life (d) | 26.7 | 22.0 |
| $\phi_\tau^{50}$ | half-maximal drug amount (molecules) | 1.012 × 10¹⁶ | 1.012 × 10¹⁶ |
| $\omega$ | body-to-lung weight ratio | 80 | 80 |
| $\lambda_P^{pro}$ (1/d) | proliferation rate | 0.36 | 0.0038 |
| $\lambda_\tau^{eff}$ (1/d) | immunotherapeutic effect | 5.2 | 0.54 |
| $\lambda$ | growth power law | 2 | 1 |
| $\lambda_{PN}$ (1/d) | proliferative→necrotic rate | 0.1 | 20 |

Shared parameters: $c_m=5\times10^{-4}$, $\varepsilon_P=5\times10^{-4}$, $c_\Psi=2$, $\sigma_{PN}=0.2$, $\kappa_i=10^{-5}$, $\alpha_H=1$, $\alpha_P=4$, $\epsilon_g=0.1$, $\chi=0$.

The P1 PK values correspond to nivolumab and the P2 values to pembrolizumab [Wagner 2023, Table 1 and ref. 16].

### 2.3 Local sensitivity indices and the α/100 factor

**Published definition.** For a scalar field $f\in\{\phi_T,\phi_P,\phi_N,V_{vis}\}$, define the time-averaged mass $\bar Q(f)=\tfrac1T\int_0^T\!\int_\Omega f\,d\mathbf x\,dt$. The article defines the local sensitivity index of parameter $\alpha$ as

$$
g_{f,\alpha}:=\frac{\partial_\alpha\bar Q(f)}{\bar Q(f)}\cdot\frac{\alpha}{100\,\%},
\tag{5}
$$

and describes it in words as "the relative change [of $\bar Q$] up to first order when varying $\alpha$ by 1 percent" [Wagner 2023, p. 16].

**Interpretation of the factor.** A first-order Taylor expansion with $\Delta\alpha=0.01\,\alpha$ gives $\Delta\bar Q/\bar Q\approx(\partial_\alpha\bar Q/\bar Q)\,\alpha/100$. This is the reading adopted here.
- Read literally with "100 %" = 1, Eq. (5) would instead be the elasticity $(\partial_\alpha\bar Q/\bar Q)\,\alpha$.
- The verbal definition and the published values (§4.2) both support the $\alpha/100$ reading.
- Under that reading, $g=0.011$ means that $\bar Q$ changes by about 1.1 % when $\alpha$ changes by 1 %.

**What the released script computes** (`local_sensitivity_analysis.py`, ll. 101–104):

$$
g^{\text{script}}_{f,\alpha}=\frac{\bar Q\big(f;\alpha(1+h)\big)-\bar Q\big(f;\alpha(1-h)\big)}{2h\,\alpha\,\bar Q(f;\alpha)}\;\approx\;\frac{\partial_\alpha\bar Q}{\bar Q},\qquad h=10^{-3},
\tag{6}
$$

with time integrals evaluated by the trapezoidal rule. Hence

$$
g^{\text{published}}\;\overset{?}{=}\;g^{\text{script}}\cdot\frac{\alpha}{100}.
\tag{7}
$$

**Status of (7).** Equation (7) is a **hypothesis** about how the published table was produced, tested in §4.2. The factor $\alpha/100$ is a definitional rescaling of a sensitivity index. **It is not a calibrated model parameter.**

### 2.4 The H01 configuration defect

**What the code does.**
- In the released script, the reference simulation of P2 uses the patient's PK parameters ($M_\tau=143\,600$, $d_\tau=0.20$, $t_{1/2}=22$).
- The perturbed simulations are rebuilt from an 11-component parameter vector that does not contain these fields (`vector_to_parameters`, ll. 35–48) [Wagner 2023, code repository].
- They therefore revert to the defaults of `parameters.py` (146 000; 0.24; 26.7), which are the nivolumab values of P1.

**Consequence for P2.** Eq. (6) is evaluated as

$$
g^{\text{script,H01}}_{f,\alpha}=\frac{\bar Q(f;\alpha(1+h),\beta_{\text{def}})-\bar Q(f;\alpha(1-h),\beta_{\text{def}})}{2h\,\alpha\,\bar Q(f;\alpha,\beta_{\text{P2}})},
\tag{8}
$$

where $\beta$ denotes the PK triplet: the numerator differentiates around a different drug exposure from the one that normalises it.

**P1 is unaffected,** because its defaults coincide with its own PK values.

---

## 3. Computational Implementation and Reproducibility Audit

### 3.1 Containerised execution environment

**Image.**
- dolfin 2019.1.0 has no Windows build, and the official FEniCS image uses a manifest format no longer supported by Docker 29.
- We therefore built the Docker [Merkel 2014] image `papercancer/t01-fenics2019:1` from conda-forge [conda-forge community 2015] (miniforge3; Python 3.10.22; fenics-dolfin 2019.1.0 [Logg & Wells 2010; Alnæs et al. 2015]; numpy 1.26.4 [Harris et al. 2020]; scipy 1.15.2 [Virtanen et al. 2020]; petsc 3.25.6 [Balay et al., PETSc manual]; joblib 1.6.0 [Joblib developers]).
- The exact package set is frozen in an explicit conda lock file.

**Code and data handling.**
- The authors' repository (commit `fa8e6229`, no licence) is mounted read-only and executed unmodified.
- Our wrappers reference it by commit and path, and it is neither copied nor redistributed.

**Hardware and resources.**
- The host had 14 cores, of which the container was allotted 8 CPUs (`--cpus 8`), and the Docker virtual machine had 7.5 GiB of RAM.
- The script spawns `cpu_count()` joblib workers (14 inside the container, as recorded in the T01 report; the value is not printed in the logs), so its 11 parallel tasks per patient share the 8-CPU quota.
- Memory was not a limiting factor:
  - the full Table 2 run ended without out-of-memory termination;
  - in the P2 correction run (23 simulations, 11 parallel workers; 177 samples, one every 60 s), container memory peaked at 1.36 GiB (18 % of 7.48 GiB; median 1.31 GiB), with a mean CPU use of 7.2 cores.

**Stability incidents** (documented; none changed any computation):
- A first full run (11 Oct 2026) was interrupted, probably because the host entered modern standby (Windows event log; not demonstrated). It was relaunched with an operating-system wake request and without auto-removal of the container.
- In the H01 correction run, loky workers intermittently died (SIGSEGV/SIGBUS) inside `MPI.init()`, which dolfin calls on import (MPICH 5.0.1 [MPICH]), when many workers started at once:
  - the first full attempt failed after its reference simulation, with no out-of-memory event;
  - the leading hypothesis is a contention for shared memory (`/dev/shm`, 64 MB by default in Docker), which is plausible but not demonstrated;
  - the second attempt enlarged `/dev/shm` to 1 GiB, removed concurrent processes and added an automatic retry, and it completed without needing a retry (exit code 0; 183.6 min).

  All attempts are archived with their logs.
- **Cost:** the full Table 2 computation (2 patients × 23 simulations) took 309 min of wall time; the P2-only correction run took 184 min.

### 3.2 Pre-specified reproduction criteria

Criteria were fixed in a task contract **before** execution.

| Target | Metric | Reproduced | Partially | Discrepancy |
|---|---|---|---|---|
| PK (Eq. 4) | last periodic peak and trough vs closed form | ≤ 0.1 % | — | > 0.1 % |
| Table 2 (88 indices) | relative error and sign | ≤ 10 %, same sign | 10–50 %, same sign (or within tolerance but rank differs) | > 50 % or sign change |
| Global hypothesis H1 | — | ≥ 80 % of the 88 indices "reproduced" | | |

The 10 % tolerance allows for:
- three-significant-figure rounding (≤ 0.5 %);
- cancellation in central differences with $h=10^{-3}$;
- solver and library version differences.

The authors did not state their versions.

### 3.3 Verification protocol

**Independent verification.** T-numbers refer to the project's task log. T01 results were independently verified before integration. The T06 results (§4.3) rest on a pre-specified analysis and a bit-exact determinism control, but **have not yet been independently reviewed**.
- **T01, execution.** Unmodified execution, PK verification, Table 2 and the article–code correspondence (35 items).
- **T03, independent critical review.** It was carried out by a second agent with its own code, reading the authors' scripts by static analysis without importing them. It covered:
  - recomputation of all comparisons;
  - seven alternative scale transformations;
  - a full re-transcription of the 88 published values and ranks against the article text;
  - verification of the 22 parameter vectors.

  The review raised two major objections:
  - H01, the configuration defect;
  - H02, over-reaching interpretation in our first draft.

  Both were accepted. The wording in this manuscript follows the reviewer's recommendations.
- **T06, declared correction variant.** P2 was re-simulated with the authors' unmodified sensitivity routine. The only change was the simulation callback, which restores the P2 PK triplet before every perturbed run and logs the integrals $\bar Q$. The analysis plan and the effect classes were pre-specified before launch. A determinism control recomputed one component of P2 with the original defect.

**Cross-check on an unrelated reconstruction task (T02, T04, T05).** The same execute–audit–correct protocol was applied to a different problem: reconstructing individual patient data from the vector Kaplan–Meier curves of the ADRIATIC trial (limited-stage small-cell lung cancer) [Cheng et al. 2024; Guyot et al. 2012]. It ran in three steps:
- an agent executed the reconstruction;
- an independent audit re-ran it byte-for-byte, re-extracted the curves by rasterisation and refitted Kaplan–Meier [Kaplan & Meier 1958] and Cox [Cox 1972] models with independent code;
- all 18 pre-specified quantities were already reproduced in the original delivery;
- a correction round fixed two defects, in the curve extraction (merged steps) and in the design of the known-truth validation, and the 18 quantities remained within tolerance.

One residual unit-test failure was kept and declared rather than edited post hoc: 7 of 400 synthetic curves lose a step narrower than PDF coordinate precision.

This task concerns a different disease. It is reported only as evidence of how the audit protocol behaves (Supplementary S2) and is **not** combined with the NSCLC model.

### 3.4 Article–code correspondence

Of the 35 items checked:
- 21 match (3 within rounding and 1 after unit conversion);
- the code resolves 5 items left unspecified in the article;
- 9 are discrepancies, retained as uncertainty and not "corrected" (Table 2).

H01 (§2.4) is an additional defect of the sensitivity script.

**Table 2. Discrepancies between the published article and the released code.**

| # | Item | Article | Code |
|---|---|---|---|
| 1 | Sensitivity index | Eq. (5), with α/100 | Eq. (6), without α/100 |
| 2 | Drug-kill term | $\lambda_\tau^{eff}/\omega$, $\omega=80$ | additional factor 0.7 (effective $\omega\approx114.3$) |
| 3 | P1 therapy start | day 296 | day 322 of the data timeline (26 d later) |
| 4 | P2 Q6W start / therapy end | days 514 / 1063 | days 671 / 1218 (157 / 155 d later) |
| 5 | P2 mesh | 500 elements | 1000 elements |
| 6 | Heaviside $H$ | step function | smooth sigmoid (slope 30) |
| 7 | Nutrient consumption | proliferative and necrotic cells | necrotic cells do not consume |
| 8 | P2 $\lambda_\tau^{eff}$ | 0.54 | 0.5489 (rounds to 0.55) |
| 9 | Horizon $T$ for Table 2 | "end of therapy" | 9 d (P1) and 2 d (P2) before the end |

The code's schedules match the figures of the authors' preprint [Wagner 2023, preprint].

---

## 4. Results and Comparative Discussion

### 4.1 Pharmacokinetics

**Exactly reproduced.**
- The original `MedicineSolver` reproduces the ODE (4).
- Across 136 administrations (96 for P1 and 40 for P2), the delivered dose equals the nominal dose.
- Over the full trajectory, the 99th percentile of the pointwise relative error is 1.7 × 10⁻⁵ (P1) and 2.1 × 10⁻⁵ (P2).

**Pre-specified criterion not met.** The peak/trough criterion is met in **3 of 6** extrema:

| Schedule | Peak error | Trough error |
|---|---|---|
| P1, Q2W | 0.0017 % | 0.107 % |
| P2, Q3W | 0.0020 % | 0.129 % |
| P2, Q6W | 0.129 % | 0.0021 % |

**Cause.** All exceedances come from one sample per dose, at the start or end of the infusion. The effective infusion window is shifted by ±0.5 of a PK substep (≈ 56 s), a discretisation detail of the solver.

**Classification: partially reproduced.** Its effect on tumour dynamics was not quantified separately. The Table 2 agreement in §4.2 indicates that it does not alter the sensitivity indices at the published precision.

### 4.2 Table 2: published, raw and rescaled indices

**Raw script output (pre-specified criterion).** The released script was executed unmodified on both patients (exit code 0; 309 min). Its output matches **none** of the 88 published indices:
- relative error: median 228, 90th percentile 2.0 × 10⁵, maximum 1.0 × 10⁷ (as fractions);
- sign agreement: 88/88;
- rank agreement: 8/88.

The reproduction hypothesis H1 is therefore **rejected**, and this classification is retained.

**Rescaled output (diagnostic).** Applying Eq. (7) recovers every printed value:

**Table 3. Agreement of transformed script output with the published Table 2** (88 indices; independent recomputation, T03).

| Transformation of $g^{\text{script}}$ | Max. relative error | Within 10 %, same sign | Ranks equal | Equal after rounding to 3 s.f. |
|---|---|---|---|---|
| none (raw) | 1.0 × 10⁹ % | 0 | 8 | 0 |
| **× α / 100** | **0.449 %** | **88** | **88** | **88** |
| × α (elasticity) | 9 931 % | 0 | 88 | 0 |
| / 100 | 1.0 × 10⁷ % | 12 | 8 | 12 |
| × α of the other patient / 100 | 19 939 % | 56 | 25 | 56 |
| × α rounded as in Table 1 / 100 | 1.81 % | 88 | 88 | 74 |
| × α / 101 (negative control) | 1.44 % | 88 | 88 | 0 |

Other figures for the × α / 100 rescaling:
- median relative error 0.068 %, 90th percentile 0.22 %;
- largest residual: P1, $\lambda_P^{pro}$, $\bar Q(\phi_T)$, with 0.01095 against a published 0.0110.

**What Table 3 shows.**
- The 10 % tolerance alone cannot identify the transformation: the control divisor 101 also passes it.
- Exact agreement after rounding singles out $\alpha/100$.
- This **supports, but does not prove,** that the published table was obtained by applying Eq. (5) to the script output. The repository does not document that step.

The rescaling removes the scale discrepancy; it does not by itself validate the procedure, as §4.3 shows.

Table 4 lists all 88 values (Figure 1: `figuras/fig_tabla2.png`).

<!-- TABLA_88_INICIO -->
**Table 4. Local sensitivity indices: published values vs released-script output (raw), rescaled ×α/100, and (P2) rescaled after correcting H01.** Published values are those of Table 2 of Wagner et al. [2023] (CC BY 4.0), with ranks in parentheses. Rel. err. = |g − g_pub|/|g_pub|. Δ_H01 = (g_corr − g_orig)/|g_orig|. Source: `tabla2_comparacion.csv` and `t06_88_corregido.csv`.

| Pt | Parameter | QoI | Published (rank) | Raw script | ×α/100 | Rel. err. | P2 corrected ×α/100 (rank) | Rel. err. | Δ_H01 |
|---|---|---|---|---|---|---|---|---|---|
| P1 | λ_P^pro | φ_T | 1.10e-2 (3) | 3.036e+0 | 1.095e-2 | 0.449 % | — (not affected) | |  |
| P1 | λ_P^pro | φ_P | 9.02e-3 (2) | 2.502e+0 | 9.023e-3 | 0.030 % | — (not affected) | |  |
| P1 | λ_P^pro | φ_N | 1.42e-2 (4) | 3.941e+0 | 1.421e-2 | 0.093 % | — (not affected) | |  |
| P1 | λ_P^pro | V_vis | 1.02e-2 (5) | 2.825e+0 | 1.019e-2 | 0.117 % | — (not affected) | |  |
| P1 | λ_τ^eff | φ_T | -3.55e-3 (7) | -6.776e-2 | -3.550e-3 | 0.004 % | — (not affected) | |  |
| P1 | λ_τ^eff | φ_P | -5.08e-3 (6) | -9.701e-2 | -5.083e-3 | 0.052 % | — (not affected) | |  |
| P1 | λ_τ^eff | φ_N | -9.57e-4 (10) | -1.826e-2 | -9.565e-4 | 0.049 % | — (not affected) | |  |
| P1 | λ_τ^eff | V_vis | -5.16e-3 (7) | -9.845e-2 | -5.158e-3 | 0.034 % | — (not affected) | |  |
| P1 | λ | φ_T | -1.64e-2 (1) | -8.196e-1 | -1.639e-2 | 0.044 % | — (not affected) | |  |
| P1 | λ | φ_P | -1.37e-2 (1) | -6.827e-1 | -1.365e-2 | 0.335 % | — (not affected) | |  |
| P1 | λ | φ_N | -2.10e-2 (3) | -1.051e+0 | -2.103e-2 | 0.132 % | — (not affected) | |  |
| P1 | λ | V_vis | -1.50e-2 (4) | -7.514e-1 | -1.503e-2 | 0.187 % | — (not affected) | |  |
| P1 | λ_PN | φ_T | 1.77e-3 (10) | 1.767e+0 | 1.767e-3 | 0.163 % | — (not affected) | |  |
| P1 | λ_PN | φ_P | -2.20e-4 (10) | -2.197e-1 | -2.197e-4 | 0.127 % | — (not affected) | |  |
| P1 | λ_PN | φ_N | 5.13e-3 (8) | 5.130e+0 | 5.130e-3 | 0.007 % | — (not affected) | |  |
| P1 | λ_PN | V_vis | 2.32e-3 (10) | 2.324e+0 | 2.324e-3 | 0.193 % | — (not affected) | |  |
| P1 | σ_PN | φ_T | 1.05e-2 (4) | 5.227e+0 | 1.045e-2 | 0.435 % | — (not affected) | |  |
| P1 | σ_PN | φ_P | -1.30e-3 (9) | -6.491e-1 | -1.298e-3 | 0.145 % | — (not affected) | |  |
| P1 | σ_PN | φ_N | 3.03e-2 (2) | 1.517e+1 | 3.034e-2 | 0.145 % | — (not affected) | |  |
| P1 | σ_PN | V_vis | 3.01e-2 (2) | 1.503e+1 | 3.006e-2 | 0.128 % | — (not affected) | |  |
| P1 | c_m | φ_T | -2.10e-4 (11) | -4.203e+1 | -2.101e-4 | 0.067 % | — (not affected) | |  |
| P1 | c_m | φ_P | -2.08e-4 (11) | -4.154e+1 | -2.077e-4 | 0.156 % | — (not affected) | |  |
| P1 | c_m | φ_N | -2.14e-4 (11) | -4.286e+1 | -2.143e-4 | 0.146 % | — (not affected) | |  |
| P1 | c_m | V_vis | -3.41e-4 (11) | -6.817e+1 | -3.408e-4 | 0.049 % | — (not affected) | |  |
| P1 | ε_P | φ_T | 8.81e-3 (5) | 1.762e+3 | 8.810e-3 | 0.003 % | — (not affected) | |  |
| P1 | ε_P | φ_P | 6.78e-3 (3) | 1.357e+3 | 6.784e-3 | 0.064 % | — (not affected) | |  |
| P1 | ε_P | φ_N | 1.22e-2 (5) | 2.447e+3 | 1.224e-2 | 0.307 % | — (not affected) | |  |
| P1 | ε_P | V_vis | 7.66e-3 (6) | 1.532e+3 | 7.661e-3 | 0.012 % | — (not affected) | |  |
| P1 | c_Ψ | φ_T | -4.62e-3 (6) | -2.308e-1 | -4.615e-3 | 0.108 % | — (not affected) | |  |
| P1 | c_Ψ | φ_P | -3.60e-3 (7) | -1.800e-1 | -3.600e-3 | 0.004 % | — (not affected) | |  |
| P1 | c_Ψ | φ_N | -6.33e-3 (7) | -3.167e-1 | -6.333e-3 | 0.048 % | — (not affected) | |  |
| P1 | c_Ψ | V_vis | -4.25e-3 (9) | -2.126e-1 | -4.252e-3 | 0.058 % | — (not affected) | |  |
| P1 | κ_i | φ_T | -2.87e-3 (8) | -2.871e+4 | -2.871e-3 | 0.036 % | — (not affected) | |  |
| P1 | κ_i | φ_P | 1.52e-3 (8) | 1.520e+4 | 1.520e-3 | 0.008 % | — (not affected) | |  |
| P1 | κ_i | φ_N | -1.03e-2 (6) | -1.030e+5 | -1.030e-2 | 0.022 % | — (not affected) | |  |
| P1 | κ_i | V_vis | -2.15e-2 (3) | -2.155e+5 | -2.155e-2 | 0.218 % | — (not affected) | |  |
| P1 | α_H | φ_T | -2.51e-3 (9) | -2.508e-1 | -2.508e-3 | 0.081 % | — (not affected) | |  |
| P1 | α_H | φ_P | -6.53e-3 (4) | -6.525e-1 | -6.525e-3 | 0.070 % | — (not affected) | |  |
| P1 | α_H | φ_N | 4.29e-3 (9) | 4.291e-1 | 4.291e-3 | 0.028 % | — (not affected) | |  |
| P1 | α_H | V_vis | -4.37e-3 (8) | -4.373e-1 | -4.373e-3 | 0.076 % | — (not affected) | |  |
| P1 | α_P | φ_T | 1.28e-2 (2) | 3.195e-1 | 1.278e-2 | 0.152 % | — (not affected) | |  |
| P1 | α_P | φ_P | -6.25e-3 (5) | -1.562e-1 | -6.246e-3 | 0.059 % | — (not affected) | |  |
| P1 | α_P | φ_N | 4.50e-2 (1) | 1.125e+0 | 4.498e-2 | 0.041 % | — (not affected) | |  |
| P1 | α_P | V_vis | 3.09e-2 (1) | 7.725e-1 | 3.090e-2 | 0.005 % | — (not affected) | |  |
| P2 | λ_P^pro | φ_T | 4.13e-2 (2) | 1.093e+3 | 4.129e-2 | 0.024 % | 4.714e-2 (2) | 14.151 % | +14.178 % |
| P2 | λ_P^pro | φ_P | 4.17e-2 (2) | 1.103e+3 | 4.167e-2 | 0.077 % | 4.758e-2 (2) | 14.091 % | +14.179 % |
| P2 | λ_P^pro | φ_N | 6.19e-4 (11) | 1.638e+1 | 6.189e-4 | 0.012 % | 6.581e-4 (11) | 6.314 % | +6.326 % |
| P2 | λ_P^pro | V_vis | 1.75e-3 (11) | 4.621e+1 | 1.746e-3 | 0.233 % | 1.711e-3 (10) | 2.242 % | -2.013 % |
| P2 | λ_τ^eff | φ_T | -2.08e-2 (4) | -3.782e+0 | -2.076e-2 | 0.194 % | -2.217e-2 (4) | 6.564 % | -6.771 % |
| P2 | λ_τ^eff | φ_P | -2.09e-2 (4) | -3.811e+0 | -2.092e-2 | 0.099 % | -2.234e-2 (4) | 6.884 % | -6.778 % |
| P2 | λ_τ^eff | φ_N | -3.41e-3 (7) | -6.210e-1 | -3.408e-3 | 0.044 % | -3.461e-3 (7) | 1.509 % | -1.554 % |
| P2 | λ_τ^eff | V_vis | -6.74e-3 (6) | -1.227e+0 | -6.736e-3 | 0.064 % | -6.105e-3 (5) | 9.417 % | +9.359 % |
| P2 | λ | φ_T | -1.82e-1 (1) | -1.822e+1 | -1.822e-1 | 0.132 % | -2.052e-1 (1) | 12.750 % | -12.602 % |
| P2 | λ | φ_P | -1.84e-1 (1) | -1.839e+1 | -1.839e-1 | 0.046 % | -2.071e-1 (1) | 12.551 % | -12.603 % |
| P2 | λ | φ_N | -1.71e-3 (8) | -1.714e-1 | -1.714e-3 | 0.258 % | -1.846e-3 (8) | 7.927 % | -7.649 % |
| P2 | λ | V_vis | -5.02e-3 (7) | -5.023e-1 | -5.023e-3 | 0.055 % | -5.093e-3 (7) | 1.451 % | -1.395 % |
| P2 | λ_PN | φ_T | 3.61e-4 (11) | 1.804e-3 | 3.608e-4 | 0.045 % | 4.470e-4 (11) | 23.812 % | +23.867 % |
| P2 | λ_PN | φ_P | 3.28e-4 (11) | 1.638e-3 | 3.276e-4 | 0.119 % | 4.144e-4 (11) | 26.336 % | +26.487 % |
| P2 | λ_PN | φ_N | 3.94e-3 (5) | 1.970e-2 | 3.940e-3 | 0.006 % | 3.956e-3 (5) | 0.411 % | +0.404 % |
| P2 | λ_PN | V_vis | 2.17e-3 (10) | 1.085e-2 | 2.169e-3 | 0.029 % | 1.234e-3 (11) | 43.152 % | -43.135 % |
| P2 | σ_PN | φ_T | 2.17e-3 (8) | 1.083e+0 | 2.165e-3 | 0.226 % | 2.682e-3 (8) | 23.589 % | +23.869 % |
| P2 | σ_PN | φ_P | 1.97e-3 (8) | 9.829e-1 | 1.966e-3 | 0.216 % | 2.486e-3 (8) | 26.215 % | +26.488 % |
| P2 | σ_PN | φ_N | 2.36e-2 (3) | 1.182e+1 | 2.364e-2 | 0.160 % | 2.373e-2 (3) | 0.566 % | +0.405 % |
| P2 | σ_PN | V_vis | 1.33e-2 (3) | 6.659e+0 | 1.332e-2 | 0.130 % | 7.996e-3 (4) | 39.880 % | -39.958 % |
| P2 | c_m | φ_T | 4.45e-3 (6) | 8.903e+2 | 4.452e-3 | 0.035 % | 5.164e-3 (6) | 16.051 % | +16.011 % |
| P2 | c_m | φ_P | 4.50e-3 (6) | 9.001e+2 | 4.501e-3 | 0.016 % | 5.220e-3 (6) | 16.010 % | +15.990 % |
| P2 | c_m | φ_N | -8.46e-4 (10) | -1.692e+2 | -8.462e-4 | 0.022 % | -8.828e-4 (10) | 4.355 % | -4.332 % |
| P2 | c_m | V_vis | -2.79e-3 (8) | -5.582e+2 | -2.791e-3 | 0.032 % | -2.817e-3 (8) | 0.974 % | -0.941 % |
| P2 | ε_P | φ_T | 1.52e-2 (5) | 3.039e+3 | 1.519e-2 | 0.036 % | 1.759e-2 (5) | 15.720 % | +15.761 % |
| P2 | ε_P | φ_P | 1.54e-2 (5) | 3.074e+3 | 1.537e-2 | 0.206 % | 1.779e-2 (5) | 15.498 % | +15.736 % |
| P2 | ε_P | φ_N | -3.52e-3 (6) | -7.042e+2 | -3.521e-3 | 0.029 % | -3.657e-3 (6) | 3.898 % | -3.868 % |
| P2 | ε_P | V_vis | -1.09e-2 (4) | -2.174e+3 | -1.087e-2 | 0.280 % | -1.115e-2 (2) | 2.279 % | -2.567 % |
| P2 | c_Ψ | φ_T | -3.15e-3 (7) | -1.573e-1 | -3.146e-3 | 0.135 % | -3.630e-3 (7) | 15.252 % | -15.407 % |
| P2 | c_Ψ | φ_P | -3.18e-3 (7) | -1.592e-1 | -3.183e-3 | 0.109 % | -3.673e-3 (7) | 15.500 % | -15.375 % |
| P2 | c_Ψ | φ_N | 9.14e-4 (9) | 4.572e-2 | 9.143e-4 | 0.036 % | 9.458e-4 (9) | 3.476 % | +3.439 % |
| P2 | c_Ψ | V_vis | 2.54e-3 (9) | 1.272e-1 | 2.545e-3 | 0.195 % | 2.792e-3 (9) | 9.935 % | +9.720 % |
| P2 | κ_i | φ_T | -1.66e-3 (10) | -1.663e+4 | -1.663e-3 | 0.183 % | -2.064e-3 (10) | 24.326 % | -24.098 % |
| P2 | κ_i | φ_P | -1.52e-3 (10) | -1.515e+4 | -1.515e-3 | 0.309 % | -1.919e-3 (10) | 26.268 % | -26.659 % |
| P2 | κ_i | φ_N | -1.76e-2 (4) | -1.758e+5 | -1.758e-2 | 0.130 % | -1.763e-2 (4) | 0.187 % | -0.317 % |
| P2 | κ_i | V_vis | -9.74e-3 (5) | -9.742e+4 | -9.742e-3 | 0.025 % | -5.956e-3 (6) | 38.849 % | +38.864 % |
| P2 | α_H | φ_T | -3.64e-2 (3) | -3.640e+0 | -3.640e-2 | 0.009 % | -4.097e-2 (3) | 12.545 % | -12.535 % |
| P2 | α_H | φ_P | -3.71e-2 (3) | -3.706e+0 | -3.706e-2 | 0.105 % | -4.167e-2 (3) | 12.313 % | -12.431 % |
| P2 | α_H | φ_N | 3.44e-2 (2) | 3.445e+0 | 3.445e-2 | 0.143 % | 3.462e-2 (2) | 0.645 % | +0.501 % |
| P2 | α_H | V_vis | 1.71e-2 (2) | 1.710e+0 | 1.710e-2 | 0.025 % | 9.372e-3 (3) | 45.192 % | -45.178 % |
| P2 | α_P | φ_T | 2.14e-3 (9) | 5.361e-2 | 2.144e-3 | 0.202 % | 2.618e-3 (9) | 22.328 % | +22.082 % |
| P2 | α_P | φ_P | 1.76e-3 (9) | 4.400e-2 | 1.760e-3 | 0.008 % | 2.236e-3 (9) | 27.072 % | +27.062 % |
| P2 | α_P | φ_N | 4.35e-2 (1) | 1.088e+0 | 4.353e-2 | 0.059 % | 4.370e-2 (1) | 0.451 % | +0.391 % |
| P2 | α_P | V_vis | 2.48e-2 (1) | 6.199e-1 | 2.480e-2 | 0.012 % | 1.512e-2 (1) | 39.018 % | -39.011 % |
<!-- TABLA_88_FIN -->

### 4.3 Impact of correcting H01 on the sensitivity of patient 2

<!-- H01_RESULTADOS_INICIO -->
**Design (pre-specified before launch).**
- The authors' sensitivity routine was called unmodified for P2 (dt = 1/24 d, T = 1102 d, h = 10⁻³).
- The only change was the simulation callback: before each of the 23 simulations, it restores the P2 triplet $(M_\tau,d_\tau,t_{1/2})=(143\,600,\;0.20,\;22)$ and logs the integrals $\bar Q$.
- The logs confirm the defect and its correction:
  - all 22 perturbed simulations arrived with the default triplet (146 000; 0.24; 26.7) and were corrected;
  - the reference simulation already carried the P2 values.
- **Effect classes**, defined beforehand on $\Delta_{H01}=(g_{corr}-g_{orig})/|g_{orig}|$:
  - *negligible*: max $|\Delta|\le0.5$ %, no sign or rank change;
  - *minor*: ≤ 10 %;
  - *relevant*: > 10 %, or any sign or rank change.

**Determinism control.** Component 1 of P2 ($\lambda_\tau^{eff}$) was recomputed **with** the original defect. All four indices were identical to the original run to every printed digit (relative difference 0.0). The simulations are therefore deterministic, and every change below is due to the correction.

**Size of the defect.** In that control, the perturbed simulations (with the P1 drug parameters: higher dose, longer half-life) gave a time-averaged total tumour mass about 15 % lower than the reference ($\bar Q(\phi_T)$ = 3.14 × 10⁻³ vs 3.71 × 10⁻³). The original P2 indices thus divide a derivative taken at one drug exposure by a mass taken at another.

**Effect on the 44 P2 indices: relevant** (Table 5; Figure 3: `figuras/fig_h01.png`).

| QoI | Median \|Δ_H01\| | Max \|Δ_H01\| | Rank changes (of 11) |
|---|---|---|---|
| $\bar Q(\phi_T)$ | 16.0 % | 24.1 % | 0 |
| $\bar Q(\phi_P)$ | 16.0 % | 27.1 % | 0 |
| $\bar Q(\phi_N)$ | 3.4 % | 7.6 % | 0 |
| $\bar Q(V_{vis})$ | 38.9 % | 45.2 % | 7 |
| **All 44** | **12.6 %** | **45.2 %** | **7** |

- **Signs:** no index changes sign.
- **Largest changes:** all in the visible volume. $\alpha_H$ (−45.2 %), $\lambda_{PN}$ (−43.1 %), $\sigma_{PN}$ (−40.0 %), $\alpha_P$ (−39.0 %) and $\kappa_i$ (+38.9 %).
- **Visible-volume ranking:** the top parameter ($\alpha_P$) is unchanged, but positions 2–6 and 10–11 are reordered. In particular, $\varepsilon_P$ rises from rank 4 to rank 2, and $\alpha_H$ falls from 2 to 3.
- **Calibrated parameters:**
  - for $\lambda_P^{pro}$ and $\lambda$, the total-mass indices change by +14.2 % and −12.6 %;
  - for the drug-effect parameter $\lambda_\tau^{eff}$, the total-mass index changes by −6.8 % and the visible-volume index by +9.4 %.

**Agreement of the corrected P2 values with the published table.**
- The original-configuration P2 values agree 44/44 at three significant figures (§4.2).
- The corrected values agree in only 1/44 (19/44 within 10 %; median error 12.7 %).
- Across all 88 indices (P1 unchanged, P2 corrected), 45/88 agree at three significant figures and 81/88 ranks coincide.
- This contrast is further evidence that the published P2 column was produced with the defective configuration.

<!-- TABLA_H01_INICIO -->
**Table 5. Patient 2: sensitivity indices (×α/100) with the original configuration (H01) and after correction.** Ranks by |g| within each QoI. Published values: Wagner et al. [2023], Table 2 (CC BY 4.0). Source: `t06_p2_indices.csv`.

| Parameter | QoI | Original (rank) | Corrected (rank) | Δ_H01 | Published (rank) |
|---|---|---|---|---|---|
| λ_P^pro | φ_T | 4.129e-2 (2) | 4.714e-2 (2) | +14.178 % | 4.13e-2 (2) |
| λ_P^pro | φ_P | 4.167e-2 (2) | 4.758e-2 (2) | +14.179 % | 4.17e-2 (2) |
| λ_P^pro | φ_N | 6.189e-4 (11) | 6.581e-4 (11) | +6.326 % | 6.19e-4 (11) |
| λ_P^pro | V_vis | 1.746e-3 (11) | 1.711e-3 (10) | -2.013 % | 1.75e-3 (11) |
| λ_τ^eff | φ_T | -2.076e-2 (4) | -2.217e-2 (4) | -6.771 % | -2.08e-2 (4) |
| λ_τ^eff | φ_P | -2.092e-2 (4) | -2.234e-2 (4) | -6.778 % | -2.09e-2 (4) |
| λ_τ^eff | φ_N | -3.408e-3 (7) | -3.461e-3 (7) | -1.554 % | -3.41e-3 (7) |
| λ_τ^eff | V_vis | -6.736e-3 (6) | -6.105e-3 (5) | +9.359 % | -6.74e-3 (6) |
| λ | φ_T | -1.822e-1 (1) | -2.052e-1 (1) | -12.602 % | -1.82e-1 (1) |
| λ | φ_P | -1.839e-1 (1) | -2.071e-1 (1) | -12.603 % | -1.84e-1 (1) |
| λ | φ_N | -1.714e-3 (8) | -1.846e-3 (8) | -7.649 % | -1.71e-3 (8) |
| λ | V_vis | -5.023e-3 (7) | -5.093e-3 (7) | -1.395 % | -5.02e-3 (7) |
| λ_PN | φ_T | 3.608e-4 (11) | 4.470e-4 (11) | +23.867 % | 3.61e-4 (11) |
| λ_PN | φ_P | 3.276e-4 (11) | 4.144e-4 (11) | +26.487 % | 3.28e-4 (11) |
| λ_PN | φ_N | 3.940e-3 (5) | 3.956e-3 (5) | +0.404 % | 3.94e-3 (5) |
| λ_PN | V_vis | 2.169e-3 (10) | 1.234e-3 (11) | -43.135 % | 2.17e-3 (10) |
| σ_PN | φ_T | 2.165e-3 (8) | 2.682e-3 (8) | +23.869 % | 2.17e-3 (8) |
| σ_PN | φ_P | 1.966e-3 (8) | 2.486e-3 (8) | +26.488 % | 1.97e-3 (8) |
| σ_PN | φ_N | 2.364e-2 (3) | 2.373e-2 (3) | +0.405 % | 2.36e-2 (3) |
| σ_PN | V_vis | 1.332e-2 (3) | 7.996e-3 (4) | -39.958 % | 1.33e-2 (3) |
| c_m | φ_T | 4.452e-3 (6) | 5.164e-3 (6) | +16.011 % | 4.45e-3 (6) |
| c_m | φ_P | 4.501e-3 (6) | 5.220e-3 (6) | +15.990 % | 4.50e-3 (6) |
| c_m | φ_N | -8.462e-4 (10) | -8.828e-4 (10) | -4.332 % | -8.46e-4 (10) |
| c_m | V_vis | -2.791e-3 (8) | -2.817e-3 (8) | -0.941 % | -2.79e-3 (8) |
| ε_P | φ_T | 1.519e-2 (5) | 1.759e-2 (5) | +15.761 % | 1.52e-2 (5) |
| ε_P | φ_P | 1.537e-2 (5) | 1.779e-2 (5) | +15.736 % | 1.54e-2 (5) |
| ε_P | φ_N | -3.521e-3 (6) | -3.657e-3 (6) | -3.868 % | -3.52e-3 (6) |
| ε_P | V_vis | -1.087e-2 (4) | -1.115e-2 (2) | -2.567 % | -1.09e-2 (4) |
| c_Ψ | φ_T | -3.146e-3 (7) | -3.630e-3 (7) | -15.407 % | -3.15e-3 (7) |
| c_Ψ | φ_P | -3.183e-3 (7) | -3.673e-3 (7) | -15.375 % | -3.18e-3 (7) |
| c_Ψ | φ_N | 9.143e-4 (9) | 9.458e-4 (9) | +3.439 % | 9.14e-4 (9) |
| c_Ψ | V_vis | 2.545e-3 (9) | 2.792e-3 (9) | +9.720 % | 2.54e-3 (9) |
| κ_i | φ_T | -1.663e-3 (10) | -2.064e-3 (10) | -24.098 % | -1.66e-3 (10) |
| κ_i | φ_P | -1.515e-3 (10) | -1.919e-3 (10) | -26.659 % | -1.52e-3 (10) |
| κ_i | φ_N | -1.758e-2 (4) | -1.763e-2 (4) | -0.317 % | -1.76e-2 (4) |
| κ_i | V_vis | -9.742e-3 (5) | -5.956e-3 (6) | +38.864 % | -9.74e-3 (5) |
| α_H | φ_T | -3.640e-2 (3) | -4.097e-2 (3) | -12.535 % | -3.64e-2 (3) |
| α_H | φ_P | -3.706e-2 (3) | -4.167e-2 (3) | -12.431 % | -3.71e-2 (3) |
| α_H | φ_N | 3.445e-2 (2) | 3.462e-2 (2) | +0.501 % | 3.44e-2 (2) |
| α_H | V_vis | 1.710e-2 (2) | 9.372e-3 (3) | -45.178 % | 1.71e-2 (2) |
| α_P | φ_T | 2.144e-3 (9) | 2.618e-3 (9) | +22.082 % | 2.14e-3 (9) |
| α_P | φ_P | 1.760e-3 (9) | 2.236e-3 (9) | +27.062 % | 1.76e-3 (9) |
| α_P | φ_N | 4.353e-2 (1) | 4.370e-2 (1) | +0.391 % | 4.35e-2 (1) |
| α_P | V_vis | 2.480e-2 (1) | 1.512e-2 (1) | -39.011 % | 2.48e-2 (1) |
<!-- TABLA_H01_FIN -->
<!-- H01_RESULTADOS_FIN -->

### 4.4 Discussion

**What reproduces.**
- The simulation pipeline, numerical scheme and PK model can still be executed seven years after the FEniCS 2019.1 release and three years after publication, provided the environment is rebuilt and locked (§3.1).
- The executed code regenerates the published sensitivity values to three significant figures once Eq. (5) is applied.
- This is a stronger result than "qualitative agreement", and it localises the original discrepancy to a single, documented post-processing step.

**What does not.** A user of the released artefacts would not obtain the published Table 2. The discrepancy is several orders of magnitude, and its size varies by parameter, because $\alpha$ spans $10^{-5}$ to 20. Ranks are also scrambled, so the parameter ranking that motivates the article's discussion is not recoverable from the script output. Because the verbal and symbolic forms of Eq. (5) are themselves ambiguous ("100 %"), we recommend reporting the elasticity $(\partial_\alpha\bar Q/\bar Q)\,\alpha$ directly, with explicit units.

**Configuration integrity.** H01 shows that the reproduction of printed numbers does not guarantee methodological correctness. The published P2 indices reproduce precisely *because* the same defective configuration was executed.
- **Size of the effect.** Correcting it shifts the indices by a median of 12.6 % and up to 45 %. That is far larger than the 0.45 % rounding-level agreement that the reproduction achieves.
- **Where it matters.** The effect concentrates on the clinically observable quantity, the CT-visible volume, whose parameter ranking is reordered in 7 of 11 positions.
- **Why.** The plausible mechanism is the drug exposure. The P1 drug parameters (dose 0.24 g vs 0.20 g; half-life 26.7 d vs 22 d) raise the antibody exposure and lower the mean tumour mass by about 15 %, and the threshold-defined visible volume responds non-linearly to mass changes near the 0.3 visibility cut-off. This mechanism was not isolated experimentally.
- **No conclusion has to be reversed.** No index changes sign, and the leading parameter of each quantity is preserved.
- **Recommendations for the authors' own reading of the table.** Rankings of secondary parameters for P2, especially for $V_{vis}$, should not be relied upon. A corrected column should accompany any re-use of the table.

**Implications for calibration and optimisation.**
- Local, one-at-a-time indices at a single, manually chosen parameter point say nothing about practical identifiability.
- For P2 they were, in addition, computed around an inconsistent PK configuration.
- The sensitivity ranking therefore cannot be used to decide which parameters to calibrate or which can be fixed.
- A likelihood-based calibration with profile likelihoods (§5) must precede any therapeutic use.

**Limitations.**
- n = 2 patients, both manually calibrated by the original authors, so nothing here informs predictive validity or efficacy.
- Library versions of the original authors are unknown. The residuals (≤ 0.45 %) are compatible with rounding alone.
- The published table was checked against the extracted article text, not against a page image.
- Only the 1D radial model was audited.
- The second part of the pre-specified H1, verification against an independent re-implementation (L2 error ≤ 5 % in $V_{vis}$), has not yet been performed.
- AI agents performed the analyses under human supervision (§7.4).

---

## 5. Proposed Pipeline for Personalised Therapy

The audit defines what must be in place before the model can support **pharmacokinetic and tumour-parameter calibration** and, eventually, **therapeutic optimisation**.

The pipeline is a proposal: **no step of it has been executed**, and each requires authorisation, data-access agreements and pre-specified criteria.

**Figure 2 (schematic, to be drawn).** Imaging → volumetry with uncertainty → geometry and PK inputs → calibration and identifiability → model comparison → out-of-time validation → constrained dose exploration.

**Stage 0. Reproducible base.** Close the remaining reproduction gaps:
- an independent 1D re-implementation verified against the original (L2 ≤ 5 % in $V_{vis}$);
- mesh and time-step convergence (250/500/1000 elements; dt = 1/12, 1/24, 1/48 d);
- a corrected sensitivity routine that reports elasticities.

**Stage 1. Imaging and volumetry with measurement error.** Patient-specific calibration needs **longitudinal on-treatment CT with dosing records**, which no public dataset provides. Public collections serve auxiliary roles:
- **LIDC-IDRI** (thoracic CT with multi-reader nodule annotations [Armato et al. 2011]):
  - training and benchmarking of nodule segmentation;
  - above all, an empirical **inter-observer volumetric error model**, which supplies the measurement variance $\sigma^2$ of the likelihood (Stage 3). It is not a source of treatment dynamics.
- **TCGA-LUSC** (squamous-cell NSCLC with genomic profiling [TCGA 2012] and baseline imaging in TCIA [Clark et al. 2013]):
  - priors on tumour geometry and histology-specific heterogeneity;
  - genomic covariates for future hierarchical models.

  It does not provide on-treatment immunotherapy trajectories.
- **On-treatment cohorts** are required for calibration: the authors' data (with permission), trial data through controlled-access platforms (e.g. Vivli [Vivli], as used by Ghaffari Laleh et al. 2022), or institutional cohorts with ethics approval.

**Stage 2. Geometry and PK inputs.**
- 1D radial geometry first. Patient-specific 3D lung and vasculature meshes (3D Slicer [Fedorov et al. 2012] and vmtk [Antiga et al. 2008], as in the original work [Wagner 2023]) only once 1D results are validated.
- PK per drug from label or population PK values ($t_{1/2}$, $M_\tau$, dose and schedule), with the exact administration dates.

**Stage 3. Likelihood-based calibration and identifiability.**
- Log-normal measurement model, $\log V_{obs}=\log V_{vis}(\theta)+\varepsilon$, $\varepsilon\sim\mathcal N(0,\sigma^2)$, with $\sigma$ informed by Stage 1.
- Maximum-likelihood estimation of $(\lambda_P^{pro},\lambda_\tau^{eff},\lambda_{PN})$ with ≥ 20 multistarts, for each $\lambda\in\{1,2\}$.
- Profile likelihoods [Raue et al. 2009]: a parameter is practically identifiable if its profile crosses $\chi^2_1(0.95)/2=1.92$ on both sides within the search range. The authors' remark that $\lambda_P^{pro}$ and $\lambda_\tau^{eff}$ are hard to determine leads to the hypothesis that they are not jointly identifiable in P2.
- Global sensitivity (e.g. Sobol indices [Sobol 2001]) over the calibrated region, replacing single-point local indices.

**Stage 4. Model comparison.**
- Parsimonious ODE comparators driven by the same PK and Emax term: exponential, Gompertz [Gompertz 1825] and logistic [Verhulst 1838] growth with drug kill.
- Comparison by AICc [Hurvich & Tsai 1989] and BIC [Schwarz 1978], with $|\Delta\mathrm{AICc}|\le2$ treated as equivalence.

**Stage 5. Out-of-time validation.**
- Rolling-origin forecasts [Tashman 2000]: calibrate up to scan $k$, predict scans $k+1\ldots k+3$.
- Paired comparison of log-volume errors against the comparators.
- Parametric bootstrap bands [Efron & Tibshirani 1993] (≥ 200 replicates), declared as parameter uncertainty under the model and not as clinical confidence intervals.

**Stage 6. Constrained dose exploration.** Only if Stages 3–5 succeed:
- counterfactual schedules (dose, interval, treatment breaks) evaluated by the posterior predictive distribution of $V_{vis}$, within label-approved ranges;
- the outputs remain hypotheses for prospective testing, **not** treatment recommendations.

**Governance.**
- Pre-registration of criteria before each stage.
- Containerised, logged execution as in §3.
- Independent review of each stage.
- Clear licensing of code and data. The original repository currently has no licence (§7.3).

---

## 6. Conclusions and Future Work

1. **The model runs and its pharmacokinetics are correct.** The released NSCLC phase-field model executes in a locked container, and its PK component reproduces the closed-form solution and the total dose exactly. The pre-specified peak/trough tolerance is missed by a half-substep discretisation shift.
2. **Table 2 is not reproduced as released.** The published sensitivity table does not follow from the released script (0/88). It is recovered exactly (88/88 at three significant figures, maximum error 0.449 %) by the α/100 rescaling implied by the article's verbal definition, which the script omits.
3. **A configuration defect affects P2.** The published P2 sensitivity indices were computed with perturbed simulations that use the wrong drug's PK parameters (H01). Correcting it changes the 44 indices by a median of 12.6 % (up to 45.2 %) and reorders 7 of 11 visible-volume ranks, without sign changes. This is a relevant effect by pre-specified criteria, verified against a bit-exact determinism control.
4. **The evidence base is thin.** With two manually calibrated patients, nine article–code discrepancies and local indices at a single point, the model is not yet ready for pharmacokinetic calibration or therapeutic optimisation claims.

**Roadmap:**
- **(i)** Independent re-implementation and convergence study.
- **(ii)** Likelihood-based calibration with profile-likelihood identifiability.
- **(iii)** Comparison with parsimonious ODE models.
- **(iv)** Out-of-time validation.
- **(v)** Access to longitudinal on-treatment imaging cohorts.
- **(vi)** Only then, constrained dose exploration.

Before publication, the original authors should be consulted on code licensing, data re-use, the α/100 step and H01.

---

## 7. Declarations

### 7.1 Data and code availability

| Material | Location |
|---|---|
| Our wrappers, logs and derived data | `Resultados/Trabajo_Claude/T01_phasefield/` and `T06_P2_H01/` |
| Independent review | `Resultados/Trabajo_Cline/T03_revision_T01/` |
| Docker recipe and conda lock | `T01_phasefield/env/` |
| Original code | github.com/wagnandr/immunotherapy-lung-cancer, commit `fa8e6229` (not redistributed; no licence) |

### 7.2 Ethics

The patient data are anonymised volumetric measurements released by the original authors, with ethics approval BLAEK 19021 [Wagner 2023, p. 7]. This work used them only to reproduce published results.

### 7.3 Licensing and permissions (blocking for publication)

- The original repository has no licence. It was used privately, unmodified and without redistribution.
- Publishing derived analyses of the patient data, or redistributing modified code, requires permission from the authors.
- A consultation draft exists but **has not been sent**.

### 7.4 Use of AI tools

Generative AI tools were used as **assistance tools** under human supervision. They are not authors, and they are cited as software [Anthropic, Claude Code; Cline; OpenAI, gpt-6-astra; Microsoft, Visual Studio Code].
- **Claude Code** (Anthropic), run as an extension of the Visual Studio Code development environment. It coordinated the tasks, ran the T01 and T06 simulations, audited T02 (T04, T05) and drafted this manuscript and its companion documents from the logged analyses.
- **Cline** (command-line interface 3.0.70) with the OpenAI model gpt-6-astra (provider `openai-codex`). It carried out the ADRIATIC reconstruction (T02) and the independent review of T01 (T03).

**Who operated the tools.** The AI tools, the development environment (Visual Studio Code) and the computing environment (Docker) were operated by Wuilson Estacio.

**Verification.** All results were obtained from logged executions. Claude Code's T01 results were reviewed by Cline (T03), and Cline's T02 reconstruction was audited by Claude Code (T04, T05). The T06 results (§4.3) have not yet been independently reviewed, and no expert human review of any task has been carried out yet. The author is responsible for the content.

**Pending.** The policies of the target journal and of the doctoral programme on the use of AI have not yet been checked. This declaration must be adapted to their requirements before submission.

### 7.5 Author contributions and funding

[PENDING]

### 7.6 Companion documents and evidence map

The companion documents are in Spanish. Each is listed with the evidence it contributes. The two lines of work are kept apart: **E1** is the NSCLC phase-field model audited in this paper; **E2** (ADRIATIC, small-cell lung cancer) is a survival-curve reconstruction used only to show how the audit protocol behaves. **E2 does not validate, calibrate or otherwise support the E1 model.**

| Document | Evidence it provides | Supports |
|---|---|---|
| [METODOLOGIA_SIMULACIONES_Y_COLABORACION_IA.md](METODOLOGIA_SIMULACIONES_Y_COLABORACION_IA.md) | Which simulations were run, labelled as original (authors' code, unmodified), corrected variant (H01) or pending. Data, parameters, versions, Docker environment, commands, run times and outcomes. Which tasks the researcher, Claude Code and Cline performed, how tasks were delegated by written contract and how each delivery was checked. Failed runs and tests, corrections and limitations | §3.1, §3.3, §4.3, §7.4 |
| [INFORME_INTEGRADO_F0_F1.md](INFORME_INTEGRADO_F0_F1.md) | Verified results of T01 (Table 2, PK, article–code correspondence) and T02/T04/T05 (ADRIATIC), each with its pre-specified classification and independent verification. Discrepancies, limitations, licences and a claim → file → execution → verification table (§10), including T06 | §3.2–3.4, §4.1–4.3, §6, §7.3, S2, S4 |
| [Primera_entrega_contribuciones_y_plan.md](Primera_entrega_contribuciones_y_plan.md) | The plan of 10 October 2026, written before any simulation: hypotheses H1–H4, tolerances, continue/stop criteria per phase, and the clinical background figures (NLST, NELSON). Its section E records what was executed, what was not and which paper sections each part supports | §1.1, §1.3, §3.2, §5 |

Canonical copies of the two reports are kept in `Resultados/Integrado/` and `Resultados/04_plan/`. The copies linked here are identical.

**Mapping of tasks to sections** (T-numbers as in §3.3):

| Task | Line | What it contributes | Paper sections |
|---|---|---|---|
| T01 | E1, original code | PK check, Table 2 (46 FEM simulations, 309 min), article–code correspondence | §2.3, §3.1–3.4, §4.1–4.2; Tables 2–4; Fig. 1 |
| T03 | E1, review (no simulations) | Independent recomputation, scale alternatives, transcription check; findings H01 and H02 | §2.4, §3.3; Table 3 |
| T06 | E1, corrected variant | P2 re-simulation with H01 corrected (23 simulations, 184 min) plus a determinism control (3 simulations) | §2.4, §3.1, §4.3; Tables 4–5; Fig. 3 |
| T02, T04, T05 | E2 only | ADRIATIC reconstruction and its audits | §3.3 (protocol cross-check) and S2 only |

### 7.7 Reuse of third-party material and attribution

| Material | Owner and licence | How it is used here |
|---|---|---|
| Model equations (Eqs. 1–4), sensitivity definition (Eq. 5), parameter values (Table 1), published sensitivity values (Tables 4–5, "Published" columns), quoted definition in §2.3 | Wagner et al. [2023], *Math. Biosci. Eng.*; CC BY 4.0 | Reproduced with attribution at each use, for verification. No change to their meaning |
| Source code (commit `fa8e6229`) | Wagner et al. [2023, code repository]; **no licence** (all rights reserved by default) | Executed privately and unmodified. Not copied, not redistributed. Cited by file and line number only |
| Patient volumetric data | Released by Wagner et al. [2023] with ethics approval BLAEK 19021; no data licence | Used only to reproduce published results. Publication requires the authors' permission (§7.3) |
| ADRIATIC survival curves | Cheng et al. [2024], *N. Engl. J. Med.*; copyright of the publisher | Numerical data extracted for a secondary analysis (S2 only). No figure of the original article is reproduced |
| Software (FEniCS/DOLFIN, PETSc, NumPy, SciPy, joblib, MPICH, conda-forge, Docker) | Their respective developers and open-source licences | Used as published; cited in the references |

---

## References

References marked † were not checked against the source document in this project and must be verified before submission. The others were checked in the project's document base, in the reference list of Wagner et al. (2023) or, for bibliographic metadata, on the publisher's or archive's page (13 October 2026).

- Allen SM, Cahn JW (1979). A microscopic theory for antiphase boundary motion and its application to antiphase domain coarsening. *Acta Metall.* 27:1085–1095. †
- Alnæs MS, Blechta J, Hake J, Johansson A, Kehlet B, Logg A, Richardson C, Ring J, Rognes ME, Wells GN (2015). The FEniCS Project Version 1.5. *Arch. Numer. Softw.* 3(100):9–23. doi:10.11588/ans.2015.100.20553.
- Anthropic. Claude Code [software: AI coding agent], run as a Visual Studio Code extension. https://claude.com/claude-code (accessed October 2026).
- Antiga L, Piccinelli M, Botti L, Ene-Iordache B, Remuzzi A, Steinman DA (2008). An image-based modeling framework for patient-specific computational hemodynamics. *Med. Biol. Eng. Comput.* 46:1097–1112. †
- Armato SG III, et al. (2011). The Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI): a completed reference database of lung nodules on CT scans. *Med. Phys.* 38:915–931. †
- Balay S, et al. PETSc/TAO Users Manual. Argonne National Laboratory, ANL-21/39 (revision for the release in use; PETSc 3.25.6 used here). https://petsc.org †
- Bray F, Ferlay J, Soerjomataram I, Siegel RL, Torre LA, Jemal A (2018). Global cancer statistics 2018: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. *CA Cancer J. Clin.* 68:394–424. doi:10.3322/caac.21492.
- Cahn JW, Hilliard JE (1958). Free energy of a nonuniform system. I. Interfacial free energy. *J. Chem. Phys.* 28:258–267. †
- Cheng Y, et al. (2024). Durvalumab after chemoradiotherapy in limited-stage small-cell lung cancer. *N. Engl. J. Med.* 391:1313–1327. doi:10.1056/NEJMoa2404873.
- Clark K, et al. (2013). The Cancer Imaging Archive (TCIA): maintaining and operating a public information repository. *J. Digit. Imaging* 26:1045–1057. †
- Cline. Cline command-line interface, version 3.0.70 [software: AI coding agent]. https://cline.bot (accessed October 2026).
- conda-forge community (2015). The conda-forge Project: Community-based Software Distribution Built on the conda Package Format and Ecosystem. Zenodo. doi:10.5281/zenodo.4774216.
- Cox DR (1972). Regression models and life-tables. *J. R. Stat. Soc. B* 34:187–220. †
- Cristini V, Lowengrub J (2010). *Multiscale Modeling of Cancer.* Cambridge University Press. doi:10.1017/cbo9780511781452.
- de Koning HJ, et al. (2020). Reduced lung-cancer mortality with volume CT screening in a randomized trial. *N. Engl. J. Med.* 382:503–513. †
- Efron B, Tibshirani RJ (1993). *An Introduction to the Bootstrap.* Chapman & Hall, New York. †
- Eyre DJ (1998). Unconditionally gradient stable time marching the Cahn–Hilliard equation. *MRS Online Proc. Lib.* 529:39–46. doi:10.1557/proc-529-39.
- Fedorov A, et al. (2012). 3D Slicer as an image computing platform for the Quantitative Imaging Network. *Magn. Reson. Imaging* 30:1323–1341. †
- Frigeri S, Grasselli M, Rocca E (2015). On a diffuse interface model of tumour growth. *Eur. J. Appl. Math.* 26:215–243. doi:10.1017/s0956792514000436.
- Fritz M, Jha PK, Köppl T, Oden JT, Wohlmuth B (2021). Analysis of a new multispecies tumor growth model coupling 3D phase-fields with a 1D vascular network. *Nonlinear Anal. Real World Appl.* 61:103331. doi:10.1016/j.nonrwa.2021.103331.
- Garcke H, Lam KF, Sitka E, Styles V (2016). A Cahn–Hilliard–Darcy model for tumour growth with chemotaxis and active transport. *Math. Models Methods Appl. Sci.* 26:1095–1148. doi:10.1142/s0218202516500263.
- Ghaffari Laleh N, et al. (2022). Classical mathematical models for prediction of response to chemotherapy and immunotherapy. *PLoS Comput. Biol.* 18:e1009822. †
- Ginzburg VL, Landau LD (1950). On the theory of superconductivity. *Zh. Eksp. Teor. Fiz.* 20:1064–1082. †
- Gompertz B (1825). On the nature of the function expressive of the law of human mortality, and on a new mode of determining the value of life contingencies. *Phil. Trans. R. Soc. Lond.* 115:513–583. †
- Guyot P, Ades AE, Ouwens MJNM, Welton NJ (2012). Enhanced secondary analysis of survival data: reconstructing the data from published Kaplan–Meier survival curves. *BMC Med. Res. Methodol.* 12:9. doi:10.1186/1471-2288-12-9.
- Harris CR, et al. (2020). Array programming with NumPy. *Nature* 585:357–362. †
- Hill AV (1910). The possible effects of the aggregation of the molecules of haemoglobin on its dissociation curves. *J. Physiol.* 40(Suppl.):iv–vii. †
- Hurvich CM, Tsai CL (1989). Regression and time series model selection in small samples. *Biometrika* 76:297–307. †
- Joblib developers. joblib: running Python functions as pipeline jobs, version 1.6.0 [software]. https://joblib.readthedocs.io †
- Kaplan EL, Meier P (1958). Nonparametric estimation from incomplete observations. *J. Am. Stat. Assoc.* 53:457–481. †
- Lee HG, Kim Y, Kim J (2015). Mathematical model and its fast numerical method for the tumor growth. *Math. Biosci. Eng.* 12:1173–1187. doi:10.3934/mbe.2015.12.1173.
- Lima EABF, Oden JT, Almeida RC (2014). A hybrid ten-species phase-field model of tumor growth. *Math. Models Methods Appl. Sci.* 24:2569–2599. doi:10.1142/s0218202514500304.
- Logg A, Mardal KA, Wells G (2012). *Automated Solution of Differential Equations by the Finite Element Method: The FEniCS Book.* Springer. doi:10.1007/978-3-642-23099-8.
- Logg A, Wells GN (2010). DOLFIN: automated finite element computing. *ACM Trans. Math. Softw.* 37(2). doi:10.1145/1731022.1731030.
- Lowengrub JS, Frieboes HB, Jin F, et al. (2009). Nonlinear modelling of cancer: bridging the gap between cells and tumours. *Nonlinearity* 23:R1. doi:10.1088/0951-7715/23/1/r01.
- Merkel D (2014). Docker: lightweight Linux containers for consistent development and deployment. *Linux J.* 2014(239):2.
- Microsoft. Visual Studio Code [software: development environment]. https://code.visualstudio.com (accessed October 2026).
- MPICH. MPICH: high-performance portable MPI, version 5.0.1 [software]. https://www.mpich.org †
- National Lung Screening Trial Research Team (2011). Reduced lung-cancer mortality with low-dose computed tomographic screening. *N. Engl. J. Med.* 365:395–409. †
- OpenAI. gpt-6-astra [large language model], accessed through the provider `openai-codex` in Cline (accessed October 2026).
- Raue A, et al. (2009). Structural and practical identifiability analysis of partially observed dynamical models by exploiting the profile likelihood. *Bioinformatics* 25:1923–1929. †
- Rockne RC, Scott JG (2019). Introduction to mathematical oncology. *JCO Clin. Cancer Inform.* 3:1–4. doi:10.1200/CCI.19.00010.
- Schlicke P, Kuttler C, Schumann C (2021). How mathematical modeling could contribute to the quantification of metastatic tumor burden under therapy: insights in immunotherapeutic treatment of non-small cell lung cancer. *Theor. Biol. Med. Model.* 18:1–15.
- Schwarz G (1978). Estimating the dimension of a model. *Ann. Stat.* 6:461–464. †
- Scibilia KR, Schlicke P, Schneller F, Kuttler C (2024). Predicting resistance and pseudoprogression: are minimalistic immunoediting mathematical models capable of forecasting checkpoint inhibitor treatment outcomes in lung cancer? *Math. Biosci.* 109287. doi:10.1016/j.mbs.2024.109287. PMID 39218211.
- Sobol IM (2001). Global sensitivity indices for nonlinear mathematical models and their Monte Carlo estimates. *Math. Comput. Simul.* 55:271–280. †
- Tashman LJ (2000). Out-of-sample tests of forecasting accuracy: an analysis and review. *Int. J. Forecast.* 16:437–450. †
- The Cancer Genome Atlas Research Network (2012). Comprehensive genomic characterization of squamous cell lung cancers. *Nature* 489:519–525. †
- Verhulst PF (1838). Notice sur la loi que la population suit dans son accroissement. *Corresp. Math. Phys.* 10:113–121. †
- Virtanen P, et al. (2020). SciPy 1.0: fundamental algorithms for scientific computing in Python. *Nat. Methods* 17:261–272. †
- Vivli. Vivli – Center for Global Clinical Research Data [data-sharing platform]. https://vivli.org †
- Wagner A, Schlicke P, Fritz M, Kuttler C, Oden JT, Schumann C, Wohlmuth B (2023). A phase-field model for non-small cell lung cancer under the effects of immunotherapy. *Math. Biosci. Eng.* 20:18670–18694. doi:10.3934/mbe.2023828.
- Wagner A, Schlicke P, Fritz M, Kuttler C, Oden JT, Schumann C, Wohlmuth B (2023, preprint). A phase-field model for non-small cell lung cancer under the effects of immunotherapy. arXiv:2303.09378 (v1, 16 March 2023).
- Wagner A, et al. (2023, code repository). immunotherapy-lung-cancer [source code and patient data]. GitHub: https://github.com/wagnandr/immunotherapy-lung-cancer, commit fa8e6229d1540d33014a994f1ea309d6525597aa (14 August 2023). No licence.
- Zappa C, Mousa SA (2016). Non-small cell lung cancer: current treatment and future advances. *Transl. Lung Cancer Res.* 5. doi:10.21037/tlcr.2016.06.07.

---

## Supplementary material

- **S1. Execution logs and checksums.** See `T01_phasefield/logs/`, `T06_P2_H01/logs/` and the SHA-256 headers of each log.
- **S2. Protocol cross-check on ADRIATIC (T02/T04/T05).** See `Resultados/Integrado/INFORME_INTEGRADO_F0_F1.md` §3.3–3.5 and §5.2, including the failing unit test (`test_e20b_all_replicates_same_truth_and_diagnostics`). That test fails for 7 of 400 synthetic curves because steps narrower than PDF coordinate precision cannot be represented. It has no measurable effect on any metric, and it was retained and declared rather than modified after the fact.
- **S3. Independent review report (T03).** See `Resultados/Trabajo_Cline/T03_revision_T01/REVISION_T03.md`.
- **S4. Traceability.** Claim → file → execution → verification: `Resultados/Integrado/INFORME_INTEGRADO_F0_F1.md` §10. For H01 (T06), see the table below.

| Claim | Source | Execution | Verification |
|---|---|---|---|
| H01 corrected in all 22 perturbed runs | `T06_P2_H01/data_derived/q_corr/*.json` (field `pk_antes`/`pk_usado`) | `logs/t06_p2_h01_20261012T235219Z.log` (exit 0) | `t06_resumen.json` → `registros_q` |
| Determinism (bit-exact) | `T06_P2_H01/data_derived/control_bug_comp1.json` | `logs/t06_control_bug_20261012T231050Z.log` (exit 0) | Compared with the T01 log |
| Δ_H01 of the 44 P2 indices; class "relevant" | `T06_P2_H01/data_derived/t06_p2_indices.csv`, `t06_resumen.json` | `src/analiza_t06.py` | Criteria in `PREESPECIFICACION_T06.md` (written before launch) |
| 88 values (P1 original, P2 corrected) | `T06_P2_H01/data_derived/t06_88_corregido.csv` | ídem | — |
| Resources and incidents | `T06_P2_H01/logs/docker_stats.csv`, `docker_inspect_final.txt`, `intento1_fallido_SIGBUS/` | — | — |

### S5. Step-by-step reproduction on another computer

The steps must be followed in order:
- Steps 1–4 prepare everything.
- Steps 5–8 reproduce the results of this paper (line E1).
- Step 9 is the optional ADRIATIC cross-check (line E2), which does not validate the E1 model.

**Rules for every run:**
- Never run the two heavy runs (steps 6 and 7) at the same time.
- Keep the computer from sleeping during them.
- Always write new runs to a separate folder, never into the reference folders: the analysis scripts overwrite their outputs, and the step-7 launcher deletes and rewrites `data_derived/q_corr`.

**Shell.** Commands are bash (Linux, macOS, or Windows with Git Bash). In Git Bash, prefix every `docker run` with `MSYS_NO_PATHCONV=1`.

**Further detail.** `Resultados/Trabajo_Claude/T01_phasefield/REPRODUCIR.md`, `T06_P2_H01/INFORME_T06.md` §4 and the companion methodology document, §6.

**Step 0. Requirements.**
- **Docker:** Docker Desktop on Windows and macOS, with at least 8 CPUs and about 8 GB of memory assigned to its virtual machine. The original runs used 8 CPUs and peaked at 1.4 GiB.
- **Python 3.10 outside Docker** for the analysis scripts. The original environment had numpy 1.26.4, matplotlib 3.10.9 and pymupdf.
- **Time:** about 9 h of computation in total. On the original host:
  - Table 2: 309 min;
  - determinism control: 37 min;
  - P2 correction: 184 min.
- **Project files:** a copy of this project's `Resultados/` folder, with our wrappers, the Docker recipe, the lock file, the reference logs and the derived data. The authors' code is not included (step 1).

**Step 1. Obtain the authors' code at the audited commit.**
1. Download `github.com/wagnandr/immunotherapy-lung-cancer` at commit `fa8e6229d1540d33014a994f1ea309d6525597aa` as a zip.
2. Check its SHA-256: `e45a8cd30cf57efea8980a60a952816c3a725cf3627acecadca0d41b1312acce`.
3. Unzip it outside the project folder.
4. Check that `reduced_models/local_sensitivity_analysis.py` has SHA-256 `e44eb9a974c0b8584b0f6922ee60d5b21cc0c0b9cb988d94f53dafbb5f96b3a8`. Each log prints this hash in its header.

The repository has no licence: do not modify or redistribute it.

**Step 2. Create clean working copies.** Our scripts are copied, and their reference outputs are removed from the copies. The only input kept is the transcribed published table.

```bash
P=/path/to/Paper_Cancer                     # copy of the project
REPO=/path/to/immunotherapy-lung-cancer-fa8e6229d1540d33014a994f1ea309d6525597aa
W=/path/to/rerun                            # new, empty folder
REF="$P/Resultados/Trabajo_Claude"          # reference results (read only)
mkdir -p "$W"
cp -r "$REF/T01_phasefield" "$W/T01"; cp -r "$REF/T06_P2_H01" "$W/T06"
cp "$REF/T01_phasefield/data_derived/tabla2_publicada.csv" "$W/"
rm -rf "$W"/T01/{data_derived,logs,figures} "$W"/T06/{data_derived,logs,figures}
mkdir -p "$W"/T01/{data_derived,logs,figures} "$W"/T06/{data_derived,logs,figures} \
         "$W"/runs_t01 "$W"/runs_t06/main/output "$W"/runs_t06/control/output
mv "$W/tabla2_publicada.csv" "$W/T01/data_derived/"
```

**Step 3. Build the container.**

```bash
docker build -t papercancer/t01-fenics2019:1 "$W/T01/env"
docker run --rm papercancer/t01-fenics2019:1 python -c \
  "import dolfin, numpy, scipy, joblib; print(dolfin.__version__, numpy.__version__, scipy.__version__, joblib.__version__)"
```

- **Expected versions:** 2019.1.0, 1.26.4, 1.15.2 and 1.6.0.
- **Pinned packages:** the Dockerfile pins only python 3.10, fenics-dolfin 2019.1.0 and numpy < 2, so a later build may resolve other versions of SciPy or PETSc.
- **Exact package set:** create the environment from `env/conda_explicit_lock.txt` (`conda create -n fx --file conda_explicit_lock.txt` inside a miniforge3 container; `REPRODUCIR.md` §1).
- **ARM computers** (e.g. Apple silicon) need `--platform linux/amd64`, because the lock file is for linux-64.

Neither the lock route nor the ARM route has been run in this project.

**Step 4. Smoke test (about 40 s).**

```bash
docker run --rm -v "$REPO:/repo:ro" -v "$W/T01/src:/src:ro" -v "$W/T01:/out" \
  -v t01_jitcache:/root/.cache papercancer/t01-fenics2019:1 python /src/smoke_test.py --days 10
```

It writes `logs/smoke_test.json`. On the original host it took 2.24 s per simulated day for P1 and 1.01 s for P2.

**Step 5. Pharmacokinetics (seconds, no Docker).**

```bash
cd "$W/T01" && python src/pk_check.py "$REPO/reduced_models" data_derived/pk_check.json
```

Expected (§4.1): 3 of 6 extrema within 0.1 %, with maximum errors of 0.107 %, 0.129 % and 0.129 %. The remaining PK diagnostics are listed in `REPRODUCIR.md` §3.

**Step 6. Table 2 with the original code (about 5 h).**

```bash
docker run -d --name t01_tabla2 --cpus 8 \
  -v "$REPO:/repo:ro" -v "$W/T01/src:/src:ro" -v "$W/T01:/out" -v "$W/runs_t01:/work" \
  -v t01_jitcache:/root/.cache -w /work papercancer/t01-fenics2019:1 bash /src/run_tabla2_original.sh
docker wait t01_tabla2 && docker rm t01_tabla2      # prints the exit code; expected 0
cd "$W/T01"
python src/compare_tabla2.py logs/tabla2_original_*.log data_derived/tabla2_publicada.csv data_derived/tabla2
python src/diag_escala_tabla2.py data_derived/tabla2_comparacion.csv data_derived/tabla2
python src/fig_tabla2.py data_derived/tabla2_diag_escala.csv figures/fig_tabla2
```

**Expected (§4.2):**
- raw script output: 0/88 reproduced, signs 88/88 and ranks 8/88;
- with ×α/100: 88/88 equal at three significant figures, maximum error 0.449 %.

To compare the raw indices with the reference run:

```bash
diff <(grep -o 'g_[a-z]*_list_p[12] = .*' logs/tabla2_original_*.log) \
     <(grep -o 'g_[a-z]*_list_p[12] = .*' "$REF/T01_phasefield/logs/tabla2_original_20261012T035307Z.log")
```

- **On the original host,** the determinism control (step 7) matched this log to every printed digit.
- **On another computer,** differences in the last digits are possible; this has not been verified.

**Step 7. P2 with H01 corrected (about 3.7 h). Start only after step 6 has finished.**

First the determinism control. It recomputes component 1 of P2 *with* the original defect (37 min):

```bash
docker run --rm --cpus 8 --shm-size=1g -e PYTHONPATH=/repo/reduced_models:/src \
  -v "$REPO:/repo:ro" -v "$W/T06/src:/src:ro" -v "$W/T06:/out" -v "$W/runs_t06/control:/work" \
  -v t01_jitcache:/root/.cache -w /work papercancer/t01-fenics2019:1 python -u /src/control_p2_bug.py 1
```

In this project the control ran inside `run_t06.sh`, alongside the first attempt of the main run. Running it on its own, as above, uses the same script but has not been done in this project.

Then the corrected run:

```bash
docker run -d --name t06_p2_h01b --cpus 8 --shm-size=1g \
  -v "$REPO:/repo:ro" -v "$W/T06/src:/src:ro" -v "$W/T06:/out" -v "$W/runs_t06:/work" \
  -v t01_jitcache:/root/.cache -w /work papercancer/t01-fenics2019:1 bash /src/run_t06_main.sh
docker wait t06_p2_h01b && docker rm t06_p2_h01b    # expected 0
```

- **`--shm-size=1g` is required.** Without it, the first attempt failed when the workers started (§3.1).
- **Automatic retries:** the launcher retries up to three times if a worker dies at start-up.

**Step 8. Analyse the corrected run and compare.**

```bash
cd "$W/T06"
python -I src/analiza_t06.py "$W"/T01/logs/tabla2_original_*.log logs/t06_p2_h01_*.log \
  "$W/T01/data_derived/tabla2_publicada.csv"
```

The script writes `data_derived/t06_resumen.json`, `t06_p2_indices.csv`, `t06_88_corregido.csv` and `figures/fig_h01.png` inside `$W/T06`.

**Expected (§4.3):**
- determinism difference 0.0 in the four indices;
- 22 perturbed runs arrive with the default PK triplet and are corrected;
- median |Δ| 12.6 % and maximum 45.2 %;
- 0 sign changes and 7 rank changes;
- class "relevant";
- the corrected P2 values agree with the published table in 1/44 cases at three significant figures.

**Tables 4 and 5.** To regenerate them, run `python -I src/tablas_paper.py <copy of the paper> "$W/T01/data_derived/tabla2_comparacion.csv" data_derived/t06_88_corregido.csv` on a **copy** of this manuscript. Then compare the blocks between the `TABLA_88` and `TABLA_H01` markers with the ones printed here.

**Step 9 (optional; line E2, ADRIATIC).** Follow `Resultados/Trabajo_Cline/T02_ADRIATIC/REPRODUCIR.md` (PowerShell) in a Python 3.10 environment created from `requirements_T02.txt`. Before running it:
- edit `project_root` and `python` in `config/config.yaml` for the new computer;
- place your own copy of the NEJM article PDF at the path given in the T02 task contract. The pipeline checks its SHA-256, and the PDF is not redistributed.

**Expected:**
- 18/18 pre-specified quantities;
- 22 of 23 tests pass. The failing test is the known resolution-limit case (S2).

**What will differ from the original runs:**
- run times and timestamps;
- the Docker image ID;
- if library versions differ, possibly the last printed digits.

The classifications and the numbers quoted above are the reference against which a reproduction should be judged.
