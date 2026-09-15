count=1
largest=0

while count<=10:
    num=int(input("Enter number: "))
if num>largest:
    largest=num
    count=count+1
else:
    print("Maximum number is: ",largest)
