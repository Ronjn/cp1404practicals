for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a)
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b)
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c)
stars = int(input("Enter number of stars: "))
for i in range(0, stars, 1):
    print("*", end='')
print()

# d)
starLines = int(input("Enter number of star lines: "))
for i in range(0, starLines):
    for j in range(0, i + 1):
        print("*", end='')
    print("")
print()
