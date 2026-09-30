class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("wpłata musi być większa niż zero")
    
    def withdraw(self, amount):
        if self.__balance > 0 and self.__balance > amount:
            self.__balance -= amount
        else:
            print("brak pieniędzy na koncie uniemożliwia wypłatę")
    
    def get_balance(self):
        return self.__balance

account_1 = BankAccount("Jan Kowalski", 1000)

account_1.deposit(2000)
account_1.withdraw(500)
print(account_1.get_balance())

