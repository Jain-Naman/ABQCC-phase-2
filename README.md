# Smart Coating: Investigating Quantum Computing for Corrosion Inhibition - Team USC

This repository contains the code, data, and methodology for a hybrid computational protocol aimed at simulating and analyzing molecule adsorption on alloy surfaces. This three-step approach leverages Density Functional Theory (DFT), quantum embedding models, and quantum algorithms to offer a scalable solution to tackle complex adsorption configurations in materials science.

## Overview of the Computational Protocol

Our protocol involves three key steps:

### Step 1: DFT Calculations
We perform plane-wave pseudopotential DFT calculations on free and molecule-covered alloy surfaces using Quantum ESPRESSO (QE) to identify stable adsorption configurations. The corresponding scripts are located in the `QE` directory.

The output files are post-processed to generate isosurface plots of single-electron orbitals, density of states, and localization indices, aiding in the selection of an active space for reduction. These scripts are available in the `utils` directory. Due to file size constraints, only a few output files are available here. The key figures and plots are presented in the submission report.

### Step 2: Quantum Embedding Models
Based on the strongly localized occupied and virtual orbitals from Step 1, quantum embedding models are developed to simplify the system while preserving essential interactions. We outline two embedding approaches:

1. **Hilbert Space Downsizing**: Reducing the system in the orbital space via QDET, using the WEST framework. Code for this is provided in `embedding/qdet`, showing the computational workflow. While we present the main workflow, multiple iterations and convergence tests are required in practice.

    - **Localization Factor Calculation**: We use `westpp_loc.in` to compute localization factors within a bounded volume around the adsorption site, selecting highly correlated KS orbitals above a chosen localization threshold for quantum computations.
    - **Renormalized Integrals**: Using `wstat.in` and `wfreq.in`, we compute renormalized 1- and 2-body integrals within an effective potential. Convergence testing on various parameters is necessary for accuracy.
    - The resulting 1- and 2-body integrals are then used to construct a second-quantized Hamiltonian, which can be mapped to a qubit Hamiltonian via techniques such as Jordan-Wigner or Bravyi-Kitaev.

2. **Real Space Downsizing**: We focus on a localized atomic region embedded in a mean-field environment, using a representative molecular structure, AlH₃, as described in the report. This approach captures the adsorption process while ensuring computational feasibility.

### Step 3: Quantum Calculations
Using the embedded models, we apply a variational quantum eigensolver (VQE) to compute ground state energies. Relevant notebooks are in the `vqe` directory under `embedding`. Although the code indicates simulator-based experiments, tests have also been run on hardware in hosted notebooks.

# Repository Structure
- adsorption/: Contains scripts and data related to adsorption process simulations
- benzotriazole/: Files and data specific to benzotriazole molecule calculations
- embedding/: Directory for quantum embedding models and related code
    - /qdet
        Contains WEST calculations, including wstat convergence tests and wfreq frequency calculations.
    - /vqe Code for variational quantum eigensolver (VQE) calculations using embedded models.
- utils/: Utility functions for various analysis tasks
    - /density_of_states -Scripts to calculate and analyze density of states (DOS)
    - /localization - Functions to compute localization indexes
- requirements.txt: Lists required Python packages and versions