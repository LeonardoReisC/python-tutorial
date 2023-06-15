class Person:  # inherits from builtins.object
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def say_class_name(self):
        print(self.__class__.__name__)


class Customer(Person):
    def say_class_name(self):
        print("This is Customer class")


class Student(Person):
    ...


customer = Customer("Vânia", "Reis")
customer.say_class_name()

student = Student("Leonardo", "Reis")
student.say_class_name()
