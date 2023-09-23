


import requests
from bs4 import BeautifulSoup
import re


def save_niraj_input_company_page(
        url = "https://pig-data.jp/", 
        out_file_path = "../Data/corpus.txt", 
        ):
    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, "html.parser")

        all_text = soup.get_text()

        # Clean and process the scraped data
        cleaned_text = re.sub(r'\s+', ' ', all_text).strip()

        with open(out_file_path, "w", encoding="utf-8") as file:
            file.write(cleaned_text)

        print("Scraped data cleaned and stored in 'corpus.txt'.")
    else:
        print("Failed to retrieve the webpage.")