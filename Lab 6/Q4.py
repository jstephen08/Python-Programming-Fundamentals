odd=0
even=0

for i in range(5):
    num=int(input("Enter number: "))
    
    if num%2==0:
        even=even+1
    else:
        odd=odd+1

print("odd numbers: ",odd)
print("even numbers: ",even)
