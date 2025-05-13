# f= open('qstn4.txt','x')
f = open('qstn4.txt','r')
a=f.readlines()
if len(a)==1:
    print(len(a))
for i in a:
    b=i.strip()
    print(b)