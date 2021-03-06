"""
Contains street suffix abbreviations.

October 16, 2018 - added Canadian street abbreviations by Andrew MacKinnon
"""

USA_ABBREVS = {
    'alley': 'aly',
    'anex': 'anx',
    'arcade': 'arc',
    'avenue': 'ave',
    'bayou': 'byu',
    'beach': 'bch',
    'bend': 'bnd',
    'bluff': 'blf',
    'bluffs': 'blfs',
    'bottom': 'btm',
    'boulevard': 'blvd',
    'branch': 'br',
    'bridge': 'brg',
    'brook': 'brk',
    'brooks': 'brks',
    'burg': 'bg',
    'burgs': 'bgs',
    'bypass': 'byp',
    'camp': 'cp',
    'canyon': 'cyn',
    'cape': 'cpe',
    'causeway': 'cswy',
    'center': 'ctr',
    'centers': 'ctrs',
    'circle': 'cir',
    'circles': 'cirs',
    'cliff': 'clf',
    'cliffs': 'clfs',
    'club': 'clb',
    'cluster': 'cl',
    'common': 'cmn',
    'commons': 'cmns',
    'corner': 'cor',
    'corners': 'cors',
    'course': 'crse',
    'court': 'ct',
    'courts': 'cts',
    'cove': 'cv',
    'coves': 'cvs',
    'creek': 'crk',
    'crescent': 'cres',
    'crest': 'crst',
    'crossing': 'xing',
    'crossroad': 'xrd',
    'crossroads': 'xrds',
    'curve': 'curv',
    'dale': 'dl',
    'dam': 'dm',
    'divide': 'dv',
    'drive': 'dr',
    'drives': 'drs',
    'estate': 'est',
    'estates': 'ests',
    'expressway': 'expy',
    'extension': 'ext',
    'extensions': 'exts',
    'fall': 'fall',
    'falls': 'fls',
    'ferry': 'fry',
    'field': 'fld',
    'fields': 'flds',
    'flat': 'flt',
    'flats': 'flts',
    'ford': 'frd',
    'fords': 'frds',
    'forest': 'frst',
    'forge': 'frg',
    'forges': 'frgs',
    'fork': 'frk',
    'forks': 'frks',
    'fort': 'ft',
    'freeway': 'fwy',
    'garden': 'gdn',
    'gardens': 'gdns',
    'gateway': 'gtwy',
    'glen': 'gln',
    'glens': 'glns',
    'green': 'grn',
    'greens': 'grns',
    'grove': 'grv',
    'groves': 'grvs',
    'harbor': 'hbr',
    'harbors': 'hbrs',
    'haven': 'hvn',
    'heights': 'hts',
    'highway': 'hwy',
    'hill': 'hl',
    'hills': 'hls',
    'hollow': 'holw',
    'inlet': 'inlt',
    'island': 'is',
    'islands': 'iss',
    'isle': 'isle',
    'junction': 'jct',
    'junctions': 'jcts',
    'key': 'ky',
    'keys': 'kys',
    'knoll': 'knl',
    'knolls': 'knls',
    'lake': 'lk',
    'lakes': 'lks',
    'land': 'land',
    'landing': 'lndg',
    'lane': 'ln',
    'light': 'lgt',
    'lights': 'lgts',
    'loaf': 'lf',
    'lock': 'lck',
    'locks': 'lcks',
    'lodge': 'ldg',
    'loop': 'lp',
    'mall': 'mall',
    'manor': 'mnr',
    'manors': 'mnrs',
    'meadow': 'mdw',
    'meadows': 'mdws',
    'mews': 'mews',
    'mill': 'ml',
    'mills': 'mls',
    'mission': 'msn',
    'motorway': 'mtwy',
    'mount': 'mt',
    'mountain': 'mtn',
    'mountains': 'mtns',
    'neck': 'nck',
    'orchard': 'orch',
    'oval': 'oval',
    'overpass': 'opas',
    'park': 'pk',
    'parks': 'pks',
    'parkway': 'pkwy',
    'parkways': 'pkwys',
    'pass': 'pass',
    'passage': 'psge',
    'path': 'path',
    'pike': 'pike',
    'pine': 'pne',
    'pines': 'pnes',
    'place': 'pl',
    'plain': 'pln',
    'plains': 'plns',
    'plaza': 'plz',
    'point': 'pt',
    'points': 'pts',
    'port': 'prt',
    'ports': 'prts',
    'prairie': 'pr',
    'radial': 'radl',
    'ramp': 'ramp',
    'ranch': 'rnch',
    'rapid': 'rpd',
    'rapids': 'rpds',
    'rest': 'rst',
    'ridge': 'rdg',
    'ridges': 'rdgs',
    'river': 'riv',
    'road': 'rd',
    'roads': 'rds',
    'route': 'rte',
    'row': 'row',
    'rue': 'rue',
    'run': 'run',
    'shoal': 'shl',
    'shoals': 'shls',
    'shore': 'shr',
    'shores': 'shrs',
    'skyway': 'skwy',
    'spring': 'spg',
    'springs': 'spgs',
    'spur': 'spur',
    'spurs': 'spurs',
    'square': 'sq',
    'squares': 'sqs',
    'station': 'sta',
    'stravenue': 'stra',
    'stream': 'strm',
    'street': 'st',
    'streets': 'sts',
    'summit': 'smt',
    'terrace': 'ter',
    'throughway': 'trwy',
    'trace': 'trce',
    'track': 'trak',
    'trafficway': 'trfy',
    'trail': 'trl',
    'trailer': 'trlr',
    'tunnel': 'tunl',
    'turnpike': 'tpke',
    'underpass': 'upas',
    'union': 'un',
    'unions': 'uns',
    'valley': 'vly',
    'valleys': 'vlys',
    'viaduct': 'via',
    'view': 'vw',
    'views': 'vws',
    'village': 'vlg',
    'villages': 'vlgs',
    'ville': 'vl',
    'vista': 'vis',
    'walk': 'walk',
    'walks': 'walks',
    'wall': 'wall',
    'way': 'way',
    'ways': 'ways',
    'well': 'wl',
    'wells': 'wls'
}

