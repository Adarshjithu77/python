class bank:
    def __init__(self):
        self.name=input("enter name:")
        self.phn_num=int(input("enter number"))
        self.email=input("enter email")
        self.balance=0
    
    def deposit(self):
        self.deposit=int(input("enter deposit amount"))
        self.balance+=self.deposit
        print("deposit amount",self.deposit)
    def withdraw(self):
        self.withdraw=int(input("enter withdraw amount"))
        self.balance-=self.withdraw
        print('withdraw amount',self.withdraw)
    def balnce(self):
        print('balance amount',self.balance)

Accnt101=bank()
Accnt101.deposit()
Accnt101.withdraw()
Accnt101.balnce()