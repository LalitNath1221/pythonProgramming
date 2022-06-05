num = int(input("Enter the Number: "))
print(f'Divisors of {num}')
i=1
while i<=num:
    if(num%i==0):
        print(i)
    i+=1