print("x", end="\t")
for i in range(1, 11):
    print(i, end="\t")
print()
x = 1
for i in range(1, 11):
    if i == x:
        print(x, end="\t")
    x += 1
    for j in range(1, 11):
        print(i * j, end="\t")
    print()
