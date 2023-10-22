line = input()

with open(line, 'r', encoding='windows-1251') as file:
    text = file.read()

letter_count = {}
for char in text:
    if char.isalpha():
        letter_count[char] = letter_count.get(char, 0) + 1

letter_count = sorted(letter_count.items(), key=lambda x: x[1])
with open("output.txt", 'w') as file:
    for letter, count in letter_count:
        file.write(f"{letter}:{count} ")