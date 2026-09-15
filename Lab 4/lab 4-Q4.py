#Question 4

income= int(input("Enter income: "))
if income>=100000:
    print("Tax amount: ", 0.2*income)
if 50000<income<100000:
    print("Tax amount: ", 0.1*income)
else:
    print("No tax applied")
