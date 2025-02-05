def rozklad(x):
    i = 2
    while x > 1:
        if x % i == 0:
            print(i)
            x /= i
            i = 2
        else:
            i += 1
    return " "


x = int(input("Podaj liczbę: "))
print("Rozkład na czynniki pierwsze liczby", x, "to")
print(rozklad(x))