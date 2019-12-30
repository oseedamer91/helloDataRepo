from array import *


# 3 possible format for excel
# year months
# year quarters
# year by year
# basic data calculation

class Util:

    def __init__(self):
        pass

    def calculateDeltaByStartMonth(self, amountOfMonthsOrQuartersOrYear, startMonthOrQuarter, total):
        delta = total / (len(amountOfMonthsOrQuartersOrYear)-amountOfMonthsOrQuartersOrYear.get(startMonthOrQuarter))
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
        noValues = [0] * 12

        numOfYears = lastYear - firstYear
        firstMonth = "January"

        deltaOne = self.calculateDeltaByStartMonth(months, releaseMonth, total)
        deltaTwo = self.calculateDeltaByStartMonth(months, firstMonth, total)

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
    def calculateCurrentValuesQuarters(self, lastYear, firstYear, monthQuarterYear, releasedYear, releaseMQY, total):
        detaOne = self.calculateDeltaByStartMonth(monthQuarterYear,releaseMQY, total)



    def calculateCurrentValuesYearly(self, lastYear, firstYear, total):
        numOfYears = lastYear - firstYear
        # write y = f(x)
        # Avatar	2009    $2,788
