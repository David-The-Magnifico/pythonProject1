class BankAccount:
    def __init__(self, number, name, pin):
        self.number = number
        self.name = name
        self.pin = pin
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Amount must be positive")

    def withdraw(self, amount, pin):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
            else:
                raise ValueError("Insufficient funds")
        else:
            raise ValueError("Amount must be positive")

    def check_balance(self, pin):
        if self.pin == pin:
            return self.balance
        else:
            raise ValueError("Invalid pin")

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def get_pin(self):
        return self.pin

    def set_pin(self, pin):
        self.pin = pin

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number