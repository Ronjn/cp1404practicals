
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """"Gets guitar entry from user and writes to guitars.csv"""
    guitars = read_file()

    print("\nEnter new guitar!")
    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitars.append(Guitar(name, year, cost))

        print(f"Guitar added.\n")

        name = input("Name: ")

    print("These are my guitars:")
    for guitar_index, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {guitar_index}: {guitar.name:>25} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")

    save_data(guitars)


def read_file():
    """Read file of guitar details, save as objects, display."""
    guitars = []
    # Open the file for reading
    in_file = open(FILENAME, 'r')
    # File format is like: Name,Year,Cost
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    # All other lines are guitar data
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # Construct a ProgrammingLanguage object using the elements
        # year should be an int
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        # Add the guitar we've just constructed to the list
        guitars.append(guitar)
    # Close the file as soon as we've finished reading it
    in_file.close()
    # Loop through and display all guitars (using their str method)
    for guitar in guitars:
        print(guitar)
    guitars.sort()
    print("------------------------------")
    # Loop through and display all guitars (using their str method)
    for guitar in guitars:
        print(guitar)

    return guitars


def save_data(guitars):
    """Saves data to file"""

    output_file = open(FILENAME, 'r+')  # Opens the file
    output_file.truncate(0)  # Deletes all file contents

    # For each guitar in guitars, adds the guitar to the file
    for guitar in guitars:
        line = f"{guitar.name},{guitar.year},{guitar.cost}\n"
        output_file.write(line)
    output_file.close()


main()

