N = int(input("Enter how mouch number you want : "))
a = i = fibosum = 0
b = 1
while i<N:
    if i<=1:
        c=i
    else:
        c=a+b
        a=b
        b=c
    fibosum+=c
    i+=1

print(f'Sum of fibnacci series upto {N} is : {fibosum}')