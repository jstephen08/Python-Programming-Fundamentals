i=1
low=0
over=0
accept=0

while i<=10:
    weight=float(input("Enter weight of product: "))
    i=i+1

    if weight==100:
        accept=accept+1
        
    elif weight<99.5:
        low=low+1
       
    elif weight>100.5:
        over=over+1
        
        
print("Total accepted amount: ",accept)
print("Total low weight amount: ",low)
print("Total over weight amount: ",over)
