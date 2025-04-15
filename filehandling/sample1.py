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

a=int(input("enter a number:"))
f=open("sample4.txt",'w')
for i in range(1,11):
    for j in range(1,a+1):
      f.write(str(i) +" * "+ str(j) + " = " + str(j*i)+"     ")
    f.write(' \n ')
    #   print(j,"*",i,"=",j*i)