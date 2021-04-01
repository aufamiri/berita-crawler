import re

from .newsBase import NewsBaseSrc
from .newsResult import NewsResult


class Kompas(NewsBaseSrc):
    def parse_url(self, url, date, page):
        return url + "/?site=news&date=" + date.strftime("%Y-%m-%d") + "&page=" + str(page)

    def get_default_url(self):
        return "https://indeks.kompas.com"
    """
    <a class="article_link" href="..."></a>
    """

    def get_linked_urls(self, url):
        html = self.download_url(url)
        soup = self.make_soup(html)
        for link in soup.find_all("a", attrs={"class": "article__link"}):
            path = link.get('href')
            yield path

    """
    --TITLE--
    <h1 class="read__title>...</h1>
    
    --CONTENT--
    <div class="read__content">
        <p>...</p>
        <p>...</p>
        <p>...</p>
    </div>
    """

    def get_content(self, url):
        html = self.download_url(url + "?page=all")
        soup = self.make_soup(html)
        result_text = ""

        title = soup.find(
            "h1", attrs={'class': 'read__title'}).get_text().strip()

        content = soup.find("div", class_="read__content")
        for text in content.find_all("p"):
            # skpping on editorial notes and promote
            if (text.find("strong")):
                if(not re.search("^(.*?)KOMPAS(.*?)-", text.get_text())):
                    continue

            # remove infgrafis information....
            if(text.find("span")):
                continue

            result_text = result_text + text.get_text()

        # remove XXXX,KOMPAS.com - at the start of article
        result_text = re.sub("^(.*?)KOMPAS(.*?)-", "", result_text)

        return NewsResult(url, title, result_text)


if __name__ == '__main__':
    # result = Kompas().run(target_total=20)
    result = Kompas().get_content(
        # "https://www.kompas.com/global/read/2021/02/28/235005770/cerita-najbullah-jual-ginjal-demi-uang-nikah-agar-keluarganya-tak-dibunuh")
        # "https://nasional.kompas.com/read/2019/04/18/19403311/setelah-deklarasi-klaim-kemenangan-apa-agenda-prabowo")
        # "https://megapolitan.kompas.com/read/2019/04/18/21052501/5500-personel-dikerahkan-amankan-ibadah-tri-hari-suci-di-jakarta")
        "https://nasional.kompas.com/read/2019/04/18/20485951/perolehan-suara-turun-di-hitung-cepat-sementara-ini-respons-demokrat")
    # "https://regional.kompas.com/read/2019/04/18/21094291/nu-jatim-imbau-warganya-tak-percaya-klaim-kemenangan-capres")
    # result = Liputan6().get_content(
    #     "https://www.liputan6.com/news/read/4495081/tim-pengkaji-uu-ite-minta-masukan-ade-armando-hingga-ahmad-dhani")

    # print(result)
