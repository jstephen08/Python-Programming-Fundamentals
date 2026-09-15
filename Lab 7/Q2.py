balance=10000
i=1
correct_pin="1234"

while i<=3:
    pin=int(input("Enter PIN: "))
   
    if pin==correct_pin:
           print("PIN accepted")

    amount=float(input("Enter withdrwal amount"))

    if amount>balance:
        print("Less balance")
    elif (balance-amount)<500:
        print("Withdrawal unsuccessful")
    else:
        balance=balance-amount
        print("Balance: ",balance)

        break
else:
    i=i+1
        
            
    
