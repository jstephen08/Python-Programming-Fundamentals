i=1
total=0

while i<=5:
    price=float(input("Enter price: "))
    qty=int(input("Enter quantity: "))
    total=total+(price*qty)
    i=i+1

if total>10000:
    discount=0.25*total
    
elif 5000<total<10000:
    discount=0.15*total
    
elif total<5000:
    discount=0
    

final_amount=total-discount
print("Total: ",total)
print("Discount: ",discount)
print("Final amount: ",final_amount)

