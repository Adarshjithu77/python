bank=[]
while True:
    print("""
1.register
2.login
3.exit
 """   )
    ch=int(input("enter your choice:"))
    if ch ==1:
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
    elif ch==2:
        username=input("enter username")
        password=input("enter password")
        f=0
        for bnk in bank:
            if bnk['username']==username and bnk['password']==password:
                print("bank",bnk)
                f=1
                while True:
                    print("""
1.deposit
2.withraw
3.balance enquiry
4.exit""")
                    ch1=int(input("enter your choice:"))
                    if ch1==1:
                        deposit=int(input("enter deposit amount:"))
                        bnk['balance_amount']+=deposit
                    elif ch1==2:
                        withraw=int(input("enter withraw amount"))
                        bnk['balance_amount']-=withraw
                    elif ch1==3:
                        print(bnk['balance_amount'])
                    elif ch1==4:
                        print("exit")
                        break
        if f==0:
                        print("no record found")
    elif ch==3:
        print("exit")
        break
    else:
        print("invalid")
    