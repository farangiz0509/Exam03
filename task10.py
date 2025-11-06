class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Yangi balans:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Yangi balans:", self.balance)
        else:
            print("Balans yetarli emas")

a = BankAccount("Ali", 1000)
a.deposit(500)
a.withdraw(2000)