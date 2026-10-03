class Account:
    def __init__(self, account, pin, balance=0):
        self.account = account
        self._pin = pin
        self._balance = balance
    def verify_pin(self,input_pin):
        return self._pin == input_pin
    def deposit(self,amount):
        if amount <= 0:
            return False
        self._balance += amount
        return True
    def withdraw(self,amount):
        if amount <= 0 or amount > self._balance:
            return False
        self._balance -= amount
        return True
    def get_balance(self):
        return self._balance

class ATM:
    def __init__(self,account):
        self._account= account
    def start(self):
        print("WELCOME TO ATM")
        for _ in range(3):
            pin = int(input("Enter Pin Number: "))
            if self._account.verify_pin(pin):
                print("Login successful")
                self.menu()
                return
            else:
                print("Invalid Pin Number")
        print("Too many failed attempts. Exiting...")
    def menu(self):
        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                balance = self._account.get_balance()
                print(f"BALANCE: ${balance}")

            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                if self._account.deposit(amount):
                    print(f"Deposited ${amount} successfully")
                else:
                    print("Invalid amount")

            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                if self._account.withdraw(amount):
                    print(f"Withdrawn ${amount} successfully")
                else:
                    print("Insufficient balance or Invalid amount! Try again")
            elif choice == "4":
                print("Thank you for using ATM")
                break

            else:
                print("Invalid choice")


user = Account("123456789", 1234, 1000)
atm = ATM(user)
atm.start()
