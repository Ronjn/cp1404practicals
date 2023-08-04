def main():
    i = get_password()
    while i < 6:
        print("Password needs to be a minimum of 6 characters")
        i = get_password()
    print("Password is: ", end='')
    print_asterisk(i)


def print_asterisk(i):
    for j in range(0, i, 1):
        print("*", end='')
    print()


def get_password():
    pwd = input("Enter password: ")
    i = len(pwd)
    return i


main()





