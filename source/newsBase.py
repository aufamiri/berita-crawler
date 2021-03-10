from abc import ABC, abstractmethod
import requests
import datetime
from bs4 import BeautifulSoup


class NewsBaseSrc(ABC):
    # get all the article links from indeks
    @abstractmethod
    def get_linked_urls(self, url):
        pass

    # get the article content and return it as string
    @abstractmethod
    def get_content(self, url):
        pass

    # return the indeks url
    @abstractmethod
    def parse_url(self, url, date, page):
        pass

    # get default url
    @abstractmethod
    def get_default_url(self):
        pass

    # return bs4 objects,
    # if the need to change the parser arise,
    # we just need to change this
    def make_soup(self, html):
        return BeautifulSoup(html, "html.parser")

    # request the page and return it as strings
    def download_url(self, url):
        return requests.get(url).text

    def run(self, site_url=None, target_total=100, initial_run=1, start_date=datetime.datetime.now(), end_date=datetime.datetime.now()):
        page = initial_run
        date = start_date

        prev_download = 0
        urls_to_download = []
        result_text_array = []

        if (site_url is None):
            site_url = self.get_default_url()

        # Search for article url until target is fullfilled
        # OR
        # {date} > {end_date}
        while target_total >= len(urls_to_download):
            url = self.parse_url(site_url, date, page)
            print(f'Crawling: {url}')

            added_data = list(self.get_linked_urls(url))

            urls_to_download.extend(added_data)

            print(f'Found New {len(added_data)} link')
            page += 1

            # change day if no more news is found
            if (len(added_data) == 0):
                # break on {date} passing the dateRange
                if(date >= end_date):
                    break

                date = date + datetime.timedelta(1)
                page = 1

        # limiting link total to target_total
        if (target_total < len(urls_to_download)):
            del urls_to_download[target_total: len(urls_to_download)]

        # Download and Parse from URL
        print(f'Found Total Link: {len(urls_to_download)}')
        for link in urls_to_download:
            print(f'Downloading : {link}')
            result = self.get_content(link)
            result_text_array.append(result)

        return result_text_array
