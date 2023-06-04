import json
import os

FILE_PATH = "person.json"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Leonardo", 20)
person2 = Person("Fernando", 19)
person3 = Person("Vânia", 56)
people = [person1.__dict__, person2.__dict__, person3.__dict__]

with open(FILE_PATH, 'w', encoding='utf-8') as file:
    json.dump(people, file, indent=2)

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    people = json.load(file)

mom = Person(**people[2])
print(mom.__dict__)

os.remove(FILE_PATH)  # to see the file content, comment this line
