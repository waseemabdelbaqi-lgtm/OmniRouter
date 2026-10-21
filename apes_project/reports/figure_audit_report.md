# Scientific figure audit report

Every Book Two question figure (162) was inspected for scientific accuracy, labels, units, scales, arrows, legends, contrast, resolution and agreement with its question; defects were fixed or the figure was redrawn. New and reused Book One figures were viewed and corrected by the chapter authors (e.g. greenhouse-effect arrow direction, succession curves, plate-boundary label overlaps).


---
### figures_A.md
# Figure audit A (QB_U1_, QB_U2_, QB_U3_; 27 figures)
Scripts: content/book2/figs/QB_U1_make.py, QB_U2_make.py, QB_U3_make.py (all PNGs regenerated at 220 dpi, data unchanged)

QB_U1_climate_station.png | fixed | added x-axis title "Month"; left axis label/ticks coloured blue (bars) and right axis red (line) so axes match series. Savanna climate and data consistent with key B.
QB_U1_carbon_fluxes.png | redrawn | labels A-E were crowded and D sat against the E arrow; rebuilt with separated arrows and boxed labels, widened atmosphere box, removed bottom clipping. Values 120/118/92/90/10 and net +6 Gt C/yr unchanged.
QB_U1_nitrogen_cycle.png | fixed | bottom box was clipped at the image edge; fixed canvas, labelled the unlabeled plants-to-dead-matter arrow ("death, waste"). P/Q/R/S/T processes verified (fixation, nitrification, assimilation, ammonification, denitrification).
QB_U1_grass_web.png | OK | arrow directions (food to eater) and trophic structure match MCQ021/022 and key.
QB_U1_energy_levels.png | redrawn | white text on orange had poor contrast, top bar text nearly touched box edges; darker orange, wider bars, title reworded. Values 20,000/1,800/160/12 unchanged (9.0%, 8.9%, 7.5%).
QB_U1_co2_station.png | fixed | y ticks changed from 410.0, 412.5 ... to whole numbers every 5 ppm. Trend (2.4 ppm/yr) and spring-peak/autumn-low seasonality match key C.
QB_U1_frq1_lake.png | redrawn | dangling unlabeled outlet arrow, farm box clipped at left edge, empty space; clean layout with labelled inlet and outlet. Nitrate 0.90 mg/L and TP 0.008 mg/L unchanged.
QB_U1_frq2_forest.png | fixed | legend collided with the GPP line; moved to clear area, added x title "Month", thousands separators, y title "Energy (kcal/m² per month)". Totals 7,990/3,990/4,000 and 49.9% verified against solution.
QB_U1_frq4_reef.png | fixed | y ticks made whole numbers (fish axis showed 2.5, 7.5 ...). Values 14/2, 3/22, 82/9 match table and solution.
QB_U2_island_model.png | OK | equilibria 40 (large near), 24, 30, 15 (small far) all read at gridline crossings; key A (25) correct.
QB_U2_tolerance.png | OK | ranges P 16-26, Q 6-34, R 24-38 agree with solution.
QB_U2_shell.png | fixed | legend text overlapped the blue curve; raised y-limit so legend sits clear.
QB_U2_fragments.png | fixed | squares now drawn as four equal patches inside a landscape matched to the "After" panel, title no longer cramped, added "Schematic, not to scale" and colour key (tan = roads and fields). 
QB_U2_stream.png | fixed | axis titles/ticks colour-matched to bars (blue) and line (red). Data match solution (80-85 to 6; DO 8.8 to 4.1).
QB_U2_pools.png | fixed | egg-mass series shown as markers only (a connecting line implied a continuous scale on an unevenly spaced category axis); axis colours matched to series. Data unchanged.
QB_U2_succession.png | fixed | right-panel y title now states the scaling (NPP x 10), x-limit padded so first points are not on the axis, legend shortened. Data unchanged.
QB_U2_islands.png | OK | matches table (A-H) and key; log x scale labelled; legend ranges match table.
QB_U3_surv.png | OK | Type III / Type I / Type II shapes correct on log axis; Curve 3 straight line = constant mortality; matches keys to MCQ017/018.
QB_U3_logistic.png | OK | K = 600; S at K/2 (300) is steepest, matches key D.
QB_U3_deer.png | OK | peak 480 in year 8, browse minimum year 9; consistent with key B.
QB_U3_yeast.png | OK | plateaus 20/45/90 proportional to glucose, same early growth; key C.
QB_U3_pyramids.png | OK | A stable column, B constrictive, C expanding, D flat base; text readable; keys C (MCQ023) and B (MCQ024) hold (solution wording corrected, see below).
QB_U3_dtm.png | OK | stages W-Z ordered correctly (both high; death falls; birth falls; both low); key A (X).
QB_U3_tfr.png | OK | ten points match keys (90%/96% have 1.8/1.5; TFR 4.6 at 41%).
QB_U3_frq1.png | OK | goats 110 to 430 (2015) to 310, forage 900 to 375; matches solution.
QB_U3_frq2.png | OK | 44/42/30/19 and 24/13/8/7 match table.
QB_U3_frq4.png | fixed | added note that Species Y has no survivors at age 10 or later (line ended with no explanation on the log axis). Data unchanged.

