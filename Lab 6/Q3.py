i=1
bill=0

while i<=5:
    price=float(input("Enter price of item: "))
    bill=bill+price
    i=i+1
print("Total amount",bill)

if bill>5000:
    discount=0.2*bill
    print("Discount: ",discount)
    total_bill=bill-discount
    print("Total bill: ", total_bill)
else:
    print("Total bill: ",bill)
