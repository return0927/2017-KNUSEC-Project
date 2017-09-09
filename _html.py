import codecs


class HTML():
    def getFile(self, filename):
        return codecs.open(self.base_Dir+filename, "r", encoding="UTF-8").read()

    def __init__(self):
        self.base_Dir = "./html/"
        self.index = self.getFile("index.html")