# Canada Post street suffix abbreviations in English from https://www.canadapost.ca/tools/pg/manual/PGaddress-e.asp
CAN_ABBREVS_EN = {
    'avenue': 'ave',
    'boulevard': 'blvd',
    'by-pass': 'bypass',
    'centre': 'ctr',
    'circle': 'cir',
    'circuit': 'circt',
    'concession': 'conc',
    'corners': 'crnrs',
    'court': 'crt',
    'crescent': 'cres',
    'cul-de-sac': 'cds',
    'diversion': 'divers',
    'drive': 'dr',
    'esplanade': 'espl',
    'expressway': 'expy',
    'extension': 'exten',
    'freeway': 'fwy',
    'gardens': 'gdns',
    'grounds': 'grnds',
    'harbour': 'harbr',
    'heights': 'hts',
    'highlands': 'hghlds',
    'highway': 'hwy',
    'limits': 'lmts',
    'lookout': 'lkout',
    'mountain': 'mtn',
    'orchard': 'orch',
    'park': 'pk',
    'passage': 'pass',
    'pathway': 'ptway',
    'place': 'pl',
    'point': 'pt',
    'private': 'pvt',
    'range': 'rg',
    'road': 'rd',
    'route': 'rte',
    'square': 'sq',
    'street': 'st',
    'subdivision': 'subdiv',
    'terrace': 'terr',
    'thicket': 'thick',
    'townline': 'tline',
    'turnabout': 'trnabt',
    'village': 'villge'
}

CAN_ABBREVS_FR = {
    'autoroute': 'aut',
    'avenue': 'av',
    'boulevard': 'boul',
    'carré': 'car',
    'carrefour': 'carref',
    'centre': 'c',
    'chemin': 'ch',
    'circle': 'cir',
    'circuit': 'circt',
    'croissant': 'crois',
    'cul-de-sac': 'cds',
    'échangeur': 'éch',
    'impasse': 'imp',
    'plateau': 'plat',
    'rond-point': 'rdpt',
    'ruelle': 'rle',
    'sentier': 'sent',
    'terrasse': 'tsse',
}

