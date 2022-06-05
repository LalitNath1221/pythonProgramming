a = int(input("Enter first number : "))
b = int(input("Enter second number ( cant be zero ): "))
c = input("Enter the operation (+, *, -, /, %)")
if c=="+":
    print(f'{a} + {b} = {a+b}')
elif c=="-":
    print(f'{a} - {b} = {a-b}')
elif c=="*":
    print(f'{a} * {b} = {a*b}')
elif c=="/":
    print(f'{a} / {b} = {a/b}')
elif c=="%":
    print(f'{a} % {b} = {a%b}')
else:
    print("Invalid operator!")