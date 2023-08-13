"""
    NFKD - Normalization Form Compatibility Composition
    - keeps the compatible combining caracters form by canonical equivalence
"""
import unicodedata

name = '\u1e9b\u0323'
name_normalized = unicodedata.normalize('NFKD', name)
print(['U+' + hex(ord(letra))[2:].zfill(4).upper()
       for letra in name_normalized])
print('     \u0073       \u0323       \u0307', end='\n\n')
print(name, '->', '\u0073 \u0323 \u0307')
