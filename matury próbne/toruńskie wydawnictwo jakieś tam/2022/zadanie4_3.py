from string import ascii_uppercase

with open("wykreslanka.txt", "r") as file:
    strings = [list(line.strip()) for line in file]

alphabet = list(ascii_uppercase)
