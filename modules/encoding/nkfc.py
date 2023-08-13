"""
    NFKC - Normalization Form Compatibility Decomposition
    - keeps the compatible caracters precomposed form by canonical equivalence
"""
import unicodedata

name = '\u1e9b\u0323'
name_normalized = unicodedata.normalize('NFKC', name)
print(['U+' + hex(ord(letra))[2:].zfill(4).upper()
       for letra in name_normalized])
print('     ṩ', end='\n\n')
print(name, '->', name_normalized)
