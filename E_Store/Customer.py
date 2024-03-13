from E_Store import Address
from E_Store import Credit_Card


class Customer:

    def __init__(self, name: str, age: int, address: Address, password: str, number: str):
        super.__init__(name, age, address, password, number)

    def get_number_of_billing_info(self):
        pass

    def add_billling_info(self, recievers_name: str, receivers_number: str, delivery_address: Address,
                          card: Credit_Card):
        pass