units= int (input("Enter number of units "))

if units <= 50:
    bill = (units*10) + 1000
elif units <= 90:
    bill = (50*10) + ((units-50)*15) + 1000
else:
     bill = (50*10) + (40*15) + ((units-90)*50) + 1000

print ("Total bill is ", bill)