# Additional street types
EXTRA_STREET_ABBREVS = {
    'ln': 'lane',
    'circ': 'circle',
    'crcl': 'circle',
    'cr': 'crescent'
}

# Province or territory in Canada
# Corresponding to first character of postal code
CAN_POSTAL_CODE_FIRST_LETTER = {
    'A': 'NL',
    'B': 'NS',
    'C': 'PE',
    'E': 'NB',
    'G': 'QC',
    'H': 'QC',
    'J': 'QC',
    'K': 'ON',
    'L': 'ON',
    'M': 'ON',
    'N': 'ON',
    'P': 'ON',
    'R': 'MB',
    'S': 'SK',
    'T': 'AB',
    'V': 'BC',
    'X': ('NT', 'NU'),
    'Y': 'YT'
}

# Valid 2nd letters of Canadian postal code
CAN_POSTAL_CODE_SECOND_LETTER = {'A','B','C','E','G','H','J','K','L','M','N','P','R','S','T','X','Y'}

# Valid 3nd letters of Canadian postal code
CAN_POSTAL_CODE_THIRD_LETTER = {'A','B','C','E','G','H','J','K','L','M','N','P','R','S','T','W','X','Y','Z'}

# List of valid Unicode hyphens
# Source: http://jkorpela.fi/dashes.html
UNICODE_HYPHENS = {'-','\u2010','\u2011', '\u2012', '\u2013', '\u2014', '\u2015', '\u2212', '\uFE58', '\uFE63', '\uFF0D'}
# In Regex format
UNICODE_HYPHENS_RE = '[\u2010\u2011\u2012\u2013\u2014\u2015\u2212\uFE58\uFE63\uFF0D]'

CAN_PROVINCES_TERRITORIES_EN = {
    'Alberta': 'AB',
    'British Columbia': 'BC',
    'Manitoba': 'MB',
    'New Brunswick': 'NB',
    'Newfoundland and Labrador': 'NL',
    'Northwest Territories': 'NT',
    'Nova Scotia': 'NS',
    'Nunavut': 'NU',
    'Ontario': 'ON',
    'Prince Edward Island': 'PE',
    # Canada Post addressing standards state that there is an accent in English in Quebec
    # but accents are rarely used in English for Quebec
    'Quebec': 'QC',
    'Saskatchewan': 'SK',
    'Yukon': 'YT'
}

CAN_PROVINCES_TERRITORIES_FR = {
    'Alberta': 'AB',
    'Colombie-Britannique': 'BC',
    'Manitoba': 'MB',
    'Nouveau-Brunswick': 'NB',
    'Terre-Neuve-et-Labrador': 'NL',
    'Territoires du Nord-Ouest': 'NT',
    'Nouvelle-Écosse': 'NS',
    'Nunavut': 'NU',
    'Ontario': 'ON',
    'Île-du-Prince-Édouard': 'PE',
    'Québec': 'QC',
    'Saskatchewan': 'SK',
    'Yukon': 'YT'
}

# States, territories and possessions - U.S.A.
US_STATES_EN = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'Armed Forces Africa': 'AE',
    'Armed Forces Americas': 'AA',
    'Armed Forces Canada': 'AE',
    'Armed Forces Europe': 'AE',
    'Armed Forces Middle East': 'AE',
    'Armed Forces Pacific': 'AE',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Marshall Islands': 'MH',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Micronesia': 'FM',
    'Minnesota': 'MN',
    'Minor Outlying Islands': 'UM',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands': 'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Virgin Islands': 'VI',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

