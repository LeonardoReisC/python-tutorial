import Account
import Person


class Bank():
    def __init__(self, agencies: list[int] | None = None,
                 customers: list[Person.Person] | None = None,
                 accounts: list[Account.Account] | None = None):

        self.agencies = agencies or []
        self.customers = customers or []
        self.accounts = accounts or []

    def validate_account(self, account: Account.Account):
        if account not in self.accounts:
            raise ValueError("Account not found")

    def validate_agency(self, agency: int):
        if agency not in self.agencies:
            raise ValueError("Agency not found")

    def validate_customer(self, customer: Person.Person):
        if customer not in self.customers:
            raise ValueError("Customer not found")

    def to_authenticate(self, customer: Person.Person,
                        account: Account.Account):
        authentication = False

        try:
            self.validate_account(account)
            self.validate_agency(account.agency)
            self.validate_customer(customer)
        except ValueError as e:
            print("AUTHENTICATION DENIED")
            print(*e.args, sep="\n")
        else:
            print("AUTHENTICATION SUCCESS")
            authentication = True
        return authentication

    @property
    def customers(self):
        return self.__customers

    @customers.setter
    def customers(self, customers):
        self.__customers = customers

    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, accounts):
        self.__accounts = accounts


if __name__ == "__main__":
    c1 = Person.Customer("Leonardo", 20)
    ca1 = Account.CheckingAccount(112, 235)
    bank = Bank([112, 848], [c1], [ca1])
    bank.to_authenticate(Person.Customer("Leonardo", 54), ca1)
    bank.to_authenticate(c1, ca1)