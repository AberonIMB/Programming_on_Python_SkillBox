line = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter = line[0]
number = int(line[3:]) % 26

for i in range(26):
    if alphabet[i] == letter:
        if i + number > 25:
            print(alphabet[i + number - 26])
        elif i + number < 0:
            print(alphabet[26 + (i + number)])
        else:
            print(alphabet[i + number])