## Question / solution edits
1. content/book2/U1.md, QB-U1-MCQ014 stem: "among three reservoirs" changed to "between the atmosphere and other reservoirs" (the figure shows four boxes: atmosphere, land, ocean, fossil fuel deposits). Answer unchanged (+6 Gt C/yr).
2. content/book3/QB_U3_sol.md, QB-U3-MCQ023 solution: sentence about Country D said its younger groups are "much smaller relative to its middle-aged groups", which is wrong for the figure (D has a flat base, youngest groups are the largest). Now says D has a flat base so births are not rising cohort to cohort, hence slower growth than C. Answer C unchanged.


---
### figures_B.md
# Figure audit TAG=B (QB_U4_*, QB_U5_*)

All 22 PNGs are 220 dpi; data, filenames and keyed answers unchanged.

QB_U4_plates_map.png | fixed | Boundary III marker overlapped arrows and plate edge: arrows moved, marker repositioned; legend now says I, II, III = plate boundaries (3 lines, no overlap with Plate S). Boundary types (I divergent, II convergent, III transform) agree with MCQ014 key.
QB_U4_benioff.png | fixed | Depth axis now runs 0 (surface) to 250 km instead of an unlabeled partial range; same points.
QB_U4_soil_profile.png | fixed | Horizon letter W was clipped by the thin 6-cm layer (font reduced); rock-fragment symbols no longer overprint label Z. Values match MCQ016 solution (Y: 36% clay, 1.2% OM).
QB_U4_texture_triangle.png | OK | Axes, tick directions and the four plotted points (1: 10/10/80 clay/silt/sand, 2: 20/40/40, 3: 60/25/15, 4: 15/65/20) verified against the table.
QB_U4_atm_profile.png | OK | Layer boundaries (12, 50, 86 km) and temperatures realistic; W-Z labels consistent with key B.
QB_U4_circulation.png | OK | Hadley/Ferrel/Polar cell directions correct; rising at W and Y, sinking at X (30 degrees), consistent with MCQ023.
QB_U4_watershed.png | fixed | Site markers were stretched ovals (now round); flow arrowheads were tiny (enlarged, more arrows); fertilizer arrow now reaches the stream between Sites 2 and 3. Key A (Sites 3 and 4) still correct.
QB_U4_orbit.png | fixed | Equal aspect ratio so Earths and Sun are round and axis tilt is true 23.5 degrees. Geometry checked: Z = N pole tilted toward Sun (June solstice), key D correct; orbit direction counterclockwise.
QB_U4_daylength.png | OK | Day-length curves for 3 N, 40 N, 45 S computed from solar declination; agree with MCQ032 key B.
QB_U4_rainshadow.png | fixed | Station W was plotted at about 13 m elevation; moved to the coast (x = 15 km) so all four stations match the table (20, 1,570, 2,500, 590 m).
QB_U4_frq1_hillside.png | fixed | Removed unlabeled dotted lines that ran through block text. Slopes/soils agree with FRQ001 solution (Blocks 1 and 2 matched).
QB_U4_enso_series.png | fixed | Top panel now has its own year labels and axis title; landings axis uses whole-number ticks. Data identical to the table and FRQ002 solution.
QB_U4_climatograms.png | redrawn | Harbor's temperature line had no axis (readable only against the precipitation axis); each panel now has its own labeled temperature axis, month axis title, and a legend. Totals 1,730 and 310 mm agree with FRQ004 solution.
QB_U5_salinization.png | fixed | White salt crust was invisible against white background: added tinted sky, outlined crust with crystals. Labels W, X, Z agree with MCQ019 key D.
QB_U5_resistance.png | OK | Legend, axes (0-105%) and values (A 92% at season 5, B 24%, 70% at season 8) agree with MCQ022 solution.
QB_U5_fishery.png | fixed | y-axis baseline was below zero with no 0 tick; now starts at 0. Values agree with MCQ025 solution (900 to 330 thousand t, 1960-85).
QB_U5_hydrograph.png | OK | Y peaks earlier (2.8 h) and higher (48 vs 13.5 m3/s) than X; baseflow, axes and units correct; matches key B.
QB_U5_footprint.png | OK | Values and deficit/surplus pattern agree with MCQ028 solution.
QB_U5_erosion_plots.png | fixed | Added note "Error bars: range among replicates" (stem describes them). Values 18.0/11.7/9.0/4.5 give 35%, 50%, 75% reductions as in key D.
QB_U5_surplus.png | OK | Logistic growth, max 125 t/yr at 500 t, growth 120 at 600 t, harvest-100 intersections at about 276 and 724 t; agrees with MCQ042 key B.
QB_U5_paddocks.png | fixed | "Creek" label sat in a white box that cut the creek; label moved above the creek. Layout and numbers agree with FRQ001 stem.
QB_U5_aquifer.png | OK | Dual-axis chart (colored axis titles, legend clear of data); values match the FRQ002 table and solution rates.

