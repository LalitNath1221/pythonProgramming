print("Enter the numbers :")
sum = i = 0
while i<10:
    a = int(input())
    if(a<0):
        break
    sum = sum+a
    i+=1
print(f'Sum = {sum}')