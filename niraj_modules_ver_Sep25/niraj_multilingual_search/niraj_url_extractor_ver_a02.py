
import re
from urllib.parse import urlparse, urlunparse
import json






def extract_urls_from_file(url_file_path = '../Data/urls.txt'):
    def extract_url(line):
        return re.findall(r'https://\S+', line)
    with open(url_file_path, 'r') as file:
        total_urls = []
        for line_number, line in enumerate(file, start=1):
            urls = extract_url(line)
            total_urls.append(urls)
    return total_urls


def save_niraj_unique_urls(
        url_file_path = '../Data/urls.txt', 
        unique_file_path = '../Data/unq_urls.json', 
        ):
    url_list = extract_urls_from_file(url_file_path)
    base_domains = []
    media_keywords = [
        "news", "media", "video", "article", "gallery", "photo",
        "story", "podcast", "press", "interview", "report", "feature",
        "headline", "coverage", "review", "analysis", "opinion",
        "update", "live", "event", "broadcast", "archive", "showcase",
        "exclusive", "press-release", "special-report", "interviews",
        "multimedia", "infographic", "newsletter", "recap", "result", 
        "blog", "document", "pdf"
    ]
    data = []
    for inner_list in url_list:
        # print(inner_list)
        inner_base_domains = []
        for url in inner_list:
            # print(url)
            url_lower = url.lower()
            # print("URL: ", url_lower)
            url_category = "NonMedia"
            for keyword in media_keywords:
                if keyword in url_lower:
                    url_category = "Media"
                    break
                    # print(url)
                    
            try:
                parsed_url = urlparse(url)
            except Exception as e:
                continue
            # print(parsed_url)

            base_domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
            country = "country"
            domain = "domain"
            item = {"url": base_domain, "country": country, "domain": domain, "category": url_category}

            # No duplicates
            if item not in data:
                data.append(item)
    with open(unique_file_path, 'w') as f:
        json.dump(data, f, indent=4)
    return data
