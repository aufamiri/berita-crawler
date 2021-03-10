import re

from .newsBase import NewsBaseSrc
from .newsResult import NewsResult

'''
!!!!THIS IS HIGHLY EXPERIMENTAL!!!!

berhubung turnbackhoax adalah user sent konten maka tidak ada bentuk konten yang pasti
ditambah, kita hanya ingin mengambil narasi berita hoax nya saja
untuk saat ini, class ini akan berasumsi bahwa konten akan memiliki layout sebagai berikut :

====
KATEGORI:
....
====
SUMBER:
...
====
NARASI:
...
{lokasi teks berita hoaks yang diinginkan}
====
PENJELASAN:
...
====

langkah yang diambil, adalah :
1. menggunakan regex untuk mengambil NARASI(and some variation of it)
2. apabila regex tersebut ditemukan, akan merubah flag dan 
   akan membuat program menyimpan teks ke variabel

3. menggunakan regex lain, untuk mencari pola "====="
4. apabila ditemukan, hentikan pencarian dan return.
'''


class TurnBackHoax(NewsBaseSrc):
    def parse_url(self, url, _, page):
        return url + "/page/" + str(page) + "/"

    def get_default_url(self):
        return "https://turnbackhoax.id"

    def get_linked_urls(self, url):
        html = self.download_url(url)
        soup = self.make_soup(html)

        for link in soup.find_all("article"):

            author = link.find("a", attrs={"class": "fn"}).get("href")

            # blacklist some people because of improper formatting (lol, sorry)
            if(re.search("xfitrah|aribowo", author)):
                continue

            item = link.find("a", attrs={"rel": "bookmark"})
            path = item.get('href')
            yield path

    def get_content(self, url):
        # show all of the article (no pagination)
        html = self.download_url(url)
        soup = self.make_soup(html)

        isNarasi = False

        # <h1 class="entry-title">...</h1>
        title = soup.find(
            "h1", attrs={'class': 'entry-title'}).get_text().strip()

        '''
        <div class="entry-content">
            ...
            <p>...</p>
            <p>...</p>
            ...
        </div>
        '''
        source = soup.find("div", attrs={"class": "entry-content"})

        result_text = ""

        for text in source.find_all("p"):

            temp_text = text.get_text()

            if(re.search("narasi", temp_text.lower())):
                isNarasi = True
                continue

            if(re.search("==", temp_text.replace(" ", "")) and isNarasi):
                isNarasi = False
                break

            if(isNarasi and not re.search("penjelasan", temp_text.lower())):
                result_text = result_text + temp_text

        print(result_text)
        print()

        return NewsResult(url, title, result_text)


if __name__ == '__main__':
    # result = TurnBackHoax().run(target_total=20)
    result = TurnBackHoax().get_content(
        "https://turnbackhoax.id/2021/03/07/salah-pesan-berantai-video-potensi-bahaya-vaksin-covid-19/")
    # print(result)