## Question/solution edits
None. No inconsistency between figures, stems, keys or solution numbers was found.


---
### figures_C.md
# Figure audit C (QB_U6_*, QB_U7_*)

All 18 PNGs are 220 dpi. Data checked against stems, keyed answers and solution numbers: all consistent. Script-wide change: every in-figure text size below 9.5 pt raised to 9.5 pt so text stays at or above 8 pt at print width.

QB_U6_mix.png | fixed | Segments of 2-3% (gas, nuclear, wind and solar, biomass) were unlabeled so the fossil-fuel sums in the solution could not be checked. Now labeled above the bar. Bars slimmer, orange segments use black text for contrast, text enlarged.
QB_U6_coal_flow.png | fixed | Boxes widened and text enlarged to 9.5 pt. Numbers (35+10+3+52=100) are correct.
QB_U6_reserves.png | fixed | Text sizes only. Data matches the solution (48 vs 9, 8 vs 31, 11 vs 21).
QB_U6_pwr.png | redrawn | Cleaner layout in the same style. The river intake and discharge arrows were tangled, circle 3 overlapped the steam-generator corner, and labels were tiny. Locations 1-4 keep the same meaning: 1 reactor water, 2 steam, 3 condensate, 4 river discharge. Answer D is unchanged.
QB_U6_decay.png | OK | Half-life 30 y, 12.5% at 90 y. Axes and units correct.
QB_U6_solar_day.png | OK | Peak demand 3.2 kW near 19:30 with PV at zero, as the solution says.
QB_U6_wind_curve.png | OK | 0.25 MW at 5 m/s, 2.0 MW at 10 m/s, rated 3.5 MW, cut-in 3 m/s, cut-out 25 m/s.
QB_U6_eroi.png | OK | 1.8 for corn ethanol matches the solution. Axis title and units are correct.
QB_U6_frack.png | fixed | Caption now says depths and horizontal spacing are not to scale (M1, M2 and M3 are drawn evenly spaced but are 0.3, 1.2 and 4 km from the pad). The "Freshwater aquifer" label was touching M1 and was moved. Text enlarged.
QB_U7_diurnal.png | OK | NO peaks about 7:30 am, O3 about 2 pm, as the solution says.
QB_U7_inversion.png | OK | Day 2: 6 °C at ground, 12 °C at 300 m, an inversion. Day 1 falls with height.
QB_U7_plant.png | fixed | The "flue gas" label overlapped the boiler and the arrow. Replaced by a note "Arrows show the path of the flue gas". Text enlarged.
QB_U7_noise.png | OK | 95, 105 and 110 dB are above 85 dB and traffic (80) is below, as keyed.
QB_U7_ozone_sites.png | fixed | The legend touched the suburb curve. Y-axis extended to 120 ppb with ticks every 20. Peaks at 1, 3 and 5 pm match the solution.
QB_U7_trends.png | OK | CO2 100 to 116 matches the solution. Index axis and legend correct.
QB_U7_school_plan.png | fixed | Rooms were off-center and nearly touched the wing edge. Re-centered. The Wing B caption now wraps and the ventilation note is moved down.
QB_U7_lakes.png | fixed | X ticks changed to 1990, 2000, 2010, 2020 to match the data table. Legend moved to the empty top of the pH panel. Data matches the table.
QB_U7_pm_days.png | OK | All values and inversion days match the table (means 79 and 16.8).

