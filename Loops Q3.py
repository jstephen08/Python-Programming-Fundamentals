i=1
low=0
medium=0
high=0
sum=0

while i<=10:
    deposit=float(input("Enter deposit amount: "))
    i=i+1
    sum=sum+deposit

    if deposit<5000:
        low=low+1
    elif 5000<deposit<=20000:
        medium=medium+1
    elif deposit>20000:
        high=high+1

    avg=sum/10
    
print("Total deposits: ",sum)
print("Low deposits: ",low)
print("High deposits: ",high)
print("Medium deposits: ",medium)
print("Average deposit: ",avg)
