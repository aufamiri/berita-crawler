from abc import ABC, abstractmethod


class NewsBaseSrc(ABC):

    @abstractmethod
    def download_url(self, url):
        pass

    @abstractmethod
    def get_linked_urls(self, url, html):
        pass

    @abstractmethod
    def get_content(self, url):
        pass

    @abstractmethod
    def run(self, url="", target_total=100, initial_run=1, start_date=None, end_date=None):
        pass
