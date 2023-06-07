print("Enter name: ")
name = input()
MENU = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU)

choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello, " + name)
    elif choice == "G":
        print("Goodbye, " + name)
    else:
        print("Invalid input")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
