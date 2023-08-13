"""
    NFC - Normalization Form Canonical Composition
    - keeps the caracters precomposed form
"""
import unicodedata

name = 'L\u0065\u0301o'
name_normalized = unicodedata.normalize('NFC', name)
print(name_normalized)
print(['U+' + hex(ord(letra))[2:].zfill(4).upper()
       for letra in name_normalized])
print("    L         é         o")
