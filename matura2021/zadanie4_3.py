with open("instrukcje.txt", "r") as file:
    instructions = []

    for line in file:
        if line.split()[0] == "DOPISZ":
            instructions.append(line.split())

only_letters = []

for instruction in instructions:
    only_letters.append(instruction[1])

dominant_letter = dict()

for letter in only_letters:
    dominant_letter.update({letter: only_letters.count(letter)})

maxAmount = max(dominant_letter.values())

for letter in dominant_letter:
    if dominant_letter[letter] == maxAmount:
        maxLetter = letter

print(maxLetter, " ", maxAmount)