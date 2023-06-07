"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def celcius_to_fahrenheit():
    global celsius
    celsius = 5 / 9 * (fahrenheit - 32)


def fahrenheit_to_celcius():
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit_to_celcius()
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        fahrenheit = float(input("Fahrenheit: "))
        celcius_to_fahrenheit()
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")