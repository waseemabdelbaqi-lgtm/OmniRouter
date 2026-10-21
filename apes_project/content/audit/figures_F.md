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
