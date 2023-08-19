# sqlite: used to store simple data without many connections
# bindings(?): used to avoid sql injections

import sqlite3

from env import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# clears the table
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

#  resets the id's sequence
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)

# creating table
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

connection.commit()

# populating the database
sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES '
    '(?, ?)'
)
cursor.executemany(
    sql,
    [
        ('Leonardo', 68),
        ('Fernando', 85),
    ]
)  # fills '?' with parameters

connection.commit()

cursor.close()
connection.close()
