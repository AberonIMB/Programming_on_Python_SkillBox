two_numbers = input()
first = 0
second = 0
counter = 0
for char in two_numbers:
    if char == ',':
        first = int(two_numbers[:counter])
        second = int(two_numbers[counter + 2:])
    counter += 1
print(first % second)
