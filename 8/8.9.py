import random

liczby = []
for i in range(0, 10):
    liczby.append(random.randint(10, 100))
for i in range(0, 10):
    for j in range(0, 10):
        if liczby[i] < liczby[j]:
            liczby[j], liczby[i] = liczby[i], liczby[j]
print (liczby)
for i in range(0, 10):
    for j in range(0, 10):
        if liczby[i] > liczby[j]:
            liczby[j], liczby[i] = liczby[i], liczby[j]
print (liczby)