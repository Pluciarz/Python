import datetime

x = datetime.datetime.now()
maj = datetime.datetime(2022, 5, 1)

print("Od 1 maja 2022 roku upłynęło", (x - maj).days, "dni")