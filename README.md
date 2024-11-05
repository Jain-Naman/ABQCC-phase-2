# Smart Coating: Investigating Quantum Computing for Corrosion Inhibition - Team USC

This repository contains the code, data, and methodology for a hybrid computational protocol aimed at simulating and analyzing molecule adsorption on alloy surfaces. This three-step approach leverages Density Functional Theory (DFT), quantum embedding models, and quantum algorithms to offer a scalable solution to tackle complex adsorption configurations in materials science.

## Overview of the Computational Protocol
Our approach comprises the following key steps:

### Step 1: DFT Calculations
Plane-wave pseudopotential DFT calculations are performed on free and molecule-covered alloy surfaces using Quantum Espresso (QE). These calculations identify stable adsorption configurations. These scripts are located in `QE` directory. 

The output files are then post-processed to obtain isosurface plots of single electron orbitals, density of states and localizatoin indices. These are helpful in selecting an active space for reduction. The scripts used for these tasks are available under `utils`. Not all output files are uploaded here, due to large file sizes. The necessary figures and plots are presented in the submission report.

### Step 2: Quantum Embedding Models
Based on strongly localized occupied and virtual orbitals from Step 1, quantum embedding models are developed to reduce the computational complexity. We propose two approaches for embedding:

Downsizing in the Hilbert space: Reducing the system in terms of the orbital space. This is acheived by employing the QDET approach using WEST. The code for this is avialble under `embedding/qdet`. We only provide a computatoinal workflow here. In principle, multiple iterations and convergence tests have to be performed. 
    
- In order to select the highly correlated orbitals, we use `westpp_loc.in` to calcualte the localization factors in a bounded volume around the adsorption site.  
- The KS orbitals having localization above a chosen threshold form the reduced Hilbert space for quantum computing calculations.

For example, convergence tests for the parameter 

Real Space Downsizing: Focusing on a localized atomic region while embedding it in a mean-field environment.
These models capture the essential physics of adsorption with reduced computational demand, while retaining accuracy.

### Step 3: Quantum Calculations
Using the embedded models, we employ a variational quantum eigensolver (VQE) in Qiskit on IBM quantum simulators (or hardware, where feasible) to compute ground state energies. Additional resource estimation is provided for scaling to other quantum algorithms, including:

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




 westpy - <version>
    qiskit - 1.2.4
    qiskit_nature - 0.7.2

        ! <Write a little about WEST: - wstat convergence tests -wfreq calculations >