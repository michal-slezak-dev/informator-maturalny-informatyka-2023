import string
with open("instrukcje.txt", "r") as file:
    instructions = []

    for line in file:
        instructions.append(line.split())
# print(instructions)

letters = list(string.ascii_uppercase)
letters.append("A")
# print(letters)
changed = dict()

for i in range(1, len(letters)):
    changed[letters[i - 1]] = letters[i]
# print(changed)

stringList = []
for instruction in instructions:
    if instruction[0] == "DOPISZ":
        stringList.append(instruction[1])
    elif instruction[0] == "ZMIEN":
        stringList[-1] = instruction[1]
    elif instruction[0] == "USUN":
        stringList.pop(-1)
    elif instruction[0] == "PRZESUN":
        if instruction[1] in stringList:
            for i in stringList:
                if i == instruction[1]:
                    i = changed[i]
                    break
print(len(stringList))