class Account:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Depostied {amount}. New balance {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")


x = Account("Kazybek", 100000)
x.deposit(1000)
x.withdraw(300)
x.withdraw(20000) 