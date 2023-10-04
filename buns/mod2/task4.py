def change_number(num1, num2, num3):
    answer1 = ""
    answer2 = ""
    answer3 = ""
    hex_chars = "0123456789ABCDEF"
    while num1 > 0:
        remainder = num1 % 2
        answer1 = str(remainder) + answer1
        num1 //= 2
    while num2 > 0:
        remainder = num2 % 8
        answer2 = str(remainder) + answer2
        num2 //= 8
    while num3 > 0:
        remainder = num3 % 16
        hex_digit = hex_chars[remainder]
        answer3 = hex_digit + answer3
        num3 //= 16
    return (f"{answer1}, {answer2}, {answer3}")

number = input()

if (float(number) != round(float(number))) or int(number) <= 0:
    print("Неверный ввод")
else:
    print(change_number(int(number), int(number), int(number)))