n = int(input("Ile jest uczniów w klasie: "))
uczniowie = []
for i in range (1, n + 1):
    imie = input("Podaj imię ucznia: ")
    uczniowie.append(imie)
unikalne_imiona = set(uczniowie)
print("Ilość różnych imion:", len(unikalne_imiona))
ilosc_chlopakow = 0
for uczen in uczniowie:
    print(uczen, uczniowie.count(uczen))
    if not uczen.endswith("a"):
        ilosc_chlopakow += 1
print("Ilość chłopaków w klasie:", ilosc_chlopakow)