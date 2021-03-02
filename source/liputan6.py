import re

from .newsBase import NewsBaseSrc
from .newsResult import NewsResult


class Liputan6(NewsBaseSrc):
    def parse_url(self, url, date, page):
        return url + "/" + \
            date.strftime("%Y/%m/%d") + "?page=" + str(page)

    def get_default_url(self):
        return "https://www.liputan6.com/indeks"
    """
    <article ... data-type="Article">
        <header>
            ...
            <h4>
                <a href=...>
            </h4>
            ...
        </header>
    </article>
    """

    def get_linked_urls(self, url):
        html = self.download_url(url)
        soup = self.make_soup(html)
        for link in soup.find_all("article", attrs={"data-type": "Article"}):

            for item in link.find_all("h4"):

                path = item.find("a").get('href')
                yield path

    """
    <div class="... article-content-body__item-content">
        <p>...</p>
        <p>...</p>
        <p class="baca-juga__header">...</p> #WE DON'T WANT THIS
        <p>...</p>
    </div>
    """

    def get_content(self, url):
        html = self.download_url(url)
        soup = self.make_soup(html)
        result_text = ""

        title = soup.find(
            "h1", attrs={'itemprop': 'headline'}).get_text().strip()

        for link in soup.find_all(class_="article-content-body__item-content"):
            for text in link.find_all("p"):

                # Delete Preamble (i.e Liputan6.com, Jakarta -)
                try:
                    text.b.decompose()
                except:
                    pass
                # print(text)

                # skpping on editorial notes and video promote
                if (text.find("strong")):
                    continue

                try:
                    if("baca-juga__header" in text["class"]):
                        continue
                except:
                    pass

                result_text = result_text + text.get_text()

        # print(result_text)
        return NewsResult(url, title, result_text)


if __name__ == '__main__':
    # result = Liputan6().run(target_total=20)
    result = Liputan6().get_content(
        "https://www.liputan6.com/news/read/4495081/tim-pengkaji-uu-ite-minta-masukan-ade-armando-hingga-ahmad-dhani")

    # print(result)
