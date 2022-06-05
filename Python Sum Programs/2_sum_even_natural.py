N = int(input("Enter NO. of natural numbers:"))
sum = 0
for i in range(1,N+1):
    if i%2==0:
        sum=sum+i
print(f'The sum of even natuaral no is : {sum}')