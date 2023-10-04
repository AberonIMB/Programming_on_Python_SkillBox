line = input()
chet = 0
nechet = 0
flag = False

while len(line) > 0:
    if flag:
        chet += int(line[0])
        flag = False
        line = line[1:]
    elif not(flag):
        nechet += int(line[0])
        flag = True
        line = line[1:]
if (chet * 3 + nechet) % 10 == 0:
    print('yes')
else:
    print('no')