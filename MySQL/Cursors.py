import os
import pymysql.cursors

import CRUD as c

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor
)

with connection:
    with connection.cursor() as cursor:
        query = (
            f'SELECT * FROM {c.TABLE_NAME} '
        )

        cursor.execute(query)

        data = cursor.fetchall()
        print(data)
        cursor.scroll(0, mode='absolute')
        print('rownumber:', cursor.rownumber)

        data = cursor.fetchall()
        print()
        for row in data:
            print(row)

        print('rowcount:', cursor.rowcount)
        print('lasrowid:', cursor.lastrowid)
