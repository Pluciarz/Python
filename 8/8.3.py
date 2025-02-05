import random

rzuty = []
for i in range (0, 100):
    rzuty.append(random.randint(1, 6))
for i in range(1, 7):
    print("Liczbę", i, "wylosowano", rzuty.count(i))