line = input()
index = line.find(',')
str = line[:index]
letter = line[index + 2:] #это если есть пробел после запятой
counter = 0

for i in range(len(str)):
    if str[i] == letter:
        counter += 1
    else:
        break
print(counter)