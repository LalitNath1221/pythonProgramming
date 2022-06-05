N = int(input("Enter how mouch number you want : "))
a = i = 0
b = 1
while i<=N:
    if i<=1:
        c=i
    else:
        c=a+b
        a=b
        b=c
    print(c)
    i+=1