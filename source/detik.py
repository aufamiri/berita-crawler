from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

from newsBase import NewsBaseSrc


class Detik(NewsBaseSrc):
    def __init__(self, urls):
        self.visited_urls = []
        self.urls_to_download = []
        self.urls_to_visit = urls
        self.result_text_array = []

    def download_url(self, url):
        return requests.get(url).text

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all(class_="media__title"):

            # Get only the completed news (no video, no "round-up")
            if link.find_previous_sibling(class_="media__subtitle"):
                continue

            for item in link.find_all("a"):
                path = item.get('href')
                # print(path)

                if path and path.startswith('/'):
                    path = urljoin(url, path)
                yield path

    def add_url_to_visit(self, url):
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_download.append(url)

    def crawl(self, url):
        html = self.download_url(url)
        for url in self.get_linked_urls(url, html):
            self.add_url_to_visit(url)

    def get_content(self, url):
        html = self.download_url(url)
        soup = BeautifulSoup(html, 'html.parser')
        source = soup.find_all(class_="itp_bodycontent")

        result_text = ""

        for text in source[0].find_all("p"):
            result_text = result_text + text.get_text()

        self.result_text_array.append(result_text)

    def run(self, target_total, initial_run=1):
        # List All Urls
        page = initial_run
        while target_total >= len(self.urls_to_download):
            url = self.urls_to_visit + "/" + str(page)
            print(f'Crawling: {url}')
            self.crawl(url)
            page += 1

        # Download and Parse from URL
        print(f'Found Total Link: {len(self.urls_to_download)}')
        for link in self.urls_to_download:
            self.get_content(link)


if __name__ == '__main__':
    Detik(urls="https://news.detik.com/indeks").run(100)
