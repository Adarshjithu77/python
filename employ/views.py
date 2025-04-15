employ=[]

def view():
    print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format('emp_id','name','age','position','salary'))#for formatting the output to a table structure
    print('-'*70)
    for emp in employ:
        print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format(emp['emp_id'],emp['name'],emp['age'],emp['position'],emp['salary']))
