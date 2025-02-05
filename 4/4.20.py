def potega(p, w):
    wynik = 1
    if w > 0:
        while w > 0:
            wynik *= p
            w -= 1
    elif w < 0:
        while w < 0:
            wynik *= 1 / p
            w += 1
    return wynik

p = int(input("Podaj podstawę: "))
w = int(input("Podaj wykładnik: "))
print(p, "do potęgi", w, "wynosi", potega(p,w))