from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter, PdfMerger

ROOT = Path(__file__).parent
ORIGINAL_PDFS = Path(__file__).parent / 'original'
NEW_PDFS = Path(__file__).parent / 'new'

REPORT_BACEN = ORIGINAL_PDFS / 'R20230210.pdf'

NEW_PDFS.mkdir(exist_ok=True)

# read pdf
reader = PdfReader(REPORT_BACEN)

page0 = reader.pages[0]
print(page0.extract_text(), end='\n\n')

image0 = page0.images[0]

with open(NEW_PDFS / image0.name, 'wb') as fp:
    fp.write(image0.data)

# write pdf
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)

    with open(NEW_PDFS / f'page{i}.pdf', 'wb') as file:

        writer.write(file)

# merge pdfs
files = [
    NEW_PDFS / 'page1.pdf',
    NEW_PDFS / 'page0.pdf',
]

merger = PdfMerger()

for file in files:
    merger.append(file)

with open(NEW_PDFS / 'merged.pdf', 'wb') as file:
    merger.write(file)