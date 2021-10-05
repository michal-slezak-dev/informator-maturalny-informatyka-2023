with open("dane1_4.txt", "r") as file:
    ciag = [int(line.strip()) for line in file]


max_suma = min(ciag)

for i in range(len(ciag)):
    for j in range(i + 1, len(ciag)):
        suma = sum(ciag[i:j + 1])

        if suma > max_suma:
            max_suma = suma
            segment = (i + 1, j + 1)

print(segment)

# STRASZNIE DŁUGO TRWA!!! ;-(