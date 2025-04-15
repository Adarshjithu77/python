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