Question/solution edits: none.


---
### figures_D.md
# Figure audit D (QB_U8_, QB_U9_) — 21 figures; all 220 dpi

QB_U8_biomag.png | OK | log scale, legend, Y ~10x per level matches solution
QB_U8_bloom.png | OK | values match solution (July 85 ug/L, Sep DO 1.2)
QB_U8_doseresp.png | OK | LD50 ~20 and ~80 mg/kg match solutions; log axis labelled
QB_U8_frq1_map.png | fixed | S3 no longer straddles pond edge-label crowding; S4 moved off the outlet arrow; Inlet labels moved next to their sites and enlarged to 9 pt
QB_U8_frq2_hg.png | fixed | log-axis ticks now plain 0.01 / 0.1 / 1 instead of 10^-2 etc. (same data)
QB_U8_frq4_dose.png | OK | matches table and LD50 estimates
QB_U8_landfill.png | OK | component 3 = leachate collection layer, 2 = gas vent, 4 = liner, 1 = cap; consistent with key
QB_U8_sag.png | OK | minimum 3.0 mg/L at ~13 km, matches stem
QB_U8_sewage.png | fixed | arrows now start/end at box edges (previously overlapped boxes); stray arrowhead after S replaced by an arrow down to "Treated water to river"
QB_U8_thermal.png | OK | 10.1 -> 8.3 mg/L gives 17.8% (key B)
QB_U9_albedo_loop.png | fixed | arrows now touch box edges, consistent gaps; loop direction unchanged
QB_U9_bleaching.png | OK | 13 reefs; Reef K outlier; consistent with MCQ030 key
QB_U9_coral_ph.png | fixed | removed odd y tick at 110; ticks 30-100 only (data unchanged; 91 -> 60 = 34%)
QB_U9_fragments.png | fixed | made both patch labels the same size (data/geometry unchanged; 50% key holds)
QB_U9_hatchery.png | OK | matches solution values (7.85 pH, 46%; 8.05, 82%)
QB_U9_icecore.png | fixed | temperature axis was "difference from present" but read +1.5 at present; rescaled so present = 0 (same curve shape, same CO2 data); added zero line; 2023 label no longer touches the dashed line
QB_U9_invasive.png | OK | levels near 1,500 and 300 as in solution
QB_U9_keeling.png | OK | seasonal peak in May, trend ~2.4 ppm/yr
QB_U9_o3_antarctic.png | OK | Oct 2000 minimum 120 DU, 1980 minimum 260 DU
QB_U9_seaice_cubs.png | OK | matches FRQ004 table
QB_U9_transect.png | fixed | the two-piece distance arrow merged into a single continuous arrow

