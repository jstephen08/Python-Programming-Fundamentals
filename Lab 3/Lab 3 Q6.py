#Question 06
num1= int(input('enter number 1'))
num2= int(input('enter number 2'))
num3= int(input('enter number 3'))

if num1>num2:
    if num1>num3:
        print ('Largest number is ', num1)
elif num2>num3:
            print ('Largest number is ', num2)
else:
    print ('Largest number is ', num3)
