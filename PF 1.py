units=int(input("Enter number of units consumed: "))

if units<=50:
    print("Total bill: ", (50*units) + 1000)
elif units<=100:
    print("Total bill: ", (50*50) + (units-50)*100 + 1000)
else:
    print("Total bill: ", (50*50) + (50*100) + (units-100)*150 + 1000)