## Question/solution edits
None. (Icecore temperature rescale does not affect any quoted number; solution cites only CO2 ~280 ppm peaks and 420 ppm.)


---
### figures_E.md
# Figure audit E (PE1_ and PE2_ figures, 35 files)

All PNGs are 220 dpi; text is at least 8 pt equivalent. Data are unchanged in every figure. Regeneration reproduced the unchanged PNGs pixel-identically (rng seeds untouched).

## PE1 (make_PE1.py)
PE1_U1_estuary_web.png | OK | Arrows run from eaten to eater; trophic levels agree with key (heron secondary and tertiary).
PE1_U2_island_biogeog.png | OK | Log area axis labeled; legend matches series; near > far at every area.
PE1_U3_survivorship.png | OK | Log y axis labeled; Curve 1 = Type III, 2 = Type I, 3 = Type II as in key.
PE1_U3_agestructure.png | OK | Each pyramid sums to 100%; sexes stated in axis title; shapes match key.
PE1_U4_enso.png | OK | Shading thresholds match caption; 2021-22 deepest negative, 2017-18 weakly negative as in solution.
PE1_U4_hydrograph.png | OK | Peaks 18 vs 52 m3/s, at 9.5 h vs 5 h, as quoted in solution.
PE1_U5_fishery.png | OK | Zero baselines; catch/effort 48/32 = 1.5 and 20/66 = 0.3 as in solution.
PE1_U6_grid_mix.png | OK | 2024 total = 1,000 GWh (wind 200, solar 300, diesel 380); legend clear of bars.
PE1_U6_insolation.png | OK | Both site means = 5.0; Site 2 above Site 1 only Apr-Sep; Dec 2.4 vs 4.0 as in solution.
PE1_U7_diurnal.png | fixed | y axis started at about 5 ppb; now starts at 0.
PE1_U7_inversion.png | fixed | 0 m data marker was half-clipped by the axis; now fully drawn.
PE1_U8_do_sag.png | OK | Minimum 3.0 mg/L at 25 km; 5 mg/L line labeled.
PE1_U8_dose_response.png | OK | LD50 10 vs 100 mg/kg on log dose axis, as in key.
PE1_U9_sea_ice.png | fixed | y axis truncated at 2 (exaggerated a percent-change question); now starts at 0. 7.8 and 3.9 labeled.
PE1_U9_ph.png | OK | pH 8.12 to 8.04 and pCO2 346 to 422 agree with stem; truncated axes acceptable for tiny pH range and values are in the stem.
PE1_FRQ1_estuary.png | redrawn | Cramped layout: H2 label collided with the marsh outline, notes crossed the farmland edge, and the ditches mentioned in the text were not drawn. Redrew with larger marsh, dashed ditch arrows, clear labels, and note moved below the frame. Same four sampling points.
PE1_FRQ2_arctic.png | fixed | Both y axes truncated; now start at 0. Values match the table.

