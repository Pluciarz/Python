imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
login = (nazwisko[::-1][len(nazwisko) - 3:] + imie[len(imie) - 3:]).upper()
print("Wygenerowany login:", login)