
import json
from langdetect import detect


def map_language_to_country(language, country):
    country = country
    language_country_mapping = {
        "en": "United States",     # English
        "es": "Spain",             # Spanish
        "fr": "France",            # French
        "de": "Germany",           # German
        "it": "Italy",             # Italian
        "pt": "Portugal",          # Portuguese
        "nl": "Netherlands",       # Dutch
        "ru": "Russia",            # Russian
        "ja": "Japan",             # Japanese
        "ko": "South Korea",       # Korean
        "zh-cn": "China",          # Simplified Chinese
        "zh-tw": "Taiwan",         # Traditional Chinese
        "ar": "Saudi Arabia",      # Arabic
        "hi": "India",             # Hindi
        "tr": "Turkey",            # Turkish
        "pl": "Poland",            # Polish
        "sv": "Sweden",            # Swedish
        "fi": "Finland",           # Finnish
        "no": "Norway",            # Norwegian
        "da": "Denmark",           # Danish
        "gr": "Greece",            # Greek
        "th": "Thailand",          # Thai
        "vi": "Vietnam",           # Vietnamese
        "id": "Indonesia",         # Indonesian
        "ms": "Malaysia",          # Malay
        "hu": "Hungary",           # Hungarian
        "ro": "Romania",           # Romanian
        "cz": "Czech Republic",    # Czech
        "sk": "Slovakia",          # Slovak
        "bg": "Bulgaria",          # Bulgarian
        "hr": "Croatia",           # Croatian
        "sl": "Slovenia",          # Slovenian
        "sr": "Serbia",            # Serbian
        "uk": "Ukraine",           # Ukrainian
        "el": "Greece",            # Greek
        "he": "Israel",            # Hebrew
        "fa": "Iran",              # Persian
        "th": "Thailand",          # Thai
        "ms": "Malaysia",          # Malay
        "ja": "Japan",             # Japanese
        "ko": "South Korea",       # Korean
        "cn": "China",             # Chinese
        "tr": "Turkey",            # Turkish
        "pt": "Portugal",          # Portuguese
        "br": "Brazil",            # Portuguese (Brazil)
        "in": "India",             # Hindi (India)
        "pk": "Pakistan",          # Urdu (Pakistan)
        "bn": "Bangladesh",        # Bengali (Bangladesh)
        "th": "Thailand",          # Thai
        "my": "Myanmar",           # Burmese
    }
    return language_country_mapping.get(language, country)


def correct_niraj_country_by_language(
        in_file_path = '../Data/urls.json', 
        out_file_path = '../Data/urls.json', 
        ):
    with open(in_file_path, 'r') as file:
        data = json.load(file)

    for item in data:
        try:
            text = item["text"]
        except KeyError:
            continue
        
        try:
            language = detect(text)
        except Exception as e:
            continue
        country = item['country']
        if language == 'en' or language == 'Unknown':
            # print(country)
            continue
        else:
            country = map_language_to_country(language, country)

        item["country"] = country

    with open(out_file_path, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Country validation complete. JSON file updated.")
    return data
