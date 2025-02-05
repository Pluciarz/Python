def NWD(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

a = int(input("Podaj liczbę: "))
b = int(input("Podaj liczbę: "))
print("NWD(", a, ",", b, ") =", NWD(a, b))