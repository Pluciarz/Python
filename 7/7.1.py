slowo = input("Podaj słowo: ")
print(slowo[3:])
print(slowo[3], slowo[6])
print(slowo[:3])
dlugosc = len(slowo)
srodek = dlugosc // 2
print(slowo[srodek - 1:srodek + 2])