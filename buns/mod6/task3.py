def get_generator():
    num = 152
    while True:
        result = sum(int(x) ** len(str(num)) for x in str(num))
        if result == num:
            yield num
        num += 1

generator = get_generator()

def get_armstrong_numbers():
    return next(generator)

for i in range(8):
    print(get_armstrong_numbers(), end=' ')