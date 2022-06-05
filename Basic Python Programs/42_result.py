math = float(input("Enter the marks of maths : "))
phy = float(input("Enter the marks of physics : "))
chem = float(input("Enter the marks of chemistry : "))
eng = float(input("Enter the marks of english : "))
hindi = float(input("Enter the marks of Hndi : "))
max_marks = int(input("Enter the maximum marks per subject"))
total = (math+phy+chem+eng+hindi)
avg = total/5
percentage  = (total/(5*max_marks))*100
print(f'Total marks : {total}\nAverage marks : {avg}\nPercentage : {percentage}')
