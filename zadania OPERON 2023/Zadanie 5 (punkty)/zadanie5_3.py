from math import gcd
from collections import defaultdict

with open("punkty.txt", "r") as file:
    coordinates = [(int(line.strip().split()[0]), int(line.strip().split()[1])) for line in file]

# generujemy wszystkie możliwe współczynniki kierunkowe, które mają punkty z pliku
a_s = [point[1]/point[0] for point in coordinates]

num_of_points = defaultdict(int)  # klucze to a, wartości to ilość punktów należących od prostej o danym a
for i in range(len(a_s)):
    if a_s[i] * coordinates[i][0] == coordinates[i][1]:
        num_of_points[a_s[i]] += 1

max_num_of_points = max(num_of_points.values())  # wyłaniamy największą ilość punktów należących do jednej prostej
for a in num_of_points:
    if num_of_points[a] == max_num_of_points:
        max_a = a  # wyłaniamy współczynnik kierunkowy prostej, do której należy najwięcej punktów z pliku

"""
Lista zawierająca punkty należące do prostej o danym a , do której należy najwięcej punktów.

1. sprawdzamy czy a (a = y/x) jest równe maksymalnemu a oraz czy współrzędne są dodatnie (tylko wtedy naturalne liczby),
2. sprawdzamy czy współrzędne punktu, który pozostał są liczbami względnie pierwszymi
"""
max_coord = [point for point in coordinates if point[1]/point[0] == max_a and point[0] > 0 < point[1]]
for max_point in max_coord:
    if gcd(max_point[0], max_point[1]) == 1:
        a_two_nums = max_point

print(f"Liczba punktów: {max_num_of_points}")
print(a_two_nums[0], a_two_nums[1])

with open("wyniki5.txt", "a", encoding="UTF-8") as out:
    out.write("\n5.3:\n")
    out.write(f"Liczba punktów: {max_num_of_points}\n")
    out.write(f"{a_two_nums[0]} {a_two_nums[1]}")