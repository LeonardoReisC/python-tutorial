def show_arguments(*args, **kwargs):
    print('UNAMED ARGUMENTS')
    print(args, '\n', sep='')

    print('NAMED ARGUMENTS')
    for key, value in kwargs.items():
        print(key, '-', value)


person = {
    'name': 'Leonardo',
    'surname': 'Reis',
}

addtional_data = {
    'age': 20,
    'country': 'Brazil',
}

person_complete = {**person, **addtional_data}  # merge both dicts
print(person_complete)

show_arguments(1, 2, 3, nickname='Leo', initials='RC')
print()
show_arguments(**person_complete)
