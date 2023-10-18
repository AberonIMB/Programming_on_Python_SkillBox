l = input().split()
s = set(l)
if len(s) == 1:
    print("Все числа равны")
elif len(s) == len(l):
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")