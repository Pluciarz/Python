import datetime

x = datetime.datetime.now()

print("Do końca roku pozostało tygodni:", 52 - int(x.strftime("%W")))