# States, territories and possessions - U.S.A. - French
US_STATES_FR = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Samoa américaine': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'Forces armées Afrique': 'AE',
    'Forces armées américaines': 'AA',
    'Forces armées Canada': 'AE',
    'Forces armées européennes': 'AE',
    'Forces armées Moyen-Orient': 'AE',
    'Forces armées Pacifique': 'AE',
    'Californie': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District de Columbia': 'DC',
    'Floride': 'FL',
    'Georgie': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiane': 'LA',
    'Maine': 'ME',
    'Îles Marshall': 'MH',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Micronésie': 'FM',
    'Minnesota': 'MN',
    'Minor Outlying Islands': 'UM',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'Nouveau Mexique': 'NM',
    'New York': 'NY',
    'Caroline du Nord': 'NC',
    'Dakota du Nord': 'ND',
    'Northern Mariana Islands': 'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvanie': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'Caroline du Sud': 'SC',
    'Dakota du Sud': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Îles Vierges': 'VI',
    'Washington': 'WA',
    'Virginie de l’Ouest': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

# Old abbreviation PQ for Quebec, NF for Newfoundland
OLD_ABBREVS = {
    'NF': 'NL',
    'PQ': 'QC'
}

DIRECTION_ABBREV_EN = {
    'east': 'E',
    'west': 'W',
    'north': 'N',
    'south': 'S',
    'northeast': 'NE',
    'southeast': 'SE',
    'southwest': 'SW',
    'northwest': 'NW'
}

DIRECTION_ABBREV_FR = {
    'est': 'E',
    'ouest': 'O',
    'nord': 'N',
    'sud': 'S',
    'nord-est': 'NE',
    'nord-ouest': 'NO',
    'sud-ouest': 'SO',
    'sud-est': 'SE'
}

CITIES_CAN = {
    'Abbotsford': 'BC',
    'Ajax': 'ON',
    'Aurora': 'ON',
    'Barrie': 'ON',
    'Belleville': 'ON',
    'Bradford': 'ON',
    'Brantford': 'ON',
    'Burlington': 'ON',
    'Calgary': 'AB',
    'Carleton Place': 'ON',
    'Caledon': 'ON',
    'Charlottetown': 'PE',
    'Chatham': 'ON',
    'Collingwood': 'ON',
    'Churchill': 'MB',
    'Edmonton': 'ON',
    'Edmundston': 'NB',
    'Fort Erie': 'ON',
    'Fort McMurray': 'AB',
    'Fredericton': 'NB',
    'Gananoque': 'ON',
    'Gatineau': 'QC',
    'Grimsby': 'ON',
    'Halifax': 'NS',
    'Halton Hills': 'ON',
    'Kelowna': 'BC',
    'Kingston': 'ON',
    'Laval': 'QC',
    'Lindsay': 'ON',
    'London': 'ON',
    'Mississauga': 'ON',
    'Markham': 'ON',
    'Milton': 'ON',
    'Moncton': 'NB',
    'Montreal': 'QC',
    'Montréal': 'QC',
    'Newmarket': 'ON',
    'Nanaimo': 'BC',
    'Napanee': 'ON',
    'Niagara Falls': 'ON',
    'North Bay': 'ON',
    'North Battleford': 'SK',
    'Oakville': 'ON',
    'Orangeville': 'ON',
    'Orillia': 'ON',
    'Oshawa': 'ON',
    'Ottawa': 'ON',
    'Owen Sound': 'ON',
    'Pickering': 'ON',
    'Port Perry': 'ON',
    'Quebec': 'QC',
    'Quebec City': 'QC',
    'Québec': 'QC',
    'Richmond Hill': 'ON',
    'Saskatoon': 'SK',
    'Sherbrooke': 'ON',
    'St. Catharines': 'ON',
    'St. John': 'NB',
    'St. John''s': 'NL',
    'Sudbury': 'ON',
    'Thunder Bay': 'ON',
    'Timmins': 'ON',
    'Toronto': 'ON',
    'Trenton': 'ON',
    'Trois-Rivières': 'QC',
    'Vancouver': 'BC',
    'Vaughan': 'ON',
    'Victoria': 'BC',
    'Whitby': 'ON',
    'Windsor': 'ON',
    'Winnipeg': 'MB'
}

