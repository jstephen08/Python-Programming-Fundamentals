#Question 1

i=1
sum=0

while i<=5:
    mark=int(input("Enter student mark: "))
    i=i+1
    sum=sum+mark

    avg=sum/5

print(avg)

if avg>=50:
    print("Pass")
else:
    print("Fail")
