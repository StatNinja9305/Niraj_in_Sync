"""

pip install mtranslate


"""

from mtranslate import translate
import os



TARGET_LANGUAGES = [
    "en",  # English
    "ja",  # Japanese {{  FOR JAPANESE MARKET SPECIFICALLY   }}
    "es",  # Spanish
    "fr",  # French
    "de",  # German
    "it",  # Italian
    "pt",  # Portuguese
    "nl",  # Dutch
    "ru",  # Russian
    "zh",  # Chinese
    "ar",  # Arabic
    "ko",  # Korean
    "tr",  # Turkish
    "hi",  # Hindi
    "sv",  # Swedish
    "fi",  # Finnish
    "no",  # Norwegian
    "da",  # Danish
    "pl",  # Polish
    "el",  # Greek
    "cs",  # Czech
    "hu",  # Hungarian
    "ro",  # Romanian
    "vi",  # Vietnamese
    "th",  # Thai
    "id",  # Indonesian
    "ms",  # Malay
    "te"   # Telugu
]

def translate_niraj_queries_to_languages(
        query_file_path = '../Data/queries.txt', 
        query_dir_path = "../Data/Queries/", 
        ):
    with open(query_file_path, 'r') as file:
        text_to_translate = file.read()

    # Make an output directory.
    if not os.path.exists(query_dir_path):
        os.mkdir(query_dir_path)
    else:
        print("Directory already exists.")
    #os.makedirs(query_dir_path)

    for lang in TARGET_LANGUAGES:
        translated_text = translate(text_to_translate, lang)
        filename = f"queries_{lang}.txt"
        temp_file_path = os.path.join(query_dir_path, filename)
        with open(temp_file_path, 'w') as file:
            file.write(translated_text)
        # queries.append(translated_text)
        print(f"Translated to {lang}")
    return query_dir_path


"""
file_list = os.listdir(query_dir_path)
for filename in file_list:
    if filename.endswith(".txt"):
        file_path = os.path.join(query_dir_path, filename)
        with open(file_path, "r") as file:
            lines = file.readlines()

        queries = []
        for line in lines:
            query = line.strip()
            queries.append(query)
        new_queries = []
        for query in queries:
            # print("Current query:", query)
            # query = query + ' NOT site:' + str(input_url)
            new_queries.append(query)
            # print(query)
        
        with open(file_path, 'w') as file:
            # Write each query to a new line in the file
            for query in new_queries:
                # print(query)
                # output_file.write(str(query[0]) + ' NOT site:' + str_url + '\n')
                file.write(str(query) + '\n')
"""
