class Account:
    def __init__(self, number, name, pin):
        self.number = number
        self.name = name
        self.pin = pin
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount, pin):
        if self.pin == pin:
            self.balance -= amount
        else:
            raise ValueError("Incorrect PIN")

    def get_balance(self, pin):
        if self.pin == pin:
            return self.balance
        else:
            raise ValueError("Incorrect PIN")