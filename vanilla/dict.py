# dictionaries are mutable data structures
import copy

person = {
    'name': 'Leonardo',
    'surname': 'Coimbra',
    'grades': [9.5, 8, 10],
}

person['age'] = 20  # create another propertie
print(person, '\n')

del person['age']  # deletion
print(person, '\n')

# USEFUL METHODS
print(len(person))  # returns the number of keys - same as person.__len__()
print(person.keys())
print(person.values())
print(person.items())
# set a default value for an existing ou non-existing property
print(person.setdefault('age', 0), '\n')

# shallow copy: copies only imutable data
person1 = person.copy()
person1['grades'][1] = 0
print(person, '\n')  # person1 points the person['grades'] mutable data

# deep copy: copies recursively the entire object
person1 = copy.deepcopy(person)
person1['grades'][0] = 0
print(person, '\n')

print(person.get("name", None))  # returns None if the property does not exists
# delete and returns the value of the corresponding key
print(person.pop('grades'))
print(person.popitem())  # delete and returns the last (key, value) of the dict

person.update({
    'surname': 'Reis',  # updates an existing property
    'age': 20  # add a new property
})
person.update(surname='Reis', age=20) # workis with named arguments
person.update([['surname', "Reis"], ['age', 20]]) # works with other iterables

print(person)
