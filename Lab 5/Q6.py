#Question 6

i=1
sum=0

while i<=10:
    mark=int(input("Enter student mark: "))
    i=i+1
    sum=sum+mark
    
avg=sum/10
print(avg)

if avg<50:
    print("Fail!")
else:
    print("Pass!")
