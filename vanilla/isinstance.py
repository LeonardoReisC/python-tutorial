# isinstance - checks the existence of a certain object type
list_ = ['a', 1, 2.0, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Leo'}]

for item in list_:
    if isinstance(item, bool):
        item = not item
    elif isinstance(item, set):
        item.add(2)
    elif isinstance(item, (int, float)):
        item **= 2
    elif isinstance(item, str):
        item = item.upper()

    print(item, end=" ")
