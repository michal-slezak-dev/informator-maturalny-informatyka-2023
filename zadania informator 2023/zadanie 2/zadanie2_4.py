def is_correct(bracket):
    openingBracket = 0
    closingBracket = 0

    if bracket == "":
        return True
    else:
        for br in bracket:
            if br == "[":
                openingBracket += 1
            else:
                closingBracket += 1

        if openingBracket == closingBracket:
            return True
    return False

with open("dane2_4.txt", "r") as file:
    brackets = []

    for line in file:
        brackets.append(line.strip())
# print(brackets)
with open("zadanie2_4.txt", "w", encoding='UTF-8') as output:
    output.write("ZADANIE 2.4\n")

    for bracket in brackets:
        if is_correct(bracket):
            print("tak")
            output.write("tak\n")
        else:
            print("nie")
            output.write("nie\n")