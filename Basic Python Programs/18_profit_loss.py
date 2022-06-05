actual_amount = float(input("Enter the Actual amount : "))
sales_amount = float(input("Enter the Sales Amount : "))

if actual_amount<sales_amount:
    print(f'Profit amount is {sales_amount-actual_amount}')
elif actual_amount>sales_amount:
    print(f'Loss amout is {actual_amount-sales_amount}')
else:
    print("NO Profit or Losss")