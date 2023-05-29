from itertools import groupby

students = [
    {"nome": "Leonardo", "mark": "A"},
    {"nome": "Fernando", "mark": "A"},
    {"nome": "Iago", "mark": "D"},
    {"nome": "Vânia", "mark": "A"},
    {"nome": "Pedro", "mark": "B"},
    {"nome": "Pedro", "mark": "D"},
    {"nome": "João", "mark": "C"},
]


def sort_(item):
    return item["mark"]


students.sort(key=sort_)
grouped_students = groupby(students, key=sort_)

for key, students in grouped_students:
    print(key)
    for student in students:
        print(student)
    print()
