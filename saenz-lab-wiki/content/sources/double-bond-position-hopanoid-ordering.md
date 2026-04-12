---
title: "Varying the position of phospholipid acyl chain unsaturation modulates hopanoid and sterol ordering"
tags: [hopanoids, sterols, diplopterol, cholesterol, double-bond-position, membrane-ordering, mesoplasma-florum, corresponding-author]
# sources: [raw/text/F24YVYAP.md]
date: 2024-07-02
draft: false
---

# Varying the position of phospholipid acyl chain unsaturation modulates hopanoid and sterol ordering

**Nguyen, H. N. A.; Sharp, L.; Lyman, E.; Sáenz, J. P.** (2024) *Biophysical Journal*, 123(13), 1896–1902. DOI: 10.1016/j.bpj.2024.06.002

## Summary

Why do both sterols and [[hopanoids]] persist across the tree of life, given their convergent ability to order membranes? We found the answer lies in how they interact with unsaturated phospholipids. Using monolayer experiments, molecular dynamics simulations, and cellular assays in *Mesoplasma florum*, we showed that [[diplopterol]] and cholesterol order unsaturated phospholipids differently depending on the position of the double bond along the acyl chain. Cholesterol condenses phospholipids regardless of double bond position (Δ6, Δ9, or Δ11), while diplopterol's ordering capacity is restricted — it condenses only the Δ11 isomer and has an unfavorable interaction with the common Δ9 position. This difference traces to the methyl group distribution on the hopanoid ring: the M2 methyl group overlaps with the Δ9 double bond, sterically hindering packing.

## Key Findings

- Cholesterol condenses all three PC double bond isomers (Δ6, Δ9, Δ11) and shows increasingly favorable ΔG_mix as the double bond moves away from the headgroup.
- [[diplopterol|Diplopterol]] condenses only Δ11-PC (ΔG_mix < 0), is ideally mixed with Δ6-PC (ΔG_mix ≈ 0), and interacts unfavorably with Δ9-PC (ΔG_mix > 0). The distinction between Δ9 and Δ11 is striking — the double bonds are only two carbons apart.
- **Molecular dynamics simulations** revealed the structural basis: the Δ9 double bond position overlaps with diplopterol's M2 methyl group along the membrane normal, preventing efficient packing. The Δ11 double bond falls between M3 and M4 methyl groups, avoiding steric clash.
- ²H NMR order parameters (S_CD) from simulations confirmed that diplopterol orders Δ11 chains more effectively than Δ9 chains, while saturated chains were ordered similarly regardless of which unsaturated isomer was present.
- **In vivo validation**: In *M. florum* fed defined lipid diets, cells with Dpop + Δ9-PC were significantly more susceptible to osmotic lysis than cells with Dpop + Δ11-PC. With cholesterol, double bond position made no difference.
- Notably, [[methylobacterium-extorquens|*Methylobacterium extorquens*]] — a hopanoid producer — uses Δ11 as its primary unsaturation position (Chwastek et al., 2020, [[principles-membrane-adaptation|Cell Reports]]), and the hopanoid-producing yeast *S. japonicus* has a Δ12-desaturase. This suggests co-evolution of hopanoid production and double bond positioning.

## Methods

- **Langmuir monolayers**: pressure–area isotherms at 20 °C, with condensation effect and ΔG_mix calculations for Chol/Dpop with Δ6-, Δ9-, Δ11-PC.
- **Molecular dynamics**: CHARMM36 force field; ~550 lipids/leaflet; 500 ns production runs; binary mixtures of Dpop with D9/D11-DOPC and D9/D11-POPC at 4 compositions. New CHARMM-compatible Dpop model developed via CGenFF.
- **Mesoplasma florum assays**: growth in chemically defined lipid diets (Dpop or Chol, with D9- or D11-PC, egg SM, palmitic acid); osmotic shock assay with propidium iodide.

## Significance

This paper resolved a longstanding puzzle: why do both sterols and hopanoids persist when they have convergent ordering functions? The answer is that cholesterol has a broader ordering capacity — it works with diverse double bond positions — while diplopterol's ordering is constrained by its methyl group topology. This constraint may have limited hopanoid-containing organisms to lipidomes with specific double bond positions (like Δ11), while cholesterol's versatility enabled the exploration of diverse eukaryotic lipidomes. The paper also identified double bond position as a tunable "knob" that hopanoid-producing bacteria may use to regulate lipid ordering homeostatically.