CITIES_US = {
    'Akron': 'OH',
    'Albany': 'NY',
    'Albuquerque': 'NM',
    'Arlington': 'TX',
    'Atlanta': 'GA',
    'Austin': 'TX',
    'Baltimore': 'MD',
    'Boston': 'MA',
    'Bronx': 'NY',
    'Brooklyn': 'NY',
    'Buffalo': 'NY',
    'Charlotte': 'NC',
    'Chicago': 'IL',
    'Cincinnati': 'OH',
    'Cleveland': 'OH',
    'Colorado Springs': 'CO',
    'Columbus': 'OH',
    'Dallas': 'TX',
    'Denver': 'CO',
    'Detroit': 'MI',
    'Durham': 'NC',
    'El Paso': 'TX',
    'Erie': 'PA',
    'Flint': 'MI',
    'Fort Worth': 'TX',
    'Fresno': 'CA',
    'Green Bay': 'WI',
    'Houston': 'TX',
    'Ithaca': 'NY',
    'Jacksonville': 'FL',
    'Kansas City': 'MO',
    'Las Vegas': 'NV',
    'Long Beach': 'CA',
    'Louisville': 'KY',
    'Los Angeles': 'CA',
    'Memphis': 'TN',
    'Mesa': 'AZ',
    'Miami': 'FL',
    'Milwaukee': 'WI',
    'Minneapolis': 'MN',
    'Nashville': 'TN',
    'New Orleans': 'LA',
    'New York': 'NY',
    'New York City': 'NY',
    'Oakland': 'CA',
    'Oklahoma City': 'OK',
    'Omaha': 'NE',
    'Ontario': 'CA',
    'Orlando': 'FL',
    'Philadelphia': 'PA',
    'Phoenix': 'AZ',
    'Pittsburgh': 'PA',
    'Portland': 'OR',
    'Queens': 'NY',
    'Raleigh': 'NC',
    'Reno': 'NV',
    'Richmond': 'VA',
    'Sacramento': 'CA',
    'San Antonio': 'TX',
    'San Diego': 'CA',
    'San Francisco': 'CA',
    'San Jose': 'CA',
    'Seattle': 'WA',
    'Staten Island': 'NY',
    'Tallahassee': 'FL',
    'Trenton': 'NJ',
    'Tucson': 'AZ',
    'Tulsa': 'OK',
    'Washington': 'DC',
    'Wichita': 'KS',
    'Yonkers': 'NY',
}

