line = input()
flag = False
numbers = ''

for i in range (len(line)):
    if line[i] == ' ':
        continue
    if line[i] not in numbers:
        numbers += line[i]
    elif line[i] in numbers:
        flag = True
        break
print(flag)