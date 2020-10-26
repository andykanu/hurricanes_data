# names of hurricanes
names = [
    "Cuba I",
    "San Felipe II Okeechobee",
    "Bahamas",
    "Cuba II",
    "CubaBrownsville",
    "Tampico",
    "Labor Day",
    "New England",
    "Carol",
    "Janet",
    "Carla",
    "Hattie",
    "Beulah",
    "Camille",
    "Edith",
    "Anita",
    "David",
    "Allen",
    "Gilbert",
    "Hugo",
    "Andrew",
    "Mitch",
    "Isabel",
    "Ivan",
    "Emily",
    "Katrina",
    "Rita",
    "Wilma",
    "Dean",
    "Felix",
    "Matthew",
    "Irma",
    "Maria",
    "Michael",
]

# months of hurricanes
months = [
    "October",
    "September",
    "September",
    "November",
    "August",
    "September",
    "September",
    "September",
    "September",
    "September",
    "September",
    "October",
    "September",
    "August",
    "September",
    "September",
    "August",
    "August",
    "September",
    "September",
    "August",
    "October",
    "September",
    "September",
    "July",
    "August",
    "September",
    "October",
    "August",
    "September",
    "October",
    "September",
    "September",
    "October",
]

# years of hurricanes
years = [
    1924,
    1928,
    1932,
    1932,
    1933,
    1933,
    1935,
    1938,
    1953,
    1955,
    1961,
    1961,
    1967,
    1969,
    1971,
    1977,
    1979,
    1980,
    1988,
    1989,
    1992,
    1998,
    2003,
    2004,
    2005,
    2005,
    2005,
    2005,
    2007,
    2007,
    2016,
    2017,
    2017,
    2018,
]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [
    165,
    160,
    160,
    175,
    160,
    160,
    185,
    160,
    160,
    175,
    175,
    160,
    160,
    175,
    160,
    175,
    175,
    190,
    185,
    160,
    175,
    180,
    165,
    165,
    160,
    175,
    180,
    185,
    175,
    175,
    165,
    180,
    175,
    160,
]

# areas affected by each hurricane
areas_affected = [
    ["Central America", "Mexico", "Cuba", "Florida", "The Bahamas"],
    ["Lesser Antilles", "The Bahamas", "United States East Coast", "Atlantic Canada"],
    ["The Bahamas", "Northeastern United States"],
    ["Lesser Antilles", "Jamaica", "Cayman Islands", "Cuba", "The Bahamas", "Bermuda"],
    ["The Bahamas", "Cuba", "Florida", "Texas", "Tamaulipas"],
    ["Jamaica", "Yucatn Peninsula"],
    ["The Bahamas", "Florida", "Georgia", "The Carolinas", "Virginia"],
    ["Southeastern United States", "Northeastern United States", "Southwestern Quebec"],
    ["Bermuda", "New England", "Atlantic Canada"],
    ["Lesser Antilles", "Central America"],
    ["Texas", "Louisiana", "Midwestern United States"],
    ["Central America"],
    ["The Caribbean", "Mexico", "Texas"],
    ["Cuba", "United States Gulf Coast"],
    ["The Caribbean", "Central America", "Mexico", "United States Gulf Coast"],
    ["Mexico"],
    ["The Caribbean", "United States East coast"],
    ["The Caribbean", "Yucatn Peninsula", "Mexico", "South Texas"],
    ["Jamaica", "Venezuela", "Central America", "Hispaniola", "Mexico"],
    ["The Caribbean", "United States East Coast"],
    ["The Bahamas", "Florida", "United States Gulf Coast"],
    ["Central America", "Yucatn Peninsula", "South Florida"],
    ["Greater Antilles", "Bahamas", "Eastern United States", "Ontario"],
    ["The Caribbean", "Venezuela", "United States Gulf Coast"],
    ["Windward Islands", "Jamaica", "Mexico", "Texas"],
    ["Bahamas", "United States Gulf Coast"],
    ["Cuba", "United States Gulf Coast"],
    ["Greater Antilles", "Central America", "Florida"],
    ["The Caribbean", "Central America"],
    ["Nicaragua", "Honduras"],
    [
        "Antilles",
        "Venezuela",
        "Colombia",
        "United States East Coast",
        "Atlantic Canada",
    ],
    [
        "Cape Verde",
        "The Caribbean",
        "British Virgin Islands",
        "U.S. Virgin Islands",
        "Cuba",
        "Florida",
    ],
    [
        "Lesser Antilles",
        "Virgin Islands",
        "Puerto Rico",
        "Dominican Republic",
        "Turks and Caicos Islands",
    ],
    ["Central America", "United States Gulf Coast (especially Florida Panhandle)"],
]

