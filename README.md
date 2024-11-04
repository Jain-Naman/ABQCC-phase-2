# Hybrid Quantum-Classical Protocol for Molecule-Surface Adsorption

This repository contains the code, data, and methodology for a hybrid computational protocol aimed at simulating and analyzing molecule adsorption on alloy surfaces. This three-step approach leverages Density Functional Theory (DFT), quantum embedding models, and quantum algorithms to offer a scalable solution to tackle complex adsorption configurations in materials science.

## Overview of the Computational Protocol
Our approach comprises the following key steps:

### Step A: DFT Calculations
Plane-wave pseudopotential DFT calculations are performed on free and molecule-covered alloy surfaces. These calculations identify stable adsorption configurations characterized by:

- Isosurface plots of single-electron orbitals
- Localization indexes to assess the electronic structure
### Step B: Quantum Embedding Models
Based on strongly localized occupied and virtual orbitals from Step A, quantum embedding models are developed to reduce the computational complexity. We propose two approaches for embedding:

Hilbert Space Downsizing: Reducing the system in terms of the orbital space.
Real Space Downsizing: Focusing on a localized atomic region while embedding it in a mean-field environment.
These models capture the essential physics of adsorption with reduced computational demand, while retaining accuracy.

### Step C: Quantum Calculations
Using the embedded models, we employ a variational quantum eigensolver (VQE) in Qiskit on IBM quantum simulators (or hardware, where feasible) to compute ground state energies. Additional resource estimation is provided for scaling to other quantum algorithms, including:

# Repository Structure
data/: Contains input files, pseudopotentials, and initial configurations.
src/: Code for DFT calculations, embedding routines, and VQE implementation.
results/: Output data, including isosurface plots, localization indexes, and energy values.
docs/: Documentation files with methodological details and references.


