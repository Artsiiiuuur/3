class Account:
    def __init__(self, owner = "", balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, sum):
        self.balance += sum
        print(self.balance)

    def withdraw(self, sum):
        if(self.balance < sum):
            print("You don't have enough money")
        else:
            self.balance -= sum
            print(self.balance)


myAccount = Account(owner = "Sabir", balance = 10000)
myAccount.withdraw(sum = 12)