a = int(input("Enter a postive no : "))
count = 0
while a>1:
    count +=1
    a=a/10
print(f'No of digits in "{a}" is : {count}')