## PE2 (make_PE2.py)
PE2_foodweb.png | OK | Arrow direction stated; links match key.
PE2_speciesarea.png | OK | 16 points; fitted line gives 38 / about 45 / 52 species at 100 / 300 / 1,000 ha, as in solution.
PE2_tolerance.png | OK | At 30 C: A = 0, B about 0.83, C = 1.0 as in solution.
PE2_survivorship.png | OK | X = Type I, Y = Type II, Z = Type III; axes labeled.
PE2_agestructure.png | OK | Each pyramid sums to 100%; legend present.
PE2_dtm.png | OK | M falls in Stage 3 with a positive birth-death gap.
PE2_elnino.png | OK | Large positive anomalies coincide with low landings; axes and units labeled.
PE2_energymix.png | OK | Each country sums to 100%; X is 80% hydro.
PE2_smog.png | OK | NO peaks, then NO2, then O3 in the afternoon.
PE2_do.png | redrawn | BOD was plotted as "BOD / 2.5" on a mg/L axis, which is misleading. Now BOD is plotted at true values on its own right axis (0-25 mg/L), DO on the left (0-10 mg/L). Same data.
PE2_doseresponse.png | OK | LD50 Q = 8 and P = 40 mg/kg, as in solution.
PE2_co2.png | OK | Annual cycle peaks in May; trend about 2.4 ppm/yr; the truncated y axis is standard for CO2.
PE2_coral.png | OK | Bleaching above 35% occurs only in years with SST above 30.5 C; matches solution.
PE2_forestloss.png | OK | Values labeled; losses are 30%, 20% and 10% as in solution.
PE2_frq1_fragment.png | OK | Edge and distance scale are clear; no answer given away.
PE2_frq2_monthly.png | OK | Monthly PM2.5 averages to about 92, equal to the 2024 table value; Dec and Jan highest.
PE2_hydrograph.png | OK | Watershed X peak is higher and earlier than Y.
PE2_overfish.png | fixed | Right-axis label crowded the neighboring panel; spacing increased. Catch per boat is 0.58 (2000) to 0.11 (2020) as in solution.

## Question and solution edits
None. No question, key or solution text was changed.


---
### figures_F.md
# Figure audit F (PE3_* and PE4_*; scripts make_PE3.py, make_pe4.py)

All 39 PNGs are 220 dpi. Every figure was checked against its stem, key and solution numbers. Both scripts were re-run, so unchanged figures were re-rendered from unchanged code.

## PE3
PE3_u1_climate.png | fixed | month letters and axes enlarged (7 pt to 8.5-9 pt); stray right spines removed on P and Q; precipitation axis label coloured to match the bars. Data unchanged (Site Q about 900 mm, dry Jun-Sep, matches key).
PE3_u2_tolerance.png | fixed | drought-line label enlarged and darkened. Data unchanged.
PE3_u3_survivorship.png | OK | log axis, curves A/B/C match keyed Type III/I/II.
PE3_u3_overshoot.png | fixed | Smoothing had flattened the peak to about 2,680, but option A quotes about 2,800. Now interpolated through the stated points (peak 2,800, plateau 1,400); thousands separators added.
PE3_u3_agestructure.png | fixed | tick, label and Male/Female text enlarged (7 pt to 8.5-9 pt). Data unchanged (each country sums to 100%).
PE3_u3_transition.png | OK | gaps 25 (1960), 23 (1980), 2 (1900), 8 (2020) match the solution.
PE3_u4_soils.png | OK | values 120/6/28 mm/h and 9/42/28% match the solution.
PE3_u4_rainshadow.png | fixed | empty headroom trimmed; site and wind labels enlarged; wind arrow moved up so it no longer collides with the "Site 1" label.
PE3_u4_enso.png | fixed | no legend for the bars and line; added legend (warm anomaly, cool anomaly, catch on right axis). Data unchanged.
PE3_u5_overfishing.png | fixed | 7 pt rotated ticks enlarged to 8.5 pt; panel titles added; axis label sizes raised. Catch per boat-day of 200 to 70 kg and effort tripling confirmed.
PE3_u6_mix.png | fixed | legend and segment numbers enlarged. Shares sum to 100% for every country; Country Z gives 0.38 kg/kWh.
PE3_u7_pm.png | fixed | guideline label and tick labels enlarged. 480/190/30 and the 94% reduction confirmed.
PE3_u7_smog.png | OK | NO and NO2 peak in the morning rush; O3 peaks about 14:00.
PE3_u8_dosag.png | fixed | outfall label enlarged and darkened. Minimum 2.5 mg/L at 12 km matches the solution.
PE3_u8_doseresponse.png | fixed | log-axis ticks changed from 10^n to 1, 10, 100, 1,000 (consistent with the other figures). LD50 values 20 and 200 mg/kg confirmed.
PE3_u9_co2.png | OK | seasonal peak in May, trend 2.4 ppm/yr, 2010-2020.
PE3_u9_invasive.png | fixed | x ticks (2006, 2008, ...) did not match the survey years; now 2005, 2008, ... 2020; thousands separators added. Increments 70 to 440 ha confirmed.
PE3_frq1_survey.png | fixed | panel title sizes made consistent. Values 9.1/7.4/4.8 confirmed.
PE3_frq2_tfr.png | fixed | replacement-level label enlarged. Country C 6.0 to 1.9, B 1.3, A 5.1 confirmed.

