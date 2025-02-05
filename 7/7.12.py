import random

imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
login = (imie[:3] + nazwisko[:3] + str(random.randint(1, 99))).lower()
print("Wygenerowany login:", login)