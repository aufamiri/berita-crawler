from .toCsv import toCSV
from .destBase import NewsBaseDest

availableDst = {
    "csv": toCSV()
}


def init(dest, content, name_files="result.csv"):
    destClass: NewsBaseDest = availableDst.get(dest, "csv")

    destClass.write(content, result_files=name_files)
