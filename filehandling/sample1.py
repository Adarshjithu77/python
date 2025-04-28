# f=open('sample.txt','x')#create
# f.write("sample file")

# f=open('sample1.txt','w')#write
# f.write('hello \n')
# f.write('welcome')
# f.write('sample')

# a=int(input("enter the limit"))
# f=open('sample2.txt','w')
# for i in range(a):
#     b=input("enter name:")
#     f.write(b+'\n')

# a=int(input("enter a number:"))
# f=open('sample3.txt','w')
# for i in range(1,11):
#     f.write(str(i)+"*"+str(a)+"="+str(i*a)+'\n')
    
#     # print(i,"*",a,"=",i*a)

# a=int(input("enter a number:"))
# f=open("sample4.txt",'w')
# for i in range(1,11):
#     for j in range(1,a+1):
#       f.write(str(i) +" * "+ str(j) + " = " + str(j*i)+"     ")
#     f.write(' \n ')
#     #   print(j,"*",i,"=",j*i)

# f=open('sample1.txt','a')
# f.write('\n new data')

# f=open('sample1.txt','r')
# # print(f.read())
# print(f.read(4))
# print(f.read())

# f=open('sample1.txt','r')
# print(f.readline())
# print(f.readline(4))
# print(f.readline())

# f=open('sample1.txt','r')
# print(f.readlines())

# f=open('word.txt','r')
# a=f.readlines()
# for i in a:
#   b=i.strip()
#   # print(b[::-1])
#   if b[::-1]==b:
#     print("its a palindrom",b)
#   else:
#     print("its not a palindrome")  

# f=open('word.txt','r')
# print(f.read())
# print(f.tell())

# f=open('word.txt','r')
# f.seek(3)
# print(f.read())

