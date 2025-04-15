bank=[]

def register():
    if len(bank)==0:
        bnk=1
    else:
        bnk=bank[-1]['bank_id']+1
    username=input("enter username:")
    accountno=int(input("enter accountno"))
    phn_no=int(input("enter phn_no"))
    email=input("enter email")
    password=input("enter password")
    balance_amount=1000
    bank.append({'bank_id':bnk,'username':username,'accountno':accountno,'phnno':phn_no,'email':email,'password':password,'balance_amount':1000})
    
def login():
    username=input("enter username")
    password=input("enter password")
    f=0
    for bnk in bank:
        if bnk['username']==username and bnk['password']==password:
          print("bank",bnk)
          f=1
    return f,bnk


def deposit(bnk):
        deposit=int(input("enter deposit amount:"))
        bnk['balance_amount']+=deposit
def withdraw(bnk):
        withraw=int(input("enter withraw amount"))
        bnk['balance_amount']-=withraw
def balance_amount(bnk):
        print(bnk['balance_amount'])
while True:
    print("""
1.register
2.login 
3.exit """)
    ch=int(input("enter your choice:"))
    if ch ==1:
        register()
    elif ch==2:
        f,bnk=login()
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
                    deposit(bnk)
                elif ch1==2:
                     withdraw(bnk)
                elif ch1==3:
                     balance_amount(bnk)
                elif ch1==4:
                    print("exit")
                    break
    elif ch==3:
        print("exit")
        break
    else:
        print("invalid choice")
                
                
                       
        











    
