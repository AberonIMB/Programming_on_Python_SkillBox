def make_dictionary(line):
    letter_count = {line[0]: 0}
    count = 0
    curr_letter = line[0]
    for char in line:
        if curr_letter == char:
            count += 1
        else:
            letter_count[curr_letter] = count
            curr_letter = char
            count = 1
    letter_count[curr_letter] = count
    return letter_count


line = sorted(input())
letter_count = make_dictionary(line)
odd_count = sum(value % 2 == 1 for value in letter_count.values())

answer = ''
if odd_count > 1:
    print("нельзя сделать палиндром")
else:
    for key, value in make_dictionary(line).items():
        if value % 2 == 0:
            answer = key * int(value / 2) + answer + key * int(value / 2)
        else:
            answer = key * (value // 2) + answer + key * (value // 2)
            answer = answer[:len(answer) // 2] + key + answer[len(answer) // 2:]
    print(answer)