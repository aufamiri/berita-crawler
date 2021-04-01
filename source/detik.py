import re

from .newsBase import NewsBaseSrc
from .newsResult import NewsResult


class Detik(NewsBaseSrc):
    def parse_url(self, url, date, page):
        return url + "/" + \
            str(page) + "?date=" + date.strftime("%m/%d/%Y")

    def get_default_url(self):
        return "https://news.detik.com/indeks"

    def get_linked_urls(self, url):
        html = self.download_url(url)
        soup = self.make_soup(html)
        for link in soup.find_all(class_="media__title"):

            # Get only the completed news (no video, no "round-up")
            if link.find_previous_sibling(class_="media__subtitle"):
                continue

            for item in link.find_all("a"):
                path = item.get('href')

                # there is some /detiktv/ link without media__subtitle
                # and the intermeso page is sooooo different, I'd rather skip it
                if (re.search('/detiktv/|/intermeso/', path)):
                    continue
                # print(path)

                yield path

    def get_content(self, url):
        # show all of the article (no pagination)
        html = self.download_url(url + "?single=1")
        soup = self.make_soup(html)
        title = soup.find(
            "h1", attrs={'class': 'detail__title'}).get_text().strip()

        source = soup.find(class_="detail__body-text")

        result_text = ""

        for text in source.find_all("p"):

            # skpping on editorial notes and video promote
            if (text.find("strong")):
                continue

            # skipping video promote
            if(text.find("a", class_='embed')):
                continue

            result_text = result_text + text.get_text()

        return NewsResult(url, title, result_text)


if __name__ == '__main__':
    result = Detik().get_content(
        "https://news.detik.com/berita/d-4153225/koalisi-jokowi-akan-minta-masukan-ormas-keagamaan-termasuk-fpi")
    # "https://news.detik.com/berita/d-4152912/gempa-56-sr-guncang-sumba-barat-tak-berpotensi-tsunami")

    # result = Detik().run(target_total=20)

    print(result.content)
