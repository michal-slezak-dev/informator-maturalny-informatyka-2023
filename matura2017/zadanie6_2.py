with open('dane.txt', encoding='UTF-8') as file:
    pixels = []
    for line in file:
        pixels.append(line.split())

# p = [1, 2, 3, 4, 4, 3, 2, 1]
#
# for i in range(len(p)):
#     print(f'{i} {len(p) - i - 1}')

how_many = 0
for line in pixels:
    for i in range(len(line)):
        # print(f'Sprawdzam {i} z {len(line) - i}')
        if line[i] != line[len(line) - i - 1]:
            how_many += 1
            break
print(how_many)

with open('wyniki6.txt', "a", encoding='UTF-8') as out:
    out.write("6.2\n")
    out.write("Liczba takich wierzy wynosi: " + str(how_many) + "\n\n")