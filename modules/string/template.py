import string
import locale
from datetime import datetime
from pathlib import Path

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')


def convert_to_brl(value: float):
    brl = 'R$ ' + locale.currency(value, symbol=False, grouping=True)
    return brl


FILE_PATH = Path(__file__).parent / 'text.txt'

date = datetime(2023, 8, 11)
data = {
    'name': 'Leonardo',
    'value': convert_to_brl(1_234_456),
    'date': date.strftime("%d/%m/%Y"),
    'company': 'L. R.',
    'telephone': '+55 35 99935-6022'
}
with open(FILE_PATH, 'r') as file:
    text = file.read()
    template = string.Template(text)
    print(template.substitute(data))