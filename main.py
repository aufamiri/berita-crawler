from source.detik import Detik
from dest.toCsv import toCSV


def run():
    result = Detik().run(target_total=5)
    result.append()
    toCSV().write(result, result_files="test.csv")


if __name__ == '__main__':
    run()
