import Account


class Person():
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f"({self.name!r}, {self.age!r})"
        return f"{class_name}{attrs}"


class Customer(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.account: Account.Account | None = None


if __name__ == "__main__":
    c1 = Customer("Leonardo", 20)
    c1.account = Account.CheckingAccount(111, 222)
    print(c1)
    print(c1.account)

    c2 = Customer("Pedro", 20)
    c2.account = Account.CheckingAccount(345, 666)
    print(c2)
    print(c2.account)
