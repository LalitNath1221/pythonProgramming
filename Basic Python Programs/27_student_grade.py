math = float(input("Enter the marks of maths : "))
phy = float(input("Enter the marks of physics : "))
chem = float(input("Enter the marks of chemistry : "))
eng = float(input("Enter the marks of english : "))
hindi = float(input("Enter the marks of Hndi : "))
max_marks = int(input("Enter the maximum marks per subject"))
percentage  = ((math+phy+chem+eng+hindi)/(5*max_marks))*100
if percentage>=60:
    print("First Division")
elif percentage>=45:
    print("Second Division")
elif percentage>=33:
    print("Third Division")
    