## PE4
PE4_01_pyramid.png | OK | question marks hide the keyed values; 60,000 and 600 shown.
PE4_02_island.png | OK | about 45 and 30 species at 100 km2, as in the solution.
PE4_03_tolerance.png | OK | X limit 30 C, Y limit 36 C and about 62% growth at 31 C match the solution.
PE4_04_survivorship.png | fixed | Curve A had a kink at 80% and a vertical cliff to zero at 100%; replaced with a smooth Type I curve. Type A/B/C/D classification unchanged.
PE4_05_overshoot.png | fixed | thousands separators added (peak 5,600 in 1964 unchanged).
PE4_06_age.png | fixed | bars summed to 110%, 96% and 102% of the population; rescaled so each country totals 100%. Shapes are unchanged and the key stays valid. Fonts enlarged (7 pt to 8.5-9 pt).
PE4_07_demographic.png | fixed | the stem says 2040 is projected but the figure did not show it; the 2010-2040 segment is now dashed and labelled. 1970 values (38 and 14) confirmed.
PE4_08_atmosphere.png | OK | W/X/Y/Z layer boundaries and temperature profile are correct.
PE4_09_enso.png | OK | P is about +2.3 C (El Nino), Q is about -1.6 C (La Nina).
PE4_10_irrigation.png | OK | 50/60/75/90% match the solution.
PE4_11_emissions.png | fixed | Wind bar was pale blue (low contrast), now teal; thousands separators added. Values unchanged.
PE4_12_biofuel.png | fixed | legend order now matches the stacking order; label enlarged. Inputs 18.0 and 10.0 MJ confirmed.
PE4_13_smog.png | OK | NO and NO2 peak in the morning, O3 peaks at about 14:30.
PE4_14_dose.png | OK | LD50 about 8 and 120 mg/kg, ratio 15.
PE4_15_co2.png | fixed | odd 2.5 ppm tick steps changed to 5 ppm.
PE4_16_icecore.png | redrawn | "Temperature change from today" did not reach 0 at the present, and CO2 was clipped flat at 180 ppm. Redrawn so today = 0 C, interglacials about 0 to +0.7 C, glacials about -8 C; CO2 180-290 ppm without clipping; annotation no longer overlaps its leader line. Present point (425 ppm) and key unchanged.
PE4_17_ph.png | fixed | endpoint markers added to the 1990 (8.11) and 2020 (8.05) pH labels; annotation enlarged.
PE4_18_ozone.png | fixed | the 220 DU line was unexplained; now labelled "ozone-hole threshold". Labels enlarged. About 100 DU in 1999 and about 127 DU in 2023 match the solution.
PE4_FRQ1_canal.png | fixed | "Return-flow drain" relabelled "Return-flow canal" to match the stem; arrow labels were sitting on the arrows and are now offset; text enlarged.
PE4_FRQ2_arctic.png | fixed | x tick labels enlarged (7 pt to 8 pt). Table values confirmed.

## Question/solution edits
None. The only data changes are the PE4_06 age-structure rescale, the PE3_u3_overshoot peak and the PE4_16 ice-core redraw. None of them is quoted numerically in a question or solution, and every keyed answer still holds. The PE4_04 curve A rewrite and the PE4_07 projection dashes are also unchanged in meaning.
