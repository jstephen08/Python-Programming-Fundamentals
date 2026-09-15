i=1
pword='admin'

while i<=3:
    password=str(input("Enter password: "))
    i=i+1
    if password==pword:
        print("Login successful!")
        break
else:
    print("Account locked")
    
