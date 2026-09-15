i=1
fail=0
passed=0
dist=0
sum=0

lowest=101
highest=-1

while i<=10:
    mark=int(input("Enter student mark: "))
    i=i+1
    sum=sum+mark

    if 50<=mark:
        passed=passed+1
    if mark>=75:
        dist=dist+1
    elif mark<50:
        fail=fail+1
    
    if mark>highest:
        highest=mark
    if mark<lowest:
        lowest=mark
        
    avg=sum/10
    failp=(fail/10)*100
    passedp=(passed/10)*100
    distp=(dist/10)*100

print("Number failed: ",fail)
print("Number passed: ",passed)
print("Number distinction: ",dist)
print("Total marks: ",sum)
print("Average marks: ",avg)
print("Highest: ",highest)
print("Lowest: ",lowest)
print("Percentage failed: ",failp)
print("Percentage passed: ",passedp)
print("Percentage distinction: ",distp)
