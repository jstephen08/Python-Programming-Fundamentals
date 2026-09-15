#Question 7

weight= int(input("Enter baggage weight: "))

if weight <= 20:
    print("No charge")
if 21<weight<30:
    print("Extra charge per kg is: ", 200*(weight-20))
elif weight >30:
    print("Baggage not allowed")
