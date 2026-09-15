total=0
avg=0
c_f_sub=0

for i in range (1,7,2):
    mark=float(input(f"Enter student mark {i}: "))
    total=total+mark

    if mark<50:
        c_f_sub=c_f_sub+1
        

avg=total/6

print("Total marks: ",total)
print("Average: ",avg)
print("Count of failed subjects: ",c_f_sub)

if avg>=60 and c_f_sub==0:
    print("Excellent performance")
elif avg>=50:
    print("Pass")
else:
    print("Fail")
    
