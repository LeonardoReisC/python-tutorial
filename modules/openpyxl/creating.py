# used to manipulate spreadsheets
from pathlib import Path

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

ROOT = Path(__file__).parent
WORKBOOK = ROOT / 'workbook.xlsx'

workbook = Workbook()

sheet_name = 'My Sheet'
workbook.create_sheet(sheet_name, 0)  # creates another sheet
worksheet: Worksheet = workbook[sheet_name]

workbook.remove(workbook['Sheet'])  # removes default sheet


# setting up headers
worksheet.cell(1, 1, 'Name')
worksheet.cell(1, 2, 'Age')
worksheet.cell(1, 3, 'Mark')

students = [
    ['Leonardo', 20, 8.8],
    ['Fernando', 20, 8.5],
    ['Pedro', 19, 9.0],
]

for student in students:
    worksheet.append(student)

workbook.save(WORKBOOK)