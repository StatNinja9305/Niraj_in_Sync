"""



pip install langdetect

"""


import requests
from bs4 import BeautifulSoup
from langdetect import detect



def get_niraj_model_to_use(
        # Path to the crawled input company landing page.
        corpus_file_path = "./Data/corpus.txt", 
        # Path to the file containing language-to-model mapping
        lang_file_path = "./Data/language_models.txt", 
        # Path to the file containing model_name to model_link mapping
        link_file_path = "./Data/model_links.txt", 
        verbose = False, 
        ):

    with open(corpus_file_path, 'r') as file:
        text = file.read()
    # Detect the language of the text
    detected_language = detect(text)

    # This function reads a file to get a dictionary.
    def load_language_to_model_mapping(file_path):
        with open(file_path, "r") as file:
            return dict(line.strip().split(": ") for line in file)
    # Load the language-to-model mapping
    language_to_model = load_language_to_model_mapping(lang_file_path)

    # Get the model based on the detected language, defaulting to "BART" for English
    model_assigned = language_to_model.get(detected_language, "distilbart")
    if verbose:
        print("Detected Language:", detected_language)
        print("Assigned Model:", model_assigned)

    def load_model_name_to_model_link_mapping(file_path):
        with open(file_path, "r") as file:
            return dict(line.strip().split(": ") for line in file)

    # Load the model_name to model_link mapping
    model_link = load_model_name_to_model_link_mapping(link_file_path)
    model_to_use = model_link.get(model_assigned, "distilbart")
    if verbose:
        print("Model link:", model_to_use)
    return model_to_use


