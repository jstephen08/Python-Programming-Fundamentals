i=1

mark=[]

while i<=10:
    smark=int(input('Enter student mark: '))
    mark.append(smark)

    
    i=i+1

print(mark)


#finding the max
#assume first data in the list is the highest

max=mark[0]

i=1
while i<=9:
    if mark[i]>max:
        max=mark[i]

    i=i+1

print('Max is= ',max)
