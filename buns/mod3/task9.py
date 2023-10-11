def s(pos, direction):
    return tuple(map(sum, zip(pos, direction)))


def do_magic_calculations(direction1, direction2, position, count, array, c_state, state):
    if s(position, direction1) not in array:
        position = s(position, direction1)
        array.append(position)
        count -= 1
        c_state = state
    else:
        position = s(position, direction2)
        array.append(position)
        count -= 1
    return position, count, array, c_state


n = int(input())
k = n
positions = [(0, 0), (-1, 0)]
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
current_state = 'Down'
pos = (-1, 0)

while n != 0:
    if current_state == "Down":
        pos, n, positions, current_state = do_magic_calculations(directions[3], directions[1], pos, n, positions, current_state, "Right")
    elif current_state == "Right":
        pos, n, positions, current_state = do_magic_calculations(directions[2], directions[3], pos, n, positions, current_state, "Up")
    elif current_state == "Up":
        pos, n, positions, current_state = do_magic_calculations(directions[0], directions[2], pos, n, positions, current_state, "Left")
    elif current_state == "Left":
        pos, n, positions, current_state = do_magic_calculations(directions[1], directions[0], pos, n, positions, current_state, "Down")

print(f"{positions[k][0]} {positions[k][1]}")
