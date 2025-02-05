import random

x = random.randint(0, 9)
y = None
while x != y:
    y = int(input("Podaj cyfrę: "))
    if y < x:
        print("Za mało")
    if y > x:
        print("Za dużo")
    if y == x:
        print("Bingo!")