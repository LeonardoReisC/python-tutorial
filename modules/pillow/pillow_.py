from pathlib import Path

from PIL import Image

ROOT = Path(__file__).parent
ORIGINAL_IMAGE = ROOT / 'nala.jpeg'
NEW_IMAGE = ROOT / 'nala_new.jpeg'

pil_image = Image.open(ORIGINAL_IMAGE)

width, height = pil_image.size
exif = pil_image.info['exif']

new_width = 768
new_height = round(height * new_width / width)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    exif=exif,
)
