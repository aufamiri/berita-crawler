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
    def run(self, target_total, initial_run=1):
        pass
