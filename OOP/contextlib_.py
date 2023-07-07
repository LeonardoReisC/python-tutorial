# creates a Context Manager using a decorator
from contextlib import contextmanager
from pathlib import Path

FILE_PATH = Path(__file__).parent / 'contextlib.txt'

@contextmanager
def my_open(file_path, mode):
    try:
        print("Opening file")
        file = open(file_path, mode, encoding='utf8')
        yield file
    except Exception as e:
        print("An error has occurred:", e)
    finally:
        print("Closing file")
        file.close()

with my_open(FILE_PATH, 'w') as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")
    print("with", file)