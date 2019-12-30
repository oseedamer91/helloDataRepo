from openpyxl import Workbook


# basic excel operations

class ExcelWriter:

    def __init__(self, excelFileName):
        self.excelName = excelFileName
        self.workbook = Workbook()
        self.sheet = self.workbook.active

    def excelWriterCell(self, column, row, value):
        self.sheet[str(column) + str(row)] = value

    def excelSave(self):
        self.workbook.save(self.excelName)
