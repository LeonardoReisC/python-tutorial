from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency: int, account_number: int, balance: float = 0) \
            -> None:
        self.agency = agency
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def to_withdraw(self, value: float):
        ...

    def to_deposit(self, value: float):
        try:
            if not value > 0:
                raise ValueError("CANNOT DEPOSIT NON-POSITIVE VALUES")

            self.balance += value
        except ValueError as e:
            print(*e.args, sep="\n")
        else:
            self.details(f"DEPOSIT {value}")

    def details(self, msg: str = ""):
        print(f"Your balance is: ${self.balance:.2f} {msg}")

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f"({self.agency!r}, {self.account_number!r}, {self.balance!r})"
        return f"{class_name}{attrs}"

    @property
    def agency(self) -> int:
        return self.__agency

    @agency.setter
    def agency(self, agency: int):
        self.__agency = agency

    @property
    def account_number(self) -> int:
        return self.__account_number

    @account_number.setter
    def account_number(self, account_number: int):
        self.__account_number = account_number

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance


class SavingsAccount(Account):
    def to_withdraw(self, value: float):
        try:
            result = self.balance - value

            if result < 0:
                raise ValueError("WITHDRAW OPERATION DENIED")

            self.balance = result
        except ValueError as e:
            print(*e.args, sep="\n")
        else:
            self.details(f"WITHDRAW {value}")


class CheckingAccount(Account):
    def __init__(self, agency: int, account_number: int, balance: float = 0,
                 balance_limit: float = 500) -> None:
        super().__init__(agency, account_number, balance)
        self.balance_limit = balance_limit

    def to_withdraw(self, value: float):
        try:
            result = self.balance - value

            if result < -self.balance_limit:
                raise ValueError("WITHDRAW OPERATION DECLINED")

            self.balance = result
        except ValueError as e:
            print(*e.args, sep="\n")
        else:
            self.details(f"WITHDRAW {value}")

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f"({self.agency!r}, {self.account_number!r}, "\
            f"{self.balance!r}, {self.balance_limit!r})"
        return f"{class_name}{attrs}"

    @property
    def balance_limit(self) -> float:
        return self.__balance_limit

    @balance_limit.setter
    def balance_limit(self, balance_limit: float):
        self.__balance_limit = balance_limit


if __name__ == '__main__':
    sa1 = SavingsAccount(111, 222)
    sa1.to_deposit(100.97)
    sa1.to_withdraw(1)
    sa1.to_withdraw(100)
    print()

    ca1 = CheckingAccount(111, 222, 0, 100)
    ca1.to_deposit(64.65)
    ca1.to_withdraw(58.50)
    ca1.to_deposit(0)
    ca1.to_withdraw(5.60)
    ca1.to_withdraw(1)
    print()
