class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance - 5
        return self
    
    def display_account_info(self):
        print("Balance: $", self.balance)
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

acc1 = BankAccount(0.01, 1000)
acc2 = BankAccount(0.05, 5000)

acc1.deposit(200).deposit(100).deposit(700).withdraw(100).yield_interest().display_account_info()
acc2.deposit(1000).deposit(1000).withdraw(100).withdraw(200).withdraw(300).withdraw(400).yield_interest().display_account_info()