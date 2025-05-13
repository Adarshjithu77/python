l=[]
number=(10,20,5)
def second_largest(numbers):
    number=list(set(numbers))
    if len(number)<=2:
        print("number",number)
