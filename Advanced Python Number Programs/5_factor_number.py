N = int(input("Enter the no to find factors : "))
print(f'The factors of {N} are :')
for i in range(1, N+1):
    if N%i==0:
        print(i)
    
