def find_longest_common(row):

    subsequence_streak = []  # przechowuje aktualne wartości countera jeśli znak ten sam
    subsequence_char = []  # przechowuje znaki jeśli takie same

    counter = 1  # zlicza liczbę takich samych znaków

    for i in range(1, len(row)):
        if row[i - 1] == row[i]:
            counter += 1
            longest_char = row[i - 1]
        else:
            counter = 1
            longest_char = ""

        subsequence_streak.append(counter)
        subsequence_char.append(longest_char)

    max_streak = max(subsequence_streak)  # długość najdłuższego spójnego podciągu
    max_char = subsequence_char[subsequence_streak.index(max_streak)]  # znak, któr

    return max_streak, max_char

with open("wykreslanka.txt", "r") as file:
    rows = [list(line.strip()) for line in file]

lengths = [find_longest_common(row)[0] for row in rows]  # długości najdłuższych spójnych podciągów
max_length = max(lengths)  # długość najdłuższego spójnego podciągu

print(f"Najdłuższy spójny podciąg składający się z takiego samego znaku ma długość: {max_length}")
print("\nCiągi o takiej długości są w wierszach o numerach:")
output = []
for i in range(100):
    longest_subsequence = find_longest_common(rows[i])
    if longest_subsequence[0] == max_length:
        print(f"{i}")  # ? dodajemy 1, bo indeksujemy od 0 ?
        output.append(i)

with open("zadanie4.txt", "a", encoding="UTF-8") as out:
    out.write("ZADANIE 4.2:\n")

    out.write(f"Najdłuższy spójny podciąg składający się z takiego samego znaku ma długość: {max_length}\n")
    out.write("\nCiągi o takiej długości są w wierszach o numerach:\n")

    for o in output:
        out.write(f"{o}\n")
