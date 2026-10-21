# Four-exam and question-bank verification report

Method: for each unit bank and each predicted exam, an independent reviewer solved every MCQ blind (before opening the solutions), then compared with the key, re-derived every FRQ calculation, checked point totals, viewed every figure, and fixed discrepancies.

- MCQ with a final key: 680 (unit banks 360 + exams 320).
- Final keys that equal the independent blind answer: 679 / 680.
- Residual differences between final key and logged blind answer: [('QB-U2-MCQ013', 'D', 'A')]. (QB-U2-MCQ013: the blind log recorded A, but the question has one defensible answer, D — land bridges exposed by lower sea levels; D re-confirmed by manual review, so this is a logging slip.)
- One genuine key error was found and corrected during verification: PE2-MCQ014 (sea-turtle survivorship; the figure's curve Z is the Type III curve, so the key is A). Re-confirmed by viewing the figure.
- Key-letter balance across all 680 MCQ: {'A': 172, 'B': 170, 'C': 169, 'D': 169}.


---
### verify_PE1.md
# Verification — PE1 (Predicted Practice Exam 1)

**Items checked:** 80 MCQ, 3 FRQ, 17 figure PNGs (all viewed), 83 solution blocks.

**Unit mix (MCQ):** U1 6, U2 5, U3 10, U4 10, U5 10, U6 10, U7 7, U8 7, U9 15 = 80. Matches the target exactly; no deviation.

**Blind solve vs key:** 80/80 agreement (100%). Blind answer letters were A 20, B 20, C 20, D 20 (key identical, perfectly balanced). No MCQ was flagged as ambiguous, wrong, or dependent on missing data. All calculations (Q3, 5, 6, 17, 20, 25, 28, 31, 35, 36, 40, 46, 48, 50, 56, 61, 63, 65, 71, 72, 76, 78) were recomputed and match the keyed values and the distractor derivations given in the solutions.

**Disagreements / fixes:** none. No edits were made to the questions or solutions.

**FRQ audit (points sum to 10 each; every part answered in the solution):**
- FRQ1 (1+1+2+1+2+1+2 = 10): sound. No errors.
- FRQ2 (1+1+2+1+2+1+2 = 10): 35/42 = 83.3% correct; 2030 estimate 86 cm (recent rate) / 84 cm (linear) correct. No errors.
- FRQ3 (2+2+1+1+1+1+2 = 10): recomputed 394,200 kWh; $40,300 + $5,052 = $45,352; payback 7.17 ≈ 7.2 yr; 3,942 t CO2; 4,800 kg N. All correct.

**IDs / structure:** 83 questions and 83 solution blocks, IDs identical, no duplicates. All 17 referenced figure files exist.

**Figures:** all readable and consistent with their stems and solutions (grid-mix 2024 wind 200 + solar 300 of 1,000 GWh; sea ice 7.8 → 3.9; inversion 200–500 m; LD50 ~10 vs ~100; ENSO negative 2021-22). Minor cosmetic only, left unchanged: in PE1_FRQ1_estuary.png the italic "Drainage ditches..." line and the bottom "Not to scale" caption straddle the edge of the farmland shading, and the H2 label touches the marsh outline; all text remains legible.

**Distractor length:** the keyed option is the longest in 41/80 items, but never conspicuously so (largest ratio to the runner-up is 1.15, MCQ052; the only other cases are numeric options). No rebalancing edits were needed.

**Unresolved:** none.


---
### verify_PE2.md
# Verification — PE2 (Predicted Practice Exam 2)

**Checked:** 80 MCQ + 3 FRQ, 83 solution blocks (IDs match 1:1), 18 figure PNGs viewed.

**Unit mix (MCQ):** U1 6, U2 5, U3 10, U4 10, U5 10, U6 10, U7 7, U8 7, U9 15. This matches the target exactly; no deviation. FRQ units: FRQ1 U9 (type 1), FRQ2 U7 (type 2), FRQ3 U6 (type 3).

**Blind agreement:** 79/80 (98.8%). Every calculation item (003, 004, 016, 020, 036, 040, 049, 050, 051, 058, 062, 063, 070, 074, 076, 078) was recomputed and matches the key.

**Disagreement**
- PE2-MCQ014 (sea turtles, survivorship). Key said D (curve X), which is a Type I curve (high survival to old age). Sea turtles are Type III, curve Z, which is option A. The reviewer was right. Fix: key changed to A and the explanation rewritten. Final key letter counts: A 21, B 20, C 20, D 19.

**Distractor rebalancing (wording only, 11 option lines in 4 items):** 046, 048, 065 and 071. In each the correct option was conspicuously the longest or most hedged. The distractors were lengthened, and no keys changed.

**FRQ audit (no errors found)**
- FRQ1: points 1+1+2+3+1+1+1 = 10.
- FRQ2: 1+2+1+1+2+2+1 = 10. The percent change is (92−134)/134 = −31.3%, which is correct. The table and Figure 1 are consistent with the solution (Dec 170 and Jan 150 are the highest PM2.5 months, with 16 and 14 inversion days).
- FRQ3: 2+2+1+2+1+2 = 10. Arithmetic verified: 800×0.5×8,760 = 3,504,000 MWh; ×0.95 = 3,328,800 t CO₂; evaporation 2.4×10⁸ m³; city use 2.7375×10⁸ m³; 87.7% ≈ 88%.
- Every part has a solution and a scoring idea.

**Figure problems fixed (cosmetic):**
- PE2_frq1_fragment.png: the "0 m" label was struck through by the edge line, "Forest edge" overlapped the edge line, and the plantation title sat against the top border. All three fixed in make_PE2.py and regenerated.
- PE2_tolerance.png: the dotted and dashed temperature lines ran through their "28 °C" and "30 °C" labels. Lines shortened, regenerated.
- All other figures are clean and consistent with their stems and keys. Figure readings were confirmed: 300 ha ≈ 45 species, LD50 of Q ≈ 8 and P ≈ 40, Country M is in Stage 3, coral bleaching >35% only when SST ≥ 30.9 °C.

**Unresolved:** none. Minor note: MCQ009 (diff 2) depends on a graph reading of ≈45, and the distractors (38, 41, 52) are well separated, so it is acceptable.


---
### verify_PE3.md
# Verification report: PE3 (Predicted Practice Exam 3)

**Checked:** 80 MCQ + 3 FRQ, 83 solution blocks (one per ID, IDs match), all 19 figure PNGs viewed.

**Unit mix (MCQ):** U1 6, U2 5, U3 10, U4 10, U5 10, U6 10, U7 7, U8 7, U9 15. Matches the required mix exactly; no deviation. FRQs: FRQ1 (U9, investigation), FRQ2 (U3, data), FRQ3 (U5, calculations).

**Blind agreement:** 80/80 (100%) after blind solve (keyed letters A/B/C/D = 20 each). Low-risk notes only: MCQ018 (growth rate must include migration, giving +0.2%; A is the natural-increase trap, key B is correct); MCQ003 (Site Q totals about 900 mm, dry June to September, savanna is correct).

**Disagreements / fixes to questions:** none needed (no wrong keys, no double-defensible items).

**Distractor balance (7 edits to PE3.md):** the correct option was the longest in 35 of 80 items. Shortened correct options in MCQ046, 053, 058, 065, 071, 079, 080 (meaning unchanged, keys unchanged; MCQ065 no longer carries the "chemical is not identified" hedge, which the solution still covers).

**FRQ audit:** points sum to 10 in all three (FRQ1 1+1+1+2+1+2+1+1; FRQ2 1+1+2+2+2+2; FRQ3 1+2+2+2+1+1+1). Arithmetic re-checked: FRQ2(b) 3.1%; FRQ3 (a) 1.2×10⁸ MJ, (b) 4.8×10⁶ MJ, (c) 1.92×10⁶ MJ and about 526 people, (d) 3.75×10⁷ MJ, about 10,274 people, ratio about 19.5, (e) 3.6×10⁶ vs 3.0×10⁶ kg, 20% over. All correct; every part answered; no errors found. Minor looseness only (FRQ2(f) solution pairs the 60-year TFR drop with 2000–2020 infant-mortality data; acceptable).

**Figures:** all exist, no clipping. One defect fixed: in PE3_frq2_tfr.png the "Replacement level (2.1)" label was overprinted by Country B's line and marker; moved the label (make_PE3.py line 201) and regenerated.

**Solution accuracy:** all numeric values quoted in explanations match the figures and tables (e.g., MCQ003 900 mm, MCQ021 gaps, MCQ031 catches, MCQ056 60%/6%/1,500%, MCQ074 increments).

**Unresolved:** none.


---
### verify_PE4.md
# Verification report: PE4 (Predicted Practice Exam 4)

**Items checked:** 80 MCQ + 3 FRQ; 83 solution blocks, IDs match one-to-one and in order with the questions file; 20 figure PNGs viewed (18 MCQ + 2 FRQ).

**Unit mix (MCQ):** U1 6, U2 5, U3 10, U4 10, U5 10, U6 10, U7 7, U8 7, U9 15 (total 80). Matches the requested mix exactly; no deviation.

**Blind answer check:** 80/80 agreement (100%). Key distribution A 20, B 20, C 20, D 20. All calculations recomputed (e.g., Q15 1.6%, Q21 K = 7, Q31 4.5 x 10^6 m3, Q40 351,000 kg, Q41 9.1%, Q50 1.1 x 10^6 t, Q58 4,800 t, Q65 30 yr, Q73 about 15%, Q78 10.4 Mt/yr). Only soft note: Q79 (negative feedback = increased outgoing IR) is correct but the least familiar of the options; kept as is.

**Disagreements:** none.

**FRQ audit:** Points sum to 10 for each (FRQ1 1+1+2+1+2+1+2; FRQ2 1+1+1+2+2+1+2; FRQ3 1+1+2+1+1+1+3). Arithmetic verified: FRQ2 2.2 ppm/yr, 45.2%, 461 ppm in 2040; FRQ3 1.2 x 10^6 L, 3,840 t, 3,336 t (13.1% reduction), 200 ha, 1.1 x 10^6 m3. Every part answered with a sensible scoring idea. No errors found; no FRQ edits.

**Figures:** all 20 exist, are legible, unclipped and consistent with the stems (Q4 pyramid gives 10% and 60 kJ; Q11 species X dead at 31 C; Q30 point P is El Nino; Q51 net energy 3 vs 11 MJ; Q64 LD50 about 8 vs 120). No problems.

**Distractor rebalancing (4 edits, wording only, answers unchanged):** Q19 D, Q43 A, Q55 D, Q56 D shortened so the correct option is no longer conspicuously the longest.

**Unresolved:** none.


---
### verify_U1.md
# Verification U1 (Book 2 / Book 3)

Items checked: 32 MCQ, 4 FRQ, 9 figures (all viewed; none clipped or overlapping; all referenced files exist). One solution block per question; IDs match.

Blind agreement: 32/32 keyed answers matched. Key letters balanced 8/8/8/8.

Disagreements: none. Solution wording errors fixed:
- QB-U1-MCQ022 solution said frogs are predators "of snakes"; corrected (frogs are prey of snakes).
- QB-U1-MCQ014 solution: vague explanation of distractors B and C reworded (key unchanged, +6 Gt C verified).

FRQ audit: points sum to 10 in all four (FRQ001 1+1+2+2+1+1+2; FRQ002 1+2+2+2+1+1+1; FRQ003 1+2+2+1+1+1+2; FRQ004 1+1+2+1+2+1+2). Arithmetic re-verified: GPP total 7,990, respiration 3,990, 49.9%; 1.8×10¹⁰ kcal/yr, 1.8×10⁸, 197 people, 19,700 people; 89% kelp decrease. No FRQ errors found.

Distractor rebalancing (correct option was longest): edits to MCQ013, 016, 019, 027, 029, 031, 032 (shortened correct options; lengthened distractors in 013, 016). Meaning and keys unchanged.

Figures: all legible. Minor note: FRQ001 lake figure shows an unlabeled outlet arrow (harmless).

Unresolved: none.


---
### verify_U2.md
# Verification — Unit 2 (QB-U2)

Items checked: 28 MCQ, 4 FRQ, 8 figure PNGs (all viewed), 32 solution blocks (one per question, IDs match, no duplicates).

MCQ blind agreement: 28/28 (100%) with the keyed answers. Key letters balanced 7/7/7/7. All calculations recomputed (MCQ011 = 25, MCQ015 = 59%, MCQ017 = $378,000, MCQ024 = $38.4 M, MCQ025, MCQ028 ratios).

Disagreements: none. No question has two defensible answers.

FRQ audit: points sum to 10 in all four (FRQ001 1+1+2+2+2+1+1; FRQ002 2+1+1+2+2+2; FRQ003 4+2+1+1+1+1; FRQ004 1+1+2+1+2+1+2). All arithmetic rechecked (352%, 0.625 and 0.048 yr⁻¹, 300 ha, $1,710, $9,210, $2,763,000, $1,140,000, $1,623,000, 1,800 t, 50%, -50%). Every part answered. No errors found.

Figures: all referenced files exist; no clipping or overlap. Figures agree with stems (island model equilibria 40 and 15; tolerance ranges P 16-26, Q 6-34, R 24-38; table data match plots).

Distractor rebalancing: 8 wording edits shortening conspicuously long correct options (MCQ009, 010, 013, 018, 022, 023, 025, 027). Keys and letters unchanged; solutions remain valid.

Unresolved: none.


---
### verify_U3.md
# Verification report — Unit 3 (QB-U3)

**Items checked:** 44 MCQ, 4 FRQ, 48 solution blocks (one per question, IDs match, no duplicates); 10 figure PNGs viewed (surv, logistic, deer, yeast, pyramids, dtm, tfr, frq1, frq2, frq4). Key letters balanced 11/11/11/11.

**Blind agreement:** 44/44 (100%). Only note: MCQ024 (blind confidence medium). Computed retiree-to-worker ratio after a 30-year cohort shift: B +0.64, A +0.43, D +0.28, C +0.14, so B is correct and the key stands.

**Disagreements:** none. All calculations (MCQ027, 028, 037, 038, 039, 040, 041, 042) re-derived and match the key.

**FRQ audit:** Points sum to 10 in all four. Arithmetic verified: FRQ2 RNI 2.9%, doubling 24 y; FRQ3 growth 1.9%, RNI 1.6%, doubling 37 y, 10 million, demand 1,003,750 t, shortfall 153,750 t (about 15%), 2.4x production; FRQ4 94% and 52%. Fix made: FRQ4 (a) solution overstated "live up to 14 years" and listed a within-Species-Y point that is not a between-species difference; reworded to compare the species.

**Figures:** all exist, no clipping or overlap, consistent with stems and keys (curve numbering, K=600 with S at 300, stage letters W-Z).

**Distractor rebalancing (4 questions, 8 option edits):** MCQ020 (A, C), MCQ022 (A, B), MCQ032 (A, D), MCQ043 (A, B) lengthened or made more specific so the key is no longer conspicuously the longest. Answer letters unchanged.

**Unresolved / notes:** MCQ036 premise (TFR 5.8 to 2.1 in 15 years, still +1.8%/yr) is aggressive but not scientifically wrong; left as is.


---
### verify_U4.md
# Verification report — Unit 4 (QB-U4)

**Items checked:** 44 MCQ, 4 FRQ; 48 solution blocks (one per question, no duplicates or missing IDs); 13 figure PNGs viewed.

**Blind-solve agreement:** 44/44 (100%) with the keyed answers. Key letters are balanced 11/11/11/11. No MCQ was flagged as ambiguous, factually wrong, or contradicted by its figure (orbit figure, plate map, texture triangle, watershed, rain-shadow, and day-length figure all consistent with keyed answers).

**Disagreements:** none.

**FRQ audit:** all four sum to 10 points; all arithmetic re-derived and correct (FRQ2: 2.55 / 9.03 / 71.8%; FRQ3: 7.92×10⁷ m³, 2.5 m³/s, 1.19×10⁴ t, 0.17 mm, 3.4×; FRQ4: 1,730 / 310 mm, 82%).
- Fixed: FRQ002 solution (e) cited La Niña rainfall as "40–110 mm"; the La Niña years (5, 6, 11) have 70, 40, 60 mm, so corrected to "40–70 mm".

**Distractor rebalancing (4 questions, wording only; keys unchanged):** MCQ011, MCQ012, MCQ031, MCQ032 — correct option was conspicuously longest; shortened the key and/or lengthened distractors.

**Figures:** all referenced files exist, none clipped or overlapping. Minor note: in the FRQ004 climatogram the Harbor panel has no temperature axis of its own (it shares the right-hand axis of the Plain panel); the data table supplies the values, so left as is.

**Unresolved:** none.


---
### verify_U5.md
# Verification report: Unit 5 (Book 2 U5 / Book 3 QB_U5_sol)

**Items checked:** 44 MCQ, 4 FRQ, 9 figure PNGs (all referenced files exist and were viewed).

**Blind agreement:** 44/44 MCQ (100%). Key letters are balanced at 11 each (A/B/C/D). Calculations independently recomputed (MCQ015, 020, 029, 031, 037, 038, 040 and all FRQ numbers) and all match the key.

**Disagreements:** none. Spot-checked MCQ021 (flood about 20%, furrow about 1/3) against the CED; consistent.

**FRQ audit:** points sum to 10 in all four; arithmetic, units and significant figures correct. Fixes:
- FRQ001(c)(iii) solution listed "grazing period length" as a control although the grazing schedule is the independent variable; replaced, and "stocking density 2 cattle/ha" changed to total cattle-days per hectare (rotational paddocks hold 6 cattle/ha while occupied).
- FRQ001(f) solution assumed creek sampling "downstream of rotational paddocks"; reworded to runoff entering the creek or sediment collectors at each paddock edge.

**Figure problems:** QB_U5_paddocks.png had the creek bordering only the R paddocks (a confound for the creek measurement in part f) and the R-note overlapped paddock borders. Regenerated via figs/QB_U5_make.py with the creek between the C and R rows and the note moved below; rechecked visually. Other figures are clean (no clipping or overlap) and consistent with their stems.

**Distractor rebalancing (4 edits):** MCQ007, 010, 039, 043 (correct option had been conspicuously longest or the only non-"Only" option; distractors lengthened or made parallel; MCQ043 option B trimmed). No answers or letters changed.

**Unresolved:** none. Minor note: MCQ035 and MCQ014 correct options are somewhat longer than others but all options are of similar length, left as is.


---
### verify_U6.md
# Verification report — U6 (QB-U6)

Items checked: 44 MCQ, 4 FRQ, 9 figures (all PNGs viewed; none clipped or overlapping; all referenced files exist). 48 solution blocks, one per question ID, no duplicates.

Blind solve: 44/44 agreement with key (100%). No ambiguity, scientific error, or figure/stem conflict found. Key letters balanced 11/11/11/11.

Disagreements: none.

FRQ audit: all point totals = 10 (FRQ1 1+1+2+2+1+2+1; FRQ2 2+2+1+2+2+1; FRQ3 2+1+2+2+2+1; FRQ4 2+2+2+1+1+1+1). Arithmetic re-derived: FRQ2 table totals sum correctly (107/106/108), 44.4% and 60.4% correct; FRQ3 438,000 kWh, 97.3%, $52,560, 12.0 y, 175 t correct; FRQ4 7.884×10⁶ MWh, 2,030 MW, 3.2 °C, 7.49×10⁶ t, 116 y correct. No FRQ errors.

Distractor rebalancing (7 wording edits in U6.md, no letter changes): MCQ019 B lengthened; MCQ026 A lengthened, D shortened; MCQ039 A lengthened, D shortened; MCQ040 D shortened; MCQ041 C shortened. Solutions remain valid.

Unresolved: none. Note: PE1_U6/PE3_u6 figures in figs/ were not part of this file and not checked.


---
### verify_U7.md
# Verification — U7 (Atmospheric Pollution)

Items checked: 34 MCQ, 4 FRQ, 9 figures (all viewed; no clipping or overlap; all referenced files exist; one solution block per ID).

Blind agreement: 34/34 MCQ (100%). No disagreements; no ambiguous, wrong, or data-missing items found. Letter distribution of keys is balanced (A 9, B 8, C 8, D 9).

FRQ audit: all four sum to 10 points; arithmetic re-derived (FRQ2 72.5%; FRQ3 3.0×10⁴ t S, 6.0×10⁴ t SO₂, 3.0×10³ t emitted, ≈$842 → $840/t; FRQ4 means 79 and 16.75 µg/m³, inversion classification matches the data). Figure 8 and Figure 9 match their tables. No errors.

Edits (distractor balance): 007 (A), 016 (A), 017 (D, also solution), 020 (B), 025 (D), 031 (B), 033 (B and D). Solution wording tweaks: MCQ017, MCQ019 (weak explanation of option A), MCQ016. Correct answers and letters unchanged.

Unresolved: none.


---
### verify_U8.md
# Verification — U8 (Book 2 questions / Book 3 solutions)

Items checked: 34 MCQ, 4 FRQ, 10 figure PNGs (all viewed; none clipped or overlapping; all referenced files exist).

Blind agreement: 34/34 MCQ matched the key; no ambiguity, scientific errors or figure/stem conflicts found. Answer letters balanced (A 9, B 9, C 8, D 8).

Disagreements: none.

FRQ audit: points sum to 10 in all four; all arithmetic re-derived and correct (FRQ2b 45x; FRQ3 164,250 t, 108,405 t, 180,675 m3, 22.1 y, 136,875 m3/y, 29.2 y; FRQ4 LD50 N about 0.17, M about 0.45 ug/bee, 28,800 bees). Each solution answers every part. No errors found.

Structure: every question has exactly one matching solution block.

Distractor rebalancing (wording only, answers unchanged): MCQ012, 019, 027, 028, 029, 030, 032 (correct option shortened and/or distractors lengthened).

Figure problems: none.
Unresolved: none.


---
### verify_U9.md
# Verification report — U9 (QB-U9)

Items checked: 56 MCQ, 6 FRQ, 11 figures (all PNGs viewed), 62 solution blocks (one per question ID, no duplicates). Key letters balanced 14/14/14/14.

## Blind-solve agreement
Blind answers matched the key on 56/56 MCQ (100%). Two items were flagged for issues (below).

## Disagreements / issues
- QB-U9-MCQ033: key (C, 34%) is right, but the stem could be read as percentage points (B, 31%). Fix: stem now says "percent ... relative to its value at pH 8.10".
- QB-U9-MCQ029: key D right, but "newly flooded continental shelves" is scientifically loose (shelves are already submerged). Fix: option D and its solution now say "newly flooded low-lying coastal land".

## FRQ audit
All six FRQs: arithmetic re-derived and correct (FRQ3: 26.5%, -6.25 DU/yr; FRQ4: -38%, -1.2 million km²/decade, ~2052; FRQ5: 88,000 kg; 3,524 t CO2e; 69.9%; 492.8 t; 14.0%; $24,640; 14.2 yr; FRQ6: 0.30/0.75 m, 16,800/52,800 people, 36,000 more, $252 M, ~$4,770/person). Points sum to 10 in each; solutions answer every part. No errors found.

## Figure problems
- QB_U9_bleaching.png: the title and caption said "twelve reefs" but 13 points are plotted (12 trend points + Reef K). Fixed title (script QB_U9_make.py rerun) and caption to "thirteen".
- All other figures: no clipping or overlap, consistent with the stems.

## Distractor rebalancing (3 edits)
- MCQ054: lengthened options A, B, C so the correct D is no longer conspicuously longest.
- MCQ050: removed the lone hedge ("could") from correct option B.

## Unresolved
None.
