f = open('demo.txt','r')

content = f.readlines()
print('no of lines',len(content))

f.seek(0)
words = 0
letters= 0
alphabets=0
numbers=0
capital=0
lower=0

for i in range(len(content)):
    line = f.readline().strip()
    for j in line: 
        if j == " ":
            words+=1 #space vrumbo increment akn
        else:
            letters+=1
            if j.isdigit():
                numbers+=1
            else:
                alphabets+=1
                if j.isupper():
                    capital+=1
                else:
                    lower+=1

    words+=1
print('words',words)
print('letters',letters)
print('numbers',numbers)
print('alphabets',alphabets)
print('capital',capital)
print('lower',lower)