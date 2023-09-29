class Person:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


def say_my_name(person: Person) -> str:
    return person.full_name


print(say_my_name(Person('Leonardo', 'Reis Coimbra')))
