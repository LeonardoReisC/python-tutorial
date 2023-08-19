import os
import dotenv
import pymysql

dotenv.load_dotenv()

TABLE_NAME = 'Customers'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with connection:
    with connection.cursor() as cursor:
        query = (
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        cursor.execute(query)
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')

    # CREATE
    with connection.cursor() as cursor:
        query = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%s, %s) '  # avoids sql injection
        )

        data1 = (
            ("Leonardo", 20),
            ("Fernando", 19),
        )

        cursor.executemany(query, data1)
    connection.commit()

    # using dictionary
    with connection.cursor() as cursor:
        query = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%(name)s, %(age)s) '  # avoids sql injection
        )

        data2 = (
            {'name': 'Pedro', 'age': 19},
            {'name': 'Yuri', 'age': 20},
        )

        cursor.executemany(query, data2)
    connection.commit()

    # READ
    with connection.cursor() as cursor:
        query = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE name LIKE %s '
        )

        cursor.execute(query, '%do')

        data3 = cursor.fetchall()
        if __name__ == '__main__':
            print(data3)

    # UPDATE
    with connection.cursor() as cursor:
        query = (
            f'UPDATE {TABLE_NAME} '
            'SET age = %s '
            'WHERE name = %s '
        )

        cursor.execute(query, (20, 'Fernando'))
    connection.commit()

    # DELETE
    with connection.cursor() as cursor:
        query = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE name NOT LIKE %s '
        )

        cursor.execute(query, ('%do',))
    connection.commit()