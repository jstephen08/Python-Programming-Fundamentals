#Question 5

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))

if num1>num2:
    if num1>num3:
        print("Largest is: ",num1)
elif num2>num3:
    print("Largest is: ",num2)
else:
    print("Largest is: ",num3)
if num1==num2 and num2==num3:
    print("All numbers are equal")
