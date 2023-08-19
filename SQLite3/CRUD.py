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

query = ''

# CREATE
query = (
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES '
    '(?, ?)'
)

cursor.executemany(
    query,
    [
        ('Leonardo', 68),
        ('Fernando', 85),
        ('Pedro', 65),
        ('João', 70),
        ('Yuri', 70)
    ]
)
connection.commit()

# READ
query = (
    f'SELECT * FROM {TABLE_NAME}'
)
cursor.execute(query)

for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

# UPDATE
query = (
    f'UPDATE {TABLE_NAME} '
    'SET name="Leo" '
    'WHERE id=1'
)
cursor.execute(query)
connection.commit()

# DELETE
query = (
    f'DELETE FROM {TABLE_NAME} '
    'WHERE id=?'
)

cursor.execute(query, ('5',))
connection.commit()

cursor.close()
connection.close()