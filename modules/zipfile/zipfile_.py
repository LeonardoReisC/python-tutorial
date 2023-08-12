import os
import shutil
from pathlib import Path

from zipfile import ZipFile

# Paths
ROOT = Path(__file__).parent
ZIP_DIR = ROOT / 'zip_dir'
ZIPPED = ROOT / 'zipped.zip'
UNZIPPED = ROOT / 'unzipped.zip'

shutil.rmtree(ZIP_DIR, ignore_errors=True)
Path.unlink(ZIPPED, missing_ok=True)
shutil.rmtree(str(ZIPPED).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(UNZIPPED, ignore_errors=True)

# creates the directory
ZIP_DIR.mkdir(exist_ok=True)


def create_files(qty: int, zip_dir: Path):
    for i in range(qty):
        text = f'file_{i}'
        with open(zip_dir / f'{text}.txt', 'w') as file:
            file.write(text)


create_files(10, ZIP_DIR)

with ZipFile(ZIPPED, 'w') as zip:
    for root, dirs, files in os.walk(ZIP_DIR):
        for file in files:
            zip.write(os.path.join(root, file), file)

with ZipFile(ZIPPED, 'r') as zip:
    for file in zip.namelist():
        print(file)

# unzip
with ZipFile(ZIPPED, 'r') as zip:
    zip.extractall(UNZIPPED)