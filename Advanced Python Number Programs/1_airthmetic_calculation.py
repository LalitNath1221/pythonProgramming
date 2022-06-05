from __future__ import division


def add(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def multiplication(num1, num2):
    return num1*num2

def division(num1, num2):
    return num1/num2

def modulus(num1, num2):
    return num1%num2

def floordivision(num1, num2):
    return num1//num2

def exponent(num1, num2):
    return num1**num2

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))


print(f'{a} + {b} = { add(a, b) }')
print(f'{a} - {b} = { sub(a, b) }')
print(f'{a} * {b} = { multiplication(a, b) }')
print(f'{a} / {b} = { division(a, b) }')
print(f'{a} % {b} = { modulus(a, b) }')
print(f'{a} // {b} = { floordivision(a, b) }')
print(f'{a} ^ {b} = { exponent(a, b) }')