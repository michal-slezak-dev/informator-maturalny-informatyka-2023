from string import ascii_lowercase

with open("wykreslanka.txt", "r") as file:
    rows = [list(line.strip()) for line in file]

columns_strings_list = [[] for _ in range(200)]
for row in rows:
    k = 0
    for i in range(200):
        columns_strings_list[i].append(row[k])
        k += 1

# zamieniamy listę list na listę napisów z kolumn
columns = [string_col for string_col in columns_strings_list]

alphabet = list(ascii_lowercase)
"""
1 x 26
26 x 1

2 x 13
13 x 2
"""

height = width = row = column = None

# sprawdzam 1 x 26
for i in range(100):
    for j in range(25, 200 - 25):
        if sorted(rows[i][j - 25:j + 1]) == alphabet:

            row = i
            column = j - 25

            height = 1
            width = 26

            print(f"Lewy górny róg (wiersz, kolumna): {i} {j - 25}\nwysokość: 1\nszerokość: 26")

# sprawdzam 26 x 1
for i in range(200):
    for j in range(25, 100 - 25):
        if sorted(columns[i][j - 25:j + 1]) == alphabet:

            row = j - 25
            column = i

            height = 26
            width = 1

            print(f"Lewy górny róg (wiersz, kolumna):  {j - 25} {i}\nwysokość: 26\nszerokość: 1")

# sprawdzam 2 x 13
for i in range(1, 100):
    for j in range(12, 200 - 12):
        sorted_row_1 = rows[i - 1][j - 12:j + 1]
        sorted_row_2 = rows[i][j - 12:j + 1]

        sorted_rows = sorted(sorted_row_1 + sorted_row_2)

        if sorted_rows == alphabet:

            row = i - 1
            column = j - 12

            height = 2
            width = 13

            print(f"Lewy górny róg (wiersz, kolumna):  {i - 1} {j - 12}\nwysokość: 2\nszerokość: 13")

# sprawdzam 13 x 2
for i in range(1, 200):
    for j in range(12, 100 - 12):
        sorted_col_1 = columns[i - 1][j - 12:j + 1]
        sorted_col_2 = columns[i][j - 12:j + 1]

        sorted_cols = sorted(sorted_col_1 + sorted_col_2)

        if sorted_cols == alphabet:

            row = j - 12
            column = i - 1

            height = 13
            width = 2

            print(f"Lewy górny róg (wiersz, kolumna): {j - 12} {i - 1}\nwysokość: 13\nszerokość: 2")

with open("zadanie4.txt", "a", encoding="UTF-8") as out:
    out.write("\nZADANIE 4.3:\n")
    out.write(f"wiersz: {row}\n")
    out.write(f"kolumna: {column}\n\n")
    out.write(f"wysokość: {height}\n")
    out.write(f"szerokość: {width}\n\n")