count = 1
output = ""

while count <= 4:
    thrust = float(input("Enter thrust: "))
    fuel_inlet = int(input("Fuel inlet open or closed: "))  # 1 for open, 0 for closed
    air_flow = float(input("Enter air flow: "))

    if thrust <= 300:
        output = output + "Engine no " + (count) + " Less thrust\n"
    if fuel_inlet != 1:
        output = output + "Engine no " + (count) + " Fuel inlet closed\n"
    if air_flow <= 120:
        output = output + "Engine no " + (count) + " Less Air Flow\n"

    count = count + 1

if output == "":
    print("All engines operating normally")
else:
    print(output)
