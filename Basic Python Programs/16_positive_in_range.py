minimum = int(input("Enter minimum range: "))
maximum = int(input("Enter maximum range: "))
if minimum<=0 and maximum<=0:
    print(f'No positive no between {minimum} and {maximum}')
else:
    print("Positive numbers are : ", minimum)
    for i in range(minimum, maximum+1):
        if(i>0):
            print(i)