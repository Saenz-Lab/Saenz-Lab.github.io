# PI Review Checklist

Scientific accuracy review for wiki content before publication. Formatting has already been checked.

---

## 1. Entity Pages

### diplopterol.md
- The page states diplopterol "interacts favorably only with saturated lipids (lipid A, sphingomyelin) and repulsively with unsaturated phospholipids." The double-bond paper (Nguyen 2024) later showed diplopterol *does* condense Delta-11-unsaturated PCs favorably. Should this page be qualified to say "repulsively with Delta-9-unsaturated phospholipids" rather than all unsaturated phospholipids?
- Diffusion times are given as "~14 ms for Atto532-SM vs. ~2 ms in DOPC." Are these the correct values, or are they diffusion *coefficients* that should have different units?

### crocosphaera-watsonii.md
- The page says "We proposed instead that high hopanoid content reduces membrane permeability to antimicrobial toxins in the environment." Was this the specific framing in the 2012 Geobiology paper, or was the hypothesis stated more cautiously (e.g., general permeability barrier, not specifically antimicrobial toxins)?

### methylobacterium-extorquens.md
- The page says carotenoids are "C30 carotenoids (squalene-derived, not the expected C40 phytoene pathway)." The Rizk 2021 paper describes deleting hpnE. Is it accurate to call hpnE "hydroxysqualene oxidoreductase"? The text in the Key Experimental Tools section calls it that, but the Rizk source page describes it differently (disrupts both hopanoid and carotenoid biosynthesis). Is the enzyme name precisely right?

### bacteriohopanepolyols.md
- The page says "Response factors vary significantly between BHP structures, so absolute quantification is reliable only for BHT and BHpentol." Is BHpentol correct here, or should it be BHaminotriol or another specific structure?

### jcvi-syn3.md
- Syn3A is listed as "~493 genes, 543 kbp." Are these numbers correct? The original Breuer et al. 2019 paper gives 493 genes for Syn3A, but confirm the 543 kbp genome size is for Syn3A specifically (not Syn3.0, which is 531 kbp).

### hopanoids.md
- The Evolutionary Significance section says "the capacity to order membranes through polycyclic isoprenoids could predate the Great Oxidation Event (~2.4 Ga)." Is 2.4 Ga the number you would use, or do you prefer ~2.3 Ga or a range?

### lipid-a.md, mycoplasma-mycoides.md
- These pages look solid. No flags.

---

## 2. Concept Pages

### lipidome-design-principles.md
- "Diplopterol condenses Delta-11-unsaturated lipids effectively but has an unfavorable interaction with the common eukaryotic Delta-9 position." The Nguyen 2024 paper showed this in model membranes and M. florum, but is it accurate to call Delta-9 "the common eukaryotic" position here? Eukaryotes use Delta-9 prominently, but also Delta-5, Delta-6, etc. Is the framing precise enough?

### membrane-ordering.md
- "Reduced diffusion relative to Ld (~7-fold slower, based on FCS measurements of ~14 ms vs. ~2 ms diffusion times)" -- same question as on diplopterol.md. Are these diffusion *times* from FCS autocorrelation? The 7-fold ratio sounds right for Lo vs Ld, but confirm the absolute values.

### hopanoid-sterol-analogy.md
- Under Key Differences: "Cholesterol interacts favorably across a broader range of unsaturation." This was the framing in the 2015 PNAS paper, but the 2024 Biophysical Journal paper showed cholesterol's interaction is also position-dependent (increasingly favorable from Delta-6 to Delta-11). Should this be updated to reflect that cholesterol is broader but still position-dependent?

### rna-lipid-interactions.md
- "Liquid-phase membranes trigger RNA degradation, preferentially in single-stranded regions." Is "trigger" the right word? Does the Czerniak 2025 paper show that the membrane actively causes degradation, or that it accelerates degradation that would occur anyway (e.g., by exposing ssRNA to hydrolysis)?

### hopanoid-biomarkers.md
- The page states adenosylhopane is "absent from marine blue water." Was it truly absent (below detection limit), or just not detected in the specific transect samples? This matters for how strongly the claim is worded.

---

## 3. Source Pages (flagged items only)

### functional-diversity-isoprenoid-lipids.md
- Key Findings: "The DeltahpnE mutant (lacking hopanoids and carotenoids, since both depend on squalene) showed impaired growth at 35C." Since DeltahpnE lacks both, the hopanoid-specific phenotype attribution relies on comparing DeltahpnE with DeltacrtB. Is it stated clearly enough that the membrane phenotypes are attributed to hopanoid loss specifically because DeltacrtB (which retains hopanoids) shows no membrane defects?

### double-bond-position-hopanoid-ordering.md
- "The M2 methyl group overlaps with the Delta-9 double bond, sterically hindering packing." Is it specifically the M2 methyl group (C-2 position on the A ring), or one of the other ring methyl groups? The source page also mentions "M3 and M4 methyl groups" for the Delta-11 position -- confirm the nomenclature matches the paper's figure.

### tuneable-minimal-cell-membrane.md
- "Acyl chain diversity is more important for growth than head group diversity." Was this shown as a general principle, or specifically for the lipid combinations tested? The claim as written could be read as universal.

### temperature-lipidome-adaptation-minimal-cells.md
- "Lipid abundances follow a universal logarithmic distribution shared across eukaryotes and bacteria." Was this a log-normal rank-abundance distribution, or a different logarithmic form? The word "universal" is strong -- was it demonstrated across enough taxa to warrant that?

All other source pages look accurate. The biogeochemistry papers (BHPs, anammox, marine cyanobacteria) and the RNA-lipid papers read cleanly.
