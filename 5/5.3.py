def potega(p, w):
    if w == 0:
        return 1
    return p * potega(p, w - 1)

p = int(input("Podaj podstawe potegi: "))
w = int(input("Podaj wykladnik potegi: "))
print("Potega liczby", p, "do potegi liczby", w, "wynosi", potega(p, w))