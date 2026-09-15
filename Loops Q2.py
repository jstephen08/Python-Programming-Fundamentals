i=1
low=0
medium=0
high=0

while i<=10:
    bill=float(input("Enter bill amount: "))
    i=i+1

    if bill<1000:
        low=low+1

    elif bill>5000:
        high=high+1

    else:
        medium=medium+1

print("Number of low sales: ",low)
print("Number of high sales: ",high)
print("Number of medium sales: ",medium)
