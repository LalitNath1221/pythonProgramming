N = int(input("Enter NO. of natural numbers:"))
evensum = oddsum = 0
for i in range(1,N+1):
    if i%2==0:
        evensum=evensum+i
    else:
        oddsum+=i
print(f'The sum of odd natuaral no from 1 to {N} is : {oddsum}\nThe sum of even natuaral no from 1 to {N} is : {evensum}')