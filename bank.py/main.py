bank=[]
from registers import register
from logins import login
from deposits import deposit
from withdraws import withdraw
from  balances import balance_amount
while True:
    print("""
1.register
2.login 
3.exit """)
    ch=int(input("enter your choice:"))
    if ch ==1:
        register(bank)
    elif ch==2:
        f,bnk=login(bank)
        print(f)
        if f==1:
            while True:
                print("""
1.deposit
2.withdraw
3.balance
4.exit """)
                ch1=int(input("enter your choice:"))
                if ch1==1:
                    deposit(bank)
                elif ch1==2:
                     withdraw(bank)
                elif ch1==3:
                     balance_amount(bank)
                elif ch1==4:
                    print("exit")
                    break
    elif ch==3:
        print("exit")
        break
    else:
        print("invalid choice")