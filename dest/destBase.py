from abc import ABC, abstractmethod


class NewsBaseDest(ABC):
    # write the listNews array to destination file type
    @abstractmethod
    def write(self, listNews, valid=True, result_files="output.csv"):
        pass

    def validString(self, valid=True):
        if(valid):
            return "Valid"
        else:
            return "Hoax"
