#
# from array import *
#
# # 3 possible format for excel
# # year months
# # year quarters
# # year by year
#
# class Util:
#
#     def calculateDeltaByStartMonth(self, months, startMonth, total):
#         delta = total / (len(months) - months.get(startMonth))
#         return delta
#
#     #given last and first year , calculate the current values Jan , Feb ,...
#     def calculateCurrentValuesMonths(self,name , lastYear ,firstYear, releaseYear, releaseMonth , total):
#         months = {
#             'January': 1,
#             'February': 2,
#             'March': 3,
#             'April': 4,
#             'May':5,
#             'June':6,
#             'July':7,
#             'August':8,
#             'September':9,
#             'October':10,
#             'November':11,
#             'December':12
#         };
#
#         values = {}
#         noValues = [0]*12
#
#         numOfYears = lastYear - firstYear
#         yearCount = 1
#
#         delta = self.calculateDeltaByStartMonth(months,releaseMonth,total)
#
#         for year in range(firstYear,lastYear):
#             if year == releaseYear:
#                 monthsValues=[]
#                 lastMonthValue=0
#                 for month in months.keys():
#                     if month >= releaseMonth:
#                         currentVal = currentVal + delta
#                         monthsValues.append(currentVal)
#                     if month < releaseMonth:
#                         monthsValues.append(0)
#              elif year > releaseYear:
#                 monthsValues = []
#                 for month in months.keys():
#                     currentVal = currentVal + delta
#                     monthsValues.append(currentVal)
#             # year not reached yet!
#             else:
#                 monthsValues = noValues
#
#             values[year] = monthsValues
#
#
#
#
#
#     # given last and first year , calculate the current values Q1 Q2 Q3 Q4
#     def calculateCurrentValuesQuarters(self, lastYear, firstYear, total):
#         quarters = ['Q1','Q2','Q3', 'Q4'];
#         numOfYears = lastYear - firstYear
#         # write y = f(x)
#         # Avatar	2009    $2,788
#
#         # given last and first year , calculate the current values Year1, Year2 ,....
#     def calculateCurrentValuesYearly(self, lastYear, firstYear, total):
#         numOfYears = lastYear - firstYear
#         # write y = f(x)
#         # Avatar	2009    $2,788