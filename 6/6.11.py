import datetime

x = datetime.datetime.now() - datetime.timedelta(1)

print(x.strftime("%A"))