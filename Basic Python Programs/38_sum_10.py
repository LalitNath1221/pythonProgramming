print("Enter 10 numbers : ")
sum = i = 0
while i<10:
    a = int(input())
    if(a>0):
        sum=sum+a
    i+=1
print(f'Sum of positive number : {sum}')