# damages (USD($)) of hurricanes
damages = [
    "Damages not recorded",
    "100M",
    "Damages not recorded",
    "40M",
    "27.9M",
    "5M",
    "Damages not recorded",
    "306M",
    "2M",
    "65.8M",
    "326M",
    "60.3M",
    "208M",
    "1.42B",
    "25.4M",
    "Damages not recorded",
    "1.54B",
    "1.24B",
    "7.1B",
    "10B",
    "26.5B",
    "6.2B",
    "5.37B",
    "23.3B",
    "1.01B",
    "125B",
    "12B",
    "29.4B",
    "1.76B",
    "720M",
    "15.1B",
    "64.8B",
    "91.6B",
    "25.1B",
]

# deaths for each hurricane
deaths = [
    90,
    4000,
    16,
    3103,
    179,
    184,
    408,
    682,
    5,
    1023,
    43,
    319,
    688,
    259,
    37,
    11,
    2068,
    269,
    318,
    107,
    65,
    19325,
    51,
    124,
    17,
    1836,
    125,
    87,
    45,
    133,
    603,
    138,
    3057,
    74,
]

# write your update damages function here:
def update_damages(damages):
    updated_damages = []
    for damage in damages:
        if damage[-1] == "M":
            updated_damages.append(float(damage[:-1]) * 1000000)
        elif damage[-1] == "B":
            updated_damages.append(float(damage[:-1]) * 1000000000)
        else:
            updated_damages.append(damage)
    return updated_damages


updated_damages = update_damages(damages)
# write your construct hurricane dictionary function here:
def hurricane_dict(names, months, years, max_winds, areas, damage, deaths):
    hurricanes_dictionary = dict()
    for i in range(len(names)):
        hurricanes_dictionary[names[i]] = {
            "Month": months[i],
            "Year": years[i],
            "Max Sustained Wind": max_winds[i],
            "Areas Affected": areas[i],
            "Damage": damage[i],
            "Deaths": deaths[i],
        }
    return hurricanes_dictionary


hurricanes_by_name = hurricane_dict(
    names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths
)


# write your construct hurricane by year dictionary function here:
def hurricane_by_year_dict(hurricanes_dict):
    dict_by_year = dict()
    for key, value in hurricanes_dict.items():
        hurricane_name = {"Name": key}
        hurricane_name.update(value)
        current_year = value["Year"]
        if current_year not in dict_by_year.keys():
            dict_by_year[current_year] = []
        dict_by_year[current_year].append(hurricane_name)
    return dict_by_year


# print(hurricane_by_year_dict(hurricanes_by_name))
# write your count affected areas function here:
def count_affected_areas(hurricanes_dict):
    dict_affected_area = dict()
    for value in hurricanes_dict.values():
        areas = value["Areas Affected"]
        for area in areas:
            if area not in dict_affected_area.keys():
                dict_affected_area[area] = 1
            dict_affected_area[area] += 1
    return dict_affected_area


# write your find most affected area function here:
def most_affected_area(affected_area_dict):
    max_value = max(affected_area_dict.values())
    max_key = [k for k, v in affected_area_dict.items() if v == max_value]
    most_affected = {k: max_value for k in max_key}
    return most_affected


# write your greatest number of deaths function here:
def highest_deaths(hurricanes_dict):
    my_dict = dict()
    for key, value in hurricanes_dict.items():
        my_dict[key] = value["Deaths"]
    max_value = max(my_dict.values())
    max_key = [k for k, v in my_dict.items() if v == max_value]
    highest_deaths = {k: max_value for k in max_key}
    return highest_deaths


# write your catgeorize by mortality function here:
def mortality_rating(hurricanes_dict):
    mortality_scale = {0: [], 1: [], 2: [], 3: [], 4: []}
    for key, value in hurricanes_dict.items():
        if value["Deaths"] == 0:
            mortality_scale[0].append({key: value})
        elif value["Deaths"] <= 100:
            mortality_scale[1].append({key: value})
        elif value["Deaths"] <= 500:
            mortality_scale[2].append({key: value})
        elif value["Deaths"] <= 1000:
            mortality_scale[3].append({key: value})
        else:
            mortality_scale[4].append({key: value})
    return mortality_scale


# write your greatest damage function here:
def most_damage(hurricanes_dict):
    my_dict = dict()
    for key, value in hurricanes_dict.items():
        if value["Damage"] != "Damages not recorded":
            my_dict[key] = value["Damage"]
    max_value = max(my_dict.values())
    max_key = [k for k, v in my_dict.items() if v == max_value]
    highest_damage = {k: max_value for k in max_key}
    return highest_damage


# write your catgeorize by damage function here:
def damage_rating(hurricanes_dict):
    damage_scale = {0: [], 1: [], 2: [], 3: [], 4: []}
    for key, value in hurricanes_dict.items():
        if value["Damage"] == 0 or value["Damage"] == "Damages not recorded":
            damage_scale[0].append({key: value})
        elif value["Damage"] <= 100000000:
            damage_scale[1].append({key: value})
        elif value["Damage"] <= 1000000000:
            damage_scale[2].append({key: value})
        elif value["Damage"] <= 10000000000:
            damage_scale[3].append({key: value})
        else:
            damage_scale[4].append({key: value})
    return damage_scale
