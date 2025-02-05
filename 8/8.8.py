n = int(input("Podaj resztę do wydania: "))
nominaly = [1, 2, 5, 10, 20]
licznik = 0
historia = []
while n > 0:
    nominal = 0
    for i in range(0, len(nominaly)):
        if nominaly[i] <= n and nominaly[i] > nominal:
            nominal = nominaly[i]
    n = n - nominal
    licznik += 1
    historia.append(nominal)
print("Resztę można wydać", licznik, "nominałami")
print("Użyte nominały:")
for i in range (0, licznik):
    print(historia[i], "zł")
