from array import *
from Record import Record
import Months as yearAsParts
import random


# 3 possible format for excel
# year months
# year quarters
# year by year
# basic data calculation

class Util:
    def __init__(self):
        self.titleData = {}
        pass

    # def calculateDeltaByStartMonth(self, amountOfMonthsOrQuartersOrYear, startMonthOrQuarter, total):
    #     delta = total / (len(amountOfMonthsOrQuartersOrYear) - amountOfMonthsOrQuartersOrYear.get(startMonthOrQuarter))
    #     return delta

    def calculateDelta(self, total, isRandom, startIndex=None):
        delta = 0
        start = 0
        stop = 1

        if isRandom:
            r = (random.uniform(start,stop))
            delta = round(total * (r / 100))
        else:
            delta = total / startIndex
        return delta

    # given last and first year , calculate the current values Jan , Feb ,...
    def calculateCurrentValuesMonths(self, name, lastYear, firstYear, releaseYear, releaseMonth, total):
        months = {
            'January': 1,
            'February': 2,
            'March': 3,
            'April': 4,
            'May': 5,
            'June': 6,
            'July': 7,
            'August': 8,
            'September': 9,
            'October': 10,
            'November': 11,
            'December': 12
        }

        values = {}
        noValues = [0] * months["December"]
        numOfYears = lastYear - firstYear
        firstMonth = "January"

        deltaOne = self.calculateDeltaByStartMonth(total, False, releaseMonth)
        deltaTwo = self.calculateDeltaByStartMonth(total, True)

        for year in range(firstYear, lastYear):
            monthsValues = []
            if year == releaseYear:
                lastMonthValue = 0
                for month in months.keys():
                    if month >= releaseMonth:
                        currentVal = currentVal + deltaOne
                        monthsValues.append(currentVal)
                    if month < releaseMonth:
                        monthsValues.append(0)
                lastMonthValue = monthsValues[-1]

            elif year > releaseYear:
                for month in months.keys():
                    lastMonthValue = lastMonthValue + deltaTwo
                    monthsValues.append(lastMonthValue)
            # year not reached yet!
            else:
                monthsValues = noValues

            values[year] = monthsValues

    # given last and first year , calculate the current values Q1 Q2 Q3 Q4
    # monthQuarterYear == number
    # releasedYear == Year
    # releaseMQY == Qi or month or year
    def calculateCurrentValues(self, record):
        informationForCurrentRecord = {}
        name = record.name
        lastYear = record.lastYear + 1
        firstYear = record.firstYear
        monthQuarterYear = record.monthQuarterYear
        releasedYear = record.releasedYear
        releaseMQY = record.releaseMQY
        total = record.total

        firstMQY = 1
        approxTargetForYear = (len(monthQuarterYear) + 1) if len(monthQuarterYear) > 1 else 2
        deltaTwo = self.calculateDelta(total, True)
        deltaOne = self.calculateDelta(total, False, releaseMQY) - round(
            random.uniform(0, approxTargetForYear) * deltaTwo)
        trackLastValue = 0

        for year in range(firstYear, lastYear):
            yearValues = []
            tempValue = 0
            if year == releasedYear:
                for mqy in monthQuarterYear:
                    if mqy == releaseMQY:
                        tempValue += deltaOne
                    elif mqy > releaseMQY:
                        tempValue += deltaTwo
                    else:
                        tempValue = 0
                    yearValues.append(tempValue)
                    trackLastValue = yearValues[-1]
            elif year > releasedYear:
                for mqy in monthQuarterYear:
                    trackLastValue = trackLastValue + deltaTwo
                    yearValues.append(trackLastValue)
            else:
                yearValues = (len(monthQuarterYear) * [0])

            self.titleData[year] = yearValues

        informationForCurrentRecord[name] = self.titleData
        return informationForCurrentRecord


# r = Record("star wars", 1999, 1977, yearAsParts.quarter_indexes, 1977, 1, 1000)
# mydata = Util().calculateCurrentValues(r)

r2 = Record("Avatar",2019,2008,yearAsParts.months_indexes,2009,2,2000000000)
mydata = Util().calculateCurrentValues(r2)

for k in mydata:
    print(str(k) +'\n' + str(mydata[k]))
