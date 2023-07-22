"""
Estimated time to complete  : 90 minutes
Actual time to complete     :  minutes
"""

from prac_07.project import Project

MENU = "Menu: \n" \
       "L - Load projects\n" \
       "S - Save projects\n" \
       "D - Display projects\n" \
       "F - Filter projects by date\n" \
       "A - Add new project\n" \
       "U - Update project\n" \
       "Q - Quit\n"


def main():
    print("Project Manager 1.0 - by Bryn Baird")
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            load_projects()
        elif choice == "S":
            save_projects()
        elif choice == "D":
            print(f"Choice is {choice}")
        elif choice == "F":
            print(f"Choice is {choice}")
        elif choice == "A":
            print(f"Choice is {choice}")
        elif choice == "U":
            print(f"Choice is {choice}")
        else:
            print("Invalid menu selection")
        print(MENU)
        choice = input(">>> ").upper()


def load_projects():
    """Read file of projects, save as objects."""\

    file_name = input("Enter the file name to load from: ")

    projects = []
    # Open the file for reading
    in_file = open(file_name, 'r')
    # File format is like: Name    Start Date  Priority    Cost Estimate   Completion Percentage
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    # All other lines are project data
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split('\t')
        # Construct a Project object using the elements
        # year should be an int
        project = Project(parts[0], (parts[1]), int(parts[2]), float(parts[3]), int(parts[4]))
        # Add the project we've just constructed to the list
        projects.append(project)
    # Close the file as soon as we've finished reading it
    in_file.close()
    # Loop through and display all projects (using their str method)
    for project in projects:
        print(project)

    return projects


def save_projects():
    file_name = input("Enter the file name to save to: ")


main()