# From https://en.wikipedia.org/wiki/ISO_3166-1
COUNTRIES = {
    'Afghanistan': 'AF',
    'Åland Islands': 'AX',
    'Albania': 'AL',
    'Algeria': 'DZ',
    'American Samoa': 'AS',
    'Andorra': 'AD',
    'Angola': 'AO',
    'Anguilla': 'AI',
    'Antarctica': 'AQ',
    'Antigua and Barbuda': 'AG',
    'Argentina': 'AR',
    'Armenia': 'AM',
    'Aruba': 'AW',
    'Australia': 'AU',
    'Austria': 'AT',
    'Azerbaijan': 'AZ',
    'Bahamas': 'BS',
    'Bahrain': 'BH',
    'Bangladesh': 'BD',
    'Barbados': 'BB',
    'Belarus': 'BY',
    'Belgium': 'BE',
    'Belize': 'BZ',
    'Benin': 'BJ',
    'Bermuda': 'BM',
    'Bhutan': 'BT',
    'Bolivia (Plurinational State of)': 'BO',
    'Bonaire, Sint Eustatius and Saba': 'BQ',
    'Bosnia and Herzegovina': 'BA',
    'Botswana': 'BW',
    'Bouvet Island': 'BV',
    'Brazil': 'BR',
    'British Indian Ocean Territory': 'IO',
    'Brunei Darussalam': 'BN',
    'Bulgaria': 'BG',
    'Burkina Faso': 'BF',
    'Burundi': 'BI',
    'Cabo Verde': 'CV',
    'Cambodia': 'KH',
    'Cameroon': 'CM',
    'Canada': 'CA',
    'Cayman Islands': 'KY',
    'Central African Republic': 'CF',
    'Chad': 'TD',
    'Chile': 'CL',
    'China': 'CN',
    'Christmas Island': 'CX',
    'Cocos (Keeling) Islands': 'CC',
    'Colombia': 'CO',
    'Comoros': 'KM',
    'Congo': 'CG',
    'Congo (Democratic Republic of the)': 'CD',
    'Cook Islands': 'CK',
    'Costa Rica': 'CR',
    'Côte d''Ivoire': 'CI',
    'Croatia': 'HR',
    'Cuba': 'CU',
    'Curaçao': 'CW',
    'Cyprus': 'CY',
    'Czechia': 'CZ',
    'Denmark': 'DK',
    'Djibouti': 'DJ',
    'Dominica': 'DM',
    'Dominican Republic': 'DO',
    'Ecuador': 'EC',
    'Egypt': 'EG',
    'El Salvador': 'SV',
    'Equatorial Guinea': 'GQ',
    'Eritrea': 'ER',
    'Estonia': 'EE',
    'Eswatini': 'SZ',
    'Ethiopia': 'ET',
    'Falkland Islands (Malvinas)': 'FK',
    'Faroe Islands': 'FO',
    'Fiji': 'FJ',
    'Finland': 'FI',
    'France': 'FR',
    'French Guiana': 'GF',
    'French Polynesia': 'PF',
    'French Southern Territories': 'TF',
    'Gabon': 'GA',
    'Gambia': 'GM',
    'Georgia': 'GE',
    'Germany': 'DE',
    'Ghana': 'GH',
    'Gibraltar': 'GI',
    'Greece': 'GR',
    'Greenland': 'GL',
    'Grenada': 'GD',
    'Guadeloupe': 'GP',
    'Guam': 'GU',
    'Guatemala': 'GT',
    'Guernsey': 'GG',
    'Guinea': 'GN',
    'Guinea-Bissau': 'GW',
    'Guyana': 'GY',
    'Haiti': 'HT',
    'Heard Island and McDonald Islands': 'HM',
    'Holy See': 'VA',
    'Honduras': 'HN',
    'Hong Kong': 'HK',
    'Hungary': 'HU',
    'Iceland': 'IS',
    'India': 'IN',
    'Indonesia': 'ID',
    'Iran (Islamic Republic of)': 'IR',
    'Iraq': 'IQ',
    'Ireland': 'IE',
    'Isle of Man': 'IM',
    'Israel': 'IL',
    'Italy': 'IT',
    'Jamaica': 'JM',
    'Japan': 'JP',
    'Jersey': 'JE',
    'Jordan': 'JO',
    'Kazakhstan': 'KZ',
    'Kenya': 'KE',
    'Kiribati': 'KI',
    'Korea (Democratic People''s Republic of)': 'KP',
    'Korea (Republic of)': 'KR',
    'Kuwait': 'KW',
    'Kyrgyzstan': 'KG',
    'Lao People''s Democratic Republic': 'LA',
    'Latvia': 'LV',
    'Lebanon': 'LB',
    'Lesotho': 'LS',
    'Liberia': 'LR',
    'Libya': 'LY',
    'Liechtenstein': 'LI',
    'Lithuania': 'LT',
    'Luxembourg': 'LU',
    'Macao': 'MO',
    'Macedonia (the former Yugoslav Republic of)': 'MK',
    'Madagascar': 'MG',
    'Malawi': 'MW',
    'Malaysia': 'MY',
    'Maldives': 'MV',
    'Mali': 'ML',
    'Malta': 'MT',
    'Marshall Islands': 'MH',
    'Martinique': 'MQ',
    'Mauritania': 'MR',
    'Mauritius': 'MU',
    'Mayotte': 'YT',
    'Mexico': 'MX',
    'Micronesia (Federated States of)': 'FM',
    'Moldova (Republic of)': 'MD',
    'Monaco': 'MC',
    'Mongolia': 'MN',
    'Montenegro': 'ME',
    'Montserrat': 'MS',
    'Morocco': 'MA',
    'Mozambique': 'MZ',
    'Myanmar': 'MM',
    'Namibia': 'NA',
    'Nauru': 'NR',
    'Nepal': 'NP',
    'Netherlands': 'NL',
    'New Caledonia': 'NC',
    'New Zealand': 'NZ',
    'Nicaragua': 'NI',
    'Niger': 'NE',
    'Nigeria': 'NG',
    'Niue': 'NU',
    'Norfolk Island': 'NF',
    'Northern Mariana Islands': 'MP',
    'Norway': 'NO',
    'Oman': 'OM',
    'Pakistan': 'PK',
    'Palau': 'PW',
    'Palestine, State of': 'PS',
    'Panama': 'PA',
    'Papua New Guinea': 'PG',
    'Paraguay': 'PY',
    'Peru': 'PE',
    'Philippines': 'PH',
    'Pitcairn': 'PN',
    'Poland': 'PL',
    'Portugal': 'PT',
    'Puerto Rico': 'PR',
    'Qatar': 'QA',
    'Réunion': 'RE',
    'Romania': 'RO',
    'Russian Federation': 'RU',
    'Rwanda': 'RW',
    'Saint Barthélemy': 'BL',
    'Saint Helena, Ascension and Tristan da Cunha': 'SH',
    'Saint Kitts and Nevis': 'KN',
    'Saint Lucia': 'LC',
    'Saint Martin (French part)': 'MF',
    'Saint Pierre and Miquelon': 'PM',
    'Saint Vincent and the Grenadines': 'VC',
    'Samoa': 'WS',
    'San Marino': 'SM',
    'Sao Tome and Principe': 'ST',
    'Saudi Arabia': 'SA',
    'Senegal': 'SN',
    'Serbia': 'RS',
    'Seychelles': 'SC',
    'Sierra Leone': 'SL',
    'Singapore': 'SG',
    'Sint Maarten (Dutch part)': 'SX',
    'Slovakia': 'SK',
    'Slovenia': 'SI',
    'Solomon Islands': 'SB',
    'Somalia': 'SO',
    'South Africa': 'ZA',
    'South Georgia and the South Sandwich Islands': 'GS',
    'South Sudan': 'SS',
    'Spain': 'ES',
    'Sri Lanka': 'LK',
    'Sudan': 'SD',
    'Suriname': 'SR',
    'Svalbard and Jan Mayen': 'SJ',
    'Sweden': 'SE',
    'Switzerland': 'CH',
    'Syrian Arab Republic': 'SY',
    'Taiwan, Province of China[a]': 'TW',
    'Tajikistan': 'TJ',
    'Tanzania, United Republic of': 'TZ',
    'Thailand': 'TH',
    'Timor-Leste': 'TL',
    'Togo': 'TG',
    'Tokelau': 'TK',
    'Tonga': 'TO',
    'Trinidad and Tobago': 'TT',
    'Tunisia': 'TN',
    'Turkey': 'TR',
    'Turkmenistan': 'TM',
    'Turks and Caicos Islands': 'TC',
    'Tuvalu': 'TV',
    'Uganda': 'UG',
    'Ukraine': 'UA',
    'United Arab Emirates': 'AE',
    'United Kingdom of Great Britain and Northern Ireland': 'GB',
    'United States of America': 'US',
    'United States Minor Outlying Islands': 'UM',
    'Uruguay': 'UY',
    'Uzbekistan': 'UZ',
    'Vanuatu': 'VU',
    'Venezuela (Bolivarian Republic of)': 'VE',
    'Vietnam': 'VN',
    'Virgin Islands (British)': 'VG',
    'Virgin Islands (U.S.)': 'VI',
    'Wallis and Futuna': 'WF',
    'Western Sahara': 'EH',
    'Yemen': 'YE',
    'Zambia': 'ZM',
    'Zimbabwe': 'ZW'
}

COUNTRIES_ALTERNATE = {
    'United States': 'US',
    'USA': 'US',
    'Venezuela': 'VE',
}