unit = float(input("Enter no of units :"))
rate = float(input("Enter rate per unit :"))
if(unit<200):
    print("Payble amount : 0")
else:
    print(f'Payble amount : {rate*unit}')