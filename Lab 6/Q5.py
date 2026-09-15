sum=0

while True:
    dep=float(input("Enter deposit amount: "))
    if dep==0:
         break
    sum=sum+dep

print("Total: ",sum)

if sum>=10000:
    print(sum,"Premium Customer")
else:
    print(sum, "Regular Customer")
    
