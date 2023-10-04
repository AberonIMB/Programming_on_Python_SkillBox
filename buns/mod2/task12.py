line = input()

chars = '-() '
answer = ''

for char in line:
    if char not in chars:
        answer += char
print(answer)