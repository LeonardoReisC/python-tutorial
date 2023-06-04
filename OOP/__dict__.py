class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Leonardo", 20)

print(person.__dict__)  # shows the instance atributes
print(vars(person))  # also works
