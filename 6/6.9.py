import datetime

x = datetime.datetime.now()
rok = int(input("Podaj rok: "))
miesiac = int(input("Podaj miesiac: "))
dzien = int(input("Podaj dzien: "))
if miesiac < x.month:
    wiek = x.year - rok
elif miesiac > x.month:
    wiek = x.year - rok - 1
else:
    if dzien <= x.day:
        wiek = x.year - rok
    else:
        wiek = x.year - rok - 1
if wiek == 1:
    print("Masz", wiek, "rok")
elif 2 <= wiek <= 4:
    print("Masz", wiek, "lata")
else:
    print("Masz", wiek, "lat")