p_amt = float(input("Enter the Principal Amount : "))
ROI = float(input("Enter Rate of Intrest : "))
time = int(input("Enter no of years : "))
ci_future = p_amt*((1+(ROI/100))**time)
compound_int = ci_future - p_amt
print(f'The compound intrest is : {compound_int}')