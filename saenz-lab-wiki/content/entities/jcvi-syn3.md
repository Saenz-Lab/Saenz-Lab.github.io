---
title: "JCVI-Syn3A / JCVI-Syn3B (Minimal Cells)"
tags: [organisms, minimal-cell, synthetic-biology, mycoplasma]
# sources: [raw/text/FHGU23H2.md, raw/text/FVHV7JGJ.md, raw/text/4SVULMWD.md, raw/text/Y4EHR7L6.md, raw/text/WGWQP4WG.md]
date: 2026-04-11
draft: false
---

# JCVI-Syn3A / JCVI-Syn3B

JCVI-Syn3A and JCVI-Syn3B are genomically minimal cells derived from [[mycoplasma-mycoides|*Mycoplasma mycoides*]] subsp. capri str. GM12 by systematic genome reduction at the J. Craig Venter Institute. They retain only essential or quasi-essential genes and represent the simplest known self-replicating organisms.

## Genome and Design

- **JCVI-Syn3.0**: the original minimal cell with the smallest genome (473 genes), but exhibited pleomorphism and irregular cell division.
- **JCVI-Syn3A**: Syn3.0 plus 19 additional genes restoring regular spherical morphology and cell division (~493 genes, 543 kbp). Used for the whole-cell kinetic model (Thornburg et al., 2022, [[whole-cell-model-minimal-cell|Cell]]) and lipidome minimization experiments (Justice et al., 2024, [[tuneable-minimal-cell-membrane|Nature Communications]]).
- **JCVI-Syn3B**: a near-identical variant used for lipidome adaptation studies (Safronova et al., 2024, [[temperature-lipidome-adaptation-minimal-cells|Cell Reports]]; Safronova et al., 2024, [[chemically-defined-lipid-diets|bioRxiv]]; Oertel et al., 2025, [[metabolic-heat-flow-minimal-cell|bioRxiv]]).

## As a Membrane Model System

Minimal cells are ideal for studying [[lipidome-design-principles|lipidome design principles]] because:
- They have a **single plasma membrane** (no cell wall, no outer membrane) — what you measure is what you get.
- They have **minimal lipid biosynthetic capacity**, relying on lipids from growth media. This enables experimental control of lipidome composition through lipid diets.
- Their **small genomes** make comprehensive characterization and modeling feasible.

## Key Findings from Our Work

- A **two-component lipidome** (cholesterol + one phospholipid) supports life in Syn3A (Justice et al., 2024, [[tuneable-minimal-cell-membrane|Nature Communications]]).
- Syn3B exhibits **lipidome flexibility** in response to temperature, but with **impaired head-group-specific acyl chain remodeling** compared to *M. mycoides* — associated with impaired homeoviscous adaptation (Safronova et al., 2024, [[temperature-lipidome-adaptation-minimal-cells|Cell Reports]]).
- **Lipidome diversity enhances robustness** to osmotic stress and correlates with maximal growth rate (Safronova et al., 2024, [[chemically-defined-lipid-diets|bioRxiv]]; Oertel et al., 2025, [[metabolic-heat-flow-minimal-cell|bioRxiv]]).
- Cyclodextrin-mediated lipid diets produce lipidomes with 7 to ~30 species, enabling systematic exploration of lipidome complexity (Safronova et al., 2024, [[chemically-defined-lipid-diets|bioRxiv]]).
