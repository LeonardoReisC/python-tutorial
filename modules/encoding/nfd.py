"""
    NFD - Normalization Form Decomposition
    - keeps the combining caracters form
"""
import unicodedata

name = 'L\u00e9o'
name_normalized = unicodedata.normalize('NFD', name)
print(name_normalized)
print(['U+' + hex(ord(letra))[2:].zfill(4).upper()
       for letra in name_normalized])
print("    L         e         acute         o")