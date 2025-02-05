def NWW(a, b):
    apom = a
    bpom = b
    while a != b:
        if a < b:
            a += apom
        else:
            b += bpom
    return a

a = int(input("Podaj liczbę: "))
b = int(input("Podaj liczbę: "))
print("NWW(", a, ",", b, ") =", NWW(a, b))