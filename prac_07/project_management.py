"""
Estimated time to complete  : 90 minutes
Actual time to complete     :  minutes
"""

from prac_07.project import Project

MENU = "\nMenu: \n" \
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
    projects = []

    while choice != "Q":
        if choice == "L":
            projects = load_projects()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
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


def display_projects(projects):
    """Displays list of incomplete and complete projects to user"""
    complete_projects = []
    incomplete_projects = []

    for project in projects:
        if project.is_complete():
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)

    print("Incomplete projects:")
    for incomplete_project in incomplete_projects:
        print(f"\t{incomplete_project}")

    print("\nComplete projects:")
    for complete_project in complete_projects:
        print(f"\t{complete_project}")



def load_projects():
    """Read file of projects, save as objects."""\

    file_name = "projects.txt"
    #file_name = input("Enter the file name to load from: ")

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


def save_projects(projects):
    """Saves data to file"""
    file_name = input("Enter the file name to save to: ")

    output_file = open(file_name, 'r+')  # Opens the file
    output_file.truncate(0)  # Deletes all file contents

    # For each project in projects, adds the project to the file
    for project in projects:
        line = f"{project.name}\t{project.date}\t{project.priority}\t{project.cost}\t{project.completion}\n"
        output_file.write(line)
    output_file.close()


main()

