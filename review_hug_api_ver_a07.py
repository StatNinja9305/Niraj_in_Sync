"""


* Warning *
This code is under development. Any part of this code is subject to change.


# Command:

ver=a07



# Setting up a server:
hug -f ./review_hug_api_ver_${ver}.py



# Web browser access:
# # Sevice:
http://localhost:8000/generate_output?url=https://pig-data.jp/


# # Documentation:
http://localhost:8000/documentation


# Test Python run:
python ./review_hug_api_ver_${ver}.py \


# Installation:
pip install dicttoxml


# In this code, @hug is the HTTP method decoder.
"""

import hug, json, re
import dicttoxml


# Custom imports.
# Module Search Query Generation.
from niraj_modules.niraj_search_query.niraj_url_scraper import save_niraj_input_company_page
from niraj_modules.niraj_search_query.niraj_choose_model import get_niraj_model_to_use
from niraj_modules.niraj_search_query.niraj_summarizer import get_niraj_corpus_summary
from niraj_modules.niraj_search_query.niraj_query_generator import generate_niraj_search_queries

# Module Multilingual Google Search.
from niraj_modules.niraj_multilingual_search.niraj_query_translator import translate_niraj_queries_to_languages
from niraj_modules.niraj_multilingual_search.niraj_query_search import search_niraj_on_google
from niraj_modules.niraj_multilingual_search.niraj_url_extractor import save_niraj_unique_urls
from niraj_modules.niraj_multilingual_search.niraj_get_country_domain import add_niraj_country_to_urls
from niraj_modules.niraj_multilingual_search.niraj_url_text_scraper import perform_niraj_url_text_crawling
from niraj_modules.niraj_multilingual_search.niraj_validate_country import correct_niraj_country_by_language

# Mogule Page Ranking.
from niraj_modules.niraj_page_ranking.niraj_rank_urls import rank_niraj_pages_by_score
from niraj_modules.niraj_page_ranking.niraj_json_to_csv import save_niraj_json_to_csv




"""
RuntimeError: Failed to import transformers.models.auto because of the following error (look up to see its traceback):
PyO3 modules may only be initialized once per interpreter process


"""


@hug.get('/generate_output')
def generate_output(
        url = "https://pig-data.jp/", 
        region = "Japan", 
        language = "JP", 

        document = "", 
        top = 20, 
        sheath = "サービス", 

        query_option_1 = "", 
        query_option_2 = "", 
        domain_type = ".com", 
        ):
    """
    # # Sevice:
    http://localhost:8000/generate_output?region=Japan
    http://localhost:8000/generate_output?url=https://pig-data.jp/
    """

    max_of_urls = 30

    record = {
            "url": "https://example.com", 
            "score": 0.123, 
            "category": "Media",
            "country": "Japan",
            "domain": "domain_name", 
            }
    
    corpus_file_path = "./Data/corpus.txt"
    text = save_niraj_input_company_page(url, corpus_file_path)
    """
    model_to_use = get_niraj_model_to_use(
            # Path to the crawled input company landing page.
            corpus_file_path = corpus_file_path, 
            # Path to the file containing language-to-model mapping
            lang_file_path = "./Data/language_models.txt", 
            # Path to the file containing model_name to model_link mapping
            link_file_path = "./Data/model_links.txt", 
            verbose = True, 
            )
    summary = get_niraj_corpus_summary(
            model_name = model_to_use, 
            corpus_file_path = corpus_file_path, 
            summary_file_path = './Data/summary_corpus.txt', 
            verbose = True, 
            )
    """
    query_file_path = './Data/queries.txt'
    queries = generate_niraj_search_queries(
            corpus_file_path = corpus_file_path, 
            output_file_path = query_file_path, 
            spacy_model_name = "ja_ginza", 
            )
    print(queries)
    
    query_dir_path = translate_niraj_queries_to_languages(
            query_file_path = query_file_path, 
            
            query_dir_path = "./Data/Queries/", 
            langs = ["ja", "en"], 
            )
    url_file_path = './Data/urls_of_raw.txt'
    url_data = search_niraj_on_google(
            query_dir_path = query_dir_path, 
            url_file_path = url_file_path, 
            verbose = True, 
            )
    unique_file_path = './Data/unq_urls.json'
    unique_data = save_niraj_unique_urls(
            url_file_path = url_file_path, 
            unique_file_path = unique_file_path, 
            )
    country_file_path = './Data/urls.txt'
    urls_data = add_niraj_country_to_urls(
            unique_file_path = unique_file_path, 
            country_file_path = country_file_path, 
            )
    text_file_path = './Data/urls_with_text.json'
    urls_with_text = perform_niraj_url_text_crawling(
            in_file_path = country_file_path, 
            out_file_path = text_file_path, 
            verbose = True, 
            max_of_urls = max_of_urls, 
            )
    correct_file_path = './Data/urls_with_text_with_correct_country.json'
    correct_data = correct_niraj_country_by_language(
            in_file_path = text_file_path, 
            out_file_path = correct_file_path, 
            )
    score_file_path = "./Data/score_URLs.json"
    scores_data = rank_niraj_pages_by_score(
            url_file_path = correct_file_path, 
            # Assume each URL entry has "text" attribute.
            corpus_file_path = corpus_file_path, 
            temp_file_path = './Data/urls_scored.json', 
            out_file_path = score_file_path, 
            )
    table_file_path = save_niraj_json_to_csv(
            input_json = score_file_path, 
            output_csv = "./Data/score_URLs.csv", 
            headers = ["URL", "Country", "Domain", "Category", "Score"], 
            )
    
    # Output handling.
    submit_data = dict(
            function = "generate_output()", 
            text = text, 
            queries = "  ,  ".join(queries) , 
            table_file_path = table_file_path, 
            )
    xml_bytes = dicttoxml.dicttoxml(submit_data)
    xml_str = xml_bytes.decode("utf-8")
    return xml_str


@hug.get('/record_user_information')
def record_user_information(label = "label.", text = "text."):
    """
    # # Sevice:
    http://localhost:8000/record_user_information?label=label_A&text=text_B
    """
    # "record_user_information: " + label + " AND " + text
    # "record_user_information: {}".format(message)
    return "record_user_information: " + label + " AND " + text


@hug.get('/subscribe')
def subscribe(user_id = "User_1."):
    """
    # # Sevice:
    http://localhost:8000/subscribe?user_id=User_A
    """
    return "subscribe: " + user_id


@hug.get('/get_demo_output')
def get_demo_output(
        url = "https://pig-data.jp/", 
        region = "Japan", 
        language = "JP", 
        ):
    """
    # # Sevice:
    http://localhost:8000/get_demo_output?region=Japan
    """
    message = generate_output(
            url = url, 
            region = region, 
            language = language, 

            document = "", 
            top = 10, 
            sheath = "サービス", 

            query_option_1 = "", 
            query_option_2 = "", 
            domain_type = ".com", 
            )
    return "get_demo_output: " + region










# End