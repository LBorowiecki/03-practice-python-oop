class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            "wpłata musi być większa niż zero"
    
    def withdraw(self, amount):
        if self.__balance > 0:
            self.__balance -= amount
        else:
            "brak pieniędzy na koncie uniemożliwia wypłatę"
    
    def get_balance(self):
        print(self.__balance)

account_1 = BankAccount("Jan Kowalski", 1000)

account_1.deposit(2000)
account_1.withdraw(1500)
account_1.get_balance()

