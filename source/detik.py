from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import datetime
import re

from .newsBase import NewsBaseSrc


class Detik(NewsBaseSrc):
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

                # there is some /detiktv/ link without media__subtitle
                if (re.search('/detiktv/', path)):
                    continue
                # print(path)

                if path and path.startswith('/'):
                    path = urljoin(url, path)
                yield path

    def crawl(self, url):
        html = self.download_url(url)
        return list(self.get_linked_urls(url, html))

    def get_content(self, url):
        html = self.download_url(url)
        soup = BeautifulSoup(html, 'html.parser')
        source = soup.find_all(class_="itp_bodycontent")get_default_url print(f'download URL : {url}')

        result_text = ""

        for text in source[0].find_all("p"):

            # skpping on editorial notes and video promote
            if (text.find("strong")):
                continue

            result_text = result_text + text.get_text()

        # self.result_text_array.append(result_text)
        return result_text


"""
    def run(self, site_url="https://news.detik.com/indeks", target_total=100, initial_run=1, start_date=datetime.datetime.now(), end_date=datetime.datetime.now()):
        page = initial_run
        date = start_date

        prev_download = 0
        urls_to_download = []
        result_text_array = []

        # List All Urls
        while target_total >= len(urls_to_download):
            print(len(urls_to_download))

            url = site_url + "/" + \
                str(page) + "?date=" + date.strftime("%m/%d/%Y")
            print(f'Crawling: {url}')
            added_data = self.crawl(url)

            urls_to_download.extend(added_data)
            page += 1

            # change day if no more news is found
            if (len(added_data) == 0):
                if(date >= end_date):
                    break

                date = date + datetime.timedelta(1)
                page = 1

        # Download and Parse from URL
        print(f'Found Total Link: {len(urls_to_download)}')
        for link in urls_to_download:
            result = self.get_content(link)
            result_text_array.append(result)

        return result_text_array
        """


if __name__ == '__main__':
    result = Detik().run("https://news.detik.com/indeks", 100,
                         end_date=datetime.datetime(2021, 2, 27))

    print(result)
