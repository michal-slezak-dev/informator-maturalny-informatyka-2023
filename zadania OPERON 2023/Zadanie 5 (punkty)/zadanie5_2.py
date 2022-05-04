from math import sqrt
BEG_X, BEG_Y = 0, 0  # współrzędne początku ukłądu współrzędnych

def distance(point):  # zwracamy odległość ze wzoru sqrt((x2-x1)^2 + (y2-y1)^2)
    return sqrt((BEG_X - point[0])**2 + (BEG_Y - point[1])**2)

with open("punkty.txt", "r") as file:
    coordinates = [(int(line.strip().split()[0]), int(line.strip().split()[1])) for line in file]

max_dist = -1  # defaultowa wartość dla maxa
counter = 0  # licznik punktów o max odległości
max_coord = []  # punkty o max odległości
for point in coordinates:
    if distance(point) > max_dist:
        max_dist = distance(point)  # wyłaniamy max odległość

for point in coordinates:
    if distance(point) == max_dist:
        counter += 1  # jeśli pkt ma max odległość to zwiększamy counter i dodajemy współrzędne punktu do listy
        max_coord.append(point)

print(f"Liczba punktów: {counter}\nNajwiększa odległość: {round(max_dist, 2)}\nWspółrzędne punktów:")
with open("wyniki5.txt", "a", encoding="UTF-8") as out:
    out.write("5.2:\n")
    out.write(f"Liczba punktów: {counter}\nNajwiększa odległość: {round(max_dist, 2)}\nWspółrzędne punktów:\n")
    for max_point in max_coord:
        print(max_point[0], max_point[1])
        out.write(f"{max_point[0]} {max_point[1]}\n")