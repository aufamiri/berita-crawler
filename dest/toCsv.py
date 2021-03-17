import csv
from .destBase import NewsBaseDest


class toCSV(NewsBaseDest):
    def write(self, listNews, valid=True, result_files="output.csv"):
        with open(result_files, "w", newline="") as file:
            mywriter = csv.writer(file, delimiter=",")
            mywriter.writerow(["url", "judul", "berita", "tagging"])

            for data in listNews:
                mywriter.writerow(
                    [data.url, data.title, data.content, self.validString(valid)])
