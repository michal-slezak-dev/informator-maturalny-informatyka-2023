with open('dane.txt', encoding='UTF-8') as file:
    pixels = []
    for line in file:
        pixels.append(line.split())

all_pixels = []

for line in pixels:
    for pixel in line:
        all_pixels.append(int(pixel))

print("Najjaśnieszy piksel to: {} \nNajciemniejszy piksel to: {}".format(max(all_pixels), min(all_pixels)))

with open('wyniki6.txt', "w", encoding='UTF-8') as output:
    output.write("6.1\n")
    output.write("Najjaśniejszy piksel to:" + str(max(all_pixels)) + "\n")
    output.write("Najciemniejszy piksel to:" + str(min(all_pixels)) + "\n\n")