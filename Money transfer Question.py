currency=["USD","GBP","Euro","Bhat","INDR"]
rates=[]

#taking inputs to my rates list using a loop
for i in range (5):
    rate=float(input(f"Enter rate in SL Rupee for {currency[i]}"))
    rates.append(rate)

#print in a nice table
print("-"*30)
print(f"{'Currency':<10}{'Rate':>10}")
print("-"*30)

for x in range (5):
    print(f"{currency[x]:<10}{rates[x]:>10}")

print("-"*30)

#calculating exchange amount
tot=0
choice=int(input("Enter 0-USD, 1-GBP, 2-Euro, 3-Bhat, 4- INDR, 5-Exit?"))
while choice!=5:
    am=float(input("Enter how much?"))
    tot=tot+rates[choice]*am
    choice=int(input("Enter 0-USD, 1-GBP, 2-Euro, 3-Bhat, 4- INDR, 5-Exit?"))

print("Bill is = ",tot)



