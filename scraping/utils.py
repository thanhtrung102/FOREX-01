from bs4 import BeautifulSoup
import cloudscraper


def get_soup_from_file(fn):
    filepath = f"./scraping/mock_files/{fn}.html"
    with open(filepath, "r", encoding='utf-8') as file:
        data = file.read()
    return BeautifulSoup(data, "html.parser")


def get_soup_from_url(url, verb="get", data=None, extra_headers=None):

    s = cloudscraper.create_scraper()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
    }

    if extra_headers:
        headers.update(extra_headers)

    if verb == 'get':
        resp = s.get(url, data=data, headers=headers)
    elif verb == 'post':
        resp = s.post(url, data=data, headers=headers)

    return BeautifulSoup(resp.content, "html.parser")