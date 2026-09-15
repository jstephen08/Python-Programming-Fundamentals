#Question 8

CORRECT_PIN = 1234
MIN_BALANCE = 500


pin = int(input("Enter your PIN: "))
balance = float(input("Enter your account balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))


if pin != CORRECT_PIN:
    print("Incorrect PIN. Access denied.")

else:
   
    if withdraw_amount > balance:
        print("Insufficient balance.")

    elif (balance - withdraw_amount) < MIN_BALANCE:
        print("Withdrawal denied. Minimum balance of 500 must be maintained.")

    else:
        balance -= withdraw_amount
        print("Withdrawal successful!")
        print("Remaining balance:", balance)

