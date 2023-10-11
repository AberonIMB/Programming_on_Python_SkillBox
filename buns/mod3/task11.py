def check_horizontal(field, char):
    for i in range(len(field)):
        if len(set(field[i])) == 1 and field[i][0] == char:
            return True

def check_vertical(field, char):
    flag = False
    for i in range(len(field)):
        for j in range(len(field)):
            if field[j][i] == char:
                flag = True
            else:
                flag = False
                break
        if flag:
            break
    return flag

def check_left_diagonal(field, char):
    flag = False
    for i in range(len(field)):
        if field[i][i] == char:
            flag = True
        else:
            flag = False
            break
    return flag

def check_right_diagonal(field, char):
    flag = False
    for i in range(len(field)):
        if field[i][len(field) - 1 - i] == char:
            flag = True
        else:
            flag = False
            break
    return flag

s = input()
k = len(s)
field = []
field.append(s)

while k - 1 != 0:
    k -= 1
    field.append(input())

if (check_horizontal(field, 'X') or check_vertical(field, 'X') or check_left_diagonal(field, 'X') or check_right_diagonal(field, 'X')) and not (check_horizontal(field, 'O') or check_vertical(field, 'O') or check_left_diagonal(field, 'O') or check_right_diagonal(field, 'O')):
    print('X')
elif (check_horizontal(field, 'O') or check_vertical(field, 'O') or check_left_diagonal(field, 'O') or check_right_diagonal(field, 'O')) and not (check_horizontal(field, 'X') or check_vertical(field, 'X') or check_left_diagonal(field, 'X') or check_right_diagonal(field, 'X')):
    print('O')
else:
    print("Ничья")