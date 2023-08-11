"""
    json: allows object serialization of a simple text

    Data Types
    - Number: int or float
    - String: between ""
    - Boolean
    - Arrays: between []
    - Objects: set of {"key": value,}
    - null: none
"""
import json

string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

movie = json.loads(string_json)  # dict
print(movie)
print()

print(json.dumps(movie, ensure_ascii=False, indent=2))
