#Bank Withdrawal System

account_balance=float(input("Enter Account Balance: "))
withdrawal_amount=float(input("Enter Withdrawal Amount: "))
remaining_balance=account_balance-withdrawal_amount

if withdrawal_amount>account_balance:
    print("Insufficient balance")
elif remaining_balance<500:
    print("Cannot withdraw. Minimum balance of 500 required")
else:
    print("Withdrawal successful")
    

print("Remaining balance: ", remaining_balance)
