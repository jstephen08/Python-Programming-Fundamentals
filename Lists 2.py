i=0

make=[]
model=[]
eng=[]

while i<4:
    m=str(input("Enter car brand: "))
    make.append(m)

    mod=str(input("Enter model: "))
    model.append(mod)

    eng_cap=float(input("Enter engine capacity: "))
    eng.append(eng_cap)

    i=i+1

print(make)
print(model)
print(eng)
