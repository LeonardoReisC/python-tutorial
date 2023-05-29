import json
import os
from pprint import pprint

person = {
    'name': 'Leonardo',
    'surname': 'Reis',
    'age': 20,
    'height': 1.70,
    'favorite_colors': ('purple', 'black'),
    'dev': True,
    'nothing': None
}

with open('person.json', 'w', encoding='utf-8') as file:
    json.dump(person, file, indent=2)

with open('person.json', 'r', encoding='utf-8') as file:
    person = json.load(file)
    pprint(person)

os.remove('person.json')
