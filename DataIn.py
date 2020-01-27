
class DataIn:

    def __init__(self, names, urls, release, totals):
        self.names = names
        self.urls = urls
        self.release = release
        self.totals = totals


    def getNames(self):
        return self.names

    def getUrls(self):
        return self.urls

    def getRelease(self):
        return self.release

    def getTotals(self):
        return  self.totals
