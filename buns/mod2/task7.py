line = input()
count_0 = 0
count_1 = 0

for char in line:
    if char == '0':
        count_0 += 1
    elif char == '1':
        count_1 += 1
if count_1 == count_0:
    print('yes')
else:
    print('no')