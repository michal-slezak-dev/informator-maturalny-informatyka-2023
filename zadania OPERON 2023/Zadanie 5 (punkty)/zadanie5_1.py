def which_quadrant(coord):
    if coord[0] < 0 < coord[1]:  # II ćwiartka dla x ujemnego i y dodatniego
        return "II"
    if coord[0] > 0 < coord[1]:  # I ćwiartka dla x dodatkiego i y dodatniego
        return "I"
    if coord[0] < 0 > coord[1]:  # III ćwiartka dla x ujemnego i y ujemnego
        return "III"
    if coord[0] > 0 > coord[1]:  # IV ćwiartka dla x dodatkiego i y ujemnego
        return "IV"

with open("punkty.txt", "r") as file:
    coordinates = [(int(line.strip().split()[0]), int(line.strip().split()[1])) for line in file]

quad1 = quad2 = quad3 = quad4 = 0
for point in coordinates:
    match which_quadrant(point):
        case "I":
            quad1 += 1
        case "II":
            quad2 += 1
        case "III":
            quad3 += 1
        case "IV":
            quad4 += 1
        case _:
            continue

print(f"I: {quad1}\nII: {quad2}\nIII: {quad3}\nIV: {quad4}\n")

with open("wyniki5.txt", "w") as out:
    out.write("5.1:\n")
    out.write(f"I: {quad1}\nII: {quad2}\nIII: {quad3}\nIV: {quad4}\n\n")