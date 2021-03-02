import re

from .newsBase import NewsBaseSrc
from .newsResult import newsResult


class Tempo(NewsBaseSrc):
    def parse_url(self, url, date, page):
        return url + "/" + date.strftime("%Y/%m/%d") + "/nasional"

    def get_default_url(self):
        return "https://www.tempo.co/indeks"
    """
    <li><a href="..."></a></li>
    <li><a href="..."></a></li>
    <li><a href="..."></a></li>
    ...
    """

    def get_linked_urls(self, url):
        html = self.download_url(url)
        soup = self.make_soup(html)
        content = soup.find('ul', attrs={'class': 'wrapper'})

        for link in content.find_all("li"):
            item = link.find("a")
            path = item.get('href')

            yield path

    """
    <div id="isi">
        <p>...</p>
        <p>...</p>
        <p>...</p>

        --OPTIONAL--
        <div class="paging">
            <a href="..."></a>
        </div>
    </div>
    """

    def get_content(self, url):
        html = self.download_url(url)
        soup = self.make_soup(html)
        result_text = ""
        pages_link = [url]

        title = soup.find(
            "h1", attrs={'itemprop': 'headline'}).get_text().strip()

        paging = soup.find("div", attrs={'class': 'paging'})

        # get all of article page url(if any)
        if(paging):
            for link in paging.find_all("a"):
                temp_link = link.get("href")

                # avoid duplicate pages
                if(temp_link not in pages_link):
                    pages_link.append(temp_link)

        for item in pages_link:
            html = self.download_url(item)
            soup = self.make_soup(html)

            content = soup.find("div", attrs={'id': 'isi'})

            for text in content.find_all("p"):

                # skpping on editorial notes and video promote
                if (text.find("strong")):
                    continue

                if(text.find("div", {"class": "paging"})):
                    continue

                result_text = result_text + text.get_text()

        print(title)
        print()

        return newsResult(url, title, result_text)


if __name__ == '__main__':
    # result = Tempo().run(target_total=20)

    # result = Tempo().get_content("https://otomotif.tempo.co/read/1436739/pabrik-tesla-di-as-sempat-tutup-karena-kekurangan-onderdil-elon-musk-bicara")
    result = Tempo().get_content(
        "https://nasional.tempo.co/read/1437826/setahun-pandemi-ini-15-pejabat-yang-pernah-positif-corona/full&view=ok")

    # print(result)
