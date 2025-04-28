f=open("wordprg.txt",'r')
a=f.readlines()
print("number of lines",len(a))
for i in a:
    b=i.strip()
    print(b)
