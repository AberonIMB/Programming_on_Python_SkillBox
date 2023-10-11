s = input()
print(f"{bin(int(s))[2:]}, {oct(int(s))[2:]}, {hex(int(s))[2:]}" if s.isdigit() else "Неверный ввод")