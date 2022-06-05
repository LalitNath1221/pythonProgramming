N = int(input("Enter the Number: "))
print(f'Enter {N} numbers')
sum = i =0
while i<N:
    sum+= int(input())
    i=i+1
print(f'Sum = {sum}\nAverage = {sum/N}')