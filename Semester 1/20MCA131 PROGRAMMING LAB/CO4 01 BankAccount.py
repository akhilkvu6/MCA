class Bank:
    # The Constructor: Sets up the initial state (name and starting balance)
    def __init__(self, name, balance):
        # 'self' is the standard Python convention for the instance reference
        self.name = name
        self.balance = balance
    
    # Method 1: Deposits amount and updates the balance
    def deposit(self, amount):
        # The balance is correctly incremented
        self.balance += amount
        print(f"DEPOSITED: ₹{amount}")
        print(f"Current Balance after deposit: ₹{self.balance:.2f}")
    
    # Method 2: Withdraws amount with validation
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"WITHDREW: ₹{amount}")
    
    # Method 3: Displays the final balance
    def dis_balance(self):
        print(f"The current final balance is ₹{self.balance:.2f}")

name = input("Enter your name: ")
balance1 = float(input("Enter your current balance: ₹"))
account = Bank(name, balance1)

deposit_amount = float(input("Enter amount to deposit: ₹"))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: ₹"))
account.withdraw(withdraw_amount)

account.dis_balance()