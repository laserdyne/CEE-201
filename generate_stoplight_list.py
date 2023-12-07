with open("chicago.txt") as file:
    data = [line.rstrip() for line in file]

with open("cameras.txt") as file:
    data2 = [line.rstrip() for line in file]


streets = []
red_lights = []
for line in data:
    l = line.split()
    streets.append((int(l[0]), int(l[1]), float(l[2])))

for line in data2:
    red_lights.append(int(line))


new_street_list = []

for street in streets:
    if street[0] not in red_lights and street[1] not in red_lights:
        new_street_list.append(street)
print(new_street_list)

f = open("routes_no_cameras.txt", "w+")

for street in new_street_list:
    source = str(street[0])
    destination = str(street[1])
    time = str(street[2])

    f.write(source + " " + destination + " " + time)
    f.write("\n")

f.close()
