def find_dot(str):
    index = 0
    for i in range(len(str)):
        if str[i] == '.':
            index = i
            break
    return index

line = input()
line = line[::-1]

while True:
    index = find_dot(line)
    if index != 0:
        print(line[:index][::-1])
        line = line[index + 1:]
    else:
        print(line[::-1])
        break