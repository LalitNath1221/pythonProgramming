p_amt = float(input("Enter the Principal Amount : "))
ROI = float(input("Enter Rate of Intrest : "))
time = int(input("Enter no of years : "))
simple_int = (p_amt*ROI*time)/100
print(f'Simple interest is : {simple_int}')