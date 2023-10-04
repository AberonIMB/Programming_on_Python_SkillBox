def find_spaces(str): #я просто не знаю можно ли использовать count
    counter = 0
    for i in range(len(str)):
        if str[i] == ' ':
            counter += 1
    return counter


line = input()
answer = ''
count = 0
for i in range(len(line)):
    if count == find_spaces(line):
        break
    if line[i + 1] == ' ':
        answer += line[i]
        count += 1
answer += line[-1]
print(answer)