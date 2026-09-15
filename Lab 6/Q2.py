#Question 2

correct_pin=1234

pin=int(input("Enter PIN: "))

while pin !=correct_pin:
    print("Incorrect PIN. Try again.")
    pin=int(input("Enter PIN: "))

print("Access granted!")
