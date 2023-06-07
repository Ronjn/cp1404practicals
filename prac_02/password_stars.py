pwd = input("Enter password: ")
i = len(pwd)
while i < 6:
    print("Password needs to be a minimum of 6 characters")
    pwd = input("Enter password: ")
    i = len(pwd)

print("Password is: ", end='')

for j in range(0, i, 1):
    print("*", end='')
print()
