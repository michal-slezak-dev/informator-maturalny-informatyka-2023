with open("dane_liczbowe.txt", "r") as file:
    nums = [[list(line.strip().split()[0]), line.strip().split()[1]] for line in file]

# lista krotek zawierających liczby n1 i n2, odejmujemy 1 (tak naprawdę to 2), bo indeksujemy od 0
# dla n2 nie dodajemy 1, bo też od 0 indeksujemy a k samo w sobie jest o 1 większe
new_nums = [(int(''.join(pair[0][:int(pair[1]) - 1])), int(''.join(pair[0][int(pair[1]):]))) for pair in nums]
max_n1, max_n2 = new_nums[0][0], new_nums[0][1]

# szukamy i wyłaniamy max dla n1 i n2
for new_pair in new_nums:
    if new_pair[0] > max_n1:
        max_n1 = new_pair[0]
    if new_pair[1] > max_n2:
        max_n2 = new_pair[1]

print(max_n1, max_n2)

with open("wynik4.txt", "a") as out:
    out.write("\n4.3:\n")
    out.write(f"{max_n1} {max_n2}")
