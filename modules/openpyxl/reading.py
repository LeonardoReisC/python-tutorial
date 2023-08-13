# used to manipulate spreadsheets
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.cell import Cell
from openpyxl.worksheet.worksheet import Worksheet

ROOT = Path(__file__).parent
WORKBOOK = ROOT / 'workbook.xlsx'

workbook: Workbook = load_workbook(WORKBOOK)

sheet_name = 'My Sheet'

worksheet: Worksheet = workbook[sheet_name]

row: tuple[Cell]
for row in worksheet.iter_rows():
    for cell in row:
        print(cell.value, end='\t')
    print()

# altering the data
worksheet['B4'].value = 20

workbook.save(WORKBOOK)