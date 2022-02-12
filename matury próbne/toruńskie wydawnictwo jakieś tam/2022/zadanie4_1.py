with open("wykreslanka.txt", "r") as file:
    strings = [list(line.strip()) for line in file]

# wiersze
rows = [i for i in range(100) if "matura" in "".join(strings[i])]

# kolumny
columns_strings_list = [[] for _ in range(200)]

"""
k odpowiada za kolejne znaki z danego wiersza
pętla for i in range odpowiada za dodawanie do właściwej kolumny
za każdym obrotem pętli i dodajemy do i-tej kolumny k-ty znak z wiersza i zwiększamy k o 1 
ogólniee to za każdym razem dla każdego wiersza dodawać będzie np.:
a a a 
b b b
c c c

a a a
[[a], [a], [a]]

b b b
[[a, b], [a, b], [a,b]]

c c c
[[a, b, c], [a, b ,c], [a, b, c]]
"""
for string in strings:
    k = 0
    for i in range(200):
        columns_strings_list[i].append(string[k])
        k += 1

# zamieniamy listę list na listę napisów z kolumn
columns_strings = ["".join(string_col) for string_col in columns_strings_list]

# kolumny, w których występuje spójny ciąg "matura"
columns = [i for i in range(200) if "matura" in "".join(columns_strings[i])]

print(f"Wiersze: {list(map(lambda x: x + 1,rows))}")
print(f"Kolumny: {list(map(lambda x: x + 1,columns))}")