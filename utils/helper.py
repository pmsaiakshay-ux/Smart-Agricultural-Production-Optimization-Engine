# Agronomic guidance database for the 22 crops in the crop recommendation dataset

CROP_DETAILS = {
    'rice': {
        'fertilizer': 'NPK Ratio 120:60:40 kg/ha. Apply Urea, Single Superphosphate (SSP), and Muriate of Potash (MOP).',
        'conditions': 'Flooded soils, high temperature (20-35°C), high humidity (>80%), clayey or loamy soils, rainfall > 1500mm.',
        'tips': 'Ensure proper water level in the field during the vegetative stage. Control weeds early using mechanical weeding or selective herbicides.'
    },
    'maize': {
        'fertilizer': 'NPK Ratio 150:75:40 kg/ha. Apply DAP (Diammonium Phosphate) and Zinc Sulfate.',
        'conditions': 'Well-drained soils, pH 5.5-7.5, moderate rainfall (500-1000mm), temperature 20-30°C.',
        'tips': 'Implement crop rotation with legumes to improve soil nitrogen. Monitor for fall armyworms and stem borers.'
    },
    'chickpea': {
        'fertilizer': 'NPK Ratio 20:60:20 kg/ha. Needs lower nitrogen as it is a nitrogen-fixing legume. Use Rhizobium inoculation.',
        'conditions': 'Cool climate, dry conditions, well-aerated light-to-medium textured soils, pH 6.0-9.0.',
        'tips': 'Avoid excessive nitrogen fertilization to prevent excessive vegetative growth. Harvest when pods turn golden brown.'
    },
    'kidneybeans': {
        'fertilizer': 'NPK Ratio 40:60:40 kg/ha. Moderate nitrogen required. Apply compost and micronutrients.',
        'conditions': 'Mild climate, pH 5.5-6.5, well-drained sandy loam soil, temperature 15-25°C.',
        'tips': 'Extremely sensitive to waterlogging. Ensure effective drainage channels. Mulch to retain critical moisture.'
    },
    'pigeonpeas': {
        'fertilizer': 'NPK Ratio 25:50:25 kg/ha. Inoculate seeds with Rhizobium culture before planting.',
        'conditions': 'Deep loam soils, high tolerance to heat, pH 5.0-8.0, rainfall 600-1000mm.',
        'tips': 'Intercrop with maize or sorghum. Protect the crop from pod borers during flowering.'
    },
    'mothbeans': {
        'fertilizer': 'NPK Ratio 10:40:10 kg/ha. Minimal fertilizer required. Responds well to organic manures.',
        'conditions': 'Extremely drought-resistant, sandy/arid soils, pH 6.5-8.0, rainfall 200-500mm.',
        'tips': 'Primarily grown as a cover crop to prevent soil erosion in drylands. Harvest when leaves yellow and dry.'
    },
    'mungbean': {
        'fertilizer': 'NPK Ratio 20:50:20 kg/ha. Apply gypsum if sulfur is deficient in the soil.',
        'conditions': 'Warm weather crop, sandy loam soils, pH 6.2-7.2, moderate rainfall (600-900mm).',
        'tips': 'Short duration crop (60-70 days). Excellent for catch-cropping between main seasons.'
    },
    'blackgram': {
        'fertilizer': 'NPK Ratio 20:40:20 kg/ha. Seed treatment with Rhizobium and Phosphobacteria is highly beneficial.',
        'conditions': 'Prefers heavy soils (black cotton soils), pH 6.5-7.8, warm and humid weather.',
        'tips': 'Sow during late kharif or spring. Control powdery mildew disease early using neem oil or fungicides.'
    },
    'lentil': {
        'fertilizer': 'NPK Ratio 20:50:20 kg/ha. Add Sulfur at 20 kg/ha if soil test indicates deficiency.',
        'conditions': 'Cold winter crop, tolerant to drought, prefers clay loam soils, pH 6.0-8.0.',
        'tips': 'Avoid sowing in waterlogging-prone fields. Practice early weeding to prevent crop suppression.'
    },
    'pomegranate': {
        'fertilizer': 'NPK Ratio 600:250:250 g/tree/year for mature trees. Apply Farm Yard Manure (FYM) regularly.',
        'conditions': 'Arid and semi-arid climates, pH 6.5-7.5, well-drained sandy/clay loam, tolerates salinity.',
        'tips': 'Prune trees annually to encourage sun penetration and air circulation. Control fruit borer moths.'
    },
    'banana': {
        'fertilizer': 'Heavy feeder. NPK Ratio 200:100:300 g/plant/year. Supplement with organic compost and potash.',
        'conditions': 'Tropical climate, pH 6.0-7.5, deep fertile alluvial or clay loam, high rainfall/irrigation.',
        'tips': 'Provide windbreaks to protect leaves. Support heavy fruit bunches using bamboo poles (propping).'
    },
    'mango': {
        'fertilizer': 'NPK Ratio 100:50:100 g/tree/year per year of age. Apply micronutrients like Zinc and Boron.',
        'conditions': 'Tropical/subtropical climate, deep loamy soils, pH 5.5-7.5, needs dry spell for flowering.',
        'tips': 'Prune dead wood after harvest. Use pheromone traps to manage fruit flies.'
    },
    'grapes': {
        'fertilizer': 'NPK Ratio 100:50:150 kg/ha. Apply organic manures and sulfate of potash.',
        'conditions': 'Mediterranean climate, gravelly or sandy loam soils, pH 6.5-7.5, dry summers.',
        'tips': 'Train vines on trellises. Practice regular drip irrigation and thin out crowded grape clusters.'
    },
    'watermelon': {
        'fertilizer': 'NPK Ratio 80:40:60 kg/ha. Needs plenty of nitrogen in early growth, potash during fruiting.',
        'conditions': 'Hot, dry climate, sandy riverbed soils, pH 6.0-7.0, high sunlight requirement.',
        'tips': 'Use black plastic mulching to warm soil and control weeds. Avoid watering from above to prevent mildew.'
    },
    'muskmelon': {
        'fertilizer': 'NPK Ratio 80:60:80 kg/ha. Apply plenty of compost and calcium to prevent blossom end rot.',
        'conditions': 'Sandy loam, warm weather, pH 6.0-7.0, low humidity, temperature 25-35°C.',
        'tips': 'Reduce irrigation during fruit ripening to improve sugar content and sweetness.'
    },
    'apple': {
        'fertilizer': 'NPK Ratio 350:175:350 g/tree/year for mature trees. Supplement with Calcium nitrate sprays.',
        'conditions': 'Temperate climate, deep loamy soil, pH 6.0-6.8, winter chilling hours (800-1500 hours).',
        'tips': 'Thin blossoms to prevent biennial bearing. Practice integrated pest management for scab disease.'
    },
    'orange': {
        'fertilizer': 'NPK Ratio 150:50:100 g/tree/year per year of growth. Needs Zinc, Iron, and Manganese.',
        'conditions': 'Subtropical, well-drained loamy soil, pH 5.5-7.5, sensitive to severe frost.',
        'tips': 'Avoid water logging at the root zone. Control citrus psylla and leaf miners promptly.'
    },
    'papaya': {
        'fertilizer': 'NPK Ratio 250:250:500 g/plant/year applied in split doses. Add compost monthly.',
        'conditions': 'Tropical climate, sandy loam, excellent drainage is mandatory, pH 6.0-6.5.',
        'tips': 'Avoid water stagnation completely as it causes root rot within 24 hours. Grow in wind-protected zones.'
    },
    'coconut': {
        'fertilizer': 'NPK Ratio 500:320:1200 g/palm/year. Requires common salt (NaCl) for optimal growth.',
        'conditions': 'Coastal sandy soils, high humidity, pH 5.2-8.0, high rainfall (1000-3000mm).',
        'tips': 'Keep the basin weed-free. Apply green leaf manure to improve water retention in sandy soils.'
    },
    'cotton': {
        'fertilizer': 'NPK Ratio 100:50:50 kg/ha. Apply Nitrogen in multiple split doses to avoid leaching.',
        'conditions': 'Black cotton soil (vertisols) or deep alluvial, dry weather during harvest, pH 6.0-8.0.',
        'tips': 'Pinch terminal buds (topping) at 80-90 days to encourage sympodial branches. Monitor for bollworms.'
    },
    'jute': {
        'fertilizer': 'NPK Ratio 60:30:30 kg/ha. Supplement with organic compost during land preparation.',
        'conditions': 'Hot and wet climate, alluvial soils, pH 6.0-7.5, high rainfall (>1000mm).',
        'tips': 'Harvest at the small pod stage for best fiber quality. Retting must be done in clean, slow-flowing water.'
    },
    'coffee': {
        'fertilizer': 'NPK Ratio 140:90:120 kg/ha. Requires regular addition of compost and leaf mulch.',
        'conditions': 'Hilly slopes, shade-grown, pH 5.0-6.5, temperate climate (15-25°C), organic-rich soil.',
        'tips': 'Grow under a two-tier shade tree canopy. Prune branches regularly to control the spread of rust.'
    }
}

def get_crop_details(crop_name):
    """Retrieves agronomic details for a given crop name (case-insensitive)."""
    normalized_name = str(crop_name).lower().strip()
    return CROP_DETAILS.get(normalized_name, {
        'fertilizer': 'N/A. Please run a local soil chemistry analysis.',
        'conditions': 'N/A. Contact your local agricultural extension service.',
        'tips': 'N/A. Check global crop cultivation guides.'
    })
