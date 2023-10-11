s = int(input())

for i in range(s):
    for j in range(1, s + 1):
        if j == s:
            print(j)
        else:
            print(j, end=', ')
print()

for i in range(1, s + 1):
    for j in range(s):
        if j == s - 1:
            print(i)
        else:
            print(i, end=', ')