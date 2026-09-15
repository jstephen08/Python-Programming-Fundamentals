num1= int(input ("Enter number 1 "))
num2= int(input ("Enter number 2"))
num3= int(input ("Enter number 3"))

if num1 > num2:
    if num1 > num3:
    print("Largest number is ", num1)
    else:
    print ("Largest number is ", num2)
else:
    if num2 > num3:
    print ("Largest number is ", num3)
