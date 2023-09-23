



#from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
import os
import threading
import json





def search(query, num_results=20, proxy=None):
    proxies = {
        'http': 'http://brd-customer-hl_c4d84340-zone-testing:su1m4td6rxw0@brd.superproxy.io:22225',
        'https': 'http://brd-customer-hl_c4d84340-zone-testing:su1m4td6rxw0@brd.superproxy.io:22225',
    }
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

    url = f"https://www.google.com/search?q={query}&num={num_results}"
    # print("search: ",url)
    # url = f"https://search.brave.com/search?q={query}&num={num_results}"
    response = requests.get(url, headers=headers, proxies=proxies)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        href_tags = soup.find_all('a', href=True)

        results = []
        for tag in href_tags:
            # print(tag['href'])
            results.append(tag['href'])
        return results
    else:
        pass
        response.raise_for_status()


def search_google(query, num_results=20):
    """
    Functions called: search, 
    """
    # print("search_google: ", query)
    urls = []
    try:
        search_results = search(query, num_results=20)
        for idx, result in enumerate(search_results, start=1):
            urls.append(result)
            # print(urls.type())
            # print(f"{idx}. {result}")
        return urls
    except Exception as e:
        pass
        print("An error occurred:", e)


def search_with_timeout(query, num_results=10):
    """
    Functions called: search_google, 
    """
    # print("search_with_timeout: ", query)
    result = []
    def worker():
        nonlocal result
        result = search_google(query, num_results=10)
    thread = threading.Thread(target=worker)
    thread.start()
    thread.join(timeout=3)  # Set timeout to 3 seconds
    return result


def search_niraj_on_google(
        query_dir_path = "../Data/Queries/", 
        url_file_path = '../Data/urls.txt', 
        verbose = False, 
        ):
    """
    # Japanese language.
    Functions called: search_with_timeout, 
    """
    file_list = os.listdir(query_dir_path)

    url_data = []
    for filename in file_list:
        if filename.endswith(".txt"):
            file_path = os.path.join(query_dir_path, filename)
            if verbose: print(file_path)
            
            with open(file_path, "r") as file:
                lines = file.readlines()
            num_results = 20

            # To get more Japanese URLs
            if filename == 'queries_ja.txt':
                num_results = 300

            queries = []
            for line in lines:
                query = line.strip()
                queries.append(query)

            total_urls = []
            for query in queries:
                # print("Current query:", query)

                urls = search_with_timeout(query,num_results)
                if urls is None:
                    # print("Function call took more than 3 seconds. Terminating iteration.")
                    continue
                
                total_urls.append(urls)
                # print(len(total_urls))
            url_data.append(total_urls)
            # print(len(url_data))
    with open(url_file_path, 'w') as file:
        file.write(str(url_data))
    return url_data


