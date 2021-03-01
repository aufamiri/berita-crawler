from .newsBase import NewsBaseSrc


class Liputan6(NewsBaseSrc):
    def parse_url(self, url, date, page):
        return url + "/" + \
            date.strftime("%Y/%m/%d") + "?page=" + str(page)

    def get_default_url(self):
        return "https://www.liputan6.com/indeks"
    """
    <article ... data-type="Article">
        ...
        <h4>
            <a href=...>
        </h4>
        ...
    </article>
    """

    def get_linked_urls(self, url):
        html = self.download_url(url)
        soup = self.make_soup(html)
        for link in soup.find_all("article", attrs={"data-type": "Article"}):

            for item in link.find_all("h4"):

                path = item.find("a").get('href')
                yield path

    def get_content(self, url):
        html = self.download_url(url)
        soup = self.make_soup(html)
        source = soup.find_all(class_="itp_bodycontent")

        print(f'download URL : {url}')

        result_text = ""

        for text in source[0].find_all("p"):

            # skpping on editorial notes and video promote
            if (text.find("strong")):
                continue

            result_text = result_text + text.get_text()

        return result_text


if __name__ == '__main__':
    result = Liputan6().run()

    print(result)
