i=1
total=0

while i<=3:
    units=int(input("Enter number of units: "))
    i=i+1
    total=total+units
    
print("Total units used: ",total)
if units>300:
    print("High usage")
else:
    print("Normal usage")
