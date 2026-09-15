deposit=0
withdrawal=0
while True:
    action=float(input("Withdrawal or deposit: "))
    if action==0:
        break
    elif action<0:
        withdrawal=withdrawal+action
    elif action>0:
        deposit=deposit+action
balance=deposit+withdrawal
if balance<0:
        print("Overdrawn")

print("Withdrawal amount",withdrawal)
print("Deposit amount",deposit)
print('balance',balance)
        
        
