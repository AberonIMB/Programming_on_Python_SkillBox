line = input()
counter_a = 0
counter_b = 0
vowels = "уеэоаыяиюё"
consonants = "йцкнгшщзхъждлрпвфчсмтьб"

for char in line:
    if char in vowels:
        counter_a += 1
    elif char in consonants:
        counter_b += 1
print(f"{counter_a} {counter_b}")