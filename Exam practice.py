i=1
tot=0
fail=0
passed=0
dist=0
highest=-1
lowest=101

while i<=10:
    mark=float(input("Enter student mark: "))
    tot=tot+mark

    if mark>highest:
        highest=mark
    if mark<lowest:
        lowest=mark

    if mark>=50:
        passed=passed+1
    if mark>=75:
        dist=dist+1
    elif mark<50:
        fail=fail+1

    i=i+1

avg=tot/10
print("Number of passes: ",passed)
print("Number of fails: ",fail)
print("Number of distinctions: ",dist)
print("Average marks: ",avg)
print("Percentage of passed: ",(passed/10)*100)
print("Percentage of failed: ",(fail/10)*100)
print("Percentage of distinctions: ",(dist/10)*100)
print("Highest mark is ",highest)
print("Lowest mark is ",lowest)


    
