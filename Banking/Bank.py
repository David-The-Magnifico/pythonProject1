class Bank:
    def __init__(self):
        self.accounts = []

    def register_customer(self, name, pin):
        branch_code = 1234
        customer_number = len(self.accounts) + 1
        account_number = self.generate_account_number(branch_code, customer_number)

        account = Account(account_number, name, pin)
        self.accounts.append(account)
        return account

    def generate_account_number(self, branch_code, customer_number):
        account_number_str = str(branch_code) + str(customer_number).zfill(4)
        return int(account_number_str)

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account is not None:
            account.deposit(amount)
        else:
            raise ValueError("Account not found")

    def withdraw(self, account_number, amount, pin):
        account = self.find_account(account_number)
        if account is not None:
            account.withdraw(amount, pin)
        else:
            raise ValueError("Account not found")

    def transfer(self, from_account_number, to_account_number, amount, pin):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)

        if from_account is not None and to_account is not None:
            from_account.withdraw(amount, pin)
            to_account.deposit(amount)
        else:
            raise ValueError("One or both accounts not found")

    def check_balance(self, account_number, pin):
        account = self.find_account(account_number)
        if account is not None:
            return account.get_balance(pin)
        else:
            raise ValueError("Account not found")

    def remove_account(self, account_number, pin):
        account = self.find_account(account_number)
        if account is not None:
            self.accounts.remove(account)
        else:
            raise ValueError("Account not found")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.get_number() == account_number:
                return account
        return None

    def get_number_of_customers(self):
        return len(self.accounts)

    def register(self, customer):
        raise ValueError("Customer")