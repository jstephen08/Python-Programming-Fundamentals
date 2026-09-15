GPA=float(input("Enter student's GPA: "))
fincome=int(input("Enter family income: "))

if GPA>=3.5 and fincome<30000:
    print("Full Scholarship received")
elif GPA>=3.0 and fincome<50000:
    print("Partial scholarship received")
else:
    print("No scholarship received")
