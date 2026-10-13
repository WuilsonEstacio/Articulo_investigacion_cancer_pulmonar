# Entorno de T01: FEniCS legado 2019.1.0 (dolfin) desde conda-forge, en Linux.
# Motivo: el código original importa dolfin (2019.1.0); no existe build win-64 y la imagen oficial
# quay.io/fenicsproject/stable:2019.1.0.r3 usa un manifiesto v1 que Docker 29/containerd>=2.1 ya no admite.
FROM condaforge/miniforge3:latest
RUN mamba create -y -n fx -c conda-forge \
      python=3.10 "fenics-dolfin=2019.1.0" "numpy<2" scipy matplotlib tqdm joblib pandas \
    && mamba clean -afy
ENV PATH=/opt/conda/envs/fx/bin:$PATH
ENV OMP_NUM_THREADS=1
WORKDIR /work
