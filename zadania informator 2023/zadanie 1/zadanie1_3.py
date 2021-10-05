with open("dane1_3.txt", "r") as file:
    ciag = [int(line.strip()) for line in file]


max_suma = min(ciag)

for i in range(len(ciag)):
    for j in range(i + 1, len(ciag)):
        # Tutaj sumujemy fragmenty danego segmentu (0 | 1 /|/ 0 | 2 /|/ 0 | 3 itd,)
        suma = sum(ciag[i:j + 1])

        # Sprawdzamy czy suma elementow danego segmentu jest większa od max_suma, jeśli tak to przypisujemu max_suma wartość suma
        if suma > max_suma:
            max_suma = suma

print(max_suma)

# Zapis do pliku
with open("zadanie1_3.txt", "w", encoding="UTF-8") as output:
    output.write(f'1.3:\n')
    output.write(str(max_suma))