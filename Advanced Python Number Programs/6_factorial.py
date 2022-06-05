def factorial(num):
    if num==0:
        return 1
    return num*factorial(num-1)
n = int(input("Enter the no for factorial"))
print(f'{n}! = {factorial(n)}')