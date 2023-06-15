# Parent object manages child's lifecycle
# If the parent object is removed, then all its childs will do so
class Customer:
    def __init__(self, name):
        self.name = name
        self.addresses = []

    def insert_address(self, street, number):
        # Address is created inside Customer
        self.addresses.append(Address(street, number))

    def list_addresses(self):
        for address in self.addresses:
            print(address.street, address.number)

    def __del__(self):  # called when the object is being deleted from memory
        print(f'Deleting customer {self.name}')


class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def __del__(self):
        print(f'Deleting Addrees [{self.street}, {self.number}]')


customer = Customer("Leonardo")
customer.insert_address("Dr. Emilio da Silveira", "398")
customer.insert_address("João Pinheiros", "204")
customer.list_addresses()
print()

del customer

print("------------#------------")
