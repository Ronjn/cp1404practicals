"""
Estimated time to complete  : 45  minutes
Actual time to complete     : 60  minutes
"""

from prac_06.guitar import Guitar


def main():

    guitars = []
    count = 0

    print("My guitars!")
    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitars.append(Guitar(name, year, cost))

        print(f"{guitars[count]} added.\n")
        count += 1

        name = input("Name: ")

    print("These are my guitars:")
    for guitar_index, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {guitar_index}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()

