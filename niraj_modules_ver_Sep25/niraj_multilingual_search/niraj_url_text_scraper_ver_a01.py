
import requests
from bs4 import BeautifulSoup
import re
import json
import threading







def perform_niraj_url_text_crawling(
        in_file_path = '../Data/urls.json', 
        out_file_path = '../Data/urls_with_text.json', 
        verbose = False, 
        ):
    with open(in_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    proxies = {
            'http': 'http://brd-customer-hl_c4d84340-zone-testing:su1m4td6rxw0@brd.superproxy.io:22225',
            'https': 'http://brd-customer-hl_c4d84340-zone-testing:su1m4td6rxw0@brd.superproxy.io:22225',
    }

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

    for entry in data:
        url = entry["url"]
        if verbose: print(url)
        
        try:
            # Send a GET request to the URL with a timeout of 3 seconds
            response = requests.get(url, headers=headers, proxies=proxies, timeout=3)
            
            if response.status_code == 200:
                try:
                    soup = BeautifulSoup(response.text.encode('latin-1').decode('utf-8'), "html.parser")
                except Exception as e:
                    soup = BeautifulSoup(response.text, "html.parser")
                all_text = soup.get_text()
                cleaned_text = re.sub(r'\s+', ' ', all_text).strip()
                entry['text'] = cleaned_text

                with open(out_file_path, 'w', encoding='utf-8') as json_file:
                    json.dump(data, json_file, ensure_ascii=False, indent=4)
                
                if verbose: print("Scraped data cleaned and stored in 'urls.json'.")
            else:
                if verbose: print("Failed to retrieve the webpage. Status code:", response.status_code)
        
        except requests.Timeout:
            if verbose: print("Connection to the URL timed out.")
        except requests.RequestException as e:
            if verbose: print("An error occurred:", str(e))
        
    if verbose: print(f"Websites Scraped and stored in {out_file_path}")
    return data