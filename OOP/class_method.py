class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_baby(cls, name):  # factory method
        return cls(name, 0)


son = Person.create_baby("Ravi")
daughter = Person.create_baby("Jade")