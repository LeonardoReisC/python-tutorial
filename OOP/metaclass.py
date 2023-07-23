'''
    metaclasses are the types of a class
    type: creates a class - type('name', (Bases,), __dict__)

    when creating a class, the following actions are taken in order:
    - __new__(mcs, name, bases, dct): create a new class
    - __call__(cls, *args, **kwargs) of  the metaclass: calls
        __new__ of the class: creates the instance
        __init__ of the class with the arguments
'''
from typing import Any


def my_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


class Meta(type):
    def __new__(mcs, name, bases, dct):
        print("Metaclass __new__")
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = my_repr

        if 'speak' not in cls.__dict__ or \
                not callable(cls.__dict__['speak']):  # comment 'speak' method
            raise NotImplementedError('Implements "speak"')
        return cls

    # make instance(class) callable -> Person("Leonardo")
    def __call__(self, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)

        if 'name' not in instance.__dict__:  # comment line 50
            raise NotImplementedError("Create 'name' attr")

        return instance


class Person(metaclass=Meta):  # default
    speak = 1234

    def __new__(cls, *args, **kwargs):
        print("My __new__")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print("My __init__")
        self.name = name

    def speak(self):
        print("speaking...")


person = Person('Leonardo')
print()
print(Person.attr, '-', person.attr)
print(person)
