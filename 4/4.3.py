suma = 0
ilosc = 0
for i in range (1, 100 + 1):
    if i % 25 == 0:
        suma += i
        ilosc += 1
        print(i)
print("Suma:", suma)
print("Ilość:", ilosc)