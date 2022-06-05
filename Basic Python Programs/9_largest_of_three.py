first = int(input("Enter the first Number: "))
second = int(input("Enter the second Number: "))
third = int(input("Enter the third Number: "))
if first>second and first>third:
    print(f'geratest out of {first}, {second}, {third} is : {first}')
elif first<second and second>third:
    print(f'geratest out of {first}, {second}, {third} is : {second}')
else:
    print(f'geratest out of {first}, {second}, {third} is : {third}')