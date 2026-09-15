print("Cement=4000,soil=20000,steel=1500,wire=8000,paint=24000")
tot=0
conti=int(input('Enter 1 to continue or 0 to exit: '))
while conti==1:

    item_price=float(input('Enter price of the item: '))
    qty=float(input('Enter quantity of the item: '))
    tot=tot+item_price*qty
    conti=int(input('Enter 1 to continue or 0 to exit: '))
    
if tot>100000:
    discount=tot*5/100
    tot=tot-discount

print('Total bill is: ',tot)
