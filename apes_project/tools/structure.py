"""Academy 7-unit / 11-chapter structure and the cross-reference to the 2026 College Board (CED) topics."""
UNITS = {
 1: ("UNIT I", "EARTH SYSTEMS AND RESOURCES", [1, 2, 3]),
 2: ("UNIT II", "THE LIVING WORLD", [4, 5]),
 3: ("UNIT III", "POPULATION", [6]),
 4: ("UNIT IV", "LAND AND WATER USE", [7]),
 5: ("UNIT V", "ENERGY RESOURCES AND CONSUMPTION", [8]),
 6: ("UNIT VI", "POLLUTION", [9, 10]),
 7: ("UNIT VII", "GLOBAL CHANGE", [11]),
}
CHAPTERS = {
 1: ("The Earth", ["Geologic Time Scale", "Earth's Structure", "Plate Tectonics", "Earthquakes", "Tsunamis", "Volcanoes", "Solar Intensity, Seasons, and Latitude–Longitude", "Soil", "The Rock Cycle", "Practice Questions and Answers"]),
 2: ("The Atmosphere", ["Composition", "Structure", "Weather and Climate", "Atmospheric Circulation—Pressure", "Hurricanes, Tornadoes, and Cyclones", "El Niño—Southern Oscillation (ENSO)", "Practice Questions and Answers"]),
 3: ("Global Water Resources and Use", ["Water Distribution and Properties", "Freshwater", "Aquifers", "Types of Ice", "Oceans", "Agricultural, Industrial, and Municipal Use", "Global Problems", "Practice Questions and Answers"]),
 4: ("Ecosystems", ["Ecology", "Law of Tolerance", "Energy Flow", "Biomes", "Biodiversity", "Practice Questions and Answers"]),
 5: ("Natural Biogeochemical Cycles", ["Carbon Cycle", "Nitrogen Cycle", "Phosphorus Cycle", "Sulfur Cycle", "Water Cycle", "Role of H₂O, C, N, P, and S in the Human Body", "Practice Questions and Answers"]),
 6: ("Populations", ["Population Ecology", "Survivorship", "Human Population Dynamics", "Demographic Transition", "Age-Structure Diagrams", "Population Size", "Impacts of Population Growth", "Practice Questions and Answers"]),
 7: ("Land and Water Use", ["Feeding a Growing Population", "Types of Agriculture", "Agricultural Productivity", "Sustainable Agriculture", "Controlling Pests", "Forestry", "Forest Fires (Wildfires)", "Wildfire Suppression", "Deforestation—Tree Harvesting", "Rangelands", "Urban Land Development", "Transportation Infrastructure", "Public and Federal Lands", "Mining", "Global Mineral Reserves", "Fishing", "Global Economics", "Tragedy of the Commons", "Practice Questions and Answers"]),
 8: ("Energy", ["Energy Concepts", "Energy Consumption (Past)", "Energy Use (Present)", "Renewable Energy Sources", "Energy Conservation", "Transportation", "Mass Transit", "Practice Questions and Answers"]),
 9: ("Pollution", ["Air Pollution", "Major Air Pollutants", "Acid Deposition", "Thermal Pollution", "Noise Pollution", "Water Pollution", "Groundwater Pollution", "Water Quality—Water Testing", "Maintaining Water Quality—Water Purification", "Septic Systems/Sewage Treatment", "Municipal Solid Waste", "Practice Questions and Answers"]),
 10: ("Impacts on the Environment and Human Health", ["Hazards to Human Health", "Dose-Response Relationships", "Hazardous Chemicals in the Environment", "Treatment, Disposal, and Cleanup of Contaminated Sites", "Perpetual Storage", "Bioaccumulation—Biomagnification", "Environmental Economics", "Sustainability—Resiliency", "Practice Questions and Answers"]),
 11: ("Stratospheric Ozone and Global Warming", ["Stratospheric Ozone", "Ozone Depletion", "Global Warming", "Impacts and Consequences of Global Warming", "Reducing Climate Change", "Loss of Biodiversity", "Practice Questions and Answers"]),
}
def unit_of_chapter(ch):
    for u, (_, _, chs) in UNITS.items():
        if ch in chs: return u
# CED topic -> (chapter, primary section number, [other sections])
CED = {
 "1.1": (4, 1, []), "1.2": (4, 4, []), "1.3": (4, 4, [3.5]), "1.4": (5, 1, []), "1.5": (5, 2, []), "1.6": (5, 3, []), "1.7": (5, 5, []),
 "1.8": (4, 3, []), "1.9": (4, 3, []), "1.10": (4, 3, []), "1.11": (4, 3, []),
 "2.1": (4, 5, []), "2.2": (4, 5, []), "2.3": (4, 5, []), "2.4": (4, 2, []), "2.5": (4, 5, []), "2.6": (4, 5, []), "2.7": (4, 5, []),
 "3.1": (6, 1, []), "3.2": (6, 1, []), "3.3": (6, 2, []), "3.4": (6, 1, []), "3.5": (6, 6, []), "3.6": (6, 5, []), "3.7": (6, 3, []), "3.8": (6, 3, [7]), "3.9": (6, 4, []),
 "4.1": (1, 3, [2, 4, 5, 6]), "4.2": (1, 8, []), "4.3": (1, 8, []), "4.4": (2, 1, [2]), "4.5": (2, 4, []), "4.6": (3, 2, []), "4.7": (1, 7, []), "4.8": (2, 3, []), "4.9": (2, 6, []),
 "5.1": (7, 18, []), "5.2": (7, 9, []), "5.3": (7, 3, [1]), "5.4": (7, 2, [3]), "5.5": (3, 6, []), "5.6": (7, 5, []), "5.7": (7, 2, [1]), "5.8": (7, 16, []), "5.9": (7, 14, []),
 "5.10": (7, 11, []), "5.11": (6, 7, []), "5.12": (10, 8, []), "5.13": (7, 11, []), "5.14": (7, 5, []), "5.15": (7, 4, []), "5.16": (7, 16, []), "5.17": (7, 6, []),
 "6.1": (8, 1, []), "6.2": (8, 2, [3]), "6.3": (8, 3, []), "6.4": (8, 3, []), "6.5": (8, 3, []), "6.6": (8, 3, [10]), "6.7": (8, 4, []), "6.8": (8, 4, []), "6.9": (8, 4, []), "6.10": (8, 4, []), "6.11": (8, 4, []), "6.12": (8, 4, []), "6.13": (8, 5, [6, 7]),
 "7.1": (9, 1, []), "7.2": (9, 2, []), "7.3": (9, 1, []), "7.4": (9, 2, []), "7.5": (9, 2, []), "7.6": (9, 1, [2]), "7.7": (9, 3, []), "7.8": (9, 5, []),
 "8.1": (9, 6, []), "8.2": (9, 6, []), "8.3": (10, 3, []), "8.4": (9, 6, []), "8.5": (9, 6, []), "8.6": (9, 4, []), "8.7": (10, 3, []), "8.8": (10, 6, []), "8.9": (9, 11, []), "8.10": (9, 11, []), "8.11": (9, 10, []),
 "8.12": (10, 2, []), "8.13": (10, 2, []), "8.14": (10, 1, []), "8.15": (10, 1, []),
 "9.1": (11, 1, [2]), "9.2": (11, 2, []), "9.3": (11, 3, []), "9.4": (11, 3, [5]), "9.5": (11, 3, [4]), "9.6": (11, 4, []), "9.7": (11, 4, []), "9.8": (11, 6, []), "9.9": (11, 6, []), "9.10": (11, 6, []),
}
def chapter_of_topic(t): return CED[t][0]
