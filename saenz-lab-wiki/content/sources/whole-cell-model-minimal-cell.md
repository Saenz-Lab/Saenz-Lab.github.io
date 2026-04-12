---
title: "Fundamental behaviors emerge from simulations of a living minimal cell"
tags: [minimal-cell, JCVI-Syn3A, whole-cell-model, computational-biology, collaborative]
# sources: [raw/text/WGWQP4WG.md]
date: 2022-01-20
draft: false
---

# Fundamental behaviors emerge from simulations of a living minimal cell

**Thornburg, Z. R.; Bianchi, D. M.; Brier, T. A.; Gilbert, B. R.; Earnest, T. M.; Melo, M. C. R.; Safronova, N.; Sáenz, J. P.; Cook, A. T.; Wise, K. S.; Hutchison, C. A.; Smith, H. O.; Glass, J. I.; Luthey-Schulten, Z.** (2022) *Cell*, 185(2), 345–360.e28. DOI: 10.1016/j.cell.2021.12.025

## Summary

This consortium effort, to which our group contributed lipidomic data and membrane expertise, presents the first whole-cell fully dynamical kinetic model (WCM) of [[jcvi-syn3|JCVI-Syn3A]], the minimal cell with 493 genes. Using cryo-electron tomograms for cell geometry and ribosome distributions, the model simulates time-dependent concentrations and reaction fluxes over a complete cell cycle. The WCM reveals how the cell balances metabolism, genetic information processing, and growth, and offers insight into the principles of life at the simplest organismal scale.

## Key Findings

- The WCM incorporates 493 genes, 155 gene products in 175 metabolic reactions organized into 7 subsystems (central, nucleotide, lipid, cofactor, amino acid, ion, and macromolecule metabolism).
- 3D spatial resolution from cryo-electron tomography provides realistic cell geometry (~400–500 nm diameter).
- Genome-wide mRNA half-lives emerge from length-dependent kinetics and diffusion without being explicitly programmed — a genuinely emergent property.
- Multiple DNA replication events per cell cycle are predicted and match qPCR experimental results.
- Detailed single-reaction, single-cell ATP cost accounting reveals how the cell allocates energy among transcription, translation, active transport, and growth.
- Emergent imbalances in metabolite concentrations lead to slowdowns in transcription and translation rates during the cell cycle.

## Our Contribution

Our group (Safronova, Sáenz) provided experimental lipidomic characterization and membrane biophysics data for parameterizing the lipid metabolism subsystem of the WCM. The lipid subsystem, though simple in Syn3A, is essential for membrane growth and cell division in the model.

## Significance

This paper represented a milestone in computational biology — the most complete dynamical model of a living cell to date. For our research program, it established the computational framework within which lipidome composition and membrane properties influence cellular behavior, directly motivating the experimental lipid diet work that followed in 2024–2025.
