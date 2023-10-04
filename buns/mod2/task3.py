numbers = input()
a = 0
b = 0
c = 0
len_a = 0 # раз нельзя через split, то придется писать такую боль
len_b = 0
space_counter = 0
for char in numbers:
    if char == ' ':
        space_counter += 1
    if space_counter == 0:
        len_a += 1
    elif space_counter == 1:
        len_b += 1
a = int(numbers[:len_a])
b = int(numbers[len_a + 1: len_a + len_b])
c = int(numbers[len_b + len_a + 1:])
if (a <= b <= c) or (a >= b >= c):
    print(b)
elif (b <= a <= c) or (b >= a >= c):
    print(a)
else:
    print(c)