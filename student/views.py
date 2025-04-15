def view(student):
    print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format('adm_no','name','age','course','fee'))
    print('-'*70)
    for std in student:
        print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format(std['adm_no'],std['name'],std['age'],std['course'],std['fee']))