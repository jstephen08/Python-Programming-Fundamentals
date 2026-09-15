i=0

flight1=[]
flight2=[]
flight3=[]
flight4=[]
flight5=[]
flight6=[]
flight7=[]
flight8=[]
flight9=[]
flight10=[]


while i<5:
    dest=str(input("Enter destination: "))
    destination.append(dest)

    air=str(input("Enter aircraft ID: "))
    aircraft_id.append(air)

    seat=int(input("Enter seat capacity: "))
    seat_capacity.append(seat)

    cap=str(input('Enter captain name: '))
    captain_name.append(cap)

    transit=str(input('Transit Yes/No: '))
    transits.append(transit)

    i=i+1

print(destination)
print(aircraft_id)
print(seat_capacity)
print(captain_name)
print(transits)
    
