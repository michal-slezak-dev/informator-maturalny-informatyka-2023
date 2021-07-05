def depth(bracket):
    countDepth = 0
    depths = []

    for br in bracket:
        if br == "[":
            countDepth += 1
        else:
            countDepth -= 1

        depths.append(countDepth)

    return max(depths)
with open("dane2_3.txt", "r") as file:
    brackets = []

    for line in file:
        brackets.append(line.strip())
# print(brackets)

out = []
for bracket in brackets:
    print(depth(bracket))
    out.append(depth(bracket))

with open("zadanie2_3.txt", "w", encoding="UTF-8") as output:
    output.write("ZADANIE 2.3\n")

    for element in out:
        output.write(f'{element} \n')