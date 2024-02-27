from re import Scanner

import java.util.Scanner


class Scanner:
    def __init__(self, input):
        self.input = input


class System:
    pass


class BankApp:
    def enter_pin(self):
        scanner = Scanner(System.in)
        print("Enter PIN:")
        pin = scanner.next()
        return pin

    def main(self):
        bank = Bank()
        scanner = Scanner(System.in)

        try:
            while True:
                print("Welcome to My Bank ATM")
                print("Select an option:")
                print("1. Register Account")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transfer")
                print("5. Check Balance")
                print("6. Remove Account")
                print("7. Exit")
                choice = input("Enter your choice: ")

                if choice == "1":
                    name = input("Enter name: ")
                    pin = self.enter_pin()
                    bank.register_customer(name, pin)
                    print("Account registered successfully.")
                elif choice == "2":
                    account_number = int(input("Enter account number: "))
                    deposit_amount = float(input("Enter amount to deposit: "))
                    bank.deposit(account_number, deposit_amount)
                    print("Deposit successful.")
                elif choice == "3":
                    account_number = int(input("Enter account number: "))
                    withdraw_amount = float(input("Enter amount to withdraw: "))
                    pin = self.enter_pin()
                    bank.withdraw(account_number, withdraw_amount, pin)
                    print("Withdrawal successful.")
                elif choice == "4":
                    from_account_number = int(input("Enter account number to transfer from: "))
                    to_account_number = int(input("Enter account number to transfer to: "))
                    transfer_amount = float(input("Enter amount to transfer: "))
                    pin = self.enter_pin()
                    bank.transfer(from_account_number, to_account_number, transfer_amount, pin)
                    print("Transfer successful.")
                elif choice == "5":
                    account_number = int(input("Enter account number: "))
                    pin = self.enter_pin()
                    balance = bank.check_balance(account_number, pin)
                    print("Current balance:", balance)
                elif choice == "6":
                    account_number = int(input("Enter account number: "))
                    pin = self.enter_pin()
                    bank.remove_account(account_number, pin)
                    print("Account removed successfully.")
                elif choice == "7":
                    print("Thank you for using My Bank ATM. Goodbye!")
                    return
                else:
                    print("Invalid choice. Please try again.")
        except Exception as e:
            print("Error:", e)
        finally:
            scanner.close()

if __name__ == "__main__":
    app = BankApp()
    app.main()