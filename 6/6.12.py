import datetime

for i in range(1, 8):
    x = datetime.datetime.now() + datetime.timedelta(i)
    print(x.year, "-", x.month, "-", x.day)