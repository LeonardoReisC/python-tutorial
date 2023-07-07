# must implement __enter__ and __exit__ to use 'with'
from pathlib import Path

FILE_PATH = Path(__file__).parent / 'context_manager.txt'


class MyOpen:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self._file = None

    def __enter__(self):
        print("Opening file")
        self._file = open(self.file_path, self.mode, encoding='utf-8')
        return self._file

    def __exit__(self, class_exception, exception, traceback):  # must have these parameters
        print("Closing file")
        self._file.close()

        exception.add_note("My note")


with MyOpen(FILE_PATH, 'w') as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n", 123)
    print("with", file)  # gets the __enter__ return
