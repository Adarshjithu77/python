import re  

a='Welcome to all1'

# print(a)

# print(re.findall('l',a)) output:['l', 'l', 'l']

# print(re.sub('all','ALL',a)) output:['l', 'l', 'l']

# print(re.split('e',a)) output:['W', 'lcom', ' to all1']

# print(re.search('al',a)) output:<_sre.SRE_Match object; span=(11, 13), match='al'>

# print(re.search('[abc]',a)) output:<_sre.SRE_Match object; span=(3, 4), match='c'>
# print(re.search('[a-z]',a)) output:<_sre.SRE_Match object; span=(1, 2), match='e'>
# print(re.search('[m-z]',a)) output:<_sre.SRE_Match object; span=(4, 5), match='o'>
# print(re.search('[A-Z]',a)) output:<_sre.SRE_Match object; span=(0, 1), match='W'>
# print(re.search('[0-9]',a)) output:<_sre.SRE_Match object; span=(14, 15), match='1'>

# a='abcd'
# print(re.search('d',a)) output:<_sre.SRE_Match object; span=(3, 4), match='d'>
# print(re.search('a.*',a)) output:<_sre.SRE_Match object; span=(0, 4), match='abcd'>
# print(re.search('c.+',a)) output:<_sre.SRE_Match object; span=(2, 4), match='cd'>
# print(re.search('a.?',a)) output:<_sre.SRE_Match object; span=(0, 2), match='ab'>

a='abcd0'

# print(re.search('[a-z].',a)) output:<_sre.SRE_Match object; span=(0, 2), match='ab'>
# print(re.search('[a-z].{4}',a)) output:<_sre.SRE_Match object; span=(0, 5), match='abcd0'>

# print(re.search('[a-z][0-9]',a)) output:<_sre.SRE_Match object; span=(3, 5), match='d0'>

# print(re.search('^[a-z]',a)) output:<_sre.SRE_Match object; span=(0, 1), match='a'> #startwith
# print(re.search('[0-9]$',a)) output:<_sre.SRE_Match object; span=(4, 5), match='0'> #endswith
# import re
# a=input("enter a number")
# len(a)
# if len(a)==10 and a.isdigit() and re.search('^[6-9]',a):
#     print("true")
# else:
#     print("false")


# import re
# a= input("enter a number")
# if re.search('^[6-9]\d{9}$',a):
#     print("mobile validate")
# else:
#     print("error")

# import re
# a= input("enter email")
# if(re.search('^[a-z0-9]..+@gmail.com$',a)):
#     print("email validate")
# else:
#     print("error")


# import re
# a= input("enter password")
# if(re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+=\-`~\[\]\{\}\|;':\"<>,.\/?]).{8,}$",a)):
#     print("password validate")
# else:
#     print("error")
