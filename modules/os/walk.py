# walks recursive trough each directory
import os
from itertools import count

path = os.path.join("D:/OneDrive/Progs", "GitHub", "python", "modules")

counter = count()
for root, dirs, files in os.walk(path):
    the_counter = next(counter)
    print(f"{the_counter} Root: {root}")

    for dir in dirs:
        print(f"    {the_counter} Dir: {dir}")

    for file in files:
        print(f"    {the_counter} FILE: {file}")