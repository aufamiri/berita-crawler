import re
import os

from .newsBase import NewsBaseSrc
from .newsResult import NewsResult


class CnnIndo(NewsBaseSrc):
    def parse_url(self, url, date, page):
        return url + "?p=" + str(page) + "&date=" + date.strftime("%Y/%m/%d")

    def get_default_url(self):
        return "https://www.cnnindonesia.com/nasional/indeks/3"
    """
    <article>
        <a href="..." target="_blank"></a>
    </article>
    """

    def get_linked_urls(self, url):
        html = self.download_url(url)
        soup = self.make_soup(html)
        for link in soup.find_all("article"):

            # not all <article> have the targeted link
            try:
                title = link.find("h2", attrs={'class': 'title'})
                if(re.search("VIDEO:", title.get_text().strip())):
                    continue

                item = link.find("a", attrs={'target': '_blank'})
                path = item.get('href')
                print(path)
                yield path
            except:
                pass

    """
    --TITLE--
    <h1 class="title">...</h1>

    --CONTENT--
    <div id="detikdetailtext">
        ....
    </div>
    """

    def get_content(self, url):
        html = self.download_url(url + "?page=all")
        soup = self.make_soup(html)
        result_text = ""

        title = soup.find(
            "h1", attrs={'class': 'title'}).get_text().strip()

        content = soup.find("div", attrs={'id': 'detikdetailtext'})

        try:
            temp_result: String = content.get_text()

            for text in temp_result.splitlines():
                if(re.search("Gambas:", text)):
                    continue

                if(text != ""):
                    text = re.sub("^(.*?)--", "", text)
                    result_text = result_text + text

            # remove meaningless (xxxx/yyyy)
            result_text = (re.sub("\(([^)]+)\)$", "", result_text))

            return NewsResult(url, title, result_text)

        except:
            pass


if __name__ == '__main__':
    # result = CnnIndo().run(target_total=50)
    result = CnnIndo().get_content(
        # "https://www.cnnindonesia.com/nasional/20200530180616-20-508320/10-provinsi-di-indonesia-nihil-kasus-baru-corona-hari-ini")
        "https://www.cnnindonesia.com/nasional/20200530191534-20-508359/polda-jateng-sekat-pemudik-arus-balik-hingga-7-juni")
