import json
import os

FILENAME = "_.json"
PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        FILENAME
    )
)

movie = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

# dumping json to file
with open(PATH, "wt") as file:
    json.dump(movie, file, ensure_ascii=False, indent=2)

# reading json from file
with open(PATH, "rt") as file:
    movie_json = json.load(file)
    print(movie_json)
