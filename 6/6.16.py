import datetime

print("Ostatnia środa była:")
for i in range(0, 7):
    x = datetime.datetime.now() - datetime.timedelta(i)
    if x.strftime("%A") == "Wednesday":
        print(x.year, "-", x.month, "-", x.day)
        break