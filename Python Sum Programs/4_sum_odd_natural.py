N = int(input("Enter NO. of natural numbers:"))
sum = 0
for i in range(1,N+1):
    if i%2==1:
        sum=sum+i
print(f'The sum of odd natuaral no is : {sum}')