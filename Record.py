class Record:

    def __init__(self, name, lastYear, firstYear, monthQuarterYear, releasedYear, releaseMQY, total):
        self.name = name
        self.lastYear = lastYear
        self.firstYear = firstYear
        self.monthQuarterYear = monthQuarterYear
        self.releasedYear = releasedYear
        self.releaseMQY = releaseMQY
        self.total = total

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_lastYear(self):
        return self.lastYear

    def set_lastYear(self, lastYear):
        self.lastYear = lastYear

    def get_firstYear(self):
        return self.firstYear

    def set_firstYear(self, firstYear):
        self.firstYear = firstYear

    def get_monthQuarterYear(self):
        return self.monthQuarterYear

    def set_monthQuarterYear(self, monthQuarterYear):
        self.monthQuarterYear = monthQuarterYear

    def get_releasedYear(self):
        return self.releasedYear

    def set_releasedYear(self, releasedYear):
        self.releasedYear = releasedYear

    def get_releaseMQY(self):
        return self.releaseMQY

    def set_releaseMQY(self, releaseMQY):
        self.releaseMQY

    def get_total(self):
        return self.total

    def set_total(self, total):
        self.total = total

    # name = property(get_name , set_name)
    # lastYear = property(get_lastYear, set_lastYear)
    # firstYear = property(get_firstYear, set_firstYear)
    # monthQuarterYear = property(get_monthQuarterYear, set_monthQuarterYear)
    # releasedYear = property(get_releasedYear, set_releasedYear)
    # releaseMQY = property(get_releaseMQY, set_releaseMQY)
    # total = property(get_total, set_total)


# r = Record("star wars", 2019, 1977, ["Q1", "Q2"], 1977, "Q1", 234000000)

